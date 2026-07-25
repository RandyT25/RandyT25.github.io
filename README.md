# Kuta–Seminyak Accounts — Sales Territory Dashboard

Live at **https://randyt25.github.io/kuta-seminyak-hotel/**

A handover dashboard for the Kuta-Seminyak hotel/resort sales territory: revenue vs. target,
top accounts (overall and per month), an at-risk/upsell action list, product performance by
category, and a searchable customer directory with per-customer product drill-down.

This page is not search-indexed (`noindex`), but the link is not access-controlled — anyone
with the URL can view it. Treat the link itself as sensitive.

## Primary refresh flow (automated)

The territory is identified in the daily company-wide export
(`data penjualan global ...xlsx`) by the `Sales` column value `"Vacant Hotel Kuta Seminyak"` /
`"Vacant Hotel Seminyak Kuta"` — the placeholder the company uses for these now-unstaffed
accounts.

1. Drop the new `data penjualan global ...xlsx` into this folder (replacing the old one).
2. Commit and push.
3. `.github/workflows/update-kuta-seminyak-data.yml` picks it up automatically: runs
   `scripts/parse_global_sales.py` (filters + aggregates into `data.json`), then
   `scripts/build_dashboard.py` (rebuilds `index.html`/`dashboard.html`), and pushes the result
   back — GitHub Pages redeploys on its own from there.

Note: the raw export is committed to this **public** repo — it contains company-wide sales data
across all regions/reps, not just this territory. This was a deliberate, explicitly confirmed
choice (matching the same pattern used by the separate `dashboard_kutaselatan` project), not an
oversight.

To republish the private Claude Artifact copy after a refresh, hand the rebuilt `dashboard.html`
to Claude and ask it to republish to the existing artifact URL.

## Legacy manual flow

`scripts/parse_sales.py` still works against the old hand-curated pivot export
(`data Lani Customer.xlsx`, gitignored, not committed) if ever needed, but is no longer the
primary path:

1. `python3 scripts/parse_sales.py "/path/to/pivot_export.xlsx"` — regenerates `data.json`.
2. `python3 scripts/build_dashboard.py` — regenerates `index.html`/`dashboard.html`.
3. Commit and push.

Fonts previously used by this dashboard were removed in the restyle to match
`dashboard_kutaselatan`'s look (system font stack instead), so `scripts/fonts/` is no longer used.
