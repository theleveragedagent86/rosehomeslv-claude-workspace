#!/usr/bin/env python3
"""
Fix Local News Blogs on Lofty CMS — AppleScript + Chrome
=========================================================
Opens each published local news blog post in the Lofty CMS editor,
strips metadata blocks (category labels, datelines, bylines) from the
HTML source, and saves the update.

Usage:
    python3 fix-local-news-blogs.py 2026-05-08
    python3 fix-local-news-blogs.py 2026-05-08 --posts 1-10
    python3 fix-local-news-blogs.py 2026-05-08 --posts 5

Requirements: macOS, Google Chrome (with View > Developer > Allow JavaScript
from Apple Events enabled), logged into Lofty CMS.
"""

import sys
import os
import re
import subprocess
import argparse
import time
from pathlib import Path

# ─── Configuration ───────────────────────────────────────────────────────────

LOCAL_NEWS_BASE = Path("/Users/ryanrose/Downloads/Claude/Instagram/Local News")
LOFTY_URL = "https://cms.lofty.com/cmsnew/blog"
TAB = "tab 4"  # Which Chrome tab to use — change if needed


# ─── Data Extraction ─────────────────────────────────────────────────────────

def parse_seo_package(seo_file):
    """Parse the blog-seo-package.md file to get slugs and titles per story."""
    content = seo_file.read_text(encoding="utf-8")
    posts = {}
    sections = re.split(r'(?=###\s+Story\s+(\d+))', content)
    current_num = None
    current_text = ""
    for section in sections:
        m = re.match(r'###\s+Story\s+(\d+)', section)
        if m:
            if current_num is not None:
                posts[current_num] = extract_fields(current_text)
            current_num = int(m.group(1))
            current_text = section
        else:
            current_text += section
    if current_num is not None:
        posts[current_num] = extract_fields(current_text)
    return posts


def extract_fields(text):
    """Extract slug and title from a story section."""
    fields = {}
    m = re.search(r'\*\*Slug:\*\*\s*(.+?)(?:\n|$)', text)
    if m:
        fields["slug"] = m.group(1).strip().strip('`"').lower()
    m = re.search(r'###\s+Story\s+\d+:\s*(.+?)(?:\n|$)', text)
    if m:
        fields["title"] = m.group(1).strip()
    return fields


def get_posts_to_fix(date_dir, post_filter=None):
    """Get list of posts with slugs and titles from SEO package."""
    seo_file = date_dir / "blog-seo-package.md"
    if not seo_file.exists():
        print(f"ERROR: SEO package not found: {seo_file}")
        sys.exit(1)

    all_posts = parse_seo_package(seo_file)
    posts = []
    for num in sorted(all_posts.keys()):
        if post_filter is not None and num not in post_filter:
            continue
        data = all_posts[num]
        if not data.get("slug"):
            print(f"  WARNING: Story {num} has no slug, skipping")
            continue
        posts.append({
            "number": num,
            "slug": data["slug"],
            "title": data.get("title", f"Story {num}"),
        })
    return posts


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
    """Wait for a DOM element to exist."""
    for _ in range(timeout * 2):
        result = chrome_js(f"!!document.querySelector('{selector}')")
        if result == "true":
            return True
        time.sleep(0.5)
    return False


# ─── Lofty CMS Actions ──────────────────────────────────────────────────────

def navigate_to_blog_list():
    """Navigate to the blog list page."""
    chrome_js(f"window.location.href = '{LOFTY_URL}'")
    time.sleep(4)
    wait_for_element('button.cms-button.add', timeout=15)


def search_for_post(slug):
    """Search for a post by slug in the Lofty blog list. Returns True if found and clicked."""
    # Look for a search input on the blog list page
    search_result = chrome_js("""
    var searchInput = document.querySelector('.blog-search input, .el-input__inner[placeholder*="Search"], .el-input__inner[placeholder*="search"], input[type="search"]');
    if (searchInput) {
        searchInput.focus();
        searchInput.select ? searchInput.select() : document.execCommand('selectAll', false, null);
        'FOUND';
    } else { 'NO_SEARCH'; }
    """)

    if search_result and "FOUND" in str(search_result):
        # Type the slug into the search box
        escaped_slug = slug.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')
        chrome_js(f"""
        var searchInput = document.querySelector('.blog-search input, .el-input__inner[placeholder*="Search"], .el-input__inner[placeholder*="search"], input[type="search"]');
        if (searchInput) {{
            searchInput.focus();
            searchInput.select ? searchInput.select() : document.execCommand('selectAll', false, null);
            var setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
            setter.call(searchInput, `{escaped_slug}`);
            searchInput.dispatchEvent(new InputEvent('input', {{bubbles: true, data: `{escaped_slug}`, inputType: 'insertText'}}));
            searchInput.dispatchEvent(new Event('change', {{bubbles: true}}));
            searchInput.dispatchEvent(new KeyboardEvent('keyup', {{bubbles: true, key: 'Enter'}}));
        }}
        """)
        time.sleep(3)

    # Find and click the post row containing the slug
    escaped_slug = slug.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${').replace("'", "\\'")
    click_result = chrome_js(f"""
    var rows = document.querySelectorAll('.blog-list-item, .el-table__row, tr[class*="row"], .blog-item, .cms-blog-item');
    var found = false;
    for (var i = 0; i < rows.length; i++) {{
        var text = rows[i].textContent || '';
        var links = rows[i].querySelectorAll('a');
        var slugMatch = false;
        for (var j = 0; j < links.length; j++) {{
            if (links[j].href && links[j].href.indexOf('{escaped_slug}') !== -1) {{
                slugMatch = true;
                break;
            }}
        }}
        if (slugMatch || text.toLowerCase().indexOf('{escaped_slug}') !== -1) {{
            var clickTarget = rows[i].querySelector('a, .blog-title, .title, td:first-child');
            if (clickTarget) {{
                clickTarget.click();
                found = true;
                break;
            }} else {{
                rows[i].click();
                found = true;
                break;
            }}
        }}
    }}
    found ? 'CLICKED' : 'NOT_FOUND: rows=' + rows.length;
    """)

    if click_result and "CLICKED" in str(click_result):
        time.sleep(4)
        # Wait for the editor dialog to appear
        if wait_for_element('input[placeholder="Add a title here..."], .tox-tbtn[title="Source code"]', timeout=15):
            time.sleep(1)
            return True
    return False


def find_post_by_scrolling(slug):
    """Scroll through the blog list looking for a post by slug."""
    escaped_slug = slug.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${').replace("'", "\\'")
    for scroll_attempt in range(10):
        click_result = chrome_js(f"""
        var allElements = document.querySelectorAll('a, td, span, div');
        var found = false;
        for (var i = 0; i < allElements.length; i++) {{
            var el = allElements[i];
            var href = el.getAttribute('href') || '';
            var text = (el.textContent || '').toLowerCase();
            if (href.indexOf('{escaped_slug}') !== -1 || text.indexOf('{escaped_slug}') !== -1) {{
                el.click();
                found = true;
                break;
            }}
        }}
        found ? 'CLICKED' : 'NOT_FOUND';
        """)

        if click_result and "CLICKED" in str(click_result):
            time.sleep(4)
            if wait_for_element('input[placeholder="Add a title here..."], .tox-tbtn[title="Source code"]', timeout=15):
                time.sleep(1)
                return True

        # Scroll down to load more posts
        chrome_js("window.scrollBy(0, 500);")
        time.sleep(1.5)

    return False


def strip_metadata_from_source():
    """Open Source Code editor, strip metadata blocks, save. Returns (success, details)."""
    # Make sure we're on the Content tab
    chrome_js("document.getElementById('tab-0').click()")
    time.sleep(2)

    # Click Source code button
    r1 = chrome_js("""
    var btn = document.querySelector('.tox-tbtn[title="Source code"]');
    if (btn) { btn.click(); 'OK'; } else { 'FAIL'; }
    """)
    if not r1 or "FAIL" in str(r1):
        return False, ["Source code button not found"]
    time.sleep(2)

    # Wait for the source code dialog textarea
    if not wait_for_element('.tox-dialog textarea.tox-textarea', timeout=10):
        return False, ["Source code dialog did not open"]

    # Read current HTML, strip metadata, write back
    result = chrome_js(r"""
    var dialog = document.querySelector('.tox-dialog');
    if (!dialog) { 'FAIL: no dialog'; }
    else {
        var ta = dialog.querySelector('textarea.tox-textarea');
        if (!ta) { 'FAIL: no textarea'; }
        else {
            var html = ta.value;
            var original = html;
            var removed = [];

            // 1. Strip <span class="category-label">...</span>
            var catMatch = html.match(/<span\s+class="category-label"[^>]*>(.*?)<\/span>/is);
            if (catMatch) { removed.push('category-label'); }
            html = html.replace(/<span\s+class="category-label"[^>]*>.*?<\/span>\s*/gis, '');

            // 2. Strip <p class="dateline">...</p>
            var dateMatch = html.match(/<p\s+class="dateline"[^>]*>(.*?)<\/p>/is);
            if (dateMatch) { removed.push('dateline'); }
            html = html.replace(/<p\s+class="dateline"[^>]*>.*?<\/p>\s*/gis, '');

            // 3. Strip <div class="article-meta">...</div>
            var metaMatch = html.match(/<div\s+class="article-meta"[^>]*>(.*?)<\/div>/is);
            if (metaMatch) { removed.push('article-meta'); }
            html = html.replace(/<div\s+class="article-meta"[^>]*>.*?<\/div>\s*/gis, '');

            if (html === original) {
                'CLEAN: no metadata found';
            } else {
                // Set the cleaned HTML
                ta.focus();
                ta.select();
                var setter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, 'value').set;
                setter.call(ta, html);
                ta.dispatchEvent(new Event('input', {bubbles: true}));
                ta.dispatchEvent(new Event('change', {bubbles: true}));

                // Click Save in the dialog
                var btns = dialog.querySelectorAll('button');
                for (var i = 0; i < btns.length; i++) {
                    if (btns[i].textContent.trim() === 'Save') {
                        btns[i].click();
                        break;
                    }
                }
                'FIXED: removed ' + removed.join(', ');
            }
        }
    }
    """)

    if not result:
        return False, ["No response from Chrome"]

    result_str = str(result)
    if "CLEAN" in result_str:
        return True, ["already clean"]
    elif "FIXED" in result_str:
        time.sleep(1)
        return True, [result_str]
    else:
        return False, [result_str]


def click_update():
    """Click the Update/Post Now button to save changes to the published post."""
    # Try "Update" first (for already-published posts), then "Post Now"
    js = """
    var dialog = document.querySelector('.edit-blog-dialog');
    if (dialog) {
        var btns = dialog.querySelectorAll('button.cms-button');
        var clicked = false;
        // Try Update first
        for (var i = 0; i < btns.length; i++) {
            var t = btns[i].textContent.trim();
            if ((t === 'Update' || t === 'Post Now') && btns[i].offsetHeight > 0) {
                btns[i].click();
                clicked = t;
                break;
            }
        }
        clicked ? 'clicked: ' + clicked : 'FAIL: no Update/Post Now button found (buttons: ' + btns.length + ')';
    } else { 'FAIL: no dialog'; }
    """
    result = chrome_js(js)
    if result and "clicked" in str(result):
        time.sleep(2)
        # Handle confirmation dialog
        chrome_js("""
        var btns = document.querySelectorAll('.el-message-box__btns button, .el-dialog button');
        for (var i = 0; i < btns.length; i++) {
            var t = btns[i].textContent.trim();
            if ((t === 'OK' || t === 'Confirm' || t === 'Yes') && btns[i].offsetHeight > 0) {
                btns[i].click();
                break;
            }
        }
        """)
        time.sleep(3)
        return True
    return False


def close_editor_dialog():
    """Close any open editor dialog."""
    chrome_js("""
    var close = document.querySelector('.edit-blog-dialog .el-dialog__close');
    if (close) { close.click(); }
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
    time.sleep(2)


# ─── Fix Flow ────────────────────────────────────────────────────────────────

def fix_post(post, report):
    """Find a published post in Lofty, strip metadata from its HTML, and save."""
    label = f"Story {post['number']}: {post['title'][:50]}"
    slug = post['slug']
    print(f"\n{'='*60}")
    print(f"Fixing {label}")
    print(f"  Slug: {slug}")
    print(f"{'='*60}")

    # Step 1: Navigate to blog list
    print("  [1/4] Navigating to blog list...")
    navigate_to_blog_list()
    time.sleep(2)

    # Step 2: Find and open the post
    print(f"  [2/4] Searching for post: {slug}...")
    found = search_for_post(slug)
    if not found:
        print(f"    Search didn't find it, trying scroll...")
        found = find_post_by_scrolling(slug)
    if not found:
        print(f"  SKIP: Could not find post with slug '{slug}'")
        report.append({"post": label, "status": "NOT FOUND", "slug": slug})
        return

    # Step 3: Open source code and strip metadata
    print("  [3/4] Stripping metadata from source...")
    success, details = strip_metadata_from_source()
    for d in details:
        print(f"    {d}")

    if not success:
        print(f"  SKIP: Could not fix source code")
        close_editor_dialog()
        report.append({"post": label, "status": "SOURCE FAIL", "slug": slug})
        time.sleep(3)
        return

    if "already clean" in details[0]:
        print(f"  CLEAN: No metadata to remove")
        close_editor_dialog()
        report.append({"post": label, "status": "CLEAN", "slug": slug})
        time.sleep(3)
        return

    # Step 4: Save the updated post
    print("  [4/4] Saving update...")
    if click_update():
        print(f"  SAVED: {label}")
        report.append({"post": label, "status": "FIXED", "slug": slug})
    else:
        print(f"  UPDATE FAILED — closing dialog")
        close_editor_dialog()
        report.append({"post": label, "status": "UPDATE FAIL", "slug": slug})

    time.sleep(4)


# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Fix local news blog posts on Lofty CMS — strip metadata blocks",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 fix-local-news-blogs.py 2026-05-08                Fix all 20 stories
  python3 fix-local-news-blogs.py 2026-05-08 --posts 1-10   Fix stories 1-10
  python3 fix-local-news-blogs.py 2026-05-08 --posts 5      Fix one story
        """
    )
    parser.add_argument("date", help="Date folder (YYYY-MM-DD)")
    parser.add_argument("--posts", help="Story numbers: '1-10' or '1,5,8'")
    parser.add_argument("--tab", type=int, default=4, help="Chrome tab number (default: 4)")
    parser.add_argument("--yes", action="store_true", help="Skip confirmation prompts")
    args = parser.parse_args()

    global TAB
    TAB = f"tab {args.tab}"

    date_dir = LOCAL_NEWS_BASE / args.date
    if not date_dir.exists():
        print(f"ERROR: Date folder not found: {date_dir}")
        print(f"\nAvailable dates:")
        for d in sorted(LOCAL_NEWS_BASE.iterdir()):
            if d.is_dir() and re.match(r'\d{4}-\d{2}-\d{2}', d.name):
                print(f"  {d.name}")
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

    posts = get_posts_to_fix(date_dir, post_filter)
    if not posts:
        print("ERROR: No posts found to fix")
        sys.exit(1)

    print(f"\nFound {len(posts)} posts to fix on Lofty:")
    for p in posts:
        print(f"  Story {p['number']}: {p['title'][:60]}")
        print(f"    Slug: {p['slug']}")

    print(f"\nUsing Chrome {TAB}")
    print("Make sure you're logged into Lofty and on the blog dashboard.")
    if not args.yes:
        confirm = input("Proceed? (y/n): ").strip().lower()
        if confirm != "y":
            print("Cancelled.")
            return

    chrome_activate()

    report = []
    for post in posts:
        fix_post(post, report)

    print(f"\n{'='*60}")
    print(f"DONE — {len(posts)} posts processed")
    print(f"{'='*60}")
    fixed = sum(1 for r in report if r["status"] == "FIXED")
    clean = sum(1 for r in report if r["status"] == "CLEAN")
    failed = sum(1 for r in report if r["status"] not in ("FIXED", "CLEAN"))
    print(f"Fixed: {fixed} | Already clean: {clean} | Failed: {failed}")
    for r in report:
        icon = "OK" if r["status"] in ("FIXED", "CLEAN") else "!!"
        print(f"  [{icon}] {r['post']} — {r['status']} — /blog/{r['slug']}")


if __name__ == "__main__":
    main()
