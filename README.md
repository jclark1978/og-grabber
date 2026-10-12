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

## Persistent content monitoring

The weekly pipeline now re-fetches each official PDF and stores
`fortinet_ordering_guides/guide_baseline.json` with stable guide identity, source
URL, PDF SHA-256, normalized extracted-text SHA-256, byte count, document-date
hint, verification time, and retirement status. PDF bytes are never committed.
Existing mirrored Markdown seeds the first text comparison; the first PDF
fingerprint is initialization, not a change alert. If there is no existing text
inventory, the first successful check establishes a silent baseline.

`guide_changes.json` holds the latest check. Immutable `changes/*.json` reports
and referenced `changes/diffs/**/*.diff` files retain evidence across later
quiet checks. Git history preserves previous baseline versions. The Action also
uploads the reports as an artifact and runs regression tests before refreshing.
A push of pipeline code to `main` runs tests and an immediate refresh; generated
guide/report commits do not recursively trigger another refresh.

Reports deliberately distinguish:

- `qualifying_changes`: verified guide additions and confirmed retirements.
- `content_review_candidates`: changed extracted content, including replacements
  at the same URL. Includes full text-diff paths and added/removed SKU evidence.
  Review these for actual model, bundle, licensing, ordering-rule, or other
  material product-lookup changes before sending a notification. A date-only,
  editorial, or extraction-layout difference is not automatically material.
- `discovery_only`: renamed/reclassified catalog entries or changed URLs with
  identical extracted content. A guide absent from the catalog but with a working
  official PDF also falls here and remains checked for future content revisions.
- `binary_only`: different PDF bytes with identical normalized extracted text.
  PDF metadata or packaging often causes this; it is not by itself evidence of
  a material change. Text comparison does not establish whether image-only
  content changed; investigate binary-only cases when there is visual evidence.
- `unverified`: download/extraction failures or retirement candidates awaiting
  confirmation. Never interpret these as successful no-change checks.

Catalog failures fall back to the last verified guide inventory and still check
known PDFs, with `discovery_verified=false`. A catalog shrinking by more than
20% is treated as possibly incomplete and cannot confirm removals. Retiring a
guide requires absence from two consecutive successfully verified catalogs and
404/410 responses from the official PDF on both checks. A 403, timeout, or
accessible PDF does not confirm retirement. Retired Markdown is retained for
historical lookup, and its manifest/baseline status is `removed`.

Changed guides retain their previous text under `changes/snapshots/` so an
interrupted run cannot lose the content needed to reconstruct a comparison.

Successful guide checks advance their individual baselines even during a partial
run. Failed guides retain their previous content and fingerprints for retry.
Incomplete checks return a nonzero exit status, but the workflow still persists
reports and verified updates. Pinned extraction dependencies keep comparisons
consistent across runs.

Run regression tests with:

```bash
python -m unittest discover -s tests -v
```
