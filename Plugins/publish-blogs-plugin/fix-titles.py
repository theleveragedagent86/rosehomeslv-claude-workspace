#!/usr/bin/env python3
"""
Fix Titles — Lofty CMS
=======================
Opens each published blog post that has "no title" and enters the correct title.

Usage:
    python3 fix-titles.py "CROSSINGS IN SUMMERLIN"
    python3 fix-titles.py "CROSSINGS IN SUMMERLIN" --tab 4

Requirements: macOS, Google Chrome (with View > Developer > Allow JavaScript
from Apple Events enabled), logged into Lofty CMS at the blog dashboard.
"""

import sys
import re
import subprocess
import time
from pathlib import Path

# ─── Configuration ───────────────────────────────────────────────────────────

BLOGS_BASE = Path("/Users/ryanrose/Downloads/Claude/Claude Blogs")
LOFTY_URL = "https://cms.lofty.com/cmsnew/blog"
TAB = "tab 4"

# ─── Chrome Control ─────────────────────────────────────────────────────────

def chrome_js(js_code):
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
    time.sleep(0.5)


def wait_for_element(selector, timeout=10):
    for _ in range(timeout * 2):
        result = chrome_js(f"!!document.querySelector('{selector}')")
        if result == "true":
            return True
        time.sleep(0.5)
    return False


# ─── Title Entry Methods ─────────────────────────────────────────────────────

def enter_title_keyboard_sim(title):
    """Simulate keyboard input with full event sequence."""
    escaped = title.replace('\\', '\\\\').replace("'", "\\'").replace('\n', '')
    js = f"""
    (function() {{
        var el = document.querySelector('input[placeholder="Add a title here..."]');
        if (!el) return 'FAIL: not found';
        el.focus();
        el.dispatchEvent(new FocusEvent('focus', {{bubbles: true}}));
        el.setSelectionRange(0, el.value.length);
        var setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
        setter.call(el, '{escaped}');
        el.dispatchEvent(new Event('input', {{bubbles: true}}));
        el.dispatchEvent(new Event('change', {{bubbles: true}}));
        el.dispatchEvent(new InputEvent('input', {{
            bubbles: true, cancelable: true, inputType: 'insertText', data: '{escaped}'
        }}));
        el.dispatchEvent(new CompositionEvent('compositionend', {{
            bubbles: true, data: '{escaped}'
        }}));
        el.dispatchEvent(new FocusEvent('blur', {{bubbles: true}}));
        return 'OK: ' + el.value.substring(0, 50);
    }})()
    """
    result = chrome_js(js)
    return result and "OK" in str(result)


def enter_title_char_by_char(title):
    """Type title character by character with KeyboardEvents."""
    escaped = title.replace('\\', '\\\\').replace("'", "\\'").replace('\n', '')
    js = f"""
    (function() {{
        var el = document.querySelector('input[placeholder="Add a title here..."]');
        if (!el) return 'FAIL: not found';
        el.focus();
        el.dispatchEvent(new FocusEvent('focus', {{bubbles: true}}));
        el.value = '';
        var title = '{escaped}';
        var setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
        for (var i = 0; i < title.length; i++) {{
            var ch = title[i];
            setter.call(el, title.substring(0, i + 1));
            el.dispatchEvent(new KeyboardEvent('keydown', {{key: ch, bubbles: true}}));
            el.dispatchEvent(new InputEvent('input', {{
                bubbles: true, inputType: 'insertText', data: ch
            }}));
            el.dispatchEvent(new KeyboardEvent('keyup', {{key: ch, bubbles: true}}));
        }}
        el.dispatchEvent(new Event('change', {{bubbles: true}}));
        el.dispatchEvent(new FocusEvent('blur', {{bubbles: true}}));
        return 'OK: ' + el.value.substring(0, 50);
    }})()
    """
    result = chrome_js(js)
    return result and "OK" in str(result)


def enter_title_clipboard(title):
    """Simulate clipboard paste into the title field."""
    escaped = title.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')
    js = f"""
    (function() {{
        var el = document.querySelector('input[placeholder="Add a title here..."]');
        if (!el) return 'FAIL: not found';
        el.focus();
        el.setSelectionRange(0, el.value.length);
        var dt = new DataTransfer();
        dt.setData('text/plain', `{escaped}`);
        var pasteEvent = new ClipboardEvent('paste', {{
            clipboardData: dt, bubbles: true, cancelable: true
        }});
        el.dispatchEvent(pasteEvent);
        // If paste didn't insert, force it
        if (el.value.length < 3) {{
            var setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
            setter.call(el, `{escaped}`);
            el.dispatchEvent(new Event('input', {{bubbles: true}}));
        }}
        el.dispatchEvent(new Event('change', {{bubbles: true}}));
        el.dispatchEvent(new FocusEvent('blur', {{bubbles: true}}));
        return 'OK: ' + el.value.substring(0, 50);
    }})()
    """
    result = chrome_js(js)
    return result and "OK" in str(result)


def enter_title_execcommand(title):
    """Use execCommand insertText."""
    escaped = title.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')
    js = f"""
    (function() {{
        var el = document.querySelector('input[placeholder="Add a title here..."]');
        if (!el) return 'FAIL: not found';
        el.focus();
        el.select();
        document.execCommand('insertText', false, `{escaped}`);
        return 'OK: ' + el.value.substring(0, 50);
    }})()
    """
    result = chrome_js(js)
    return result and "OK" in str(result)


def enter_title_all_methods(title):
    """Try every method until one works."""
    methods = [
        ("keyboard sim", enter_title_keyboard_sim),
        ("execCommand", enter_title_execcommand),
        ("clipboard paste", enter_title_clipboard),
        ("char-by-char", enter_title_char_by_char),
    ]
    for name, method in methods:
        print(f"      Trying {name}...")
        if method(title):
            time.sleep(1)
            print(f"      {name}: value set")
            return True
        time.sleep(1)
    return False


# ─── Data Extraction ─────────────────────────────────────────────────────────

def get_post_titles(community_dir):
    """Extract slug-to-title mapping from blog files."""
    slug_to_title = {}
    for f in sorted(community_dir.iterdir()):
        if f.suffix != ".html":
            continue
        if f.stem.startswith("seo-package") or f.stem.startswith("SEO"):
            continue
        content = f.read_text(encoding="utf-8")

        # Get title
        title = None
        tm = re.search(r'<h1[^>]*>(.+?)</h1>', content, re.IGNORECASE | re.DOTALL)
        if tm:
            title = re.sub(r'<[^>]+>', '', tm.group(1)).strip()
        if not title:
            tm = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            if tm:
                title = tm.group(1).strip()
        if not title:
            tm = re.search(r'"headline"\s*:\s*"([^"]+)"', content)
            if tm:
                title = tm.group(1).strip()

        # Get slug from schema
        slug = None
        sm = re.search(r'"@id"\s*:\s*"https?://[^/]+/blogs/([^"]+)"', content)
        if sm:
            slug = sm.group(1).strip()
        if not slug:
            # From filename
            slug_m = re.search(r'(?:post\d+-|blog-\d+-|\d+-)(.+)$', f.stem)
            if slug_m:
                slug = slug_m.group(1)

        if title and slug:
            slug_to_title[slug] = title

    return slug_to_title


# ─── Lofty Blog List Actions ────────────────────────────────────────────────

def navigate_to_blog_list():
    chrome_js(f"window.location.href = '{LOFTY_URL}'")
    time.sleep(4)
    wait_for_element('ul.list-container', timeout=15)
    time.sleep(2)


def count_no_title():
    """Count 'no title' items visible on the page."""
    result = chrome_js("""
    (function() {
        var items = document.querySelectorAll('li.list-item');
        var noTitle = 0;
        for (var i = 0; i < items.length; i++) {
            var titleSpan = items[i].querySelector('div.title span.text');
            if (titleSpan && titleSpan.textContent.trim().toLowerCase() === 'no title') {
                noTitle++;
            }
        }
        return noTitle + '/' + items.length;
    })()
    """)
    return result


def scroll_blog_list():
    """Scroll the blog list to load more posts."""
    chrome_js("""
    (function() {
        var container = document.querySelector('.blog-list.blog-content-container') ||
                        document.querySelector('.blog-content') ||
                        document.querySelector('ul.list-container');
        if (container) {
            container.scrollTop = container.scrollHeight;
        }
        // Also try window scroll
        window.scrollTo(0, document.body.scrollHeight);
    })()
    """)
    time.sleep(2)


def click_first_no_title():
    """Click the edit icon on the first li.list-item that has 'no title'."""
    js = """
    (function() {
        var items = document.querySelectorAll('li.list-item');
        for (var i = 0; i < items.length; i++) {
            var titleSpan = items[i].querySelector('div.title span.text');
            if (titleSpan && titleSpan.textContent.trim().toLowerCase() === 'no title') {
                // Click the edit icon (pencil) inside div.op
                var editIcon = items[i].querySelector('i.icon-edit1');
                if (editIcon) {
                    // Click the parent span (el-tooltip item) which is the actual clickable
                    var editBtn = editIcon.closest('span.item') || editIcon.parentElement;
                    editBtn.click();
                    return 'clicked-edit:' + i;
                }
                // Fallback: try clicking the title span itself
                titleSpan.click();
                return 'clicked-title:' + i;
            }
        }
        return 'NONE';
    })()
    """
    result = chrome_js(js)
    if result and "clicked" in str(result):
        time.sleep(4)
        if wait_for_element('input[placeholder="Add a title here..."]', timeout=15):
            time.sleep(1)
            return True
        # Sometimes editor opens slower
        time.sleep(3)
        if wait_for_element('input[placeholder="Add a title here..."]', timeout=10):
            time.sleep(1)
            return True
    return False


def get_current_slug():
    """Read the slug from the currently open editor (Settings tab)."""
    chrome_js("document.getElementById('tab-1').click()")
    time.sleep(2)
    wait_for_element('#pane-1', timeout=8)
    time.sleep(1)

    js = """
    (function() {
        var pane = document.getElementById('pane-1');
        if (!pane) return 'FAIL: no pane-1';
        var inputs = pane.querySelectorAll('input.el-input__inner');
        // Look for slug input (has hyphens, no spaces, no @)
        for (var i = 0; i < inputs.length; i++) {
            var v = inputs[i].value;
            if (v && v.indexOf('-') !== -1 && v.length > 3 && !v.includes(' ') && !v.includes('@')) {
                return v;
            }
        }
        // Fallback: second input
        if (inputs.length >= 2) return inputs[1].value;
        return 'FAIL';
    })()
    """
    result = chrome_js(js)
    # Switch back to Content tab
    chrome_js("document.getElementById('tab-0').click()")
    time.sleep(1)
    if result and "FAIL" not in str(result):
        return result.strip()
    return None


def save_post():
    """Click Update to save the post."""
    js = """
    (function() {
        var dialog = document.querySelector('.edit-blog-dialog');
        if (!dialog) return 'FAIL: no dialog';
        var btns = dialog.querySelectorAll('button.cms-button');
        for (var i = 0; i < btns.length; i++) {
            var t = btns[i].textContent.trim();
            if ((t === 'Publish' || t === 'Update' || t === 'Post Now' || t === 'Save') && btns[i].offsetHeight > 0) {
                btns[i].click();
                return 'clicked: ' + t;
            }
        }
        // Also try any button with publish-like text
        var allBtns = dialog.querySelectorAll('button');
        for (var i = 0; i < allBtns.length; i++) {
            var t = allBtns[i].textContent.trim().toLowerCase();
            if ((t === 'publish' || t === 'update' || t === 'save' || t === 'post now') && allBtns[i].offsetHeight > 0) {
                allBtns[i].click();
                return 'clicked: ' + t;
            }
        }
        return 'FAIL: no save button';
    })()
    """
    result = chrome_js(js)
    if result and "clicked" in str(result):
        time.sleep(3)
        # Handle confirmation
        chrome_js("""
        var btns = document.querySelectorAll('.el-message-box__btns button');
        for (var i = 0; i < btns.length; i++) {
            var t = btns[i].textContent.trim();
            if (t === 'OK' || t === 'Confirm' || t === 'Yes') {
                btns[i].click(); break;
            }
        }
        """)
        time.sleep(3)
        return True
    return False


def close_editor():
    chrome_js("""
    var close = document.querySelector('.edit-blog-dialog .el-dialog__close');
    if (close) { close.click(); }
    """)
    time.sleep(2)
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


# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Fix missing blog post titles in Lofty CMS")
    parser.add_argument("community", help="Community folder name")
    parser.add_argument("--tab", type=int, default=4, help="Chrome tab number (default: 4)")
    parser.add_argument("--yes", action="store_true", help="Skip confirmation")
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

    slug_to_title = get_post_titles(community_dir)
    print(f"\nLoaded {len(slug_to_title)} slug-to-title mappings from {community_dir.name}")

    if not args.yes:
        confirm = input("Proceed? (y/n): ").strip().lower()
        if confirm != "y":
            print("Cancelled.")
            return

    chrome_activate()

    print("\nNavigating to blog list...")
    navigate_to_blog_list()

    # Scroll to load posts
    print("Loading posts...")
    for _ in range(5):
        scroll_blog_list()

    count = count_no_title()
    print(f"No-title posts on page: {count}")

    fixed = 0
    failed = 0
    skipped = 0

    for attempt in range(200):  # safety limit
        remaining = count_no_title()
        no_title_count = 0
        if remaining and '/' in str(remaining):
            no_title_count = int(remaining.split('/')[0])
        if no_title_count == 0:
            print(f"\nNo more 'no title' posts! Done.")
            break

        print(f"\n{'='*60}")
        print(f"Round {attempt + 1} — {no_title_count} 'no title' remaining")
        print(f"{'='*60}")

        # Click first no-title post
        if not click_first_no_title():
            print("  Could not open editor. Scrolling and retrying...")
            for _ in range(3):
                scroll_blog_list()
            time.sleep(2)
            if not click_first_no_title():
                print("  Still can't open. Refreshing page...")
                navigate_to_blog_list()
                for _ in range(5):
                    scroll_blog_list()
                if not click_first_no_title():
                    print("  GIVING UP on this round.")
                    failed += 1
                    if failed > 5:
                        break
                    continue

        # Read the slug to identify the post
        slug = get_current_slug()
        if not slug:
            print("  Could not read slug. Closing.")
            close_editor()
            time.sleep(2)
            failed += 1
            continue

        print(f"  Slug: {slug}")

        title = slug_to_title.get(slug)
        if not title:
            print(f"  WARNING: slug '{slug}' not in local files. Skipping.")
            close_editor()
            time.sleep(2)
            skipped += 1
            continue

        print(f"  Title: {title}")

        # Make sure we're on Content tab
        chrome_js("document.getElementById('tab-0').click()")
        time.sleep(2)
        wait_for_element('input[placeholder="Add a title here..."]', timeout=10)
        time.sleep(1)

        if enter_title_all_methods(title):
            print(f"  Saving...")
            time.sleep(1)
            if save_post():
                print(f"  FIXED!")
                fixed += 1
            else:
                print(f"  Save failed. Closing.")
                close_editor()
                failed += 1
        else:
            print(f"  ALL METHODS FAILED. Closing.")
            close_editor()
            failed += 1

        time.sleep(3)
        # Wait for the list to reappear instead of refreshing the page
        if not wait_for_element('ul.list-container', timeout=10):
            print("  List not visible, navigating back...")
            navigate_to_blog_list()
            for _ in range(3):
                scroll_blog_list()
        else:
            time.sleep(1)
            for _ in range(3):
                scroll_blog_list()
        time.sleep(1)

    print(f"\n{'='*60}")
    print(f"DONE — Fixed: {fixed} | Failed: {failed} | Skipped: {skipped}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
