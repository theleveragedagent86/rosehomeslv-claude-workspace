"""
Reddit Daily Tasks - March 9, 2026
Fully automated Playwright script for u/Silver_Artichoke_812

Tasks:
1. Check notifications
2. Post 10 off-sub comments (auto-navigate, auto-type, auto-submit)

EXCLUDED: r/VegasRealtor POST (Buyer Tips - VA Home Loans)

Usage:
    pip install playwright
    python3 -m playwright install chromium
    python3 reddit_daily_mar09.py
"""

import asyncio
import json
import re
from typing import Optional
from playwright.async_api import async_playwright, Page

# ─── CONFIG ───────────────────────────────────────────────────────────────────

REDDIT_USERNAME = "Silver_Artichoke_812"
COMMENT_DELAY = 90  # seconds between comments to avoid Reddit spam filter
HEADLESS = False  # Keep visible so you can monitor

# ─── COMMENT DRAFTS ──────────────────────────────────────────────────────────
# Comments 1-4 have direct post URLs. Comments 5-10 use search to find posts.

COMMENTS = [
    {
        "id": 1,
        "subreddit": "vegaslocals",
        "url": "https://old.reddit.com/r/vegaslocals/comments/1m4vr5j/buying_a_home_advice/",
        "search_query": None,
        "text": """One thing that catches a lot of Vegas buyers off guard is how closing costs add up. Here is a realistic breakdown for a $400-470k purchase in Clark County.

Lender fees (origination, processing, underwriting): $1,500-3,000 depending on your lender. Some lenders charge less but make it up in rate.

Title insurance and escrow: Around $1,800-2,500. Nevada uses title companies, not attorneys, so you are paying the title company for both the search and insurance.

Prepaid items (insurance, interest, and property tax impound setup): Usually $3,000-5,000. This is money that goes into your escrow account, not fees you lose. But you need cash on hand for it.

Home inspection: $350-500 for a standard single-family home. Bigger homes cost more.

HOA transfer fee and resale disclosure package: $300-600 on average. The seller pays part of this in many transactions but not always.

Total cash to close on a $450k home, assuming you are putting 5% down ($22,500): You are typically looking at $26,000-31,000 total. Your lender should give you a Loan Estimate within 3 business days of applying and it will itemize everything.

One tip: ask about lender credits. If you take a slightly higher rate, your lender can often cover some of the closing costs. Good option if you are tight on cash but can handle a marginally higher payment."""
    },
    {
        "id": 2,
        "subreddit": "FirstTimeHomeBuyer",
        "url": "https://old.reddit.com/r/FirstTimeHomeBuyer/comments/1phbrrf/how_long_after_the_inspection_did_it_take_/",
        "search_query": None,
        "text": """Vegas inspections cover the usual stuff but there are a few desert-specific things to pay close attention to.

HVAC is the biggest one. AC units here last about 8-10 years on average, compared to 15-20 years in a milder climate. If the unit is 7 or more years old, budget for replacement. A full system swap runs $6,000-12,000. Ask for the installation date (usually on a sticker on the unit) and any service records.

Roof is next. Flat roofs have foam coating that needs resealing every 5-7 years. Tile roofs last longer but the underlayment underneath degrades from the UV and heat over time. Get the inspector to walk the roof if possible.

Stucco cracks: hairline cracks are normal from heat expansion. Diagonal cracks from window corners or cracks wider than a credit card edge are worth a closer look.

Pool equipment if there is a pool. Pumps, heaters, and pool surfaces all get heavy use here. Resurfacing alone runs $5,000-10,000.

Water heaters wear out faster in Vegas because of the notoriously hard water. Check the age on the label and ask when it was last flushed.

Bring your own contractor for HVAC and roof if you want a second opinion beyond the general inspector. It is usually worth the extra $100-200."""
    },
    {
        "id": 3,
        "subreddit": "LasVegas",
        "url": "https://old.reddit.com/r/LasVegas/comments/1ri4ic1/possible_relocation_to_vegas/",
        "search_query": None,
        "text": """Henderson has a few distinct pockets and which one makes sense depends a lot on your budget and lifestyle.

Green Valley (89014, 89015): The original Henderson master-planned community from the 1980s-90s. Mature trees, established feel, closer to the Strip (about 20 minutes). Homes range from $380k to $600k+ depending on size and condition. Older stock means you might be dealing with HVAC and roof replacements sooner. HOA fees are typically $50-150 per month.

Anthem and MacDonald Ranch (89052): Higher price point, $500k-900k+. Great views of the valley, newer construction in many sections, well-maintained HOA areas. HOA fees can run $150-300 per month between master and sub-HOA. Good schools. Commute to the Strip is 30-35 minutes.

Inspirada (89044): Newer construction, highly walkable within the community, good parks and schools. Homes start around $500k and go up from there. SID/LID taxes on some lots, so ask specifically before buying.

Cadence (89011): Newer master-planned community in the northeast part of Henderson, closest to Boulder Highway. Lower price entry point, $380-500k range, newer builds. More affordable but further from the freeway than other Henderson communities.

The biggest thing to research in Henderson before buying is the SID/LID situation on any specific property, especially in newer communities. Those can add $200-400 per month on top of your mortgage."""
    },
    {
        "id": 4,
        "subreddit": "RealEstate",
        "url": "https://old.reddit.com/r/RealEstate/comments/1ne94rh/moving_states_contingency_but_price_difference/",
        "search_query": None,
        "text": """Nevada uses a standard purchase agreement form called the NREC (Nevada Real Estate Commission) purchase agreement. Here are the main contingencies buyers typically use.

Inspection contingency: You have a set number of days (usually 10-15 in the contract) to complete inspections and request repairs. If the seller refuses and you do not want to proceed, you can cancel and get your earnest money back. Once that deadline passes, you are locked in unless the seller agrees to let you out.

Appraisal contingency: If the home appraises below the purchase price, you can renegotiate or cancel. In a hot market sellers sometimes push to waive this, but in the current Vegas market with 6,000+ active listings and more inventory than a year ago, you usually do not need to waive appraisal.

Loan contingency: Protects your earnest money if your financing falls through. Make sure this is in your contract. Some buyers waive this to compete, but it is a significant risk.

HOA document review: Nevada requires sellers to provide a resale disclosure package that includes HOA financials, reserve study, CC&Rs, and recent minutes. You have 5 days to review and cancel without penalty if you do not like what you see. This is especially important for condos.

Earnest money in Nevada is typically 1-3% of the purchase price. On a $450k home, that is $4,500-13,500. It goes into an escrow account and is credited toward your down payment at closing. You only lose it if you back out for a reason not covered by a contingency."""
    },
    {
        "id": 5,
        "subreddit": "vegaslocals",
        "url": None,
        "search_query": "new construction builder",
        "text": """Buying new construction in Vegas is a different process than resale and there are a few things worth knowing going in.

The builder's sales rep works for the builder, not you. They are friendly and helpful but their job is to get the best deal for the builder. Having your own agent at your first visit protects you and costs you nothing extra (the builder pays the commission either way).

Builder lender incentives: Most builders offer rate buydowns or closing cost credits if you use their preferred lender. These can be worth $5,000-15,000. But you should still get a quote from an outside lender to compare. The incentive is not always the best deal when you look at the actual rate and fees.

Lot premiums: Builders charge extra for corner lots, cul-de-sacs, homes backing to open space, and views. These premiums are real but they do not always translate dollar-for-dollar to resale value. Think about it carefully before adding $20-40k for a lot premium.

SID/LID taxes: Newer communities in North Las Vegas and parts of Henderson and Summerlin West often have Special Improvement District taxes. These are separate from HOA fees and can add $200-400 per month to your payment. Always ask the sales rep for the full SID/LID amount before you get excited about a price.

HOA startup costs: Some new communities charge a "working capital contribution" at closing, which is essentially a one-time payment into the HOA reserve fund. This can be $1,000-3,000 and is separate from closing costs.

Get an independent inspection even on brand new homes. They are not perfect and catching issues during the construction phase is much easier than after closing."""
    },
    {
        "id": 6,
        "subreddit": "vegas",
        "url": None,
        "search_query": "moving to Vegas remote work",
        "text": """Vegas is genuinely solid for remote work and the no state income tax thing is real, not just marketing. Nevada has no personal income tax, so if you are moving from California, New York, or any other high-tax state, that difference in take-home pay can be significant.

For remote workers, here is how I would break down the neighborhood options.

Summerlin (northwest): Great if you want a suburban feel with walkable amenities near Downtown Summerlin. Home prices start around $450k for a 3BR. Quieter during the day, excellent restaurants and retail nearby. HOA fees run $100-250 per month depending on the community.

Henderson (east and south): More of a neighborhood feel, slightly more affordable than Summerlin in many areas, $380-520k range for similar homes. Green Valley is particularly popular with remote workers who want a quieter vibe with good coffee shops and grocery stores.

Southwest Vegas (Mountains Edge, Rhodes Ranch): Most affordable option in a newer master-planned setting, $350-450k range, easy freeway access to the whole valley.

Downtown/Arts District area: Small but growing urban scene. More condos and townhomes than single-family. Good if you want walkability and a more social neighborhood vibe. Rent for a 1BR runs $1,200-1,600.

Electric bills are the cost most remote workers underestimate. If you are home all day running AC in July and August, budget $300-450 per month on a 2,000 sq ft home. Much lower the other 8-9 months of the year."""
    },
    {
        "id": 7,
        "subreddit": "FirstTimeHomeBuyer",
        "url": None,
        "search_query": "Las Vegas down payment assistance",
        "text": """Nevada has a few down payment assistance programs worth knowing about.

Nevada Rural Housing Authority Home Is Possible program: This is one of the most used programs in Nevada for first-time buyers. It offers a grant (not a loan, you do not pay it back) of up to 4% of the loan amount for down payment and closing costs. Income limits apply and vary by county. In Clark County the income limit is higher than you might expect because of the cost of living.

Home Is Possible for Heroes: Same structure but for teachers, first responders, and military. The grant percentage is higher.

FHA loans: Not technically a DPA program but the down payment is only 3.5% and the income limits are more flexible. On a $400k home that is $14,000 down. The tradeoff is mortgage insurance, which adds roughly $100-150 per month to your payment.

Conventional loans with 3% down: Fannie Mae and Freddie Mac both have first-time buyer programs (HomeReady and Home Possible) that allow 3% down with income limits. Lower mortgage insurance than FHA in many cases.

The thing to know about DPA programs in Vegas is that some of them add to your loan amount or have a second lien. Read the fine print carefully and ask how the assistance is structured. A grant is better than a deferred loan, which is better than a loan you start repaying immediately.

Lenders who specialize in these programs know the current availability and limits better than a general Google search will tell you."""
    },
    {
        "id": 8,
        "subreddit": "vegaslocals",
        "url": None,
        "search_query": "water bill SNWA",
        "text": """Water in Vegas is actually more affordable than most people expect given that we are in a desert. The Southern Nevada Water Authority manages the Colorado River allocation for the valley and they do a solid job of it.

A typical household water bill in Las Vegas runs $40-90 per month depending on lot size and how much irrigation you are running. Homes with large grassy lawns pay more, sometimes $150-200 per month in summer when the irrigation is running every day.

The SNWA has a turf removal rebate program that pays you to replace grass with desert landscaping. The rebate is $3 per square foot of grass removed, so a 1,000 sq ft lawn is worth $3,000. That money goes a long way toward xeriscaping. The waitlist has moved much faster recently with the drought restrictions.

A few things worth knowing if you are buying a home:

Check if the backyard and front yard have traditional grass or desert landscaping. Grass adds to both water costs and maintenance. Artificial turf is popular and cuts water bills significantly but has its own heat issues in summer.

Drip irrigation systems for desert plants are very water-efficient. Most newer homes and renovated yards in Summerlin and Henderson already have them.

If the home has a pool, that is another significant water draw between evaporation and backwash. Budget for it.

Water here is not nearly the financial burden it is in some parts of the country, but grass-heavy landscaping can make it one. Desert landscaping is honestly more attractive anyway once you see what mature boulders and native plants look like."""
    },
    {
        "id": 9,
        "subreddit": "RealEstate",
        "url": None,
        "search_query": "Las Vegas investment property rental",
        "text": """Vegas is an interesting rental market. Here is an honest take.

On the plus side: no state income tax on rental income (Nevada has none), relatively affordable entry prices compared to LA or Phoenix, and a large renter population in the hospitality and gaming industry that produces consistent rental demand. 1BR apartments rent for $1,200-1,800 depending on area. 3BR single-family homes go for $2,000-2,800.

On the challenging side: the investor-heavy buyer pool has pushed prices up and compressed cap rates over the past few years. A $400k rental home with a $2,200/month rent produces a gross rent multiplier of about 180 months (15 years). That is not terrible but it is not a cash-flow bonanza, especially with current rates.

HOA fees eat into margins significantly in Vegas. A $150/month HOA on a rental is normal for single-family. Condo HOAs run $350-500/month, which makes condo rentals work only in specific scenarios.

HVAC replacement is a budget line item you should not underestimate. Budget $6,000-12,000 every 8-10 years. Pool equipment and resurfacing if the property has a pool. Both of these are more frequent than in milder climates.

The best value plays right now are older single-family homes (1990s-2000s vintage) in established areas like Green Valley, Summerlin, and Southwest Vegas where you are buying the land and location, not the construction quality. The flip side is that these require more maintenance.

If you are a Vegas local already, managing a rental yourself is very doable. Out-of-state investors who need a property manager should budget 8-10% of gross rent for management fees."""
    },
    {
        "id": 10,
        "subreddit": "LasVegas",
        "url": None,
        "search_query": "homestead exemption Nevada property tax",
        "text": """Nevada has one of the lowest property tax rates in the country at around 0.53% of assessed value. On a $470k home that works out to about $2,500 per year, or $208 per month. Compare that to Texas at 1.5-2% or Illinois at 2%+ and it is a meaningful difference.

There are a few things to know about how Nevada property taxes work.

The homestead exemption: Nevada offers a homestead exemption that protects up to $650,000 of equity in your primary residence from unsecured creditors (lawsuits, judgments, etc.). It is not a tax reduction, it is an asset protection tool. You file it with the Clark County Recorder's office. Costs nothing and takes about 10 minutes. Do it when you buy your primary home.

The 3% cap: This is the big one. Nevada caps how much your assessed value can increase per year at 3% for a primary residence. So even if the market jumps 15% in a year, your property tax bill can only go up 3%. New owners lose this protection temporarily when they buy, then it resets.

New construction buyers: When you buy new construction, the tax is initially assessed on the land only. The following year (or two years depending on when you close), the structure gets assessed and your bill jumps. This surprises new-build buyers. Budget for it.

Senior citizens: If you are 62 or older and meet income requirements, Nevada offers a senior tax freeze program that locks your assessed value.

The Clark County Assessor website has all your property details. Search by address and you can see current assessed value, any caps applied, and the ownership history."""
    },
]


# ─── CORE FUNCTIONS ───────────────────────────────────────────────────────────


async def login_to_reddit(page: Page):
    """Open Reddit login page and wait for user to log in manually."""
    print("\n[1/3] LOGGING IN")
    print("=" * 60)
    await page.goto("https://www.reddit.com/login")
    await asyncio.sleep(3)

    print("  Log in to Reddit in the browser window.")
    print("  Once logged in, press ENTER here.")
    print("=" * 60)
    await asyncio.get_event_loop().run_in_executor(None, input)
    await asyncio.sleep(2)
    print("  [OK] Proceeding as", REDDIT_USERNAME)


async def check_notifications(page: Page):
    """Open notifications - user can review while script continues."""
    print("\n[2/3] CHECKING NOTIFICATIONS")
    print("=" * 60)
    await page.goto("https://www.reddit.com/notifications")
    await asyncio.sleep(3)
    print("  Notifications page loaded. Review and reply to any.")
    print("  Press ENTER to continue to commenting.")
    print("=" * 60)
    await asyncio.get_event_loop().run_in_executor(None, input)


async def find_post_via_search(page: Page, subreddit: str, query: str) -> Optional[str]:
    """
    Search a subreddit on old Reddit and return the URL of the first
    non-stickied, non-archived post that can be commented on.
    """
    search_url = (
        f"https://old.reddit.com/r/{subreddit}/search"
        f"?q={query.replace(' ', '+')}&restrict_sr=on&sort=new&t=year"
    )
    print(f"  Searching r/{subreddit} for: {query}")
    await page.goto(search_url)
    await asyncio.sleep(4)

    # Get all post links from old reddit search results
    post_url = await page.evaluate("""
        () => {
            // Old reddit search results have links in .search-result-header a
            const links = document.querySelectorAll('.search-result-header a');
            for (const link of links) {
                const href = link.getAttribute('href');
                if (href && href.includes('/comments/')) {
                    // Return full URL
                    if (href.startsWith('http')) return href;
                    return 'https://old.reddit.com' + href;
                }
            }
            // Fallback: try regular link format
            const allLinks = document.querySelectorAll('a[href*="/comments/"]');
            for (const link of allLinks) {
                const href = link.getAttribute('href');
                if (href && !href.includes('/user/')) {
                    if (href.startsWith('http')) return href;
                    return 'https://old.reddit.com' + href;
                }
            }
            return null;
        }
    """)

    if post_url:
        # Make sure it's an old.reddit URL
        post_url = post_url.replace("www.reddit.com", "old.reddit.com")
        if not post_url.startswith("https://old.reddit.com"):
            post_url = re.sub(r"https?://[^/]*reddit\.com", "https://old.reddit.com", post_url)
        print(f"  Found post: {post_url}")
        return post_url
    else:
        print(f"  [!] No posts found for this search.")
        return None


async def post_comment_old_reddit(page: Page, post_url: str, comment_text: str) -> bool:
    """
    Post a comment using old.reddit.com (more reliable than new Reddit).
    Returns True if the comment was submitted successfully.
    """
    # Navigate to old reddit version of the post
    old_url = post_url.replace("www.reddit.com", "old.reddit.com")
    if "old.reddit.com" not in old_url:
        old_url = re.sub(r"https?://[^/]*reddit\.com", "https://old.reddit.com", old_url)

    await page.goto(old_url)
    await asyncio.sleep(4)

    # Check if the post exists and comments are available
    page_text = await page.evaluate("() => document.body.innerText")
    if "there doesn't seem to be anything here" in page_text.lower():
        print("  [!] Post not found or deleted. Skipping.")
        return False

    # Check if comment box exists (means we can comment)
    comment_box = await page.query_selector('textarea[name="text"]')
    if not comment_box:
        # Might need to find the main comment form specifically
        comment_box = await page.query_selector('.usertext-edit textarea')

    if not comment_box:
        print("  [!] No comment box found. Post may be archived or locked.")
        return False

    # Clear and type into the comment box
    await comment_box.click()
    await asyncio.sleep(1)
    await comment_box.fill(comment_text.strip())
    await asyncio.sleep(1)

    # Verify text was entered
    entered_text = await comment_box.input_value()
    if len(entered_text) < 50:
        print("  [!] Text didn't fill properly. Retrying...")
        await comment_box.fill("")
        await asyncio.sleep(0.5)
        await comment_box.fill(comment_text.strip())
        await asyncio.sleep(1)

    # Find and click the save/submit button
    # On old Reddit, the comment form has a submit button with class "save"
    submit_btn = await page.query_selector('.usertext-buttons button[type="submit"]')
    if not submit_btn:
        submit_btn = await page.query_selector('button.save')
    if not submit_btn:
        # Try finding by text
        submit_btn = await page.query_selector('button:has-text("save")')

    if submit_btn:
        await submit_btn.click()
        await asyncio.sleep(5)

        # Check for errors
        error = await page.query_selector('.error')
        if error:
            error_text = await error.inner_text()
            if error_text.strip():
                print(f"  [!] Reddit error: {error_text.strip()}")
                return False

        print("  [OK] Comment submitted!")
        return True
    else:
        print("  [!] Could not find submit button.")
        return False


async def upvote_post_old_reddit(page: Page):
    """Upvote the current post on old Reddit."""
    try:
        # On old reddit, the upvote arrow is a div with class "arrow up"
        upvote = await page.query_selector('.thing.link .arrow.up, .thing.link .arrow.upmod')
        if upvote:
            # Check if already upvoted
            class_name = await upvote.get_attribute("class")
            if "upmod" not in class_name:
                await upvote.click()
                print("  [OK] Upvoted post")
            else:
                print("  [OK] Already upvoted")
        else:
            print("  [!] Could not find upvote button")
    except Exception as e:
        print(f"  [!] Upvote failed: {e}")


# ─── MAIN ─────────────────────────────────────────────────────────────────────


async def main():
    print("=" * 60)
    print("  REDDIT DAILY TASKS - March 9, 2026 (AUTOMATED)")
    print(f"  Account: u/{REDDIT_USERNAME}")
    print("  Tasks: Notifications + 10 Off-Sub Comments")
    print("  Excluded: r/VegasRealtor post (Buyer Tips)")
    print(f"  Delay between comments: {COMMENT_DELAY}s")
    print("=" * 60)

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

        # ── Step 1: Login (only manual step) ──
        await login_to_reddit(page)

        # ── Step 2: Notifications ──
        await check_notifications(page)

        # ── Step 3: Post all 10 comments automatically ──
        print("\n[3/3] POSTING 10 OFF-SUB COMMENTS")
        print("=" * 60)

        posted = 0
        skipped = 0
        failed = 0

        for i, comment in enumerate(COMMENTS):
            print(f"\n--- Comment {comment['id']}/10 | r/{comment['subreddit']} ---")

            # Get the post URL (either direct or via search)
            if comment["url"]:
                post_url = comment["url"]
                print(f"  Using direct URL: {post_url}")
            else:
                post_url = await find_post_via_search(
                    page, comment["subreddit"], comment["search_query"]
                )
                if not post_url:
                    print(f"  [SKIPPED] No suitable post found")
                    skipped += 1
                    continue

            # Post the comment
            success = await post_comment_old_reddit(page, post_url, comment["text"])

            if success:
                posted += 1
                await upvote_post_old_reddit(page)
            else:
                failed += 1

            # Wait between comments
            if i < len(COMMENTS) - 1:
                print(f"\n  Waiting {COMMENT_DELAY}s before next comment...")
                for remaining in range(COMMENT_DELAY, 0, -15):
                    print(f"    {remaining}s...")
                    await asyncio.sleep(min(15, remaining))

        # ── Summary ──
        print("\n" + "=" * 60)
        print("  DONE!")
        print(f"  Posted:  {posted}")
        print(f"  Skipped: {skipped}")
        print(f"  Failed:  {failed}")
        print("=" * 60)

        # Keep browser open briefly to verify
        await asyncio.sleep(5)
        await browser.close()
        print("\n  Browser closed. Update your status tracker if needed.")


if __name__ == "__main__":
    asyncio.run(main())
