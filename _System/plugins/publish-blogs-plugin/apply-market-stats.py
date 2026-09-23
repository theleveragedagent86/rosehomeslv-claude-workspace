#!/usr/bin/env python3
"""
Write a dated "what homes are selling for" section into the AEO blog posts.

Reads market-stats-latest.json (built by market-stats.py) and inserts one
generated section into every AEO post whose slug names an area we have sales
for. The section is delimited by its own heading, so re-running replaces the
old numbers instead of stacking a second copy. That is what makes the every
two weeks refresh safe.

Usage:
  python3 apply-market-stats.py              # all AEO folders
  python3 apply-market-stats.py --dry-run
  python3 apply-market-stats.py --folders "AEO Matrix"
  python3 apply-market-stats.py --list-unmatched
"""

import argparse
import json
import re
from datetime import date
from pathlib import Path

BLOGS = Path("/Users/ryanrose/Downloads/Claude/Rose Homes LV/Content/Claude Blogs")
STATS = Path("/Users/ryanrose/Downloads/Claude/Rose Homes LV/Content/Research/"
             "market-stats/market-stats-latest.json")
AEO_FOLDERS = ["AEO Best Choice", "AEO Reasons to Choose", "AEO Local Service",
               "AEO Questions", "AEO Matrix"]

EXPLORE = "## Explore More Las Vegas Communities"
HEADING_RE = re.compile(r"^## What .*?Selling For in .*$", re.M)

# Slug suffix -> (area key in the stats file, name to print). Longest first.
AREA_BY_SUFFIX = [
    ("centennial-hills-skye-canyon", "Centennial Hills and Skye Canyon",
     "Centennial Hills and Skye Canyon"),
    ("aliante-north-las-vegas", "Aliante (North Las Vegas)", "Aliante"),
    ("green-valley-henderson", "Green Valley (Henderson)", "Green Valley"),
    ("inspirada-henderson", "Inspirada (Henderson)", "Inspirada"),
    ("seven-hills-henderson", "Seven Hills / Anthem (Henderson 89052)", "Seven Hills"),
    ("providence-las-vegas", "Providence (Las Vegas)", "Providence"),
    ("spring-valley-las-vegas", "Spring Valley", "Spring Valley"),
    ("southern-highlands", "Southern Highlands", "Southern Highlands"),
    ("mountains-edge", "Mountains Edge", "Mountains Edge"),
    ("north-las-vegas", "North Las Vegas", "North Las Vegas"),
    ("henderson-nv", "Henderson", "Henderson"),
    ("in-henderson", "Henderson", "Henderson"),
    ("henderson", "Henderson", "Henderson"),
    ("summerlin", "Summerlin", "Summerlin"),
    ("las-vegas", "Las Vegas (valley wide)", "the Las Vegas valley"),
]

# Posts about one property type read better with that type's median up front.
CONDO_PREFIX = "condo-townhome-realtor-"

TYPE_PHRASE = {"single family": "single family homes", "townhome": "townhomes",
               "condo": "condos", "manufactured": "manufactured homes"}


def money(n):
    return f"${n:,}"


def month_range(stats):
    start = date.fromisoformat(stats["window_start"])
    end = date.fromisoformat(stats["window_end"])
    return (f"{start.strftime('%B %-d')} through "
            f"{end.strftime('%B %-d, %Y')}")


def pick_area(slug, stats):
    for suffix, key, label in AREA_BY_SUFFIX:
        if slug.endswith(suffix) or f"-{suffix}-" in slug or slug.startswith(suffix):
            if key in stats["areas"]:
                return key, label
    return None, None


def resolve(fragment, stats):
    """Match a bare slug fragment (one side of an X-vs-Y slug) to an area."""
    for suffix, key, label in AREA_BY_SUFFIX:
        if fragment.endswith(suffix) or fragment.startswith(suffix):
            if key in stats["areas"]:
                return key, label
    return None, None


def build_comparison(left, right, stats):
    (lk, ll), (rk, rl) = left, right
    a, b = stats["areas"][lk], stats["areas"][rk]
    window = month_range(stats)
    heading = f"## What Homes Are Selling For in {ll} and {rl}"
    lines = [
        f"Las Vegas MLS closed sales from {window} put the median at "
        f"{money(a['median'])} in {ll} across {a['count']:,} sales, and "
        f"{money(b['median'])} in {rl} across {b['count']:,} sales."
    ]
    if a.get("p25") and b.get("p25"):
        lines.append(
            f"The middle half of {ll} sales ran {money(a['p25'])} to "
            f"{money(a['p75'])}. In {rl} it ran {money(b['p25'])} to "
            f"{money(b['p75'])}. Those bands overlap more than the medians "
            "suggest, so the area matters less than the specific street and "
            "the home itself.")
    if a.get("median_ppsf") and b.get("median_ppsf"):
        lines.append(
            f"Per square foot, the medians were {money(a['median_ppsf'])} in "
            f"{ll} and {money(b['median_ppsf'])} in {rl}.")
    lines.append(
        "These are closed sales for that date window only, not a forecast, and "
        "they move every month. Areas are grouped by zip code, so they track "
        "the neighborhood closely without matching a master plan boundary "
        "exactly. Ask Ryan for a current pull before you price anything.")
    return heading + "\n\n" + "\n\n".join(lines) + "\n"


def build_section(slug, key, label, stats):
    a = stats["areas"][key]
    window = month_range(stats)
    types = a.get("by_type", {})
    condo_post = slug.startswith(CONDO_PREFIX)

    heading = f"## What Homes Are Selling For in {label}"

    parts = [
        f"Here is what actually closed. Las Vegas MLS records {a['count']:,} "
        f"home sales in {label} from {window}, at a median price of "
        f"{money(a['median'])}."
    ]
    if a.get("p25") and a.get("p75"):
        parts.append(
            f"Half of those sales landed between {money(a['p25'])} and "
            f"{money(a['p75'])}, so that middle band is the realistic range for "
            "most buyers.")
    extras = []
    if a.get("median_ppsf"):
        extras.append(f"the median worked out to about {money(a['median_ppsf'])} "
                      "per square foot")
    if a.get("median_dom") is not None:
        extras.append(f"the median home went under contract in about "
                      f"{a['median_dom']} days")
    if extras:
        parts.append("Across the same sales, " + " and ".join(extras) + ".")

    if types:
        order = (["condo", "townhome", "single family"] if condo_post
                 else ["single family", "townhome", "condo"])
        bits = [f"{TYPE_PHRASE[name]} at {money(types[name]['median'])} "
                f"({types[name]['count']:,} sales)"
                for name in order if name in types]
        if bits:
            parts.append("By property type, the medians were " +
                         ", ".join(bits[:-1]) +
                         (" and " if len(bits) > 1 else "") + bits[-1] + ".")

    parts.append(
        "These are closed sales for that date window only, not a forecast, and "
        "they move every month. Areas are grouped by zip code, so they track "
        "the neighborhood closely without matching a master plan boundary "
        "exactly. Ask Ryan for a current pull before you price anything.")

    return heading + "\n\n" + "\n\n".join(parts) + "\n"


def strip_old(text):
    """Remove a previously generated section, heading through the next ## or
    the end of the body."""
    m = HEADING_RE.search(text)
    if not m:
        return text, False
    rest = text[m.end():]
    nxt = re.search(r"^## ", rest, re.M)
    end = m.end() + (nxt.start() if nxt else len(rest))
    return (text[:m.start()] + text[end:]), True


def apply_to(path, stats, dry_run):
    slug = path.stem
    section = None
    if "-vs-" in slug:
        left_frag, right_frag = slug.split("-vs-", 1)
        left, right = resolve(left_frag, stats), resolve(right_frag, stats)
        if left[0] and right[0] and left[0] != right[0]:
            section = build_comparison(left, right, stats)
    if section is None:
        key, label = pick_area(slug, stats)
        if not key:
            return "unmatched"
        section = build_section(slug, key, label, stats)
    text = path.read_text(encoding="utf-8")
    text, replaced = strip_old(text)

    idx = text.find(EXPLORE)
    if idx == -1:
        # No Explore block: drop it in ahead of the sources line or the JSON-LD.
        m = re.search(r'^<p style="font-size: 0\.85em|^<script type="application/ld\+json"',
                      text, re.M)
        idx = m.start() if m else len(text)
    new = text[:idx].rstrip() + "\n\n" + section + "\n" + text[idx:]
    if not dry_run:
        path.write_text(new, encoding="utf-8")
    return "updated" if replaced else "added"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--folders", nargs="+", default=AEO_FOLDERS)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--list-unmatched", action="store_true")
    args = ap.parse_args()

    stats = json.loads(STATS.read_text())
    tally = {"added": 0, "updated": 0, "unmatched": 0}
    unmatched = []

    for folder in args.folders:
        d = BLOGS / folder
        if not d.is_dir():
            print(f"  [!!] missing folder {folder}")
            continue
        for f in sorted(d.glob("*.html")):
            if re.search(r"seo[-_]?package", f.stem, re.I):
                continue
            result = apply_to(f, stats, args.dry_run)
            tally[result] += 1
            if result == "unmatched":
                unmatched.append(f"{folder}/{f.stem}")

    print(f"window: {month_range(stats)}   source rows: {stats['total_sales']:,}")
    print(f"added: {tally['added']}   updated: {tally['updated']}   "
          f"no area match: {tally['unmatched']}")
    if args.list_unmatched:
        for u in unmatched:
            print(f"  - {u}")


if __name__ == "__main__":
    main()
