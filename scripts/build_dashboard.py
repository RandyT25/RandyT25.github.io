#!/usr/bin/env python3
"""
Assemble dashboard.html + index.html from scripts/dashboard_template.html + data.json + the
embedded fonts.

Usage:
    python3 build_dashboard.py [path/to/data.json]

Run this after parse_sales.py has (re)generated data.json. Fonts are cached in
scripts/fonts/ so this step never needs network access.

Two identical output files are written on purpose:
  - dashboard.html — used when publishing the private Claude Artifact.
  - index.html     — used when serving the same page via GitHub Pages (which requires
                      an index.html at the repo root).
"""
import sys
import json
import base64
from pathlib import Path


def main():
    project_root = Path(__file__).resolve().parent.parent
    scripts_dir = Path(__file__).resolve().parent

    data_path = Path(sys.argv[1]) if len(sys.argv) > 1 else project_root / "data.json"

    template = (scripts_dir / "dashboard_template.html").read_text()
    fraunces_b64 = base64.b64encode((scripts_dir / "fonts" / "fraunces.woff2").read_bytes()).decode("ascii")
    sourcesans_b64 = base64.b64encode((scripts_dir / "fonts" / "sourcesans3.woff2").read_bytes()).decode("ascii")

    data = json.loads(data_path.read_text())
    data_json = json.dumps(data, ensure_ascii=False).replace("</script", "<\\/script")

    html = (template
            .replace("__FRAUNCES_B64__", fraunces_b64)
            .replace("__SOURCESANS_B64__", sourcesans_b64)
            .replace("__DATA_JSON__", data_json))

    for name in ("dashboard.html", "index.html"):
        out_path = project_root / name
        out_path.write_text(html)
        print(f"Wrote {out_path} ({out_path.stat().st_size / 1024:.0f} KB)")


if __name__ == "__main__":
    main()
