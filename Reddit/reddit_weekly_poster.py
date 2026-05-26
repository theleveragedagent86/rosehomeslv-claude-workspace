"""
Reddit Weekly Scheduler for r/VegasRealtor
Schedules all 21 weekly posts using new Reddit's post scheduling feature.
Each post is scheduled at its intended date and time (10 AM, 1 PM, or 4 PM).

Usage:
    python3 reddit_weekly_poster.py                    # interactive mode
    python3 reddit_weekly_poster.py --non-interactive  # auto mode
    python3 reddit_weekly_poster.py --delay 90         # seconds between scheduling actions
    python3 reddit_weekly_poster.py --start-at 5       # skip to post #5 (resume after failure)

Requires:
    pip install playwright
    python3 -m playwright install chromium
"""

import asyncio
import re
import sys
import os
import subprocess
from datetime import datetime
from typing import Optional, List, Dict
from playwright.async_api import async_playwright, Page, BrowserContext


def get_keychain_value(service: str) -> Optional[str]:
    """Retrieve a password from macOS Keychain."""
    try:
        result = subprocess.run(
            ["security", "find-generic-password", "-s", service, "-w"],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except Exception:
        pass
    return None


# Config
REDDIT_USERNAME = "Silver_Artichoke_812"
POST_DELAY = 15
HEADLESS = False
NON_INTERACTIVE = False
START_AT = 1
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Schedule mapping: post number -> (date, time_label, hour, minute)
SCHEDULE = {
    1:  ("2026-04-06", "10:00 AM", 10, 0),
    2:  ("2026-04-06", "1:00 PM",  13, 0),
    3:  ("2026-04-06", "4:00 PM",  16, 0),
    4:  ("2026-04-07", "10:00 AM", 10, 0),
    5:  ("2026-04-07", "1:00 PM",  13, 0),
    6:  ("2026-04-07", "4:00 PM",  16, 0),
    7:  ("2026-04-08", "10:00 AM", 10, 0),
    8:  ("2026-04-08", "1:00 PM",  13, 0),
    9:  ("2026-04-08", "4:00 PM",  16, 0),
    10: ("2026-04-09", "10:00 AM", 10, 0),
    11: ("2026-04-09", "1:00 PM",  13, 0),
    12: ("2026-04-09", "4:00 PM",  16, 0),
    13: ("2026-04-10", "10:00 AM", 10, 0),
    14: ("2026-04-10", "1:00 PM",  13, 0),
    15: ("2026-04-10", "4:00 PM",  16, 0),
    16: ("2026-04-11", "10:00 AM", 10, 0),
    17: ("2026-04-11", "1:00 PM",  13, 0),
    18: ("2026-04-11", "4:00 PM",  16, 0),
    19: ("2026-04-12", "10:00 AM", 10, 0),
    20: ("2026-04-12", "1:00 PM",  13, 0),
    21: ("2026-04-12", "4:00 PM",  16, 0),
}


def parse_weekly_posts(filepath: str) -> List[Dict]:
    """Parse the weekly posts markdown file and extract all 21 posts."""
    with open(filepath, "r") as f:
        content = f.read()

    posts = []
    post_blocks = re.split(r"### Post (\d+) of 21", content)

    for i in range(1, len(post_blocks) - 1, 2):
        post_num = int(post_blocks[i])
        block = post_blocks[i + 1]

        title_match = re.search(r"\*\*Title:\*\*\s*(.+)", block)
        flair_match = re.search(r"\*\*Flair:\*\*\s*(.+)", block)
        body_match = re.search(
            r"\*\*Body:\*\*\s*\n\n(.*?)(?=\n---\n|\n### Post|\Z)",
            block, re.DOTALL
        )

        if title_match and body_match:
            schedule_info = SCHEDULE.get(post_num, ("2026-04-06", "10:00 AM", 10, 0))
            posts.append({
                "number": post_num,
                "title": title_match.group(1).strip(),
                "flair": flair_match.group(1).strip() if flair_match else "",
                "body": body_match.group(1).strip(),
                "date": schedule_info[0],
                "time_label": schedule_info[1],
                "hour": schedule_info[2],
                "minute": schedule_info[3],
            })

    return posts


async def login_to_reddit(page: Page, context: BrowserContext):
    """Log in to Reddit via Google OAuth."""
    print("\n[1] LOGGING IN TO REDDIT")
    print("=" * 60)

    google_email = get_keychain_value("reddit-google-email")
    google_password = get_keychain_value("reddit-google-password")

    if not google_email or not google_password:
        print("  [!] Could not read credentials from Keychain.")
        await page.goto("https://www.reddit.com/login")
        await asyncio.sleep(3)
        if NON_INTERACTIVE:
            print("  Non-interactive: waiting 45s for manual login...")
            await asyncio.sleep(45)
        else:
            print("  Log in manually in the browser, then press ENTER.")
            await asyncio.get_event_loop().run_in_executor(None, input)
        await asyncio.sleep(2)
        print(f"  [OK] Proceeding as {REDDIT_USERNAME}\n")
        return

    print(f"  Email: {google_email}")
    print("  Password: loaded from Keychain")

    await page.goto("https://www.reddit.com/login")
    await asyncio.sleep(4)

    google_btn = None
    for sel in [
        'button:has-text("Continue with Google")',
        'a:has-text("Continue with Google")',
        '[data-provider="google"]',
        'button:has-text("Google")',
        'a:has-text("Google")',
    ]:
        try:
            btn = await page.wait_for_selector(sel, timeout=3000)
            if btn:
                google_btn = btn
                break
        except Exception:
            continue

    if not google_btn:
        if NON_INTERACTIVE:
            print("  [!] Could not find Google button. Waiting 45s...")
            await asyncio.sleep(45)
        else:
            print("  [!] Could not find Google button. Log in manually, then press ENTER.")
            await asyncio.get_event_loop().run_in_executor(None, input)
        await asyncio.sleep(2)
        print(f"  [OK] Proceeding as {REDDIT_USERNAME}\n")
        return

    print("  Clicking 'Continue with Google'...")

    try:
        async with context.expect_page(timeout=10000) as popup_info:
            await google_btn.click()

        google_page = await popup_info.value
        await google_page.wait_for_load_state("domcontentloaded")
        await asyncio.sleep(3)

        try:
            print("  Entering email...")
            email_input = await google_page.wait_for_selector('input[type="email"]', timeout=10000)
            await email_input.fill(google_email)
            await asyncio.sleep(1)
            next_btn = await google_page.wait_for_selector('button:has-text("Next"), #identifierNext', timeout=5000)
            await next_btn.click()
            await asyncio.sleep(4)

            print("  Entering password...")
            password_input = await google_page.wait_for_selector('input[type="password"]', timeout=10000)
            await password_input.fill(google_password)
            await asyncio.sleep(1)
            next_btn2 = await google_page.wait_for_selector('button:has-text("Next"), #passwordNext', timeout=5000)
            await next_btn2.click()
            await asyncio.sleep(5)

            if not google_page.is_closed():
                page_text = await google_page.evaluate("() => document.body.innerText")
                if "2-step" in page_text.lower() or "verify" in page_text.lower():
                    print("  [!] Google 2FA required.")
                    if NON_INTERACTIVE:
                        print("  Waiting 45s for 2FA...")
                        await asyncio.sleep(45)
                    else:
                        print("  Complete 2FA, then press ENTER.")
                        await asyncio.get_event_loop().run_in_executor(None, input)

            await asyncio.sleep(5)
            print(f"  [OK] Logged in as {REDDIT_USERNAME}\n")

        except Exception as e:
            print(f"  [!] Auto-login error: {e}")
            if NON_INTERACTIVE:
                print("  Waiting 45s for manual login...")
                await asyncio.sleep(45)
            else:
                print("  Complete login manually, then press ENTER.")
                await asyncio.get_event_loop().run_in_executor(None, input)
            await asyncio.sleep(2)
            print(f"  [OK] Proceeding as {REDDIT_USERNAME}\n")

    except Exception as e:
        print(f"  [!] Google popup did not open: {e}")
        print("  Falling back to manual login...")
        if NON_INTERACTIVE:
            print("  Waiting 45s for manual login...")
            await asyncio.sleep(45)
        else:
            print("  Complete login manually in the browser, then press ENTER.")
            await asyncio.get_event_loop().run_in_executor(None, input)
        await asyncio.sleep(2)
        print(f"  [OK] Proceeding as {REDDIT_USERNAME}\n")


def markdown_to_html(text: str) -> str:
    """Convert markdown bold (**text**) to HTML <strong> tags for rich text paste."""
    # Convert **bold** to <strong>bold</strong>
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # Convert line breaks to <br> for proper paragraph handling
    # Double newline = paragraph break, single newline = line break
    paragraphs = html.split('\n\n')
    html_parts = []
    for p in paragraphs:
        p = p.strip()
        if p:
            # Replace single newlines within a paragraph with <br>
            p = p.replace('\n', '<br>')
            html_parts.append(f'<p>{p}</p>')
    return ''.join(html_parts)


async def schedule_post(page: Page, post_data: Dict) -> bool:
    """Schedule a single post on new Reddit using rich text editor."""
    post_num = post_data["number"]
    sched_date = post_data["date"]
    sched_hour = post_data["hour"]
    time_label = post_data["time_label"]

    print(f"\n  [{post_num}/21] {post_data['title'][:55]}...")
    print(f"    Schedule: {sched_date} at {time_label} | Flair: {post_data['flair']}")

    # Navigate to new Reddit submit
    await page.goto("https://www.reddit.com/r/VegasRealtor/submit?type=TEXT")
    await asyncio.sleep(8)  # Give React app time to fully load
    # Scroll down slightly to make sure all elements are rendered
    await page.evaluate("window.scrollBy(0, 100)")
    await asyncio.sleep(1)

    # ── STEP 1: Fill in the title ──
    # New Reddit's title field could be a textarea, input, or contenteditable div.
    # The label shows "Title*". We try multiple approaches.
    title_filled = False

    # Try standard selectors first
    for sel in [
        'textarea[placeholder*="Title"]',
        'textarea[placeholder*="title"]',
        'input[placeholder*="Title"]',
        'textarea[name="title"]',
        'input[name="title"]',
        'textarea[aria-label*="itle"]',
        'input[aria-label*="itle"]',
        '[data-testid="post-title"] textarea',
        '[data-testid="post-title"] input',
    ]:
        try:
            el = await page.wait_for_selector(sel, timeout=2000)
            if el:
                await el.click()
                await asyncio.sleep(0.3)
                await el.fill(post_data["title"])
                await asyncio.sleep(0.3)
                try:
                    entered = await el.input_value()
                    if len(entered) > 10:
                        title_filled = True
                        print(f"    [OK] Title filled")
                        break
                except Exception:
                    # contenteditable might not have input_value
                    title_filled = True
                    print(f"    [OK] Title filled")
                    break
        except Exception:
            continue

    if not title_filled:
        # JS approach: find any input/textarea near a "Title" label
        title_filled = await page.evaluate(
            """(titleText) => {
                // Method 1: Find textarea or input elements
                const fields = document.querySelectorAll('textarea, input[type="text"], input:not([type])');
                for (const field of fields) {
                    const ph = field.getAttribute('placeholder') || '';
                    const label = field.getAttribute('aria-label') || '';
                    const name = field.getAttribute('name') || '';
                    if (ph.includes('Title') || ph.includes('title') ||
                        label.includes('Title') || label.includes('title') ||
                        name === 'title') {
                        field.focus();
                        field.value = titleText;
                        field.dispatchEvent(new Event('input', { bubbles: true }));
                        field.dispatchEvent(new Event('change', { bubbles: true }));
                        return true;
                    }
                }

                // Method 2: Find the first textarea on the page (likely the title)
                const firstTextarea = document.querySelector('textarea');
                if (firstTextarea) {
                    firstTextarea.focus();
                    firstTextarea.value = titleText;
                    firstTextarea.dispatchEvent(new Event('input', { bubbles: true }));
                    firstTextarea.dispatchEvent(new Event('change', { bubbles: true }));
                    return true;
                }

                // Method 3: Find the first visible input on the page
                const inputs = document.querySelectorAll('input');
                for (const inp of inputs) {
                    const rect = inp.getBoundingClientRect();
                    if (rect.width > 100 && rect.height > 10) {
                        inp.focus();
                        inp.value = titleText;
                        inp.dispatchEvent(new Event('input', { bubbles: true }));
                        inp.dispatchEvent(new Event('change', { bubbles: true }));
                        return true;
                    }
                }

                return false;
            }""",
            post_data["title"]
        )
        if title_filled:
            await asyncio.sleep(0.5)
            print(f"    [OK] Title filled via JS")

    if not title_filled:
        # Last resort: click where the title field should be and type
        try:
            # The title field is near the top of the form, roughly at y=350 based on screenshots
            await page.mouse.click(600, 350)
            await asyncio.sleep(0.5)
            await page.keyboard.type(post_data["title"], delay=10)
            await asyncio.sleep(0.5)
            title_filled = True
            print(f"    [OK] Title typed via mouse click + keyboard")
        except Exception:
            pass

    if not title_filled:
        print("    [!] Could not fill title")
        return False

    await asyncio.sleep(1)

    # ── STEP 2: Switch to Markdown mode ──
    # Click the three-dot overflow menu in the formatting toolbar,
    # then click "Switch to Markdown". This makes the body a regular textarea
    # which is much easier to fill than a contenteditable div.
    # In markdown mode, **text** renders as bold automatically.
    markdown_mode = False

    # Find and click the three-dot (overflow/ellipsis) menu button
    overflow_clicked = await page.evaluate("""
        () => {
            // Look for a button with "..." or ellipsis icon in the formatting toolbar area
            const buttons = document.querySelectorAll('button');
            for (const btn of buttons) {
                const text = btn.textContent.trim();
                const label = (btn.getAttribute('aria-label') || '').toLowerCase();
                const title = (btn.getAttribute('title') || '').toLowerCase();
                // Match overflow/more/ellipsis buttons
                if (text === '...' || text === '\u2026' || text === '\u22EF' ||
                    label.includes('more') || label.includes('overflow') ||
                    label.includes('option') || label.includes('ellipsis') ||
                    title.includes('more') || title.includes('option')) {
                    // Make sure it's in the toolbar area (not in header/nav)
                    const rect = btn.getBoundingClientRect();
                    if (rect.top > 200 && rect.top < 600 && rect.width < 60) {
                        btn.click();
                        return 'found_by_label';
                    }
                }
            }

            // Fallback: look for small buttons with SVG (icon-only) near the formatting toolbar
            // The toolbar is typically between the title and body, around y=400-500
            for (const btn of buttons) {
                const svg = btn.querySelector('svg');
                if (!svg) continue;
                const rect = btn.getBoundingClientRect();
                const text = btn.textContent.trim();
                // Three-dot button is usually small, icon-only, at the right side of toolbar
                if (rect.top > 300 && rect.top < 550 && rect.width < 50 &&
                    rect.left > 500 && text.length < 3) {
                    btn.click();
                    return 'found_by_svg_position';
                }
            }

            return null;
        }
    """)

    if overflow_clicked:
        print(f"    [OK] Overflow menu opened ({overflow_clicked})")
        await asyncio.sleep(1.5)

        # Now click "Switch to Markdown" in the dropdown
        md_clicked = await page.evaluate("""
            () => {
                // Search for menu items containing "Markdown"
                const allEls = document.querySelectorAll('*');
                for (const el of allEls) {
                    const text = el.textContent.trim();
                    if ((text === 'Switch to Markdown' || text === 'Markdown mode' ||
                         text === 'Switch to markdown' || text.includes('Markdown')) &&
                        el.children.length <= 3) {
                        el.click();
                        return true;
                    }
                }
                // Also try role="menuitem" elements
                const menuItems = document.querySelectorAll('[role="menuitem"], [role="option"]');
                for (const item of menuItems) {
                    if (item.textContent.toLowerCase().includes('markdown')) {
                        item.click();
                        return true;
                    }
                }
                return false;
            }
        """)

        if md_clicked:
            await asyncio.sleep(2)
            markdown_mode = True
            print(f"    [OK] Switched to Markdown mode")
        else:
            print(f"    [!] Could not find 'Switch to Markdown' in menu")
    else:
        print(f"    [!] Could not find overflow (three-dot) menu button")

    # ── STEP 3: Fill in the body ──
    body_filled = False

    if markdown_mode:
        # In markdown mode, body is a textarea. Much simpler!
        # The body text already has **bold** markers which markdown will render.
        for sel in [
            'textarea[placeholder*="ody"]',
            'textarea[placeholder*="optional"]',
            'textarea:not([placeholder*="itle"])',
            'div[data-testid="post-body"] textarea',
        ]:
            try:
                body_el = await page.query_selector(sel)
                if body_el:
                    # Make sure it's not the title textarea
                    ph = await body_el.get_attribute("placeholder") or ""
                    if "itle" in ph.lower() and "ody" not in ph.lower():
                        continue
                    await body_el.click()
                    await asyncio.sleep(0.3)
                    await body_el.fill(post_data["body"])
                    await asyncio.sleep(0.5)
                    body_filled = True
                    print(f"    [OK] Body filled in markdown textarea")
                    break
            except Exception:
                continue

        if not body_filled:
            # Fallback: find the second textarea on the page (first is title)
            try:
                textareas = await page.query_selector_all("textarea")
                if len(textareas) >= 2:
                    await textareas[1].click()
                    await asyncio.sleep(0.3)
                    await textareas[1].fill(post_data["body"])
                    await asyncio.sleep(0.5)
                    body_filled = True
                    print(f"    [OK] Body filled in 2nd textarea")
            except Exception as e:
                print(f"    [!] 2nd textarea failed: {e}")

    if not body_filled:
        # Fallback for rich text mode: Tab from title into body and type
        print(f"    [!] Markdown textarea not found. Trying Tab + type...")
        # Click the title first to make sure we have a known focus point
        try:
            title_el = await page.query_selector('textarea[placeholder*="itle"], textarea')
            if title_el:
                await title_el.click()
                await asyncio.sleep(0.3)
        except Exception:
            pass
        await page.keyboard.press("Tab")
        await asyncio.sleep(1)
        # Type the body text (will show ** literally if not in markdown mode)
        await page.keyboard.type(post_data["body"], delay=5)
        await asyncio.sleep(1)
        body_filled = True
        print(f"    [OK] Body typed via Tab + keyboard")

    if not body_filled:
        print(f"    [!] Could not fill body text")
        return False

    await asyncio.sleep(1)

    # ── STEP 4: Set flair ──
    # Click "Add flair and tags" link, then select the matching flair
    flair = post_data.get("flair", "")
    if flair:
        try:
            # The flair trigger shows "Add flair and tags" text. It may be a button, span, or div.
            flair_opened = await page.evaluate("""
                () => {
                    // Search all elements for the flair trigger text
                    const walker = document.createTreeWalker(
                        document.body, NodeFilter.SHOW_ELEMENT, null, false
                    );
                    while (walker.nextNode()) {
                        const el = walker.currentNode;
                        const text = el.textContent.trim();
                        // Match "Add flair and tags" or just "Add flair"
                        if (text === 'Add flair and tags' || text === 'Add flair') {
                            // Make sure this is a leaf-ish element, not a huge container
                            if (el.children.length <= 3) {
                                el.click();
                                return true;
                            }
                        }
                    }
                    return false;
                }
            """)

            if flair_opened:
                await asyncio.sleep(2)

                # Click the matching flair option in the picker
                flair_selected = await page.evaluate(
                    """(flairName) => {
                        // Try all clickable elements in any dialog/modal/dropdown
                        const els = document.querySelectorAll(
                            '[role="dialog"] *, [role="listbox"] *, [class*="flair"] *, ' +
                            '[class*="modal"] *, [class*="Modal"] *, [class*="overlay"] *'
                        );
                        for (const el of els) {
                            const text = el.textContent.trim();
                            if (text === flairName && (el.tagName === 'SPAN' || el.tagName === 'DIV' ||
                                el.tagName === 'LABEL' || el.tagName === 'BUTTON' ||
                                el.tagName === 'LI' || el.closest('label') || el.closest('button'))) {
                                // Click the element or its parent label/button
                                const clickTarget = el.closest('label') || el.closest('button') || el.closest('li') || el;
                                clickTarget.click();
                                return true;
                            }
                        }
                        return false;
                    }""",
                    flair
                )

                if flair_selected:
                    await asyncio.sleep(1)
                    # Click Apply/Done/Save if present
                    await page.evaluate("""
                        () => {
                            const buttons = document.querySelectorAll('button');
                            for (const btn of buttons) {
                                const text = btn.textContent.trim().toLowerCase();
                                if (text === 'apply' || text === 'done' || text === 'save' ||
                                    text === 'apply flair' || text === 'select') {
                                    btn.click();
                                    return true;
                                }
                            }
                            return false;
                        }
                    """)
                    await asyncio.sleep(1)
                    print(f"    [OK] Flair set: {flair}")
                else:
                    print(f"    [!] Flair '{flair}' not found in picker")
            else:
                print(f"    [!] Could not open flair picker")
        except Exception as e:
            print(f"    [!] Flair error: {e}")

    await asyncio.sleep(1)

    # ── STEP 5: Click the schedule (clock icon) button ──
    # From the screenshot: it is a circular button with a clock icon,
    # positioned between "Save Draft" (left) and "Post" (right) at the bottom.
    schedule_opened = False

    # Try aria-label selectors first
    for sel in [
        'button[aria-label*="chedule"]',
        'button[aria-label*="Schedule"]',
        'button[aria-label*="schedule"]',
        'button[aria-label*="Timer"]',
        'button[aria-label*="timer"]',
    ]:
        try:
            el = await page.query_selector(sel)
            if el:
                await el.click()
                await asyncio.sleep(2)
                schedule_opened = True
                print("    [OK] Schedule button clicked")
                break
        except Exception:
            continue

    if not schedule_opened:
        # JS: Multiple strategies to find the clock/schedule button
        schedule_opened = await page.evaluate("""
            () => {
                const allButtons = [...document.querySelectorAll('button')];

                // Find Save Draft and Post buttons
                let saveDraft = null;
                let postBtn = null;
                for (const btn of allButtons) {
                    const text = btn.textContent.trim();
                    if (text === 'Save Draft' || text === 'Save draft') saveDraft = btn;
                    if (text === 'Post' && !text.includes('Draft')) postBtn = btn;
                }

                // Strategy 1: Find button between Save Draft and Post by position
                if (saveDraft && postBtn) {
                    const sdRect = saveDraft.getBoundingClientRect();
                    const postRect = postBtn.getBoundingClientRect();

                    for (const btn of allButtons) {
                        if (btn === saveDraft || btn === postBtn) continue;
                        const rect = btn.getBoundingClientRect();
                        if (rect.left > sdRect.right - 20 && rect.right < postRect.left + 20) {
                            if (Math.abs(rect.top - sdRect.top) < 40) {
                                btn.click();
                                return 'between_buttons';
                            }
                        }
                    }

                    // Strategy 2: Same parent container, any child that isn't Save Draft or Post
                    const parent = saveDraft.parentElement;
                    if (parent) {
                        const allInParent = parent.querySelectorAll('button');
                        for (const btn of allInParent) {
                            const t = btn.textContent.trim().toLowerCase();
                            if (t !== 'save draft' && t !== 'post' && t !== '') {
                                btn.click();
                                return 'parent_sibling';
                            }
                        }
                        // Try icon-only buttons (no text, just SVG)
                        for (const btn of allInParent) {
                            const t = btn.textContent.trim();
                            if (t === '' && btn.querySelector('svg')) {
                                btn.click();
                                return 'parent_svg_btn';
                            }
                        }
                    }
                }

                // Strategy 3: Any button with SVG that's near the bottom of the form
                // and is not Save Draft / Post / Cancel
                const skipTexts = ['save draft', 'post', 'cancel', 'discard', 'add flair'];
                for (const btn of allButtons) {
                    const text = btn.textContent.trim().toLowerCase();
                    if (skipTexts.some(s => text.includes(s))) continue;
                    if (!btn.querySelector('svg')) continue;
                    const rect = btn.getBoundingClientRect();
                    // Should be in the lower portion of the viewport (bottom action bar)
                    if (rect.top > 500 && rect.width < 80 && rect.height < 60) {
                        btn.click();
                        return 'svg_bottom_btn';
                    }
                }

                // Strategy 4: Look for any element with tooltip/title containing "schedule"
                const allEls = document.querySelectorAll('[title], [aria-label], [data-tooltip]');
                for (const el of allEls) {
                    const tip = (el.title || el.getAttribute('aria-label') || el.getAttribute('data-tooltip') || '').toLowerCase();
                    if (tip.includes('schedule') || tip.includes('timer') || tip.includes('clock')) {
                        el.click();
                        return 'tooltip_match';
                    }
                }

                return false;
            }
        """)
        if schedule_opened:
            await asyncio.sleep(2)
            print(f"    [OK] Schedule clock button found ({schedule_opened})")

    if not schedule_opened:
        print("    [!] Could not find schedule clock button")
        if not NON_INTERACTIVE:
            print("    >> Click the clock icon between Save Draft and Post, then press ENTER")
            await asyncio.get_event_loop().run_in_executor(None, input)
            schedule_opened = True

    if not schedule_opened:
        print("    [!] SKIPPING: Could not access schedule feature")
        return False

    await asyncio.sleep(1)

    # ── STEP 6: Set date and time in the schedule picker ──
    year, month, day = post_data["date"].split("-")
    time_24 = f"{post_data['hour']:02d}:{post_data['minute']:02d}"

    # Try date input
    date_set = False
    for sel in ['input[type="date"]', 'input[name*="date"]', 'input[aria-label*="ate"]']:
        try:
            date_input = await page.query_selector(sel)
            if date_input:
                await date_input.fill(post_data["date"])
                date_set = True
                print(f"    [OK] Date: {post_data['date']}")
                break
        except Exception:
            continue

    if not date_set:
        # JS fallback for date
        await page.evaluate(
            """(dateStr) => {
                const inputs = document.querySelectorAll('input');
                for (const inp of inputs) {
                    const type = inp.type || '';
                    const label = (inp.getAttribute('aria-label') || '').toLowerCase();
                    if (type === 'date' || label.includes('date')) {
                        const nativeSetter = Object.getOwnPropertyDescriptor(
                            HTMLInputElement.prototype, 'value').set;
                        nativeSetter.call(inp, dateStr);
                        inp.dispatchEvent(new Event('input', { bubbles: true }));
                        inp.dispatchEvent(new Event('change', { bubbles: true }));
                    }
                }
            }""",
            post_data["date"]
        )

    await asyncio.sleep(0.5)

    # Try time input
    time_set = False
    for sel in ['input[type="time"]', 'input[name*="time"]', 'input[aria-label*="ime"]']:
        try:
            time_input = await page.query_selector(sel)
            if time_input:
                await time_input.fill(time_24)
                time_set = True
                print(f"    [OK] Time: {time_label}")
                break
        except Exception:
            continue

    if not time_set:
        # JS fallback for time
        await page.evaluate(
            """(timeStr) => {
                const inputs = document.querySelectorAll('input');
                for (const inp of inputs) {
                    const type = inp.type || '';
                    const label = (inp.getAttribute('aria-label') || '').toLowerCase();
                    if (type === 'time' || label.includes('time')) {
                        const nativeSetter = Object.getOwnPropertyDescriptor(
                            HTMLInputElement.prototype, 'value').set;
                        nativeSetter.call(inp, timeStr);
                        inp.dispatchEvent(new Event('input', { bubbles: true }));
                        inp.dispatchEvent(new Event('change', { bubbles: true }));
                    }
                }
            }""",
            time_24
        )

    await asyncio.sleep(1)

    # ── STEP 7: Click the final Schedule button ──
    submitted = False

    # Look for a Schedule button (this should appear after the schedule picker opens)
    for sel in [
        'button:has-text("Schedule")',
        'button:has-text("Schedule post")',
    ]:
        try:
            btns = await page.query_selector_all(sel)
            for btn in btns:
                text = (await btn.inner_text()).strip()
                if "schedule" in text.lower():
                    await btn.click()
                    await asyncio.sleep(5)
                    submitted = True
                    break
            if submitted:
                break
        except Exception:
            continue

    if not submitted:
        submitted = await page.evaluate("""
            () => {
                const buttons = [...document.querySelectorAll('button')];
                for (const btn of buttons) {
                    const text = btn.textContent.trim().toLowerCase();
                    if (text === 'schedule' || text === 'schedule post') {
                        btn.click();
                        return true;
                    }
                }
                return false;
            }
        """)
        if submitted:
            await asyncio.sleep(5)

    if submitted:
        await asyncio.sleep(2)
        current_url = page.url
        if "submit" not in current_url.lower():
            print(f"    [OK] SCHEDULED #{post_num} for {post_data['date']} {time_label}")
            return True
        else:
            error_text = await page.evaluate("""
                () => {
                    const errors = document.querySelectorAll('[class*="error" i], [class*="Error"], [role="alert"]');
                    return [...errors].map(e => e.textContent.trim()).filter(t => t).join('; ');
                }
            """)
            if error_text:
                print(f"    [!] Error: {error_text[:100]}")
                return False
            else:
                print(f"    [?] Submitted but still on page. May have worked.")
                return True
    else:
        print(f"    [!] Could not find final Schedule button")
        if not NON_INTERACTIVE:
            print("    >> Click Schedule manually, then press ENTER")
            await asyncio.get_event_loop().run_in_executor(None, input)
            return True
        return False


async def main():
    global NON_INTERACTIVE, POST_DELAY, START_AT

    args = sys.argv[1:]
    if "--non-interactive" in args:
        NON_INTERACTIVE = True
        args = [a for a in args if a != "--non-interactive"]

    if "--delay" in args:
        idx = args.index("--delay")
        POST_DELAY = int(args[idx + 1])
        args = [a for i, a in enumerate(args) if i != idx and i != idx + 1]

    if "--start-at" in args:
        idx = args.index("--start-at")
        START_AT = int(args[idx + 1])
        args = [a for i, a in enumerate(args) if i != idx and i != idx + 1]

    # Find the weekly posts file
    if args and not args[0].startswith("--"):
        filepath = args[0]
        if not os.path.isabs(filepath):
            filepath = os.path.join(SCRIPT_DIR, filepath)
    else:
        import glob
        week_files = glob.glob(os.path.join(SCRIPT_DIR, "Week_*.md"))
        if not week_files:
            print("[!] No Week_*.md file found.")
            sys.exit(1)
        week_files.sort(key=os.path.getmtime, reverse=True)
        filepath = week_files[0]

    print(f"Reading posts from: {os.path.basename(filepath)}")
    posts = parse_weekly_posts(filepath)
    print(f"Found {len(posts)} posts total.\n")

    if START_AT > 1:
        posts = [p for p in posts if p["number"] >= START_AT]
        print(f"Starting at post #{START_AT} ({len(posts)} posts remaining)\n")

    if not posts:
        print("[!] No posts to schedule.")
        sys.exit(1)

    # Preview
    print("SCHEDULE PREVIEW:")
    print("-" * 75)
    for p in posts:
        print(f"  #{p['number']:2d}  {p['date']} {p['time_label']:8s}  [{p['flair']:18s}]  {p['title'][:40]}")
    print("-" * 75)

    if not NON_INTERACTIVE:
        confirm = input("\nProceed with scheduling? (y/n): ").strip().lower()
        if confirm != "y":
            print("Cancelled.")
            sys.exit(0)

    results = {"success": [], "failed": []}

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=HEADLESS)
        context = await browser.new_context(
            viewport={"width": 1400, "height": 900},
            user_agent=(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            ),
        )
        # Grant clipboard permissions
        await context.grant_permissions(["clipboard-read", "clipboard-write"])
        page = await context.new_page()

        await login_to_reddit(page, context)
        await page.goto("https://www.reddit.com/r/VegasRealtor")
        await asyncio.sleep(3)

        print(f"\n[2] SCHEDULING {len(posts)} POSTS")
        print("=" * 60)
        print(f"  Delay: {POST_DELAY}s | Est. time: ~{(len(posts) * POST_DELAY) // 60} min\n")

        for i, post in enumerate(posts):
            success = await schedule_post(page, post)
            if success:
                results["success"].append(post["number"])
            else:
                results["failed"].append(post["number"])
                try:
                    ss = os.path.join(SCRIPT_DIR, f"debug_post{post['number']}.png")
                    await page.screenshot(path=ss)
                    print(f"    [DEBUG] Screenshot: {ss}")
                except Exception:
                    pass

            if i < len(posts) - 1:
                print(f"    Waiting {POST_DELAY}s...")
                await asyncio.sleep(POST_DELAY)

        await browser.close()

    print("\n\n=== RESULTS ===")
    print(f"Total: {len(posts)}")
    print(f"Scheduled: {len(results['success'])}")
    print(f"Failed: {len(results['failed'])}")
    if results["failed"]:
        print(f"Failed: {results['failed']}")
        print(f"To retry failed posts, run with: --start-at {results['failed'][0]}")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=== END RESULTS ===")


if __name__ == "__main__":
    asyncio.run(main())
