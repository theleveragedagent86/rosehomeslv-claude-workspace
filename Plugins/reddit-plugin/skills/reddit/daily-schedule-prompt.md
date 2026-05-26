# Reddit Daily Schedule — Paste into Cowork Scheduler

Use this as the prompt when setting up a scheduled task in Cowork.

**Important:** The prompt below runs `reddit_discover_api.py` as its first step to find real Reddit posts before writing any comments. This ensures every comment responds to an actual post, not a generic topic.

---

## Schedule Settings

- **Frequency:** Daily
- **Time:** 10:00 AM (weekdays)

---

## Prompt to Paste

```
Run the daily Reddit routine for r/VegasRealtor.

STEP 1 — DISCOVER REAL POSTS

Run this command in the terminal and wait for it to finish (~2-3 minutes):
python3 /Users/ryanrose/Downloads/Claude/Reddit/reddit_discover_api.py

This searches Reddit's API for 10 real posts across the target subreddits. It saves a PostDiscovery file with the actual post URLs, titles, and body text.

After the script finishes, read the output file:
/Users/ryanrose/Downloads/Claude/Reddit/PostDiscovery_[MonDD]_[YYYY].md
(Use today's date in the filename, e.g., PostDiscovery_Mar18_2026.md)

If the discovery script fails or finds zero posts, SKIP the off-sub comments section entirely. Do NOT write generic comments. Report the failure and move on to the r/VegasRealtor post only.

STEP 2 — DRAFT TODAY'S CONTENT

Read these files for context:
- /Users/ryanrose/Downloads/Claude/Reddit/CLAUDE.md
- /Users/ryanrose/Downloads/Claude/Reddit/VegasRealtor_Reddit_Strategy_Status.md
- /Users/ryanrose/Downloads/Claude/Reddit/VegasRealtor_Content_Calendar_30Day.md

Determine today's date. Look up today's r/VegasRealtor post topic from the content calendar. Check if a pre-written version exists in the Week files in that same folder. If not, write it fresh.

Check the status tracker for recent comment interactions that may need replies. If there are any, draft replies with the direct old.reddit.com URL to the comment being replied to.

Now read the PostDiscovery file from Step 1. For each slot that has a real post:
- Read the post title and body text CAREFULLY
- Write a comment that DIRECTLY RESPONDS to what that specific OP asked
- Your opening sentence must reference something specific from their post (their budget, their city, their question, their concern)
- Then layer in helpful data and Vegas-specific details

ABSOLUTE RULES FOR OFF-SUB COMMENTS:
- Every comment MUST reference something specific from the OP's post title or body
- If the OP mentioned a budget, reference that budget
- If the OP asked about a specific neighborhood, talk about that neighborhood
- If the OP is moving from a specific state, acknowledge where they're coming from
- A comment that could apply to ANY post is a BAD comment. Every comment must feel like it was written for that one person.
- For slots where discovery found no post, SKIP that slot. Do not write a generic comment.

Generate a DailyDrafts file at:
/Users/ryanrose/Downloads/Claude/Reddit/DailyDrafts_[MonDD]_[YYYY].md

The file MUST follow this EXACT format (the Python auto-poster parses it):

---

# Daily Drafts — [Full Date]

**Reddit Account:** u/Silver_Artichoke_812
**Date:** [Full Date]
**Status:** Ready for auto-posting

---

## NOTIFICATION REPLIES

(If there are replies to draft, use this format for each. If none, write "No pending replies." and move on.)

---

### Reply 1
**Reply to:** https://old.reddit.com/r/[subreddit]/comments/[id]/[slug]/[comment_id]/
**Context:** [Brief description of what the person said]

---

[Reply text here. For follow-up questions, write 100-200 words. For short thank-yous, keep it brief and warm. Same writing rules apply.]

---

## r/VegasRealtor POST — [Date] ([Category])

**Title:** [exact title from calendar]

**Flair:** [Market Data | Neighborhood Guide | Buyer Tips | Seller Tips | Educational]

**Body:**

[Full post body, 300-600 words. Lead with the most interesting data point. Short paragraphs. End with an open question to encourage comments.]

---

## OFF-SUB COMMENTS — Drafts for [Date]

(Only include comments for slots where the PostDiscovery file had a real post with a URL. Skip slots that had no post found.)

---

### Comment 1 — r/vegaslocals
**Post URL:** [EXACT URL from the PostDiscovery file]
**Post title:** [the actual title of the post you are responding to]
**Search query:** [fallback search terms from the discovery file]
**NOTE: Can lightly mention being a realtor or r/VegasRealtor as an off-hand comment**

---

[Full comment text, 200-400 words. MUST open by addressing the OP's specific situation. Data-rich, Vegas-specific, knowledgeable neighbor voice.]

---

### Comment 2 — r/vegas
**Post URL:** [EXACT URL from PostDiscovery file]
**Post title:** [actual post title]
**Search query:** [fallback search terms]
**NOTE: Can lightly mention being a realtor or r/VegasRealtor as an off-hand comment**

---

[Comment text]

---

(Continue for all slots that had real posts. Spread across: r/vegaslocals, r/vegas, r/LasVegas, r/FirstTimeHomeBuyer, r/RealEstate)

CRITICAL FORMAT RULES:
- Comment headers MUST use the em-dash character: ### Comment N — r/subreddit (not a hyphen)
- Reply headers: ### Reply N
- **Reply to:** must contain a full old.reddit.com URL to the specific comment
- **Post URL:** MUST be the exact URL from the PostDiscovery file (the Python script navigates directly there)
- **Post title:** the real title of the post so you can verify your comment is on-topic
- **Search query:** fallback if the Post URL fails
- All content text goes between --- delimiters
- Do not engage with comments/replies that are political, refer to LGBTQ communities, or have an argumentative tone

Writing rules for ALL content (NON-NEGOTIABLE):
- No em-dashes ever (not in the content text, only in the ### headers)
- 6th grade reading level
- Data-rich with specific numbers
- Vegas-specific with neighborhood names
- Knowledgeable neighbor voice, not salesy
- No links in comment or reply text
- Do NOT identify as agent in r/FirstTimeHomeBuyer
- Start lightly mentioning that you are a realtor, in a non-braggy way, more humble and as an off-hand comment

Key data points to reference: median home price ~$470k, active listings grew from ~3k to 6k+, property tax ~0.53%, no state income tax, summer electric $200-400/mo, HOA $100-200/mo houses / $350-500/mo condos, SID/LID taxes in newer communities $200-400/mo, HVAC lifespan 8-10 years in Vegas.

STEP 3 — RUN THE AUTO-POSTER

After the DailyDrafts file is saved, run this command in the terminal:

nohup python3 /Users/ryanrose/Downloads/Claude/Reddit/reddit_daily.py --non-interactive > /tmp/reddit_daily_$(date +%Y%m%d).log 2>&1 &

This runs the Playwright auto-poster in the background. It will:
- Log in to Reddit via Google OAuth (credentials from macOS Keychain)
- Post notification replies (if any)
- Post the r/VegasRealtor content
- Post all off-sub comments using the Post URLs directly (search query as fallback only)
- Upvote each post after commenting
- Print structured results at the end

Wait approximately 18 minutes, then read the log file:
cat /tmp/reddit_daily_$(date +%Y%m%d).log

Look for the === RESULTS === section at the end of the log.

STEP 4 — UPDATE STATUS

After reading the log results, update:
- /Users/ryanrose/Downloads/Claude/Reddit/VegasRealtor_Reddit_Strategy_Status.md — add today's session with what was posted, which subs, any failures
- /Users/ryanrose/Downloads/Claude/Reddit/VegasRealtor_Content_Calendar_30Day.md — mark today's post as published in the status table

STEP 5 — REPORT

Report a summary of everything done:
- How many posts the discovery script found
- How many notification replies were sent
- r/VegasRealtor post title and status
- How many off-sub comments posted vs failed
- Which subreddits were covered
- Any issues or failures from the log
- If the script failed to run, output the command for manual execution:
  python3 /Users/ryanrose/Downloads/Claude/Reddit/reddit_daily.py
```
