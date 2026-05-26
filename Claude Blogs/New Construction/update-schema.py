#!/usr/bin/env python3
"""
Lofty CMS Schema Updater — AppleScript + Chrome
=================================================
Updates existing blog posts in the Lofty CMS to add JSON-LD schema markup.
Reads the schema block from local HTML files and appends it to each published
post via the CMS Source Code editor.

Usage:
    python3 update-schema.py                        Update all 60 posts
    python3 update-schema.py --dry-run               Show what would be updated
    python3 update-schema.py --start 15              Resume from post #15
    python3 update-schema.py --tab 3                 Use Chrome tab 3
    python3 update-schema.py --start 5 --end 10      Update posts 5-10 only

Requirements: macOS, Google Chrome (with View > Developer > Allow JavaScript
from Apple Events enabled), logged into Lofty CMS.
"""

import sys
import os
import re
import json
import subprocess
import argparse
import time
from pathlib import Path

# ─── Configuration ───────────────────────────────────────────────────────────

BLOGS_DIR = Path("/Users/ryanrose/Downloads/Claude/Claude Blogs/New Construction")
CMS_URL = "https://cms.lofty.com/cmsnew/blog?sp=post"
TAB = "tab 4"  # Which Chrome tab to use — change with --tab flag

# ─── Chrome Control via AppleScript ──────────────────────────────────────────

def chrome_js(js_code, timeout=30):
    """Execute JS in Chrome tab via AppleScript using temp file."""
    tmp = Path("/tmp/lofty-schema-js-cmd.js")
    tmp.write_text(js_code)

    applescript = f'''
    set jsCode to read POSIX file "{str(tmp)}"
    tell application "Google Chrome"
        tell {TAB} of window 1
            execute javascript jsCode
        end tell
    end tell
    '''
    try:
        result = subprocess.run(
            ['osascript', '-e', applescript],
            capture_output=True, text=True, timeout=timeout
        )
        out = result.stdout.strip()
        if out == "missing value":
            return None
        return out
    except subprocess.TimeoutExpired:
        print("    WARNING: Chrome JS execution timed out")
        return None
    except Exception as e:
        print(f"    WARNING: Chrome JS error: {e}")
        return None


def chrome_activate():
    """Bring Chrome to foreground."""
    subprocess.run(
        ['osascript', '-e', 'tell application "Google Chrome" to activate'],
        capture_output=True
    )
    time.sleep(0.3)


def wait_for_element(selector, timeout=10):
    """Wait for a DOM element to exist."""
    escaped_selector = selector.replace("'", "\\'")
    for _ in range(timeout * 2):
        result = chrome_js(f"!!document.querySelector('{escaped_selector}')")
        if result == "true":
            return True
        time.sleep(0.5)
    return False


def wait_for_element_gone(selector, timeout=10):
    """Wait for a DOM element to disappear."""
    escaped_selector = selector.replace("'", "\\'")
    for _ in range(timeout * 2):
        result = chrome_js(f"!document.querySelector('{escaped_selector}')")
        if result == "true":
            return True
        time.sleep(0.5)
    return False


# ─── Schema Extraction ──────────────────────────────────────────────────────

def extract_schema_block(html_file):
    """Extract the JSON-LD schema block from a local HTML file.
    Returns the full <script type="application/ld+json">...</script> string,
    or None if not found.
    """
    content = html_file.read_text(encoding="utf-8")
    m = re.search(
        r'(<script\s+type=["\']application/ld\+json["\']>.*?</script>)',
        content,
        re.DOTALL | re.IGNORECASE
    )
    if m:
        return m.group(1)
    return None


def extract_schema_data(schema_block):
    """Parse JSON-LD block and return the JSON data dict."""
    m = re.search(
        r'<script\s+type=["\']application/ld\+json["\']>\s*(.*?)\s*</script>',
        schema_block,
        re.DOTALL | re.IGNORECASE
    )
    if m:
        try:
            return json.loads(m.group(1))
        except json.JSONDecodeError:
            return None
    return None


def extract_slug_from_schema(schema_data):
    """Extract the URL slug from the schema's mainEntityOfPage @id field."""
    if not schema_data:
        return None
    main_entity = schema_data.get("mainEntityOfPage", {})
    page_id = main_entity.get("@id", "")
    # URL like: https://www.rosehomeslv.com/blog/some-slug-here
    m = re.search(r'/blog/([^/\s]+)$', page_id)
    if m:
        return m.group(1)
    return None


def extract_title_from_file(html_file):
    """Extract the H1 title from a local HTML file."""
    content = html_file.read_text(encoding="utf-8")
    # Try markdown H1
    m = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if m:
        return m.group(1).strip()
    # Try HTML h1
    m = re.search(r'<h1[^>]*>(.+?)</h1>', content, re.IGNORECASE | re.DOTALL)
    if m:
        return re.sub(r'<[^>]+>', '', m.group(1)).strip()
    # Try title tag
    m = re.search(r'<title>(.+?)</title>', content, re.IGNORECASE)
    if m:
        return re.sub(r'<[^>]+>', '', m.group(1)).strip()
    return None


def extract_headline_from_schema(schema_data):
    """Extract the headline from the schema data."""
    if schema_data:
        return schema_data.get("headline")
    return None


# ─── Slug Matching ──────────────────────────────────────────────────────────

def normalize_slug(slug):
    """Remove trailing numbers (like '1' or '2') that the CMS may have
    appended to disambiguate duplicate slugs.
    e.g. 'cancel-new-construction-contract-las-vegas1' -> 'cancel-new-construction-contract-las-vegas'
    """
    if not slug:
        return slug
    # Remove trailing single digits that were appended (not part of years like 2026)
    # Pattern: slug ends with a single digit that is NOT preceded by a digit
    m = re.match(r'^(.+?)(\d)$', slug)
    if m:
        base = m.group(1)
        digit = m.group(2)
        # Make sure we're not stripping digits from years (e.g., 2026)
        # If the base ends with a digit, this trailing digit is part of a number
        if base and not base[-1].isdigit():
            return base
    return slug


def match_slugs(published_slug, local_slug):
    """Check if a published CMS slug matches a local file slug.
    Handles cases where the CMS appended a number or suffix to disambiguate.
    """
    if not published_slug or not local_slug:
        return False
    if published_slug == local_slug:
        return True
    # Try normalizing the published slug
    if normalize_slug(published_slug) == local_slug:
        return True
    # Try normalizing both
    if normalize_slug(published_slug) == normalize_slug(local_slug):
        return True
    # Check if one is a prefix of the other (CMS may append digits like "2026" → "20261")
    if published_slug.startswith(local_slug) or local_slug.startswith(published_slug):
        return True
    return False


# ─── Build Post Mapping ────────────────────────────────────────────────────

def build_post_data():
    """Read all local HTML files, extract schema blocks and metadata.
    Returns a list of dicts with: file, title, headline, slug, schema_block.
    """
    posts = []
    html_files = sorted(BLOGS_DIR.glob("batch*.html"))

    for html_file in html_files:
        schema_block = extract_schema_block(html_file)
        if not schema_block:
            print(f"  WARNING: No schema found in {html_file.name} — skipping")
            continue

        schema_data = extract_schema_data(schema_block)
        slug = extract_slug_from_schema(schema_data)
        title = extract_title_from_file(html_file)
        headline = extract_headline_from_schema(schema_data)

        # Use headline from schema (typically what the CMS post title is)
        # Fall back to the H1 title from the file
        search_title = headline or title

        if not search_title:
            print(f"  WARNING: No title found in {html_file.name} — skipping")
            continue

        if not slug:
            print(f"  WARNING: No slug found in {html_file.name} — skipping")
            continue

        # Compute post number from filename
        m = re.match(r'batch(\d+)-post(\d+)', html_file.stem)
        if m:
            batch = int(m.group(1))
            post_in_batch = int(m.group(2))
            post_num = (batch - 1) * 5 + post_in_batch
        else:
            post_num = 0

        posts.append({
            "number": post_num,
            "file": html_file.name,
            "title": search_title,
            "slug": slug,
            "schema_block": schema_block,
        })

    posts.sort(key=lambda x: x["number"])
    return posts


# ─── CMS Actions ────────────────────────────────────────────────────────────

def navigate_to_blog_list():
    """Navigate to the CMS blog list page."""
    chrome_js(f"window.location.href = '{CMS_URL}';")
    time.sleep(3)
    # Wait for the blog list table to load
    wait_for_element('input[placeholder="Search"]', timeout=15)
    time.sleep(1)


def search_for_post(title):
    """Type the post title into the CMS search box and press Enter to filter.
    Returns True if search was executed and at least one result found.
    """
    # Clear any existing search first
    clear_js = """
    var searchInput = document.querySelector('input[placeholder="Search"]');
    if (searchInput) {
        searchInput.focus();
        var setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
        setter.call(searchInput, '');
        searchInput.dispatchEvent(new Event('input', {bubbles: true}));
        searchInput.dispatchEvent(new KeyboardEvent('keyup', {key: 'Enter', keyCode: 13, bubbles: true}));
        'cleared';
    } else { 'FAIL: no search input'; }
    """
    result = chrome_js(clear_js)
    if not result or "FAIL" in str(result):
        print("    WARNING: Could not clear search box")
        return False
    time.sleep(2)

    # Use a truncated search term — just the first few distinctive words
    search_term = title[:60] if len(title) > 60 else title
    escaped = search_term.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')

    search_js = f"""
    var searchInput = document.querySelector('input[placeholder="Search"]');
    if (searchInput) {{
        searchInput.focus();
        var setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
        setter.call(searchInput, `{escaped}`);
        searchInput.dispatchEvent(new Event('input', {{bubbles: true}}));
        searchInput.dispatchEvent(new Event('change', {{bubbles: true}}));
        // Must press Enter to trigger search
        searchInput.dispatchEvent(new KeyboardEvent('keydown', {{key: 'Enter', keyCode: 13, bubbles: true}}));
        searchInput.dispatchEvent(new KeyboardEvent('keyup', {{key: 'Enter', keyCode: 13, bubbles: true}}));
        searchInput.dispatchEvent(new KeyboardEvent('keypress', {{key: 'Enter', keyCode: 13, bubbles: true}}));
        'OK: searched';
    }} else {{ 'FAIL: no search input'; }}
    """
    result = chrome_js(search_js)
    if not result or "FAIL" in str(result):
        print("    WARNING: Could not type into search box")
        return False

    time.sleep(3)  # Wait for search results to filter

    # Verify we got results
    count_js = """
    var items = document.querySelectorAll('li.list-item');
    items.length + ' results';
    """
    count = chrome_js(count_js)
    if count and "0 results" in str(count):
        print(f"    WARNING: No search results found for this title")
        return False
    print(f"    Search results: {count}")
    return True


def click_edit_button():
    """Click the edit (pencil) icon on the first blog list item.
    Lofty uses li.list-item rows with .icon-edit1 in a .op div.
    Returns True if the editor opened.
    """
    edit_js = """
    var row = document.querySelector('li.list-item');
    if (!row) { 'FAIL: no list-item rows found'; }
    else {
        var editIcon = row.querySelector('.icon-edit1');
        if (!editIcon) { 'FAIL: no .icon-edit1 in row'; }
        else {
            var editSpan = editIcon.closest('span') || editIcon;
            editSpan.click();
            'OK: clicked edit';
        }
    }
    """
    result = chrome_js(edit_js)

    if result and "OK" in str(result):
        time.sleep(3)
        # Wait for the BLOG EDITOR dialog to appear
        if wait_for_element('.tox-editor-header, .tox-tbtn[title="Source code"]', timeout=15):
            return True
        else:
            print("    WARNING: Editor dialog did not appear after clicking edit")
            return False

    print(f"    WARNING: Could not find edit button: {result}")
    return False


def open_source_code_editor():
    """Click the 'Source code' button in the TinyMCE toolbar.
    Returns True if the source code dialog opened.
    """
    # Wait for TinyMCE toolbar
    if not wait_for_element('.tox-tbtn[title="Source code"]', timeout=10):
        print("    WARNING: Source code button not found in toolbar")
        return False

    result = chrome_js("""
    var btn = document.querySelector('.tox-tbtn[title="Source code"]');
    if (btn) { btn.click(); 'OK'; } else { 'FAIL'; }
    """)
    if not result or "FAIL" in str(result):
        return False

    time.sleep(1)
    # Wait for the source code dialog
    if not wait_for_element('.tox-dialog textarea.tox-textarea', timeout=10):
        print("    WARNING: Source code dialog textarea did not appear")
        return False

    return True


def read_source_code():
    """Read the current HTML from the source code dialog textarea.
    Returns the HTML string, or None if failed.
    """
    result = chrome_js("""
    var dialog = document.querySelector('.tox-dialog');
    if (dialog) {
        var ta = dialog.querySelector('textarea.tox-textarea');
        if (ta) {
            ta.value;
        } else { 'FAIL: no textarea'; }
    } else { 'FAIL: no dialog'; }
    """)
    if result and "FAIL" not in str(result):
        return result
    return None


def has_existing_schema(html_content):
    """Check if the HTML content already contains a JSON-LD schema block."""
    if not html_content:
        return False
    return 'application/ld+json' in html_content


def append_schema_to_source(schema_block):
    """Append the schema block to the source code textarea and click Save.
    Returns True if successful.
    """
    # Escape the schema block for JS template literal
    escaped_schema = schema_block.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')

    # Write schema to a hidden element to avoid escaping issues
    chrome_js(f"""
    var tmp = document.getElementById('__lofty_schema_tmp');
    if (!tmp) {{
        tmp = document.createElement('textarea');
        tmp.id = '__lofty_schema_tmp';
        tmp.style.display = 'none';
        document.body.appendChild(tmp);
    }}
    tmp.value = `{escaped_schema}`;
    'injected';
    """)
    time.sleep(0.3)

    # Read current content, append schema, set new content, click Save
    result = chrome_js("""
    (function() {
        var dialog = document.querySelector('.tox-dialog');
        if (!dialog) return 'FAIL: no dialog';
        var ta = dialog.querySelector('textarea.tox-textarea');
        var schemaBlock = document.getElementById('__lofty_schema_tmp').value;
        if (!ta || !schemaBlock) return 'FAIL: no textarea or schema';
        var currentHTML = ta.value;
        var newHTML = currentHTML + '\\n' + schemaBlock;
        var setter = Object.getOwnPropertyDescriptor(
            window.HTMLTextAreaElement.prototype, 'value'
        ).set;
        setter.call(ta, newHTML);
        ta.dispatchEvent(new Event('input', {bubbles: true}));
        ta.dispatchEvent(new Event('change', {bubbles: true}));
        var btns = dialog.querySelectorAll('button');
        for (var i = 0; i < btns.length; i++) {
            if (btns[i].textContent.trim() === 'Save') {
                btns[i].click();
                return 'OK: appended schema, len=' + newHTML.length;
            }
        }
        return 'FAIL: no Save button found';
    })();
    """)

    if result and "OK" in str(result):
        time.sleep(1)
        return True
    print(f"    Source code save result: {result}")
    return False


def save_post_update():
    """Click the Publish button on the post editor dialog.
    Lofty editor has: Cancel, Save as Draft, Preview, Publish.
    Returns True if successful.
    """
    result = chrome_js("""
    (function() {
        var btns = document.querySelectorAll('.el-dialog__wrapper button, .el-dialog button');
        var buttonTexts = [];
        for (var i = 0; i < btns.length; i++) {
            var t = btns[i].textContent.trim();
            buttonTexts.push(t);
            if ((t === 'Publish' || t === 'Update' || t === 'Save' || t === 'Post Now') && btns[i].offsetHeight > 0) {
                btns[i].click();
                return 'OK: clicked ' + t;
            }
        }
        return 'FAIL: no Publish/Save button. Found: ' + buttonTexts.join(', ');
    })();
    """)

    if result and "OK" in str(result):
        time.sleep(2)
        # Handle confirmation dialog if one appears
        chrome_js("""
        (function() {
            var btns = document.querySelectorAll('.el-message-box__btns button, .el-dialog button');
            for (var i = 0; i < btns.length; i++) {
                var t = btns[i].textContent.trim();
                if ((t === 'OK' || t === 'Confirm' || t === 'Yes') && btns[i].offsetHeight > 0) {
                    btns[i].click();
                    break;
                }
            }
        })();
        """)
        time.sleep(3)
        return True

    print(f"    Save result: {result}")
    return False


def close_editor_dialog():
    """Close the editor dialog by navigating back to the blog list.
    This is the most reliable way to ensure the dialog is fully closed,
    since programmatic clicks on the X button don't always work in Lofty.
    """
    # First close any TinyMCE source code dialog if open
    chrome_js("""
    (function() {
        var tinyDialog = document.querySelector('.tox-dialog');
        if (tinyDialog) {
            var cancelBtn = tinyDialog.querySelector('button.tox-button--secondary');
            if (cancelBtn) cancelBtn.click();
        }
    })();
    """)
    time.sleep(0.5)

    # Try clicking Cancel button (not X) to avoid discard confirmation
    chrome_js("""
    (function() {
        var btns = document.querySelectorAll('.el-dialog__wrapper button, .el-dialog button');
        for (var i = 0; i < btns.length; i++) {
            var t = btns[i].textContent.trim();
            if (t === 'Cancel' && btns[i].offsetHeight > 0) {
                btns[i].click();
                return 'clicked Cancel';
            }
        }
        // Fallback: click X close button
        var closeBtn = document.querySelector('.el-dialog__headerbtn');
        if (closeBtn) { closeBtn.click(); return 'clicked X'; }
        return 'no close button';
    })();
    """)
    time.sleep(1.5)

    # Handle any "discard changes" confirmation
    chrome_js("""
    (function() {
        var btns = document.querySelectorAll('.el-message-box__btns button');
        for (var i = 0; i < btns.length; i++) {
            var t = btns[i].textContent.trim();
            if (t === 'OK' || t === 'Confirm' || t === 'Yes' || t === 'Discard') {
                btns[i].click();
                return 'confirmed';
            }
        }
        return 'no confirmation needed';
    })();
    """)
    time.sleep(1)

    # Verify dialog is gone by checking for tox-editor-header
    for attempt in range(6):
        result = chrome_js("!document.querySelector('.tox-editor-header')")
        if result == "true":
            return  # Dialog is gone
        time.sleep(1)

    # If dialog still present, force reload the page to clear it
    print("    WARNING: Dialog did not close, forcing page reload...")
    chrome_js(f"window.location.href = '{CMS_URL}';")
    time.sleep(4)
    wait_for_element('li.list-item', timeout=15)


# ─── Pagination-Based Update Logic ──────────────────────────────────────────

def get_slug_from_settings():
    """Switch to Settings tab and extract the slug value.
    Returns the slug string, or None.
    """
    # Click Settings tab
    result = chrome_js("""
    (function() {
        var tabs = document.querySelectorAll('.el-dialog .el-tabs__item');
        for (var i = 0; i < tabs.length; i++) {
            if (tabs[i].textContent.trim() === 'Settings') {
                tabs[i].click();
                return 'OK';
            }
        }
        return 'FAIL: no Settings tab';
    })();
    """)
    if not result or "FAIL" in str(result):
        return None
    time.sleep(1)

    # Read the slug input value — it's the 3rd input (index 2) in the settings pane
    slug = chrome_js("""
    (function() {
        var inputs = document.querySelectorAll('.el-dialog input.el-input__inner');
        // Slug is index 2 (after title at 0, author at 1)
        if (inputs.length > 2 && inputs[2].value) {
            return inputs[2].value;
        }
        // Fallback: look for slug-like value (has hyphens, no spaces)
        for (var i = 0; i < inputs.length; i++) {
            var v = inputs[i].value;
            if (v && v.indexOf('-') !== -1 && v.length > 3 && !v.includes(' ') && !v.includes('@')) {
                return v;
            }
        }
        return 'FAIL: no slug found';
    })();
    """)
    if slug and "FAIL" not in str(slug):
        return slug.strip()
    return None


def switch_to_content_tab():
    """Switch back to the Content tab in the editor."""
    chrome_js("""
    (function() {
        var tabs = document.querySelectorAll('.el-dialog .el-tabs__item');
        for (var i = 0; i < tabs.length; i++) {
            if (tabs[i].textContent.trim() === 'Content') {
                tabs[i].click();
                return 'OK';
            }
        }
    })();
    """)
    time.sleep(1)


def close_source_code_dialog():
    """Close the TinyMCE source code dialog without saving."""
    chrome_js("""
    (function() {
        var dialog = document.querySelector('.tox-dialog');
        if (dialog) {
            var cancelBtn = dialog.querySelector('button.tox-button--secondary');
            if (cancelBtn) cancelBtn.click();
        }
    })();
    """)
    time.sleep(0.5)


def get_page_items():
    """Get all blog list items on the current CMS page.
    Returns list of dicts with index, title, category, date info.
    """
    result = chrome_js("""
    (function() {
        var items = document.querySelectorAll('li.list-item');
        var data = [];
        items.forEach(function(li, idx) {
            var titleEl = li.querySelector('.title .text');
            var title = titleEl ? titleEl.textContent.trim() : '';
            var text = li.textContent;
            // Extract category and date from the row text
            var hasNewConstruction = text.indexOf('New Construction') !== -1;
            // Look for date pattern MM/DD/YYYY
            var dateMatch = text.match(/(\\d{2}\\/\\d{2}\\/\\d{4})/);
            var pubDate = dateMatch ? dateMatch[1] : '';
            data.push({idx: idx, title: title.substring(0, 60), category_nc: hasNewConstruction, date: pubDate});
        });
        return JSON.stringify(data);
    })();
    """)
    if result:
        try:
            return json.loads(result)
        except json.JSONDecodeError:
            return []
    return []


def click_edit_by_index(idx):
    """Click the edit button on a specific list item by index.
    Returns True if editor opened.
    """
    # First make sure no editor dialog is currently open
    existing = chrome_js("!!document.querySelector('.tox-editor-header')")
    if existing == "true":
        print("    Closing stale editor before opening new one...")
        close_editor_dialog()
        time.sleep(1)

    # Mark a timestamp to detect fresh dialog
    chrome_js("window.__lofty_edit_ts = Date.now();")

    result = chrome_js(f"""
    (function() {{
        var items = document.querySelectorAll('li.list-item');
        if (items.length <= {idx}) return 'FAIL: index out of range, only ' + items.length + ' items';
        var row = items[{idx}];
        // Trigger hover to ensure edit icon is visible
        row.dispatchEvent(new MouseEvent('mouseenter', {{bubbles: true}}));
        row.dispatchEvent(new MouseEvent('mouseover', {{bubbles: true}}));
        var editIcon = row.querySelector('.icon-edit1');
        if (!editIcon) return 'FAIL: no edit icon';
        var editSpan = editIcon.closest('span') || editIcon;
        editSpan.click();
        return 'OK';
    }})();
    """)
    if result and "OK" in str(result):
        time.sleep(3)
        if wait_for_element('.tox-editor-header, .tox-tbtn[title="Source code"]', timeout=15):
            return True
        print(f"    WARNING: Editor did not appear after clicking edit on item {idx}")
    else:
        print(f"    WARNING: Could not click edit on item {idx}: {result}")
    return False


def go_to_next_page():
    """Click the next page button. Returns True if successful."""
    result = chrome_js("""
    (function() {
        var nextBtn = document.querySelector('.btn-next');
        if (nextBtn && !nextBtn.disabled) {
            nextBtn.click();
            return 'OK';
        }
        return 'FAIL: no next page or disabled';
    })();
    """)
    if result and "OK" in str(result):
        time.sleep(2)
        return True
    return False


def process_single_item(item_idx, slug_to_schema):
    """Open editor for a specific list item, identify by slug, add schema.
    Returns tuple: (status, slug_or_info).
    """
    # Step 1: Click edit
    if not click_edit_by_index(item_idx):
        return ("FAILED", "could not open editor")

    # Step 2: Get slug from Settings tab
    slug = get_slug_from_settings()
    if not slug:
        close_editor_dialog()
        return ("FAILED", "could not read slug")

    print(f"    Slug: {slug}")

    # Step 3: Match slug to local schema
    schema_block = None
    matched_slug = None
    for local_slug, schema in slug_to_schema.items():
        if match_slugs(slug, local_slug):
            schema_block = schema
            matched_slug = local_slug
            break

    if not schema_block:
        print(f"    No matching local schema for slug: {slug}")
        close_editor_dialog()
        return ("SKIPPED", slug)

    print(f"    Matched to local: {matched_slug}")

    # Step 4: Switch to Content tab and open source code
    switch_to_content_tab()

    if not open_source_code_editor():
        close_editor_dialog()
        return ("FAILED", f"could not open source code for {slug}")

    # Step 5: Check for existing schema
    current_html = read_source_code()
    if current_html is None:
        close_source_code_dialog()
        close_editor_dialog()
        return ("FAILED", f"could not read source for {slug}")

    if has_existing_schema(current_html):
        print(f"    Schema already exists — skipping")
        close_source_code_dialog()
        close_editor_dialog()
        return ("ALREADY_HAS", slug)

    # Step 6: Append schema
    if not append_schema_to_source(schema_block):
        close_editor_dialog()
        return ("FAILED", f"could not append schema for {slug}")
    print(f"    Schema appended!")

    # Step 7: Save
    time.sleep(1)
    if not save_post_update():
        close_editor_dialog()
        return ("FAILED", f"could not save {slug}")

    time.sleep(2)
    print(f"    SAVED!")
    return ("OK", slug)


# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Update Lofty CMS blog posts with JSON-LD schema markup",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Paginates through the CMS blog list and updates every New Construction
post from March 2026 onward with its matching JSON-LD schema block.

Examples:
  python3 update-schema.py                  Run the updater
  python3 update-schema.py --dry-run        Show what would be updated
  python3 update-schema.py --page 2         Start from CMS page 2
  python3 update-schema.py --tab 1          Use Chrome tab 1
        """
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Show what would be updated without making changes"
    )
    parser.add_argument(
        "--page", type=int, default=1,
        help="Start from this CMS page number (default: 1)"
    )
    parser.add_argument(
        "--max-pages", type=int, default=20,
        help="Maximum number of CMS pages to scan (default: 20)"
    )
    parser.add_argument(
        "--tab", type=int, default=1,
        help="Chrome tab number to use (default: 1)"
    )
    parser.add_argument(
        "--yes", "-y", action="store_true",
        help="Skip confirmation prompt"
    )
    args = parser.parse_args()

    global TAB
    TAB = f"tab {args.tab}"

    # ── Step 1: Build slug-to-schema mapping from local files ──
    print("\n" + "="*70)
    print("  LOFTY CMS SCHEMA UPDATER (Pagination Mode)")
    print("="*70)
    print(f"\nReading local HTML files from:\n  {BLOGS_DIR}\n")

    posts = build_post_data()
    if not posts:
        print("ERROR: No posts with schema blocks found.")
        sys.exit(1)

    # Build slug -> schema_block mapping
    slug_to_schema = {}
    for p in posts:
        slug_to_schema[p["slug"]] = p["schema_block"]

    print(f"Loaded {len(slug_to_schema)} schema blocks from local files.")
    print(f"Will scan CMS pages {args.page} through {args.page + args.max_pages - 1}.")
    print(f"Processing New Construction posts from 03/2026 onward.\n")

    if not args.yes:
        print(f"Using Chrome {TAB}")
        print("Make sure Lofty CMS blog list is open in Chrome.")
        confirm = input("\nProceed? (y/n): ").strip().lower()
        if confirm != "y":
            print("Cancelled.")
            return

    # ── Step 2: Navigate to blog list ──
    chrome_activate()
    navigate_to_blog_list()

    # If starting from a page > 1, navigate there
    if args.page > 1:
        print(f"  Navigating to page {args.page}...")
        for _ in range(args.page - 1):
            if not go_to_next_page():
                print("  ERROR: Could not navigate to target page")
                return
        time.sleep(2)

    # ── Step 3: Process pages ──
    report = []
    processed = 0
    current_page = args.page
    stop_scanning = False

    for page_num in range(args.max_pages):
        if stop_scanning:
            break

        print(f"\n{'='*70}")
        print(f"  SCANNING CMS PAGE {current_page}")
        print(f"{'='*70}")

        items = get_page_items()
        if not items:
            print("  No items found on this page — stopping.")
            break

        print(f"  Found {len(items)} items on page {current_page}")

        for item in items:
            idx = item["idx"]
            title = item["title"] or "(no title)"
            is_nc = item["category_nc"]
            pub_date = item["date"]

            # Check if this is a March 2026+ New Construction post
            if not is_nc:
                print(f"  [{idx}] {title} — not New Construction, skipping")
                continue

            # Check date — stop if before March 2026
            if pub_date:
                month = int(pub_date.split("/")[0]) if "/" in pub_date else 0
                year = int(pub_date.split("/")[2]) if pub_date.count("/") == 2 else 0
                if year < 2026 or (year == 2026 and month < 3):
                    print(f"  [{idx}] {title} — date {pub_date} before 03/2026, stopping scan")
                    stop_scanning = True
                    break

            print(f"\n  >>> [{idx}] {title} (NC, {pub_date})")
            processed += 1

            if args.dry_run:
                print(f"    [DRY RUN] Would process this post")
                report.append({"title": title, "status": "DRY_RUN", "slug": ""})
                continue

            try:
                status, info = process_single_item(idx, slug_to_schema)
            except KeyboardInterrupt:
                print("\n\nInterrupted! Resume with: python3 update-schema.py --page " + str(current_page))
                break
            except Exception as e:
                print(f"    ERROR: {e}")
                status, info = "ERROR", str(e)
                # Make sure editor is closed on error
                close_editor_dialog()

            report.append({"title": title, "status": status, "slug": info})

            # Navigate back to blog list to get a clean state
            # (the editor dialog doesn't close reliably via JS clicks)
            navigate_to_blog_list()
            # Re-navigate to current page
            if current_page > 1:
                for _ in range(current_page - 1):
                    go_to_next_page()
                time.sleep(1)
            time.sleep(2)

        # Go to next page
        if not stop_scanning and page_num < args.max_pages - 1:
            print(f"\n  Moving to page {current_page + 1}...")
            if not go_to_next_page():
                print("  No more pages — stopping.")
                break
            current_page += 1
            time.sleep(2)

    # ── Step 4: Summary ──
    print(f"\n\n{'='*70}")
    print(f"  UPDATE COMPLETE")
    print(f"{'='*70}\n")

    ok = sum(1 for r in report if r["status"] == "OK")
    skip = sum(1 for r in report if r["status"] in ("SKIPPED", "ALREADY_HAS"))
    fail = sum(1 for r in report if r["status"] == "FAILED")
    err = sum(1 for r in report if r["status"] == "ERROR")

    print(f"  Processed:      {len(report)}")
    print(f"  Schema added:   {ok}")
    print(f"  Skipped:        {skip}")
    print(f"  Failed:         {fail}")
    print(f"  Errors:         {err}")
    print()

    for r in report:
        s = r["status"]
        icon = {"OK": "OK", "ALREADY_HAS": "~~", "SKIPPED": "--", "FAILED": "XX", "ERROR": "!!"}.get(s, "??")
        print(f"  [{icon}] {r['title'][:50]} — {r['slug']}")

    if fail > 0 or err > 0:
        print(f"\nSome posts failed. You can re-run the script to retry.")


if __name__ == "__main__":
    main()
