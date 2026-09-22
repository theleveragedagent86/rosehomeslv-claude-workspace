"""
Reddit Post Discovery — API Version (No Browser Required)
Uses Reddit's public JSON API to find real posts and extract their content.
Runs inside the Cowork scheduler as Step 0 before Claude writes any comments.

Saves results to: PostDiscovery_[MonDD]_[YYYY].md

No login, no Playwright, no Keychain needed.
Requires: pip install requests --break-system-packages
"""

import requests
import json
import time
import random
import sys
import os
from datetime import datetime
from typing import Optional, List, Dict

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# How many candidate posts to fetch per search query
RESULTS_PER_QUERY = 3

# Seconds to wait between API calls (be polite to Reddit's servers)
RATE_LIMIT_DELAY = 2

# Query pools per subreddit — the script picks 2 per sub each day using date-based rotation
# This ensures different posts surface on different days
# Queries must be specific enough to return real-estate-related posts even in general subs
QUERY_POOLS = {
    "vegaslocals": [
        "buying house Las Vegas",
        "moving to Vegas rent house",
        "HOA fees Las Vegas home",
        "electric bill NV Energy house",
        "Las Vegas neighborhood buying home",
        "property tax Nevada house",
        "rent vs buy Las Vegas house",
        "Las Vegas home inspection buying",
        "moving Las Vegas apartment rent",
        "Henderson Summerlin house buying",
    ],
    "vegas": [
        "moving to Las Vegas buying house",
        "rent apartment house Las Vegas cost",
        "relocating Las Vegas home buying",
        "Las Vegas neighborhood house rent",
        "living Las Vegas cost housing",
        "moving Vegas house rent advice",
        "Las Vegas area buy home",
        "Las Vegas housing rent apartment",
    ],
    "LasVegas": [
        "Henderson Summerlin real estate",
        "buying first home Las Vegas",
        "North Las Vegas homes buying",
        "Las Vegas condo townhome buying",
        "Summerlin Henderson buying home",
        "Las Vegas new construction home",
    ],
    "FirstTimeHomeBuyer": [
        "Las Vegas Nevada home",
        "Nevada closing costs first time",
        "Las Vegas down payment house",
        "Nevada FHA VA loan home",
        "first home Las Vegas budget",
        "Las Vegas buyer tips home",
    ],
    "RealEstate": [
        "Las Vegas Nevada market",
        "Henderson Nevada investment property",
        "Nevada rental investment Las Vegas",
        "Las Vegas real estate appreciation",
        "Vegas housing inventory market",
        "Las Vegas HOA reserve study",
    ],
}

# Keywords that indicate a post is relevant to real estate / housing / moving
# At least one must appear in the post title (case-insensitive) for general subs
# Avoid single generic words like "buy", "rent", "move" that match non-housing posts
RELEVANCE_KEYWORDS = [
    # Unambiguous housing terms
    "home", "house", "apartment", "condo", "townhome", "townhouse",
    "mortgage", "closing cost", "down payment", "real estate",
    "hoa", "property tax", "landlord", "tenant", "lease",
    "renting", "realtor", "housing",
    # Actions + housing context
    "buying a", "moving to", "moving from", "relocat",
    "cost of living",
    # Home systems / utilities
    "nv energy", "electric bill", "hvac", "solar panel",
    # Las Vegas neighborhoods (these are strong signals)
    "henderson", "summerlin", "north las vegas", "green valley",
    "centennial hills", "southwest las vegas", "spring valley",
    "lake las vegas", "southern highlands", "aliante",
    "mountains edge", "inspirada", "cadence", "skye canyon",
]

# Subs where we enforce title relevance filtering (general-purpose subs)
# For dedicated real-estate subs, every post is already on-topic
FILTER_SUBS = {"vegaslocals", "vegas", "LasVegas"}

# Agent notes per subreddit
AGENT_NOTES = {
    "vegaslocals":        "Can lightly mention being a realtor",
    "vegas":              "Can lightly mention being a realtor",
    "LasVegas":           "Can lightly mention being a realtor",
    "FirstTimeHomeBuyer": "Do NOT identify as agent in this sub",
    "RealEstate":         "Can lightly mention being a realtor",
}

# Distribution: how many slots per subreddit (total = 10)
SUB_SLOT_COUNTS = {
    "vegaslocals": 2,
    "vegas": 2,
    "LasVegas": 2,
    "FirstTimeHomeBuyer": 2,
    "RealEstate": 2,
}


def build_todays_slots() -> List[Dict]:
    """Build 10 search slots using date-based rotation so queries vary each day."""
    day_seed = int(datetime.now().strftime("%Y%m%d"))
    slots = []
    for sub, count in SUB_SLOT_COUNTS.items():
        pool = QUERY_POOLS[sub]
        rng = random.Random(day_seed + hash(sub))
        picked = rng.sample(pool, min(count, len(pool)))
        for query in picked:
            slots.append({
                "subreddit": sub,
                "query": query,
                "agent_note": AGENT_NOTES[sub],
            })
    return slots

HEADERS = {
    "User-Agent": "PostDiscovery/1.0 (personal use; contact via reddit u/Silver_Artichoke_812)"
}


def search_subreddit(subreddit: str, query: str, limit: int = 5, sort: str = "relevance") -> List[Dict]:
    """Search a subreddit via Reddit's public JSON API and return post metadata."""
    url = (
        f"https://www.reddit.com/r/{subreddit}/search.json"
        f"?q={requests.utils.quote(query)}"
        f"&restrict_sr=1&sort={sort}&t=year&limit={limit}"
    )
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        posts = data.get("data", {}).get("children", [])
        results = []
        for post in posts:
            p = post.get("data", {})
            # Skip archived, locked, or deleted posts
            if p.get("archived") or p.get("locked") or p.get("removed_by_category"):
                continue
            # Skip posts older than ~6 months (180 days)
            age_days = (time.time() - p.get("created_utc", 0)) / 86400
            if age_days > 180:
                continue
            results.append({
                "id": p.get("id", ""),
                "title": p.get("title", ""),
                "selftext": p.get("selftext", ""),
                "url": f"https://old.reddit.com{p.get('permalink', '')}",
                "num_comments": p.get("num_comments", 0),
                "score": p.get("score", 0),
                "age_days": round(age_days, 1),
                "is_self": p.get("is_self", True),
            })
        return results
    except Exception as e:
        print(f"  [!] Search failed for r/{subreddit} '{query}': {e}")
        return []


def get_post_body(subreddit: str, post_id: str) -> str:
    """Fetch full post body text via the post's JSON endpoint."""
    url = f"https://www.reddit.com/r/{subreddit}/comments/{post_id}.json?limit=1"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        if isinstance(data, list) and len(data) > 0:
            post_data = data[0].get("data", {}).get("children", [{}])[0].get("data", {})
            body = post_data.get("selftext", "")
            if body and body not in ("[deleted]", "[removed]"):
                # Truncate to ~600 chars for readability
                if len(body) > 600:
                    body = body[:597] + "..."
                return body.strip()
    except Exception as e:
        print(f"  [!] Could not fetch post body for {post_id}: {e}")
    return ""


def format_age(age_days: float) -> str:
    if age_days < 1:
        hours = round(age_days * 24)
        return f"{hours} hour{'s' if hours != 1 else ''} ago"
    elif age_days < 7:
        days = round(age_days)
        return f"{days} day{'s' if days != 1 else ''} ago"
    elif age_days < 30:
        weeks = round(age_days / 7)
        return f"{weeks} week{'s' if weeks != 1 else ''} ago"
    else:
        months = round(age_days / 30)
        return f"{months} month{'s' if months != 1 else ''} ago"


def write_discovery_file(slots: List[Dict], output_path: str, found_count: int):
    """Write the PostDiscovery markdown file."""
    now = datetime.now()
    date_str = now.strftime("%A, %B %d, %Y")

    lines = [
        f"# Post Discovery — {date_str}",
        "",
        f"**Generated:** {date_str}",
        f"**Posts found:** {found_count} of {len(slots)}",
        f"**Method:** Reddit public JSON API",
        "",
        "---",
        "",
        "## INSTRUCTIONS FOR CLAUDE",
        "",
        "For each slot below that has a real post:",
        "- Read the post title and body carefully",
        "- Write a comment that responds SPECIFICALLY to what the OP asked or their situation",
        "- Reference their details: their budget, their question, their specific concern",
        "- Open the comment by addressing their situation, not with a generic intro",
        "- Still follow all writing rules (no em-dashes in text, data-rich, Vegas-specific, knowledgeable neighbor voice)",
        "- Use the Post URL — the poster script will go directly to that thread",
        "",
        "For slots marked 'No post found', SKIP that slot entirely. Do NOT write a generic comment.",
        "",
        "---",
        "",
    ]

    for i, slot in enumerate(slots, 1):
        sub = slot["subreddit"]
        agent_note = slot.get("agent_note", "")
        post = slot.get("post")

        lines.append(f"## Slot {i} — r/{sub}")
        lines.append(f"**Agent note:** {agent_note}")
        lines.append(f"**Fallback search query:** {slot['query']}")
        lines.append("")

        if post:
            lines.append(f"**Post URL:** {post['url']}")
            lines.append(f"**Title:** {post['title']}")
            lines.append(f"**Age:** {format_age(post['age_days'])}")
            lines.append(f"**Comments:** {post['num_comments']}")
            lines.append("")
            if post.get("body"):
                lines.append("**What the OP said:**")
                lines.append("")
                lines.append(post["body"])
            else:
                lines.append("**What the OP said:** *(link post or no body — respond to the title alone)*")
        else:
            lines.append("**Post URL:** (none — no suitable post found, use search query fallback)")
            lines.append("**Title:** (N/A)")
            lines.append("")
            lines.append("**What the OP said:** *(no post found — write a generic topical comment)*")

        lines += [
            "",
            "---",
            "",
            f"### Comment {i} — r/{sub}",
            "",
            "*(Claude writes tailored comment here)*",
            "",
            "---",
            "",
        ]

    with open(output_path, "w") as f:
        f.write("\n".join(lines))


def main():
    now = datetime.now()
    month_abbr = now.strftime("%b")
    day = now.strftime("%d")
    year = now.strftime("%Y")
    output_filename = f"PostDiscovery_{month_abbr}{day}_{year}.md"
    output_path = os.path.join(SCRIPT_DIR, output_filename)

    search_slots = build_todays_slots()

    print("=" * 60)
    print("  REDDIT POST DISCOVERY (API)")
    print(f"  Output: {output_filename}")
    print(f"  Slots:  {len(search_slots)}")
    print("=" * 60)
    print()

    populated_slots = []
    found_count = 0
    seen_post_ids = set()  # Dedup: don't assign the same post to multiple slots

    for i, slot in enumerate(search_slots, 1):
        sub = slot["subreddit"]
        query = slot["query"]
        # Use relevance sort for general subs (better matches), new sort for real estate subs
        sort = "relevance" if sub in FILTER_SUBS else "new"
        print(f"[{i}/{len(search_slots)}] r/{sub} — \"{query}\" (sort={sort})")

        posts = search_subreddit(sub, query, limit=RESULTS_PER_QUERY * 5, sort=sort)
        best_post = None

        for p in posts:
            # Skip posts already assigned to another slot
            if p["id"] in seen_post_ids:
                continue
            # Skip posts that are too old
            if p["age_days"] > 90:
                continue
            # For general subs, check TITLE relevance to real estate / housing / moving
            # Only checking title prevents false matches from body text mentioning
            # keywords casually (e.g., "going home" in a nightlife post)
            if sub in FILTER_SUBS:
                title_lower = p["title"].lower()
                if not any(kw in title_lower for kw in RELEVANCE_KEYWORDS):
                    continue
            best_post = p
            break

        if best_post:
            seen_post_ids.add(best_post["id"])
            # Fetch full body text
            time.sleep(RATE_LIMIT_DELAY)
            body = get_post_body(sub, best_post["id"])
            best_post["body"] = body
            populated_slots.append({**slot, "post": best_post})
            found_count += 1
            print(f"  [OK] Found: \"{best_post['title'][:60]}\" ({format_age(best_post['age_days'])})")
        else:
            populated_slots.append({**slot, "post": None})
            print(f"  [--] No suitable post found — will use search query fallback")

        time.sleep(RATE_LIMIT_DELAY)

    print()
    write_discovery_file(populated_slots, output_path, found_count)
    print(f"\n  Saved: {output_filename}")
    print(f"  {found_count}/{len(search_slots)} slots have real post content")
    print()

    if found_count == 0:
        print("  [!] No posts found. Check network connectivity to reddit.com")
        sys.exit(1)
    else:
        print("  Discovery complete. Claude will now write context-aware comments.")
        sys.exit(0)


if __name__ == "__main__":
    main()
