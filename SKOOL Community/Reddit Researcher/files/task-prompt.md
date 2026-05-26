# Reddit Real Estate AI Demand Research — Multi-Agent Task

## Your Role: Manager Agent

You are the Manager Agent orchestrating a multi-agent research pipeline. Your end goal is to produce a demand-ranked intelligence report that tells you exactly which real estate AI pain points have the most people asking about them — so the user can prioritize which Skool community modules to build first and which YouTube videos will get the most traction.

You coordinate multiple dedicated Research Agents (one per subreddit), a QA Agent, and a Topic Synthesizer.

## Setup

Before starting, create the output directories:
```bash
mkdir -p ./output/by-subreddit
```

Read the reference files:
- `references/subreddits.md` — your target subreddits ranked by priority
- `references/keywords.md` — your search keyword matrix with combination strategy

---

## Pipeline Execution

### Phase 1: Spawn Dedicated Research Agents (One Per Subreddit)

Each subreddit gets its own Research Agent. This is intentional — each sub has different culture, terminology, and posting patterns. A dedicated agent can tune its approach per community.

**Spawn order — start all Primary subreddit agents first, then Secondary as needed:**

#### Primary Subreddit Agents (spawn all of these)
1. **Research Agent: r/realtors** — The biggest community. Expect the highest volume.
2. **Research Agent: r/RealEstateTechnology** — Most focused on proptech/AI. Expect highest relevance per post.
3. **Research Agent: r/RealEstateAgents** — Working agents. Strong workflow pain point signal.
4. **Research Agent: r/realestate** — General sub, noisier, but large user base surfaces good threads.
5. **Research Agent: r/CommercialRealEstate** — CRE has distinct needs. Separate signal.

#### Secondary Subreddit Agents (spawn if Primary yields < 60 qualified posts)
6. **Research Agent: r/PropertyManagement**
7. **Research Agent: r/RealEstateSales**
8. **Research Agent: r/Flipping**

#### Tertiary (spawn only for gap-filling specific categories)
9. **Research Agent: r/ChatGPT** (filtered to real estate context)
10. **Research Agent: r/smallbusiness** (filtered to real estate context)

**For EACH subreddit Research Agent, use this prompt template:**

```
You are Research Agent: r/{{SUBREDDIT_NAME}}.

Your sole focus is the r/{{SUBREDDIT_NAME}} subreddit. Search it exhaustively
for posts where real estate professionals are asking about AI tools,
automation, or technology solutions for specific workflow tasks.

SEARCH STRATEGY:
Run through the keyword matrix from references/keywords.md systematically.
For each search:
1. Use web_search: site:reddit.com r/{{SUBREDDIT_NAME}} {{KEYWORD_COMBO}}
2. Open the top 3-5 most promising results with web_fetch to read full threads
3. Also scan the comments — sometimes the real demand signal is in a reply,
   not the original post. If a commenter says "I wish there was an AI for X",
   that counts as a demand signal. Capture it.

KEYWORD SWEEP — run these combinations (adapt phrasing to this sub's style):
- Tier 1 intent signals x each task domain (MLS, content, leads, follow-up,
  transactions, CRM, market analysis, client comms, marketing)
- If Tier 1 produces fewer than 10 posts, expand to Tier 2 intent signals
- If still under 10, use Tier 3

SUBREDDIT-SPECIFIC NOTES FOR r/{{SUBREDDIT_NAME}}:
{{MANAGER: Insert 1-2 sentences about this sub's culture. Examples:
  - r/realtors: "Active, professional. Posts often start with 'What's your
    tech stack?' or 'How are you using AI?' Look for weekly thread roundups."
  - r/RealEstateTechnology: "Very focused. Almost every post is about tools.
    Filter hard for AI-specific vs general SaaS discussion."
  - r/realestate: "Mixed audience (agents + consumers). Filter carefully to
    only capture posts from industry professionals, not homebuyers."
  - r/CommercialRealEstate: "Different workflows — deal analysis, tenant
    management, lease abstraction. Different pain points than residential."
}}

FOR EACH RELEVANT POST OR COMMENT, extract:
{
  "post_id": "unique URL slug",
  "subreddit": "r/{{SUBREDDIT_NAME}}",
  "title": "post title",
  "url": "full Reddit URL",
  "date_posted": "approximate date (month/year)",
  "source_type": "original_post" or "comment",
  "post_body_summary": "2-3 sentence summary of what they're asking for",
  "specific_task": "the EXACT workflow they want AI help with — be precise",
  "task_normalized": "map to one of: mls_listing, content_creation,
    lead_generation, lead_followup, transaction_mgmt, crm_database,
    market_analysis, client_comms, marketing_ads, other",
  "tools_mentioned": ["any specific tools, platforms, or AI products named"],
  "pain_point": "the core frustration or unmet need in their own words",
  "engagement": {
    "upvotes_approx": number,
    "comments_approx": number,
    "sentiment": "positive/negative/mixed/curious"
  },
  "notable_replies": ["1-2 sentence summaries of top replies with any tool recs"],
  "me_too_count": number of commenters who say something like "same",
    "I need this too", "following", "+1", or express the same need
}

THE "me_too_count" FIELD IS CRITICAL. This captures demand volume beyond just
the original poster. A post with 3 upvotes but 12 comments saying "I need
this too" is a stronger signal than a post with 50 upvotes and 2 comments.
Count every commenter who expresses the same need or desire.

QUALITY FILTERS — Only include posts/comments that:
- Come from a real estate professional (agent, broker, team lead, TC, admin)
- Ask about or discuss AI/automation for a SPECIFIC workflow task
- Are NOT pure vendor advertisements or product launches
- Have some engagement (>2 comments or >3 upvotes, but include any post
  where the specific_task is very clear even if low engagement)

Skip:
- "Will AI replace agents" opinion debates
- Vendor AMAs or product launch announcements
- Meme/joke posts
- Posts older than 18 months

Save results to: ./output/by-subreddit/{{SUBREDDIT_NAME}}.json
Return the JSON array and a summary line: "r/{{SUBREDDIT_NAME}}: Found X
qualifying posts across Y task categories."
```

**After ALL Research Agents complete:**
- Merge all per-subreddit JSON files into `./output/raw-posts.json`
- Deduplicate by URL (same post can appear in cross-posted threads)
- Log per-subreddit counts to `./output/run-log.md`
- Count total raw posts. If under 50, spawn Secondary subreddit agents.

---

### Phase 2: QA Agent Validation

Once you have 50+ raw posts (or have exhausted search budget), spawn the QA Agent.

**Spawn a QA Agent subagent with this prompt:**

```
You are the QA Agent. Review every post in ./output/raw-posts.json and
validate each one for quality, relevance, and accuracy.

FOR EACH POST, evaluate and ADD these fields:

1. qa_score (integer 1-5):
   5 = Explicitly asks "is there an AI that can [specific task]?" — clear,
       specific, actionable demand signal
   4 = Discusses AI/automation needs for a defined real estate workflow
   3 = Mentions wanting to automate or streamline something, AI-adjacent
   2 = Tangentially related, more about general tools than AI
   1 = Off-topic, misclassified, spam, or vendor post

2. authentic (boolean):
   true = Genuine question or pain point from a practitioner
   false = Vendor post, bot, or promotional content

3. is_vendor_post (boolean):
   true = Post language or account behavior suggests marketing
   false = Appears to be a genuine practitioner

4. duplicate_of (string or null):
   If this post is essentially the same ask as another, note the post_id.
   Keep the one with higher engagement + me_too_count.

5. engagement_quality ("high" / "medium" / "low"):
   high = Replies contain specific tool recs, detailed experiences, or debates
   medium = Mix of useful replies and generic responses
   low = Mostly "me too" / "following" with no substance beyond the signal

6. verified_me_too_count (integer):
   Re-check the Research Agent's me_too_count. If you can verify it, confirm.
   If it seems inflated or undercounted, correct it. This number matters
   for demand volume scoring downstream.

7. qa_notes (string):
   1-2 sentence rationale for your score

8. task_normalized_verified (string):
   Confirm or correct the Research Agent's task_normalized categorization.
   Use ONLY these values: mls_listing, content_creation, lead_generation,
   lead_followup, transaction_mgmt, crm_database, market_analysis,
   client_comms, marketing_ads, other

PASS THRESHOLD: qa_score >= 3 AND authentic == true

OUTPUT:
- Save full scored array to ./output/scored-posts.json
- Print summary:
  * Total reviewed: X
  * Passed: X (Y%)
  * Failed: X
  * Score distribution: 5=X, 4=X, 3=X, 2=X, 1=X
  * Category distribution of passing posts (count per task_normalized)
  * Total verified_me_too_count across all passing posts
```

**After QA completes:**
- If pass rate < 50%, refine search keywords and run another Research Agent pass
- If fewer than 30 posts passed, spawn Secondary/Tertiary Research Agents
- If any task_normalized category has 0 qualifying posts, flag it for targeted search
- Log QA summary to `./output/run-log.md`

---

### Phase 3: Topic Synthesizer — Demand Volume & Content Prioritization

This is the core deliverable. The Topic Synthesizer doesn't just categorize — it COUNTS and RANKS so the user knows exactly where to invest time building Skool content and YouTube videos.

**Spawn a Topic Synthesizer subagent with this prompt:**

```
You are the Topic Synthesizer Agent. Your job is to turn validated Reddit
posts into a demand-ranked content strategy for a Skool community and
YouTube channel focused on AI tools for real estate agents.

INPUT: Read ./output/scored-posts.json
Filter to: qa_score >= 3 AND authentic == true

===============================================================
STEP 1: DEMAND VOLUME COUNTING
===============================================================

This is the most important step. For each task_normalized_verified category,
calculate a DEMAND SCORE using this formula:

  demand_score = (post_count x 2) + total_me_too_count + (avg_comments x 0.5)

Where:
- post_count = number of unique qualifying posts in that category
- total_me_too_count = sum of all verified_me_too_count across posts
- avg_comments = average comments_approx across posts in that category

This gives you a single number that represents: "How many real people are
actively asking about this specific thing?"

Also calculate for each category:
- unique_posters: number of distinct posts (people who cared enough to write)
- total_engaged: post_count + total_me_too_count (total humans in the thread
  who expressed this need)
- frustration_index: count of posts with sentiment "negative" or "mixed"
  divided by total posts in category (0.0 to 1.0)
- solution_gap: count of posts where notable_replies contain NO tool
  recommendation divided by total posts (higher = bigger opportunity)
- avg_qa_score: average quality score (higher = clearer demand signal)

===============================================================
STEP 2: RANK AND PRIORITIZE FOR CONTENT CREATION
===============================================================

Using the demand_score and supporting metrics, produce TWO ranked lists:

LIST A: "BUILD THIS FIRST" — Skool Module Priority
Rank categories by: demand_score x solution_gap
(Highest demand + least existing solutions = build first)

For each category in priority order, suggest:
- Skool module name (catchy, benefit-driven)
- 3-5 specific lessons/tutorials that would answer the top asks
- Which Reddit posts to reference as "proof of demand" in marketing
- Estimated audience size based on total_engaged count

LIST B: "FILM THIS FIRST" — YouTube Video Priority
Rank categories by: demand_score x frustration_index
(Highest demand + most frustrated people = most clickable videos)

For each category in priority order, suggest:
- 3-5 YouTube video titles (use patterns like "How I Automated [X] as a
  Real Estate Agent" or "The AI Tool That [Solved Pain Point]")
- Which specific Reddit questions each video would answer
- Hook angle based on the most emotionally charged posts
- Estimated search demand signal (high/medium/low based on post frequency)

===============================================================
STEP 3: CROSS-SUBREDDIT ANALYSIS
===============================================================

Since we searched multiple subreddits, analyze WHERE the demand shows up:

For each subreddit that contributed posts:
- Post count contributed
- Top 2 categories by volume from that sub
- Any unique pain points that ONLY appeared in this sub
- Sub-specific language/framing to use in marketing to that audience

Identify:
- Which pain points appear across ALL subreddits (universal demand)
- Which are subreddit-specific (niche opportunity)
- Cross-posting patterns (same question posted to multiple subs = high demand)

===============================================================
STEP 4: DETAILED CATEGORY BREAKDOWN
===============================================================

For each of the 10 categories (ordered by demand_score, highest first):

### [Category Name]
Demand Score: [X] | Posts: [X] | Total Engaged: [X] | Frustration: [X%]

What agents are asking for:
- The #1 most common specific ask, with exact count of how many posts/
  comments mention it
- The #2 most common ask
- The #3 most common ask

Representative post summaries (paraphrased):
- 2-3 representative post summaries that capture the demand

Tools people are already trying:
| Tool | Times Mentioned | Sentiment | Common Complaint |
(table of every tool mentioned in this category)

What's NOT being solved:
- Specific asks where commenters had no solution to offer
- Tasks where every tool mentioned got complaints

Top Posts by Engagement:
| Title | Sub | Upvotes | Comments | Me Too | Link |
(top 5 posts in this category)

===============================================================
STEP 5: WRITE THE FINAL REPORT
===============================================================

Assemble the full report as markdown:

# Real Estate AI Demand Report — Reddit Research
## Generated: [today's date]
## Total Posts Analyzed: [X] | Total Humans Expressing Need: [X]

### Executive Summary
7-10 sentences. Lead with: "Across [X] subreddits, [Y] real estate
professionals are actively searching for AI solutions. The #1 demand
category is [X] with [Y] people asking. The biggest unmet need is [Z]."
Frame everything through the lens of "what should we build/teach first?"

### Demand Leaderboard
| Rank | Category | Demand Score | Posts | Total Engaged | Frustration | Solution Gap |
(all 10 categories ranked by demand_score)

### Skool Community Blueprint (LIST A)
Full "BUILD THIS FIRST" list with module names, lesson ideas, proof posts

### YouTube Content Calendar (LIST B)
Full "FILM THIS FIRST" list with video titles, hooks, source posts

### Cross-Subreddit Heat Map
Which subs have which demand, what's universal vs niche

### Category Deep Dives
Full breakdown for each category (from Step 4)

### Top 25 Highest-Signal Posts
| # | Title | Sub | Category | QA Score | Engagement | Me Too | Link |
(table sorted by demand signal strength)

### Appendix A: All Categorized Posts
Full table of every qualifying post

### Appendix B: All Tools Mentioned
| Tool | Category | Times Mentioned | Avg Sentiment |
(complete tool inventory)

### Appendix C: Methodology
Brief explanation of scoring formula and research process

Save to ./output/reddit-ai-demand-report.md
```

---

### Phase 4: Manager Review & Gap Fill

After the Topic Synthesizer delivers:

1. **Check the demand leaderboard.** Does the ranking make intuitive sense? Are the numbers defensible?
2. **Check category coverage.** Any category with fewer than 3 posts gets flagged. Spawn a targeted Research Agent for that specific category using Tier 2/3 keywords.
3. **Check the Skool blueprint.** Are the module names specific enough? Do the lesson ideas directly answer real Reddit questions?
4. **Check the YouTube list.** Are the video titles something you'd actually click? Do they reference real pain points?
5. **Verify the demand scores.** Spot-check 3-5 posts to make sure me_too_counts look accurate.
6. **Verify all links** are present and properly formatted.
7. **Compile final output:**
   - `./output/reddit-ai-demand-report.md` (main report)
   - `./output/raw-posts.json` (all raw results)
   - `./output/scored-posts.json` (QA-validated results)
   - `./output/by-subreddit/*.json` (per-subreddit raw data)
   - `./output/run-log.md` (execution log)
8. **Write final run-log entry:**
   - Total queries executed across all Research Agents
   - Per-subreddit post counts
   - Total raw to QA pass rate
   - Demand leaderboard summary (top 3 categories)
   - Gaps identified
   - Timestamp

---

## Important Notes

- **Parallel execution:** Spawn all Primary Research Agents simultaneously when possible. They're independent — each covers one subreddit.
- **Rate limiting:** Each Research Agent should pace its web_search calls (2-3 seconds between). Don't blast the same domain.
- **Context management:** Each Research Agent writes to its own file in `./output/by-subreddit/`. The Manager merges them. This keeps context windows clean.
- **me_too_count accuracy:** This is the most valuable metric in the entire pipeline. A post might have 5 upvotes but if 15 commenters say "same, I need this" — that's 15 potential Skool members. Count carefully.
- **Deduplication:** Cross-posted threads (same question in r/realtors and r/RealEstateAgents) should be merged, with engagement numbers combined and noted as "cross-posted" — this is actually a strong demand signal.
- **Failure handling:** If web_fetch fails on a Reddit URL, log it and move on. Don't retry more than once. Reddit rate-limits aggressively.
- **Privacy:** No Reddit usernames in the final report. The research is about demand signals, not individuals.
- **Skool framing:** The Topic Synthesizer should think like a community builder. Every category is a potential Skool module. Every high-engagement post is proof-of-demand for marketing copy.
