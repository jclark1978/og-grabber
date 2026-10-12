#!/usr/bin/env python3
"""Discover, freshly download/hash, compare, and mirror official ordering guides."""
import argparse
from pathlib import Path

from monitor_ordering_guides import run

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_OUTPUT_DIR = SCRIPT_DIR / "fortinet_ordering_guides"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output_dir", nargs="?", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()
    return run(args.output_dir.expanduser().resolve())


if __name__ == "__main__":
    raise SystemExit(main())
