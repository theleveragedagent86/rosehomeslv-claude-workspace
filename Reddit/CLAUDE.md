# Reddit Strategy for r/VegasRealtor - Instructions for Claude

**IMPORTANT: Read this entire file before doing anything. This is your playbook.**

---

## Who You Are Working For

- **Name:** Ryan Rose
- **Business:** Rose Homes LV (Las Vegas real estate)
- **Reddit Account:** u/Silver_Artichoke_812 (display name: "Ryan Rose with Rose Homes LV")
- **Subreddit:** r/VegasRealtor (owned/moderated by Ryan)

## What We Are Doing

Building credibility and community for r/VegasRealtor through a multi-phase Reddit growth strategy. The full strategy document is in this same folder: `Building VegasRealtor_ A Data-Driven Reddit Community Strategy for Las Vegas Real Estate.pdf`. There is also a YouTube cross-posting playbook: `YouTube Videos on Reddit_ A Playbook for r_VegasRealtor.pdf`.

The current phase (Phase 3) involves posting helpful, data-rich comments on real estate related posts across target subreddits to build Silver_Artichoke_812's reputation as a knowledgeable voice. We do NOT promote r/VegasRealtor in these comments. The credibility comes first.

---

## Target Subreddits

- **r/vegaslocals** - Vegas residents, local topics
- **r/vegas** - Mix of locals and visitors
- **r/LasVegas** - Similar to r/vegas, slightly different audience
- **r/FirstTimeHomeBuyer** - National sub, Vegas-specific posts only. **CRITICAL: Do NOT identify as a real estate agent here. Sub rules ban industry professional posts.**
- **r/RealEstate** - National sub, Vegas/Nevada posts only. Can identify as agent here.

## Writing Rules (NON-NEGOTIABLE)

Every single comment MUST follow these rules:

1. **NO EM-DASHES EVER.** Not one. Use commas, periods, or the word "and" instead. This is the #1 rule.
2. **6th grade reading level.** Simple words. Short sentences. No jargon unless you explain it.
3. **Medium length.** Not one-liners, not walls of text. Aim for 150-300 words typically.
4. **No links.** Never. Not even to helpful resources.
5. **No self-promotion.** Never mention r/VegasRealtor, Rose Homes LV, or any business.
6. **Data-rich.** Include specific numbers: prices, percentages, dollar amounts, timeframes.
7. **Vegas-specific.** Use neighborhood names, local details, specific streets/areas.
8. **"Knowledgeable neighbor" voice.** You're the friend who happens to know a ton about real estate. Casual, warm, helpful. Not salesy, not formal.
9. **Do NOT identify as an agent in r/FirstTimeHomeBuyer.** In other subs it's fine.
10. **Broad scope:** Answer anything that impacts buying/selling -- schools, utilities, neighborhoods, HOAs, insurance, cost of living, etc.

## How to Find Posts to Comment On

Use varied search terms. Don't repeat the same ones:
- "moving to Las Vegas", "buying house Vegas", "Henderson", "Summerlin"
- "Nevada taxes", "Las Vegas HOA", "rent or buy Vegas"
- "property tax Nevada", "first time buyer Las Vegas"
- "cost of living Vegas", "Vegas neighborhood", "Henderson vs Summerlin"
- "Las Vegas market", "Vegas real estate", "NV Energy", "Vegas solar"
- "closing costs Nevada", "Vegas condo", "Vegas townhome"

Use Reddit search with `subreddit:SubName keyword` format for scoped searches.

**Good posts to comment on:**
- Questions from people moving to Vegas
- Rent vs buy discussions
- Neighborhood comparison questions
- Market condition discussions
- New homeowner celebration posts (add helpful tips)
- HOA/property tax/utility questions
- School district questions
- Any post where Vegas-specific knowledge adds real value

**Skip these:**
- Posts where the comments section already has thorough, accurate answers
- Posts that are just jokes or political tangents with no real question
- Posts older than 6 months (archived, can't comment)
- Posts not related to real estate or topics that impact buying/selling

## Key Data Points to Reference in Comments

Keep these handy for writing data-rich comments:

- **Median home price (Vegas):** ~$470k
- **Active listings:** grew from ~3,000 to over 6,000 in the past year
- **Property tax rate:** ~0.53% (one of the lowest in the country)
- **Property tax cap:** 3% max increase/year for primary residence
- **No state income tax** in Nevada
- **Summer electric bills:** $200-400/month for older homes
- **HOA fees:** $100-200/month typical for houses, $350-500/month for condos
- **NV Energy budget billing** available to flatten monthly payments
- **SID/LID taxes** in newer communities: $200-400/month additional
- **HVAC lifespan in Vegas:** 8-10 years (vs 15-20 in milder climates)
- **NRS 116:** Nevada HOA law governing reserve studies, resale packages
- **Homestead exemption:** Available for primary residence
- **Rent ranges:** 1BR $1,200-1,800 depending on area; 2BR $1,500-2,400
- **Mortgage estimate:** ~$2,500-2,800/month for median priced home with taxes/insurance

## Replying to Responses on Your Comments

When people reply to Silver_Artichoke_812's comments:
- Always reply back. Engagement builds the account's reputation.
- Keep the same friendly, knowledgeable tone.
- If they ask follow-up questions, give detailed answers.
- If they just say thanks, keep it short and warm. Invite more questions.
- Check notifications regularly (every session).

---

## Automated Posting Workflow (Updated March 2026)

Reddit blocks Cowork's Chrome browser automation. All posting is now handled by a standalone Python script using Playwright.

### How It Works

1. **Cowork generates** the `DailyDrafts_[MonDD]_[YYYY].md` file with all content (replies, r/VegasRealtor post, 10 off-sub comments)
2. **Cowork runs** the script in background via bash:
   ```bash
   nohup python3 /Users/ryanrose/Downloads/Claude/Reddit/reddit_daily.py --non-interactive > /tmp/reddit_daily_$(date +%Y%m%d).log 2>&1 &
   ```
3. **The script handles**: Login via Google OAuth (macOS Keychain), posting notification replies, posting r/VegasRealtor content, posting 10 off-sub comments with 90s delays, upvoting posts
4. **Cowork reads** the log file (~18 min later) and updates status files

### Script: `reddit_daily.py`

**Location:** `/Users/ryanrose/Downloads/Claude/Reddit/reddit_daily.py`

**Flags:**
- `--non-interactive` — No input() pauses, required when Cowork runs it
- `--skip-vegasrealtor` — Skip the r/VegasRealtor post
- `--delay N` — Seconds between comments (default 90)

**Credentials:** Stored in macOS Keychain:
- `reddit-google-email` — Google email for Reddit login
- `reddit-google-password` — Google password

**Structured output:** The script prints a `=== RESULTS ===` block at the end that Cowork can parse for reporting.

### DailyDrafts File Format

The Python parser depends on exact formatting. See SKILL.md for the complete format specification. Key rules:
- Comment headers use em-dash: `### Comment N — r/subreddit`
- Reply headers: `### Reply N` with `**Reply to:**` URL
- Text blocks between `---` delimiters

### Legacy Notes (Deprecated)

The Chrome-based browser automation via Cowork MCP tools (navigate, javascript_tool, find, etc.) no longer works for Reddit. All those approaches are replaced by the Playwright script above. Old Reddit (old.reddit.com) is still used by the script for posting as it is more reliable than new Reddit.

---

## Current Progress

**See the full status tracker:** `VegasRealtor_Reddit_Strategy_Status.md` (in this same folder)

**Quick summary as of Feb 15, 2026:**
- 18 comments posted across all target subreddits
- 3 replies to people who responded to our comments
- Phase 3 active round complete (10/10 comments)
- Next: monitor replies, consider another round, or move to next phase items

---

## 30-Day Content Calendar

A daily content calendar for r/VegasRealtor has been created covering Feb 16 - Mar 17, 2026. See: `VegasRealtor_Content_Calendar_30Day.md`

- 30 posts, one per day
- Rotating mix: Market Data, Neighborhood Guides, Buyer Tips, Seller Tips, Educational
- Recurring series: Weekly Stat Drop (Sundays), Neighborhood Breakdown (Tue/Fri)
- Same writing rules apply to these posts as to comments (no em-dashes, data-rich, etc.)
- Posts should be 300-600 words, end with a question to encourage engagement

## File Locations

- **This file:** `/Reddit/CLAUDE.md`
- **Status tracker:** `/Reddit/VegasRealtor_Reddit_Strategy_Status.md`
- **Content calendar:** `/Reddit/VegasRealtor_Content_Calendar_30Day.md`
- **Strategy PDF:** `/Reddit/Building VegasRealtor_ A Data-Driven Reddit Community Strategy for Las Vegas Real Estate.pdf`
- **YouTube playbook:** `/Reddit/YouTube Videos on Reddit_ A Playbook for r_VegasRealtor.pdf`
