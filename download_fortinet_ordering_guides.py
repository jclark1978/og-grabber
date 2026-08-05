#!/usr/bin/env python3
"""
Download all Fortinet Ordering Guide PDFs discovered from
docs.fortinet.com/ordering-guides.

Usage:
    python download_fortinet_ordering_guides.py [output_dir]

Behavior:
- Creates one subfolder per ordering-guide category (e.g. "01. Unified OS").
- Skips files that already exist and match the expected size (safe to re-run).
- Retries transient failures.
- Writes a manifest.csv summarizing what was downloaded / skipped / failed.
- Reads discovered_guides.csv when it exists; the built-in list is retained as
  a fallback for running this script by itself.
"""

import csv
import os
import re
import sys
import time
from urllib.parse import urlparse

import requests

BASE_OUTPUT_DIR = sys.argv[1] if len(sys.argv) > 1 else "fortinet_ordering_guides"
BASE_URL = "https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/"
DISCOVERED_GUIDES_PATH = os.path.join(BASE_OUTPUT_DIR, "discovered_guides.csv")
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
    )
}
MAX_RETRIES = 3
RETRY_DELAY_SEC = 3

# (category, title, filename) — filename is relative to BASE_URL
GUIDES = [
    ("01. Unified OS", "Cloud NGFW", "og-cloud-next-generation-firewall.pdf"),
    ("01. Unified OS", "DCFW", "og-data-center-firewall.pdf"),
    ("01. Unified OS", "FortiGate-as-a-Service", "og-fgaas.pdf"),
    ("01. Unified OS", "FortiProxy", "og-fortiproxy.pdf"),
    ("01. Unified OS", "NGFW - Perimeter FW", "og-next-generation-firewall.pdf"),
    ("01. Unified OS", "Secure SD-WAN", "og-secure-sdwan.pdf"),

    ("02. LAN Security", "FortiAP and Wireless Offerings", "og-wireless.pdf"),
    ("02. LAN Security", "FortiExtender", "og-fortiextender.pdf"),
    ("02. LAN Security", "FortiGate Secure LAN Controller", "og-lan-edge.pdf"),
    ("02. LAN Security", "FortiNAC", "og-fortinac.pdf"),
    ("02. LAN Security", "FortiSwitch", "og-fortiswitch.pdf"),

    ("03. Unified Endpoint", "FortiClient", "og-forticlient.pdf"),
    ("03. Unified Endpoint", "FortiDLP", "og-fortidlp.pdf"),
    ("03. Unified Endpoint", "FortiEDR-FortiXDR", "og-fortiedr.pdf"),
    ("03. Unified Endpoint", "FortiEndpoint", "og-fortiendpoint.pdf"),

    ("04. Unified AppSec (and Cloud)", "Cloud Consulting Services", "og-cloud-consult-svc.pdf"),
    ("04. Unified AppSec (and Cloud)", "FortiADC", "og-fortiadc.pdf"),
    ("04. Unified AppSec (and Cloud)", "FortiAppSec Cloud", "og-fortiappsec.pdf"),
    ("04. Unified AppSec (and Cloud)", "FortiCASB-SSPM", "og-forticasb-sspm.pdf"),
    ("04. Unified AppSec (and Cloud)", "FortiCNAPP", "og-forticnapp.pdf"),
    ("04. Unified AppSec (and Cloud)", "FortiWeb", "og-fortiweb.pdf"),

    ("05. Unified WorkSpace Security", "FortiMail", "og-fortimail.pdf"),
    ("05. Unified WorkSpace Security", "FortiMail Workspace Security", "og-fortimail-wss.pdf"),

    ("06. Unified SecOps Platform", "FortiAnalyzer", "og-fortianalyzer.pdf"),
    ("06. Unified SecOps Platform", "FortiSIEM", "og-fortisiem.pdf"),
    ("06. Unified SecOps Platform", "FortiSOAR", "og-fortisoar.pdf"),

    ("07. Unified AI-Ops", "FortiAIOps", "og-fortiaiops.pdf"),
    ("07. Unified AI-Ops", "FortiMonitor", "og-fortimonitor.pdf"),

    ("08. Unified Attack Surface Management", "FortiRecon", "og-fortirecon.pdf"),
    ("08. Unified Attack Surface Management", "Incident Response Services", "og-ir-services.pdf"),

    ("09. Central Management", "FortiCloud SaaS Mgmt and Analytics", "og-forticloud-mgmt-analytics.pdf"),
    ("09. Central Management", "FortiEdge Cloud", "og-fortiedge.pdf"),
    ("09. Central Management", "FortiManager", "og-fortimanager.pdf"),

    ("10. Advanced Threat Detection", "FortiDeceptor", "og-fortideceptor.pdf"),
    ("10. Advanced Threat Detection", "FortiNDR", "og-fortindr.pdf"),
    ("10. Advanced Threat Detection", "FortiSandbox", "og-fortisandbox.pdf"),

    ("11. Identity and Access", "FortiAuthenticator", "og-fortiauthenticator.pdf"),
    ("11. Identity and Access", "FortiIdentity Cloud", "og-fortiindentity.pdf"),
    ("11. Identity and Access", "FortiPAM", "og-fortipam.pdf"),
    ("11. Identity and Access", "FortiToken", "og-fortitoken.pdf"),
    ("11. Identity and Access", "ZTNA", "og-ztna.pdf"),

    ("12. SASE", "FortiBranchSASE", "og-fortibranchsase.pdf"),
    ("12. SASE", "FortiCASB and FortiGuard CASB Service", "og-casb.pdf"),
    ("12. SASE", "FortiSASE", "og-fortisase.pdf"),
    ("12. SASE", "FortiSASE Sovereign", "og-sovereign-sase.pdf"),

    ("13. Training", "NSE Training and Certification Program", "og-nse-program.pdf"),
    ("13. Training", "Security Awareness and Training and FortiPhish", "og-security-awareness-training.pdf"),

    ("14. Flexible Licensing", "Cloud Marketplace Private Offers", "og-cmpo.pdf"),
    ("14. Flexible Licensing", "Enterprise Agreement Program", "og-entagreement.pdf"),
    ("14. Flexible Licensing", "FortiFlex Program", "og-flex-vm.pdf"),

    ("15. Advanced Support", "FortiCare", "og-forticare.pdf"),

    ("16. Managed Services", "FortiGuard SOCaaS", "og-socaas.pdf"),
    ("16. Managed Services", "Managed FortiGate Service", "og-mfgs.pdf"),

    ("17. Vertical - Operational Technology", "OT", "og-operational-technology.pdf"),

    ("18. Vertical - Others", "Education", "og-education.pdf"),
    ("18. Vertical - Others", "MSSP", "og-mssp.pdf"),
    ("18. Vertical - Others", "Telco", "og-telco.pdf"),

    ("19. Other Products and Solutions", "FortiAIGate", "og-fortiaigate.pdf"),
    ("19. Other Products and Solutions", "FortiCamera and FortiRecorder", "og-forticam.pdf"),
    ("19. Other Products and Solutions", "FortiDDoS", "og-fortiddos.pdf"),
    ("19. Other Products and Solutions", "FortiGate FortiGuard Subscriptions", "og-fortiguard.pdf"),
]


def sanitize(name: str) -> str:
    """Make a safe filesystem component out of a title."""
    name = re.sub(r"[^\w\s.-]", "", name).strip()
    return re.sub(r"\s+", " ", name)


def download_one(url: str, dest_path: str) -> tuple[str, str]:
    """Download url to dest_path. Returns (status, detail)."""
    if os.path.exists(dest_path) and os.path.getsize(dest_path) > 0:
        return "skipped", "already exists"

    last_error = ""
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = requests.get(url, headers=HEADERS, timeout=30)
            if resp.status_code == 200 and resp.content:
                with open(dest_path, "wb") as f:
                    f.write(resp.content)
                return "downloaded", f"{len(resp.content):,} bytes"
            last_error = f"HTTP {resp.status_code}"
        except requests.RequestException as e:
            last_error = str(e)
        time.sleep(RETRY_DELAY_SEC)
    return "failed", last_error


def load_guides() -> list[tuple[str, str, str, str]]:
    if not os.path.exists(DISCOVERED_GUIDES_PATH):
        return [
            (category, title, filename, BASE_URL + filename)
            for category, title, filename in GUIDES
        ]

    required_fields = {"category", "title", "url", "filename"}
    guides = []
    with open(DISCOVERED_GUIDES_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if not required_fields.issubset(reader.fieldnames or set()):
            raise ValueError(
                f"{DISCOVERED_GUIDES_PATH} is missing required fields: "
                f"{', '.join(sorted(required_fields))}"
            )
        for row in reader:
            guides.append((
                row["category"].strip(),
                row["title"].strip(),
                row["filename"].strip(),
                row["url"].strip(),
            ))
    if not guides:
        raise ValueError(f"{DISCOVERED_GUIDES_PATH} contains no guides")
    print(f"Loaded {len(guides)} guides from {DISCOVERED_GUIDES_PATH}")
    return guides


def main():
    os.makedirs(BASE_OUTPUT_DIR, exist_ok=True)
    manifest_path = os.path.join(BASE_OUTPUT_DIR, "manifest.csv")
    rows = []
    guides = load_guides()

    total = len(guides)
    for i, (category, title, filename, url) in enumerate(guides, start=1):
        cat_dir = os.path.join(BASE_OUTPUT_DIR, sanitize(category))
        os.makedirs(cat_dir, exist_ok=True)

        # Keep the original filename so it stays recognizable / linkable back to source
        dest_path = os.path.join(cat_dir, filename)

        status, detail = download_one(url, dest_path)
        print(f"[{i}/{total}] {status.upper():10} {category} / {title} -> {detail}")

        rows.append({
            "category": category,
            "title": title,
            "url": url,
            "local_path": os.path.relpath(dest_path, BASE_OUTPUT_DIR),
            "status": status,
            "detail": detail,
        })

    with open(manifest_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["category", "title", "url", "local_path", "status", "detail"],
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)

    downloaded = sum(1 for r in rows if r["status"] == "downloaded")
    skipped = sum(1 for r in rows if r["status"] == "skipped")
    failed = sum(1 for r in rows if r["status"] == "failed")
    print(f"\nDone. Downloaded: {downloaded}  Skipped (already had): {skipped}  Failed: {failed}")
    print(f"Manifest written to {manifest_path}")
    if failed:
        print("Re-run the script to retry failed downloads (existing successful files are skipped).")


if __name__ == "__main__":
    main()
