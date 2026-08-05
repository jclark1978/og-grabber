#!/usr/bin/env python3
"""
Convert Fortinet Ordering Guide PDFs to Markdown.

Walks a directory tree (default: fortinet_ordering_guides, the output of
download_fortinet_ordering_guides.py), finds every .pdf, and writes a
same-named .md file right next to it — so the category folder structure
from the download script is preserved automatically.

Usage:
    python convert_ordering_guides_to_markdown.py [root_dir]

Behavior:
- Skips a PDF if a .md file already exists and is newer than the PDF
  (safe to re-run after downloading new/updated guides).
- Deletes the PDF after a successful conversion or when its existing .md
  file is already up to date.
- Extracts body text page by page, plus any tables (common in these guides
  for SKU / part-number listings), rendered as Markdown tables.
- Falls back to pdftotext (poppler) if pdfplumber can't parse a file.
- Writes a conversion_manifest.csv in root_dir summarizing results.
"""

import csv
import os
import subprocess
import sys

import pdfplumber

ROOT_DIR = sys.argv[1] if len(sys.argv) > 1 else "fortinet_ordering_guides"


def table_to_markdown(table: list[list]) -> str:
    """Render a pdfplumber-extracted table (list of rows) as a Markdown table."""
    if not table or not table[0]:
        return ""
    # Normalize None cells / strip whitespace
    rows = [[(cell or "").strip().replace("\n", " ") for cell in row] for row in table]
    header, body = rows[0], rows[1:]
    col_count = len(header)

    def fmt_row(row):
        row = row + [""] * (col_count - len(row))  # pad short rows
        return "| " + " | ".join(row[:col_count]) + " |"

    lines = [fmt_row(header), "| " + " | ".join(["---"] * col_count) + " |"]
    lines.extend(fmt_row(r) for r in body)
    return "\n".join(lines)


def convert_with_pdfplumber(pdf_path: str) -> str:
    parts = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            text = (page.extract_text() or "").strip()
            if text:
                parts.append(text)

            tables = page.extract_tables()
            for t_idx, table in enumerate(tables, start=1):
                md_table = table_to_markdown(table)
                if md_table:
                    parts.append(f"\n**Table {i}.{t_idx}**\n\n{md_table}")

    return "\n\n".join(parts).strip()


def convert_with_pdftotext(pdf_path: str) -> str:
    """Fallback: shell out to poppler's pdftotext, preserving rough layout."""
    result = subprocess.run(
        ["pdftotext", "-layout", pdf_path, "-"],
        capture_output=True, text=True, timeout=60,
    )
    return result.stdout.strip()


def convert_one(pdf_path: str, md_path: str) -> tuple[str, str]:
    if os.path.exists(md_path) and os.path.getmtime(md_path) >= os.path.getmtime(pdf_path):
        try:
            os.remove(pdf_path)
        except OSError as e:
            return "skipped", f"up to date; PDF delete failed: {e}"
        return "skipped", "up to date; PDF deleted"

    title = os.path.splitext(os.path.basename(pdf_path))[0]
    body = ""
    method = "pdfplumber"
    try:
        body = convert_with_pdfplumber(pdf_path)
    except Exception as e:
        method = f"pdftotext (pdfplumber failed: {e})"
        try:
            body = convert_with_pdftotext(pdf_path)
        except Exception as e2:
            return "failed", f"both extractors failed: {e2}"

    if not body:
        return "failed", "no extractable text (possibly scanned/image-only PDF)"

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write(body)
        f.write("\n")

    try:
        os.remove(pdf_path)
    except OSError as e:
        return "converted", f"{method}; PDF delete failed: {e}"

    return "converted", f"{method}; PDF deleted"


def main():
    if not os.path.isdir(ROOT_DIR):
        print(f"Directory not found: {ROOT_DIR}")
        print("Run download_fortinet_ordering_guides.py first, or pass the correct path.")
        sys.exit(1)

    pdf_paths = []
    for dirpath, _dirnames, filenames in os.walk(ROOT_DIR):
        for fn in filenames:
            if fn.lower().endswith(".pdf"):
                pdf_paths.append(os.path.join(dirpath, fn))
    pdf_paths.sort()

    if not pdf_paths:
        print(f"No PDFs found under {ROOT_DIR}")
        return

    rows = []
    total = len(pdf_paths)
    for i, pdf_path in enumerate(pdf_paths, start=1):
        md_path = os.path.splitext(pdf_path)[0] + ".md"
        status, detail = convert_one(pdf_path, md_path)
        rel = os.path.relpath(pdf_path, ROOT_DIR)
        print(f"[{i}/{total}] {status.upper():10} {rel} -> {detail}")
        rows.append({
            "pdf": rel,
            "markdown": os.path.relpath(md_path, ROOT_DIR),
            "status": status,
            "detail": detail,
        })

    manifest_path = os.path.join(ROOT_DIR, "conversion_manifest.csv")
    with open(manifest_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["pdf", "markdown", "status", "detail"],
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)

    converted = sum(1 for r in rows if r["status"] == "converted")
    skipped = sum(1 for r in rows if r["status"] == "skipped")
    failed = sum(1 for r in rows if r["status"] == "failed")
    print(f"\nDone. Converted: {converted}  Skipped (up to date): {skipped}  Failed: {failed}")
    print(f"Manifest written to {manifest_path}")


if __name__ == "__main__":
    main()
