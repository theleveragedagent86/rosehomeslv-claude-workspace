#!/usr/bin/env python3
"""
Lofty CMS Local News Blog Publisher (background, via Lofty API)
===========================================================
Publishes local news blog posts to the Lofty CMS by controlling Chrome via AppleScript.

By default it publishes EVERY blog in the run: the selected stories in blogs/
(story-NN-slug.html, SEO from blog-seo-package.md) and the bonus stories in
blogs/bonus/ (bonus-NN-slug.html, SEO from bonus-blog-seo-package.md).

Usage:
    python3 publish-local-news.py 2026-05-08                    All stories and bonus
    python3 publish-local-news.py 2026-05-08 --only story       Selected stories only
    python3 publish-local-news.py 2026-05-08 --only bonus       Bonus stories only
    python3 publish-local-news.py 2026-05-08 --posts 1-10       Stories 1 to 10
    python3 publish-local-news.py 2026-05-08 --bonus-posts 1-5  Bonus 1 to 5

Runs in the background: it calls Lofty's blog API through any open
cms.lofty.com tab (any window, any tab number) and never needs focus.
--ui brings back the old editor-driving method (tab 4, hands off).

Requirements: macOS, Google Chrome (with View > Developer > Allow JavaScript
from Apple Events enabled), logged into Lofty CMS in some tab.
"""

import sys
import os
import re
import json
import subprocess
import argparse
import time
from datetime import datetime
from pathlib import Path

# ─── Configuration ───────────────────────────────────────────────────────────

LOCAL_NEWS_BASE = Path("/Users/ryanrose/Downloads/Claude/Rose Homes LV/Content/Instagram/Local News")
LOFTY_URL = "https://cms.lofty.com/cmsnew/blog"
TAB = "tab 4"  # Which Chrome tab to use — change if needed
CATEGORY = "Local News"  # Lofty category for local news posts

# ─── Data Extraction ─────────────────────────────────────────────────────────

def find_blog_files(date_dir, story_filter=None, bonus_filter=None, scope="all"):
    """Find every blog file to publish.

    Selected stories live in blogs/ as story-NN-slug.html.
    Bonus stories live in blogs/bonus/ as bonus-NN-slug.html.

    Returns a list of dicts ordered stories first, then bonus, each by number.
    """
    sources = []
    if scope in ("all", "story"):
        sources.append(("story", "Story", date_dir / "blogs",
                        r'story-(\d+)-(.+)\.html', story_filter, 0))
    if scope in ("all", "bonus"):
        sources.append(("bonus", "Bonus", date_dir / "blogs" / "bonus",
                        r'bonus-(\d+)-(.+)\.html', bonus_filter, 1))

    found = []
    for kind, word, d, pattern, post_filter, order in sources:
        if not d.exists():
            if scope != "all":
                print(f"ERROR: Directory not found: {d}")
                sys.exit(1)
            continue
        for f in sorted(d.iterdir()):
            if f.suffix != ".html":
                continue
            m = re.match(pattern, f.name)
            if not m:
                continue
            num = int(m.group(1))
            if post_filter is not None and num not in post_filter:
                continue
            found.append({
                "kind": kind,
                "number": num,
                "label": f"{word} {num}",
                "slug_from_name": m.group(2),
                "path": f,
                "order": order,
            })

    found.sort(key=lambda x: (x["order"], x["number"]))
    return found



def _section_re(heading):
    """Matches every section heading format the skill has produced:
    '### Story 3: Title', '### S03. Story 3: Title', '### Bonus 3: Title', '### B03. Title'."""
    letter = heading[0]
    return (r'###\s+(?:' + letter + r'(\d+)\.\s*(?:' + heading + r'\s+\d+\s*:\s*)?|'
            + heading + r'\s+(\d+)\s*:?\s*)')


def _section_num(m):
    return int(m.group(1) or m.group(2))


def parse_seo_package(seo_file, heading="Story"):
    """Parse an SEO package .md file into per-story SEO data.

    heading is the word used in the section headings, "Story" for
    blog-seo-package.md and "Bonus" for bonus-blog-seo-package.md.
    """
    content = seo_file.read_text(encoding="utf-8")
    posts = {}

    # Split by "### Story N:" or "### Bonus N:" sections
    # split on the heading without its capture groups, so no None pieces appear
    sections = re.split('(?=' + re.sub(r'\((?!\?)', '(?:', _section_re(heading)) + ')', content)

    current_num = None
    current_text = ""
    for section in sections:
        m = re.match(_section_re(heading), section)
        if m:
            if current_num is not None:
                posts[current_num] = extract_seo_fields(current_text)
            current_num = _section_num(m)
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


def extract_schema(content):
    """Extract the JSON-LD block from a blog HTML file and return it as pretty JSON.

    The schema is authored inside <script type="application/ld+json"> in the source
    file (keeps the file portable), but it must NOT be pasted into Lofty's body
    editor. TinyMCE intermittently wraps the JSON in <p> tags inside the <script>
    element, which makes it invalid and Google silently discards it. It goes in
    Lofty's Schema tab instead.

    Returns (schema_json_string_or_None, error_or_None).
    """
    m = re.search(
        r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
        content, re.IGNORECASE | re.DOTALL)
    if not m:
        return None, None

    raw = m.group(1)
    # Strip any HTML that leaked into the block and decode entities
    raw = re.sub(r'</?(?:p|br|div|span)\b[^>]*>', '', raw, flags=re.IGNORECASE)
    raw = (raw.replace('&quot;', '"').replace('&amp;', '&')
              .replace('&nbsp;', ' ').replace('&lt;', '<').replace('&gt;', '>'))
    raw = raw.strip()

    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as e:
        return None, f"JSON-LD does not parse: {e}"

    return json.dumps(parsed, indent=2, ensure_ascii=False), None


def build_fallback_schema(title, slug, meta_description, meta_keywords, date_str):
    """Build a minimal valid @graph when the source file has no JSON-LD.

    Every post ships with schema. The Person and RealEstateAgent @id values are
    identical on every post by design — that consistency is what lets search
    engines and LLMs merge them into a single entity over time.
    """
    url = f"https://www.rosehomeslv.com/blog/{slug}"
    return json.dumps({
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "NewsArticle",
                "@id": f"{url}#article",
                "headline": title,
                "description": meta_description or "",
                "author": {"@id": "https://www.rosehomeslv.com/#ryanrose"},
                "publisher": {"@id": "https://www.rosehomeslv.com/#org"},
                "datePublished": date_str,
                "dateModified": date_str,
                "mainEntityOfPage": {"@type": "WebPage", "@id": url},
                "keywords": meta_keywords or "",
            },
            {
                "@type": "Person",
                "@id": "https://www.rosehomeslv.com/#ryanrose",
                "name": "Ryan Rose",
                "jobTitle": "Las Vegas Real Estate Expert",
                "url": "https://www.rosehomeslv.com",
                "worksFor": {"@id": "https://www.rosehomeslv.com/#org"},
            },
            {
                "@type": "RealEstateAgent",
                "@id": "https://www.rosehomeslv.com/#org",
                "name": "Rose Homes LV",
                "url": "https://www.rosehomeslv.com",
                "telephone": "+1-702-747-5921",
                "areaServed": {"@type": "AdministrativeArea",
                               "name": "Clark County, Nevada"},
            },
        ],
    }, indent=2, ensure_ascii=False)


def extract_blog_data(html_file):
    """Extract title, body, and JSON-LD schema from a blog HTML file."""
    content = html_file.read_text(encoding="utf-8")
    schema, schema_err = extract_schema(content)

    # Title = the H1 headline. <title> is the SEO title ("... | Ryan Rose"),
    # which goes in the SEO tab, not on the page.
    title = None
    m = re.search(r'<h1[^>]*>(.+?)</h1>', content, re.IGNORECASE | re.DOTALL)
    if m:
        title = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', m.group(1))).strip()
    if not title:
        m = re.search(r'<title>(.+?)</title>', content, re.IGNORECASE)
        if m:
            title = re.sub(r'\s*\|\s*Ryan Rose\s*$', '', re.sub(r'<[^>]+>', '', m.group(1))).strip()

    # Extract body — strip HTML wrapper, head, h1, title, meta, dateline/byline
    body = content
    body = re.sub(r'<!DOCTYPE[^>]*>', '', body, flags=re.IGNORECASE)
    body = re.sub(r'</?html[^>]*>', '', body, flags=re.IGNORECASE)
    body = re.sub(r'<head>.*?</head>', '', body, flags=re.IGNORECASE | re.DOTALL)
    body = re.sub(r'</?body[^>]*>', '', body, flags=re.IGNORECASE)
    body = re.sub(r'<h1[^>]*>.*?</h1>', '', body, flags=re.IGNORECASE | re.DOTALL)
    body = re.sub(r'<title>.*?</title>', '', body, flags=re.IGNORECASE | re.DOTALL)
    body = re.sub(r'<meta[^>]*>', '', body, flags=re.IGNORECASE)
    # Schema is entered on the Schema tab, never in the body — TinyMCE corrupts it
    body = re.sub(r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>.*?</script>',
                  '', body, flags=re.IGNORECASE | re.DOTALL)
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

    return title, body, schema, schema_err


def prepare_posts(date_dir, story_filter=None, bonus_filter=None, scope="all"):
    """Prepare all posts for publishing, selected stories and bonus stories."""
    blog_files = find_blog_files(date_dir, story_filter, bonus_filter, scope)
    if not blog_files:
        print(f"ERROR: No blog files found under {date_dir / 'blogs'}")
        sys.exit(1)

    # Parse whichever SEO packages this run actually needs
    seo_sources = {
        "story": (date_dir / "blog-seo-package.md", "Story"),
        "bonus": (date_dir / "bonus-blog-seo-package.md", "Bonus"),
    }
    all_seo = {"story": {}, "bonus": {}}
    for kind in sorted({b["kind"] for b in blog_files}):
        seo_file, heading = seo_sources[kind]
        if seo_file.exists():
            all_seo[kind] = parse_seo_package(seo_file, heading)
        else:
            print(f"WARNING: No SEO package found at {seo_file}")

    posts = []
    errors = []
    for entry in blog_files:
        html_file = entry["path"]
        label = entry["label"]
        title, body, schema, schema_err = extract_blog_data(html_file)
        seo = all_seo[entry["kind"]].get(entry["number"], {})
        if schema_err:
            errors.append(f"{label} ({html_file.name}): {schema_err}")

        slug = seo.get("slug")
        meta_title = seo.get("meta_title")
        meta_keywords = seo.get("meta_keywords")
        meta_description = seo.get("meta_description")

        # Fallback: derive slug from filename
        if not slug:
            slug = entry["slug_from_name"]

        # Every post ships with schema. If the source file had none, build one.
        if not schema and not schema_err and slug and title:
            schema = build_fallback_schema(
                title, slug, meta_description, meta_keywords,
                date_dir.name if re.match(r'\d{4}-\d{2}-\d{2}', date_dir.name)
                else datetime.now().strftime("%Y-%m-%d"))
            print(f"  NOTE: {label} had no JSON-LD, generated a fallback graph.")

        post = {
            "number": entry["number"], "kind": entry["kind"], "label": label,
            "file": html_file.name, "title": title, "body": body,
            "slug": slug, "category": CATEGORY,
            "meta_title": meta_title, "meta_keywords": meta_keywords,
            "meta_description": meta_description, "schema": schema,
        }
        missing = [f for f in ["title", "body", "slug", "meta_title", "meta_keywords", "meta_description", "schema"] if not post[f]]
        if missing:
            errors.append(f"{label} ({html_file.name}): missing {', '.join(missing)}")
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


def click_schema_tab():
    """Click the Schema tab in the blog editor.

    Find it by label rather than by index — Lofty added this tab in Aug 2026 and
    the index could shift again if they add another.
    """
    js = """
    var tabs = document.querySelectorAll('.el-tabs__item, [role="tab"]');
    var hit = '';
    for (var i = 0; i < tabs.length; i++) {
        if (tabs[i].textContent.trim() === 'Schema' && tabs[i].offsetHeight > 0) {
            tabs[i].click();
            hit = 'clicked:' + (tabs[i].id || 'noid');
            break;
        }
    }
    hit || 'FAIL: no Schema tab';
    """
    result = chrome_js(js)
    if result and "clicked" in str(result):
        time.sleep(2)
        return True
    # Fallback: Schema sits after Content/Settings/SEO
    chrome_js("var t = document.getElementById('tab-3'); if (t) { t.click(); }")
    time.sleep(2)
    return bool(chrome_js("document.querySelector('.json-schema-editor') ? 'YES' : ''"))


def enter_schema(schema_json):
    """Enter JSON-LD into Lofty's Schema tab (a CodeMirror JSON editor).

    CodeMirror's JS instance lives on the DOM node as an expando property
    (el.CodeMirror), and AppleScript's `execute javascript` runs in an ISOLATED
    world, where page-set expandos are invisible. So setValue() is unreachable
    from here even though the element is right there. Chrome extensions can see
    it; we cannot.

    What does work is driving CodeMirror through the events it listens for on
    its hidden textarea: a Cmd-A keydown to select all, then a paste event
    carrying the JSON. Same technique the SEO fields already use.

    Note the keydown must set metaKey ONLY. Setting metaKey and ctrlKey together
    makes CodeMirror read the combo as "Ctrl-Cmd-A", which maps to nothing, and
    the paste then appends to the existing content instead of replacing it.
    """
    if not click_schema_tab():
        return False

    # json.dumps gives a JS string literal that is pure ASCII with \n escapes.
    # This matters twice over: it survives AppleScript's `read POSIX file`
    # (which decodes as MacRoman and would mangle any raw non-ASCII), and it
    # avoids every newline and quoting problem a template literal would have.
    payload_literal = json.dumps(schema_json, ensure_ascii=True)

    js = f"""
    (function() {{
        var payload = {payload_literal};
        var ta = document.querySelector('.json-schema-editor .CodeMirror textarea');
        if (!ta) {{ return 'FAIL: no CodeMirror textarea in .json-schema-editor'; }}
        ta.focus();
        ta.dispatchEvent(new KeyboardEvent('keydown', {{
            key: 'a', code: 'KeyA', keyCode: 65, which: 65,
            metaKey: true, bubbles: true, cancelable: true
        }}));
        var dt = new DataTransfer();
        dt.setData('text/plain', payload);
        ta.dispatchEvent(new ClipboardEvent('paste', {{
            clipboardData: dt, bubbles: true, cancelable: true
        }}));
        return 'PASTED:' + payload.length;
    }})()
    """
    result = chrome_js(js)
    if not result or "PASTED" not in str(result):
        print(f"    SCHEMA: {result}")
        return False

    time.sleep(1.5)

    # CodeMirror virtualizes: only the lines currently in view exist in the DOM,
    # and after a paste the viewport sits at the END of the document. The opening
    # "@graph" line is then unrendered, so innerText comes back short and the
    # check below reports a false failure even though the field is correct.
    # Scroll back to the top and let it repaint before reading.
    chrome_js("""
    var sc = document.querySelector('.json-schema-editor .CodeMirror-scroll');
    if (sc) { sc.scrollTop = 0; }
    """)
    time.sleep(1.0)

    # Verify against the rendered text and Lofty's own validator
    # NOTE: raw string. The \u200b and \n escapes below must reach Chrome as
    # literal backslash sequences. Without the r prefix Python turns '\n' into
    # a real newline, the JS string literal breaks, the script fails to parse,
    # and Chrome returns nothing -- which reads as "could not verify".
    check = chrome_js(r"""
    (function() {
        var w = document.querySelector('.json-schema-editor');
        var code = document.querySelector('.json-schema-editor .CodeMirror-code');
        var txt = code ? code.innerText.replace(/\u200b/g, '') : '';
        var indicator = w ? w.innerText.split('\n').pop().trim() : 'none';
        return JSON.stringify({
            len: txt.length,
            hasGraph: txt.indexOf('@graph') > -1,
            indicator: indicator
        });
    })()
    """)
    try:
        info = json.loads(str(check))
    except Exception:
        print(f"    SCHEMA: could not verify ({check})")
        return False

    if info.get("indicator") != "Valid JSON":
        print(f"    SCHEMA: validator reads '{info.get('indicator')}'")
        return False
    if not info.get("hasGraph") or info.get("len", 0) < 200:
        print(f"    SCHEMA: content looks wrong (len={info.get('len')}, "
              f"hasGraph={info.get('hasGraph')})")
        return False
    return True


def _post_now_dialog_open():
    """True while the blog editor is actually open.

    Do NOT test for .edit-blog-dialog — that element stays in the DOM after the
    editor closes (as an empty shell), so its presence always reads true and a
    successful publish would be reported as a failure. The editor's own tab bar
    (Content/Settings/SEO/Schema) is only mounted while the editor is open.
    """
    r = chrome_js("!!document.getElementById('tab-0')")
    return str(r).strip() == "true"


def _wait_editor_closed(timeout=8):
    """Poll until the editor closes. Publishing is not instant — checking once
    right after the activation reports a false failure on a slow save."""
    deadline = time.time() + timeout
    while time.time() < deadline:
        if not _post_now_dialog_open():
            return True
        time.sleep(1)
    return not _post_now_dialog_open()


def _confirm_followup_dialog():
    """Dismiss the OK/Confirm popup that can follow a publish."""
    chrome_js("""
    var btns = document.querySelectorAll('.el-message-box__btns button, .el-dialog button');
    for (var i = 0; i < btns.length; i++) {
        var t = btns[i].textContent.trim();
        if ((t === 'OK' || t === 'Confirm' || t === 'Yes') && btns[i].offsetHeight > 0) {
            btns[i].focus(); btns[i].click(); break;
        }
    }
    """)
    time.sleep(3)


# Lofty's own blog list endpoint. Publishing a slug that already exists leaves
# the editor open with a validation error, which this script used to misreport as
# an Accessibility problem. These headers are what the CMS app itself sends; without
# them the endpoint returns 601.
LOFTY_SITE_ID = 120104
LOFTY_LIST_PATH = "/api-blog/post/listV2"


def find_existing_slugs(candidate_slugs, timeout=90):
    """Return the subset of candidate_slugs that already exist in Lofty.

    Runs in the CMS page, so it reuses the logged-in session. Returns None if the
    check could not run at all, which the caller treats as "unknown, proceed".
    """
    payload = json.dumps(list(candidate_slugs))
    chrome_js(f"""
    window.__slugCheck = 'PENDING';
    (async function() {{
        try {{
            var want = new Set({payload});
            var H = {{
                'Accept': 'application/json, text/plain, */*',
                'CURRENTSITEID': {LOFTY_SITE_ID},
                'CURRENTLANGUAGE': 'en',
                'CMSACCOUNTROLE': 0
            }};
            var hits = [];
            for (var pn = 1; pn <= 60; pn++) {{
                var r = await fetch('{LOFTY_LIST_PATH}?keywords=&status=1&pageNum=' + pn +
                                    '&pageSize=500&t=' + Date.now(),
                                    {{ credentials: 'include', headers: H }});
                var j = await r.json();
                var list = j && j.data && j.data.postList;
                if (!list) {{ window.__slugCheck = 'ERR: unexpected response'; return; }}
                if (!list.length) break;
                for (var i = 0; i < list.length; i++) {{
                    if (want.has(list[i].slug)) hits.push(list[i].slug);
                }}
            }}
            window.__slugCheck = 'OK:' + hits.join(',');
        }} catch (e) {{
            window.__slugCheck = 'ERR: ' + e.message;
        }}
    }})();
    'started'
    """)

    deadline = time.time() + timeout
    while time.time() < deadline:
        time.sleep(2)
        res = str(chrome_js("window.__slugCheck || 'PENDING'") or "").strip()
        if res.startswith("OK:"):
            body = res[3:].strip()
            return [s for s in body.split(",") if s]
        if res.startswith("ERR"):
            print(f"  Slug check could not run ({res[:120]})")
            return None
    print("  Slug check timed out.")
    return None


def _osa(script, timeout=15):
    """Run an AppleScript with a hard timeout.

    Without a timeout these calls block forever when macOS is waiting on an
    Accessibility permission prompt, which leaves the whole run wedged and only
    killable with Ctrl-C. Returns (ok, stderr_text).
    """
    try:
        r = subprocess.run(['osascript', '-e', script],
                           capture_output=True, timeout=timeout)
        return r.returncode == 0, (r.stderr or b"").decode("utf-8", "replace")
    except subprocess.TimeoutExpired:
        return False, "timed out waiting on osascript (permission prompt?)"


def check_accessibility_permission():
    """Verify this terminal can send trusted UI events before we start.

    Publishing depends on System Events keystrokes and clicks. Without the
    Accessibility grant every post gets fully filled in and then fails at the
    final step, which is a slow and confusing way to discover a checkbox.
    """
    ok, err = _osa('tell application "System Events" to return name of first process')
    if ok:
        return True
    print("\n" + "=" * 60)
    print("ACCESSIBILITY PERMISSION MISSING")
    print("=" * 60)
    print("This script publishes by sending real keystrokes and clicks, which")
    print("macOS blocks until the terminal app is granted Accessibility access.")
    print("\nFix it:")
    print("  1. System Settings > Privacy & Security > Accessibility")
    print("  2. Turn on your terminal app (Terminal, or iTerm)")
    print("  3. QUIT the terminal completely (Cmd-Q) and reopen it")
    print("     The grant only applies to a freshly launched process.")
    print("  4. Re-run this command")
    if err.strip():
        print(f"\nosascript said: {err.strip()[:300]}")
    print("\nEverything except the final publish click would have worked, so")
    print("nothing is wrong with your content. Stopping before wasting a run.")
    return False


def click_post_now():
    """Activate Post Now with a TRUSTED OS event.

    Lofty's Post Now handler ignores synthetic clicks. A JavaScript
    element.click() fills nothing and publishes nothing — every field saves, the
    dialog just sits there. The button has to be activated by a real OS event.

    Strategy: focus the button in JS (allowed), then send a trusted Return via
    System Events. If the dialog is still open after that, fall back to a real
    click at the button's screen coordinates.

    Requires: System Settings > Privacy & Security > Accessibility > enable
    Terminal (or iTerm), in addition to Chrome's "Allow JavaScript from Apple
    Events".
    """
    focused = chrome_js("""
    var dialog = document.querySelector('.edit-blog-dialog');
    var done = 'FAIL: no dialog';
    if (dialog) {
        var btns = dialog.querySelectorAll('button.cms-button');
        for (var i = 0; i < btns.length; i++) {
            if (btns[i].textContent.trim() === 'Post Now' && btns[i].offsetHeight > 0) {
                btns[i].focus();
                done = (document.activeElement === btns[i]) ? 'focused' : 'FAIL: not focused';
                break;
            }
        }
    }
    done;
    """)
    if not focused or str(focused).strip() != "focused":
        print(f"    POST NOW: could not focus button ({focused})")
        return False

    # Attempt 1 — trusted Return keystroke to the focused button
    _osa('tell application "Google Chrome" to activate')
    time.sleep(0.5)
    ok, err = _osa('tell application "System Events" to key code 36')  # 36 = Return
    if not ok:
        print(f"    POST NOW: keystroke blocked ({err.strip()[:120]})")
    time.sleep(2)
    _confirm_followup_dialog()

    if _wait_editor_closed(8):
        return True

    # Attempt 2 — trusted click at the button's real screen coordinates
    print("    POST NOW: Return keystroke did not take, trying a real click...")
    coords = chrome_js("""
    var dlg = document.querySelector('.edit-blog-dialog');
    var b = null;
    if (dlg) {
        var btns = dlg.querySelectorAll('button.cms-button');
        for (var i = 0; i < btns.length; i++) {
            if (btns[i].textContent.trim() === 'Post Now' && btns[i].offsetHeight > 0) {
                b = btns[i]; break;
            }
        }
    }
    if (b) {
        var r = b.getBoundingClientRect();
        var x = Math.round(window.screenX + r.left + r.width / 2);
        var y = Math.round(window.screenY + (window.outerHeight - window.innerHeight)
                           + r.top + r.height / 2);
        x + ',' + y;
    } else { 'FAIL'; }
    """)
    coords = str(coords).strip() if coords else "FAIL"
    if "," not in coords:
        print("    POST NOW: could not locate button coordinates")
        return False

    x, y = [c.strip() for c in coords.split(',')[:2]]
    ok, err = _osa(f'tell application "System Events" to click at {{{x}, {y}}}')
    if not ok:
        print(f"    POST NOW: click blocked ({err.strip()[:120]})")
    time.sleep(2)
    _confirm_followup_dialog()

    if not _wait_editor_closed(8):
        print("    POST NOW: dialog still open — check Accessibility permission "
              "for Terminal in System Settings > Privacy & Security")
        return False
    return True


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
    label = f"{post.get('label', 'Story ' + str(post['number']))}: {post['title'][:50]}"
    print(f"\n{'='*60}")
    print(f"Publishing {label}")
    print(f"{'='*60}")

    # Step 1: Navigate and open editor
    print("  [1/10] Opening editor...")
    navigate_to_blog_list()
    if not click_add_new():
        print("  ERROR: Could not open editor. Skipping.")
        report.append({"post": label, "status": "SKIP", "slug": post["slug"]})
        return

    # Step 2: Title
    print("  [2/10] Title...")
    time.sleep(1)
    if retry_field(enter_title, post["title"], label="TITLE"):
        print(f"    TITLE: OK")
    else:
        print(f"    TITLE: FAIL")
    time.sleep(1)

    # Step 3: HTML Body
    print("  [3/10] HTML body...")
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
    print("  [4/10] Slug...")
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
    print("  [5/10] Category...")
    if retry_field(enter_category, post["category"], label="CATEGORY"):
        print(f"    CATEGORY: OK — {post['category']}")
    else:
        print(f"    CATEGORY: FAIL — select manually")
    time.sleep(1)

    # Step 6: SEO tab
    print("  [6/10] Switching to SEO tab...")
    chrome_js("document.getElementById('tab-2').click()")
    time.sleep(3)

    # Step 7: SEO fields
    print("  [7/10] SEO fields...")
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

    # Step 8: Schema tab
    print("  [8/10] Schema (JSON-LD)...")
    if retry_field(enter_schema, post["schema"], label="SCHEMA"):
        print(f"    SCHEMA: OK — Valid JSON")
    else:
        print(f"    SCHEMA: FAIL — enter manually on the Schema tab")
    time.sleep(1)

    # Step 9: QA check
    print("  [9/10] QA check...")
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

    # Schema tab — a broken schema block is invisible once published, so verify it
    if click_schema_tab():
        # raw string -- see the note in enter_schema()
        schema_check = chrome_js(r"""
        (function() {
            var w = document.querySelector('.json-schema-editor');
            var code = document.querySelector('.json-schema-editor .CodeMirror-code');
            if (!w || !code) { return 'NO_EDITOR'; }
            var txt = code.innerText.replace(/\u200b/g, '').trim();
            if (!txt) { return 'EMPTY'; }
            var indicator = w.innerText.split('\n').pop().trim();
            if (indicator !== 'Valid JSON') { return 'BAD_JSON'; }
            return txt.indexOf('@graph') > -1 ? 'VALID' : 'NO_GRAPH';
        })()
        """)
        schema_check = str(schema_check).strip() if schema_check else "NO_RESULT"
        if schema_check != "VALID":
            qa_issues.append(f"SCHEMA ({schema_check.lower()})")
    else:
        qa_issues.append("SCHEMA (tab not found)")

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
        if any("SCHEMA" in i for i in qa_issues):
            retry_field(enter_schema, post["schema"], retries=2, label="SCHEMA")
        print("  Retry complete.")
    else:
        print("  ** QA PASSED — all fields verified")

    # Step 9: Post Now
    print("  [10/10] Publishing...")
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

# ─── API publishing (default) ────────────────────────────────────────────────
# Calls Lofty's own blog API from inside any open cms.lofty.com tab, so it runs
# in the background: no tab number, no focus, no keystrokes. Keep using the Mac.

def _lofty_api():
    import importlib.util as iu
    here = Path(__file__).resolve().parent
    path = here / "lofty_api.py"  # bundled copy in the zip
    if not path.exists():
        path = here.parent / "publish-blogs-plugin" / "lofty_api.py"  # dev workspace
    spec = iu.spec_from_file_location("lofty_api", path)
    mod = iu.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def api_publish(posts, args):
    L = _lofty_api()
    print("\nRuns in the background through any open Lofty tab. You can keep using your Mac.")
    if not args.yes and input("Proceed? (y/n): ").strip().lower() != "y":
        print("Cancelled.")
        return
    existing = L.find_by_slug([p["slug"] for p in posts])
    if existing:
        print(f"\n  {len(existing)} slugs already published, skipping them"
              f" (use fix-local-news-blogs.py to update):")
        for s in existing:
            print(f"    {s}")
        posts = [p for p in posts if p["slug"] not in existing]
    if not posts:
        print("\nNothing left to publish. Done.")
        return
    print(f"\nPublishing {len(posts)} posts...")
    rows = L.create([{
        "title": p["title"], "slug": p["slug"], "content": p["body"],
        "seoTitle": p["meta_title"], "seoKeyword": p["meta_keywords"],
        "seoDescription": p["meta_description"], "customSchema": p["schema"],
    } for p in posts], args.category)
    ok = [r for r in rows if r[1].startswith("OK")]
    print(f"\n{'='*60}\nPublished: {len(ok)}/{len(posts)}\n{'='*60}")
    for r in rows:
        if not r[1].startswith("OK"):
            print(f"  [!!] /blog/{r[0]}  {r[1]}")


def main():
    parser = argparse.ArgumentParser(
        description="Publish local news blog posts to Lofty CMS",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 publish-local-news.py 2026-05-08                     Every blog, selected and bonus
  python3 publish-local-news.py 2026-05-08 --only story        Selected stories only
  python3 publish-local-news.py 2026-05-08 --only bonus        Bonus stories only
  python3 publish-local-news.py 2026-05-08 --posts 1-10        Selected stories 1 to 10
  python3 publish-local-news.py 2026-05-08 --bonus-posts 1,5   Bonus 1 and 5
        """
    )
    parser.add_argument("date", help="Date folder (YYYY-MM-DD)")
    parser.add_argument("--only", choices=["all", "story", "bonus"], default="all",
                        help="Which set to publish (default: all)")
    parser.add_argument("--posts", help="Selected story numbers: '1-10' or '1,5,8'")
    parser.add_argument("--bonus-posts", dest="bonus_posts",
                        help="Bonus story numbers: '1-10' or '1,5,8'")
    parser.add_argument("--no-publish", action="store_true", help="Prepare data only, don't publish")
    parser.add_argument("--ui", action="store_true",
                        help="Old way: drive the editor on a focused Chrome tab (needs --tab)")
    parser.add_argument("--tab", type=int, default=4, help="Chrome tab number for --ui (default: 4)")
    parser.add_argument("--category", default="Local News", help="Lofty category (default: Local News)")
    parser.add_argument("--yes", action="store_true", help="Skip confirmation prompts")
    parser.add_argument("--force-duplicates", action="store_true",
                        help="Try to publish even if the slug already exists in Lofty")
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

    def parse_filter(spec):
        if not spec:
            return None
        nums = set()
        for part in spec.split(","):
            part = part.strip()
            if "-" in part:
                s, e = part.split("-")
                nums.update(range(int(s), int(e) + 1))
            else:
                nums.add(int(part))
        return nums

    story_filter = parse_filter(args.posts)
    bonus_filter = parse_filter(args.bonus_posts)

    scope = args.only
    # Naming a filter for only one set implies you meant just that set.
    if scope == "all" and story_filter and not bonus_filter:
        scope = "story"
    elif scope == "all" and bonus_filter and not story_filter:
        scope = "bonus"

    print(f"\nPreparing local news posts from: {date_dir}")
    posts = prepare_posts(date_dir, story_filter, bonus_filter, scope)

    n_story = sum(1 for p in posts if p["kind"] == "story")
    n_bonus = sum(1 for p in posts if p["kind"] == "bonus")
    print(f"\nFound {len(posts)} posts to publish ({n_story} selected, {n_bonus} bonus):")
    for p in posts:
        print(f"  {p['label']}: {p['title'][:60]}")
        print(f"    Slug: {p['slug']}")

    if args.no_publish:
        print("\n--no-publish flag set. Done.")
        return

    if not args.ui:
        return api_publish(posts, args)

    if not check_accessibility_permission():
        sys.exit(1)

    print(f"\nUsing Chrome {TAB}")
    print("Make sure you're logged into Lofty and on the blog dashboard.")
    if not args.yes:
        confirm = input("Proceed? (y/n): ").strip().lower()
        if confirm != "y":
            print("Cancelled.")
            return

    chrome_activate()

    # Preflight: a slug that already exists in Lofty cannot be published again.
    # The editor stays open on a validation error, which looks exactly like a
    # failed Post Now click, so catch it here instead of guessing later.
    print("\nChecking for slugs that already exist in Lofty...")
    existing = find_existing_slugs([p["slug"] for p in posts if p.get("slug")])
    if existing:
        dupes = [p for p in posts if p["slug"] in set(existing)]
        print(f"\n  {len(dupes)} of {len(posts)} slugs are ALREADY PUBLISHED:")
        for p in dupes:
            print(f"    {p['label']}: {p['slug']}")
        if args.force_duplicates:
            print("\n  --force-duplicates set, attempting them anyway.")
        else:
            posts = [p for p in posts if p["slug"] not in set(existing)]
            print(f"\n  Skipping those. {len(posts)} posts left to publish.")
            print("  To update a published post instead, use fix-local-news-blogs.py,")
            print("  or re-run with --force-duplicates.")
        if not posts:
            print("\nNothing left to publish. Done.")
            return
    elif existing is not None:
        print("  None. All slugs are new.")

    report = []
    for post in posts:
        publish_post(post, report)

    print(f"\n{'='*60}")
    print(f"DONE, {len(posts)} posts attempted")
    print(f"{'='*60}")
    ok = sum(1 for r in report if "OK" in r["status"])
    print(f"Published: {ok}/{len(posts)}")
    for r in report:
        icon = "OK" if "OK" in r["status"] else "!!"
        print(f"  [{icon}] {r['post']} — /blog/{r['slug']}")


if __name__ == "__main__":
    main()
