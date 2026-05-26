"""
Reddit Post Discovery Script
Searches target subreddits and extracts post content BEFORE Claude writes comments.
Saves results to PostDiscovery_[MonDD]_[YYYY].md so Claude can write context-aware comments.

Usage:
    python3 reddit_discover.py                  # auto-generates today's discovery file
    python3 reddit_discover.py --queries-file queries.txt  # custom search queries
    python3 reddit_discover.py --results 3      # how many candidate posts per query (default 3)

Run this BEFORE the Cowork session generates DailyDrafts. Then Cowork reads the
PostDiscovery file and writes comments tailored to each real post's content.

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
from playwright.async_api import async_playwright, Page


# ─── CONFIG ───────────────────────────────────────────────────────────────────

REDDIT_USERNAME = "Silver_Artichoke_812"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
HEADLESS = False  # Set to True to run without browser window

# Default search queries per subreddit (10 total, 2 per sub)
# Claude will pick the best post from each set of results
DEFAULT_QUERIES = [
    {"subreddit": "vegaslocals",        "query": "buying home Las Vegas 2026"},
    {"subreddit": "vegaslocals",        "query": "moving neighborhood rent HOA Vegas"},
    {"subreddit": "vegas",              "query": "moving to Las Vegas neighborhood advice"},
    {"subreddit": "vegas",              "query": "buying house Vegas cost of living"},
    {"subreddit": "LasVegas",           "query": "real estate Henderson Summerlin buying"},
    {"subreddit": "LasVegas",           "query": "first time home buyer Las Vegas"},
    {"subreddit": "FirstTimeHomeBuyer", "query": "Las Vegas Nevada closing mortgage"},
    {"subreddit": "FirstTimeHomeBuyer", "query": "Nevada home purchase first time 2026"},
    {"subreddit": "RealEstate",         "query": "Las Vegas Nevada investment buying"},
    {"subreddit": "RealEstate",         "query": "Henderson Nevada real estate purchase"},
]


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


def clean_text(text: str) -> str:
    """Clean and truncate post body text."""
    if not text:
        return ""
    # Remove excessive whitespace
    text = re.sub(r'\n{3,}', '\n\n', text.strip())
    # Truncate to ~800 chars for readability in the discovery file
    if len(text) > 800:
        text = text[:797] + "..."
    return text


async def login_to_reddit(page: Page, context):
    """Log in to Reddit via Google OAuth."""
    print("\n[LOGIN] Logging in to Reddit...")

    google_email = get_keychain_value("reddit-google-email")
    google_password = get_keychain_value("reddit-google-password")

    if not google_email or not google_password:
        print("  [!] Could not read credentials from Keychain.")
        print("  Log in manually in the browser, then press ENTER.")
        await page.goto("https://www.reddit.com/login")
        await asyncio.sleep(3)
        await asyncio.get_event_loop().run_in_executor(None, input)
        await asyncio.sleep(2)
        print(f"  [OK] Proceeding as {REDDIT_USERNAME}\n")
        return

    await page.goto("https://www.reddit.com/login")
    await asyncio.sleep(4)

    # Click "Continue with Google"
    google_btn = None
    for sel in [
        'button:has-text("Continue with Google")',
        'a:has-text("Continue with Google")',
        '[data-provider="google"]',
        'button:has-text("Google")',
    ]:
        try:
            btn = await page.wait_for_selector(sel, timeout=3000)
            if btn:
                google_btn = btn
                break
        except Exception:
            continue

    if not google_btn:
        print("  [!] Could not find Google button. Log in manually, then press ENTER.")
        await asyncio.get_event_loop().run_in_executor(None, input)
        await asyncio.sleep(2)
        print(f"  [OK] Proceeding as {REDDIT_USERNAME}\n")
        return

    async with context.expect_page() as popup_info:
        await google_btn.click()

    google_page = await popup_info.value
    await google_page.wait_for_load_state("domcontentloaded")
    await asyncio.sleep(3)

    try:
        email_input = await google_page.wait_for_selector('input[type="email"]', timeout=10000)
        await email_input.fill(google_email)
        await asyncio.sleep(1)
        next_btn = await google_page.wait_for_selector('button:has-text("Next"), #identifierNext', timeout=5000)
        await next_btn.click()
        await asyncio.sleep(4)

        password_input = await google_page.wait_for_selector('input[type="password"]', timeout=10000)
        await password_input.fill(google_password)
        await asyncio.sleep(1)
        next_btn2 = await google_page.wait_for_selector('button:has-text("Next"), #passwordNext', timeout=5000)
        await next_btn2.click()
        await asyncio.sleep(5)

        if not google_page.is_closed():
            page_text = await google_page.evaluate("() => document.body.innerText")
            if "2-step" in page_text.lower() or "verify" in page_text.lower():
                print("  [!] 2FA required. Complete it, then press ENTER.")
                await asyncio.get_event_loop().run_in_executor(None, input)

        await asyncio.sleep(5)
        print(f"  [OK] Logged in as {REDDIT_USERNAME}\n")

    except Exception as e:
        print(f"  [!] Auto-login error: {e}")
        print("  Complete login manually in the browser, then press ENTER.")
        await asyncio.get_event_loop().run_in_executor(None, input)
        await asyncio.sleep(2)
        print(f"  [OK] Proceeding as {REDDIT_USERNAME}\n")


async def search_and_extract_posts(page: Page, subreddit: str, query: str, num_results: int = 3) -> List[Dict]:
    """
    Search a subreddit and extract post content from the top results.
    Returns a list of post dicts with: title, url, age, comment_count, body
    """
    search_url = (
        f"https://old.reddit.com/r/{subreddit}/search"
        f"?q={query.replace(' ', '+')}&restrict_sr=on&sort=new&t=year&limit=25"
    )
    print(f"  Searching r/{subreddit}: \"{query}\"")
    await page.goto(search_url)
    await asyncio.sleep(4)

    # Extract post links from search results
    post_links = await page.evaluate("""
        () => {
            const results = [];
            const items = document.querySelectorAll('.search-result-link, .search-result');
            for (const item of items) {
                const titleEl = item.querySelector('.search-title, .title a[href*="/comments/"]');
                const timeEl = item.querySelector('time, .search-result-meta time');
                const commentsEl = item.querySelector('a[href*="/comments/"]:last-child, .search-comments');

                if (titleEl) {
                    const href = titleEl.getAttribute('href');
                    results.push({
                        url: href && href.startsWith('http') ? href : 'https://old.reddit.com' + href,
                        title: titleEl.innerText || titleEl.textContent,
                        age: timeEl ? timeEl.getAttribute('title') || timeEl.innerText : '',
                        comments: commentsEl ? commentsEl.innerText : ''
                    });
                }
                if (results.length >= 8) break;
            }
            return results;
        }
    """)

    if not post_links:
        # Fallback: grab any /comments/ links
        post_links = await page.evaluate("""
            () => {
                const seen = new Set();
                const results = [];
                const allLinks = document.querySelectorAll('a[href*="/comments/"]');
                for (const link of allLinks) {
                    const href = link.getAttribute('href');
                    if (href && !seen.has(href) && !href.includes('/user/')) {
                        seen.add(href);
                        const url = href.startsWith('http') ? href : 'https://old.reddit.com' + href;
                        results.push({ url, title: link.innerText.trim(), age: '', comments: '' });
                    }
                    if (results.length >= 8) break;
                }
                return results;
            }
        """)

    posts = []
    count = 0
    for link_data in post_links:
        if count >= num_results:
            break
        url = link_data.get("url", "")
        if not url or "/comments/" not in url:
            continue

        # Convert to old.reddit.com
        url = re.sub(r"https?://[^/]*reddit\.com", "https://old.reddit.com", url)

        print(f"    Reading post: {url}")
        try:
            await page.goto(url)
            await asyncio.sleep(3)

            # Extract post content
            post_data = await page.evaluate("""
                () => {
                    // Title
                    const titleEl = document.querySelector('.thing.link .title a.title, h1.title');
                    const title = titleEl ? titleEl.innerText.trim() : '';

                    // Body text (self post)
                    const bodyEl = document.querySelector('.thing.link .usertext-body .md');
                    const body = bodyEl ? bodyEl.innerText.trim() : '';

                    // Age
                    const timeEl = document.querySelector('.thing.link time');
                    const age = timeEl ? timeEl.getAttribute('title') || timeEl.innerText : '';

                    // Comment count
                    const commentEl = document.querySelector('.thing.link .comments');
                    const commentCount = commentEl ? commentEl.innerText.trim() : '';

                    // Check if archived/locked
                    const archived = !!document.querySelector('.archived-infobar, .locked-infobar');

                    // Top-level comment count estimate
                    const topComments = document.querySelectorAll('.commentarea > .thing.comment').length;

                    return { title, body, age, commentCount, archived, topComments };
                }
            """)

            if post_data.get("archived"):
                print(f"    [skip] Post is archived")
                continue

            if not post_data.get("title"):
                print(f"    [skip] Could not extract title")
                continue

            posts.append({
                "subreddit": subreddit,
                "url": url,
                "title": post_data.get("title", link_data.get("title", "")).strip(),
                "body": clean_text(post_data.get("body", "")),
                "age": post_data.get("age", link_data.get("age", "")).strip(),
                "comment_count": post_data.get("commentCount", "").strip(),
            })
            count += 1
            print(f"    [OK] Extracted: \"{post_data.get('title', '')[:60]}\"")

        except Exception as e:
            print(f"    [!] Error reading post: {e}")
            continue

    return posts


def write_discovery_file(results: List[Dict], output_path: str):
    """Write the discovery results to a markdown file."""
    now = datetime.now()
    date_str = now.strftime("%A, %B %d, %Y")

    lines = [
        f"# Post Discovery — {date_str}",
        "",
        "**Generated by:** reddit_discover.py",
        f"**Date:** {date_str}",
        "**Purpose:** Claude reads this file and writes context-aware comments for DailyDrafts.",
        "",
        "---",
        "",
        "## HOW TO USE THIS FILE",
        "",
        "This file contains real Reddit posts found today. For each slot below:",
        "1. Claude reads the post title and body",
        "2. Claude writes a comment that responds SPECIFICALLY to what the OP asked",
        "3. The post URL is locked in — no searching needed",
        "",
        "Writing rules still apply: no em-dashes, 6th grade reading level, data-rich,",
        "knowledgeable neighbor voice, no links, no self-promotion.",
        "Do NOT identify as agent in r/FirstTimeHomeBuyer posts.",
        "",
        "---",
        "",
    ]

    for i, post in enumerate(results, 1):
        sub = post["subreddit"]
        url = post["url"]
        title = post["title"]
        body = post["body"]
        age = post["age"]
        comments = post["comment_count"]

        lines += [
            f"## Slot {i} — r/{sub}",
            "",
            f"**Post URL:** {url}",
            f"**Title:** {title}",
            f"**Age:** {age}",
            f"**Comments:** {comments}",
            "",
            "**Post body:**",
            "",
            body if body else "(Link post or no body text — write comment based on title alone.)",
            "",
            "---",
            "",
            f"### Draft Comment {i} — r/{sub}",
            "",
            "*(Claude: write your tailored comment here, responding to the specific post above)*",
            "",
            "---",
            "",
        ]

    with open(output_path, "w") as f:
        f.write("\n".join(lines))

    print(f"\n[OK] Discovery file saved: {os.path.basename(output_path)}")
    print(f"     {len(results)} posts found and saved.")


async def main():
    args = sys.argv[1:]
    num_results = 1  # Default: 1 best post per query slot

    if "--results" in args:
        idx = args.index("--results")
        num_results = int(args[idx + 1])
        args = args[:idx] + args[idx + 2:]

    # Output file
    now = datetime.now()
    month_abbr = now.strftime("%b")
    day = now.strftime("%d")
    year = now.strftime("%Y")
    output_filename = f"PostDiscovery_{month_abbr}{day}_{year}.md"
    output_path = os.path.join(SCRIPT_DIR, output_filename)

    print("=" * 60)
    print("  REDDIT POST DISCOVERY")
    print(f"  Output: {output_filename}")
    print(f"  Queries: {len(DEFAULT_QUERIES)}")
    print(f"  Posts per query: {num_results}")
    print("=" * 60)

    all_posts = []

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

        # Login
        await login_to_reddit(page, context)

        # Search each query
        print("\n[SEARCHING] Finding posts...\n")
        for q in DEFAULT_QUERIES:
            posts = await search_and_extract_posts(
                page, q["subreddit"], q["query"], num_results=num_results
            )
            all_posts.extend(posts)
            await asyncio.sleep(3)

        await browser.close()

    # Write discovery file
    write_discovery_file(all_posts, output_path)
    print(f"\nNext step: Open Cowork and run the daily Reddit routine.")
    print(f"Cowork will read {output_filename} and write tailored comments.")


if __name__ == "__main__":
    asyncio.run(main())
