#!/usr/bin/env python3
"""Persistent PDF/content comparison for the Ordering Guru guide mirror.

A catalog disappearance is discovery-only until two live catalog checks also
receive 404/410 from the old PDF. An unavailable catalog never retires guides.
Text changes are review candidates, not automatic claims of material changes.
"""
from __future__ import annotations

import csv
import difflib
import hashlib
import json
import re
import tempfile
import time
import unicodedata
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urlparse

import requests

from convert_ordering_guides_to_markdown import convert_one
from discover_ordering_guides import (
    ALLOWED_PDF_HOSTS, HEADERS, discover_guides,
)

SCHEMA_VERSION = 1
MAX_PDF_BYTES = 40 * 1024 * 1024
SKU_PATTERN = re.compile(r"\b(?:FC\d*|FG|FS|FAP|FWF|FEX|FAC|FML|FAZ|FMG|FSA|FNAC|FPC|FVE|FADC|FPX|FDC|FDD|FND)-[A-Z0-9][A-Z0-9*-]*(?:\b|(?<=\*))")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def normalize(text: str) -> str:
    # Preserve words, numbers, table cells, and ordering rules. Ignore only
    # Unicode/whitespace differences. Semantic materiality is reviewed later.
    text = re.sub(r"^# [^\n]*\n", "", text, count=1)
    return " ".join(unicodedata.normalize("NFKC", text).split())


def safe_path(root: Path, relative: str) -> Path:
    candidate = (root / relative).resolve()
    if not candidate.is_relative_to(root.resolve()):
        raise ValueError(f"Guide path escapes output directory: {relative}")
    return candidate


def read_csv(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


def write_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    temporary.replace(path)


def seed_baseline(root: Path) -> dict:
    """Use already mirrored Markdown as the initial text baseline, not an alert."""
    guides = {}
    manifest = root / "manifest.csv"
    if manifest.exists():
        for row in read_csv(manifest):
            relative = str(Path(row["local_path"]).with_suffix(".md"))
            path = safe_path(root, relative)
            if not path.exists():
                continue
            body = path.read_text(encoding="utf-8")
            key = Path(urlparse(row["url"]).path).stem
            guides[key] = {
                "guide_key": key, "title": row["title"], "category": row["category"],
                "url": row["url"], "local_path": relative,
                "text_sha256": digest(normalize(body).encode()),
                "pdf_sha256": None, "file_size": None, "checked_at": None,
                "document_date": document_date(body), "status": "legacy_text_baseline",
                "missing_checks": 0,
            }
    return {"schema_version": SCHEMA_VERSION, "initialized": bool(guides), "guides": guides}


def document_date(body: str) -> str | None:
    # Fortinet footers commonly carry YYYYMMDD or Month DD, YYYY.
    matches = re.findall(r"\b20\d{2}[01]\d[0-3]\d\b|\b(?:January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2},? 20\d{2}\b", body)
    return matches[-1] if matches else None


def download_pdf(url: str) -> tuple[bytes | None, int]:
    """Fetch fresh bytes, validating redirects, size, and PDF signature."""
    last_error = None
    for attempt in range(3):
        try:
            current = url
            for _ in range(6):
                parsed = urlparse(current)
                if parsed.scheme != "https" or parsed.hostname not in ALLOWED_PDF_HOSTS:
                    raise ValueError(f"PDF URL outside official hosts: {current}")
                with requests.get(current, headers={**HEADERS, "Cache-Control": "no-cache"},
                                  timeout=(10, 30), stream=True, allow_redirects=False) as response:
                    if response.is_redirect:
                        from urllib.parse import urljoin
                        current = urljoin(current, response.headers["Location"])
                        continue
                    if response.status_code in (404, 410):
                        return None, response.status_code
                    response.raise_for_status()
                    chunks, size = [], 0
                    for chunk in response.iter_content(65536):
                        size += len(chunk)
                        if size > MAX_PDF_BYTES:
                            raise ValueError("PDF exceeds size limit")
                        chunks.append(chunk)
                    data = b"".join(chunks)
                    if not data.startswith(b"%PDF-"):
                        raise ValueError("Response is not a PDF")
                    return data, response.status_code
            raise ValueError("Too many PDF redirects")
        except requests.RequestException as error:
            last_error = error
            if attempt < 2:
                time.sleep(attempt + 1)
    raise RuntimeError(f"PDF download failed: {last_error}")


def read_document(data: bytes, filename: str) -> str:
    with tempfile.TemporaryDirectory() as temp:
        pdf_path = Path(temp) / filename
        md_path = pdf_path.with_suffix(".md")
        pdf_path.write_bytes(data)
        status, detail = convert_one(str(pdf_path), str(md_path))
        if status != "converted":
            raise RuntimeError(f"PDF conversion failed: {detail}")
        body = md_path.read_text(encoding="utf-8")
        if not normalize(body):
            raise RuntimeError("PDF has no extractable content")
        return body


def baseline_text(root: Path, old: dict) -> str:
    """Recover prior content after an interrupted run wrote newer Markdown."""
    path = safe_path(root, old["local_path"])
    body = path.read_text(encoding="utf-8") if path.exists() else ""
    if digest(normalize(body).encode()) != old["text_sha256"]:
        snapshot = root / "changes" / "snapshots" / f"{old['text_sha256']}.md"
        body = snapshot.read_text(encoding="utf-8")
        if digest(normalize(body).encode()) != old["text_sha256"]:
            raise ValueError("Previous text baseline is inconsistent; comparison withheld")
    return body


def change_evidence(before: str, after: str) -> dict:
    old_skus, new_skus = set(SKU_PATTERN.findall(before)), set(SKU_PATTERN.findall(after))
    # Comparing normalized text lines avoids layout/line-wrap-only changes.
    old_lines = [normalize(line) for line in before.splitlines() if normalize(line)]
    new_lines = [normalize(line) for line in after.splitlines() if normalize(line)]
    patch = "\n".join(difflib.unified_diff(old_lines, new_lines, fromfile="previous", tofile="current", lineterm="")) + "\n"
    return {"added_skus": sorted(new_skus - old_skus),
            "removed_skus": sorted(old_skus - new_skus), "diff": patch}


def entry_event(kind: str, guide: dict, detail: str, **extra) -> dict:
    return {"kind": kind, "guide_key": guide["guide_key"], "title": guide["title"],
            "url": guide["url"], "local_path": guide["local_path"], "detail": detail, **extra}


def update_guides(root: Path, baseline: dict, catalog: list[dict], live: bool,
                  checked_at: str, fetch=download_pdf, extract=read_document) -> tuple[dict, dict]:
    """Update only successfully verified guides; preserve failed guide baselines."""
    # Copy so callers can retain the previous state for review/tests.
    previous = baseline["guides"]
    current = json.loads(json.dumps(previous))
    report = {"schema_version": SCHEMA_VERSION, "checked_at": checked_at,
              "discovery_verified": live, "qualifying_changes": [],
              "content_review_candidates": [], "discovery_only": [],
              "binary_only": [], "unverified": [], "baseline_initialized": []}
    seen = set()
    catalog_keys = {Path(item["filename"]).stem for item in catalog}
    for item in catalog:
        key = Path(item["filename"]).stem
        old_key = key
        old = previous.get(key)
        if old is None:
            matches = [k for k, g in previous.items()
                       if g["title"].casefold() == item["title"].casefold() and k not in seen]
            if len(matches) == 1:
                old_key, old = matches[0], previous[matches[0]]
        seen.add(old_key)
        relative = str(Path(item["category"]) / Path(item["filename"]).with_suffix(".md"))
        guide = {"guide_key": key, "title": item["title"], "category": item["category"],
                 "url": item["url"], "local_path": relative}
        try:
            destination = safe_path(root, relative)
            if Path(item["filename"]).name != item["filename"]:
                raise ValueError("Invalid PDF filename")
            data, status = fetch(item["url"])
            if data is None:
                raise RuntimeError(f"HTTP {status}; catalog still lists this PDF")
            pdf_hash = digest(data)
            before = baseline_text(root, old) if old else ""
            # Always extract when binary bytes change. A missing local copy is
            # an error above, never mistaken for a newly added guide.
            after = before if old and old.get("pdf_sha256") == pdf_hash else extract(data, item["filename"])
            text_hash = digest(normalize(after).encode())
            if old is None:
                # A renamed title AND filename can still be the same guide.
                # Match only a unique identical-content guide no longer listed;
                # never collapse two simultaneously catalogued products.
                matches = [k for k, value in previous.items()
                           if k not in catalog_keys and k not in seen
                           and value["text_sha256"] == text_hash]
                if len(matches) == 1:
                    old_key, old = matches[0], previous[matches[0]]
                    before = baseline_text(root, old)
                    seen.add(old_key)
            guide.update(pdf_sha256=pdf_hash, text_sha256=text_hash, file_size=len(data),
                         checked_at=checked_at, document_date=document_date(after),
                         status="verified", missing_checks=0)
            if old is None and not baseline.get("initialized", bool(previous)):
                report["baseline_initialized"].append(key)
            elif old is None or old.get("status") == "removed":
                report["qualifying_changes"].append(entry_event("added", guide,
                    "New catalog guide; PDF downloaded and text verified.",
                    inventory_impact="Add guide to inventory.", lookup_impact="New product lookup source available."))
            elif old["text_sha256"] != text_hash:
                # Preserve the previous source before replacing its mirror. If
                # a job is interrupted before committing the new baseline,
                # the next run can still reconstruct the correct comparison.
                snapshot = root / "changes" / "snapshots" / f"{old['text_sha256']}.md"
                snapshot.parent.mkdir(parents=True, exist_ok=True)
                snapshot.write_text(before, encoding="utf-8")
                evidence = change_evidence(before, after)
                diff_name = f"changes/diffs/{checked_at.replace(':', '').replace('+', '_')}/{key}.diff"
                patch = evidence.pop("diff")
                diff_path = safe_path(root, diff_name)
                diff_path.parent.mkdir(parents=True, exist_ok=True)
                diff_path.write_text(patch, encoding="utf-8")
                report["content_review_candidates"].append(entry_event(
                    "replaced" if old["url"] != guide["url"] or old_key != key else "content_changed",
                    guide, "Extracted content changed; review diff for material ordering impact before notifying.",
                    previous_url=old["url"], previous_pdf_sha256=old.get("pdf_sha256"),
                    pdf_sha256=pdf_hash, diff_path=diff_name,
                    inventory_impact="Mirrored text refreshed; review guide identity if replaced.",
                    lookup_impact="Review model, SKU, bundle, licensing, and ordering-rule differences.",
                    **evidence))
            else:
                if any(old.get(field) != guide[field] for field in ("url", "title", "category", "local_path")) or old_key != key:
                    report["discovery_only"].append(entry_event("catalog_changed", guide, "Catalog identity/location changed; guide content unchanged."))
                if old.get("pdf_sha256") is None:
                    report["baseline_initialized"].append(key)
                elif old["pdf_sha256"] != pdf_hash:
                    report["binary_only"].append(entry_event("binary_changed", guide, "PDF bytes changed; extracted content unchanged."))
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(after, encoding="utf-8")
            current.pop(old_key, None)
            current[key] = guide
        except (requests.RequestException, RuntimeError, ValueError, OSError) as error:
            report["unverified"].append(entry_event("verification_failed", guide, str(error)))
            # Reset a prior missing streak because the catalog now lists it.
            if old_key in current:
                current[old_key]["missing_checks"] = 0
        print(f"Checked {item['title']}", flush=True)
    for key, old in previous.items():
        if key in seen or old.get("status") == "removed":
            continue
        if not live:
            continue  # A failed/partial discovery can never confirm removal.
        try:
            data, status = fetch(old["url"])
            if data is not None:
                # Keep checking PDF revisions even if only the catalog link
                # disappears. Reuse fetched bytes rather than download twice.
                item = {"title": old["title"], "category": old["category"],
                        "url": old["url"], "filename": Path(urlparse(old["url"]).path).name}
                verified, findings = update_guides(root,
                    {"guides": {key: old}, "initialized": True}, [item], False,
                    checked_at, fetch=lambda url: (data, status), extract=extract)
                current.update(verified["guides"])
                for section in ("content_review_candidates", "binary_only", "unverified", "baseline_initialized"):
                    report[section].extend(findings[section])
                report["discovery_only"].append(entry_event("catalog_absent", old, "Absent from catalog but official PDF still available; not a confirmed removal."))
            else:
                missing = old.get("missing_checks", 0) + 1
                current[key]["missing_checks"] = missing
                if missing >= 2:
                    current[key]["status"] = "removed"
                    report["qualifying_changes"].append(entry_event("removed", old,
                        "Absent from two consecutive verified catalogs and official PDF returned 404/410 on both checks.",
                        inventory_impact="Mark guide retired; retain archived text for historical lookup.",
                        lookup_impact="Do not use retired guide as a current ordering source."))
                else:
                    report["unverified"].append(entry_event("removal_pending", old, f"Catalog absent and HTTP {status}; awaiting a second live check."))
        except (requests.RequestException, RuntimeError, ValueError, OSError) as error:
            current[key]["missing_checks"] = 0
            report["unverified"].append(entry_event("removal_unverified", old, str(error)))
    report["comparison_complete"] = live and not report["unverified"]
    return {"schema_version": SCHEMA_VERSION, "initialized": bool(current), "checked_at": checked_at, "guides": current}, report


def write_manifests(root: Path, baseline: dict, report: dict) -> None:
    rows = []
    failures = {item["guide_key"]: item for item in report["unverified"]}
    for key, guide in sorted(baseline["guides"].items()):
        failure = failures.get(key)
        rows.append({"category": guide["category"], "title": guide["title"],
                     "url": guide["url"], "local_path": guide["local_path"],
                     "status": "failed" if failure else guide["status"],
                     "detail": failure["detail"] if failure else "PDF/content baseline retained"})
    for key, failure in failures.items():
        if key not in baseline["guides"]:
            rows.append({"category": "", "title": failure["title"], "url": failure["url"],
                         "local_path": failure["local_path"], "status": "failed", "detail": failure["detail"]})
    with (root / "manifest.csv").open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=["category", "title", "url", "local_path", "status", "detail"], lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def run(root: Path) -> int:
    root.mkdir(parents=True, exist_ok=True)
    path = root / "guide_baseline.json"
    baseline = json.loads(path.read_text(encoding="utf-8")) if path.exists() else seed_baseline(root)
    if baseline.get("schema_version") != SCHEMA_VERSION:
        raise ValueError("Unsupported guide baseline version")
    checked_at = datetime.now(timezone.utc).isoformat(timespec="microseconds")
    error = None
    live = True
    try:
        discover_guides(str(root))
        catalog = read_csv(root / "discovered_guides.csv")
        # A large unexpected catalog shrink may be partial HTML. Keep known
        # PDFs and withhold removals, while still checking discovered additions.
        active = [g for g in baseline["guides"].values() if g.get("status") != "removed"]
        if active and len(catalog) < len(active) * 0.8:
            live = False
            error = "Catalog shrank by more than 20%; completeness unverified. Removals withheld."
    except (requests.RequestException, RuntimeError, ValueError, OSError) as exc:
        live, error, catalog = False, str(exc), []
    if not live:
        known = {Path(item["filename"]).stem for item in catalog}
        catalog.extend({"title": guide["title"], "category": guide["category"],
                        "url": guide["url"], "filename": Path(urlparse(guide["url"]).path).name}
                       for key, guide in baseline["guides"].items()
                       if key not in known and guide.get("status") != "removed")
    if not catalog:
        report = {"schema_version": SCHEMA_VERSION, "checked_at": checked_at,
                  "discovery_verified": False, "comparison_complete": False,
                  "discovery_error": error or "No guide inventory available", "qualifying_changes": [],
                  "content_review_candidates": [], "discovery_only": [], "binary_only": [], "unverified": []}
    else:
        # Bounded parallel network requests; comparison and writes stay serial.
        # All futures are resolved inside the executor's lifetime.
        with ThreadPoolExecutor(max_workers=4) as pool:
            futures = {item["url"]: pool.submit(download_pdf, item["url"]) for item in catalog}
            def fetch(url):
                return futures[url].result() if url in futures else download_pdf(url)
            baseline, report = update_guides(root, baseline, catalog, live, checked_at, fetch=fetch)
        report["discovery_error"] = error
        write_json(path, baseline)
        write_manifests(root, baseline, report)
    # Every check gets an immutable report, so a later quiet check cannot hide a
    # previous change from the weekly notification task.
    stamp = checked_at.replace(":", "").replace("+", "_")
    write_json(root / "changes" / f"{stamp}.json", report)
    write_json(root / "guide_changes.json", report)
    print(f"Guide check: {len(report['qualifying_changes'])} confirmed inventory changes, "
          f"{len(report['content_review_candidates'])} content review candidates.")
    return 0 if report["comparison_complete"] else 1


if __name__ == "__main__":
    import sys
    sys.exit(run(Path(sys.argv[1] if len(sys.argv) > 1 else "fortinet_ordering_guides").resolve()))
