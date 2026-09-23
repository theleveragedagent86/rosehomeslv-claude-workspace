#!/usr/bin/env python3
"""
Fix already-published Claude Blogs posts in Lofty — AppleScript + Chrome
=========================================================================
Opens each live post in the Lofty editor, applies one fix, and clicks Update.
Reuses the search/update steps from fix-local-news-blogs.py and the Schema tab
entry from publish-local-news.py.

Modes:
  links   Rewrite rosehomeslv.com/blogs/ to /blog/ inside the post's HTML source.
          Leaves everything else in the live post untouched.
  body    Replace the whole post body with the current local file (JSON-LD is
          stripped from the body and entered on the Schema tab instead).
  schema  Replace the live schema with the local file's JSON-LD.
          WARNING: live posts carry FAQPage and an Article image that the local
          files do not. This mode overwrites them. Run backfill_schema.py after
          it, or only use it on posts whose local schema is the newer one.

Usage:
  python3 fix-live-posts.py links "SPRING VALLEY" --yes
  python3 fix-live-posts.py body ALIANTE --posts 10 --live-title "Old Title" --yes
  python3 fix-live-posts.py schema "AEO Best Choice" --slugs best-realtor-for-investors-las-vegas --yes
  python3 fix-live-posts.py links "SPRING VALLEY" --dry-run      List posts only
  python3 fix-live-posts.py schema "AEO Best Choice" --ui --yes  Old editor method

Runs in the background: it calls Lofty's blog API through any open
cms.lofty.com tab, matches posts by SLUG, and writes only the field the mode
owns, so nothing else on the live post is disturbed. Keep using your Mac.

--ui restores the old method, which drives the Lofty editor: it opens each
post by TITLE (search box, then an exact title match on the row), retypes the
field and clicks Update. Slower, and the Lofty tab must be left alone. If
Publish does nothing there, Lofty rejected the save (error 601); the known
cause is a <script> block in the body, which links mode strips.

Requirements: macOS, Chrome with View > Developer > Allow JavaScript from
Apple Events, logged into Lofty with a tab open on cms.lofty.com.
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
LN_DIR = HERE.parent / "local-news-plugin"


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


aeo = _load("publish_aeo", HERE / "publish-aeo.py")               # body/schema prep
fx = _load("fix_local_news", LN_DIR / "fix-local-news-blogs.py")  # find + update
ln = aeo.ln                                                        # schema tab


# ---- Background-safe Chrome targeting --------------------------------------
# The shared chrome_js helpers talk to "tab N of window 1", which changes the
# moment Ryan clicks another Chrome window. This script only drives Lofty with
# page JavaScript (no keystrokes, no clicks on screen), so it can run in the
# background if it pins itself to the Lofty tab by its fixed window/tab ids.
PIN = {}
JS_FILE = Path("/tmp/lofty-fix-live-js.js")


def find_lofty_tab():
    """Return (window_id, tab_id, url) of the Lofty CMS tab, preferring the blog list."""
    r = subprocess.run(["osascript", "-e", '''
    set out to ""
    tell application "Google Chrome"
        repeat with w in windows
            repeat with t in tabs of w
                if URL of t contains "cms.lofty.com" then
                    set out to out & (id of w) & "|" & (id of t) & "|" & (URL of t) & linefeed
                end if
            end repeat
        end repeat
    end tell
    return out
    '''], capture_output=True, text=True, timeout=30)
    rows = [l.split("|", 2) for l in r.stdout.strip().splitlines() if l.count("|") >= 2]
    if not rows:
        return None
    rows.sort(key=lambda x: "/cmsnew/blog" not in x[2])
    return rows[0]


def pinned_chrome_js(js_code):
    JS_FILE.write_text(js_code)
    script = f'''
    set jsCode to read POSIX file "{JS_FILE}"
    tell application "Google Chrome"
        tell (tab id {PIN["tab"]} of window id {PIN["win"]})
            execute javascript jsCode
        end tell
    end tell
    '''
    r = subprocess.run(["osascript", "-e", script], capture_output=True, text=True, timeout=30)
    out = r.stdout.strip()
    return None if out == "missing value" else out


def pin_to_lofty():
    found = find_lofty_tab()
    if not found:
        return False
    PIN["win"], PIN["tab"], url = found
    # Every helper in both shared modules looks up chrome_js at call time
    fx.chrome_js = ln.chrome_js = pinned_chrome_js
    print(f"Pinned to Lofty tab: {url}")
    return True


def slug_for(path):
    """Numbered community files are NN-<slug>.html; AEO files are <slug>.html."""
    return re.sub(r"^\d+-", "", path.stem)


def gather(folder, mode, post_filter, slug_filter):
    files = sorted(f for f in folder.iterdir() if f.suffix == ".html")
    posts = []
    if mode == "links":
        # Only the slug is needed, so skip SEO parsing (older folders use mixed formats)
        for i, f in enumerate(files, 1):
            title = aeo.pb.extract_blog_data(f)[0]
            schema_json, _ = ln.extract_schema(f.read_text(encoding="utf-8"))
            schema = aeo.build_graph(json.loads(schema_json)) if schema_json else None
            posts.append({"number": i, "file": f.name, "slug": slug_for(f), "title": title,
                          "schema": schema})
    else:
        # Pass the number filter down: prepare() validates every file it loads
        # and exits on the first one missing JSON-LD, so a folder with a few
        # unpublishable legacy files would otherwise block fixing any post in it.
        posts = aeo.prepare(folder, "unused", post_filter)
    if post_filter:
        posts = [p for p in posts if p["number"] in post_filter]
    if slug_filter:
        posts = [p for p in posts if p["slug"] in slug_filter]
    return posts


def _norm(t):
    t = t.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
    return re.sub(r"\s+", " ", t).strip().lower()


# Finds the list row (li.list-item) whose title is exactly the post title and
# clicks that row's edit (pencil) icon. The title text itself does not open the
# editor. Exact only, so a similar title never gets edited by mistake.
# Kept pure ASCII: AppleScript reads the JS file as MacRoman.
CLICK_BY_TITLE_JS = """
(function() {
    var want = %s;
    function norm(t) {
        return (t || '').replace(/[\\u2018\\u2019]/g, "'").replace(/[\\u201c\\u201d]/g, '"')
                        .replace(/\\s+/g, ' ').trim().toLowerCase();
    }
    var rows = document.querySelectorAll('li.list-item');
    for (var i = 0; i < rows.length; i++) {
        var t = rows[i].querySelector('.title .text');
        if (!t || norm(t.getAttribute('title') || t.textContent) !== want) { continue; }
        var edit = rows[i].querySelector('.op .icon-edit1');
        if (!edit) { return 'NO_EDIT_ICON'; }
        (edit.closest('span') || edit).click();
        return 'CLICKED';
    }
    return 'NOT_FOUND: rows=' + rows.length;
})()
"""


def open_post(title):
    """Find a published post in the Lofty blog list by its title and open it."""
    want = _norm(title)
    fx.navigate_to_blog_list()
    time.sleep(2)
    # Type the title into the blog list search box (the visible one with
    # placeholder "Search"; a hidden "Search by domain name" box also exists)
    q = json.dumps(title[:60])
    fx.chrome_js(f"""
    var s = Array.from(document.querySelectorAll('input[placeholder="Search"]'))
                 .filter(function(i) {{ return i.offsetHeight > 0; }})[0];
    if (s) {{
        s.focus();
        var setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
        setter.call(s, {q});
        s.dispatchEvent(new InputEvent('input', {{bubbles: true}}));
        s.dispatchEvent(new Event('change', {{bubbles: true}}));
        ['keydown', 'keypress', 'keyup'].forEach(function(t) {{
            s.dispatchEvent(new KeyboardEvent(t, {{bubbles: true, key: 'Enter', code: 'Enter', keyCode: 13, which: 13}}));
        }});
    }}
    """)
    time.sleep(3)
    js = CLICK_BY_TITLE_JS % json.dumps(want)
    for _ in range(10):
        r = str(fx.chrome_js(js) or "")
        if r.startswith("CLICKED"):
            time.sleep(4)
            if fx.wait_for_element('input[placeholder="Add a title here..."], .tox-tbtn[title="Source code"]', timeout=15):
                time.sleep(1)
                return True
            return False
        fx.chrome_js("window.scrollBy(0, 600);")
        time.sleep(1.5)
    return False


def edit_source(js_transform):
    """Open TinyMCE's Source code dialog, run js_transform on `html`, save.

    js_transform is JS that reads `html` and assigns the new value to `html`.
    Returns 'CHANGED', 'SAME', or an error string.
    """
    fx.chrome_js("document.getElementById('tab-0').click()")
    time.sleep(2)
    if "OK" not in str(fx.chrome_js(
            "var b=document.querySelector('.tox-tbtn[title=\"Source code\"]');"
            "b ? (b.click(), 'OK') : 'FAIL'")):
        return "FAIL: Source code button not found"
    time.sleep(2)
    if not fx.wait_for_element('.tox-dialog textarea.tox-textarea', timeout=10):
        return "FAIL: source dialog did not open"
    res = fx.chrome_js(f"""
    (function() {{
        var d = document.querySelector('.tox-dialog');
        var ta = d && d.querySelector('textarea.tox-textarea');
        if (!ta) {{ return 'FAIL: no textarea'; }}
        var html = ta.value, before = html;
        {js_transform}
        var btns = d.querySelectorAll('button');
        if (html === before) {{
            for (var i = 0; i < btns.length; i++) {{
                if (btns[i].textContent.trim() === 'Cancel') {{ btns[i].click(); break; }}
            }}
            return 'SAME';
        }}
        var setter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, 'value').set;
        setter.call(ta, html);
        ta.dispatchEvent(new Event('input', {{bubbles: true}}));
        ta.dispatchEvent(new Event('change', {{bubbles: true}}));
        for (var j = 0; j < btns.length; j++) {{
            if (btns[j].textContent.trim() === 'Save') {{ btns[j].click(); break; }}
        }}
        return 'CHANGED';
    }})()
    """)
    time.sleep(1.5)
    return str(res)


def _editor_open():
    return str(fx.chrome_js(
        "var d=document.querySelector('.edit-blog-dialog'); d && d.offsetHeight > 0 ? 'OPEN' : 'CLOSED'")) == "OPEN"


def _confirm_popups():
    fx.chrome_js("""
    var b = document.querySelectorAll('.el-message-box__btns button');
    for (var i = 0; i < b.length; i++) {
        var t = b[i].textContent.trim();
        if ((t === 'OK' || t === 'Confirm' || t === 'Yes') && b[i].offsetHeight > 0) { b[i].click(); break; }
    }
    """)


def _wait_closed(seconds):
    for _ in range(seconds):
        time.sleep(1)
        _confirm_popups()
        if not _editor_open():
            return True
    return False


def save_post():
    """Click Publish (Lofty's save for a live post). True once the editor closes."""
    r = str(fx.chrome_js("""
    (function() {
        var d = document.querySelector('.edit-blog-dialog');
        if (!d) { return 'FAIL: no dialog'; }
        var btns = d.querySelectorAll('button.cms-button');
        for (var i = 0; i < btns.length; i++) {
            if (btns[i].textContent.trim() === 'Publish' && btns[i].offsetHeight > 0) {
                btns[i].click();
                return 'clicked';
            }
        }
        return 'FAIL: no Publish button';
    })()
    """) or "")
    if r != "clicked":
        print(f"  {r}")
        return False
    if _wait_closed(10):
        return True
    print("  Lofty did not accept the save. Usually a <script> left in the body.")
    return False


# Also strips any <script> block from the body. Older posts had JSON-LD pasted in
# the body, and Lofty's server now rejects every save of a body that contains a
# script (error 601, the Publish button just does nothing). The schema goes on
# the Schema tab instead.
# Same two rewrites as LINKS_JS, for the API path.
LINK_RE = re.compile(r"rosehomeslv\.com/blogs/")
SCRIPT_RE = re.compile(r"<script[\s\S]*?</script>|<p>\s*</p>", re.I)

LINKS_JS = (r"html = html.replace(/rosehomeslv\.com\/blogs\//g, 'rosehomeslv.com/blog/');"
            r" html = html.replace(/<script[\s\S]*?<\\?\/script>/gi, '').replace(/<p>\s*<\/p>/g, '');")


def fix_one(post, mode, report):
    slug = post["slug"]
    search = post.get("live_title") or post["title"]
    print(f"\n{'='*60}\n{mode.upper()}: {search}\n  slug: {slug}\n{'='*60}")
    if not open_post(search):
        print(f"  NOT FOUND in Lofty by title: {search}")
        report.append((slug, "NOT FOUND"))
        return

    changed = False
    if mode == "links":
        r = edit_source(LINKS_JS)
        print(f"  Source: {r}")
        if r.startswith("FAIL"):
            fx.close_editor_dialog()
            report.append((slug, r))
            return
        changed = r == "CHANGED"
        if changed and post.get("schema"):
            ok = ln.enter_schema(post["schema"])
            print(f"  Schema: {'OK' if ok else 'FAIL, enter it on the Schema tab by hand'}")
    elif mode == "body":
        body = json.dumps(post["body"])  # safe JS string literal
        r = edit_source(f"html = {body};")
        print(f"  Body: {r}")
        if r.startswith("FAIL"):
            fx.close_editor_dialog()
            report.append((slug, r))
            return
        changed = r == "CHANGED"
        if post.get("live_title") and _norm(post["live_title"]) != _norm(post["title"]):
            ok = ln.retry_field(ln.enter_title, post["title"], label="TITLE")
            print(f"  Title -> {post['title']}: {'OK' if ok else 'FAIL'}")
            changed = changed or ok
    if mode in ("body", "schema"):
        ok = ln.enter_schema(post["schema"])
        print(f"  Schema: {'OK' if ok else 'FAIL, enter it on the Schema tab by hand'}")
        changed = changed or ok

    if not changed:
        print("  Nothing to change")
        fx.close_editor_dialog()
        report.append((slug, "CLEAN"))
        return
    if save_post():
        print("  SAVED")
        report.append((slug, "FIXED"))
    else:
        print("  UPDATE FAILED, closing")
        fx.close_editor_dialog()
        report.append((slug, "UPDATE FAIL"))
    time.sleep(3)


def api_fix(posts, mode, dry=False):
    """Apply the fix through Lofty's API: no focus, no tab to leave alone.

    Each mode writes exactly one field. body mode deliberately does NOT touch
    customSchema or featuredImage: the live posts carry FAQ schema and featured
    images that no local file has, so re-entering local schema would undo them.
    """
    L = _load("lofty_api", HERE / "lofty_api.py")
    ids = L.find_by_slug([p["slug"] for p in posts])
    missing = [p["slug"] for p in posts if p["slug"] not in ids]
    posts = [p for p in posts if p["slug"] in ids]
    for slug in missing:
        print(f"  [!!] {slug}: NOT FOUND in Lofty")
    if not posts:
        print("\nNothing to fix.")
        return

    patches, by_id = {}, {}
    if mode == "links":
        live = L.read([ids[p["slug"]] for p in posts], fields=("content",))
        for p in posts:
            pid = ids[p["slug"]]
            html = (live.get(pid) or {}).get("content") or ""
            fixed = LINK_RE.sub("rosehomeslv.com/blog/", html)
            fixed = SCRIPT_RE.sub("", fixed)
            by_id[pid] = p["slug"]
            if fixed != html:
                patches[str(pid)] = {"content": fixed}
            else:
                print(f"  CLEAN {p['slug']}")
    else:
        field, key = ("customSchema", "schema") if mode == "schema" else ("content", "body")
        for p in posts:
            pid = ids[p["slug"]]
            by_id[pid] = p["slug"]
            if p.get(key):
                patches[str(pid)] = {field: p[key]}
            else:
                print(f"  [!!] {p['slug']}: no local {key}")

    if not patches:
        print("\nNothing to change.")
        return
    print(f"\n{'Would patch' if dry else 'Patching'} {len(patches)} posts...")
    rows = L.patch(patches, dry=dry)
    good = {"OK", "SAME", "WOULD"}
    print(f"\n{'='*60}")
    for pid, slug, status in rows:
        if status.split()[0] not in good:
            print(f"  [!!] {slug or by_id.get(int(pid), pid)}: {status}")
    st = [r[2] for r in rows]
    print(f"changed: {sum(1 for s in st if s.startswith(('OK', 'WOULD')))}"
          f"   already correct: {sum(1 for s in st if s.startswith('SAME'))}"
          f"   failed: {sum(1 for s in st if s.split()[0] not in good)}")


def main():
    ap = argparse.ArgumentParser(description="Fix already-published posts in Lofty")
    ap.add_argument("mode", choices=["links", "body", "schema"])
    ap.add_argument("folder", help="Folder under Claude Blogs")
    ap.add_argument("--posts", help="File numbers in folder order: '1-10' or '3,7'")
    ap.add_argument("--slugs", nargs="+", help="Only these slugs")
    ap.add_argument("--live-title", help="Search Lofty by this title instead of the local one "
                    "(use when the live title differs; body mode then updates it)")
    ap.add_argument("--dry-run", action="store_true",
                    help="List posts, and show what the API would change, without writing")
    ap.add_argument("--ui", action="store_true",
                    help="Old way: drive the Lofty editor in Chrome (must be left alone)")
    ap.add_argument("--yes", action="store_true")
    args = ap.parse_args()

    folder = aeo.pb.BLOGS_BASE / args.folder
    if not folder.is_dir():
        sys.exit(f"ERROR: Folder not found: {folder}")

    posts = gather(folder, args.mode, aeo.parse_filter(args.posts),
                   set(args.slugs) if args.slugs else None)
    if args.live_title:
        if len(posts) != 1:
            sys.exit("ERROR: --live-title needs exactly one post (use --posts or --slugs)")
        posts[0]["live_title"] = args.live_title
    print(f"\n{len(posts)} posts to fix ({args.mode}) in {args.folder}:")
    for p in posts:
        print(f"  {p['number']}: {p.get('live_title') or p['title']}")
    if not posts:
        return
    if not args.ui:
        if not args.dry_run and not args.yes \
                and input("Proceed? (y/n): ").strip().lower() != "y":
            return
        return api_fix(posts, args.mode, dry=args.dry_run)

    if args.dry_run:
        return
    if not args.yes and input("Proceed? (y/n): ").strip().lower() != "y":
        return
    if not pin_to_lofty():
        sys.exit("ERROR: No Chrome tab open on cms.lofty.com. Open the Lofty blog list and retry.")

    report = []
    for p in posts:
        fix_one(p, args.mode, report)

    print(f"\n{'='*60}")
    for status in ("FIXED", "CLEAN"):
        print(f"{status}: {sum(1 for _, s in report if s == status)}")
    for slug, s in report:
        if s not in ("FIXED", "CLEAN"):
            print(f"  [!!] {slug}: {s}")


if __name__ == "__main__":
    main()
