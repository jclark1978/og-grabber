# Ordering Guide Grabber

Discovers Fortinet ordering guides from the official ordering-guide page,
downloads them, and converts them to Markdown.

## Run locally

Install the Python dependencies and Poppler, then run:

```bash
python3 -m pip install -r requirements.txt
python3 run_ordering_guides_pipeline.py
```

The pipeline discovers the current guide list, downloads the PDFs, converts
them to Markdown, and deletes each PDF after successful conversion. Failed
conversions keep their PDFs for retry.

The discovery results are saved in `fortinet_ordering_guides/discovered_guides.csv`.
The downloader uses that file when available and retains its built-in guide
list as a fallback when run by itself.

## GitHub Actions

The workflow in `.github/workflows/update-ordering-guides.yml` runs weekly on
Monday at 03:17 UTC and can also be started manually from the Actions tab. It
commits changed Markdown files and manifests to the repository. PDFs are
ignored and are not committed.
