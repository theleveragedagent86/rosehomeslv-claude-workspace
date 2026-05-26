#!/usr/bin/env python3
"""
Lofty CMS Schema Updater — AppleScript + Chrome
================================================
Updates existing blog posts on Lofty CMS by appending schema markup
to the HTML body via the Source Code editor.

Usage:
    python3 update-schema.py "Reverence" --posts 1-40
    python3 update-schema.py "Reverence" --tab 4

Requirements: macOS, Google Chrome (with View > Developer > Allow JavaScript
from Apple Events enabled), logged into Lofty CMS at the blog dashboard.
"""

import sys
import os
import re
import subprocess
import argparse
import time
from pathlib import Path

# ─── Configuration ───────────────────────────────────────────────────────────

BLOGS_BASE = Path("/Users/ryanrose/Downloads/Claude/Claude Blogs")
LOFTY_URL = "https://cms.lofty.com/cmsnew/blog"
TAB = "tab 4"

# ─── Chrome Control via AppleScript ──────────────────────────────────────────

def chrome_js(js_code):
    """Execute JS in Chrome tab via AppleScript using temp file."""
    tmp = Path("/tmp/lofty-js-cmd.js")
    tmp.write_text(js_code)
    applescript = f'''
    set jsCode to read POSIX file "{str(tmp)}"
    tell application "Google Chrome"
        tell {TAB} of window 1
            execute javascript jsCode
        end tell
    end tell
    '''
    result = subprocess.run(['osascript', '-e', applescript], capture_output=True, text=True, timeout=30)
    out = result.stdout.strip()
    if out == "missing value":
        return None
    return out


def chrome_activate():
    subprocess.run(['osascript', '-e', 'tell application "Google Chrome" to activate'], capture_output=True)
    time.sleep(0.3)


def wait_for_element(selector, timeout=10):
    for _ in range(timeout * 2):
        result = chrome_js(f"!!document.querySelector('{selector}')")
        if result == "true":
            return True
        time.sleep(0.5)
    return False


# ─── Data Extraction ─────────────────────────────────────────────────────────

def find_blog_files(community_dir, post_filter=None):
    files = []
    for f in sorted(community_dir.iterdir()):
        if f.suffix != ".html":
            continue
        if "seo-package" in f.stem:
            continue
        m = re.match(r'(?:post|blog-?)(\d+)', f.stem)
        if m:
            num = int(m.group(1))
            if post_filter is None or num in post_filter:
                files.append((num, f))
            continue
        m = re.match(r'batch(\d+)-post(\d+)', f.stem)
        if m:
            batch = int(m.group(1))
            post_in_batch = int(m.group(2))
            num = (batch - 1) * 5 + post_in_batch
            if post_filter is None or num in post_filter:
                files.append((num, f))
            continue
    files.sort(key=lambda x: x[0])
    return files


def extract_schema_block(html_file):
    """Extract just the <script type="application/ld+json">...</script> block."""
    content = html_file.read_text(encoding="utf-8")
    m = re.search(r'(<script\s+type=["\']application/ld\+json["\']>.*?</script>)',
                  content, re.DOTALL | re.IGNORECASE)
    if m:
        return m.group(1)
    return None


def extract_title(html_file):
    """Extract the blog title for matching on Lofty."""
    content = html_file.read_text(encoding="utf-8")
    m = re.search(r'<title>(.+?)</title>', content, re.IGNORECASE)
    if m:
        return re.sub(r'<[^>]+>', '', m.group(1)).strip()
    m = re.search(r'<h1[^>]*>(.+?)</h1>', content, re.IGNORECASE | re.DOTALL)
    if m:
        return re.sub(r'<[^>]+>', '', m.group(1)).strip()
    m = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if m:
        return m.group(1).strip()
    return None


# ─── Lofty CMS Actions ──────────────────────────────────────────────────────

def click_edit_post(title):
    """Find and click on a blog post by title to open its editor."""
    escaped_title = title.replace("'", "\\'").replace('"', '\\"')
    js = f"""
    var found = false;
    var all = document.querySelectorAll('a, span, div, td, p');
    for (var i = 0; i < all.length; i++) {{
        var t = all[i].textContent.trim();
        if (t === "{escaped_title}" && all[i].offsetHeight > 0) {{
            all[i].click();
            found = true;
            break;
        }}
    }}
    found ? 'clicked' : 'not found';
    """
    result = chrome_js(js)
    if result and "clicked" in str(result):
        time.sleep(3)
        return True
    return False


def append_schema_to_body(schema_block):
    """Open source code editor and append schema block to the end of HTML body."""
    chrome_js("document.getElementById('tab-0').click()")
    time.sleep(1)

    r1 = chrome_js("""
    var btn = document.querySelector('.tox-tbtn[title="Source code"]');
    if (btn) { btn.click(); 'OK'; } else { 'FAIL'; }
    """)
    if not r1 or "FAIL" in str(r1):
        return False
    time.sleep(1.5)

    # Check if schema already exists
    check = chrome_js("""
    var dialog = document.querySelector('.tox-dialog');
    if (dialog) {
        var ta = dialog.querySelector('textarea.tox-textarea');
        if (ta && ta.value.indexOf('application/ld+json') !== -1) {
            'ALREADY_HAS_SCHEMA';
        } else {
            'NO_SCHEMA';
        }
    } else { 'NO_DIALOG'; }
    """)
    if check and "ALREADY_HAS_SCHEMA" in str(check):
        chrome_js("""
        var dialog = document.querySelector('.tox-dialog');
        var close = dialog.querySelector('.tox-dialog__header button');
        if (close) close.click();
        """)
        time.sleep(0.5)
        return "SKIPPED"

    # Inject schema into hidden element
    escaped = schema_block.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')
    chrome_js(f"""
    var tmp = document.getElementById('__schema_tmp');
    if (!tmp) {{ tmp = document.createElement('textarea'); tmp.id = '__schema_tmp'; tmp.style.display='none'; document.body.appendChild(tmp); }}
    tmp.value = `{escaped}`;
    'injected';
    """)
    time.sleep(0.3)

    # Append schema to existing HTML and click Save
    r4 = chrome_js("""
    var dialog = document.querySelector('.tox-dialog');
    if (!dialog) { 'FAIL: no dialog'; }
    else {
        var ta = dialog.querySelector('textarea.tox-textarea');
        var schema = document.getElementById('__schema_tmp').value;
        if (ta) {
            var existing = ta.value;
            var newContent = existing.trimEnd() + '\\n\\n' + schema;
            var setter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, 'value').set;
            setter.call(ta, newContent);
            ta.dispatchEvent(new Event('input', {bubbles: true}));
            ta.dispatchEvent(new Event('change', {bubbles: true}));
            var btns = dialog.querySelectorAll('button');
            for (var i = 0; i < btns.length; i++) {
                if (btns[i].textContent.trim() === 'Save') {
                    btns[i].click();
                    break;
                }
            }
            'OK: appended ' + schema.length + ' chars';
        } else { 'FAIL: no textarea'; }
    }
    """)
    return r4 and "OK" in str(r4)


def click_update():
    """Click Update/Save/Post Now button to save changes."""
    js = """
    var dialog = document.querySelector('.edit-blog-dialog');
    if (dialog) {
        var btns = dialog.querySelectorAll('button.cms-button');
        for (var i = 0; i < btns.length; i++) {
            var t = btns[i].textContent.trim();
            if ((t === 'Publish' || t === 'Update' || t === 'Post Now' || t === 'Save') && btns[i].offsetHeight > 0) {
                btns[i].click();
                'clicked: ' + t;
                break;
            }
        }
    } else { 'FAIL: no dialog'; }
    """
    result = chrome_js(js)
    if result and "clicked" in str(result):
        time.sleep(2)
        chrome_js("""
        var btns = document.querySelectorAll('.el-message-box__btns button, .el-dialog button');
        for (var i = 0; i < btns.length; i++) {
            var t = btns[i].textContent.trim();
            if ((t === 'OK' || t === 'Confirm' || t === 'Yes') && btns[i].offsetHeight > 0) {
                btns[i].click(); break;
            }
        }
        """)
        time.sleep(3)
        return True
    return False


def close_editor():
    """Close the editor dialog without saving."""
    chrome_js("""
    var dialog = document.querySelector('.edit-blog-dialog, .tox-dialog');
    if (dialog) {
        var close = dialog.querySelector('.el-dialog__close, .el-icon-close, button[aria-label="Close"]');
        if (close) close.click();
    }
    """)
    time.sleep(1)
    chrome_js("""
    var btns = document.querySelectorAll('.el-message-box__btns button');
    for (var i = 0; i < btns.length; i++) {
        var t = btns[i].textContent.trim();
        if (t === 'OK' || t === 'Confirm' || t === 'Yes' || t === 'Discard') {
            btns[i].click(); break;
        }
    }
    """)
    time.sleep(1)


# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Update existing Lofty blog posts with schema markup",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 update-schema.py "Reverence" --posts 1-40
  python3 update-schema.py "Reverence" --tab 4
  python3 update-schema.py "New Construction" --posts 26-45
        """
    )
    parser.add_argument("community", help="Community/neighborhood name (folder name)")
    parser.add_argument("--posts", help="Post numbers to update: '1-40' or '1,2,3'")
    parser.add_argument("--tab", type=int, default=4, help="Chrome tab number (default: 4)")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be updated without touching Chrome")
    parser.add_argument("--yes", "-y", action="store_true", help="Skip confirmation prompt")
    args = parser.parse_args()

    global TAB
    TAB = f"tab {args.tab}"

    community_dir = BLOGS_BASE / args.community
    if not community_dir.exists():
        for d in BLOGS_BASE.iterdir():
            if d.is_dir() and d.name.lower() == args.community.lower():
                community_dir = d
                break
        else:
            print(f"ERROR: Folder not found: {community_dir}")
            sys.exit(1)

    post_filter = None
    if args.posts:
        post_filter = set()
        for part in args.posts.split(","):
            part = part.strip()
            if "-" in part:
                s, e = part.split("-")
                post_filter.update(range(int(s), int(e) + 1))
            else:
                post_filter.add(int(part))

    blog_files = find_blog_files(community_dir, post_filter)
    if not blog_files:
        print(f"ERROR: No blog files found in {community_dir}")
        sys.exit(1)

    posts = []
    for num, f in blog_files:
        schema = extract_schema_block(f)
        title = extract_title(f)
        if not schema:
            print(f"  WARNING: No schema found in {f.name}, skipping")
            continue
        if not title:
            print(f"  WARNING: No title found in {f.name}, skipping")
            continue
        posts.append({"number": num, "file": f.name, "title": title, "schema": schema})

    print(f"\nFound {len(posts)} posts to update with schema:")
    for p in posts:
        print(f"  Post {p['number']}: {p['title'][:60]}")

    if args.dry_run:
        print("\n--dry-run flag. Showing schema blocks:\n")
        for p in posts:
            print(f"--- Post {p['number']}: {p['title'][:50]} ---")
            print(p['schema'][:200] + "...")
            print()
        return

    print(f"\nUsing Chrome {TAB}")
    print("Make sure you're logged into Lofty and on the blog dashboard.")
    print("The script will search for each post by title, open it, and append the schema.\n")
    if not args.yes:
        confirm = input("Proceed? (y/n): ").strip().lower()
        if confirm != "y":
            print("Cancelled.")
            return

    chrome_activate()

    report = []
    for i, post in enumerate(posts):
        label = f"Post {post['number']}: {post['title'][:50]}"
        print(f"\n{'='*60}")
        print(f"[{i+1}/{len(posts)}] Updating: {label}")
        print(f"{'='*60}")

        # Step 1: Navigate to blog list
        print("  [1/4] Navigating to blog list...")
        chrome_js(f"window.location.href = '{LOFTY_URL}'")
        time.sleep(3)
        wait_for_element('div.title', timeout=10)

        # Step 2: Search for the post
        print(f"  [2/4] Searching for post...")
        search_title = post['title'][:40]
        escaped_search = search_title.replace("'", "\\'").replace('"', '\\"').replace('?', '')
        chrome_js(f"""
        var search = document.querySelector('.blog-list-search-input input.el-input__inner');
        if (search) {{
            search.focus();
            search.select();
            var setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
            setter.call(search, "{escaped_search}");
            search.dispatchEvent(new Event('input', {{bubbles: true}}));
            search.dispatchEvent(new Event('change', {{bubbles: true}}));
            search.dispatchEvent(new KeyboardEvent('keyup', {{bubbles: true, key: 'Enter', keyCode: 13}}));
            'searched';
        }} else {{ 'no search box'; }}
        """)
        time.sleep(3)

        # Step 3: Click edit icon for the post
        print(f"  [3/4] Opening post editor...")
        escaped_title = post['title'].replace("'", "\\'").replace('"', '\\"')
        click_result = chrome_js(f"""
        var titles = document.querySelectorAll('div.title');
        var found = false;
        for (var i = 0; i < titles.length; i++) {{
            var t = titles[i].textContent.trim();
            if (t === "{escaped_title}" && titles[i].offsetHeight > 0) {{
                var row = titles[i];
                for (var j = 0; j < 8; j++) {{ row = row.parentElement; if (!row) break; }}
                if (row) {{
                    var editBtn = row.querySelector('i.cms-icon.icon-edit1');
                    if (editBtn) {{
                        editBtn.parentElement.click();
                        found = true;
                        break;
                    }}
                }}
                if (!found) {{ titles[i].click(); found = true; break; }}
            }}
        }}
        found ? 'clicked' : 'not found (visible: ' + titles.length + ')';
        """)
        if not click_result or "clicked" not in str(click_result):
            print(f"  ERROR: Could not find post: {post['title']}")
            print(f"    Response: {click_result}")
            report.append({"post": label, "status": "FAIL"})
            continue
        time.sleep(3)


        wait_for_element('.tox-tbtn[title="Source code"]', timeout=10)

        # Step 4: Append schema
        print(f"  [4/4] Appending schema...")
        result = append_schema_to_body(post['schema'])
        if result == "SKIPPED":
            print(f"  SKIPPED: Schema already exists in this post")
            report.append({"post": label, "status": "SKIPPED"})
            close_editor()
        elif result:
            print(f"  SCHEMA APPENDED — saving...")
            time.sleep(1)
            if click_update():
                print(f"  SAVED: {label}")
                report.append({"post": label, "status": "OK"})
            else:
                print(f"  SAVE FAILED — please save manually")

                report.append({"post": label, "status": "MANUAL"})
        else:
            print(f"  ERROR: Could not append schema")
            report.append({"post": label, "status": "FAIL"})
            close_editor()

        time.sleep(2)

    # Final report
    print(f"\n{'='*60}")
    print(f"DONE — {len(posts)} posts processed")
    print(f"{'='*60}")
    ok = sum(1 for r in report if r["status"] == "OK")
    skipped = sum(1 for r in report if r["status"] == "SKIPPED")
    failed = sum(1 for r in report if r["status"] in ("FAIL", "MANUAL"))
    print(f"Updated: {ok}  |  Skipped (already had schema): {skipped}  |  Failed: {failed}")
    for r in report:
        icon = {"OK": "OK", "SKIPPED": ">>", "FAIL": "!!", "MANUAL": "??"}[r["status"]]
        print(f"  [{icon}] {r['post']}")


if __name__ == "__main__":
    main()
