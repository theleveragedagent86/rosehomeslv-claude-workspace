---
name: local-news
description: Use when someone asks to research local news, create green-screen video scripts, generate weekly Las Vegas news content, build local news transcripts, run the weekly news roundup, create Clark County news videos for Instagram or YouTube, write local news blog posts, or create local news Reddit posts.
argument-hint: "optional: date override (YYYY-MM-DD)"
---

## What This Skill Does

Researches Clark County, NV local news across five categories (Government/Development, School Board, Hockey, Real Estate Market, Local News and Events), ranks stories by viral potential, and produces a complete content package: green-screen video transcripts with CTAs, 2400-word blog articles with images and schema, Reddit posts for r/VegasRealtor (real estate stories only), Instagram captions, YouTube descriptions, and a compiled story spreadsheet.

The Real Estate Market category is fed by two research agents: a local Las Vegas market agent, and a national-to-local agent that finds national real estate headlines and reframes them against the actual Clark County numbers (national real estate news is not the same as local real estate news).

The Local News and Events category is the quick-hit local beat, modeled on the @realvegaslocals Instagram account: events and things to do, restaurant and business openings and closings, traffic and road closures, weather and utilities, public safety of broad interest, community and human interest, viral local moments, and neighborhood-level happenings. Residents first, tourists never.

Every researched story that does NOT make the weekly selected set still gets a blog post. That is the **bonus blog set**: blog only, no video transcript, no Instagram caption, no YouTube description, no Reddit post. It exists purely for SEO volume, so nothing verified goes to waste. Bonus blogs land in `blogs/bonus/` and never delay or degrade the main set.

**Account:** @rosehomeslv
**Website:** rosehomeslv.com
**Expert:** Ryan Rose, Las Vegas Real Estate Expert

**Supporting files in this skill directory:**
- [research-gov-dev.md](research-gov-dev.md) - Government and Development Research Agent
- [research-school-board.md](research-school-board.md) - School Board and Education Research Agent
- [research-hockey.md](research-hockey.md) - Hockey Research Agent
- [research-real-estate.md](research-real-estate.md) - Real Estate Market Research Agent (local Las Vegas)
- [research-national-real-estate.md](research-national-real-estate.md) - National-to-Local Real Estate Research Agent
- [research-local-events.md](research-local-events.md) - Local News and Events Research Agent
- [viral-strategist.md](viral-strategist.md) - Viral Scoring and Story Selection Agent
- [content-producer.md](content-producer.md) - Green-Screen Video Transcript Agent
- [social-media-writer.md](social-media-writer.md) - Instagram Caption and YouTube Description Agent
- [blog-strategist.md](blog-strategist.md) - Blog SEO and Slug Assignment Agent
- [blog-creator.md](blog-creator.md) - 2400-Word Blog Article Agent
- [bonus-blog-strategist.md](bonus-blog-strategist.md) - Bonus Blog SEO and Slug Assignment Agent (unselected stories)
- [bonus-blog-creator.md](bonus-blog-creator.md) - Bonus Blog Article Agent (unselected stories)
- [reddit-post-writer.md](reddit-post-writer.md) - Reddit Post Agent (real estate stories only)
- [spreadsheet-assembler.md](spreadsheet-assembler.md) - Spreadsheet and Summary Agent
- [content-rules.md](content-rules.md) - Content rules for all output
- [source-registry.md](source-registry.md) - Research source URLs by category
- [transcript-templates.md](transcript-templates.md) - Templates for all output formats

---

## Architecture

You are the **Manager**. You orchestrate fifteen sub-agents:

1. **Government/Development Research Agent** - Finds 10-15 gov/dev news stories
2. **School Board/Education Research Agent** - Finds 8-12 school board stories
3. **Hockey Research Agent** - Finds 8-12 hockey stories
4. **Real Estate Market Research Agent** - Finds 8-12 local Las Vegas residential market stories
5. **National-to-Local Real Estate Research Agent** - Finds 6-10 national real estate stories, each with a verified Clark County tie-in
6. **Local News and Events Research Agent** - Finds 10-15 local news and events stories across the quick-hit beats
7. **Viral Strategist Agent** - Scores all stories, selects the balanced set (minimum 27), and writes the bonus set of everything unselected
8. **Content Producer Agent** - Writes green-screen video transcripts with CTAs
9. **Social Media Writer Agent** - Writes Instagram captions and YouTube descriptions
10. **Blog Strategist Agent** - Creates SEO package with slugs, titles, meta, keywords
11. **Blog Creator Agent** - Writes 2400-word HTML blog articles with images and schema
12. **Bonus Blog Strategist Agent** - Creates the bonus SEO package, checks every slug against all prior runs, assigns angles to duplicate cuts
13. **Bonus Blog Creator Agent** - Writes the bonus blog articles into `blogs/bonus/`
14. **Reddit Post Writer Agent** - Creates Reddit posts for r/VegasRealtor (real estate stories only, never bonus stories)
15. **Spreadsheet Assembler Agent** - Compiles spreadsheet and weekly summary

**You never write content yourself.** You orchestrate, validate, and assemble the final output.

---

## Workflow

### Step 0: Initialize

1. Parse `$ARGUMENTS` for an optional date override (YYYY-MM-DD format). If not provided, use today's date. Store as `TARGET_DATE`.

2. Set the output directory:
   ```
   /Users/ryanrose/Downloads/Claude/Rose Homes LV/Content/Instagram/Local News/[TARGET_DATE]/
   ```
   Create this directory, a `blogs/` subdirectory inside it, and a `blogs/bonus/` subdirectory inside that. The bonus folder must exist before Step 5B runs.

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
   - `RESEARCH_LOCAL_EVENTS` ← contents of research-local-events.md
   - `VIRAL_STRATEGIST` ← contents of viral-strategist.md
   - `CONTENT_PRODUCER` ← contents of content-producer.md
   - `SOCIAL_MEDIA_WRITER` ← contents of social-media-writer.md
   - `BLOG_STRATEGIST` ← contents of blog-strategist.md
   - `BLOG_CREATOR` ← contents of blog-creator.md
   - `BONUS_BLOG_STRATEGIST` ← contents of bonus-blog-strategist.md
   - `BONUS_BLOG_CREATOR` ← contents of bonus-blog-creator.md
   - `REDDIT_POST_WRITER` ← contents of reddit-post-writer.md
   - `SPREADSHEET_ASSEMBLER` ← contents of spreadsheet-assembler.md
   - `CONTENT_RULES` ← contents of content-rules.md
   - `SOURCE_REGISTRY` ← contents of source-registry.md
   - `TRANSCRIPT_TEMPLATES` ← contents of transcript-templates.md

---

### Step 1: Spawn 6 Research Agents (parallel)

Spawn **six agents in parallel** using the Agent tool (all `general-purpose` type) in a SINGLE response:

**Agent 1 - Government/Development Research Agent:**

```
You are a Government and Development Research Agent for the local-news system.

[FULL CONTENTS OF RESEARCH_GOV_DEV]

[FULL CONTENTS OF CONTENT_RULES]

[FULL CONTENTS OF SOURCE_REGISTRY - Government and Development section only]

Target week ending: [TARGET_DATE]
Geographic scope: Clark County, Nevada (Las Vegas, Henderson, North Las Vegas, Boulder City, Summerlin, Spring Valley, Centennial Hills, Skye Canyon, Green Valley, unincorporated Clark County)

Return your findings in the exact structured format specified in the instructions. Use WebSearch and WebFetch to research. Be thorough and verify all stories against official sources.
```

**Agent 2 - School Board/Education Research Agent:**

```
You are a School Board and Education Research Agent for the local-news system.

[FULL CONTENTS OF RESEARCH_SCHOOL_BOARD]

[FULL CONTENTS OF CONTENT_RULES]

[FULL CONTENTS OF SOURCE_REGISTRY - School Board and Education section only]

Target week ending: [TARGET_DATE]
Geographic scope: Clark County, Nevada

Return your findings in the exact structured format specified in the instructions. Use WebSearch and WebFetch to research. Be thorough and verify all stories against official sources.
```

**Agent 3 - Hockey Research Agent:**

```
You are a Hockey Research Agent for the local-news system.

[FULL CONTENTS OF RESEARCH_HOCKEY]

[FULL CONTENTS OF CONTENT_RULES]

[FULL CONTENTS OF SOURCE_REGISTRY - Hockey section only]

Target week ending: [TARGET_DATE]
Geographic scope: Clark County, Nevada (Las Vegas, Henderson, North Las Vegas, T-Mobile Arena, Henderson Pavilion, local ice rinks)

Return your findings in the exact structured format specified in the instructions. Use WebSearch and WebFetch to research. Be thorough and verify all stories against official sources. Prioritize playoff news, roster moves, and community-impacting rink/arena stories.
```

**Agent 4 - Real Estate Market Research Agent (local Las Vegas):**

```
You are a Real Estate Market Research Agent for the local-news system.

[FULL CONTENTS OF RESEARCH_REAL_ESTATE]

[FULL CONTENTS OF CONTENT_RULES]

[FULL CONTENTS OF SOURCE_REGISTRY - Real Estate Market section only]

Target week ending: [TARGET_DATE]
Geographic scope: Clark County, Nevada (Las Vegas, Henderson, North Las Vegas, Boulder City, Summerlin, Spring Valley, Centennial Hills, Skye Canyon, Green Valley, unincorporated Clark County)

Return your findings in the exact structured format specified in the instructions. Use WebSearch and WebFetch to research. Be thorough and verify all stories against official sources. Focus on residential real estate only - homes, condos, townhomes, land for housing, and the buyers and sellers who make up the market. Do not report on commercial, industrial, or retail properties.
```

**Agent 5 - National-to-Local Real Estate Research Agent:**

```
You are a National-to-Local Real Estate Research Agent for the local-news system.

[FULL CONTENTS OF RESEARCH_NATIONAL_REAL_ESTATE]

[FULL CONTENTS OF CONTENT_RULES]

[FULL CONTENTS OF SOURCE_REGISTRY - National Real Estate section only]

Target week ending: [TARGET_DATE]
National scope for the trigger story; Clark County, Nevada scope for the local tie-in number.

Return your findings in the exact structured format specified in the instructions. Use WebSearch and WebFetch to research. For EVERY national story, you must also find and verify the matching Clark County / Las Vegas number so the contrast can be reframed for a local audience. Do not keep a national story that has no findable local counterpart. Focus on residential real estate only.
```

**Agent 6 - Local News and Events Research Agent:**

```
You are a Local News and Events Research Agent for the local-news system.

[FULL CONTENTS OF RESEARCH_LOCAL_EVENTS]

[FULL CONTENTS OF CONTENT_RULES]

[FULL CONTENTS OF SOURCE_REGISTRY - Local News and Events section only]

Target week ending: [TARGET_DATE]
Geographic scope: Clark County, Nevada (Las Vegas, Henderson, North Las Vegas, Boulder City, Summerlin, Spring Valley, Centennial Hills, Skye Canyon, Green Valley, unincorporated Clark County)

Return your findings in the exact structured format specified in the instructions. Use WebSearch and WebFetch to research. Find 10-15 stories with a varied spread across the beats: events and things to do, openings and closings, traffic and road closures, weather and utilities, public safety of broad community interest, community and human interest, viral local moments, and neighborhood-specific happenings. Do not hand back a set that is all one beat type. Residents first, tourists never. Instagram accounts are leads only - always locate and cite the underlying primary or news source.
```

**Wait for all 6 agents to complete.**

Store outputs as `GOV_DEV_DATA`, `SCHOOL_BOARD_DATA`, `HOCKEY_DATA`, `REAL_ESTATE_DATA`, `NATIONAL_RE_DATA`, `LOCAL_EVENTS_DATA`.

**Validation gate:**
- The four Clark County agents (Gov-Dev, School Board, Hockey, Real Estate) should each return at least 6 stories with source URLs (they target 8-12).
- The National-to-Local agent should return at least 4 stories (it targets 6-10), and EACH must include both a national figure and a verified local Clark County figure. Drop any national story missing its local tie-in.
- The Local News and Events agent should return at least 8 stories (it targets 10-15). The returned set must be varied, not all one beat type. If it comes back with, for example, ten restaurant openings and nothing else, send it back once for a broader spread.
- **For ALL six agents:** every story must include a `Source` (publication name) and an `Article Title` (the exact headline of the source article, word for word). A story with no article title cannot be published. Drop it. This feeds the Instagram source line.
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

LOCAL NEWS AND EVENTS RESEARCH:
[LOCAL_EVENTS_DATA]

Select a balanced set of AT LEAST 27 stories (27 is the weekly minimum - it feeds roughly 4 posts a day). Target balance: 5 Government-Development / 4 School Board / 5 Hockey / 7 Real Estate Market / 6 Local News and Events. The Real Estate Market count blends local Las Vegas stories and national-to-local stories, roughly half and half. The Local News and Events count must be varied - mix across at least 4 different beat types, not 6 of the same kind. Score each story and rank them. Follow the selection criteria exactly.

Every story you output must carry its Source (publication name) and Article Title (the exact source headline, word for word). A story with no article title cannot be published - drop it and take the next-best story in that category.

NEVER cut a Red-tier or Extremely Important story just to hold the balance. If there are more than enough top stories, expand the total above 27 so nothing important is dropped.

PREVIOUSLY COVERED STORIES - DO NOT SELECT THESE AGAIN:
[PREVIOUSLY_COVERED_HEADLINES]

A story is "previously covered" if it describes the same news event - same incident, same announcement, same opening/closing, same vote, same entity and location. An ongoing topic (VGK playoffs, A's stadium construction, water restrictions) may be included ONLY if there is a genuinely NEW development this week that was not covered in any prior run. A minor update or recap with no new facts does not qualify. Apply this check after scoring but before finalizing your selections. If a story would be a duplicate, skip it and select the next-best story in that category.

YOU MUST ALSO PRODUCE THE BONUS SET. Write a second file, bonus-stories.md, containing EVERY researched story from all six agents that you did not select. Each entry carries headline, category, story type, area, full summary, source name, article title, URL, date, why it matters, national and local figures where applicable, and a Cut Reason of Duplicate, Score, or Overlap. Every Duplicate cut also carries a Prior Coverage field naming the earlier headline it duplicates. Do NOT write a bonus entry for a story with no verified source URL, and do NOT write a bonus entry for a story that is functionally the same content as a story already in your selected set (mark those Overlap in your notes and skip them). The bonus set is never a reason to shrink the selected set.
```

Store output as `TOP_STORIES_DATA` and `BONUS_STORIES_DATA`.

**Validation gate:**
- At least 27 stories selected.
- Category balance approximately 5 Gov-Dev / 4 School Board / 5 Hockey / 7 Real Estate / 6 Local News and Events (+/- 1 per category), with the floors from the viral strategist honored (Gov-Dev ≥4, School Board ≥3, Hockey ≥3, Real Estate ≥5, Local News and Events ≥4).
- The Local News and Events selections span at least 4 different beat types. Six of the same kind is a failed selection.
- No Red-tier or Extremely Important story was dropped to hold the balance.
- Every story has a viral score (Red/Orange/Yellow/Green) and an Extremely Important flag (Yes/No).
- Every story carries a `Source` and an exact `Article Title`.
- If the count is below 27 or a category is below its floor, retry up to 2 times.
- Save to `top-stories.md` in the output directory.
- **Bonus set:** `bonus-stories.md` also exists in the output directory. Every bonus entry has a verified source URL and a Cut Reason of Duplicate or Score. Every Duplicate entry has a Prior Coverage field. No bonus entry duplicates a selected story. If `bonus-stories.md` is missing, ask the strategist for it once. This is non-blocking. If it still does not come back, skip Step 5B and note it in the final report.
- **Save combined research file:** After the viral strategist output is validated, save a single `research.md` to the output directory. This file contains the full research data for all selected stories (headline, category, story type, area, summary, source(s), article title(s), URL(s), date, why it matters, national/local figures for national-to-local stories, flags) in the same viral-ranked order as `top-stories.md`. This is the ONLY research file saved to disk. Do not save separate per-category research files.

---

### Step 3: Spawn Content Producer + Social Media Writer (parallel)

Spawn **two agents in parallel** in a SINGLE response:

**Agent 1 - Content Producer:**

```
You are the Content Producer for the local-news system.

[FULL CONTENTS OF CONTENT_PRODUCER]

[FULL CONTENTS OF TRANSCRIPT_TEMPLATES - video transcript section only]

[FULL CONTENTS OF CONTENT_RULES]

SELECTED RANKED STORIES:
[TOP_STORIES_DATA]

Write green-screen video transcripts for every selected story. Assign lengths from the 15/30/45/60/75 second tiers based on viral score. There is no 90-second option. 75 seconds is reserved for stories flagged Extremely Important and must be used sparingly. Include CTAs as specified. For national-to-local real estate stories, lead with the national-vs-Vegas contrast. Save to [OUTPUT_DIR]/video-transcripts.md
```

**Agent 2 - Social Media Writer:**

```
You are the Social Media Writer for the local-news system.

[FULL CONTENTS OF SOCIAL_MEDIA_WRITER]

[FULL CONTENTS OF TRANSCRIPT_TEMPLATES - Instagram caption and YouTube description sections]

[FULL CONTENTS OF CONTENT_RULES]

SELECTED RANKED STORIES:
[TOP_STORIES_DATA]

Write Instagram captions, YouTube Shorts descriptions, and YouTube tags for every selected story. For national-to-local real estate stories, lead with the national-vs-Vegas contrast. Save captions to [OUTPUT_DIR]/instagram-captions.md and save descriptions with tags to [OUTPUT_DIR]/youtube-descriptions.md
```

**Wait for both to complete.**

Store outputs as `TRANSCRIPTS_DATA` and `SOCIAL_DATA`.

**Validation gate:**
- One transcript per selected story, each with a length marker (15s/30s/45s/60s/75s) and appropriate CTAs. No 90s scripts. 75s only on Extremely Important stories.
- One Instagram caption per story (long-form, 250-400 words, Dustin Fox style), each carrying the source line built from the story's Source and Article Title.
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

Blog creation runs in waves of 6 to avoid context pressure. Each wave spawns up to 6 `general-purpose` agents in parallel. Run as many waves as needed to cover every selected story (27 stories = 5 waves of 6/6/6/6/3; a larger set may need a 6th wave).

**Wave 1 - Stories 1-6:**

Spawn 6 agents in a SINGLE response. Each agent writes one blog post:

```
You are a Blog Creator for the local-news system.

[FULL CONTENTS OF BLOG_CREATOR]

[FULL CONTENTS OF TRANSCRIPT_TEMPLATES - blog post HTML template and NewsArticle schema sections]

[FULL CONTENTS OF CONTENT_RULES]

STORY TO WRITE:
[Story N data from TOP_STORIES_DATA - headline, summary, source, article title, source URL(s), category, story type, area, viral score; for national-to-local stories include the national figure, local Vegas figure, and the local angle]

SEO PACKAGE FOR THIS STORY:
[Story N data from SEO_PACKAGE_DATA - slug, SEO title, meta description, keywords, related links]

ALL BLOG SLUGS (for internal linking):
[List of all selected slugs with titles from SEO_PACKAGE_DATA]

Target date: [TARGET_DATE]
Output file: [OUTPUT_DIR]/blogs/story-[NN]-[slug].html

Write a 2400-word blog article. Find and embed 4-5 images using direct web URLs. Include NewsArticle schema, source attribution, contact CTA, and 3 related blog links. For national-to-local stories, build the article around the national-vs-Vegas contrast. Save the file to the specified path.
```

**Wait for Wave 1 to complete. Verify the wave's HTML files exist.**

If a wave fails, retry the failing agents once before moving to the next wave.

**Wave 2 - Stories 7-12:** Same pattern.
**Wave 3 - Stories 13-18:** Same pattern.
**Wave 4 - Stories 19-24:** Same pattern.
**Wave 5 - Stories 25-30:** Same pattern (only the stories that exist).
**Wave 6 - Stories 31+:** Only if the selected set exceeds 30 stories.

**Validation gate (after all waves):**
- One HTML file per selected story exists in the `blogs/` directory.
- Each file contains `<article>` content, `<script type="application/ld+json">`, and `<img>` tags.
- **Image URL check:** Run `grep -rl 'src="#"' [OUTPUT_DIR]/blogs/` to find any blogs with placeholder images. If any files are returned, those agents failed. Retry them with this explicit instruction added to their prompt: "CRITICAL: Your previous submission had `src=\"#\"` placeholder images. You MUST search the web for real image URLs before writing. Use WebSearch to find images from Unsplash, Pexels, or Pixabay. `src=\"#\"` is not acceptable."
- Flag any missing files but do not block the rest of the workflow.

---

### Step 5B: Spawn Bonus Blog Strategist, then Bonus Blog Creators (batched, waves of 6)

Every researched story that did not make the selected set becomes a blog post and nothing else. This stage is entirely non-blocking. It never delays or degrades the main set, and if it fails outright the run is still a success.

Skip this step only if `bonus-stories.md` does not exist or contains zero entries.

**5B-1: Bonus Blog Strategist (sequential)**

Spawn a single `general-purpose` agent:

```
You are the Bonus Blog Strategist for the local-news system.

[FULL CONTENTS OF BONUS_BLOG_STRATEGIST]

[FULL CONTENTS OF CONTENT_RULES]

BONUS STORIES:
[BONUS_STORIES_DATA]

SELECTED STORY SLUGS (this week, for internal linking and collision avoidance):
[List of all selected slugs with titles from SEO_PACKAGE_DATA]

Target date: [TARGET_DATE]

Run the slug collision command first and hold the full list of existing slugs before assigning anything. Create the SEO package for every bonus story: slug, SEO title, meta description, keywords, 3 related links, and for every Duplicate cut an Angle naming both the distinct treatment and the prior post's slug. Save to [OUTPUT_DIR]/bonus-blog-seo-package.md
```

Store output as `BONUS_SEO_PACKAGE_DATA`.

**Validation gate:**
- One entry per bonus story with a unique slug.
- No slug collides with any slug from a prior run or from this week's selected set.
- All SEO titles under 60 characters, all meta descriptions under 150 characters, all keyword strings close to 500 characters, all stories with 3 related links.
- Every `Duplicate` cut has an Angle naming the treatment and the prior post's slug.
- If validation fails, retry once. If it fails again, flag and skip the rest of Step 5B.

**5B-2: Bonus Blog Creators (waves of 6)**

Same wave pattern as Step 5. Spawn up to 6 `general-purpose` agents in parallel per wave and run as many waves as the bonus set needs.

```
You are a Bonus Blog Creator for the local-news system.

[FULL CONTENTS OF BONUS_BLOG_CREATOR]

[FULL CONTENTS OF BLOG_CREATOR]

[FULL CONTENTS OF TRANSCRIPT_TEMPLATES - blog post HTML template and NewsArticle schema sections]

[FULL CONTENTS OF CONTENT_RULES]

BONUS STORY TO WRITE:
[Bonus story N data from BONUS_STORIES_DATA - headline, full summary, why it matters, source, article title, source URL, category, story type, area, cut reason, prior coverage if any; for national-to-local stories include the national figure and the local Vegas figure]

BONUS SEO PACKAGE FOR THIS STORY:
[Bonus story N data from BONUS_SEO_PACKAGE_DATA - slug, SEO title, meta description, keywords, related links, Angle if this is a Duplicate cut]

ALL SLUGS (for internal linking):
[List of all selected slugs and all bonus slugs with titles]

Target date: [TARGET_DATE]
Output file: [OUTPUT_DIR]/blogs/bonus/bonus-[NN]-[slug].html

Write a 2400-word blog article in the standard blog-creator format. Find and embed 4-5 real image URLs. Include NewsArticle schema, source attribution, contact CTA, and 3 related blog links. If this is a Duplicate cut, write to the assigned Angle and include one sentence linking back to the prior post as earlier coverage. Never restate the earlier article. Do not write a video transcript, caption, description, or Reddit post. Save the file to the specified path.
```

**Wait for each wave to complete before starting the next. Verify the wave's HTML files exist.**

**Validation gate (after all waves):**
- One HTML file per bonus story exists in `[OUTPUT_DIR]/blogs/bonus/`.
- Each file contains `<article>` content, `<script type="application/ld+json">`, and `<img>` tags.
- **Image URL check:** Run `grep -rl 'src="#"' [OUTPUT_DIR]/blogs/bonus/` to find any bonus blogs with placeholder images. Retry those agents once with the same explicit instruction used in Step 5: "CRITICAL: Your previous submission had `src=\"#\"` placeholder images. You MUST search the web for real image URLs before writing. Use WebSearch to find images from Unsplash, Pexels, or Pixabay. `src=\"#\"` is not acceptable."
- **Non-blocking.** Flag every miss and continue. Never retry a bonus wave more than once, and never let a bonus failure stop Step 6 or Step 7.

---

### Step 6: Spawn Reddit Post Writer (sequential)

Spawn a single `general-purpose` agent. **Reddit posts are created for Real Estate Market stories in the SELECTED set ONLY** (both local Las Vegas and national-to-local). Government/Development, School Board, Hockey, and Local News and Events stories do NOT get Reddit posts. **Bonus stories are excluded from Reddit entirely**, including bonus real estate stories. Do not pass `BONUS_STORIES_DATA` to this agent.

```
You are the Reddit Post Writer for the local-news system.

[FULL CONTENTS OF REDDIT_POST_WRITER]

[FULL CONTENTS OF TRANSCRIPT_TEMPLATES - Reddit post template section]

[FULL CONTENTS OF CONTENT_RULES]

SELECTED RANKED STORIES:
[TOP_STORIES_DATA]

BLOG SLUGS (for linking):
[List of all selected slugs from SEO_PACKAGE_DATA]

Write Reddit posts for r/VegasRealtor for the selected Real Estate Market stories ONLY. Skip every Government/Development, School Board, Hockey, and Local News and Events story - do not write posts for them. Bonus stories get no Reddit post at all. Reference that the video exists on Ryan's profile. Link to the full blog post. End each post with an engagement question. Save to [OUTPUT_DIR]/reddit-posts.md
```

Store output as `REDDIT_DATA`.

**Validation gate:**
- One post per selected Real Estate Market story (typically ~7), each with a title (bracket tag), body (200-400 words), flair, and engagement question.
- No posts for non-real-estate categories.
- No posts for bonus stories.
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

BONUS STORIES (appendix only):
[BONUS_STORIES_DATA]

BONUS SEO PACKAGE (appendix only):
[BONUS_SEO_PACKAGE_DATA]

Create the formatted spreadsheet and weekly summary. Save to [OUTPUT_DIR]/story-spreadsheet.md and [OUTPUT_DIR]/weekly-summary.md

Bonus stories are EXCLUDED from the main spreadsheet table and from the weekly summary. They have no video length, no caption, and no Reddit post, so they do not belong in a row alongside the selected set. Instead, add a short appendix table at the bottom of the spreadsheet with four columns only: Bonus Headline, Category, Cut Reason, Slug. Nothing else.
```

**Validation gate:**
- Spreadsheet has one row per selected story with all required columns, including Source and Article Title.
- No bonus story appears in the main table.
- The bonus appendix table exists with one row per bonus story and exactly the four columns: headline, category, cut reason, slug. If there were no bonus stories, the appendix is omitted.
- Weekly summary has entries for all selected stories and none for bonus stories.

---

### Step 8: Final Report

After all agents complete, display the final report:

```
## Local News Content Package Complete - [TARGET_DATE]

**Output directory:** [OUTPUT_DIR]

### Files Generated
1. research.md - All [N] researched stories combined, ordered by viral ranking
2. top-stories.md - [N] stories ranked by viral potential with scores and reasoning
3. video-transcripts.md - [N] green-screen video scripts ([N]x75s / [N]x60s / [N]x45s / [N]x30s / [N]x15s)
4. instagram-captions.md - [N] Instagram captions
5. youtube-descriptions.md - [N] YouTube descriptions
6. blog-seo-package.md - SEO package with [N] slugs
7. blogs/ - [N] blog articles (~2400 words each, with images and schema)
8. bonus-stories.md - [N] researched stories that did not make the selected set
9. bonus-blog-seo-package.md - Bonus SEO package with [N] slugs
10. blogs/bonus/ - [N] bonus blog articles (~2400 words each, blog only)
11. reddit-posts.md - [N] Reddit posts for r/VegasRealtor (selected real estate stories only)
12. story-spreadsheet.md - Compiled spreadsheet with all metadata, plus the bonus appendix
13. weekly-summary.md - Bulleted summary with viral reasoning

### Category Breakdown
- Government and Development: [N] stories
- School Board and Education: [N] stories
- Hockey: [N] stories
- Real Estate Market: [N] stories (of which [N] are national-to-local)
- Local News and Events: [N] stories
- TOTAL: [N] (minimum 27)

### Bonus Blogs
- Bonus stories written: [N]
- Cut reason Duplicate: [N] (each written to a new angle, each linking back to the earlier post)
- Cut reason Score: [N]
- Excluded, overlapped a selected story: [N]
- Excluded, no verified source URL: [N]
- Slugs rewritten to avoid a collision with a prior run: [N]
- Bonus blogs that failed or came back short: [N] ([list])

### Content Stats
- Video scripts: [N]x75s + [N]x60s + [N]x45s + [N]x30s + [N]x15s = ~[N] min recording time
- Blog posts, selected: [N] x ~2400 words = ~[N] words total
- Blog posts, bonus: [N] x ~2400 words = ~[N] words total
- Blog posts, all in: [N] = ~[N] words total
- Reddit posts: [N] (selected real estate stories only, typically ~7, never bonus)
- Instagram captions: [N] (selected stories only)
- YouTube descriptions: [N] (selected stories only)

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
- **Local News and Events agent failure:** Retry once with the same prompt. If it comes back thin or all one beat type, note the thin data and proceed; backfill the open slots from the other categories so the total still clears 27.
- **Viral strategist failure:** Blocking. Retry up to 2 times. If still failing, stop and report.
- **Content/social writer failure:** Retry once. Note missing items in the final report.
- **Blog strategist failure:** Blocking. Retry once. Must have SEO package before blog creation.
- **Blog creator wave failure:** Retry failing agents once. Continue to next wave. Flag missing blogs.
- **Bonus set missing from the viral strategist:** Non-blocking. Ask for `bonus-stories.md` once. If it still does not arrive, skip Step 5B entirely and note it in the final report. Never rerun the strategist's main selection over this.
- **Bonus blog strategist failure:** Non-blocking. Retry once. If it fails again, skip the bonus blog creators and note it. The selected set is unaffected.
- **Bonus blog creator wave failure:** Non-blocking, always. Retry the failing wave once, then flag whatever is still missing and continue. Never retry a bonus wave twice, and never let a bonus failure delay Step 6 or Step 7.
- **Bonus slug collision found:** Send the colliding entries back to the bonus blog strategist once for new slugs. If a collision survives that, drop those specific stories rather than publishing a duplicate URL.
- **Reddit post writer failure:** Retry once. Flag missing posts.
- **Spreadsheet assembler failure:** Retry once. Non-blocking for overall workflow.

## Core Principles

- Never stop to ask between steps. Run the full pipeline autonomously.
- Always validate before proceeding to the next step.
- Save intermediate outputs to disk as you go. Do not wait until the end.
- The manager never writes content. Sub-agents do all substantive work.
- Minimum 27 stories a week (roughly 4 a day), balanced across the five categories, but never cut a Red or Extremely Important story to hit the balance.
- Every story carries its Source and exact Article Title through the whole pipeline. That is what powers the Instagram source line, which credits the original reporting.
- National real estate news is not local real estate news. Every national-to-local story must carry the Clark County counterpart number.
- Local News and Events is written for residents, never for tourists. If a local would never go, it does not run.
- Bonus blogs never delay or degrade the main set. Every bonus stage is non-blocking. If the bonus pipeline falls over, the week still ships.
- A bonus blog on a previously covered event must add a new angle, not duplicate the earlier post. Write the newer development, the deeper explainer, the what-this-means piece, or the background timeline, and link back to the original coverage.
- Quality over speed. Better to retry a failing agent than deliver incomplete content.
