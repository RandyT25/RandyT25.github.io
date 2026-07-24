# Kuta–Seminyak Accounts — Sales Territory Dashboard

Live at **https://randyt25.github.io/**

A handover dashboard for the Kuta-Seminyak hotel/resort sales territory: revenue vs. target,
top accounts (overall and per month), an at-risk/upsell action list, product performance by
category, and a searchable customer directory with per-customer product drill-down.

This page is not search-indexed (`noindex`), but the link is not access-controlled — anyone
with the URL can view it. Treat the link itself as sensitive.

## Refreshing with a new monthly export

1. Drop the new Excel export somewhere on disk.
2. `python3 scripts/parse_sales.py "/path/to/new export.xlsx"` — regenerates `data.json`.
3. `python3 scripts/build_dashboard.py` — regenerates both `index.html` (GitHub Pages) and
   `dashboard.html` (used when republishing the private Claude Artifact copy).
4. Commit and push `index.html` and `data.json`.

Fonts are cached in `scripts/fonts/`, so step 3 never needs network access.
