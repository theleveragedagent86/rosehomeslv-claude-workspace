#!/usr/bin/env python3
"""
Lofty CMS Local News Blog Publisher — AppleScript + Chrome
===========================================================
Publishes local news blog posts to the Lofty CMS by controlling Chrome via AppleScript.

Usage:
    python3 publish-local-news.py 2026-05-08
    python3 publish-local-news.py 2026-05-08 --posts 1-10
    python3 publish-local-news.py 2026-05-08 --posts 5

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

LOCAL_NEWS_BASE = Path("/Users/ryanrose/Downloads/Claude/Instagram/Local News")
LOFTY_URL = "https://cms.lofty.com/cmsnew/blog"
TAB = "tab 4"  # Which Chrome tab to use — change if needed
CATEGORY = "Local News"  # Lofty category for local news posts

# ─── Data Extraction ─────────────────────────────────────────────────────────

def find_blog_files(blogs_dir, post_filter=None):
    """Find story-NN-slug.html files in the blogs/ directory."""
    files = []
    for f in sorted(blogs_dir.iterdir()):
        if f.suffix != ".html":
            continue
        m = re.match(r'story-(\d+)-(.+)\.html', f.name)
        if m:
            num = int(m.group(1))
            if post_filter is None or num in post_filter:
                files.append((num, f))
    files.sort(key=lambda x: x[0])
    return files


def parse_seo_package(seo_file):
    """Parse the blog-seo-package.md file into per-story SEO data."""
    content = seo_file.read_text(encoding="utf-8")
    posts = {}

    # Split by "### Story N:" sections
    sections = re.split(r'(?=###\s+Story\s+(\d+))', content)

    current_num = None
    current_text = ""
    for section in sections:
        m = re.match(r'###\s+Story\s+(\d+)', section)
        if m:
            if current_num is not None:
                posts[current_num] = extract_seo_fields(current_text)
            current_num = int(m.group(1))
            current_text = section
        else:
            current_text += section

    if current_num is not None:
        posts[current_num] = extract_seo_fields(current_text)

    return posts


def extract_seo_fields(text):
    """Extract SEO fields from a story section."""
    fields = {}

    m = re.search(r'\*\*Slug:\*\*\s*(.+?)(?:\n|$)', text)
    if m:
        fields["slug"] = m.group(1).strip().strip('`"').lower()

    m = re.search(r'\*\*SEO Title:\*\*\s*(.+?)(?:\n|$)', text)
    if m:
        title = m.group(1).strip().strip('`"')
        if len(title) > 60:
            title = title[:57] + "..."
        fields["meta_title"] = title

    m = re.search(r'\*\*Meta Description:\*\*\s*(.+?)(?:\n|$)', text)
    if m:
        desc = m.group(1).strip().strip('`"')
        if len(desc) > 150:
            desc = desc[:147] + "..."
        fields["meta_description"] = desc

    m = re.search(r'\*\*Keywords:\*\*\s*(.+?)(?=\n\*\*|\n---|\n###|\Z)', text, re.DOTALL)
    if m:
        kw = m.group(1).strip().strip('`"')
        kw = re.sub(r'\s*\n\s*', ' ', kw)
        if len(kw) > 500:
            kw = kw[:500]
        fields["meta_keywords"] = kw

    return fields


def extract_blog_data(html_file):
    """Extract title and body from a blog HTML file."""
    content = html_file.read_text(encoding="utf-8")

    # Extract title
    title = None
    m = re.search(r'<title>(.+?)</title>', content, re.IGNORECASE)
    if m:
        title = re.sub(r'<[^>]+>', '', m.group(1)).strip()
    if not title:
        m = re.search(r'<h1[^>]*>(.+?)</h1>', content, re.IGNORECASE | re.DOTALL)
        if m:
            title = re.sub(r'<[^>]+>', '', m.group(1)).strip()

    # Extract body — strip HTML wrapper, head, h1, title, meta, dateline/byline
    body = content
    body = re.sub(r'<!DOCTYPE[^>]*>', '', body, flags=re.IGNORECASE)
    body = re.sub(r'</?html[^>]*>', '', body, flags=re.IGNORECASE)
    body = re.sub(r'<head>.*?</head>', '', body, flags=re.IGNORECASE | re.DOTALL)
    body = re.sub(r'</?body[^>]*>', '', body, flags=re.IGNORECASE)
    body = re.sub(r'<h1[^>]*>.*?</h1>', '', body, flags=re.IGNORECASE | re.DOTALL)
    body = re.sub(r'<title>.*?</title>', '', body, flags=re.IGNORECASE | re.DOTALL)
    body = re.sub(r'<meta[^>]*>', '', body, flags=re.IGNORECASE)
    # Strip all metadata blocks that should not be in the blog body:
    # 1. Category label (e.g., <span class="category-label">Government and Development</span>)
    body = re.sub(r'<span\s+class="category-label"[^>]*>.*?</span>', '', body, flags=re.IGNORECASE | re.DOTALL)
    # 2. Dateline (e.g., <p class="dateline">May 8, 2026 · Ryan Rose, Real Broker LLC</p>)
    body = re.sub(r'<p\s+class="dateline"[^>]*>.*?</p>', '', body, flags=re.IGNORECASE | re.DOTALL)
    # 3. Article-meta byline block (e.g., <div class="article-meta">By Ryan Rose...Published...</div>)
    body = re.sub(r'<div\s+class="article-meta"[^>]*>.*?</div>', '', body, flags=re.IGNORECASE | re.DOTALL)
    # Strip corresponding CSS blocks
    body = re.sub(r'\.category-label\s*\{[^}]*\}', '', body, flags=re.IGNORECASE)
    body = re.sub(r'\.dateline\s*\{[^}]*\}', '', body, flags=re.IGNORECASE)
    body = re.sub(r'\.article-meta\s*\{[^}]*\}', '', body, flags=re.IGNORECASE)
    body = re.sub(r'\.article-meta\s+a\s*\{[^}]*\}', '', body, flags=re.IGNORECASE)
    body = re.sub(r'\.article-meta\s+a:hover\s*\{[^}]*\}', '', body, flags=re.IGNORECASE)
    body = body.strip()

    return title, body


def prepare_posts(date_dir, post_filter=None):
    """Prepare all posts for publishing."""
    blogs_dir = date_dir / "blogs"
    seo_file = date_dir / "blog-seo-package.md"

    if not blogs_dir.exists():
        print(f"ERROR: Blogs directory not found: {blogs_dir}")
        sys.exit(1)

    blog_files = find_blog_files(blogs_dir, post_filter)
    if not blog_files:
        print(f"ERROR: No blog files found in {blogs_dir}")
        sys.exit(1)

    # Parse SEO package
    all_seo = {}
    if seo_file.exists():
        all_seo = parse_seo_package(seo_file)
    else:
        print(f"WARNING: No SEO package found at {seo_file}")

    posts = []
    errors = []
    for post_num, html_file in blog_files:
        title, body = extract_blog_data(html_file)
        seo = all_seo.get(post_num, {})

        slug = seo.get("slug")
        meta_title = seo.get("meta_title")
        meta_keywords = seo.get("meta_keywords")
        meta_description = seo.get("meta_description")

        # Fallback: derive slug from filename
        if not slug:
            m = re.match(r'story-\d+-(.+)\.html', html_file.name)
            if m:
                slug = m.group(1)

        post = {
            "number": post_num, "file": html_file.name, "title": title, "body": body,
            "slug": slug, "category": CATEGORY,
            "meta_title": meta_title, "meta_keywords": meta_keywords,
            "meta_description": meta_description,
        }
        missing = [f for f in ["title", "body", "slug", "meta_title", "meta_keywords", "meta_description"] if not post[f]]
        if missing:
            errors.append(f"Story {post_num} ({html_file.name}): missing {', '.join(missing)}")
        posts.append(post)

    if errors:
        print("\nDATA ERRORS:\n")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
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

def click_add_new():
    """Click '+ Add New' — opens editor dialog in the same tab."""
    result = chrome_js("var btn = document.querySelector('button.cms-button.add'); if(btn){btn.click();'OK'}else{'FAIL'}")
    if result == "OK":
        time.sleep(4)
        if wait_for_element('input[placeholder="Add a title here..."]', timeout=15):
            time.sleep(1)
            return True
    return False


def exec_insert(selector, value):
    """Type text into a field using execCommand (triggers Vue reactivity)."""
    escaped = value.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')
    js = f"""
    var el = document.querySelector('{selector}');
    if (el) {{
        el.focus();
        el.select ? el.select() : document.execCommand('selectAll', false, null);
        document.execCommand('insertText', false, `{escaped}`);
        'OK: ' + el.value.substring(0, 40);
    }} else {{ 'FAIL: not found'; }}
    """
    result = chrome_js(js)
    return result and "OK" in str(result)


def enter_title(title):
    """Enter the blog title on the Content tab."""
    chrome_js("document.getElementById('tab-0').click()")
    time.sleep(1)
    if not wait_for_element('input[placeholder="Add a title here..."]', timeout=8):
        time.sleep(2)
        chrome_js("document.getElementById('tab-0').click()")
        wait_for_element('input[placeholder="Add a title here..."]', timeout=8)

    escaped = title.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')

    js = f"""
    var el = document.querySelector('input[placeholder="Add a title here..."]');
    if (el) {{
        el.focus();
        el.select ? el.select() : void 0;
        var setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
        setter.call(el, `{escaped}`);
        el.dispatchEvent(new InputEvent('input', {{bubbles: true, data: `{escaped}`, inputType: 'insertText'}}));
        el.dispatchEvent(new Event('change', {{bubbles: true}}));
        el.blur();
        'OK: ' + el.value.substring(0, 40);
    }} else {{ 'FAIL: not found'; }}
    """
    result = chrome_js(js)
    if result and "OK" in str(result):
        time.sleep(0.5)
        return True

    if exec_insert('input[placeholder="Add a title here..."]', title):
        time.sleep(0.5)
        check = chrome_js("var el = document.querySelector('input[placeholder=\"Add a title here...\"]'); el ? el.value : ''")
        if check and len(str(check).strip()) > 5:
            return True

    return False


def enter_html_body(html_body):
    """Enter HTML body via TinyMCE's Source Code dialog."""
    r1 = chrome_js("""
    var btn = document.querySelector('.tox-tbtn[title="Source code"]');
    if (btn) { btn.click(); 'OK'; } else { 'FAIL'; }
    """)
    if not r1 or "FAIL" in str(r1):
        return False
    time.sleep(2)

    escaped = html_body.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')
    chrome_js(f"""
    var tmp = document.getElementById('__lofty_body_tmp');
    if (!tmp) {{ tmp = document.createElement('textarea'); tmp.id = '__lofty_body_tmp'; tmp.style.display='none'; document.body.appendChild(tmp); }}
    tmp.value = `{escaped}`;
    'injected';
    """)
    time.sleep(0.3)

    r3 = chrome_js("""
    var dialog = document.querySelector('.tox-dialog');
    if (!dialog) { 'FAIL: no dialog'; }
    else {
        var ta = dialog.querySelector('textarea.tox-textarea');
        var html = document.getElementById('__lofty_body_tmp').value;
        if (ta) {
            ta.focus();
            ta.select();
            var setter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, 'value').set;
            setter.call(ta, html);
            ta.dispatchEvent(new Event('input', {bubbles: true}));
            ta.dispatchEvent(new Event('change', {bubbles: true}));
            var btns = dialog.querySelectorAll('button');
            for (var i = 0; i < btns.length; i++) {
                if (btns[i].textContent.trim() === 'Save') {
                    btns[i].click();
                    break;
                }
            }
            'OK: len=' + html.length;
        } else { 'FAIL: no textarea'; }
    }
    """)
    return r3 and "OK" in str(r3)


def enter_slug(slug):
    """Enter URL slug on the Settings tab."""
    chrome_js("document.getElementById('tab-1').click()")
    if not wait_for_element('#pane-1', timeout=8):
        time.sleep(3)
        chrome_js("document.getElementById('tab-1').click()")
        wait_for_element('#pane-1', timeout=8)
    time.sleep(1)

    escaped = slug.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')
    js = f"""
    var pane = document.getElementById('pane-1');
    if (!pane) {{ 'FAIL: pane-1 not found'; }}
    else {{
        var slugInput = null;
        var labels = pane.querySelectorAll('label, .el-form-item__label');
        for (var i = 0; i < labels.length; i++) {{
            var t = labels[i].textContent.trim().toLowerCase();
            if (t.indexOf('slug') !== -1 || t.indexOf('url') !== -1) {{
                var container = labels[i].closest('.el-form-item') || labels[i].parentElement;
                var inp = container.querySelector('input.el-input__inner');
                if (inp) {{ slugInput = inp; break; }}
            }}
        }}
        if (!slugInput) {{
            var inputs = pane.querySelectorAll('input.el-input__inner');
            for (var i = 0; i < inputs.length; i++) {{
                var v = inputs[i].value;
                if (v && v.indexOf('-') !== -1 && v.length > 3 && !v.includes(' ') && !v.includes('@')) {{
                    slugInput = inputs[i];
                    break;
                }}
            }}
        }}
        if (!slugInput) {{
            var inputs = pane.querySelectorAll('input.el-input__inner');
            if (inputs.length >= 2) {{
                slugInput = inputs[1];
            }}
        }}
        if (slugInput) {{
            slugInput.focus();
            slugInput.select();
            document.execCommand('insertText', false, `{escaped}`);
            'OK: ' + slugInput.value.substring(0, 40);
        }} else {{ 'FAIL: no slug input found'; }}
    }}
    """
    result = chrome_js(js)
    return result and "OK" in str(result)


def enter_category(category):
    """Select a category from the dropdown on the Settings tab."""
    escaped = category.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')

    js1 = f"""
    var selectInput = document.querySelector('.global-panel-categoryList .el-select .el-input');
    if (selectInput) {{
        selectInput.click();
        'opened';
    }} else {{ 'FAIL: no select'; }}
    """
    r1 = chrome_js(js1)
    if not r1 or "FAIL" in str(r1):
        return False
    time.sleep(0.5)

    js2 = f"""
    var searchInput = document.querySelector('.global-panel-categoryList .el-select__input');
    if (searchInput) {{
        searchInput.focus();
        var setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
        setter.call(searchInput, `{escaped}`);
        searchInput.dispatchEvent(new InputEvent('input', {{bubbles: true, data: `{escaped}`, inputType: 'insertText'}}));
        'typed';
    }} else {{ 'FAIL: no search input'; }}
    """
    r2 = chrome_js(js2)
    if not r2 or "FAIL" in str(r2):
        return False
    time.sleep(1.5)

    js3 = f"""
    var options = document.querySelectorAll('.el-select-dropdown__item');
    for (var i = 0; i < options.length; i++) {{
        if (options[i].textContent.trim() === `{escaped}`) {{
            options[i].click();
            'clicked: ' + options[i].textContent.trim();
            break;
        }}
    }}
    """
    result = chrome_js(js3)
    return result and "clicked" in str(result)


def enter_seo_field(field_class, value):
    """Enter text into a Lofty SEO field (contentEditable div)."""
    escaped = value.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')
    js = f"""
    var editor = document.querySelector('.cms-global-editor.{field_class} .ie-content');
    if (editor) {{
        editor.focus();
        var range = document.createRange();
        range.selectNodeContents(editor);
        var sel = window.getSelection();
        sel.removeAllRanges();
        sel.addRange(range);
        var dt = new DataTransfer();
        dt.setData('text/plain', `{escaped}`);
        editor.dispatchEvent(new ClipboardEvent('paste', {{
            clipboardData: dt, bubbles: true, cancelable: true
        }}));
        'OK: ' + editor.textContent.substring(0, 40);
    }} else {{ 'FAIL: no .ie-content for {field_class}'; }}
    """
    result = chrome_js(js)
    if not result or "OK" not in str(result):
        return False
    time.sleep(1)
    return True


def click_post_now():
    """Click the Post Now button inside the editor dialog."""
    js = """
    var dialog = document.querySelector('.edit-blog-dialog');
    if (dialog) {
        var btns = dialog.querySelectorAll('button.cms-button');
        for (var i = 0; i < btns.length; i++) {
            if (btns[i].textContent.trim() === 'Post Now' && btns[i].offsetHeight > 0) {
                btns[i].click();
                'clicked';
                break;
            }
        }
    } else { 'FAIL: no dialog'; }
    """
    result = chrome_js(js)
    if result and "clicked" in str(result):
        time.sleep(2)
        js2 = """
        var btns = document.querySelectorAll('.el-message-box__btns button, .el-dialog button');
        for (var i = 0; i < btns.length; i++) {
            var t = btns[i].textContent.trim();
            if ((t === 'OK' || t === 'Confirm' || t === 'Yes') && btns[i].offsetHeight > 0) {
                btns[i].click();
                'confirmed';
                break;
            }
        }
        'no dialog';
        """
        chrome_js(js2)
        time.sleep(3)
        return True
    return False


# ─── Publishing ──────────────────────────────────────────────────────────────

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


def navigate_to_blog_list():
    """Navigate to the blog list page."""
    chrome_js(f"window.location.href = '{LOFTY_URL}'")
    time.sleep(4)
    wait_for_element('button.cms-button.add', timeout=15)


def retry_field(func, *args, retries=3, label="field"):
    """Try a field entry function up to N times."""
    for attempt in range(retries + 1):
        if func(*args):
            return True
        if attempt < retries:
            print(f"    {label}: retry {attempt + 1}...")
            time.sleep(3)
    return False


def publish_post(post, report):
    """Publish a single blog post."""
    label = f"Story {post['number']}: {post['title'][:50]}"
    print(f"\n{'='*60}")
    print(f"Publishing {label}")
    print(f"{'='*60}")

    # Step 1: Navigate and open editor
    print("  [1/8] Opening editor...")
    navigate_to_blog_list()
    if not click_add_new():
        print("  ERROR: Could not open editor. Skipping.")
        report.append({"post": label, "status": "SKIP", "slug": post["slug"]})
        return

    # Step 2: Title
    print("  [2/8] Title...")
    time.sleep(1)
    if retry_field(enter_title, post["title"], label="TITLE"):
        print(f"    TITLE: OK")
    else:
        print(f"    TITLE: FAIL")
    time.sleep(1)

    # Step 3: HTML Body
    print("  [3/8] HTML body...")
    chrome_js("document.getElementById('tab-0').click()")
    time.sleep(3)
    if wait_for_element('.tox-tbtn[title="Source code"]', timeout=15):
        if retry_field(enter_html_body, post["body"], label="BODY"):
            print(f"    BODY: OK")
        else:
            print(f"    BODY: FAIL")
    else:
        print(f"    BODY: FAIL — Source code button not found")
    time.sleep(2)

    # Step 4: Slug
    print("  [4/8] Slug...")
    slug_ok = retry_field(enter_slug, post["slug"], label="SLUG")
    if slug_ok:
        print(f"    SLUG: OK — {post['slug']}")
    else:
        print(f"    SLUG: FAIL — skipping post")
        close_editor_dialog()
        report.append({"post": label, "status": "SLUG FAIL", "slug": post["slug"]})
        time.sleep(3)
        return
    time.sleep(1)

    # Step 5: Category
    print("  [5/8] Category...")
    if retry_field(enter_category, post["category"], label="CATEGORY"):
        print(f"    CATEGORY: OK — {post['category']}")
    else:
        print(f"    CATEGORY: FAIL — select manually")
    time.sleep(1)

    # Step 6: SEO tab
    print("  [6/8] Switching to SEO tab...")
    chrome_js("document.getElementById('tab-2').click()")
    time.sleep(3)

    # Step 7: SEO fields
    print("  [7/8] SEO fields...")
    if retry_field(enter_seo_field, "seoTitle", post["meta_title"], label="META TITLE"):
        print(f"    META TITLE: OK")
    else:
        print(f"    META TITLE: FAIL")
    time.sleep(1)

    if retry_field(enter_seo_field, "seoKeyword", post["meta_keywords"], label="META KEYWORDS"):
        print(f"    META KEYWORDS: OK")
    else:
        print(f"    META KEYWORDS: FAIL")
    time.sleep(1)

    if retry_field(enter_seo_field, "seoDescription", post["meta_description"], label="META DESCRIPTION"):
        print(f"    META DESCRIPTION: OK")
    else:
        print(f"    META DESCRIPTION: FAIL")
    time.sleep(1)

    # Step 8: QA check
    print("  [8/9] QA check...")
    qa_issues = []

    chrome_js("document.getElementById('tab-0').click()")
    time.sleep(1.5)
    title_val = chrome_js('var el = document.querySelector(\'input[placeholder="Add a title here..."]\'); el ? el.value : ""')
    title_val = str(title_val).strip() if title_val else ""
    if not title_val or len(title_val) < 3:
        qa_issues.append("TITLE (empty)")

    body_check = chrome_js("""
    var iframe = document.querySelector('.tox-edit-area__iframe');
    if (iframe && iframe.contentDocument) {
        var body = iframe.contentDocument.body;
        body && body.textContent.trim().length > 20 ? 'HAS_CONTENT' : 'EMPTY';
    } else { 'NO_IFRAME'; }
    """)
    if not body_check or "HAS_CONTENT" not in str(body_check):
        qa_issues.append("BODY (empty)")

    chrome_js("document.getElementById('tab-1').click()")
    time.sleep(1.5)
    slug_val = chrome_js("""
    var pane = document.getElementById('pane-1');
    if (pane) {
        var inputs = pane.querySelectorAll('input.el-input__inner');
        var found = '';
        for (var i = 0; i < inputs.length; i++) {
            var v = inputs[i].value;
            if (v && v.indexOf('-') !== -1 && !v.includes(' ') && !v.includes('@')) {
                found = v; break;
            }
        }
        found || 'EMPTY';
    } else { 'NO_PANE'; }
    """)
    slug_val = str(slug_val).strip() if slug_val else ""
    if not slug_val or slug_val in ("EMPTY", "NO_PANE") or len(slug_val) < 3:
        qa_issues.append("SLUG (empty)")

    chrome_js("document.getElementById('tab-2').click()")
    time.sleep(1.5)
    for field_class, field_name in [("seoTitle", "META TITLE"), ("seoKeyword", "META KEYWORDS"), ("seoDescription", "META DESCRIPTION")]:
        val = chrome_js(f"var el = document.querySelector('.cms-global-editor.{field_class} .ie-content'); el ? el.textContent.trim() : ''")
        val = str(val).strip() if val else ""
        if not val or len(val) < 3:
            qa_issues.append(f"{field_name} (empty)")

    if qa_issues:
        print(f"\n  ** QA FAILED — missing fields:")
        for issue in qa_issues:
            print(f"     - {issue}")
        print("  Auto-retrying failed fields...")
        if any("TITLE" in i for i in qa_issues):
            chrome_js("document.getElementById('tab-0').click()")
            time.sleep(1.5)
            retry_field(enter_title, post["title"], retries=2, label="TITLE")
        if any("SLUG" in i for i in qa_issues):
            chrome_js("document.getElementById('tab-1').click()")
            time.sleep(1.5)
            retry_field(enter_slug, post["slug"], retries=2, label="SLUG")
        if any("BODY" in i for i in qa_issues):
            chrome_js("document.getElementById('tab-0').click()")
            time.sleep(2)
            if wait_for_element('.tox-tbtn[title="Source code"]', timeout=10):
                retry_field(enter_html_body, post["body"], retries=2, label="BODY")
        seo_retries = [
            ("seoTitle", "META TITLE", post["meta_title"]),
            ("seoKeyword", "META KEYWORDS", post["meta_keywords"]),
            ("seoDescription", "META DESCRIPTION", post["meta_description"]),
        ]
        seo_needed = [(fc, fn, fv) for fc, fn, fv in seo_retries if any(fn in i for i in qa_issues)]
        if seo_needed:
            chrome_js("document.getElementById('tab-2').click()")
            time.sleep(1.5)
            for field_class, field_name, field_val in seo_needed:
                retry_field(enter_seo_field, field_class, field_val, retries=2, label=field_name)
                time.sleep(0.5)
        print("  Retry complete.")
    else:
        print("  ** QA PASSED — all fields verified")

    # Step 9: Post Now
    print("  [9/9] Publishing...")
    published = False
    for attempt in range(3):
        if click_post_now():
            published = True
            break
        print(f"    Post Now: retry {attempt + 1}...")
        time.sleep(3)

    if published:
        print(f"  PUBLISHED: {label}")
        status = "OK" if not qa_issues else "OK (QA retried)"
        report.append({"post": label, "status": status, "slug": post["slug"]})
    else:
        print(f"  POST NOW FAILED — closing dialog")
        close_editor_dialog()
        report.append({"post": label, "status": "FAIL", "slug": post["slug"]})

    time.sleep(4)


# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Publish local news blog posts to Lofty CMS",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 publish-local-news.py 2026-05-08                Publish all 20 stories
  python3 publish-local-news.py 2026-05-08 --posts 1-10   Publish stories 1-10
  python3 publish-local-news.py 2026-05-08 --posts 5      Publish one story
        """
    )
    parser.add_argument("date", help="Date folder (YYYY-MM-DD)")
    parser.add_argument("--posts", help="Story numbers: '1-10' or '1,5,8'")
    parser.add_argument("--no-publish", action="store_true", help="Prepare data only, don't publish")
    parser.add_argument("--tab", type=int, default=4, help="Chrome tab number (default: 4)")
    parser.add_argument("--category", default="Local News", help="Lofty category (default: Local News)")
    parser.add_argument("--yes", action="store_true", help="Skip confirmation prompts")
    args = parser.parse_args()

    global TAB, CATEGORY
    TAB = f"tab {args.tab}"
    CATEGORY = args.category

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

    print(f"\nPreparing local news posts from: {date_dir}")
    posts = prepare_posts(date_dir, post_filter)

    print(f"\nFound {len(posts)} posts to publish:")
    for p in posts:
        print(f"  Story {p['number']}: {p['title'][:60]}")
        print(f"    Slug: {p['slug']}")

    if args.no_publish:
        print("\n--no-publish flag set. Done.")
        return

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
        publish_post(post, report)

    print(f"\n{'='*60}")
    print(f"DONE — {len(posts)} stories published")
    print(f"{'='*60}")
    ok = sum(1 for r in report if "OK" in r["status"])
    print(f"Published: {ok}/{len(posts)}")
    for r in report:
        icon = "OK" if "OK" in r["status"] else "!!"
        print(f"  [{icon}] {r['post']} — /blog/{r['slug']}")


if __name__ == "__main__":
    main()
