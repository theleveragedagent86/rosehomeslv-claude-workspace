"""
Reddit Daily Auto-Poster (Reusable)
Reads a DailyDrafts markdown file and posts all comments, replies, and
r/VegasRealtor posts automatically via Playwright browser automation.

Usage:
    python3 reddit_daily.py                          # auto-detects today's file
    python3 reddit_daily.py DailyDrafts_Mar10_2026.md  # specific file
    python3 reddit_daily.py --skip-vegasrealtor       # skip r/VegasRealtor post
    python3 reddit_daily.py --delay 120               # 120s between comments
    python3 reddit_daily.py --non-interactive          # no input() pauses (for Cowork/cron)

Requires:
    pip install playwright
    python3 -m playwright install chromium
"""

import asyncio
import re
import sys
import os
import glob
import subprocess
from datetime import datetime
from typing import Optional, List, Dict
from playwright.async_api import async_playwright, Page


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

# ─── CONFIG ───────────────────────────────────────────────────────────────────

REDDIT_USERNAME = "Silver_Artichoke_812"
COMMENT_DELAY = 90  # seconds between comments (override with --delay)
HEADLESS = False
NON_INTERACTIVE = False  # set via --non-interactive flag
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


# ─── MARKDOWN PARSER ──────────────────────────────────────────────────────────


def find_todays_file() -> str:
    """Find the DailyDrafts file for today's date."""
    now = datetime.now()
    # Try formats like DailyDrafts_Mar09_2026.md
    month_abbr = now.strftime("%b")
    day = now.strftime("%d")
    year = now.strftime("%Y")
    filename = f"DailyDrafts_{month_abbr}{day}_{year}.md"
    filepath = os.path.join(SCRIPT_DIR, filename)

    if os.path.exists(filepath):
        return filepath

    # Try finding any DailyDrafts file with today's date in different formats
    patterns = [
        f"DailyDrafts_{month_abbr}{day}_{year}.md",
        f"DailyDrafts_{month_abbr}{int(day)}_{year}.md",  # no leading zero
        f"DailyDrafts_{now.strftime('%m')}_{day}_{year}.md",
    ]
    for pattern in patterns:
        fp = os.path.join(SCRIPT_DIR, pattern)
        if os.path.exists(fp):
            return fp

    # List available files
    available = glob.glob(os.path.join(SCRIPT_DIR, "DailyDrafts_*.md"))
    if available:
        available.sort(key=os.path.getmtime, reverse=True)
        print(f"  No file found for today ({filename}).")
        print(f"  Most recent available:")
        for f in available[:5]:
            print(f"    {os.path.basename(f)}")
        print()

    raise FileNotFoundError(
        f"No DailyDrafts file found for today. "
        f"Expected: {filename}\n"
        f"Run with a specific file: python3 reddit_daily.py DailyDrafts_Mar10_2026.md"
    )


def parse_drafts_file(filepath: str, skip_vegasrealtor: bool = False) -> Dict:
    """
    Parse a DailyDrafts markdown file and extract:
    - vegasrealtor_post: dict with title, flair, body (or None)
    - comments: list of dicts with subreddit, urls, text
    - replies: list of dicts with url, context, text
    """
    with open(filepath, "r") as f:
        content = f.read()

    result = {
        "vegasrealtor_post": None,
        "comments": [],
        "replies": [],
    }

    # ── Parse notification replies ──
    reply_blocks = re.split(r"### Reply \d+", content)
    for i in range(1, len(reply_blocks)):
        block = reply_blocks[i]
        # Extract the reply-to URL
        url_match = re.search(
            r"\*\*Reply to:\*\*\s*(https?://[^\s]+)", block
        )
        # Extract context
        ctx_match = re.search(r"\*\*Context:\*\*\s*(.+)", block)
        # Extract reply text between --- delimiters
        text_match = re.search(r"\n---\n\n(.*?)(?=\n---\n|\Z)", block, re.DOTALL)
        if url_match and text_match:
            url = url_match.group(1).strip()
            # Ensure old.reddit.com
            url = url.replace("www.reddit.com", "old.reddit.com").replace(
                "https://reddit.com", "https://old.reddit.com"
            )
            result["replies"].append({
                "url": url,
                "context": ctx_match.group(1).strip() if ctx_match else "",
                "text": text_match.group(1).strip(),
            })

    # ── Parse r/VegasRealtor post ──
    if not skip_vegasrealtor:
        vr_match = re.search(
            r"## r/VegasRealtor POST.*?\n\n"
            r"\*\*Title:\*\*\s*(.+)\n\n"
            r"\*\*Flair:\*\*\s*(.+)\n\n"
            r"\*\*Body:\*\*\s*\n\n(.*?)(?=\n---\n)",
            content,
            re.DOTALL,
        )
        if vr_match:
            result["vegasrealtor_post"] = {
                "title": vr_match.group(1).strip(),
                "flair": vr_match.group(2).strip(),
                "body": vr_match.group(3).strip(),
            }

    # ── Parse off-sub comments ──
    # Split by comment headers: ### Comment N — r/subreddit
    comment_blocks = re.split(r"### Comment \d+ — r/(\w+)", content)
    # comment_blocks[0] is everything before first comment
    # Then alternating: [subreddit, block, subreddit, block, ...]

    for i in range(1, len(comment_blocks) - 1, 2):
        subreddit = comment_blocks[i]
        block = comment_blocks[i + 1]

        # Extract post URLs
        urls = re.findall(
            r"https?://(?:www\.)?reddit\.com/r/\w+/comments/\w+/\w+/?",
            block,
        )
        # Convert to old.reddit.com
        urls = [
            u.replace("www.reddit.com", "old.reddit.com").replace(
                "https://reddit.com", "https://old.reddit.com"
            )
            for u in urls
        ]

        # Extract search query (fallback when no direct URLs)
        search_query = None
        sq_match = re.search(r"\*\*Search query:\*\*\s*(.+)", block)
        if sq_match:
            search_query = sq_match.group(1).strip().strip('"').strip("'")

        # Extract the comment text (everything after the first --- line)
        text_match = re.search(r"\n---\n\n(.*?)(?=\n---\n|\Z)", block, re.DOTALL)
        if text_match:
            text = text_match.group(1).strip()
        else:
            # Fallback: grab everything after the metadata
            lines = block.strip().split("\n")
            text_lines = []
            past_meta = False
            for line in lines:
                if line.strip() == "---":
                    if past_meta:
                        break
                    past_meta = True
                    continue
                if past_meta:
                    text_lines.append(line)
            text = "\n".join(text_lines).strip()

        if text and urls:
            result["comments"].append(
                {
                    "subreddit": subreddit,
                    "urls": urls,
                    "search_query": None,
                    "text": text,
                }
            )
        elif text:
            # No URLs found — include with search_query fallback
            result["comments"].append(
                {
                    "subreddit": subreddit,
                    "urls": [],
                    "search_query": search_query,
                    "text": text,
                }
            )

    return result


# ─── REDDIT AUTOMATION ────────────────────────────────────────────────────────


async def find_post_via_search(page, subreddit: str, query: str) -> Optional[str]:
    """Search a subreddit on old Reddit and return the URL of the first
    commentable post. Returns None if nothing found."""
    search_url = (
        f"https://old.reddit.com/r/{subreddit}/search"
        f"?q={query.replace(' ', '+')}&restrict_sr=on&sort=new&t=year"
    )
    print(f"    Searching r/{subreddit} for: {query}")
    await page.goto(search_url)
    import asyncio as _asyncio
    await _asyncio.sleep(4)

    post_url = await page.evaluate("""
        () => {
            const links = document.querySelectorAll('.search-result-header a');
            for (const link of links) {
                const href = link.getAttribute('href');
                if (href && href.includes('/comments/')) {
                    return href.startsWith('http') ? href : 'https://old.reddit.com' + href;
                }
            }
            const allLinks = document.querySelectorAll('a[href*="/comments/"]');
            for (const link of allLinks) {
                const href = link.getAttribute('href');
                if (href && !href.includes('/user/')) {
                    return href.startsWith('http') ? href : 'https://old.reddit.com' + href;
                }
            }
            return null;
        }
    """)

    if post_url:
        post_url = post_url.replace("www.reddit.com", "old.reddit.com")
        if not post_url.startswith("https://old.reddit.com"):
            post_url = re.sub(r"https?://[^/]*reddit\.com", "https://old.reddit.com", post_url)
        print(f"    Found post: {post_url}")
        return post_url

    print(f"    [!] No posts found for search: {query}")
    return None


async def login_to_reddit(page: Page, context):
    """Log in to Reddit via Google OAuth, fully automated."""
    print("\n[1] LOGGING IN")
    print("=" * 60)

    # Get credentials from Keychain
    google_email = get_keychain_value("reddit-google-email")
    google_password = get_keychain_value("reddit-google-password")

    if not google_email or not google_password:
        print("  [!] Could not read credentials from Keychain.")
        print("  Make sure you ran:")
        print('    security add-generic-password -a "reddit-google-email" -s "reddit-google-email" -w \'your@email.com\'')
        print('    security add-generic-password -a "reddit-google-password" -s "reddit-google-password" -w \'yourpassword\'')
        print("\n  Falling back to manual login...")
        await page.goto("https://www.reddit.com/login")
        await asyncio.sleep(3)
        if NON_INTERACTIVE:
            print("  Non-interactive mode: waiting 30s for manual login...")
            await asyncio.sleep(30)
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

    # Click "Continue with Google"
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
            print("  [!] Could not find Google button. Non-interactive: waiting 30s...")
            await asyncio.sleep(30)
        else:
            print("  [!] Could not find Google button. Log in manually, then press ENTER.")
            await asyncio.get_event_loop().run_in_executor(None, input)
        await asyncio.sleep(2)
        print(f"  [OK] Proceeding as {REDDIT_USERNAME}\n")
        return

    print("  Clicking 'Continue with Google'...")

    # Google opens a popup window. Listen for it.
    async with context.expect_page() as popup_info:
        await google_btn.click()

    google_page = await popup_info.value
    await google_page.wait_for_load_state("domcontentloaded")
    await asyncio.sleep(3)

    # Fill in email
    print("  Entering email...")
    try:
        email_input = await google_page.wait_for_selector(
            'input[type="email"]', timeout=10000
        )
        await email_input.fill(google_email)
        await asyncio.sleep(1)

        # Click Next
        next_btn = await google_page.wait_for_selector(
            'button:has-text("Next"), #identifierNext', timeout=5000
        )
        await next_btn.click()
        await asyncio.sleep(4)

        # Fill in password
        print("  Entering password...")
        password_input = await google_page.wait_for_selector(
            'input[type="password"]', timeout=10000
        )
        await password_input.fill(google_password)
        await asyncio.sleep(1)

        # Click Next
        next_btn2 = await google_page.wait_for_selector(
            'button:has-text("Next"), #passwordNext', timeout=5000
        )
        await next_btn2.click()
        await asyncio.sleep(5)

        # Check if 2FA or additional verification is needed
        # If the popup is still open, there might be a 2FA step
        if not google_page.is_closed():
            page_text = await google_page.evaluate("() => document.body.innerText")
            if "2-step" in page_text.lower() or "verify" in page_text.lower():
                print("  [!] Google 2FA/verification required.")
                if NON_INTERACTIVE:
                    print("  Non-interactive mode: waiting 30s for 2FA completion...")
                    await asyncio.sleep(30)
                else:
                    print("  Complete it in the browser, then press ENTER.")
                    await asyncio.get_event_loop().run_in_executor(None, input)

        # Wait for redirect back to Reddit
        await asyncio.sleep(5)
        print(f"  [OK] Logged in as {REDDIT_USERNAME}\n")

    except Exception as e:
        print(f"  [!] Auto-login error: {e}")
        if NON_INTERACTIVE:
            print("  Non-interactive mode: waiting 30s for manual login...")
            await asyncio.sleep(30)
        else:
            print("  Complete login manually in the browser, then press ENTER.")
            await asyncio.get_event_loop().run_in_executor(None, input)
        await asyncio.sleep(2)
        print(f"  [OK] Proceeding as {REDDIT_USERNAME}\n")


async def check_notifications(page: Page):
    """Open notifications for review."""
    print("[2] CHECKING NOTIFICATIONS")
    print("=" * 60)
    await page.goto("https://www.reddit.com/notifications")
    await asyncio.sleep(3)
    if NON_INTERACTIVE:
        print("  Non-interactive mode: skipping manual notification review.")
        await asyncio.sleep(5)
    else:
        print("  Review notifications and reply to any.")
        print("  Press ENTER to continue to posting.")
        print("=" * 60)
        await asyncio.get_event_loop().run_in_executor(None, input)
    print()


async def post_vegasrealtor(page: Page, post_data: Dict) -> bool:
    """Post to r/VegasRealtor using old Reddit submit form."""
    print("[3] POSTING TO r/VegasRealtor")
    print("=" * 60)
    print(f"  Title: {post_data['title']}")
    print(f"  Flair: {post_data['flair']}")

    await page.goto("https://old.reddit.com/r/VegasRealtor/submit?selftext=true")
    await asyncio.sleep(4)

    # Fill in the title
    title_input = await page.query_selector('textarea[name="title"], input[name="title"]')
    if title_input:
        await title_input.fill(post_data["title"])
    else:
        print("  [!] Could not find title field")
        return False

    await asyncio.sleep(1)

    # Fill in the body
    body_input = await page.query_selector('textarea[name="text"]')
    if body_input:
        await body_input.click()
        await body_input.fill(post_data["body"])
    else:
        print("  [!] Could not find body field")
        return False

    await asyncio.sleep(1)

    # Submit
    submit_btn = await page.query_selector('button[type="submit"][name="submit"]')
    if not submit_btn:
        submit_btn = await page.query_selector('button:has-text("submit")')
    if not submit_btn:
        submit_btn = await page.query_selector('#submit button')

    if submit_btn:
        await submit_btn.click()
        await asyncio.sleep(5)
        print(f"  [OK] Posted to r/VegasRealtor: {post_data['title']}")
        print(f"  [!] Remember to add flair '{post_data['flair']}' manually if needed")
        return True
    else:
        print("  [!] Could not find submit button")
        return False


async def post_comment_old_reddit(page: Page, post_url: str, comment_text: str) -> bool:
    """Post a comment using old.reddit.com. Returns True on success."""
    old_url = post_url
    if "old.reddit.com" not in old_url:
        old_url = re.sub(r"https?://[^/]*reddit\.com", "https://old.reddit.com", old_url)

    await page.goto(old_url)
    await asyncio.sleep(4)

    # Check post exists
    page_text = await page.evaluate("() => document.body.innerText")
    if "there doesn't seem to be anything here" in page_text.lower():
        print("    [!] Post not found or deleted")
        return False

    # Find comment box
    comment_box = await page.query_selector('textarea[name="text"]')
    if not comment_box:
        comment_box = await page.query_selector(".usertext-edit textarea")
    if not comment_box:
        print("    [!] No comment box (post may be archived/locked)")
        return False

    # Type comment
    await comment_box.click()
    await asyncio.sleep(1)
    await comment_box.fill(comment_text.strip())
    await asyncio.sleep(1)

    # Verify text entered
    entered = await comment_box.input_value()
    if len(entered) < 50:
        print("    [!] Text fill failed, retrying...")
        await comment_box.fill("")
        await asyncio.sleep(0.5)
        await comment_box.fill(comment_text.strip())
        await asyncio.sleep(1)

    # Submit
    submit_btn = await page.query_selector('.usertext-buttons button[type="submit"]')
    if not submit_btn:
        submit_btn = await page.query_selector("button.save")
    if not submit_btn:
        submit_btn = await page.query_selector('button:has-text("save")')

    if submit_btn:
        await submit_btn.click()
        await asyncio.sleep(5)

        # Check for errors
        error = await page.query_selector(".error")
        if error:
            error_text = await error.inner_text()
            if error_text.strip():
                print(f"    [!] Reddit error: {error_text.strip()}")
                return False

        print("    [OK] Comment posted!")
        return True
    else:
        print("    [!] Submit button not found")
        return False


async def upvote_post(page: Page):
    """Upvote the current post on old Reddit."""
    try:
        upvote = await page.query_selector(
            ".thing.link .arrow.up, .thing.link .arrow.upmod"
        )
        if upvote:
            cls = await upvote.get_attribute("class")
            if "upmod" not in cls:
                await upvote.click()
                print("    [OK] Upvoted")
            else:
                print("    [OK] Already upvoted")
    except Exception:
        pass


async def post_reply_old_reddit(page: Page, comment_url: str, reply_text: str) -> bool:
    """Navigate to a comment on old.reddit.com and post a reply. Returns True on success."""
    old_url = comment_url
    if "old.reddit.com" not in old_url:
        old_url = re.sub(r"https?://[^/]*reddit\.com", "https://old.reddit.com", old_url)

    await page.goto(old_url)
    await asyncio.sleep(4)

    # On old Reddit, the target comment should be highlighted. Find the reply link.
    # The URL with a comment ID (e.g., /comments/abc/slug/def456/) focuses that comment.
    # Look for the "reply" link in the targeted/highlighted comment.
    reply_link = await page.query_selector(".thing.target .flat-list a.reply-button, .thing.target a[onclick*='reply']")
    if not reply_link:
        # Fallback: find any reply link in the comment area
        reply_link = await page.query_selector(".commentarea .thing .flat-list a.reply-button")
    if not reply_link:
        # Broader fallback: look for "reply" text links
        reply_link = await page.query_selector(".commentarea a:has-text('reply')")

    if not reply_link:
        print("    [!] Could not find reply link on comment")
        return False

    await reply_link.click()
    await asyncio.sleep(2)

    # Find the reply textarea that appeared
    reply_box = await page.query_selector(".thing.target .usertext-edit textarea")
    if not reply_box:
        reply_box = await page.query_selector(".commentarea .usertext-edit textarea:visible")
    if not reply_box:
        # Broader: any visible textarea in the comment area
        textareas = await page.query_selector_all(".commentarea textarea[name='text']")
        for ta in textareas:
            if await ta.is_visible():
                reply_box = ta
                break

    if not reply_box:
        print("    [!] Could not find reply textarea")
        return False

    await reply_box.click()
    await asyncio.sleep(1)
    await reply_box.fill(reply_text.strip())
    await asyncio.sleep(1)

    # Verify text entered
    entered = await reply_box.input_value()
    if len(entered) < 20:
        print("    [!] Text fill failed, retrying...")
        await reply_box.fill("")
        await asyncio.sleep(0.5)
        await reply_box.fill(reply_text.strip())
        await asyncio.sleep(1)

    # Find the save button in the same form
    save_btn = await page.query_selector(".thing.target .usertext-buttons button[type='submit']")
    if not save_btn:
        save_btn = await page.query_selector(".commentarea .usertext-buttons button.save:visible")
    if not save_btn:
        buttons = await page.query_selector_all(".commentarea button.save, .commentarea button:has-text('save')")
        for btn in buttons:
            if await btn.is_visible():
                save_btn = btn
                break

    if save_btn:
        await save_btn.click()
        await asyncio.sleep(5)

        # Check for errors
        error = await page.query_selector(".error")
        if error:
            error_text = await error.inner_text()
            if error_text.strip():
                print(f"    [!] Reddit error: {error_text.strip()}")
                return False

        print("    [OK] Reply posted!")
        return True
    else:
        print("    [!] Save button not found")
        return False


# ─── MAIN ─────────────────────────────────────────────────────────────────────


async def main():
    # ── Parse CLI args ──
    global NON_INTERACTIVE
    args = sys.argv[1:]
    skip_vr = "--skip-vegasrealtor" in args
    args = [a for a in args if a != "--skip-vegasrealtor"]
    if "--non-interactive" in args:
        NON_INTERACTIVE = True
        args = [a for a in args if a != "--non-interactive"]

    delay = COMMENT_DELAY
    if "--delay" in args:
        idx = args.index("--delay")
        delay = int(args[idx + 1])
        args = args[:idx] + args[idx + 2 :]

    # ── Find drafts file ──
    if args and not args[0].startswith("--"):
        filepath = args[0]
        if not os.path.isabs(filepath):
            filepath = os.path.join(SCRIPT_DIR, filepath)
    else:
        filepath = find_todays_file()

    if not os.path.exists(filepath):
        print(f"[ERROR] File not found: {filepath}")
        sys.exit(1)

    filename = os.path.basename(filepath)
    print("=" * 60)
    print(f"  REDDIT DAILY AUTO-POSTER")
    print(f"  File:    {filename}")
    print(f"  Account: u/{REDDIT_USERNAME}")
    print(f"  Delay:   {delay}s between comments")
    if skip_vr:
        print(f"  Skip:    r/VegasRealtor post")
    if NON_INTERACTIVE:
        print(f"  Mode:    non-interactive")
    print("=" * 60)

    # ── Parse the file ──
    drafts = parse_drafts_file(filepath, skip_vegasrealtor=skip_vr)

    vr_post = drafts["vegasrealtor_post"]
    comments = drafts["comments"]
    replies = drafts["replies"]

    if replies:
        print(f"\n  Found {len(replies)} notification replies to post")
    print(f"  Found {len(comments)} comments to post")
    if vr_post:
        print(f"  Found r/VegasRealtor post: {vr_post['title']}")
    else:
        print(f"  No r/VegasRealtor post (skipped or not in file)")

    for i, c in enumerate(comments):
        url_count = len(c["urls"])
        print(f"    {i+1}. r/{c['subreddit']} ({url_count} post link{'s' if url_count != 1 else ''})")

    print()

    # ── Launch browser ──
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=HEADLESS,
            slow_mo=300,
            args=["--disable-blink-features=AutomationControlled"],
        )
        context = await browser.new_context(
            viewport={"width": 1280, "height": 900},
            user_agent=(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/122.0.0.0 Safari/537.36"
            ),
        )
        page = await context.new_page()

        # ── Login ──
        await login_to_reddit(page, context)

        # ── Notifications ──
        await check_notifications(page)

        # ── Notification replies ──
        replies_posted = 0
        replies_failed = 0
        step = 3
        if replies:
            print(f"\n[{step}] POSTING {len(replies)} NOTIFICATION REPLIES")
            print("=" * 60)
            for i, reply in enumerate(replies):
                num = i + 1
                print(f"\n--- Reply {num}/{len(replies)} ---")
                print(f"    URL: {reply['url']}")
                if reply['context']:
                    print(f"    Context: {reply['context']}")
                print(f"    Text preview: {reply['text'][:80]}...")
                success = await post_reply_old_reddit(page, reply['url'], reply['text'])
                if success:
                    replies_posted += 1
                else:
                    replies_failed += 1
                if i < len(replies) - 1:
                    print(f"    Waiting 10s...")
                    await asyncio.sleep(10)
            print()
            step += 1

        # ── r/VegasRealtor post ──
        if vr_post:
            await post_vegasrealtor(page, vr_post)
            print()
            step = 4

        # ── Off-sub comments ──
        print(f"[{step}] POSTING {len(comments)} OFF-SUB COMMENTS")
        print("=" * 60)

        posted = 0
        skipped = 0
        failed = 0

        for i, comment in enumerate(comments):
            num = i + 1
            print(f"\n--- Comment {num}/{len(comments)} | r/{comment['subreddit']} ---")
            print(f"    Text preview: {comment['text'][:80]}...")

            success = False
            post_url = None

            # Try direct URLs first
            if comment["urls"]:
                for j, url in enumerate(comment["urls"]):
                    print(f"    Trying link {j+1}/{len(comment['urls'])}: {url}")
                    success = await post_comment_old_reddit(page, url, comment["text"])
                    if success:
                        await upvote_post(page)
                        break
                    else:
                        print(f"    Trying next link...")
                        await asyncio.sleep(2)

            # Fallback: search for a post if no URLs or all URLs failed
            if not success and comment.get("search_query"):
                print(f"    No direct URLs — searching for a post...")
                post_url = await find_post_via_search(
                    page, comment["subreddit"], comment["search_query"]
                )
                if post_url:
                    success = await post_comment_old_reddit(page, post_url, comment["text"])
                    if success:
                        await upvote_post(page)

            if success:
                posted += 1
            elif not comment["urls"] and not comment.get("search_query"):
                print(f"    [SKIPPED] No post URLs or search query for this comment")
                skipped += 1
            elif not success:
                print(f"    [FAILED] Could not post this comment")
                failed += 1

            # Wait between comments
            if i < len(comments) - 1 and success:
                print(f"\n    Waiting {delay}s...")
                for remaining in range(delay, 0, -15):
                    print(f"      {remaining}s...")
                    await asyncio.sleep(min(15, remaining))

        # ── Summary ──
        print("\n" + "=" * 60)
        print("  DONE!")
        if replies:
            print(f"  Replies posted:  {replies_posted}/{len(replies)}")
        print(f"  Comments posted: {posted}/{len(comments)}")
        print(f"  Comments skipped: {skipped}")
        print(f"  Comments failed: {failed}")
        if vr_post:
            print(f"  VegasRealtor post: submitted")
        print("=" * 60)

        # Structured output for log parsing
        print("\n=== RESULTS ===")
        print(f"Replies posted: {replies_posted}/{len(replies)}")
        vr_status = "SUCCESS" if vr_post else "SKIPPED"
        print(f"VegasRealtor post: {vr_status}")
        print(f"Comments posted: {posted}/{len(comments)}")
        print(f"Comments failed: {failed}/{len(comments)}")
        print(f"Comments skipped: {skipped}/{len(comments)}")
        print("=== END RESULTS ===")

        await asyncio.sleep(5)
        await browser.close()
        print("\n  Browser closed. Update your status tracker if needed.")


if __name__ == "__main__":
    asyncio.run(main())
