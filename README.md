# Ordering Guide Grabber

Downloads Fortinet ordering guides and converts them to Markdown.

## Run locally

Install the Python dependencies and Poppler, then run:

```bash
python3 -m pip install -r requirements.txt
python3 run_ordering_guides_pipeline.py
```

The pipeline downloads the PDFs, converts them to Markdown, and deletes each
PDF after successful conversion. Failed conversions keep their PDFs for retry.

## GitHub Actions

The workflow in `.github/workflows/update-ordering-guides.yml` runs weekly on
Monday at 03:17 UTC and can also be started manually from the Actions tab. It
commits changed Markdown files and manifests to the repository. PDFs are
ignored and are not committed.
