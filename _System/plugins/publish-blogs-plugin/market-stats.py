#!/usr/bin/env python3
"""
Turn a Lofty/MLS "Agent Single Line" sold CSV into dated per-area price stats.

The AEO blog library needs price anchors it can defend: a median, a range, a
property-type split, and a stated date window, per Las Vegas area. This reads
the raw sold export and writes both a JSON file (for scripts) and a markdown
file (for writers and subagent briefs).

Usage:
  python3 market-stats.py "/Users/ryanrose/Downloads/Agent Single Line (7).csv"
  python3 market-stats.py <csv> --out-dir "<folder>"

Expected columns: Zip Code, Stat, Current Price, Sub, Approx Liv Area,
Beds Total, Year Built, Actual Close Date, DOM. Only Stat == S (sold) counts.
"""

import argparse
import csv
import json
import re
import statistics
from collections import defaultdict
from datetime import datetime
from pathlib import Path

DEFAULT_OUT = Path(
    "/Users/ryanrose/Downloads/Claude/Rose Homes LV/Content/Research/market-stats"
)

# Area -> zip codes. Zips are approximate area proxies, which is why every
# published figure says "zip codes 891xx" rather than claiming a boundary.
AREAS = {
    "Las Vegas (valley wide)": None,  # every zip in the file
    "Summerlin": ["89135", "89138", "89134", "89144", "89145"],
    "Summerlin West": ["89138", "89166"],
    "Henderson": ["89002", "89011", "89012", "89014", "89015", "89044",
                  "89052", "89074", "89002"],
    "Green Valley (Henderson)": ["89014", "89074", "89012"],
    "Seven Hills / Anthem (Henderson 89052)": ["89052"],
    "Inspirada (Henderson)": ["89044"],
    "North Las Vegas": ["89030", "89031", "89032", "89081", "89084", "89086"],
    "Aliante (North Las Vegas)": ["89084", "89086"],
    "Centennial Hills": ["89149", "89131", "89143"],
    "Centennial Hills and Skye Canyon": ["89149", "89131", "89143", "89166"],
    "Skye Canyon / Summerlin North (89166)": ["89166"],
    "Providence (Las Vegas)": ["89166", "89149"],
    "Spring Valley": ["89117", "89147", "89148", "89113"],
    "Southern Highlands": ["89141"],
    "Mountains Edge": ["89178", "89179"],
    "Enterprise / southwest": ["89178", "89141", "89148", "89113"],
}

TYPE_LABEL = {"SFR": "single family", "TWH": "townhome", "CON": "condo",
              "MAN": "manufactured"}


def money(text):
    digits = re.sub(r"[^0-9.]", "", text or "")
    try:
        return float(digits)
    except ValueError:
        return None


def number(text):
    digits = re.sub(r"[^0-9.]", "", text or "")
    try:
        return float(digits)
    except ValueError:
        return None


def load(csv_path):
    sold = []
    with open(csv_path, newline="", encoding="utf-8-sig") as fh:
        for row in csv.DictReader(fh):
            if (row.get("Stat") or "").strip().upper() != "S":
                continue
            price = money(row.get("Current Price"))
            if not price:
                continue
            closed = (row.get("Actual Close Date") or "").strip()
            try:
                closed_on = datetime.strptime(closed, "%m/%d/%Y").date()
            except ValueError:
                continue
            sold.append({
                "zip": (row.get("Zip Code") or "").strip(),
                "price": price,
                "type": (row.get("Sub") or "").strip().upper(),
                "sqft": number(row.get("Approx Liv Area")),
                "beds": number(row.get("Beds Total")),
                "year": number(row.get("Year Built")),
                "dom": number(row.get("DOM")),
                "closed": closed_on,
            })
    return sold


def summarize(rows):
    prices = sorted(r["price"] for r in rows)
    ppsf = [r["price"] / r["sqft"] for r in rows if r["sqft"]]
    doms = [r["dom"] for r in rows if r["dom"] is not None]
    out = {
        "count": len(rows),
        "median": round(statistics.median(prices)),
        "low": round(prices[0]),
        "high": round(prices[-1]),
        "p25": round(statistics.quantiles(prices, n=4)[0]) if len(prices) > 3 else None,
        "p75": round(statistics.quantiles(prices, n=4)[2]) if len(prices) > 3 else None,
        "median_ppsf": round(statistics.median(ppsf)) if ppsf else None,
        "median_dom": round(statistics.median(doms)) if doms else None,
    }
    by_type = {}
    for code in ("SFR", "TWH", "CON"):
        subset = [r["price"] for r in rows if r["type"] == code]
        if len(subset) >= 5:
            by_type[TYPE_LABEL[code]] = {
                "count": len(subset),
                "median": round(statistics.median(sorted(subset))),
            }
    out["by_type"] = by_type
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv_path")
    ap.add_argument("--out-dir", default=str(DEFAULT_OUT))
    ap.add_argument("--min-sales", type=int, default=10,
                    help="skip an area with fewer closed sales than this")
    args = ap.parse_args()

    sold = load(args.csv_path)
    if not sold:
        raise SystemExit("no sold rows found, check the CSV columns")

    first = min(r["closed"] for r in sold)
    last = max(r["closed"] for r in sold)
    window = f"{first.strftime('%B %-d, %Y')} through {last.strftime('%B %-d, %Y')}"

    by_zip = defaultdict(list)
    for r in sold:
        by_zip[r["zip"]].append(r)

    areas = {}
    for name, zips in AREAS.items():
        rows = sold if zips is None else [r for r in sold if r["zip"] in set(zips)]
        if len(rows) < args.min_sales:
            continue
        entry = summarize(rows)
        entry["zips"] = sorted(set(r["zip"] for r in rows)) if zips else "all"
        areas[name] = entry

    zips_out = {z: summarize(rows) for z, rows in sorted(by_zip.items())
                if len(rows) >= args.min_sales}

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = last.strftime("%Y-%m-%d")

    payload = {
        "source": "Las Vegas MLS closed sales export (Agent Single Line)",
        "pulled": datetime.now().strftime("%Y-%m-%d"),
        "window_start": first.isoformat(),
        "window_end": last.isoformat(),
        "window_text": window,
        "total_sales": len(sold),
        "areas": areas,
        "zips": zips_out,
    }
    json_path = out_dir / f"market-stats-{stamp}.json"
    json_path.write_text(json.dumps(payload, indent=2))
    (out_dir / "market-stats-latest.json").write_text(json.dumps(payload, indent=2))

    lines = [
        f"# Las Vegas closed sales, {window}",
        "",
        f"Source: Las Vegas MLS closed sales export, {len(sold):,} closed sales, "
        f"pulled {payload['pulled']}. Areas are grouped by zip code, so they are "
        "close to but not identical to master plan boundaries. Say the date "
        "window every time you publish one of these numbers.",
        "",
        "| Area | Closed sales | Median price | Middle half | Median $/sq ft | Median days on market |",
        "|---|---|---|---|---|---|",
    ]
    for name, a in areas.items():
        mid = (f"${a['p25']:,} to ${a['p75']:,}" if a["p25"] else "n/a")
        ppsf = f"${a['median_ppsf']:,}" if a["median_ppsf"] else "n/a"
        dom = a["median_dom"] if a["median_dom"] is not None else "n/a"
        lines.append(f"| {name} | {a['count']} | ${a['median']:,} | {mid} | {ppsf} | {dom} |")

    lines += ["", "## Property type split", ""]
    for name, a in areas.items():
        if not a["by_type"]:
            continue
        parts = [f"{label} ${v['median']:,} ({v['count']} sales)"
                 for label, v in a["by_type"].items()]
        lines.append(f"- **{name}:** " + ", ".join(parts))

    lines += ["", "## By zip code", "",
              "| Zip | Closed sales | Median price | Median $/sq ft | Median DOM |",
              "|---|---|---|---|---|"]
    for z, a in zips_out.items():
        ppsf = f"${a['median_ppsf']:,}" if a["median_ppsf"] else "n/a"
        dom = a["median_dom"] if a["median_dom"] is not None else "n/a"
        lines.append(f"| {z} | {a['count']} | ${a['median']:,} | {ppsf} | {dom} |")

    md_path = out_dir / f"market-stats-{stamp}.md"
    md_path.write_text("\n".join(lines) + "\n")
    (out_dir / "market-stats-latest.md").write_text("\n".join(lines) + "\n")

    print(f"{len(sold):,} closed sales, {window}")
    print(f"wrote {md_path}")
    print(f"wrote {json_path}")
    print(f"wrote {out_dir/'market-stats-latest.md'} and -latest.json")


if __name__ == "__main__":
    main()
