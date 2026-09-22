#!/usr/bin/env python3
"""
Fix Live Blog Links on Lofty CMS — AppleScript + Chrome
========================================================
Opens each published Claude Blogs post in the Lofty editor and rewrites
broken internal links from /blogs/<slug> (404s) to /blog/<slug>, then saves.

With --sync-body it instead replaces the whole post body with the local
file (converted the same way publish.py does), for posts whose text changed.

Which posts: read from a slug list file (one slug per line). Build it with
--build-list, which finds every local post git reports as changed.

Usage:
    python3 fix-blog-links.py --build-list                 Write fix-blog-links-slugs.txt
    python3 fix-blog-links.py                              Fix every slug in the list
    python3 fix-blog-links.py --posts 1-25                 Only list entries 1 to 25
    python3 fix-blog-links.py --slug summerlin-home-prices-2026
    python3 fix-blog-links.py --sync-body --folder ALIANTE --slug aliante-townhomes-condos-villagio

Requirements: macOS, Google Chrome (View > Developer > Allow JavaScript from
Apple Events enabled), logged into Lofty CMS, blog dashboard on tab 4.
"""

import argparse
import importlib.util
import json
import re
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = Path("/Users/ryanrose/Downloads/Claude")
BLOGS_BASE = REPO / "Rose Homes LV/Content/Claude Blogs"
LIST_FILE = HERE / "fix-blog-links-slugs.txt"
LOG_FILE = HERE / "fix-blog-links-log.txt"


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# Reuse the proven Lofty helpers from the local news fixer, and the
# markdown conversion from publish.py, so behavior matches what's live.
ln = _load("fixln", REPO / "_System/plugins/local-news-plugin/fix-local-news-blogs.py")
pub = _load("pub", HERE / "publish.py")


# ─── Slug list ───────────────────────────────────────────────────────────────

def slug_for_file(path):
    text = path.read_text(encoding="utf-8", errors="ignore")
    m = re.search(r'"@id"\s*:\s*"https?://(?:www\.)?rosehomeslv\.com/blogs?/([a-z0-9\-]+)"', text)
    if m:
        return m.group(1)
    return None


_seo_cache = {}


def slug_from_seo(path):
    """Fallback: map a file to its slug the same way publish.py does."""
    d = path.parent
    if d not in _seo_cache:
        m = {}
        try:
            by_num, by_slug = {}, set()
            for batch_num, seo_file in pub.find_seo_files(d).items():
                for n, fields in pub.parse_seo_package(seo_file).items():
                    if fields.get("slug"):
                        s = fields["slug"].strip("/").split("/")[-1]
                        by_num[n if n > 5 else (batch_num - 1) * 5 + n] = s
                        by_slug.add(s)
            for num, f in pub.find_blog_files(d):
                if num in by_num:
                    m[f.name] = by_num[num]
            for f in d.glob("*.html"):
                stem = re.sub(r'^(?:post|blog|batch\d+-post|seller)?-?\d+-', '', f.stem)
                if f.name not in m and stem in by_slug:
                    m[f.name] = stem
        except Exception:
            pass
        _seo_cache[d] = m
    return _seo_cache[d].get(path.name)


def build_list():
    out = subprocess.run(
        ["git", "-C", str(REPO), "diff", "--name-only", "--", str(BLOGS_BASE)],
        capture_output=True, text=True).stdout.splitlines()
    rows, missing = [], []
    for rel in out:
        p = REPO / rel
        if p.suffix != ".html" or not p.exists() or "seo-package" in p.name:
            continue
        diff = subprocess.run(["git", "-C", str(REPO), "diff", "--", rel],
                              capture_output=True, text=True).stdout
        if "/blogs/" not in diff:
            continue
        slug = slug_for_file(p) or slug_from_seo(p)
        if slug:
            rows.append(f"{slug}\t{p.parent.name}")
        else:
            missing.append(rel)
    rows = sorted(set(rows))
    LIST_FILE.write_text("\n".join(rows) + "\n")
    print(f"Wrote {len(rows)} slugs to {LIST_FILE}")
    if missing:
        print(f"{len(missing)} changed files had no slug in their JSON-LD (skipped):")
        for m in missing[:20]:
            print(f"  {m}")


# ─── Source edits ────────────────────────────────────────────────────────────

FIX_LINKS_JS = r"""
var dialog = document.querySelector('.tox-dialog');
var ta = dialog && dialog.querySelector('textarea.tox-textarea');
if (!ta) { 'FAIL: no textarea'; }
else {
    var html = ta.value, original = html;
    var n = (html.match(/(rosehomeslv\.com\/blogs\/|href="\/blogs\/|\]\(\/blogs\/)/g) || []).length;
    html = html.replace(/rosehomeslv\.com\/blogs\//g, 'rosehomeslv.com/blog/')
               .replace(/href="\/blogs\//g, 'href="/blog/');
    if (html === original) { 'CLEAN'; }
    else {
        var setter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, 'value').set;
        setter.call(ta, html);
        ta.dispatchEvent(new Event('input', {bubbles: true}));
        ta.dispatchEvent(new Event('change', {bubbles: true}));
        var btns = dialog.querySelectorAll('button');
        for (var i = 0; i < btns.length; i++) { if (btns[i].textContent.trim() === 'Save') { btns[i].click(); break; } }
        'FIXED: ' + n + ' links';
    }
}
"""


def set_body_js(new_html):
    payload = json.dumps(new_html)
    return r"""
var dialog = document.querySelector('.tox-dialog');
var ta = dialog && dialog.querySelector('textarea.tox-textarea');
if (!ta) { 'FAIL: no textarea'; }
else {
    var html = """ + payload + r""";
    var setter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, 'value').set;
    setter.call(ta, html);
    ta.dispatchEvent(new Event('input', {bubbles: true}));
    ta.dispatchEvent(new Event('change', {bubbles: true}));
    var btns = dialog.querySelectorAll('button');
    for (var i = 0; i < btns.length; i++) { if (btns[i].textContent.trim() === 'Save') { btns[i].click(); break; } }
    'FIXED: body replaced';
}
"""


def open_source_dialog():
    ln.chrome_js("var t=document.getElementById('tab-0'); if(t){t.click();}")
    time.sleep(2)
    r = ln.chrome_js("var b=document.querySelector('.tox-tbtn[title=\"Source code\"]'); if(b){b.click();'OK'}else{'FAIL'}")
    if not r or "FAIL" in str(r):
        return False
    time.sleep(2)
    return ln.wait_for_element('.tox-dialog textarea.tox-textarea', timeout=10)


def local_body(folder, slug):
    d = BLOGS_BASE / folder
    for f in d.glob("*.html"):
        if (slug_for_file(f) or slug_from_seo(f)) == slug:
            _, body, _ = pub.extract_blog_data(f)
            return body
    return None


# ─── Flow ────────────────────────────────────────────────────────────────────

def fix_one(slug, folder, sync_body, report):
    print(f"\n{'='*60}\n{slug}  ({folder})\n{'='*60}")
    new_body = None
    if sync_body:
        new_body = local_body(folder, slug)
        if not new_body:
            print("  SKIP: local file not found")
            report.append((slug, "NO LOCAL FILE"))
            return
    ln.navigate_to_blog_list()
    time.sleep(2)
    found = ln.search_for_post(slug) or ln.find_post_by_scrolling(slug)
    if not found:
        print("  SKIP: not found in Lofty (maybe never published)")
        report.append((slug, "NOT FOUND"))
        return
    if not open_source_dialog():
        print("  SKIP: source code dialog did not open")
        ln.close_editor_dialog()
        report.append((slug, "SOURCE FAIL"))
        return
    res = str(ln.chrome_js(set_body_js(new_body) if sync_body else FIX_LINKS_JS))
    print(f"  {res}")
    if "CLEAN" in res:
        ln.close_editor_dialog()
        report.append((slug, "CLEAN"))
        return
    if "FIXED" not in res:
        ln.close_editor_dialog()
        report.append((slug, "EDIT FAIL"))
        return
    time.sleep(1)
    if ln.click_update():
        print("  SAVED")
        report.append((slug, "FIXED"))
    else:
        print("  UPDATE FAILED, closing")
        ln.close_editor_dialog()
        report.append((slug, "UPDATE FAIL"))
    time.sleep(3)


def parse_range(spec):
    nums = set()
    for part in spec.split(","):
        if "-" in part:
            a, b = part.split("-")
            nums.update(range(int(a), int(b) + 1))
        else:
            nums.add(int(part))
    return nums


def main():
    ap = argparse.ArgumentParser(description="Fix /blogs/ links on live Lofty posts")
    ap.add_argument("--build-list", action="store_true", help="Build the slug list from git changes")
    ap.add_argument("--posts", help="List entries to run, e.g. 1-25")
    ap.add_argument("--slug", help="Run one slug only")
    ap.add_argument("--folder", help="Folder for --slug (needed with --sync-body)")
    ap.add_argument("--sync-body", action="store_true", help="Replace the whole body with the local file")
    ap.add_argument("--tab", type=int, default=4, help="Chrome tab number (default: 4)")
    ap.add_argument("--yes", action="store_true", help="Skip confirmation")
    args = ap.parse_args()

    if args.build_list:
        build_list()
        return

    ln.TAB = f"tab {args.tab}"

    if args.slug:
        items = [(args.slug, args.folder or "")]
    else:
        if not LIST_FILE.exists():
            print("No slug list yet. Run with --build-list first.")
            sys.exit(1)
        items = [tuple((l.split("\t") + [""])[:2]) for l in LIST_FILE.read_text().splitlines() if l.strip()]
        if args.posts:
            keep = parse_range(args.posts)
            items = [it for i, it in enumerate(items, 1) if i in keep]

    print(f"{len(items)} posts to process on Chrome tab {args.tab}"
          f" ({'replace body' if args.sync_body else 'fix /blogs/ links'}).")
    if not ln_check():
        sys.exit(1)
    if not args.yes and input("Proceed? (y/n): ").strip().lower() != "y":
        return

    ln.chrome_activate()
    report = []
    for slug, folder in items:
        try:
            fix_one(slug, folder, args.sync_body, report)
        except Exception as e:  # keep going on a single bad post
            print(f"  ERROR: {e}")
            report.append((slug, f"ERROR {e}"))
        with LOG_FILE.open("a") as log:
            log.write(f"{time.strftime('%Y-%m-%d %H:%M')}\t{report[-1][0]}\t{report[-1][1]}\n")

    print(f"\n{'='*60}\nDONE")
    for status in sorted({s for _, s in report}):
        print(f"  {status}: {sum(1 for _, s in report if s == status)}")
    print(f"Log: {LOG_FILE}")


def ln_check():
    chk = getattr(pub, "check_accessibility_permission", None)
    return chk() if chk else True


if __name__ == "__main__":
    main()
