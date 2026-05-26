---
name: local-news
description: Use when someone asks to research local news, create green-screen video scripts, generate weekly Las Vegas news content, build local news transcripts, run the weekly news roundup, create Clark County news videos for Instagram or YouTube, write local news blog posts, or create local news Reddit posts.
argument-hint: "optional: date override (YYYY-MM-DD)"
---

## What This Skill Does

Researches Clark County, NV local news across three categories (Government/Development, Restaurant/Business, School Board), ranks stories by viral potential, and produces a complete content package: green-screen video transcripts with CTAs, 2400-word blog articles with images and schema, Reddit posts for r/VegasRealtor, Instagram captions, YouTube descriptions, and a compiled story spreadsheet.

**Account:** @rosehomeslv
**Website:** rosehomeslv.com
**Expert:** Ryan Rose, Las Vegas Real Estate Expert

**Supporting files in this skill directory:**
- [research-gov-dev.md](research-gov-dev.md) — Government and Development Research Agent
- [research-restaurant-biz.md](research-restaurant-biz.md) — Restaurant and Business Research Agent
- [research-school-board.md](research-school-board.md) — School Board and Education Research Agent
- [viral-strategist.md](viral-strategist.md) — Viral Scoring and Top-20 Selection Agent
- [content-producer.md](content-producer.md) — Green-Screen Video Transcript Agent
- [social-media-writer.md](social-media-writer.md) — Instagram Caption and YouTube Description Agent
- [blog-strategist.md](blog-strategist.md) — Blog SEO and Slug Assignment Agent
- [blog-creator.md](blog-creator.md) — 2400-Word Blog Article Agent
- [reddit-post-writer.md](reddit-post-writer.md) — Reddit Post Agent
- [spreadsheet-assembler.md](spreadsheet-assembler.md) — Spreadsheet and Summary Agent
- [content-rules.md](content-rules.md) — Content rules for all output
- [source-registry.md](source-registry.md) — Research source URLs by category
- [transcript-templates.md](transcript-templates.md) — Templates for all output formats

---

## Architecture

You are the **Manager**. You orchestrate ten sub-agents:

1. **Government/Development Research Agent** — Finds 10-15 gov/dev news stories
2. **Restaurant/Business Research Agent** — Finds 10-15 restaurant/business stories
3. **School Board/Education Research Agent** — Finds 8-12 school board stories
4. **Viral Strategist Agent** — Scores all stories and selects top 20
5. **Content Producer Agent** — Writes green-screen video transcripts with CTAs
6. **Social Media Writer Agent** — Writes Instagram captions and YouTube descriptions
7. **Blog Strategist Agent** — Creates SEO package with slugs, titles, meta, keywords
8. **Blog Creator Agent** — Writes 2400-word HTML blog articles with images and schema
9. **Reddit Post Writer Agent** — Creates Reddit posts for r/VegasRealtor
10. **Spreadsheet Assembler Agent** — Compiles spreadsheet and weekly summary

**You never write content yourself.** You orchestrate, validate, and assemble the final output.

---

## Workflow

### Step 0: Initialize

1. Parse `$ARGUMENTS` for an optional date override (YYYY-MM-DD format). If not provided, use today's date. Store as `TARGET_DATE`.

2. Set the output directory:
   ```
   /Users/ryanrose/Downloads/Claude/Instagram/Local News/[TARGET_DATE]/
   ```
   Create this directory and a `blogs/` subdirectory inside it.

3. Read ALL supporting files from this skill directory and store each as a variable:
   - `RESEARCH_GOV_DEV` ← contents of research-gov-dev.md
   - `RESEARCH_RESTAURANT_BIZ` ← contents of research-restaurant-biz.md
   - `RESEARCH_SCHOOL_BOARD` ← contents of research-school-board.md
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

### Step 1: Spawn 3 Research Agents (parallel)

Spawn **three agents in parallel** using the Agent tool (all `general-purpose` type) in a SINGLE response:

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

**Agent 2 — Restaurant/Business Research Agent:**

```
You are a Restaurant and Business Research Agent for the local-news system.

[FULL CONTENTS OF RESEARCH_RESTAURANT_BIZ]

[FULL CONTENTS OF CONTENT_RULES]

[FULL CONTENTS OF SOURCE_REGISTRY — Restaurant and Business section only]

Target week ending: [TARGET_DATE]
Geographic scope: Clark County, Nevada (Las Vegas, Henderson, North Las Vegas, Boulder City, Summerlin, Spring Valley, Centennial Hills, Skye Canyon, Green Valley, unincorporated Clark County)

Return your findings in the exact structured format specified in the instructions. Use WebSearch and WebFetch to research. Be thorough and verify all stories against official sources. Prioritize nostalgia-driven closures and trendy/Instagram-worthy openings.
```

**Agent 3 — School Board/Education Research Agent:**

```
You are a School Board and Education Research Agent for the local-news system.

[FULL CONTENTS OF RESEARCH_SCHOOL_BOARD]

[FULL CONTENTS OF CONTENT_RULES]

[FULL CONTENTS OF SOURCE_REGISTRY — School Board and Education section only]

Target week ending: [TARGET_DATE]
Geographic scope: Clark County, Nevada

Return your findings in the exact structured format specified in the instructions. Use WebSearch and WebFetch to research. Be thorough and verify all stories against official sources.
```

**Wait for all 3 agents to complete.**

Store outputs as `GOV_DEV_DATA`, `RESTAURANT_BIZ_DATA`, `SCHOOL_BOARD_DATA`.

**Validation gate:**
- Each agent must return at least 8 stories with source URLs.
- If an agent returns fewer than 8, note it but proceed.
- If an agent returns 0 stories, retry once with the same prompt.
- Save raw research to the output directory as `research-gov-dev.md`, `research-restaurant-biz.md`, `research-school-board.md`.

---

### Step 2: Spawn Viral Strategist (sequential)

Spawn a single `general-purpose` agent:

```
You are the Viral Strategist for the local-news system.

[FULL CONTENTS OF VIRAL_STRATEGIST]

[FULL CONTENTS OF CONTENT_RULES]

GOVERNMENT AND DEVELOPMENT RESEARCH:
[GOV_DEV_DATA]

RESTAURANT AND BUSINESS RESEARCH:
[RESTAURANT_BIZ_DATA]

SCHOOL BOARD AND EDUCATION RESEARCH:
[SCHOOL_BOARD_DATA]

Select the top 20 stories maintaining the 40/50/10 category balance. Score each story and rank them. Follow the selection criteria exactly.
```

Store output as `TOP_20_DATA`.

**Validation gate:**
- Exactly 20 stories selected.
- Category balance approximately 8/10/2 (+/- 1 per category).
- Every story has a viral score (Red/Orange/Yellow/Green).
- If count is wrong or balance is off, retry up to 2 times.
- Save to `top-20-stories.md` in the output directory.

---

### Step 3: Spawn Content Producer + Social Media Writer (parallel)

Spawn **two agents in parallel** in a SINGLE response:

**Agent 1 — Content Producer:**

```
You are the Content Producer for the local-news system.

[FULL CONTENTS OF CONTENT_PRODUCER]

[FULL CONTENTS OF TRANSCRIPT_TEMPLATES — video transcript section only]

[FULL CONTENTS OF CONTENT_RULES]

TOP 20 RANKED STORIES:
[TOP_20_DATA]

Write green-screen video transcripts for all 20 stories. Assign lengths based on viral score. Include CTAs as specified. Save to [OUTPUT_DIR]/video-transcripts.md
```

**Agent 2 — Social Media Writer:**

```
You are the Social Media Writer for the local-news system.

[FULL CONTENTS OF SOCIAL_MEDIA_WRITER]

[FULL CONTENTS OF TRANSCRIPT_TEMPLATES — Instagram caption and YouTube description sections]

[FULL CONTENTS OF CONTENT_RULES]

TOP 20 RANKED STORIES:
[TOP_20_DATA]

Write Instagram captions and YouTube descriptions for all 20 stories. Save captions to [OUTPUT_DIR]/instagram-captions.md and descriptions to [OUTPUT_DIR]/youtube-descriptions.md
```

**Wait for both to complete.**

Store outputs as `TRANSCRIPTS_DATA` and `SOCIAL_DATA`.

**Validation gate:**
- 20 transcripts with length markers (10s/20s/30s) and appropriate CTAs.
- 20 Instagram captions with hook + body + CTA + hashtags.
- 20 YouTube descriptions.
- If any are missing, flag but proceed.

---

### Step 4: Spawn Blog Strategist (sequential)

Spawn a single `general-purpose` agent:

```
You are the Blog Strategist for the local-news system.

[FULL CONTENTS OF BLOG_STRATEGIST]

[FULL CONTENTS OF CONTENT_RULES]

TOP 20 RANKED STORIES:
[TOP_20_DATA]

Target date: [TARGET_DATE]

Create the SEO package for all 20 stories. Assign slugs, SEO titles, meta descriptions, keywords, and internal linking plans. Save to [OUTPUT_DIR]/blog-seo-package.md
```

Store output as `SEO_PACKAGE_DATA`.

**Validation gate:**
- 20 entries with unique slugs.
- All SEO titles under 60 characters.
- All meta descriptions under 150 characters.
- All keyword strings close to 500 characters.
- All stories have 3 related links.
- If validation fails, retry once.

---

### Step 5: Spawn Blog Creators (batched, waves of 5)

Blog creation runs in 4 waves to avoid context pressure. Each wave spawns 5 `general-purpose` agents in parallel.

**Wave 1 — Stories 1-5:**

Spawn 5 agents in a SINGLE response. Each agent writes one blog post:

```
You are a Blog Creator for the local-news system.

[FULL CONTENTS OF BLOG_CREATOR]

[FULL CONTENTS OF TRANSCRIPT_TEMPLATES — blog post HTML template and NewsArticle schema sections]

[FULL CONTENTS OF CONTENT_RULES]

STORY TO WRITE:
[Story N data from TOP_20_DATA — headline, summary, source URL, category, area, viral score]

SEO PACKAGE FOR THIS STORY:
[Story N data from SEO_PACKAGE_DATA — slug, SEO title, meta description, keywords, related links]

ALL 20 BLOG SLUGS (for internal linking):
[List of all 20 slugs with titles from SEO_PACKAGE_DATA]

Target date: [TARGET_DATE]
Output file: [OUTPUT_DIR]/blogs/story-[NN]-[slug].html

Write a 2400-word blog article. Find and embed 4-5 images using direct web URLs. Include NewsArticle schema, source attribution, contact CTA, and 3 related blog links. Save the file to the specified path.
```

**Wait for Wave 1 to complete. Verify 5 HTML files exist.**

If a wave fails, retry the failing agents once before moving to the next wave.

**Wave 2 — Stories 6-10:** Same pattern.
**Wave 3 — Stories 11-15:** Same pattern.
**Wave 4 — Stories 16-20:** Same pattern.

**Validation gate (after all 4 waves):**
- 20 HTML files exist in the `blogs/` directory.
- Each file contains `<article>` content, `<script type="application/ld+json">`, and `<img>` tags.
- Flag any missing files but do not block the rest of the workflow.

---

### Step 6: Spawn Reddit Post Writer (sequential)

Spawn a single `general-purpose` agent:

```
You are the Reddit Post Writer for the local-news system.

[FULL CONTENTS OF REDDIT_POST_WRITER]

[FULL CONTENTS OF TRANSCRIPT_TEMPLATES — Reddit post template section]

[FULL CONTENTS OF CONTENT_RULES]

TOP 20 RANKED STORIES:
[TOP_20_DATA]

BLOG SLUGS (for linking):
[List of all 20 slugs from SEO_PACKAGE_DATA]

Write 20 Reddit posts for r/VegasRealtor. Reference that the video exists on Ryan's profile. Link to the full blog post. End each post with an engagement question. Save to [OUTPUT_DIR]/reddit-posts.md
```

Store output as `REDDIT_DATA`.

**Validation gate:**
- 20 posts with titles (bracket tags), bodies (200-400 words), flairs, and engagement questions.
- If any are missing, flag but proceed.

---

### Step 7: Spawn Spreadsheet Assembler (sequential)

Spawn a single `general-purpose` agent:

```
You are the Spreadsheet Assembler for the local-news system.

[FULL CONTENTS OF SPREADSHEET_ASSEMBLER]

TOP 20 STORIES WITH VIRAL SCORES:
[TOP_20_DATA]

VIDEO TRANSCRIPTS:
[TRANSCRIPTS_DATA]

SEO PACKAGE:
[SEO_PACKAGE_DATA]

Create the formatted spreadsheet and weekly summary. Save to [OUTPUT_DIR]/story-spreadsheet.md and [OUTPUT_DIR]/weekly-summary.md
```

**Validation gate:**
- Spreadsheet has 20 rows with all required columns.
- Weekly summary has entries for all 20 stories.

---

### Step 8: Final Report

After all agents complete, display the final report:

```
## Local News Content Package Complete — [TARGET_DATE]

**Output directory:** [OUTPUT_DIR]

### Files Generated
1. research-gov-dev.md — [N] government/development stories researched
2. research-restaurant-biz.md — [N] restaurant/business stories researched
3. research-school-board.md — [N] school board stories researched
4. top-20-stories.md — Top 20 ranked by viral potential
5. video-transcripts.md — 20 green-screen video scripts ([N]x30s, [N]x20s, [N]x10s)
6. instagram-captions.md — 20 Instagram captions
7. youtube-descriptions.md — 20 YouTube descriptions
8. blog-seo-package.md — SEO package with 20 slugs
9. blogs/ — 20 blog articles (~2400 words each, with images and schema)
10. reddit-posts.md — 20 Reddit posts for r/VegasRealtor
11. story-spreadsheet.md — Compiled spreadsheet with all metadata
12. weekly-summary.md — Bulleted summary with viral reasoning

### Category Breakdown
- Government and Development: [N] stories
- Restaurant and Business: [N] stories
- School Board and Education: [N] stories

### Content Stats
- Video scripts: [N]x30s + [N]x20s + [N]x10s = ~[N] min recording time
- Blog posts: 20 x ~2400 words = ~48,000 words total
- Reddit posts: 20
- Instagram captions: 20
- YouTube descriptions: 20

### Terminal Commands

Run these in Terminal when you're ready:

**Publish all blogs to Lofty:**
```
python3 /Users/ryanrose/Downloads/Claude/Plugins/local-news-plugin/publish-local-news.py [TARGET_DATE] --yes
```

**Fix already-published blogs** (opens each post in Lofty, strips category labels, datelines, and bylines from the source HTML, and saves):
```
python3 /Users/ryanrose/Downloads/Claude/Plugins/local-news-plugin/fix-local-news-blogs.py [TARGET_DATE] --yes
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
- Quality over speed. Better to retry a failing agent than deliver incomplete content.
