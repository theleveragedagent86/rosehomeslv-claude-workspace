"""
Shared helpers for Lofty landing-page + buyer-guide publishers.

Drives Chrome via AppleScript against the user's already-logged-in Lofty tab
at https://crm.lofty.com/admin/home/campaigns/landingPage. Same pattern as
publish.py (the blog publisher) — only the page-builder specifics differ.
"""

import re
import json
import subprocess
import time
from pathlib import Path

# ─── Constants ───────────────────────────────────────────────────────────────

NEW_CONSTRUCTION_BASE = Path("/Users/ryanrose/Downloads/Claude/New-Construction")
LOFTY_LANDING_URL = "https://cms.lofty.com/cmsnew/landing-page?crm=true"
GA_ID = "G-50N1D59DW6"
FB_PIXEL_ID = "621835647008401"
RECON_OUTPUT = Path("/tmp/lofty-recon.json")

# Builder name canonicalization. Long form (as it appears in research-report.md)
# → short form (for the Lofty page name and lead source).
BUILDER_SHORT = {
    "century communities": "Century",
    "pulte": "Pulte",
    "pulte homes": "Pulte",
    "del webb": "Del Webb",
    "lennar": "Lennar",
    "taylor morrison": "Taylor Morrison",
    "kb home": "KB",
    "kb homes": "KB",
    "beazer": "Beazer",
    "beazer homes": "Beazer",
    "richmond american": "Richmond American",
    "tri pointe homes": "Tri Pointe",
    "tri pointe": "Tri Pointe",
    "toll brothers": "Toll Brothers",
    "dr horton": "DR Horton",
    "d.r. horton": "DR Horton",
    "william lyon": "William Lyon",
    "ryland": "Ryland",
    "meritage homes": "Meritage",
    "meritage": "Meritage",
    "harmony homes": "Harmony",
    "woodside homes": "Woodside",
    "shea homes": "Shea",
}

ROMAN_TO_ARABIC = {
    "I": "1", "II": "2", "III": "3", "IV": "4", "V": "5",
    "VI": "6", "VII": "7", "VIII": "8", "IX": "9", "X": "10",
}


# ─── Chrome control via AppleScript ─────────────────────────────────────────

# Module-level so callers can update it after switching tabs.
_TAB = "tab 4"


def set_tab(tab_label):
    """e.g. set_tab('tab 5')"""
    global _TAB
    _TAB = tab_label


def get_tab():
    return _TAB


def chrome_js(js_code):
    """Execute JS in the active Chrome tab. Returns stdout or None on
    'missing value'. Writes JS to a temp file to dodge AppleScript escaping."""
    tmp = Path("/tmp/lofty-js-cmd.js")
    tmp.write_text(js_code)
    applescript = f'''
    set jsCode to read POSIX file "{str(tmp)}"
    tell application "Google Chrome"
        tell {_TAB} of window 1
            execute javascript jsCode
        end tell
    end tell
    '''
    result = subprocess.run(
        ["osascript", "-e", applescript],
        capture_output=True, text=True, timeout=30,
    )
    out = result.stdout.strip()
    if out == "missing value":
        return None
    return out


def chrome_activate():
    subprocess.run(
        ["osascript", "-e", 'tell application "Google Chrome" to activate'],
        capture_output=True,
    )
    time.sleep(0.3)


def chrome_tab_count():
    """Return number of tabs in window 1."""
    result = subprocess.run(
        ["osascript", "-e",
         'tell application "Google Chrome" to count of tabs of window 1'],
        capture_output=True, text=True,
    )
    try:
        return int(result.stdout.strip())
    except ValueError:
        return 0


def switch_to_newest_tab():
    """The Lofty landing-page Save action opens the builder in a new tab.
    Switch _TAB to the newest one and make it active."""
    n = chrome_tab_count()
    if n < 1:
        return False
    subprocess.run(
        ["osascript", "-e",
         f'tell application "Google Chrome" to set active tab index of window 1 to {n}'],
        capture_output=True,
    )
    set_tab(f"tab {n}")
    time.sleep(0.5)
    return True


def wait_for_element(selector, timeout=10):
    """Wait up to `timeout` seconds for a DOM element to exist."""
    for _ in range(timeout * 2):
        result = chrome_js(f"!!document.querySelector({json.dumps(selector)})")
        if result == "true":
            return True
        time.sleep(0.5)
    return False


def wait_for_text(text, timeout=10):
    """Wait for any element with the given visible text to exist."""
    safe = json.dumps(text)
    for _ in range(timeout * 2):
        result = chrome_js(f"""
        (function(t) {{
            var els = document.querySelectorAll('button, a, span, div');
            for (var i=0; i<els.length; i++) {{
                if (els[i].textContent && els[i].textContent.trim() === t) return true;
            }}
            return false;
        }})({safe})
        """)
        if result == "true":
            return True
        time.sleep(0.5)
    return False


def retry_field(func, *args, retries=3, label="field"):
    """Try a field-entry function up to `retries` times."""
    for attempt in range(retries + 1):
        if func(*args):
            return True
        if attempt < retries:
            print(f"    {label}: retry {attempt + 1}...")
            time.sleep(2)
    return False


# ─── Field-entry primitives (work on Lofty's Vue/React inputs) ──────────────

def set_input_value(selector, value):
    """Set an <input> or <textarea> value via native setter + InputEvent.
    This is the only method that reliably triggers Vue/React reactivity."""
    js = f"""
    var el = document.querySelector({json.dumps(selector)});
    if (!el) {{ 'FAIL: not found'; }}
    else {{
        el.focus();
        var proto = el.tagName === 'TEXTAREA'
            ? window.HTMLTextAreaElement.prototype
            : window.HTMLInputElement.prototype;
        var setter = Object.getOwnPropertyDescriptor(proto, 'value').set;
        setter.call(el, {json.dumps(value)});
        el.dispatchEvent(new InputEvent('input', {{bubbles: true, data: {json.dumps(value)}, inputType: 'insertText'}}));
        el.dispatchEvent(new Event('change', {{bubbles: true}}));
        'OK: ' + (el.value || '').substring(0, 60);
    }}
    """
    result = chrome_js(js)
    return result and "OK" in str(result)


def click_by_text(text, tag="*", scope_selector=None):
    """Click the first element whose trimmed textContent equals `text`.
    Optionally restrict to descendants of `scope_selector`."""
    scope_js = (f"document.querySelector({json.dumps(scope_selector)})"
                if scope_selector else "document")
    js = f"""
    var scope = {scope_js};
    if (!scope) {{ 'FAIL: scope not found'; }}
    else {{
        var els = scope.querySelectorAll({json.dumps(tag)});
        var hit = null;
        for (var i=0; i<els.length; i++) {{
            var t = (els[i].textContent || '').trim();
            if (t === {json.dumps(text)} && els[i].offsetHeight > 0) {{ hit = els[i]; break; }}
        }}
        if (hit) {{ hit.click(); 'OK'; }} else {{ 'FAIL: no match'; }}
    }}
    """
    result = chrome_js(js)
    return result and "OK" in str(result)


def click_selector(selector):
    js = f"""
    var el = document.querySelector({json.dumps(selector)});
    if (el) {{ el.click(); 'OK'; }} else {{ 'FAIL'; }}
    """
    result = chrome_js(js)
    return result and "OK" in str(result)


def paste_into_textarea(selector, value):
    """Replace textarea contents and fire input/change. For TinyMCE-style
    source-code modals where the textarea has hot Vue bindings."""
    return set_input_value(selector, value)


# ─── Recon helper ───────────────────────────────────────────────────────────

def dump_dom(label, scope_selector=None, output_path=RECON_OUTPUT):
    """Capture DOM snippets to a JSON log file so we can lock down selectors
    after a recon run. Appends to RECON_OUTPUT."""
    scope_js = (f"document.querySelector({json.dumps(scope_selector)})"
                if scope_selector else "document.body")
    js = f"""
    (function() {{
        var scope = {scope_js};
        if (!scope) return JSON.stringify({{error: 'scope not found'}});
        function describe(el) {{
            var rect = el.getBoundingClientRect();
            return {{
                tag: el.tagName,
                id: el.id || null,
                cls: el.className && el.className.toString ? el.className.toString().slice(0, 200) : null,
                role: el.getAttribute('role'),
                aria: el.getAttribute('aria-label'),
                title: el.getAttribute('title'),
                placeholder: el.getAttribute('placeholder'),
                text: (el.textContent || '').trim().slice(0, 80),
                visible: rect.width > 0 && rect.height > 0,
            }};
        }}
        var snapshot = {{
            url: window.location.href,
            title: document.title,
            buttons: [],
            inputs: [],
            interactive: [],
        }};
        scope.querySelectorAll('button').forEach(function(b) {{ snapshot.buttons.push(describe(b)); }});
        scope.querySelectorAll('input, textarea, select').forEach(function(i) {{ snapshot.inputs.push(describe(i)); }});
        scope.querySelectorAll('[role=button], [draggable=true], [data-testid]').forEach(function(i) {{ snapshot.interactive.push(describe(i)); }});
        return JSON.stringify(snapshot);
    }})()
    """
    raw = chrome_js(js)
    if not raw:
        print(f"    [recon] {label}: chrome_js returned nothing")
        return
    try:
        snap = json.loads(raw)
    except json.JSONDecodeError:
        print(f"    [recon] {label}: could not parse JSON")
        return
    record = {"label": label, "snapshot": snap}
    existing = []
    if output_path.exists():
        try:
            existing = json.loads(output_path.read_text())
        except json.JSONDecodeError:
            existing = []
    existing.append(record)
    output_path.write_text(json.dumps(existing, indent=2))
    print(f"    [recon] {label}: dumped to {output_path}")


# ─── Community-folder data extraction ───────────────────────────────────────

def find_community_dir(community_arg):
    """Resolve `community_arg` (slug, folder name, or absolute path) to a real
    community directory under New-Construction/."""
    p = Path(community_arg).expanduser()
    if p.is_absolute() and p.is_dir():
        return p
    direct = NEW_CONSTRUCTION_BASE / community_arg
    if direct.is_dir():
        return direct
    for child in NEW_CONSTRUCTION_BASE.iterdir():
        if child.is_dir() and child.name.lower() == community_arg.lower():
            return child
    return None


def read_builder_name(community_dir):
    """Extract the short builder name from research-report.md.
    Tolerates several formats: '**Builder:**', '**Builder name:**',
    '**Builder Name:**', '### <Builder> (sole builder)' under '## Builders'.
    Returns e.g. 'Century' or None if not found."""
    rr = community_dir / "research-report.md"
    if not rr.exists():
        return None
    text = rr.read_text(encoding="utf-8", errors="replace")

    # Try '**Builder:**' / '**Builder name:**' / '**Builder Name:**'.
    # Skip lines like '**Builder parent community:**' or '**Builder URL:**'.
    for line in text.splitlines():
        m = re.match(
            r"^\s*[-*]?\s*\*\*Builder(?:s|\s+[Nn]ame)?:\*\*\s*(.+?)\s*$",
            line,
        )
        if m:
            return _normalize_builder(m.group(1))

    # Fallback: '### <Builder> (sole builder)' under a '## Builders' heading.
    m = re.search(r"^##\s+Builders?\s*$", text, re.MULTILINE)
    if m:
        after = text[m.end():]
        m2 = re.search(r"^###\s+(.+?)$", after, re.MULTILINE)
        if m2:
            return _normalize_builder(m2.group(1))

    return None


def _normalize_builder(raw):
    raw = raw.strip().rstrip(".").rstrip(",")
    raw = re.sub(r"\s*\(.*?\)\s*", "", raw)
    raw = re.sub(r",\s*(Inc\.?|LLC|Corp\.?|Company|Co\.?)$", "", raw, flags=re.I)
    raw = raw.strip()
    return BUILDER_SHORT.get(raw.lower(), raw)


def _strip_parens(s):
    return re.sub(r"\s*\(.*?\)\s*", "", s).strip()


def _roman_to_arabic(s):
    def repl(m):
        return ROMAN_TO_ARABIC.get(m.group(0), m.group(0))
    return re.sub(r"\b(I{1,3}|IV|VI{0,3}|IX|X)\b", repl, s)


def derive_dev_name(community_dir, builder_short=None):
    """Pull a clean development name from research-report.md's 'Official
    [community] name'. Strips parentheticals, drops a leading 'The ',
    converts roman numerals to arabic. Falls back to folder-name conversion
    if research-report is missing or doesn't have the field."""
    rr = community_dir / "research-report.md"
    name = None
    if rr.exists():
        text = rr.read_text(encoding="utf-8", errors="replace")
        for pat in (
            r"\*\*Official\s+community\s+name:\*\*\s*(.+?)(?:\n|$)",
            r"\*\*Official\s+name:\*\*\s*(.+?)(?:\n|$)",
            r"\*\*Community\s+name:\*\*\s*(.+?)(?:\n|$)",
            r"#\s*RESEARCH\s+REPORT:\s*(.+?)(?:\(|\n|$)",
        ):
            m = re.search(pat, text, re.IGNORECASE)
            if m:
                name = m.group(1).strip()
                break
    if not name:
        name = community_dir.name.replace("-", " ")
        if builder_short and f" by {builder_short.lower()}" in name.lower():
            name = re.sub(rf"\s+by\s+{re.escape(builder_short)}.*$", "",
                          name, flags=re.IGNORECASE)
        name = name.title()

    name = _strip_parens(name)
    name = re.sub(r"^The\s+", "", name)
    name = _roman_to_arabic(name)
    if builder_short:
        pat = re.compile(rf"\s+by\s+{re.escape(builder_short)}.*$", re.IGNORECASE)
        name = pat.sub("", name)
    return name.strip()


# ─── SEO loader ─────────────────────────────────────────────────────────────

def read_seo_block(community_dir, section_heading_regex):
    """Pull <title> and <meta name="description"> from a section of
    seo-package.md whose heading matches `section_heading_regex`.
    Returns (meta_title, meta_description) or (None, None)."""
    seo = community_dir / "seo-package.md"
    if not seo.exists():
        return None, None
    text = seo.read_text(encoding="utf-8", errors="replace")
    sections = re.split(r"^##\s+", text, flags=re.MULTILINE)
    target = None
    for s in sections:
        first_line = s.split("\n", 1)[0]
        if re.search(section_heading_regex, first_line, re.IGNORECASE):
            target = s
            break
    if not target:
        return None, None
    title = None
    desc = None
    m = re.search(r"<title>([^<]+)</title>", target)
    if m:
        title = m.group(1).strip()
    m = re.search(
        r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']+)["\']',
        target,
    )
    if m:
        desc = m.group(1).strip()
    return title, desc


# ─── Naming derivations ─────────────────────────────────────────────────────

def compact_dev(dev_name):
    """'Bluffs 1' → 'Bluffs1'. Strips spaces."""
    return re.sub(r"\s+", "", dev_name)


def page_display_name(builder_short, dev_name, is_buyer_guide=False):
    """e.g. 'Century - Bluffs 1' or 'Century - Bluffs 1 BG'"""
    base = f"{builder_short} - {dev_name}"
    return f"{base} BG" if is_buyer_guide else base


def lead_source_name(builder_short, dev_name, is_buyer_guide=False):
    """e.g. 'Century-Bluffs1' or 'Century-Bluffs1 BG'"""
    base = f"{builder_short}-{compact_dev(dev_name)}"
    return f"{base} BG" if is_buyer_guide else base


def url_slug(builder_short, dev_name, is_buyer_guide=False):
    """Destination-URL slug. e.g. 'century-bluffs1' or 'century-bluffs1-BG'"""
    base = f"{builder_short.lower()}-{compact_dev(dev_name).lower()}"
    return f"{base}-BG" if is_buyer_guide else base


# ─── HTML loader ────────────────────────────────────────────────────────────

def read_source_html(community_dir, filename):
    path = community_dir / filename
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")
