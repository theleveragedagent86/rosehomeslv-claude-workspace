---
name: local-news
description: Use when someone asks to research local news, create green-screen video scripts, generate weekly Las Vegas news content, build local news transcripts, run the weekly news roundup, create Clark County news videos for Instagram or YouTube, write local news blog posts, or create local news Reddit posts.
argument-hint: "optional: date override (YYYY-MM-DD)"
---

## What This Skill Does

Researches Clark County, NV local news across four categories (Government/Development, School Board, Hockey, Real Estate Market), ranks stories by viral potential, and produces a complete content package: green-screen video transcripts with CTAs, 2400-word blog articles with images and schema, Reddit posts for r/VegasRealtor (real estate stories only), Instagram captions, YouTube descriptions, and a compiled story spreadsheet.

The Real Estate Market category is fed by two research agents: a local Las Vegas market agent, and a national-to-local agent that finds national real estate headlines and reframes them against the actual Clark County numbers (national real estate news is not the same as local real estate news).

**Account:** @rosehomeslv
**Website:** rosehomeslv.com
**Expert:** Ryan Rose, Las Vegas Real Estate Expert

**Supporting files in this skill directory:**
- [research-gov-dev.md](research-gov-dev.md) — Government and Development Research Agent
- [research-school-board.md](research-school-board.md) — School Board and Education Research Agent
- [research-hockey.md](research-hockey.md) — Hockey Research Agent
- [research-real-estate.md](research-real-estate.md) — Real Estate Market Research Agent (local Las Vegas)
- [research-national-real-estate.md](research-national-real-estate.md) — National-to-Local Real Estate Research Agent
- [viral-strategist.md](viral-strategist.md) — Viral Scoring and Story Selection Agent
- [content-producer.md](content-producer.md) — Green-Screen Video Transcript Agent
- [social-media-writer.md](social-media-writer.md) — Instagram Caption and YouTube Description Agent
- [blog-strategist.md](blog-strategist.md) — Blog SEO and Slug Assignment Agent
- [blog-creator.md](blog-creator.md) — 2400-Word Blog Article Agent
- [reddit-post-writer.md](reddit-post-writer.md) — Reddit Post Agent (real estate stories only)
- [spreadsheet-assembler.md](spreadsheet-assembler.md) — Spreadsheet and Summary Agent
- [content-rules.md](content-rules.md) — Content rules for all output
- [source-registry.md](source-registry.md) — Research source URLs by category
- [transcript-templates.md](transcript-templates.md) — Templates for all output formats

---

## Architecture

You are the **Manager**. You orchestrate twelve sub-agents:

1. **Government/Development Research Agent** — Finds 10-15 gov/dev news stories
2. **School Board/Education Research Agent** — Finds 8-12 school board stories
3. **Hockey Research Agent** — Finds 8-12 hockey stories
4. **Real Estate Market Research Agent** — Finds 8-12 local Las Vegas residential market stories
5. **National-to-Local Real Estate Research Agent** — Finds 6-10 national real estate stories, each with a verified Clark County tie-in
6. **Viral Strategist Agent** — Scores all stories and selects the balanced set (minimum 21)
7. **Content Producer Agent** — Writes green-screen video transcripts with CTAs
8. **Social Media Writer Agent** — Writes Instagram captions and YouTube descriptions
9. **Blog Strategist Agent** — Creates SEO package with slugs, titles, meta, keywords
10. **Blog Creator Agent** — Writes 2400-word HTML blog articles with images and schema
11. **Reddit Post Writer Agent** — Creates Reddit posts for r/VegasRealtor (real estate stories only)
12. **Spreadsheet Assembler Agent** — Compiles spreadsheet and weekly summary

**You never write content yourself.** You orchestrate, validate, and assemble the final output.

---

## Workflow

### Step 0: Initialize

1. Parse `$ARGUMENTS` for an optional date override (YYYY-MM-DD format). If not provided, use today's date. Store as `TARGET_DATE`.

2. Set the output directory:
   ```
   /Users/ryanrose/Downloads/Claude/Rose Homes LV/Content/Instagram/Local News/[TARGET_DATE]/
   ```
   Create this directory and a `blogs/` subdirectory inside it.

3. **Check for previously covered stories (deduplication):**
   - List all subdirectories in `/Users/ryanrose/Downloads/Claude/Rose Homes LV/Content/Instagram/Local News/` that have a YYYY-MM-DD name and are NOT the current TARGET_DATE.
   - For each past directory that contains a `top-stories.md` file (or a legacy `top-30-stories.md` file from older runs), read it and extract every story headline (the lines starting with `### [N].` or `### Story [N]:`).
   - Compile all extracted headlines into a single deduplicated list.
   - Store as `PREVIOUSLY_COVERED_HEADLINES`. If no past runs exist, this list is empty.
   - Log how many past-run directories were scanned and how many total headlines were found.

4. Read ALL supporting files from this skill directory and store each as a variable:
   - `RESEARCH_GOV_DEV` ← contents of research-gov-dev.md
   - `RESEARCH_SCHOOL_BOARD` ← contents of research-school-board.md
   - `RESEARCH_HOCKEY` ← contents of research-hockey.md
   - `RESEARCH_REAL_ESTATE` ← contents of research-real-estate.md
   - `RESEARCH_NATIONAL_REAL_ESTATE` ← contents of research-national-real-estate.md
   - `VIRAL_STRATEGIST` ← contents of viral-strategist.md
   - `CONTENT_PRODUCER` ← contents of content-producer.md
   - `SOCIAL_MEDIA_WRITER` ← contents of social-media-writer.md
   - `BLOG_STRATEGIST` ← contents of blog-strategist.md
   - `BLOG_CREATOR` ← contents of blog-creator.md
   - `REDDIT_POST_WRITER` ← contents of reddit-post-writer.md
   - `SPREADSHEET_ASSEMBLER` ← contents of spreadsheet-assembler.md
   - `CONTENT_RULES` ← contents of content-rules.md
   - `SOURCE_REGISTRY` ← contents of source-registry.md
   - `TRANSCRIPT_TEMPLATES` ← contents of transcript-templates.md

---

### Step 1: Spawn 5 Research Agents (parallel)

Spawn **five agents in parallel** using the Agent tool (all `general-purpose` type) in a SINGLE response:

**Agent 1 — Government/Development Research Agent:**

```
You are a Government and Development Research Agent for the local-news system.

[FULL CONTENTS OF RESEARCH_GOV_DEV]

[FULL CONTENTS OF CONTENT_RULES]

[FULL CONTENTS OF SOURCE_REGISTRY — Government and Development section only]

Target week ending: [TARGET_DATE]
Geographic scope: Clark County, Nevada (Las Vegas, Henderson, North Las Vegas, Boulder City, Summerlin, Spring Valley, Centennial Hills, Skye Canyon, Green Valley, unincorporated Clark County)

Return your findings in the exact structured format specified in the instructions. Use WebSearch and WebFetch to research. Be thorough and verify all stories against official sources.
```

**Agent 2 — School Board/Education Research Agent:**

```
You are a School Board and Education Research Agent for the local-news system.

[FULL CONTENTS OF RESEARCH_SCHOOL_BOARD]

[FULL CONTENTS OF CONTENT_RULES]

[FULL CONTENTS OF SOURCE_REGISTRY — School Board and Education section only]

Target week ending: [TARGET_DATE]
Geographic scope: Clark County, Nevada

Return your findings in the exact structured format specified in the instructions. Use WebSearch and WebFetch to research. Be thorough and verify all stories against official sources.
```

**Agent 3 — Hockey Research Agent:**

```
You are a Hockey Research Agent for the local-news system.

[FULL CONTENTS OF RESEARCH_HOCKEY]

[FULL CONTENTS OF CONTENT_RULES]

[FULL CONTENTS OF SOURCE_REGISTRY — Hockey section only]

Target week ending: [TARGET_DATE]
Geographic scope: Clark County, Nevada (Las Vegas, Henderson, North Las Vegas, T-Mobile Arena, Henderson Pavilion, local ice rinks)

Return your findings in the exact structured format specified in the instructions. Use WebSearch and WebFetch to research. Be thorough and verify all stories against official sources. Prioritize playoff news, roster moves, and community-impacting rink/arena stories.
```

**Agent 4 — Real Estate Market Research Agent (local Las Vegas):**

```
You are a Real Estate Market Research Agent for the local-news system.

[FULL CONTENTS OF RESEARCH_REAL_ESTATE]

[FULL CONTENTS OF CONTENT_RULES]

[FULL CONTENTS OF SOURCE_REGISTRY — Real Estate Market section only]

Target week ending: [TARGET_DATE]
Geographic scope: Clark County, Nevada (Las Vegas, Henderson, North Las Vegas, Boulder City, Summerlin, Spring Valley, Centennial Hills, Skye Canyon, Green Valley, unincorporated Clark County)

Return your findings in the exact structured format specified in the instructions. Use WebSearch and WebFetch to research. Be thorough and verify all stories against official sources. Focus on residential real estate only — homes, condos, townhomes, land for housing, and the buyers and sellers who make up the market. Do not report on commercial, industrial, or retail properties.
```

**Agent 5 — National-to-Local Real Estate Research Agent:**

```
You are a National-to-Local Real Estate Research Agent for the local-news system.

[FULL CONTENTS OF RESEARCH_NATIONAL_REAL_ESTATE]

[FULL CONTENTS OF CONTENT_RULES]

[FULL CONTENTS OF SOURCE_REGISTRY — National Real Estate section only]

Target week ending: [TARGET_DATE]
National scope for the trigger story; Clark County, Nevada scope for the local tie-in number.

Return your findings in the exact structured format specified in the instructions. Use WebSearch and WebFetch to research. For EVERY national story, you must also find and verify the matching Clark County / Las Vegas number so the contrast can be reframed for a local audience. Do not keep a national story that has no findable local counterpart. Focus on residential real estate only.
```

**Wait for all 5 agents to complete.**

Store outputs as `GOV_DEV_DATA`, `SCHOOL_BOARD_DATA`, `HOCKEY_DATA`, `REAL_ESTATE_DATA`, `NATIONAL_RE_DATA`.

**Validation gate:**
- The four Clark County agents (Gov-Dev, School Board, Hockey, Real Estate) should each return at least 6 stories with source URLs (they target 8-12).
- The National-to-Local agent should return at least 4 stories (it targets 6-10), and EACH must include both a national figure and a verified local Clark County figure. Drop any national story missing its local tie-in.
- If an agent returns fewer than its floor, note it but proceed.
- If an agent returns 0 stories, retry once with the same prompt.
- Do NOT save separate research files. Store all raw research in memory only. A single combined research file is created after the viral strategist ranks the stories in Step 2.

---

### Step 2: Spawn Viral Strategist (sequential)

Spawn a single `general-purpose` agent:

```
You are the Viral Strategist for the local-news system.

[FULL CONTENTS OF VIRAL_STRATEGIST]

[FULL CONTENTS OF CONTENT_RULES]

GOVERNMENT AND DEVELOPMENT RESEARCH:
[GOV_DEV_DATA]

SCHOOL BOARD AND EDUCATION RESEARCH:
[SCHOOL_BOARD_DATA]

HOCKEY RESEARCH:
[HOCKEY_DATA]

REAL ESTATE MARKET RESEARCH (LOCAL LAS VEGAS):
[REAL_ESTATE_DATA]

REAL ESTATE MARKET RESEARCH (NATIONAL-TO-LOCAL):
[NATIONAL_RE_DATA]

Select a balanced set of AT LEAST 21 stories (21 is the weekly minimum — it feeds 3 posts a day). Target balance: 6 Government-Development / 4 School Board / 5 Hockey / 6 Real Estate Market. The Real Estate Market count blends local Las Vegas stories and national-to-local stories, roughly half and half. Score each story and rank them. Follow the selection criteria exactly.

NEVER cut a Red-tier or Extremely Important story just to hold the balance. If there are more than enough top stories, expand the total above 21 so nothing important is dropped.

PREVIOUSLY COVERED STORIES — DO NOT SELECT THESE AGAIN:
[PREVIOUSLY_COVERED_HEADLINES]

A story is "previously covered" if it describes the same news event — same incident, same announcement, same opening/closing, same vote, same entity and location. An ongoing topic (VGK playoffs, A's stadium construction, water restrictions) may be included ONLY if there is a genuinely NEW development this week that was not covered in any prior run. A minor update or recap with no new facts does not qualify. Apply this check after scoring but before finalizing your selections. If a story would be a duplicate, skip it and select the next-best story in that category.
```

Store output as `TOP_STORIES_DATA`.

**Validation gate:**
- At least 21 stories selected.
- Category balance approximately 6 Gov-Dev / 4 School Board / 5 Hockey / 6 Real Estate (+/- 1 per category), with the floors from the viral strategist honored (Gov-Dev ≥4, School Board ≥3, Hockey ≥3, Real Estate ≥4).
- No Red-tier or Extremely Important story was dropped to hold the balance.
- Every story has a viral score (Red/Orange/Yellow/Green) and an Extremely Important flag (Yes/No).
- If the count is below 21 or a category is below its floor, retry up to 2 times.
- Save to `top-stories.md` in the output directory.
- **Save combined research file:** After the viral strategist output is validated, save a single `research.md` to the output directory. This file contains the full research data for all selected stories (headline, category, story type, area, summary, source(s), URL(s), date, why it matters, national/local figures for national-to-local stories, flags) in the same viral-ranked order as `top-stories.md`. This is the ONLY research file saved to disk. Do not save separate per-category research files.

---

### Step 3: Spawn Content Producer + Social Media Writer (parallel)

Spawn **two agents in parallel** in a SINGLE response:

**Agent 1 — Content Producer:**

```
You are the Content Producer for the local-news system.

[FULL CONTENTS OF CONTENT_PRODUCER]

[FULL CONTENTS OF TRANSCRIPT_TEMPLATES — video transcript section only]

[FULL CONTENTS OF CONTENT_RULES]

SELECTED RANKED STORIES:
[TOP_STORIES_DATA]

Write green-screen video transcripts for every selected story. Assign lengths from the 15/30/45/60/75 second tiers based on viral score. There is no 90-second option. 75 seconds is reserved for stories flagged Extremely Important and must be used sparingly. Include CTAs as specified. For national-to-local real estate stories, lead with the national-vs-Vegas contrast. Save to [OUTPUT_DIR]/video-transcripts.md
```

**Agent 2 — Social Media Writer:**

```
You are the Social Media Writer for the local-news system.

[FULL CONTENTS OF SOCIAL_MEDIA_WRITER]

[FULL CONTENTS OF TRANSCRIPT_TEMPLATES — Instagram caption and YouTube description sections]

[FULL CONTENTS OF CONTENT_RULES]

SELECTED RANKED STORIES:
[TOP_STORIES_DATA]

Write Instagram captions, YouTube Shorts descriptions, and YouTube tags for every selected story. For national-to-local real estate stories, lead with the national-vs-Vegas contrast. Save captions to [OUTPUT_DIR]/instagram-captions.md and save descriptions with tags to [OUTPUT_DIR]/youtube-descriptions.md
```

**Wait for both to complete.**

Store outputs as `TRANSCRIPTS_DATA` and `SOCIAL_DATA`.

**Validation gate:**
- One transcript per selected story, each with a length marker (15s/30s/45s/60s/75s) and appropriate CTAs. No 90s scripts. 75s only on Extremely Important stories.
- One Instagram caption per story (long-form, 250-400 words, Dustin Fox style).
- One YouTube description per story.
- If any are missing, flag but proceed.

---

### Step 4: Spawn Blog Strategist (sequential)

Spawn a single `general-purpose` agent:

```
You are the Blog Strategist for the local-news system.

[FULL CONTENTS OF BLOG_STRATEGIST]

[FULL CONTENTS OF CONTENT_RULES]

SELECTED RANKED STORIES:
[TOP_STORIES_DATA]

Target date: [TARGET_DATE]

Create the SEO package for every selected story. Assign slugs, SEO titles, meta descriptions, keywords, and internal linking plans. Save to [OUTPUT_DIR]/blog-seo-package.md
```

Store output as `SEO_PACKAGE_DATA`.

**Validation gate:**
- One entry per selected story with a unique slug.
- All SEO titles under 60 characters.
- All meta descriptions under 150 characters.
- All keyword strings close to 500 characters.
- All stories have 3 related links.
- If validation fails, retry once.

---

### Step 5: Spawn Blog Creators (batched, waves of 6)

Blog creation runs in waves of 6 to avoid context pressure. Each wave spawns up to 6 `general-purpose` agents in parallel. Run as many waves as needed to cover every selected story (21 stories = 4 waves of 6/6/6/3; a larger set may need a 5th wave).

**Wave 1 — Stories 1-6:**

Spawn 6 agents in a SINGLE response. Each agent writes one blog post:

```
You are a Blog Creator for the local-news system.

[FULL CONTENTS OF BLOG_CREATOR]

[FULL CONTENTS OF TRANSCRIPT_TEMPLATES — blog post HTML template and NewsArticle schema sections]

[FULL CONTENTS OF CONTENT_RULES]

STORY TO WRITE:
[Story N data from TOP_STORIES_DATA — headline, summary, source URL(s), category, story type, area, viral score; for national-to-local stories include the national figure, local Vegas figure, and the local angle]

SEO PACKAGE FOR THIS STORY:
[Story N data from SEO_PACKAGE_DATA — slug, SEO title, meta description, keywords, related links]

ALL BLOG SLUGS (for internal linking):
[List of all selected slugs with titles from SEO_PACKAGE_DATA]

Target date: [TARGET_DATE]
Output file: [OUTPUT_DIR]/blogs/story-[NN]-[slug].html

Write a 2400-word blog article. Find and embed 4-5 images using direct web URLs. Include NewsArticle schema, source attribution, contact CTA, and 3 related blog links. For national-to-local stories, build the article around the national-vs-Vegas contrast. Save the file to the specified path.
```

**Wait for Wave 1 to complete. Verify the wave's HTML files exist.**

If a wave fails, retry the failing agents once before moving to the next wave.

**Wave 2 — Stories 7-12:** Same pattern.
**Wave 3 — Stories 13-18:** Same pattern.
**Wave 4 — Stories 19-24:** Same pattern (only the stories that exist).
**Wave 5 — Stories 25+:** Only if the selected set exceeds 24 stories.

**Validation gate (after all waves):**
- One HTML file per selected story exists in the `blogs/` directory.
- Each file contains `<article>` content, `<script type="application/ld+json">`, and `<img>` tags.
- **Image URL check:** Run `grep -rl 'src="#"' [OUTPUT_DIR]/blogs/` to find any blogs with placeholder images. If any files are returned, those agents failed. Retry them with this explicit instruction added to their prompt: "CRITICAL: Your previous submission had `src=\"#\"` placeholder images. You MUST search the web for real image URLs before writing. Use WebSearch to find images from Unsplash, Pexels, or Pixabay. `src=\"#\"` is not acceptable."
- Flag any missing files but do not block the rest of the workflow.

---

### Step 6: Spawn Reddit Post Writer (sequential)

Spawn a single `general-purpose` agent. **Reddit posts are created for Real Estate Market stories ONLY** (both local Las Vegas and national-to-local). Government/Development, School Board, and Hockey stories do NOT get Reddit posts.

```
You are the Reddit Post Writer for the local-news system.

[FULL CONTENTS OF REDDIT_POST_WRITER]

[FULL CONTENTS OF TRANSCRIPT_TEMPLATES — Reddit post template section]

[FULL CONTENTS OF CONTENT_RULES]

SELECTED RANKED STORIES:
[TOP_STORIES_DATA]

BLOG SLUGS (for linking):
[List of all selected slugs from SEO_PACKAGE_DATA]

Write Reddit posts for r/VegasRealtor for the Real Estate Market stories ONLY. Skip every Government/Development, School Board, and Hockey story — do not write posts for them. Reference that the video exists on Ryan's profile. Link to the full blog post. End each post with an engagement question. Save to [OUTPUT_DIR]/reddit-posts.md
```

Store output as `REDDIT_DATA`.

**Validation gate:**
- One post per Real Estate Market story (typically ~6), each with a title (bracket tag), body (200-400 words), flair, and engagement question.
- No posts for non-real-estate categories.
- If any are missing, flag but proceed.

---

### Step 7: Spawn Spreadsheet Assembler (sequential)

Spawn a single `general-purpose` agent:

```
You are the Spreadsheet Assembler for the local-news system.

[FULL CONTENTS OF SPREADSHEET_ASSEMBLER]

SELECTED STORIES WITH VIRAL SCORES:
[TOP_STORIES_DATA]

VIDEO TRANSCRIPTS:
[TRANSCRIPTS_DATA]

SEO PACKAGE:
[SEO_PACKAGE_DATA]

Create the formatted spreadsheet and weekly summary. Save to [OUTPUT_DIR]/story-spreadsheet.md and [OUTPUT_DIR]/weekly-summary.md
```

**Validation gate:**
- Spreadsheet has one row per selected story with all required columns.
- Weekly summary has entries for all selected stories.

---

### Step 8: Final Report

After all agents complete, display the final report:

```
## Local News Content Package Complete — [TARGET_DATE]

**Output directory:** [OUTPUT_DIR]

### Files Generated
1. research.md — All [N] researched stories combined, ordered by viral ranking
2. top-stories.md — [N] stories ranked by viral potential with scores and reasoning
3. video-transcripts.md — [N] green-screen video scripts ([N]x75s / [N]x60s / [N]x45s / [N]x30s / [N]x15s)
4. instagram-captions.md — [N] Instagram captions
5. youtube-descriptions.md — [N] YouTube descriptions
6. blog-seo-package.md — SEO package with [N] slugs
7. blogs/ — [N] blog articles (~2400 words each, with images and schema)
8. reddit-posts.md — [N] Reddit posts for r/VegasRealtor (real estate stories only)
9. story-spreadsheet.md — Compiled spreadsheet with all metadata
10. weekly-summary.md — Bulleted summary with viral reasoning

### Category Breakdown
- Government and Development: [N] stories
- School Board and Education: [N] stories
- Hockey: [N] stories
- Real Estate Market: [N] stories (of which [N] are national-to-local)

### Content Stats
- Video scripts: [N]x75s + [N]x60s + [N]x45s + [N]x30s + [N]x15s = ~[N] min recording time
- Blog posts: [N] x ~2400 words = ~[N] words total
- Reddit posts: [N] (real estate stories only)
- Instagram captions: [N]
- YouTube descriptions: [N]

### Terminal Commands

Run these in Terminal when you're ready:

**Publish all blogs to Lofty:**
```
python3 /Users/ryanrose/Downloads/Claude/_System/plugins/local-news-plugin/publish-local-news.py [TARGET_DATE] --yes
```

**Fix already-published blogs** (opens each post in Lofty, strips category labels, datelines, and bylines from the source HTML, and saves):
```
python3 /Users/ryanrose/Downloads/Claude/_System/plugins/local-news-plugin/fix-local-news-blogs.py [TARGET_DATE] --yes
```

**Subset options** (work on both scripts):
```
--posts 1-10    # specific range
--posts 5       # single story
--tab N         # Chrome tab number (default: 4)
```

**Requirements:** Chrome open, logged into Lofty, blog dashboard on tab 4.

[If any issues:]
### Notes
- [list any research gaps, retry outcomes, validation failures, or missing files]
```

---

## Error Handling

- **Research agent failure:** Retry once with the same prompt. If still empty, note thin data but proceed with available stories.
- **National-to-local agent thin on local tie-ins:** Not blocking. Keep only the stories with a verified local counterpart; if that leaves fewer than the Real Estate target, backfill the Real Estate Market slots with local Las Vegas stories from Agent 4.
- **Viral strategist failure:** Blocking. Retry up to 2 times. If still failing, stop and report.
- **Content/social writer failure:** Retry once. Note missing items in the final report.
- **Blog strategist failure:** Blocking. Retry once. Must have SEO package before blog creation.
- **Blog creator wave failure:** Retry failing agents once. Continue to next wave. Flag missing blogs.
- **Reddit post writer failure:** Retry once. Flag missing posts.
- **Spreadsheet assembler failure:** Retry once. Non-blocking for overall workflow.

## Core Principles

- Never stop to ask between steps. Run the full pipeline autonomously.
- Always validate before proceeding to the next step.
- Save intermediate outputs to disk as you go. Do not wait until the end.
- The manager never writes content. Sub-agents do all substantive work.
- Minimum 21 stories a week (3 a day), balanced across the four categories, but never cut a Red or Extremely Important story to hit the balance.
- National real estate news is not local real estate news. Every national-to-local story must carry the Clark County counterpart number.
- Quality over speed. Better to retry a failing agent than deliver incomplete content.
