#!/usr/bin/env python3
"""
The every two weeks price refresh for the AEO blog library.

One command runs the whole chain:
  1. find the newest MLS sold export in ~/Downloads
  2. rebuild the dated per area stats
  3. rewrite the "What Homes Are Selling For in X" section in every AEO post
  4. push the changed posts live through Lofty
  5. re-backfill FAQ schema and featured images, which the body push overwrites

Only step 1 needs Ryan. Everything downstream is deterministic, so the whole
thing is safe to re-run.

Usage:
  python3 refresh-market-stats.py                 # full run
  python3 refresh-market-stats.py --dry-run       # stats + local diff only
  python3 refresh-market-stats.py --csv <path>    # use a specific export
  python3 refresh-market-stats.py --max-age-days 21
"""

import argparse
import glob
import os
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
DOWNLOADS = Path.home() / "Downloads"
WORKSPACE = Path("/Users/ryanrose/Downloads/Claude")
AEO_FOLDERS = ["AEO Best Choice", "AEO Reasons to Choose", "AEO Local Service",
               "AEO Questions", "AEO Matrix"]
SCRATCH = HERE / ".market-stats-run"


def newest_export():
    hits = glob.glob(str(DOWNLOADS / "Agent Single Line*.csv"))
    if not hits:
        return None
    return Path(max(hits, key=os.path.getmtime))


def run(cmd, **kw):
    print(f"\n$ {' '.join(str(c) for c in cmd)}")
    result = subprocess.run([str(c) for c in cmd], **kw)
    if result.returncode != 0:
        sys.exit(f"FAILED: {cmd[1] if len(cmd) > 1 else cmd[0]}")
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--max-age-days", type=int, default=21,
                    help="refuse an export older than this many days")
    ap.add_argument("--folders", nargs="+", default=AEO_FOLDERS)
    args = ap.parse_args()

    csv_path = Path(args.csv) if args.csv else newest_export()
    if not csv_path or not csv_path.exists():
        sys.exit(
            "NO EXPORT FOUND.\n"
            "Ryan needs to run the MLS Agent Single Line sold search and save "
            "the CSV to ~/Downloads, then re-run this. Nothing was changed.")

    age = (datetime.now() - datetime.fromtimestamp(csv_path.stat().st_mtime)).days
    print(f"export: {csv_path.name}  ({age} days old)")
    if age > args.max_age_days:
        sys.exit(
            f"EXPORT IS STALE ({age} days old, limit {args.max_age_days}).\n"
            "Publishing these numbers would date the posts wrong. Ryan needs a "
            "fresh MLS sold export in ~/Downloads. Nothing was changed.")

    run([sys.executable, HERE / "market-stats.py", csv_path])
    run([sys.executable, HERE / "apply-market-stats.py"]
        + (["--dry-run"] if args.dry_run else []))

    if args.dry_run:
        subprocess.run(["git", "-C", str(WORKSPACE), "diff", "--stat", "--",
                        "Rose Homes LV/Content/Claude Blogs"])
        print("\ndry run, nothing published")
        return

    for folder in args.folders:
        print(f"\n### publishing {folder}")
        run([sys.executable, HERE / "fix-live-posts.py", "body", folder, "--yes"])

    SCRATCH.mkdir(exist_ok=True)
    dump = SCRATCH / "dump.json"
    patches = SCRATCH / "patches.json"
    run([sys.executable, HERE / "lofty_api.py", "dump", dump])
    run([sys.executable, HERE / "backfill_schema.py", dump, patches])
    run([sys.executable, HERE / "lofty_api.py", "patch", patches])

    print(f"\nDone {date.today().isoformat()}. "
          "Stats, local posts, live posts and schema are all in sync.")


if __name__ == "__main__":
    main()
