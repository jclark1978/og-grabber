#!/usr/bin/env python3
"""Download ordering-guide PDFs and convert them to Markdown in sequence.

Usage:
    python run_ordering_guides_pipeline.py [output_dir]

The child scripts' progress is streamed directly to the terminal. Conversion
starts only when the download script exits successfully.
"""

import argparse
import subprocess
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
DOWNLOAD_SCRIPT = SCRIPT_DIR / "download_fortinet_ordering_guides.py"
CONVERT_SCRIPT = SCRIPT_DIR / "convert_ordering_guides_to_markdown.py"
DEFAULT_OUTPUT_DIR = SCRIPT_DIR / "fortinet_ordering_guides"


def run_stage(stage_name: str, script_path: Path, output_dir: Path) -> int:
    print(f"\n=== {stage_name} ===", flush=True)
    result = subprocess.run(
        [sys.executable, str(script_path), str(output_dir)],
        cwd=SCRIPT_DIR,
    )
    if result.returncode != 0:
        print(f"\n{stage_name} failed with exit code {result.returncode}.", flush=True)
    return result.returncode


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Download ordering guides, then convert them to Markdown."
    )
    parser.add_argument(
        "output_dir",
        nargs="?",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help=f"Directory for guides (default: {DEFAULT_OUTPUT_DIR})",
    )
    args = parser.parse_args()
    output_dir = args.output_dir.expanduser().resolve()

    print(f"Ordering guide pipeline started. Output directory: {output_dir}", flush=True)

    if run_stage("Downloading ordering guides", DOWNLOAD_SCRIPT, output_dir) != 0:
        return 1

    print("\nDownload stage completed. Starting conversion...", flush=True)
    if run_stage("Converting ordering guides", CONVERT_SCRIPT, output_dir) != 0:
        return 1

    print("\nOrdering guide pipeline completed successfully.", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
