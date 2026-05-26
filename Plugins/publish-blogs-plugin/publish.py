#!/usr/bin/env python3
"""
Lofty CMS Blog Publisher — AppleScript + Chrome
================================================
Publishes blog posts to the Lofty CMS by controlling Chrome via AppleScript.

Usage:
    python3 publish.py "Community Name"
    python3 publish.py "Community Name" --posts 36-40
    python3 publish.py "New Construction" --posts 110

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

BLOGS_BASE = Path("/Users/ryanrose/Downloads/Claude/Claude Blogs")
LOFTY_URL = "https://cms.lofty.com/cmsnew/blog"
TAB = "tab 4"  # Which Chrome tab to use — change if needed

# ─── Data Extraction ─────────────────────────────────────────────────────────

def find_blog_files(community_dir, post_filter=None):
    files = []
    for f in sorted(community_dir.iterdir()):
        if f.suffix != ".html":
            continue
        m = re.match(r'(?:post|blog)-?(\d+)', f.stem)
        if m:
            num = int(m.group(1))
            if post_filter is None or num in post_filter:
                files.append((num, f))
            continue
        m = re.match(r'^(\d+)-', f.stem)
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


def find_seo_files(community_dir):
    seo_files = {}
    for f in community_dir.iterdir():
        if f.stem.lower().startswith("seo-package"):
            m = re.search(r'batch-?(\d+)', f.stem, re.IGNORECASE)
            if m:
                seo_files[int(m.group(1))] = f
    return seo_files


def parse_seo_package(seo_file):
    content = seo_file.read_text(encoding="utf-8")
    posts = {}
    # Handle both plain text and HTML heading formats: "POST 1:", "### Post 1:", "<h2>Post 1:"
    sections = re.split(r'(?=(?:^|\n)(?:<h[1-6]>)?(?:#{0,3}\s*)?(?:\*\*)?POST\s+(\d+)(?:\*\*)?[\s:].)', content, flags=re.MULTILINE | re.IGNORECASE)
    current_num = None
    current_text = ""
    for section in sections:
        m = re.match(r'(?:<h[1-6]>)?(?:#{0,3}\s*)?(?:\*\*)?POST\s+(\d+)(?:\*\*)?[\s:]', section, re.IGNORECASE)
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
    fields = {}

    # Try HTML formats: <td><strong>Field</strong></td><td>value</td>
    # or <p><strong>Field:</strong> value</p>
    if '<strong>' in text:
        # Table format: <td><strong>Slug</strong></td><td>value</td>
        # Paragraph format: <p><strong>Slug:</strong> value</p>
        m = re.search(r'<strong>\s*(?:URL\s+)?Slug\s*:?\s*</strong>\s*(?:</td>\s*<td>|)\s*(.+?)\s*(?:</td>|</p>)', text, re.IGNORECASE)
        if m:
            fields["slug"] = m.group(1).strip().strip('`"').lower()

        m = re.search(r'<strong>\s*(?:SEO\s+Title|Meta\s+Title)\s*:?\s*</strong>\s*(?:</td>\s*<td>|)\s*(.+?)\s*(?:</td>|</p>)', text, re.IGNORECASE)
        if m:
            title = m.group(1).strip().strip('`"')
            if len(title) > 60:
                title = title[:57] + "..."
            fields["meta_title"] = title

        m = re.search(r'<strong>\s*(?:Meta\s+)?Keywords?\s*:?\s*</strong>\s*(?:</td>\s*<td>|)\s*(.+?)\s*(?:</td>|</p>)', text, re.IGNORECASE | re.DOTALL)
        if m:
            kw = m.group(1).strip().strip('`"')
            kw = re.sub(r'\s*\n\s*', ' ', kw)
            if len(kw) > 500:
                kw = kw[:500]
            fields["meta_keywords"] = kw

        m = re.search(r'<strong>\s*(?:Meta\s+)?Description\s*:?\s*</strong>\s*(?:</td>\s*<td>|)\s*(.+?)\s*(?:</td>|</p>)', text, re.IGNORECASE)
        if m:
            desc = m.group(1).strip().strip('`"')
            if len(desc) > 150:
                desc = desc[:147] + "..."
            fields["meta_description"] = desc

        if fields:
            return fields

    # Plain text format fallback (colon is optional to handle "**Keywords** value" format)
    m = re.search(r'^[*\-\s]*(?:URL\s+)?Slug[*]*(?:\s*\([^)]*\))?\s*:?\s*[*]*\s*(.+?)\s*[*]*$', text, re.MULTILINE | re.IGNORECASE)
    if not m:
        # Handle slug on next line: "**Slug**:\n slug-value"
        m = re.search(r'^[*\-\s]*(?:URL\s+)?Slug[*]*(?:\s*\([^)]*\))?\s*:?\s*[*]*\s*\n\s*([a-z0-9][a-z0-9\-]+)\s*$', text, re.MULTILINE | re.IGNORECASE)
    if m:
        fields["slug"] = m.group(1).strip().strip('`"').lower()

    m = re.search(r'^[*\-\s]*Title[*]*(?:\s*\([^)]*\))?\s*:?\s*[*]*\s*(.+?)\s*[*]*$', text, re.MULTILINE | re.IGNORECASE)
    if m:
        title = m.group(1).strip().strip('`"')
        if len(title) > 60:
            title = title[:57] + "..."
        fields["meta_title"] = title

    m2 = re.search(r'^[*\-\s]*(?:Meta Title|SEO Title)[*]*(?:\s*\([^)]*\))?\s*:?\s*[*]*\s*(.+?)\s*[*]*$', text, re.MULTILINE | re.IGNORECASE)
    if m2:
        title = m2.group(1).strip().strip('`"')
        if len(title) > 60:
            title = title[:57] + "..."
        fields["meta_title"] = title

    m = re.search(r'^[*\-\s]*(?:Meta\s+)?Keywords[*]*(?:\s*\([^)]*\))?\s*:?\s*[*]*\s*(.+?)(?=\n[*\-\s]*(?:Characters|Slug|AI Image|Meta Desc)|\n\n)', text, re.MULTILINE | re.IGNORECASE | re.DOTALL)
    if not m:
        m = re.search(r'^[*\-\s]*(?:Meta\s+)?Keywords[*]*(?:\s*\([^)]*\))?\s*:?\s*[*]*\s*(.+)$', text, re.MULTILINE | re.IGNORECASE)
    if m:
        kw = m.group(1).strip().strip('`"')
        kw = re.sub(r'\s*\n\s*', ' ', kw)
        if len(kw) > 500:
            kw = kw[:500]
        fields["meta_keywords"] = kw

    # Handle "Primary Keyword" + "Secondary Keywords" format (combine into meta_keywords)
    if "meta_keywords" not in fields:
        parts = []
        m_pk = re.search(r'^[*\-\s]*Primary\s+Keywords?[*]*\s*:?\s*[*]*\s*(.+?)\s*[*]*$', text, re.MULTILINE | re.IGNORECASE)
        if m_pk:
            parts.append(m_pk.group(1).strip().strip('`"'))
        m_sk = re.search(r'^[*\-\s]*Secondary\s+Keywords?[*]*\s*:?\s*[*]*\s*(.+?)\s*[*]*$', text, re.MULTILINE | re.IGNORECASE)
        if m_sk:
            parts.append(m_sk.group(1).strip().strip('`"'))
        if parts:
            kw = ", ".join(parts)
            if len(kw) > 500:
                kw = kw[:500]
            fields["meta_keywords"] = kw

    m = re.search(r'^[*\-\s]*(?:Meta\s+)?Description[*]*(?:\s*\([^)]*\))?\s*:?\s*[*]*\s*(.+?)\s*[*]*$', text, re.MULTILINE | re.IGNORECASE)
    if m:
        desc = m.group(1).strip().strip('`"')
        if len(desc) > 150:
            desc = desc[:147] + "..."
        fields["meta_description"] = desc

    return fields


def markdown_to_html(text):
    """Convert simple markdown to HTML (headings, links, bold, italic, hr, paragraphs)."""
    # Remove JSON-LD code blocks
    text = re.sub(r'```json\s*\{[^`]*\}\s*```', '', text, flags=re.DOTALL)
    text = text.strip()

    lines = text.split('\n')
    html_lines = []
    in_paragraph = False

    for line in lines:
        stripped = line.strip()

        # Blank line — close paragraph
        if not stripped:
            if in_paragraph:
                html_lines.append('</p>')
                in_paragraph = False
            continue

        # Horizontal rule
        if re.match(r'^(-{3,}|\*{3,}|_{3,})$', stripped):
            if in_paragraph:
                html_lines.append('</p>')
                in_paragraph = False
            html_lines.append('<hr />')
            continue

        # Headings
        m = re.match(r'^(#{1,6})\s+(.+)$', stripped)
        if m:
            if in_paragraph:
                html_lines.append('</p>')
                in_paragraph = False
            level = len(m.group(1))
            heading_text = m.group(2).strip()
            # Process inline markdown in heading
            heading_text = _inline_markdown(heading_text)
            html_lines.append(f'<h{level}>{heading_text}</h{level}>')
            continue

        # Lines that already contain HTML tags — pass through
        if stripped.startswith('<'):
            if in_paragraph:
                html_lines.append('</p>')
                in_paragraph = False
            html_lines.append(stripped)
            continue

        # Regular text — wrap in paragraph
        processed = _inline_markdown(stripped)
        if not in_paragraph:
            html_lines.append('<p>' + processed)
            in_paragraph = True
        else:
            html_lines.append(' ' + processed)

    if in_paragraph:
        html_lines.append('</p>')

    return '\n'.join(html_lines)


def _inline_markdown(text):
    """Convert inline markdown: links, bold, italic."""
    # Links: [text](url)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    # Bold: **text** or __text__
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'__(.+?)__', r'<strong>\1</strong>', text)
    # Italic: *text* or _text_
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    text = re.sub(r'(?<!\w)_(.+?)_(?!\w)', r'<em>\1</em>', text)
    return text


def is_markdown(content):
    """Detect if content is markdown (not HTML)."""
    # If it starts with HTML tags, it's HTML
    stripped = content.strip()
    if stripped.startswith('<html') or stripped.startswith('<!DOCTYPE') or stripped.startswith('<head'):
        return False
    # If it has markdown headings, it's markdown
    if re.search(r'^#{1,6}\s+', stripped, re.MULTILINE):
        return True
    # If it has no HTML block tags but has markdown links, it's markdown
    if not re.search(r'<(p|div|h[1-6]|section)\b', stripped) and re.search(r'\[.+\]\(.+\)', stripped):
        return True
    return False


def extract_schema_fields(content):
    """Extract SEO fields from JSON-LD schema block in the blog file."""
    fields = {}
    m = re.search(r'"headline"\s*:\s*"([^"]+)"', content)
    if m:
        fields["title"] = m.group(1).strip()
    m = re.search(r'"description"\s*:\s*"([^"]+)"', content)
    if m:
        fields["meta_description"] = m.group(1).strip()
    m = re.search(r'"keywords"\s*:\s*"([^"]+)"', content)
    if m:
        fields["meta_keywords"] = m.group(1).strip()
    m = re.search(r'"@id"\s*:\s*"https?://[^/]+/blogs/([^"]+)"', content)
    if m:
        fields["slug"] = m.group(1).strip()
    return fields


def extract_blog_data(html_file):
    content = html_file.read_text(encoding="utf-8")
    schema = extract_schema_fields(content)
    title = None

    # Extract title from markdown heading or HTML
    m = re.search(r'<title>(.+?)</title>', content, re.IGNORECASE)
    if m:
        title = re.sub(r'<[^>]+>', '', m.group(1)).strip()
    if not title:
        m = re.search(r'<h1[^>]*>(.+?)</h1>', content, re.IGNORECASE | re.DOTALL)
        if m:
            title = re.sub(r'<[^>]+>', '', m.group(1)).strip()
    if not title:
        m = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if m:
            title = m.group(1).strip()
    if not title:
        title = schema.get("title")

    if is_markdown(content):
        # Remove the H1 title line before converting
        body = re.sub(r'^#\s+.+$', '', content, count=1, flags=re.MULTILINE)
        body = markdown_to_html(body)
    else:
        body = content
        body = re.sub(r'<!DOCTYPE[^>]*>', '', body, flags=re.IGNORECASE)
        body = re.sub(r'</?html[^>]*>', '', body, flags=re.IGNORECASE)
        body = re.sub(r'<head>.*?</head>', '', body, flags=re.IGNORECASE | re.DOTALL)
        body = re.sub(r'</?body[^>]*>', '', body, flags=re.IGNORECASE)
        body = re.sub(r'<h1[^>]*>.*?</h1>', '', body, flags=re.IGNORECASE | re.DOTALL)
        # body = re.sub(r'<script\s+type=["\']application/ld\+json["\']>.*?</script>', '', body, flags=re.IGNORECASE | re.DOTALL)
        body = re.sub(r'<title>.*?</title>', '', body, flags=re.IGNORECASE | re.DOTALL)
        body = re.sub(r'<meta[^>]*>', '', body, flags=re.IGNORECASE)
    body = body.strip()
    return title, body, schema


def prepare_posts(community_dir, community_name, post_filter=None):
    blog_files = find_blog_files(community_dir, post_filter)
    seo_files = find_seo_files(community_dir)
    if not blog_files:
        print(f"ERROR: No blog files found in {community_dir}")
        sys.exit(1)

    all_seo = {}
    for batch_num, seo_file in seo_files.items():
        parsed = parse_seo_package(seo_file)
        for post_in_batch, fields in parsed.items():
            if not fields.get("slug"):
                continue
            if post_in_batch > 5:
                absolute_num = post_in_batch
            else:
                absolute_num = (batch_num - 1) * 5 + post_in_batch
            all_seo[absolute_num] = fields

    posts = []
    errors = []
    for post_num, html_file in blog_files:
        title, body, schema = extract_blog_data(html_file)
        seo = all_seo.get(post_num, {})
        # Schema fields as fallback for missing SEO package data
        slug = seo.get("slug") or schema.get("slug")
        meta_title = seo.get("meta_title") or schema.get("title")
        meta_keywords = seo.get("meta_keywords") or schema.get("meta_keywords")
        meta_description = seo.get("meta_description") or schema.get("meta_description")
        post = {
            "number": post_num, "file": html_file.name, "title": title, "body": body,
            "slug": slug, "category": community_name,
            "meta_title": meta_title, "meta_keywords": meta_keywords,
            "meta_description": meta_description,
        }
        missing = [f for f in ["title", "body", "slug", "meta_title", "meta_keywords", "meta_description"] if not post[f]]
        if missing:
            errors.append(f"Post {post_num} ({html_file.name}): missing {', '.join(missing)}")
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
        # Wait for the editor dialog to appear
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
    # Wait for the title input to actually exist in the DOM
    if not wait_for_element('input[placeholder="Add a title here..."]', timeout=8):
        time.sleep(2)
        chrome_js("document.getElementById('tab-0').click()")
        wait_for_element('input[placeholder="Add a title here..."]', timeout=8)

    escaped = title.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')

    # Primary: native setter + InputEvent (triggers Vue reactivity)
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

    # Fallback: execCommand insertText
    if exec_insert('input[placeholder="Add a title here..."]', title):
        time.sleep(0.5)
        check = chrome_js("var el = document.querySelector('input[placeholder=\"Add a title here...\"]'); el ? el.value : ''")
        if check and len(str(check).strip()) > 5:
            return True

    return False


def enter_html_body(html_body):
    """Enter HTML body via TinyMCE's Source Code dialog."""
    # Step 1: Click Source code button to open the source editor
    r1 = chrome_js("""
    var btn = document.querySelector('.tox-tbtn[title="Source code"]');
    if (btn) { btn.click(); 'OK'; } else { 'FAIL'; }
    """)
    if not r1 or "FAIL" in str(r1):
        return False
    time.sleep(2)

    # Step 2: Write HTML to a hidden element to avoid JS escaping issues
    escaped = html_body.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')
    chrome_js(f"""
    var tmp = document.getElementById('__lofty_body_tmp');
    if (!tmp) {{ tmp = document.createElement('textarea'); tmp.id = '__lofty_body_tmp'; tmp.style.display='none'; document.body.appendChild(tmp); }}
    tmp.value = `{escaped}`;
    'injected';
    """)
    time.sleep(0.3)

    # Step 3: Set the source code textarea content and click Save
    r3 = chrome_js("""
    var dialog = document.querySelector('.tox-dialog');
    if (!dialog) { 'FAIL: no dialog'; }
    else {
        var ta = dialog.querySelector('textarea.tox-textarea');
        var html = document.getElementById('__lofty_body_tmp').value;
        if (ta) {
            ta.focus();
            ta.select();
            // Use native setter + events
            var setter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, 'value').set;
            setter.call(ta, html);
            ta.dispatchEvent(new Event('input', {bubbles: true}));
            ta.dispatchEvent(new Event('change', {bubbles: true}));
            // Click Save
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
    # Wait for the Settings pane to actually render
    if not wait_for_element('#pane-1', timeout=8):
        time.sleep(3)
        chrome_js("document.getElementById('tab-1').click()")
        wait_for_element('#pane-1', timeout=8)
    time.sleep(1)

    escaped = slug.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')
    # The slug input is in pane-1 — find it by label or by position
    js = f"""
    var pane = document.getElementById('pane-1');
    if (!pane) {{ 'FAIL: pane-1 not found'; }}
    else {{
        var slugInput = null;
        // Method 1: Find by label text "URL Slug" or "Slug"
        var labels = pane.querySelectorAll('label, .el-form-item__label');
        for (var i = 0; i < labels.length; i++) {{
            var t = labels[i].textContent.trim().toLowerCase();
            if (t.indexOf('slug') !== -1 || t.indexOf('url') !== -1) {{
                var container = labels[i].closest('.el-form-item') || labels[i].parentElement;
                var inp = container.querySelector('input.el-input__inner');
                if (inp) {{ slugInput = inp; break; }}
            }}
        }}
        // Method 2: Fallback — find input with hyphenated value (auto-generated slug)
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
        // Method 3: Find input whose placeholder contains "slug" or "url"
        if (!slugInput) {{
            var inputs = pane.querySelectorAll('input.el-input__inner');
            for (var i = 0; i < inputs.length; i++) {{
                var ph = (inputs[i].placeholder || '').toLowerCase();
                if (ph.indexOf('slug') !== -1 || ph.indexOf('url') !== -1) {{
                    slugInput = inputs[i];
                    break;
                }}
            }}
        }}
        // Method 4: Second input in pane (first is Author, second is Slug)
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
        }} else {{ 'FAIL: no slug input found in pane-1 (inputs: ' + pane.querySelectorAll('input.el-input__inner').length + ')'; }}
    }}
    """
    result = chrome_js(js)
    return result and "OK" in str(result)


def enter_category(category):
    """Select a category from the dropdown on the Settings tab."""
    # We should already be on Settings tab from enter_slug
    escaped = category.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')

    # Step 1: Click the select to open it, then type to filter
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

    # Step 2: Type into the select's search input using native setter (execCommand doesn't work on el-select)
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

    # Step 3: Click the matching option in the dropdown
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
    """Enter text into a Lofty SEO field (contentEditable div).
    Uses ClipboardEvent paste simulation — the only method that triggers
    Vue's reactivity on these custom contentEditable components.
    field_class: seoTitle, seoKeyword, seoDescription
    """
    escaped = value.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')
    js = f"""
    var editor = document.querySelector('.cms-global-editor.{field_class} .ie-content');
    if (editor) {{
        editor.focus();
        // Select all existing content (including template variable tags)
        var range = document.createRange();
        range.selectNodeContents(editor);
        var sel = window.getSelection();
        sel.removeAllRanges();
        sel.addRange(range);
        // Paste our text — the component's paste handler picks this up
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
    # Vue updates the counter asynchronously — wait for it
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
        # Handle confirmation dialog if one appears
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
    """Close any open editor dialog and navigate back to blog list."""
    # Try clicking cancel/close button
    chrome_js("""
    var close = document.querySelector('.edit-blog-dialog .el-dialog__close');
    if (close) { close.click(); }
    """)
    time.sleep(1)
    # Handle "are you sure" confirmation if it appears
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
    """Ensure we're on the blog list page, not in an editor."""
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
    label = f"Post {post['number']}: {post['title'][:50]}"
    print(f"\n{'='*60}")
    print(f"Publishing {label}")
    print(f"{'='*60}")

    # Step 1: Navigate to blog list and click Add New
    print("  [1/8] Opening editor...")
    navigate_to_blog_list()
    if not click_add_new():
        print("  ERROR: Could not open editor dialog. Skipping.")
        report.append({"post": label, "status": "SKIP", "slug": post["slug"]})
        return

    # Step 2: Title (Content tab)
    print("  [2/8] Title...")
    time.sleep(1)
    if retry_field(enter_title, post["title"], label="TITLE"):
        print(f"    TITLE: OK")
    else:
        print(f"    TITLE: FAIL")
    time.sleep(1)

    # Step 3: HTML Body (via Source Code button)
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

    # Step 4: Slug (switches to Settings tab)
    print("  [4/8] Slug...")
    slug_ok = retry_field(enter_slug, post["slug"], label="SLUG")
    if slug_ok:
        print(f"    SLUG: OK — {post['slug']}")
    else:
        print(f"    SLUG: FAIL — skipping post (slug is required)")
        close_editor_dialog()
        report.append({"post": label, "status": "SLUG FAIL", "slug": post["slug"]})
        time.sleep(3)
        return
    time.sleep(1)

    # Step 5: Category (still on Settings tab)
    print("  [5/8] Category...")
    if retry_field(enter_category, post["category"], label="CATEGORY"):
        print(f"    CATEGORY: OK — {post['category']}")
    else:
        print(f"    CATEGORY: FAIL — select manually")
    time.sleep(1)

    # Step 6: Switch to SEO tab
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

    # Step 8: QA Verification — read back all fields before publishing
    print("  [8/9] QA check...")
    qa_issues = []

    # Check Title (Content tab)
    chrome_js("document.getElementById('tab-0').click()")
    time.sleep(1.5)
    title_val = chrome_js('var el = document.querySelector(\'input[placeholder="Add a title here..."]\'); el ? el.value : ""')
    title_val = str(title_val).strip() if title_val else ""
    if not title_val or len(title_val) < 3:
        qa_issues.append("TITLE (empty)")
    elif title_val != post["title"]:
        qa_issues.append(f"TITLE (got: '{title_val[:40]}...')")

    # Check Body (look for content in TinyMCE iframe)
    body_check = chrome_js("""
    var iframe = document.querySelector('.tox-edit-area__iframe');
    if (iframe && iframe.contentDocument) {
        var body = iframe.contentDocument.body;
        body && body.textContent.trim().length > 20 ? 'HAS_CONTENT' : 'EMPTY';
    } else { 'NO_IFRAME'; }
    """)
    if not body_check or "HAS_CONTENT" not in str(body_check):
        qa_issues.append("BODY (empty or not loaded)")

    # Check Slug (Settings tab)
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

    # Check SEO fields (SEO tab)
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
        # Auto-retry all failed fields
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
        description="Publish blog posts to Lofty CMS",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 publish.py "Green Valley"                 Publish all posts
  python3 publish.py "Green Valley" --posts 36-40   Publish posts 36-40
  python3 publish.py "New Construction" --posts 110  Publish one post
        """
    )
    parser.add_argument("community", nargs="?", help="Community/neighborhood name")
    parser.add_argument("--posts", help="Post numbers: '36-40' or '36,37,38'")
    parser.add_argument("--no-publish", action="store_true", help="Prepare data only")
    parser.add_argument("--tab", type=int, default=4, help="Chrome tab number to use (default: 4)")
    parser.add_argument("--category", help="Lofty category name (overrides community name)")
    parser.add_argument("--yes", action="store_true", help="Skip confirmation prompts")
    args = parser.parse_args()

    if not args.community:
        parser.error("Community name required")

    global TAB, AUTO_YES
    TAB = f"tab {args.tab}"
    AUTO_YES = args.yes

    folder_name = args.community
    community_name = args.category or args.community
    community_dir = BLOGS_BASE / folder_name
    if not community_dir.exists():
        for d in BLOGS_BASE.iterdir():
            if d.is_dir() and d.name.lower() == folder_name.lower():
                community_dir = d
                if not args.category:
                    community_name = d.name
                break
        else:
            print(f"ERROR: Folder not found: {community_dir}")
            for d in sorted(BLOGS_BASE.iterdir()):
                if d.is_dir():
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

    print(f"\nPreparing posts from: {community_dir}")
    posts = prepare_posts(community_dir, community_name, post_filter)

    print(f"\nFound {len(posts)} posts to publish:")
    for p in posts:
        print(f"  Post {p['number']}: {p['title'][:60]}")
        print(f"    Slug: {p['slug']}")

    if args.no_publish:
        print("\n--no-publish flag. Done.")
        return

    print(f"\nUsing Chrome {TAB}")
    print("Make sure you're logged into Lofty and on the blog dashboard.")
    if not AUTO_YES:
        confirm = input("Proceed? (y/n): ").strip().lower()
        if confirm != "y":
            print("Cancelled.")
            return

    chrome_activate()

    report = []
    for post in posts:
        publish_post(post, report)

    print(f"\n{'='*60}")
    print(f"DONE — {len(posts)} posts")
    print(f"{'='*60}")
    ok = sum(1 for r in report if r["status"] == "OK")
    print(f"Published: {ok}/{len(posts)}")
    for r in report:
        icon = "OK" if r["status"] == "OK" else "!!"
        print(f"  [{icon}] {r['post']} — {r['slug']}")


if __name__ == "__main__":
    main()
