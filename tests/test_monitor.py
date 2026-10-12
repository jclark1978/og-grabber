import copy
import csv
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import requests
import monitor_ordering_guides as monitor


class MonitorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.catalog = [{"title": "FortiGate", "category": "01. Unified OS",
                         "url": "https://www.fortinet.com/og-fortigate.pdf",
                         "filename": "og-fortigate.pdf"}]
        self.body = "# og-fortigate\n\nOrder FG-100F with UTP.\n"
        self.payload = b"%PDF-test-v1"
        self.baseline, _ = self.check({"guides": {}}, body=self.body)

    def check(self, baseline=None, catalog=None, payload=None, body=None, live=True, status=200):
        return monitor.update_guides(self.root, baseline or self.baseline,
            self.catalog if catalog is None else catalog, live, "2026-10-12T20:00:00+00:00",
            fetch=lambda url: (self.payload if payload is None else payload, status),
            extract=lambda data, filename: self.body if body is None else body)

    def test_initial_baseline_is_silent(self):
        _, report = self.check({"guides": {}}, payload=b"different")
        self.assertEqual(report["qualifying_changes"], [])
        self.assertEqual(report["baseline_initialized"], ["og-fortigate"])

    def test_same_url_replacement_with_same_size_detected(self):
        _, report = self.check(payload=b"%PDF-test-v2", body=self.body.replace("100F", "120G"))
        change = report["content_review_candidates"][0]
        self.assertEqual(change["kind"], "content_changed")
        self.assertEqual(change["added_skus"], ["FG-120G"])
        self.assertEqual(change["removed_skus"], ["FG-100F"])
        self.assertIn("FG-120G", (self.root / change["diff_path"]).read_text())

    def test_binary_metadata_and_whitespace_are_silent(self):
        _, report = self.check(payload=b"%PDF-metadata", body=self.body.replace(" with ", "\nwith   "))
        self.assertEqual(report["content_review_candidates"], [])
        self.assertEqual(len(report["binary_only"]), 1)

    def test_catalog_rename_and_url_change_same_content_are_silent(self):
        catalog = copy.deepcopy(self.catalog)
        catalog[0].update(title="Renamed", category="02. LAN", url="https://docs.fortinet.com/og-fortigate.pdf")
        _, report = self.check(catalog=catalog)
        self.assertEqual(len(report["discovery_only"]), 1)
        self.assertEqual(report["content_review_candidates"], [])

    def test_replaced_filename_matched_by_unique_title(self):
        catalog = copy.deepcopy(self.catalog)
        catalog[0].update(filename="og-new.pdf", url="https://www.fortinet.com/og-new.pdf")
        state, report = self.check(catalog=catalog, payload=b"%PDF-new", body=self.body.replace("UTP", "ATP"))
        self.assertNotIn("og-fortigate", state["guides"])
        self.assertEqual(report["content_review_candidates"][0]["kind"], "replaced")
        self.assertEqual(report["qualifying_changes"], [])

    def test_renamed_title_and_filename_identical_content_are_silent(self):
        catalog = [{**self.catalog[0], "title": "New name", "filename": "og-new.pdf",
                    "url": "https://www.fortinet.com/og-new.pdf"}]
        state, report = self.check(catalog=catalog)
        self.assertEqual(report["qualifying_changes"], [])
        self.assertEqual(len(report["discovery_only"]), 1)
        self.assertNotIn("og-fortigate", state["guides"])

    def test_added_pdf_is_confirmed(self):
        catalog = self.catalog + [{**self.catalog[0], "title": "Switch", "filename": "og-switch.pdf",
                                   "url": "https://www.fortinet.com/og-switch.pdf"}]
        _, report = self.check(catalog=catalog)
        self.assertEqual(report["qualifying_changes"][0]["kind"], "added")

    def test_failed_pdf_preserves_baseline_and_text(self):
        state, report = monitor.update_guides(self.root, self.baseline, self.catalog, True,
            "next", fetch=lambda url: (_ for _ in ()).throw(requests.HTTPError("403")))
        self.assertEqual(state["guides"], self.baseline["guides"])
        self.assertFalse(report["comparison_complete"])
        self.assertEqual(report["qualifying_changes"], [])
        self.assertEqual((self.root / "01. Unified OS/og-fortigate.md").read_text(), self.body)

    def test_catalog_absence_with_accessible_pdf_is_discovery_only(self):
        _, report = self.check(catalog=[])
        self.assertEqual(len(report["discovery_only"]), 1)
        self.assertEqual(report["qualifying_changes"], [])

    def test_catalog_absent_pdf_still_checked_for_content(self):
        _, report = self.check(catalog=[], payload=b"%PDF-changed", body=self.body.replace("UTP", "ATP"))
        self.assertEqual(len(report["content_review_candidates"]), 1)

    def test_removal_requires_two_live_checks(self):
        missing = lambda url: (None, 404)
        state, report = monitor.update_guides(self.root, self.baseline, [], True, "first", fetch=missing)
        self.assertEqual(report["qualifying_changes"], [])
        state, report = monitor.update_guides(self.root, state, [], True, "second", fetch=missing)
        self.assertEqual(report["qualifying_changes"][0]["kind"], "removed")
        self.assertTrue((self.root / "01. Unified OS/og-fortigate.md").exists())
        _, report = monitor.update_guides(self.root, state, [], True, "third", fetch=missing)
        self.assertEqual(report["qualifying_changes"], [])

    def test_removed_guide_can_return(self):
        state = copy.deepcopy(self.baseline)
        state["guides"]["og-fortigate"]["status"] = "removed"
        _, report = self.check(state)
        self.assertEqual(report["qualifying_changes"][0]["kind"], "added")

    def test_unverified_catalog_never_retires_guides(self):
        _, report = monitor.update_guides(self.root, self.baseline, [], False, "failed",
                                          fetch=lambda url: (None, 404))
        self.assertEqual(report["qualifying_changes"], [])
        self.assertFalse(report["comparison_complete"])

    def test_nonconsecutive_404_does_not_confirm_removal(self):
        missing = lambda url: (None, 404)
        state, _ = monitor.update_guides(self.root, self.baseline, [], True, "first", fetch=missing)
        state, _ = monitor.update_guides(self.root, state, [], True, "error",
                    fetch=lambda url: (_ for _ in ()).throw(requests.HTTPError("403")))
        _, report = monitor.update_guides(self.root, state, [], True, "second", fetch=missing)
        self.assertEqual(report["qualifying_changes"], [])

    def test_seed_uses_existing_markdown_without_fabricating_pdf_hash(self):
        with (self.root / "manifest.csv").open("w", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=["title", "category", "url", "local_path", "status"])
            writer.writeheader()
            writer.writerow({**{k: self.catalog[0][k] for k in ("title", "category", "url")},
                             "local_path": "01. Unified OS/og-fortigate.pdf", "status": "downloaded"})
        seed = monitor.seed_baseline(self.root)
        self.assertIsNone(seed["guides"]["og-fortigate"]["pdf_sha256"])
        _, report = self.check(seed)
        self.assertEqual(report["content_review_candidates"], [])
        self.assertEqual(report["qualifying_changes"], [])

    def test_interrupted_run_retains_correct_old_content_diff(self):
        self.check(payload=b"%PDF-v2", body=self.body.replace("100F", "120G"))
        # Pretend baseline persistence was interrupted after the text write.
        _, report = self.check(self.baseline, payload=b"%PDF-v2", body=self.body.replace("100F", "120G"))
        change = report["content_review_candidates"][0]
        self.assertEqual(change["removed_skus"], ["FG-100F"])
        self.assertEqual(change["added_skus"], ["FG-120G"])

    def test_paths_cannot_escape_root(self):
        catalog = [{**self.catalog[0], "category": "../../outside"}]
        _, report = self.check(catalog=catalog)
        self.assertEqual(len(report["unverified"]), 1)

    def test_discovery_failure_checks_known_guides_without_removing(self):
        monitor.write_json(self.root / "guide_baseline.json", self.baseline)
        with patch.object(monitor, "discover_guides", side_effect=requests.HTTPError("403")), \
             patch.object(monitor, "download_pdf", return_value=(self.payload, 200)):
            # Default dependency is bound at function definition; replace call's
            # fetch/extract through a wrapper to keep this a network-free test.
            original = monitor.update_guides
            with patch.object(monitor, "update_guides", side_effect=lambda *args, **kwargs: original(*args,
                 fetch=lambda url: (self.payload, 200), extract=lambda data, filename: self.body)):
                self.assertEqual(monitor.run(self.root), 1)
        report = json.loads((self.root / "guide_changes.json").read_text())
        self.assertFalse(report["discovery_verified"])
        self.assertEqual(report["qualifying_changes"], [])
        self.assertEqual(len(list((self.root / "changes").glob("*.json"))), 1)


class DownloadTests(unittest.TestCase):
    def test_html_response_is_rejected(self):
        response = unittest.mock.MagicMock()
        response.__enter__.return_value = response
        response.is_redirect = False
        response.status_code = 200
        response.iter_content.return_value = [b"<html>403</html>"]
        with patch.object(monitor.requests, "get", return_value=response):
            with self.assertRaisesRegex(ValueError, "not a PDF"):
                monitor.download_pdf("https://www.fortinet.com/og-test.pdf")

    def test_unofficial_redirect_is_rejected(self):
        response = unittest.mock.MagicMock()
        response.__enter__.return_value = response
        response.is_redirect = True
        response.headers = {"Location": "https://example.com/og-test.pdf"}
        with patch.object(monitor.requests, "get", return_value=response):
            with self.assertRaisesRegex(ValueError, "outside official"):
                monitor.download_pdf("https://www.fortinet.com/og-test.pdf")


if __name__ == "__main__":
    unittest.main()
