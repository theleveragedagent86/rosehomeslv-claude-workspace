#!/usr/bin/env python3
"""
Listing Leads Page Scraper
===========================
Scrapes specific pages from listingleads.com: blueprints, campaign libraries,
and the designs editor. Organizes content into the existing Listing Leads
Content folder structure.

Usage:
    python3 scrape_listing_leads_pages.py --tab 1                     # Scrape all 8 URLs
    python3 scrape_listing_leads_pages.py --tab 1 --discover           # DOM discovery on current page
    python3 scrape_listing_leads_pages.py --tab 1 --discover --url URL # DOM discovery on specific URL
    python3 scrape_listing_leads_pages.py --tab 1 --url URL            # Scrape one specific URL
    python3 scrape_listing_leads_pages.py --tab 1 --type blueprints    # Only blueprints
    python3 scrape_listing_leads_pages.py --tab 1 --type campaigns     # Only campaign libraries
    python3 scrape_listing_leads_pages.py --tab 1 --type designs       # Only designs
    python3 scrape_listing_leads_pages.py --tab 1 --resume             # Resume from checkpoint
    python3 scrape_listing_leads_pages.py --tab 1 --no-download        # Skip file downloads
    python3 scrape_listing_leads_pages.py --tab 1 --list               # Print target URLs and exit

Requirements: macOS, Google Chrome (with View > Developer > Allow JavaScript
from Apple Events enabled), logged into listingleads.com.
"""

import sys
import os
import re
import json
import subprocess
import argparse
import time
import urllib.parse
from pathlib import Path
from datetime import datetime

try:
    import requests
except ImportError:
    print("ERROR: requests not installed. Run: pip3 install requests")
    sys.exit(1)


# --- Configuration -----------------------------------------------------------

TAB = "tab 1"
OUTPUT_DIR = Path("/Users/ryanrose/Downloads/Claude/Listing Leads Content")
CHECKPOINT_FILE = Path("/tmp/listing_leads_pages_progress.json")

# Target URLs organized by type
TARGETS = {
    "blueprints": [
        {
            "url": "https://www.listingleads.com/blueprints/the-2026-expired-marketing-blueprint",
            "name": "2026 Expired Marketing Blueprint",
        },
        {
            "url": "https://www.listingleads.com/blueprints/the-silver-tsunami-blueprint",
            "name": "Silver Tsunami Blueprint",
        },
        {
            "url": "https://www.listingleads.com/blueprints/fsbo-blueprint",
            "name": "FSBO Blueprint",
        },
    ],
    "campaigns": [
        {
            "url": "https://www.listingleads.com/campaigns/phone-text-scripts",
            "folder": "Phone & Text Scripts",
        },
        {
            "url": "https://www.listingleads.com/campaigns/email",
            "folder": "Email Campaigns",
        },
        {
            "url": "https://www.listingleads.com/campaigns/direct-mail",
            "folder": "Direct Mail Templates",
        },
        {
            "url": "https://www.listingleads.com/campaigns/social",
            "folder": "Social Shareables",
        },
    ],
    "designs": [
        {
            "url": "https://app.listingleads.com/designs",
            "name": "Expired Editor Designs",
        },
    ],
}


# --- Chrome Control -----------------------------------------------------------

def chrome_js(js_code):
    """Execute JS in Chrome tab via AppleScript using temp file."""
    tmp = Path("/tmp/ll-pages-js-cmd.js")
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
            capture_output=True, text=True, timeout=60
        )
        out = result.stdout.strip()
        if out == "missing value":
            return None
        return out
    except subprocess.TimeoutExpired:
        print("  WARNING: Chrome JS execution timed out")
        return None


def chrome_activate():
    subprocess.run(
        ['osascript', '-e', 'tell application "Google Chrome" to activate'],
        capture_output=True
    )
    time.sleep(0.3)


def wait_for_element(selector, timeout=10):
    """Wait for a DOM element to exist."""
    for _ in range(timeout * 2):
        result = chrome_js(f"!!document.querySelector('{selector}')")
        if result == "true":
            return True
        time.sleep(0.5)
    return False


def get_current_url():
    """Get the current URL of the Chrome tab."""
    applescript = f'''
    tell application "Google Chrome"
        tell {TAB} of window 1
            get URL
        end tell
    end tell
    '''
    result = subprocess.run(['osascript', '-e', applescript], capture_output=True, text=True)
    return result.stdout.strip()


def navigate_to(url):
    """Navigate Chrome tab to a URL."""
    applescript = f'''
    tell application "Google Chrome"
        tell {TAB} of window 1
            set URL to "{url}"
        end tell
    end tell
    '''
    subprocess.run(['osascript', '-e', applescript], capture_output=True, text=True)
    time.sleep(3)


def sanitize_filename(name, max_len=80):
    """Create a safe filename from text."""
    name = re.sub(r'[<>:"/\\|?*\[\]]', '', name)
    name = re.sub(r'\s+', '_', name.strip())
    name = re.sub(r'_+', '_', name)
    if len(name) > max_len:
        name = name[:max_len]
    return name or "untitled"


def scroll_to_bottom():
    """Scroll down in steps to trigger lazy-loaded content."""
    chrome_js("""
    (function() {
        var totalHeight = document.body.scrollHeight;
        var step = 800;
        var current = 0;
        var timer = setInterval(function() {
            current += step;
            window.scrollTo(0, current);
            if (current >= totalHeight) {
                clearInterval(timer);
            }
        }, 200);
    })()
    """)
    time.sleep(4)
    # Scroll back to top
    chrome_js("window.scrollTo(0, 0)")
    time.sleep(0.5)


# --- Cookie Extraction & File Downloads ---------------------------------------

def get_chrome_cookies():
    """Extract cookies from Chrome for authenticated downloads."""
    cookies_str = chrome_js("document.cookie")
    jar = {}
    if cookies_str:
        for pair in cookies_str.split(';'):
            pair = pair.strip()
            if '=' in pair:
                k, v = pair.split('=', 1)
                jar[k.strip()] = v.strip()
    return jar


def download_file(url, dest_path, cookies=None):
    """Download a file from a URL to the destination path."""
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
        }
        resp = requests.get(url, headers=headers, timeout=30, stream=True, allow_redirects=True)
        if resp.status_code in (401, 403) and cookies:
            resp = requests.get(url, headers=headers, cookies=cookies, timeout=30,
                                stream=True, allow_redirects=True)

        if resp.status_code == 200:
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            with open(dest_path, 'wb') as f:
                for chunk in resp.iter_content(chunk_size=8192):
                    f.write(chunk)
            size_kb = dest_path.stat().st_size / 1024
            print(f"    Downloaded ({size_kb:.0f} KB): {dest_path.name}")
            return True
        else:
            print(f"    Download failed ({resp.status_code}): {url[:80]}")
            return False
    except Exception as e:
        print(f"    Download error: {e}")
        return False


def guess_extension(url):
    """Guess file extension from URL."""
    parsed = urllib.parse.urlparse(url)
    path = parsed.path.lower()
    for ext in ['.pdf', '.png', '.jpg', '.jpeg', '.gif', '.svg', '.mp4',
                '.zip', '.docx', '.xlsx', '.webp']:
        if ext in path:
            return ext
    if '_next/image' in url:
        query = urllib.parse.parse_qs(parsed.query)
        orig_url = query.get('url', [''])[0]
        if orig_url:
            return guess_extension(orig_url)
        return '.png'
    return ''


# --- DOM Discovery ------------------------------------------------------------

def discover_page(url=None):
    """Generic DOM discovery for any URL. Dumps structure to terminal."""
    if url:
        print(f"\nNavigating to: {url}")
        navigate_to(url)
        time.sleep(3)

    current = get_current_url()
    print("\n" + "=" * 70)
    print("PAGE DISCOVERY")
    print("=" * 70)
    print(f"Current URL: {current}")

    # Check for login redirect
    if '/login' in current or '/sign-in' in current or '/signin' in current:
        print("\nWARNING: Redirected to login page! You need to log in first.")
        return

    print("\n--- FULL PAGE TEXT (first 15000 chars) ---")
    result = chrome_js("""
    (function() {
        var main = document.querySelector('main') || document.body;
        return main.innerText.substring(0, 15000);
    })()
    """)
    print(result or "(no results)")

    print("\n--- HEADINGS ---")
    result = chrome_js("""
    (function() {
        var headings = document.querySelectorAll('h1, h2, h3, h4');
        var items = [];
        headings.forEach(function(el) {
            items.push({
                tag: el.tagName,
                text: el.textContent.trim().substring(0, 200),
                classes: el.className.toString().substring(0, 100)
            });
        });
        return JSON.stringify(items, null, 2);
    })()
    """)
    print(result or "(no results)")

    print("\n--- CONTENT SECTIONS ---")
    result = chrome_js("""
    (function() {
        var els = document.querySelectorAll(
            '[class*="content"], [class*="body"], [class*="description"], ' +
            '[class*="script"], [class*="copy"], [class*="template"], ' +
            'article, section, [class*="campaign"], [class*="detail"], ' +
            '[class*="card"], [class*="grid"], [class*="list"]'
        );
        var items = [];
        els.forEach(function(el) {
            var rect = el.getBoundingClientRect();
            if (rect.width > 100 && rect.height > 50 && items.length < 40) {
                items.push({
                    tag: el.tagName,
                    classes: el.className.toString().substring(0, 150),
                    textPreview: el.textContent.trim().substring(0, 300),
                    childCount: el.children.length,
                    id: el.id
                });
            }
        });
        return JSON.stringify(items, null, 2);
    })()
    """)
    print(result or "(no results)")

    print("\n--- ALL LINKS ---")
    result = chrome_js("""
    (function() {
        var links = document.querySelectorAll('a[href]');
        var items = [];
        links.forEach(function(el) {
            var rect = el.getBoundingClientRect();
            if (rect.width > 0 && rect.height > 0) {
                items.push({
                    href: el.href,
                    text: el.textContent.trim().substring(0, 100),
                    classes: el.className.toString().substring(0, 80)
                });
            }
        });
        return JSON.stringify(items, null, 2);
    })()
    """)
    print(result or "(no results)")

    print("\n--- ALL IMAGES ---")
    result = chrome_js("""
    (function() {
        var imgs = document.querySelectorAll('img[src]');
        var items = [];
        imgs.forEach(function(el) {
            var rect = el.getBoundingClientRect();
            if (rect.width > 20 && rect.height > 20) {
                items.push({
                    src: el.src.substring(0, 250),
                    alt: el.alt,
                    size: Math.round(rect.width) + 'x' + Math.round(rect.height)
                });
            }
        });
        return JSON.stringify(items, null, 2);
    })()
    """)
    print(result or "(no results)")

    print("\n--- BUTTONS ---")
    result = chrome_js("""
    (function() {
        var btns = document.querySelectorAll('button');
        var items = [];
        btns.forEach(function(el) {
            var rect = el.getBoundingClientRect();
            if (rect.width > 0 && rect.height > 0 && items.length < 30) {
                items.push({
                    text: el.textContent.trim().substring(0, 100),
                    classes: el.className.toString().substring(0, 120),
                    type: el.type || ''
                });
            }
        });
        return JSON.stringify(items, null, 2);
    })()
    """)
    print(result or "(no results)")

    print("\n--- DOWNLOAD LINKS & BUTTONS ---")
    result = chrome_js("""
    (function() {
        var els = document.querySelectorAll(
            'a[href*="download"], a[download], a[href*=".pdf"], a[href*=".png"], ' +
            'a[href*=".jpg"], a[href*=".zip"], a[href*=".docx"], ' +
            'a[href*="canva"], a[href*="drive.google"], a[href*="dropbox"], ' +
            'button[class*="download"], [class*="download"], ' +
            'a[href*="imagekit"], a[href*="s3.amazonaws"]'
        );
        var items = [];
        els.forEach(function(el) {
            items.push({
                tag: el.tagName,
                href: el.href || '',
                text: el.textContent.trim().substring(0, 100),
                classes: el.className.toString().substring(0, 120)
            });
        });
        return JSON.stringify(items, null, 2);
    })()
    """)
    print(result or "(no results)")

    print("\n--- IFRAMES & VIDEOS ---")
    result = chrome_js("""
    (function() {
        var items = [];
        document.querySelectorAll('iframe').forEach(function(el) {
            items.push({tag: 'IFRAME', src: el.src, width: el.width, height: el.height});
        });
        document.querySelectorAll('video').forEach(function(el) {
            items.push({
                tag: 'VIDEO',
                src: el.src || (el.querySelector('source') || {}).src || '',
                poster: el.poster || ''
            });
        });
        return JSON.stringify(items, null, 2);
    })()
    """)
    print(result or "(no results)")

    print("\n--- OUTER HTML (first 10000 chars) ---")
    result = chrome_js("""
    (function() {
        var main = document.querySelector('main') || document.body;
        return main.outerHTML.substring(0, 10000);
    })()
    """)
    print(result or "(no results)")


# --- Campaign Detail Scraper (from existing script) --------------------------

def scrape_campaign_detail(url):
    """
    Navigate to a campaign detail page and scrape all content.
    Reused from scrape_listing_leads.py.
    """
    navigate_to(url)
    time.sleep(3)
    wait_for_element('section', timeout=10)
    time.sleep(1)

    result = chrome_js("""
    (function() {
        var data = {sections: [], copy_blocks: [], images: [], videos: [], links: []};

        var container = document.querySelector('.w-full.h-full.bg-background') ||
                        document.querySelector('main .flex-1') ||
                        document.querySelector('main') || document.body;

        data.full_text = container.innerText.substring(0, 20000);

        var sections = container.querySelectorAll('section');
        sections.forEach(function(sec) {
            var heading = sec.querySelector('h2, h3, h4, [class*="heading"]');
            var headingText = heading ? heading.textContent.trim() : '';
            data.sections.push({
                heading: headingText,
                text: sec.innerText.substring(0, 5000),
                html: sec.innerHTML.substring(0, 8000)
            });
        });

        var allButtons = container.querySelectorAll('button');
        var copyBtnIndex = 0;
        allButtons.forEach(function(btn) {
            var btnText = btn.textContent.trim();
            if (btnText !== 'Copy' && btnText !== 'Copied!') return;
            copyBtnIndex++;
            var parent = btn.parentElement;
            for (var i = 0; i < 6 && parent; i++) {
                if (parent.tagName === 'SECTION') break;
                var children = parent.children;
                var contentParts = [];
                var foundBtn = false;
                for (var j = 0; j < children.length; j++) {
                    var child = children[j];
                    if (child === btn || child.contains(btn)) {
                        foundBtn = true;
                        continue;
                    }
                    var t = child.textContent.trim();
                    if (child.tagName === 'BUTTON') continue;
                    if (t === 'Copy' || t === 'Copied!') continue;
                    if (t.length > 3) contentParts.push(t);
                }
                if (foundBtn && contentParts.length > 0) {
                    var content = contentParts.join('\\n');
                    var label = '';
                    var prevSib = parent.previousElementSibling;
                    while (prevSib) {
                        var prevText = prevSib.textContent.trim();
                        if (prevText.length > 0 && prevText.length < 60 && prevText !== 'Copy') {
                            label = prevText;
                            break;
                        }
                        prevSib = prevSib.previousElementSibling;
                    }
                    if (!label) label = 'Copy Block ' + copyBtnIndex;
                    data.copy_blocks.push({
                        label: label,
                        content: content.substring(0, 3000)
                    });
                    break;
                }
                parent = parent.parentElement;
            }
        });

        container.querySelectorAll('img[src]').forEach(function(img) {
            var rect = img.getBoundingClientRect();
            if (rect.width > 80 && rect.height > 80) {
                var src = img.src;
                if (src.indexOf('/_next/image') > -1) {
                    try {
                        var urlObj = new URL(src);
                        var origUrl = urlObj.searchParams.get('url');
                        if (origUrl) src = origUrl;
                    } catch(e) {}
                }
                if (src.indexOf('logo') === -1) {
                    data.images.push({
                        src: src,
                        alt: img.alt || '',
                        size: Math.round(rect.width) + 'x' + Math.round(rect.height)
                    });
                }
            }
        });

        container.querySelectorAll('iframe').forEach(function(f) {
            if (f.src) data.videos.push({src: f.src, type: 'iframe'});
        });
        container.querySelectorAll('video').forEach(function(v) {
            var src = v.src || '';
            var source = v.querySelector('source');
            if (source && source.src) src = source.src;
            if (src) data.videos.push({src: src, type: 'video'});
        });

        container.querySelectorAll('a[href]').forEach(function(a) {
            var rect = a.getBoundingClientRect();
            var href = a.href || '';
            if (rect.width > 0 && rect.height > 0 && href.indexOf('listingleads.com/campaigns') === -1
                && href.indexOf('listingleads.com/plan') === -1
                && href.indexOf('listingleads.com/social') === -1
                && href.indexOf('listingleads.com/favorites') === -1
                && href.indexOf('listingleads.com/blueprints') === -1
                && href.indexOf('listingleads.com/coaching') === -1
                && href.indexOf('listingleads.com/viral') === -1) {
                data.links.push({
                    href: href,
                    text: a.textContent.trim().substring(0, 150),
                    download: a.getAttribute('download') || ''
                });
            }
        });

        data.download_buttons = [];
        container.querySelectorAll('a[download], a[href*="download"], a[href*=".pdf"], a[href*=".zip"], a[href*=".docx"]').forEach(function(el) {
            data.download_buttons.push({
                href: el.href || '',
                text: el.textContent.trim().substring(0, 100)
            });
        });

        return JSON.stringify(data);
    })()
    """)

    if not result:
        return None
    try:
        return json.loads(result)
    except json.JSONDecodeError:
        return {"full_text": result}


# --- Blueprint Scraper --------------------------------------------------------

def scrape_blueprint_page(url):
    """Scrape a blueprint page for all content."""
    print(f"\n  Navigating to blueprint: {url}")
    navigate_to(url)
    time.sleep(4)

    # Check for login redirect
    current = get_current_url()
    if '/login' in current or '/sign-in' in current:
        print("  ERROR: Redirected to login page. Log in first!")
        return None

    # Wait for content
    wait_for_element('h1', timeout=15)
    time.sleep(1)

    # Scroll to trigger lazy loading
    print("  Scrolling to load all content...")
    scroll_to_bottom()

    # Get page title
    title = chrome_js("""
    (function() {
        var h1 = document.querySelector('h1');
        return h1 ? h1.textContent.trim() : '';
    })()
    """) or ""

    print(f"  Title: {title}")

    # Scrape content using same approach as campaign detail
    # but with broader extraction for long-form content
    result = chrome_js("""
    (function() {
        var data = {sections: [], copy_blocks: [], images: [], videos: [], links: []};

        var container = document.querySelector('.w-full.h-full.bg-background') ||
                        document.querySelector('main .flex-1') ||
                        document.querySelector('main') || document.body;

        data.full_text = container.innerText.substring(0, 30000);

        // Extract sections
        var sections = container.querySelectorAll('section, [class*="section"]');
        if (sections.length === 0) {
            // Fallback: use headings to define sections
            var headings = container.querySelectorAll('h2, h3');
            headings.forEach(function(h) {
                var text = '';
                var el = h.nextElementSibling;
                while (el && !el.matches('h2, h3')) {
                    text += el.textContent.trim() + '\\n';
                    el = el.nextElementSibling;
                    if (text.length > 5000) break;
                }
                data.sections.push({
                    heading: h.textContent.trim(),
                    text: text.substring(0, 5000)
                });
            });
        } else {
            sections.forEach(function(sec) {
                var heading = sec.querySelector('h2, h3, h4, [class*="heading"]');
                var headingText = heading ? heading.textContent.trim() : '';
                data.sections.push({
                    heading: headingText,
                    text: sec.innerText.substring(0, 5000)
                });
            });
        }

        // Extract copy blocks (same approach as campaign detail)
        var allButtons = container.querySelectorAll('button');
        var copyBtnIndex = 0;
        allButtons.forEach(function(btn) {
            var btnText = btn.textContent.trim();
            if (btnText !== 'Copy' && btnText !== 'Copied!') return;
            copyBtnIndex++;
            var parent = btn.parentElement;
            for (var i = 0; i < 6 && parent; i++) {
                if (parent.tagName === 'SECTION') break;
                var children = parent.children;
                var contentParts = [];
                var foundBtn = false;
                for (var j = 0; j < children.length; j++) {
                    var child = children[j];
                    if (child === btn || child.contains(btn)) {
                        foundBtn = true;
                        continue;
                    }
                    var t = child.textContent.trim();
                    if (child.tagName === 'BUTTON') continue;
                    if (t === 'Copy' || t === 'Copied!') continue;
                    if (t.length > 3) contentParts.push(t);
                }
                if (foundBtn && contentParts.length > 0) {
                    var content = contentParts.join('\\n');
                    var label = '';
                    var prevSib = parent.previousElementSibling;
                    while (prevSib) {
                        var prevText = prevSib.textContent.trim();
                        if (prevText.length > 0 && prevText.length < 60 && prevText !== 'Copy') {
                            label = prevText;
                            break;
                        }
                        prevSib = prevSib.previousElementSibling;
                    }
                    if (!label) label = 'Copy Block ' + copyBtnIndex;
                    data.copy_blocks.push({
                        label: label,
                        content: content.substring(0, 3000)
                    });
                    break;
                }
                parent = parent.parentElement;
            }
        });

        // Images
        container.querySelectorAll('img[src]').forEach(function(img) {
            var rect = img.getBoundingClientRect();
            if (rect.width > 80 && rect.height > 80) {
                var src = img.src;
                if (src.indexOf('/_next/image') > -1) {
                    try {
                        var urlObj = new URL(src);
                        var origUrl = urlObj.searchParams.get('url');
                        if (origUrl) src = origUrl;
                    } catch(e) {}
                }
                if (src.indexOf('logo') === -1) {
                    data.images.push({src: src, alt: img.alt || '', size: Math.round(rect.width) + 'x' + Math.round(rect.height)});
                }
            }
        });

        // Videos
        container.querySelectorAll('iframe').forEach(function(f) {
            if (f.src) data.videos.push({src: f.src, type: 'iframe'});
        });
        container.querySelectorAll('video').forEach(function(v) {
            var src = v.src || '';
            var source = v.querySelector('source');
            if (source && source.src) src = source.src;
            if (src) data.videos.push({src: src, type: 'video'});
        });

        // All links (both external and internal listingleads.com links)
        data.internal_links = [];
        container.querySelectorAll('a[href]').forEach(function(a) {
            var rect = a.getBoundingClientRect();
            var href = a.href || '';
            if (rect.width <= 0 || rect.height <= 0 || href.indexOf('#') === 0) return;

            if (href.indexOf('listingleads.com') > -1) {
                // Internal link -- save separately for link-following
                // Skip nav/category pages, only keep detail pages
                if (!href.match(/\\/(plan|blueprints|coaching|viral|favorites|phone-text-scripts|direct-mail|social)\\/?$/)
                    && !href.match(/\\/campaigns\\/(email)\\/?$/)) {
                    data.internal_links.push({
                        href: href,
                        text: a.textContent.trim().substring(0, 150)
                    });
                }
            } else {
                data.links.push({
                    href: href,
                    text: a.textContent.trim().substring(0, 150),
                    download: a.getAttribute('download') || ''
                });
            }
        });

        // Download buttons
        data.download_buttons = [];
        container.querySelectorAll('a[download], a[href*="download"], a[href*=".pdf"], a[href*=".zip"], a[href*=".docx"]').forEach(function(el) {
            data.download_buttons.push({
                href: el.href || '',
                text: el.textContent.trim().substring(0, 100)
            });
        });

        return JSON.stringify(data);
    })()
    """)

    if not result:
        print("  WARNING: No content extracted from blueprint page")
        return None

    try:
        data = json.loads(result)
    except json.JSONDecodeError:
        data = {"full_text": result}

    data["title"] = title
    data["url"] = url

    # If full_text was truncated, try to get more in a second pass
    full_text = data.get("full_text", "")
    if len(full_text) >= 29000:
        print("  Content is long, fetching remainder...")
        more = chrome_js("""
        (function() {
            var container = document.querySelector('.w-full.h-full.bg-background') ||
                            document.querySelector('main .flex-1') ||
                            document.querySelector('main') || document.body;
            return container.innerText.substring(30000, 60000);
        })()
        """)
        if more:
            data["full_text"] = full_text + more

    return data


def save_blueprint(data, blueprint_info, download_files=True, cookies=None):
    """Save blueprint content to Blueprints/ folder."""
    if not data:
        return []

    saved_files = []
    bp_name = sanitize_filename(blueprint_info.get("name", data.get("title", "untitled")))
    base_dir = OUTPUT_DIR / "Blueprints" / bp_name
    base_dir.mkdir(parents=True, exist_ok=True)

    # 1. Save full content as markdown
    title = data.get("title", blueprint_info.get("name", ""))
    sections = data.get("sections", [])
    full_text = data.get("full_text", "")

    md_content = f"# {title}\n\n"
    md_content += f"Source: {data.get('url', '')}\n\n"

    if sections:
        for sec in sections:
            heading = sec.get("heading", "")
            text = sec.get("text", "")
            if heading:
                md_content += f"## {heading}\n\n"
            if text:
                md_content += f"{text}\n\n"
    elif full_text:
        md_content += full_text

    md_file = base_dir / "full_content.md"
    md_file.write_text(md_content.strip(), encoding="utf-8")
    saved_files.append(str(md_file))
    print(f"  Saved: {md_file.name} ({len(md_content)} chars)")

    # 2. Save copy blocks
    copy_blocks = data.get("copy_blocks", [])
    if copy_blocks:
        copy_text = ""
        for block in copy_blocks:
            label = block.get("label", "")
            content = block.get("content", "")
            if label:
                copy_text += f"=== {label} ===\n"
            copy_text += f"{content}\n\n"
        if copy_text.strip():
            copy_file = base_dir / "copy_blocks.txt"
            copy_file.write_text(copy_text.strip(), encoding="utf-8")
            saved_files.append(str(copy_file))
            print(f"  Saved: {copy_file.name} ({len(copy_blocks)} blocks)")

    # 3. Save external resource links
    ext_links = data.get("links", [])
    if ext_links:
        links_text = "External Resources & Tools\n" + "=" * 30 + "\n\n"
        for link in ext_links:
            href = link.get("href", "")
            text = link.get("text", "")
            if href:
                links_text += f"- {text}\n  {href}\n\n"
        if links_text.count("\n") > 4:
            links_file = base_dir / "resources.txt"
            links_file.write_text(links_text.strip(), encoding="utf-8")
            saved_files.append(str(links_file))
            print(f"  Saved: {links_file.name}")

    # 4. Save video URLs
    videos = data.get("videos", [])
    video_links = [v.get("src", "") for v in videos if v.get("src")]
    for link in ext_links:
        href = link.get("href", "")
        if any(v in href.lower() for v in ['youtube.com', 'youtu.be', 'vimeo.com', 'wistia', 'loom']):
            video_links.append(href)
    if video_links:
        vid_file = base_dir / "videos.txt"
        vid_file.write_text("\n".join(sorted(set(video_links))), encoding="utf-8")
        saved_files.append(str(vid_file))
        print(f"  Saved: {vid_file.name} ({len(video_links)} videos)")

    # 5. Download images
    if download_files:
        seen_urls = set()
        for img in data.get("images", []):
            src = img.get("src", "")
            if not src or src in seen_urls:
                continue
            seen_urls.add(src)
            ext = guess_extension(src) or '.png'
            alt = sanitize_filename(img.get("alt", "")) or f"image_{len(seen_urls)}"
            dest = base_dir / f"{alt}{ext}"
            if not dest.exists():
                if download_file(src, dest, cookies):
                    saved_files.append(str(dest))
                time.sleep(0.5)

        for dl in data.get("download_buttons", []):
            href = dl.get("href", "")
            if not href or href in seen_urls:
                continue
            seen_urls.add(href)
            ext = guess_extension(href) or '.pdf'
            dl_name = sanitize_filename(dl.get("text", "")) or "download"
            dest = base_dir / f"{dl_name}{ext}"
            if not dest.exists():
                if download_file(href, dest, cookies):
                    saved_files.append(str(dest))
                time.sleep(0.5)

    # 6. Save raw JSON
    raw_file = base_dir / "raw_data.json"
    raw_file.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

    return saved_files


# --- Campaign Library Scraper ------------------------------------------------

def scrape_campaign_library_page(url):
    """
    Scrape a campaign library page to get all campaign card URLs.
    Returns list of campaign card dicts with url, title.
    """
    print(f"\n  Navigating to library: {url}")
    navigate_to(url)
    time.sleep(3)

    # Check for login redirect
    current = get_current_url()
    if '/login' in current or '/sign-in' in current:
        print("  ERROR: Redirected to login page. Log in first!")
        return []

    # Wait for content
    wait_for_element('a', timeout=10)
    time.sleep(1)

    # Scroll to load all cards
    print("  Scrolling to load all campaign cards...")
    prev_count = 0
    for attempt in range(10):
        scroll_to_bottom()
        time.sleep(2)

        # Check for "Load More" or "Show More" buttons
        chrome_js("""
        (function() {
            var btns = document.querySelectorAll('button');
            btns.forEach(function(b) {
                var t = b.textContent.trim().toLowerCase();
                if (t.indexOf('load more') > -1 || t.indexOf('show more') > -1 || t.indexOf('see more') > -1) {
                    b.click();
                }
            });
        })()
        """)
        time.sleep(1)

        # Count current cards
        count = chrome_js("""
        (function() {
            var links = document.querySelectorAll('a[href*="/campaigns/"]');
            return links.length.toString();
        })()
        """)
        current_count = int(count) if count and count.isdigit() else 0

        if current_count == prev_count and attempt > 0:
            break
        prev_count = current_count

    # Extract all campaign card links (broad search, then filter)
    result = chrome_js("""
    (function() {
        var cards = [];
        var seen = {};

        // Strategy 1: Look for links to /campaigns/ detail pages
        var links = document.querySelectorAll('a[href*="/campaigns/"]');
        links.forEach(function(a) {
            var href = a.href;
            // Skip library/category links (the pages we're already on)
            if (href.match(/\\/campaigns\\/(phone-text-scripts|email|direct-mail|social)\\/?$/)) return;
            // Skip nav/sidebar links
            if (href.match(/\\/campaigns\\/(plan|blueprints|coaching|viral|favorites)\\/?/)) return;
            if (seen[href]) return;
            seen[href] = true;

            var title = '';
            var h = a.querySelector('h2, h3, h4, [class*="title"]');
            if (h) {
                title = h.textContent.trim();
            } else {
                title = a.textContent.trim().substring(0, 100);
            }

            var img = a.querySelector('img');
            var thumb = img ? img.src : '';

            cards.push({url: href, title: title, thumbnail: thumb});
        });

        // Strategy 2: If no /campaigns/ links found, look for card-like
        // elements with links (the page may use a different URL pattern)
        if (cards.length === 0) {
            var container = document.querySelector('main .flex-1') ||
                            document.querySelector('main') ||
                            document.querySelector('[class*="grid"]') || document.body;
            var allLinks = container.querySelectorAll('a[href]');
            allLinks.forEach(function(a) {
                var href = a.href;
                var rect = a.getBoundingClientRect();
                // Must be a visible, clickable card (not tiny nav links)
                if (rect.width < 100 || rect.height < 50) return;
                // Must be on listingleads.com
                if (href.indexOf('listingleads.com') === -1) return;
                // Skip nav/category links
                if (href.match(/\\/(plan|blueprints|coaching|viral|favorites|social|phone-text-scripts|direct-mail)\\/?$/)) return;
                if (href.match(/\\/campaigns\\/(email)\\/?$/)) return;
                // Skip current page
                if (href === window.location.href) return;
                if (seen[href]) return;
                seen[href] = true;

                var title = '';
                var h = a.querySelector('h2, h3, h4, [class*="title"]');
                if (h) {
                    title = h.textContent.trim();
                } else {
                    title = a.textContent.trim().substring(0, 100);
                }

                var img = a.querySelector('img');
                var thumb = img ? img.src : '';

                if (title.length > 2) {
                    cards.push({url: href, title: title, thumbnail: thumb});
                }
            });
        }

        return JSON.stringify(cards);
    })()
    """)

    if not result:
        print("  WARNING: No campaign cards found on library page")
        return []

    try:
        cards = json.loads(result)
    except json.JSONDecodeError:
        print("  WARNING: Could not parse campaign cards")
        return []

    print(f"  Found {len(cards)} campaign cards")
    return cards


def save_library_campaign(campaign_data, category_folder, title,
                          download_files=True, cookies=None):
    """Save a library campaign into the Library/ subfolder of its category."""
    if not campaign_data:
        return []

    saved_files = []
    base_dir = OUTPUT_DIR / category_folder / "Library"
    base_dir.mkdir(parents=True, exist_ok=True)

    safe_title = sanitize_filename(title or "untitled")

    # 1. Save copy blocks (templates, scripts)
    copy_blocks = campaign_data.get("copy_blocks", [])
    if copy_blocks:
        copy_text = ""
        for block in copy_blocks:
            label = block.get("label", "")
            content = block.get("content", "")
            if label:
                copy_text += f"=== {label} ===\n"
            copy_text += f"{content}\n\n"
        if copy_text.strip():
            copy_file = base_dir / f"{safe_title}_templates.txt"
            copy_file.write_text(copy_text.strip(), encoding="utf-8")
            saved_files.append(str(copy_file))

    # 2. Save full page content
    full_text = campaign_data.get("full_text", "")
    if full_text:
        # Clean sidebar text
        for marker in ["Back\n"]:
            idx = full_text.find(marker)
            if idx >= 0:
                full_text = full_text[idx:]
                break
        text_file = base_dir / f"{safe_title}_full.txt"
        text_file.write_text(full_text.strip(), encoding="utf-8")
        saved_files.append(str(text_file))

    # 3. Save sections individually
    sections = campaign_data.get("sections", [])
    for sec in sections:
        heading = sec.get("heading", "")
        text = sec.get("text", "")
        if heading and text and heading != "Step Content":
            sec_name = sanitize_filename(heading)
            sec_file = base_dir / f"{safe_title}_{sec_name}.txt"
            sec_file.write_text(text.strip(), encoding="utf-8")
            saved_files.append(str(sec_file))

    # 4. Save external resource links
    ext_links = campaign_data.get("links", [])
    if ext_links:
        links_text = "External Resources & Tools\n" + "=" * 30 + "\n\n"
        for link in ext_links:
            href = link.get("href", "")
            text = link.get("text", "")
            if href and "listingleads.com" not in href:
                links_text += f"- {text}\n  {href}\n\n"
        if links_text.count("\n") > 4:
            links_file = base_dir / f"{safe_title}_resources.txt"
            links_file.write_text(links_text.strip(), encoding="utf-8")
            saved_files.append(str(links_file))

    if not download_files:
        return saved_files

    # 5. Download images
    seen_urls = set()
    for img in campaign_data.get("images", []):
        src = img.get("src", "")
        if not src or src in seen_urls:
            continue
        seen_urls.add(src)
        ext = guess_extension(src) or '.png'
        alt = sanitize_filename(img.get("alt", "")) or f"image_{len(seen_urls)}"
        dest = base_dir / f"{safe_title}_{alt}{ext}"
        if not dest.exists():
            if download_file(src, dest, cookies):
                saved_files.append(str(dest))
            time.sleep(0.5)

    # 6. Download explicit downloads
    for dl in campaign_data.get("download_buttons", []):
        href = dl.get("href", "")
        if not href or href in seen_urls:
            continue
        seen_urls.add(href)
        ext = guess_extension(href) or '.pdf'
        dl_name = sanitize_filename(dl.get("text", "")) or "download"
        dest = base_dir / f"{safe_title}_{dl_name}{ext}"
        if not dest.exists():
            if download_file(href, dest, cookies):
                saved_files.append(str(dest))
            time.sleep(0.5)

    # 7. Save video URLs
    videos = campaign_data.get("videos", [])
    video_links = [v.get("src", "") for v in videos if v.get("src")]
    for link in ext_links:
        href = link.get("href", "")
        if any(v in href.lower() for v in ['youtube.com', 'youtu.be', 'vimeo.com', 'wistia', 'loom']):
            video_links.append(href)
    if video_links:
        vid_file = base_dir / f"{safe_title}_videos.txt"
        vid_file.write_text("\n".join(sorted(set(video_links))), encoding="utf-8")
        saved_files.append(str(vid_file))

    return saved_files


# --- Designs Page Scraper -----------------------------------------------------

def scrape_designs_page(url):
    """
    Scrape the designs editor page at app.listingleads.com/designs.
    Collects all design cards with their Personalize URLs, then follows
    each one to extract the full Claude prompt.
    """
    print(f"\n  Navigating to designs page: {url}")
    navigate_to(url)
    time.sleep(5)

    # Check for login redirect
    current = get_current_url()
    if '/login' in current or '/sign-in' in current:
        print("  ERROR: Redirected to login page. Log in first!")
        return None

    wait_for_element('h3', timeout=15)
    time.sleep(2)
    scroll_to_bottom()

    # Extract all design cards with their customize URLs
    result = chrome_js("""
    (function() {
        var data = {designs: []};
        var cards = document.querySelectorAll('.bg-card.rounded-2xl');
        cards.forEach(function(card) {
            var h3 = card.querySelector('h3');
            var title = h3 ? h3.textContent.trim() : '';

            var desc = card.querySelector('p.text-muted-foreground');
            var description = desc ? desc.textContent.trim() : '';

            var link = card.querySelector('a[href*="/templates/"]');
            var customizeUrl = link ? link.href : '';

            var img = card.querySelector('img');
            var imgSrc = '';
            if (img) {
                imgSrc = img.src;
                if (imgSrc.indexOf('/_next/image') > -1) {
                    try {
                        var urlObj = new URL(imgSrc);
                        var origUrl = urlObj.searchParams.get('url');
                        if (origUrl) imgSrc = origUrl;
                    } catch(e) {}
                }
            }

            if (title && customizeUrl) {
                data.designs.push({
                    title: title,
                    description: description,
                    customize_url: customizeUrl,
                    image: imgSrc
                });
            }
        });
        return JSON.stringify(data);
    })()
    """)

    if not result:
        print("  WARNING: No design cards found")
        return None

    try:
        data = json.loads(result)
    except json.JSONDecodeError:
        print("  WARNING: Could not parse design cards")
        return None

    designs = data.get("designs", [])
    print(f"  Found {len(designs)} designs with Personalize links")

    # Phase 2: Follow each customize URL to extract the Claude prompt
    for i, design in enumerate(designs, 1):
        customize_url = design.get("customize_url", "")
        title = design.get("title", "")
        if not customize_url:
            continue

        print(f"\n    [{i}/{len(designs)}] {title}")
        print(f"      Navigating to customize page...")
        navigate_to(customize_url)
        time.sleep(4)

        # Wait for the prompt to load (it's in a <pre> tag)
        wait_for_element('pre', timeout=15)
        time.sleep(1)

        # Extract the full Claude prompt from the <pre> element
        # The prompt can be very long (25k+ chars), so we get it in chunks
        prompt_text = chrome_js("""
        (function() {
            var pre = document.querySelector('pre');
            if (!pre) return '';
            return pre.textContent.substring(0, 30000);
        })()
        """)

        if prompt_text and len(prompt_text) >= 29000:
            # Get more if truncated
            more = chrome_js("""
            (function() {
                var pre = document.querySelector('pre');
                if (!pre) return '';
                return pre.textContent.substring(30000, 60000);
            })()
            """)
            if more:
                prompt_text += more

        if prompt_text:
            design["prompt"] = prompt_text
            char_count = len(prompt_text)
            print(f"      Extracted prompt ({char_count:,} chars)")
        else:
            print(f"      WARNING: No prompt found on customize page")
            design["prompt"] = ""

        # Also check for the HTML template code embedded in the prompt
        # (it's part of the prompt text, so already captured)

        time.sleep(1)

    return data


def save_designs(data, download_files=True, cookies=None):
    """Save designs page content with Claude prompts."""
    if not data:
        return []

    saved_files = []
    base_dir = OUTPUT_DIR / "Expired Editor Designs"
    base_dir.mkdir(parents=True, exist_ok=True)

    designs = data.get("designs", [])

    # Save raw catalog
    catalog_file = base_dir / "designs_catalog.json"
    catalog_file.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    saved_files.append(str(catalog_file))
    print(f"  Saved: {catalog_file.name}")

    # Save each design's prompt as its own file
    for design in designs:
        title = design.get("title", "Untitled")
        safe_name = sanitize_filename(title)
        description = design.get("description", "")
        prompt = design.get("prompt", "")

        if prompt:
            # Save the full Claude prompt
            prompt_file = base_dir / f"{safe_name}_claude_prompt.txt"
            header = f"Design: {title}\n"
            header += f"Description: {description}\n"
            header += f"URL: {design.get('customize_url', '')}\n"
            header += "=" * 60 + "\n\n"
            prompt_file.write_text(header + prompt, encoding="utf-8")
            saved_files.append(str(prompt_file))
            print(f"  Saved: {prompt_file.name} ({len(prompt):,} chars)")

    # Save summary of all designs
    summary = "Expired Editor Designs - Claude Prompts\n" + "=" * 50 + "\n\n"
    for i, d in enumerate(designs, 1):
        summary += f"{i}. {d.get('title', 'Untitled')}\n"
        summary += f"   {d.get('description', '')[:200]}\n"
        has_prompt = "YES" if d.get("prompt") else "NO"
        summary += f"   Prompt captured: {has_prompt}\n"
        if d.get("prompt"):
            summary += f"   Prompt size: {len(d['prompt']):,} chars\n"
        summary += f"   URL: {d.get('customize_url', '')}\n\n"

    summary_file = base_dir / "designs_summary.txt"
    summary_file.write_text(summary.strip(), encoding="utf-8")
    saved_files.append(str(summary_file))
    print(f"  Saved: {summary_file.name}")

    # Download design preview images
    if download_files:
        seen_urls = set()
        for d in designs:
            src = d.get("image", "")
            if not src or src in seen_urls:
                continue
            seen_urls.add(src)
            name = sanitize_filename(d.get("title", "")) or f"design_{len(seen_urls)}"
            ext = guess_extension(src) or '.png'
            dest = base_dir / f"{name}{ext}"
            if not dest.exists():
                if download_file(src, dest, cookies):
                    saved_files.append(str(dest))
                time.sleep(0.5)

    return saved_files


# --- Checkpoint / Resume -----------------------------------------------------

def save_checkpoint(data):
    """Save progress to checkpoint file."""
    with open(CHECKPOINT_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def load_checkpoint():
    """Load progress from checkpoint file."""
    if CHECKPOINT_FILE.exists():
        with open(CHECKPOINT_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"completed_urls": [], "library_progress": {}}


# --- Main Orchestrator --------------------------------------------------------

def run_scraper(args):
    """Main scraper orchestrator."""
    global TAB
    TAB = f"tab {args.tab}"

    download_files = not args.no_download
    target_type = args.type

    # Load checkpoint if resuming
    checkpoint = load_checkpoint() if args.resume else {"completed_urls": [], "library_progress": {}}
    completed = set(checkpoint.get("completed_urls", []))

    # Get cookies for authenticated downloads
    print("Extracting Chrome cookies for downloads...")
    cookies = get_chrome_cookies()

    total_files = 0

    # Determine which targets to scrape
    if args.url:
        # Single URL mode -- figure out which type it is
        url = args.url
        all_targets = []
        for bp in TARGETS["blueprints"]:
            if bp["url"] == url:
                all_targets.append(("blueprint", bp))
        for lib in TARGETS["campaigns"]:
            if lib["url"] == url:
                all_targets.append(("campaign", lib))
        for des in TARGETS["designs"]:
            if des["url"] == url:
                all_targets.append(("design", des))
        if not all_targets:
            # Unknown URL -- try to guess by pattern
            if "/blueprints/" in url:
                all_targets.append(("blueprint", {"url": url, "name": url.split("/")[-1].replace("-", " ").title()}))
            elif "/campaigns/" in url:
                all_targets.append(("campaign", {"url": url, "folder": "Other"}))
            else:
                all_targets.append(("design", {"url": url, "name": "Custom Page"}))
    else:
        all_targets = []
        if target_type in ("all", "blueprints"):
            for bp in TARGETS["blueprints"]:
                all_targets.append(("blueprint", bp))
        if target_type in ("all", "campaigns"):
            for lib in TARGETS["campaigns"]:
                all_targets.append(("campaign", lib))
        if target_type in ("all", "designs"):
            for des in TARGETS["designs"]:
                all_targets.append(("design", des))

    print(f"\nTargeting {len(all_targets)} pages to scrape")
    print("=" * 60)

    for page_type, target in all_targets:
        url = target["url"]

        if page_type == "blueprint":
            if url in completed:
                print(f"\n  SKIP (already done): {target.get('name', url)}")
                continue

            print(f"\n{'=' * 60}")
            print(f"BLUEPRINT: {target.get('name', '')}")
            print(f"{'=' * 60}")

            data = scrape_blueprint_page(url)
            if data:
                files = save_blueprint(data, target, download_files=download_files, cookies=cookies)
                total_files += len(files)
                print(f"  Saved {len(files)} files")

                # Follow internal links from blueprint
                internal_links = data.get("internal_links", [])
                if internal_links:
                    follow_links = []
                    seen_follow = set()
                    for link in internal_links:
                        href = link.get("href", "")
                        if not href or href in seen_follow or href in completed or href == url:
                            continue
                        seen_follow.add(href)
                        follow_links.append(link)

                    if follow_links:
                        bp_name = sanitize_filename(target.get("name", data.get("title", "untitled")))
                        bp_dir = OUTPUT_DIR / "Blueprints" / bp_name / "Linked_Pages"
                        bp_dir.mkdir(parents=True, exist_ok=True)

                        print(f"\n  Following {len(follow_links)} internal links from blueprint...")
                        for j, link in enumerate(follow_links, 1):
                            link_url = link.get("href", "")
                            link_text = link.get("text", "")[:60]
                            print(f"    [{j}/{len(follow_links)}] {link_text}")

                            # Scrape the linked page using campaign detail scraper
                            linked_data = scrape_campaign_detail(link_url)
                            if linked_data:
                                safe_name = sanitize_filename(link_text or link_url.split("/")[-1])

                                # Save copy blocks
                                cblocks = linked_data.get("copy_blocks", [])
                                if cblocks:
                                    ct = ""
                                    for block in cblocks:
                                        lbl = block.get("label", "")
                                        con = block.get("content", "")
                                        if lbl:
                                            ct += f"=== {lbl} ===\n"
                                        ct += f"{con}\n\n"
                                    if ct.strip():
                                        f = bp_dir / f"{safe_name}_templates.txt"
                                        f.write_text(ct.strip(), encoding="utf-8")
                                        total_files += 1

                                # Save full text
                                ft = linked_data.get("full_text", "")
                                if ft:
                                    for marker in ["Back\n"]:
                                        idx = ft.find(marker)
                                        if idx >= 0:
                                            ft = ft[idx:]
                                            break
                                    f = bp_dir / f"{safe_name}_full.txt"
                                    f.write_text(ft.strip(), encoding="utf-8")
                                    total_files += 1

                                # Save sections
                                for sec in linked_data.get("sections", []):
                                    heading = sec.get("heading", "")
                                    stxt = sec.get("text", "")
                                    if heading and stxt and heading != "Step Content":
                                        sec_name = sanitize_filename(heading)
                                        f = bp_dir / f"{safe_name}_{sec_name}.txt"
                                        f.write_text(stxt.strip(), encoding="utf-8")
                                        total_files += 1

                                # Download images
                                if download_files:
                                    seen_img = set()
                                    for img in linked_data.get("images", []):
                                        src = img.get("src", "")
                                        if not src or src in seen_img:
                                            continue
                                        seen_img.add(src)
                                        ext = guess_extension(src) or '.png'
                                        alt = sanitize_filename(img.get("alt", "")) or f"image_{len(seen_img)}"
                                        dest = bp_dir / f"{safe_name}_{alt}{ext}"
                                        if not dest.exists():
                                            if download_file(src, dest, cookies):
                                                total_files += 1
                                            time.sleep(0.5)

                                print(f"      Scraped linked page")
                            else:
                                print(f"      No data extracted")

                            completed.add(link_url)
                            time.sleep(2)
            else:
                print("  FAILED: No data extracted")

            completed.add(url)
            checkpoint["completed_urls"] = list(completed)
            save_checkpoint(checkpoint)
            time.sleep(2)

        elif page_type == "campaign":
            folder = target.get("folder", "Other")
            print(f"\n{'=' * 60}")
            print(f"CAMPAIGN LIBRARY: {folder}")
            print(f"{'=' * 60}")

            # Phase 1: Get all campaign cards
            lib_progress = checkpoint.get("library_progress", {}).get(url, {})
            cards = lib_progress.get("cards", None)
            cards_done = set(lib_progress.get("cards_done", []))

            if cards is None:
                cards = scrape_campaign_library_page(url)
                # Save card list to checkpoint
                if "library_progress" not in checkpoint:
                    checkpoint["library_progress"] = {}
                checkpoint["library_progress"][url] = {
                    "cards": cards,
                    "cards_done": list(cards_done),
                }
                save_checkpoint(checkpoint)

            if not cards:
                print("  No campaign cards found")
                completed.add(url)
                checkpoint["completed_urls"] = list(completed)
                save_checkpoint(checkpoint)
                continue

            # Phase 2: Scrape each campaign detail
            print(f"\n  Scraping {len(cards)} campaigns from {folder}...")
            for i, card in enumerate(cards, 1):
                card_url = card.get("url", "")
                card_title = card.get("title", "")

                if card_url in cards_done:
                    print(f"  [{i}/{len(cards)}] SKIP: {card_title[:50]}")
                    continue

                print(f"\n  [{i}/{len(cards)}] {card_title[:60]}")
                detail = scrape_campaign_detail(card_url)

                if detail:
                    files = save_library_campaign(
                        detail, folder, card_title,
                        download_files=download_files, cookies=cookies
                    )
                    total_files += len(files)
                    print(f"    Saved {len(files)} files")
                else:
                    print(f"    FAILED: No data extracted")

                cards_done.add(card_url)
                checkpoint["library_progress"][url]["cards_done"] = list(cards_done)
                save_checkpoint(checkpoint)
                time.sleep(2)

            # Mark library as complete
            completed.add(url)
            checkpoint["completed_urls"] = list(completed)
            save_checkpoint(checkpoint)

        elif page_type == "design":
            if url in completed:
                print(f"\n  SKIP (already done): {target.get('name', url)}")
                continue

            print(f"\n{'=' * 60}")
            print(f"DESIGNS: {target.get('name', '')}")
            print(f"{'=' * 60}")

            data = scrape_designs_page(url)
            if data:
                files = save_designs(data, download_files=download_files, cookies=cookies)
                total_files += len(files)
                print(f"  Saved {len(files)} files")
            else:
                print("  FAILED: No data extracted")
                print("  TIP: Run with --discover --url to explore the DOM first")

            completed.add(url)
            checkpoint["completed_urls"] = list(completed)
            save_checkpoint(checkpoint)
            time.sleep(2)

    # Summary
    print(f"\n{'=' * 60}")
    print(f"DONE! Saved {total_files} total files")
    print(f"Output: {OUTPUT_DIR}")
    print(f"{'=' * 60}")


# --- CLI ----------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Scrape specific pages from listingleads.com"
    )
    parser.add_argument("--tab", type=int, default=1,
                        help="Chrome tab number (default: 1)")
    parser.add_argument("--discover", action="store_true",
                        help="DOM discovery mode on current page (or --url)")
    parser.add_argument("--url", type=str, default=None,
                        help="Scrape a specific URL")
    parser.add_argument("--type", choices=["all", "blueprints", "campaigns", "designs"],
                        default="all", help="Type of pages to scrape (default: all)")
    parser.add_argument("--resume", action="store_true",
                        help="Resume from checkpoint")
    parser.add_argument("--no-download", action="store_true",
                        help="Skip file downloads (text content only)")
    parser.add_argument("--list", action="store_true",
                        help="List all target URLs and exit")

    args = parser.parse_args()

    global TAB
    TAB = f"tab {args.tab}"

    if args.list:
        print("\nTarget URLs:")
        print("=" * 60)
        for type_name, targets in TARGETS.items():
            print(f"\n  {type_name.upper()}:")
            for t in targets:
                name = t.get("name", t.get("folder", ""))
                print(f"    {name}")
                print(f"      {t['url']}")
        return

    if args.discover:
        discover_page(url=args.url)
        return

    print("\n" + "=" * 60)
    print("LISTING LEADS PAGE SCRAPER")
    print("=" * 60)
    print(f"Tab: {args.tab}")
    print(f"Type: {args.type}")
    print(f"Download files: {not args.no_download}")
    print(f"Resume: {args.resume}")
    if args.url:
        print(f"URL: {args.url}")
    print(f"Output: {OUTPUT_DIR}")
    print()

    run_scraper(args)


if __name__ == "__main__":
    main()
