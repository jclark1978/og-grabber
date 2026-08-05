#!/usr/bin/env python3
"""Discover Fortinet ordering guides from the official ordering-guide page.

Usage:
    python discover_ordering_guides.py [output_dir]

Writes discovered_guides.csv in output_dir for the downloader to consume.
"""

import csv
import os
import re
import sys
from collections import Counter, defaultdict
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests


DISCOVERY_URL = "https://docs.fortinet.com/ordering-guides"
DEFAULT_OUTPUT_DIR = "fortinet_ordering_guides"
OUTPUT_FILENAME = "discovered_guides.csv"
ALLOWED_PDF_HOSTS = {"docs.fortinet.com", "fortinet.com", "www.fortinet.com"}
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
    )
}


def clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


class OrderingGuideParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.current_category = ""
        self.row_type = None
        self.row_text = []
        self.current_url = None
        self.link_text = []
        self.in_pdf_link = False
        self.guides = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "tr":
            classes = set(attributes.get("class", "").split())
            if "og-group" in classes:
                self.row_type = "group"
                self.row_text = []
            elif "og-guide" in classes:
                self.row_type = "guide"
                self.current_url = None
                self.link_text = []
        elif self.row_type == "guide" and tag == "a":
            href = attributes.get("href", "")
            absolute_url = urljoin(DISCOVERY_URL, href)
            path = urlparse(absolute_url).path.lower()
            if path.endswith(".pdf"):
                self.current_url = absolute_url
                self.in_pdf_link = True
                self.link_text = []

    def handle_endtag(self, tag):
        if tag == "a" and self.in_pdf_link:
            self.in_pdf_link = False
        elif tag == "tr" and self.row_type == "group":
            category = clean_text(" ".join(self.row_text))
            if category:
                self.current_category = category
            self.row_type = None
            self.row_text = []
        elif tag == "tr" and self.row_type == "guide":
            if self.current_url and self.current_category:
                title = clean_text(" ".join(self.link_text))
                self.guides.append((self.current_category, title, self.current_url))
            self.row_type = None
            self.current_url = None
            self.link_text = []

    def handle_data(self, data):
        if self.row_type == "group":
            self.row_text.append(data)
        elif self.row_type == "guide" and self.in_pdf_link:
            self.link_text.append(data)


def existing_category_by_filename(output_dir: str):
    categories = {}
    if not os.path.isdir(output_dir):
        return categories
    for dirpath, _dirnames, filenames in os.walk(output_dir):
        if os.path.abspath(dirpath) == os.path.abspath(output_dir):
            continue
        category = os.path.relpath(dirpath, output_dir)
        for filename in filenames:
            if filename.lower().endswith(".md") and filename not in categories:
                categories[Path(filename).stem] = category
    return categories


def validate_and_prepare_guides(parsed_guides, output_dir: str):
    existing_categories = existing_category_by_filename(output_dir)
    category_matches = defaultdict(Counter)
    parsed_with_filenames = []
    for category, title, url in parsed_guides:
        filename = Path(urlparse(url).path).name
        filename_stem = Path(filename).stem
        if filename_stem in existing_categories:
            category_matches[category][existing_categories[filename_stem]] += 1
        parsed_with_filenames.append((category, title, url, filename))

    canonical_categories = {
        category: matches.most_common(1)[0][0]
        for category, matches in category_matches.items()
        if matches
    }
    guides = []
    seen_urls = set()
    seen_filenames = set()
    for category, title, url, filename in parsed_with_filenames:
        parsed_url = urlparse(url)
        if (
            parsed_url.scheme != "https"
            or parsed_url.hostname not in ALLOWED_PDF_HOSTS
            or not filename.lower().endswith(".pdf")
        ):
            raise RuntimeError(f"Unexpected ordering-guide URL: {url}")
        if not title:
            title = Path(filename).stem
        if url in seen_urls:
            continue
        if filename in seen_filenames:
            raise RuntimeError(f"Duplicate ordering-guide filename: {filename}")
        seen_urls.add(url)
        seen_filenames.add(filename)
        guides.append({
            "category": canonical_categories.get(category, category),
            "title": title,
            "url": url,
            "filename": filename,
        })
    if not guides:
        raise RuntimeError(
            "No ordering guides were discovered; the page structure may have changed."
        )
    return guides


def discover_guides(output_dir: str):
    response = requests.get(DISCOVERY_URL, headers=HEADERS, timeout=30)
    response.raise_for_status()

    parser = OrderingGuideParser()
    parser.feed(response.text)
    guides = validate_and_prepare_guides(parser.guides, output_dir)

    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, OUTPUT_FILENAME)
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["category", "title", "url", "filename"],
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(guides)

    for index, guide in enumerate(guides, start=1):
        print(
            f"[{index}/{len(guides)}] DISCOVERED {guide['category']} / "
            f"{guide['title']} -> {guide['filename']}"
        )
    print(f"\nDiscovered {len(guides)} ordering guides.")
    print(f"Discovery manifest written to {output_path}")


def main():
    output_dir = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUTPUT_DIR
    try:
        discover_guides(output_dir)
    except (requests.RequestException, RuntimeError) as error:
        print(f"Discovery failed: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
