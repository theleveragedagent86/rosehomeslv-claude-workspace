---
name: blog-writer
description: Use when someone asks to create blog posts, write a blog post, generate real estate content, write about a Las Vegas neighborhood or community, or create content for Rose Homes LV.
argument-hint: "neighborhood or community name"
---

## What This Skill Does

Creates SEO-optimized blog posts about Las Vegas area residential real estate communities and neighborhoods using a multi-agent orchestration system. Builds topical authority for Ryan Rose as the premier Las Vegas real estate expert. Content is optimized for traditional search (SEO), AI answer engines (AEO), and generative AI platforms (GEO).

**Website:** www.rosehomeslv.com
**Blog Index:** www.rosehomeslv.com/blogs
**Expert/Author:** Ryan Rose, Las Vegas Real Estate Expert

**Supporting files in this skill directory:**
- [research-agent.md](research-agent.md) — Research Agent instructions
- [organizer-agent.md](organizer-agent.md) — Organizer Agent instructions
- [content-producer.md](content-producer.md) — Content Producer Agent instructions
- [templates.md](templates.md) — Blog post structure and SEO package format
- [content-rules.md](content-rules.md) — Content verification and formatting rules
- [seo-guidelines.md](seo-guidelines.md) — SEO/AEO/GEO strategy

---

## Architecture

You are the **Manager**. You orchestrate three types of sub-agents:

1. **Research Agent** (1 instance) — Gathers all factual data about the neighborhood
2. **Organizer Agent** (1 instance) — Creates topics, batches, and the Slug Registry
3. **Content Producers** (up to 5 per wave, parallel) — Each writes a batch of 5 posts + SEO package

**You never write blog posts yourself.** You only orchestrate, track progress, and verify output.

---

## Workflow

### Step 0: Initialize

Get the neighborhood name from `$ARGUMENTS` or ask the user.

Set the output directory:
```
/Users/ryanrose/Downloads/Claude/Claude Blogs/[NEIGHBORHOOD NAME]/
```

Create the directory if it does not exist (use uppercase neighborhood name for the folder, matching existing pattern like `MADEIRA CANYON`).

---

### Step 1: Spawn Research Agent

Read the file `research-agent.md` from this skill directory.

Use the **Agent tool** to spawn a single `general-purpose` sub-agent with this prompt structure:

```
You are a Research Agent for the blog-writer system.

[FULL CONTENTS OF research-agent.md]

Neighborhood to research: [NEIGHBORHOOD NAME]

Return your findings in the exact structured format specified in the instructions.
```

Wait for the Research Agent to complete. Store its entire output as `RESEARCH_DATA`.

**Validate research quality before proceeding:**
- Confirm the Source URLs table has at least 10 entries. If fewer, note it but proceed.
- Confirm the People Also Ask section has at least 10 questions. If fewer than 10, flag this for the Organizer (topic generation may be limited).
- Confirm the Restaurants & Dining section has at least 5 entries. If thin, note which categories have sparse data so the Organizer can adjust batch planning.
- Check for any "Not found" or "Limited data available" markers and log them. These will affect which topics are viable.

Save the raw research data to the output directory as `research-data.md` for reference.

---

### Step 2: Spawn Organizer Agent

Read the file `organizer-agent.md` from this skill directory.

Use the **Agent tool** to spawn a single `general-purpose` sub-agent with this prompt structure:

```
You are an Organizer Agent for the blog-writer system.

[FULL CONTENTS OF organizer-agent.md]

Here is the research data to organize:

[RESEARCH_DATA]

Research quality notes:
- PAA questions found: [count]
- Thin data categories: [list any categories with sparse data]
- "Not found" markers: [list any]

The existing blog files directory to check for slug conflicts: /Users/ryanrose/Downloads/Claude/Claude Blogs/
The live website to check for slug conflicts: https://www.rosehomeslv.com/blogs/

Create the master topic list, batch assignments, and verified Slug Registry.
```

Wait for the Organizer Agent to complete. Store its output as `ORGANIZED_DATA` (contains the master topic list, batch assignments, and Slug Registry).

Save the master topic list to the output directory as `master-topic-list.md`.

**Before proceeding to content production, verify the Organizer output:**
- Every topic has a unique slug (no duplicates within the list)
- Every slug follows the format rules (lowercase, hyphens, under 60 chars, includes neighborhood name)
- Batch 1 contains the foundation posts (overview, prices, "good place to live", HOA/community, schools/PAA)
- Total topic count is reasonable for the research data available (minimum 15 topics for a well-documented neighborhood; fewer is acceptable for thin-data communities)

Display to the user: the total topic count, total batch count, and batch theme names. Then immediately proceed to Step 3.

---

### Step 3: Content Production (Waves)

Read these files from this skill directory:
- `content-producer.md`
- `templates.md`
- `content-rules.md`
- `seo-guidelines.md`

Store their contents. These will be passed to every Content Producer agent.

**Process batches in waves of up to 5 batches per wave.**

For each wave:

1. Determine which batches are in this wave (e.g., Wave 1 = Batches 1-5, Wave 2 = Batches 6-10).

2. For each batch in the wave, **extract the relevant research data sections** for that batch's topics. Do not dump the entire research dataset; select only what applies:

   | Batch Theme | Research Sections to Include |
   |---|---|
   | Foundation | Official Community Info, Real Estate Overview, Lifestyle & Location, Schools (summary), PAA Questions |
   | Parks & Recreation | Parks & Recreation, Trails, Lifestyle & Location (pet/family info) |
   | Schools & Education | Schools, Lifestyle & Location (family info), Official Community Info (age restrictions) |
   | Dining | Restaurants & Dining, Shopping & Retail (for location context) |
   | Shopping | Shopping & Retail, Attractions & Points of Interest |
   | Real Estate | Real Estate Overview, Official Community Info (HOA, gated status), Lifestyle & Location |
   | Lifestyle | Lifestyle & Location, Official Community Info, Parks (for pet/outdoor topics) |
   | Community / HOA | Official Community Info, Real Estate Overview (gated/builders), Lifestyle & Location |
   | Comparisons | All sections (comparisons need broad data) |

   Always include the Source URLs table so the Content Producer can attribute sources.

3. Spawn a **Content Producer agent** for each batch using the Agent tool with `general-purpose` type. Use this prompt structure:

```
You are a Content Producer Agent for the blog-writer system.

[FULL CONTENTS OF content-producer.md]

=== YOUR ASSIGNMENT ===

Neighborhood: [NEIGHBORHOOD NAME]
Batch Number: [B]
Post Number Range: [start]-[end] (e.g., posts 6-10)
Today's Date: [YYYY-MM-DD]

Your 5 Topics:
[Topic table for this batch from ORGANIZED_DATA — post number, title, slug, category]

=== SLUG REGISTRY (for internal linking) ===

[FULL Slug Registry table from ORGANIZED_DATA — all topics, all batches]

=== RESEARCH DATA (relevant to your topics) ===

[FILTERED research sections relevant to this batch's theme/topics]

=== Source URLs from Research ===

[Source URLs table from RESEARCH_DATA]

=== CONTENT RULES ===

[FULL CONTENTS OF content-rules.md]

=== TEMPLATES ===

[FULL CONTENTS OF templates.md]

=== SEO GUIDELINES ===

[FULL CONTENTS OF seo-guidelines.md]

=== OUTPUT DIRECTORY ===

Save all files to: [OUTPUT DIRECTORY PATH]

Write all 5 posts and the SEO package, save them as files, and return your summary.
```

4. **Spawn ALL batch agents for this wave in a single response** (parallel Agent tool calls). This is critical for performance — do NOT spawn them one at a time.

5. Wait for all agents in the wave to complete.

6. **Verify output after each wave:**
   - Check the output directory for expected files: 5 `.html` files per batch + 1 `seo-package-batch[B].md` per batch
   - Count total files vs. expected
   - Note any flags returned by Content Producers (thin data posts, missing source URLs)
   - If any batch produced fewer than 5 posts, log the missing posts for retry

7. Display a brief progress summary:
```
Wave [X] complete: [N] posts written (posts [start]-[end])
Files verified: [count] of [expected]
Flags: [any thin-data or missing-source notes from Content Producers]
Total progress: [completed]/[total] posts
```

8. **Immediately proceed to the next wave.** Do NOT ask the user for permission between waves.

---

### Step 4: Final Report

After all waves are complete:

1. **Run a final file audit:**
   - List all files in the output directory
   - Confirm post count matches the master topic list
   - Confirm all SEO package files exist
   - Note any missing files

2. Display the final report:

```
Blog writing complete for [NEIGHBORHOOD NAME]:

Posts written: [N] of [expected]
Batches completed: [B] of [expected]
SEO packages: [B]
Master topic list: master-topic-list.md
Research data: research-data.md
Output directory: [OUTPUT DIRECTORY PATH]

[If any flags:]
Notes:
- [list any thin-data flags, missing files, or retried batches]
```

---

### Error Handling

**Content Producer failure (no output or partial output):**
1. Automatically retry that batch by spawning a new Content Producer with the same prompt
2. Allow up to **2 retry attempts** per batch
3. On retry, include a note in the prompt: "Previous attempt for this batch failed. Ensure all 5 posts are written and saved."
4. Only alert the user if a batch fails after 2 retries
5. Continue with remaining waves regardless of individual batch failures

**Research Agent returns thin data:**
- Do NOT re-run the Research Agent (it already used fallback strategies)
- Pass the thin-data notes to the Organizer so it generates fewer, more focused topics
- The system should produce fewer but higher-quality posts rather than padding thin data into bad content

**Organizer produces very few topics (under 10):**
- This is acceptable for small or new communities
- Proceed normally; even 2 batches (10 posts) has value
- Note the lower count in the final report

**File write failures:**
- If a Content Producer reports it could not save files, check the output directory exists and has write permissions
- Retry once with the same prompt
- If still failing, alert the user with the specific error

---

## Core Principles

- **The slug is the most important ranking factor.** All slugs are verified unique by the Organizer Agent.
- **Answer first.** Put the most important information at the very start. Never bury the lead.
- **One blog, one specific topic.** "Dog Parks in Southern Highlands" not "Parks in Southern Highlands."
- **No filler.** Every sentence must serve the reader.
- **Facts only.** All information must be verifiable from official or reputable sources.
- **Unlimited posts per community.** A single neighborhood can have 50-100+ posts.
- **Internal linking.** Every post includes 3 related blog links using the Slug Registry.
- **Ryan Rose positioning.** Naturally woven in as local expert, never forced or salesy.
- **Source attribution.** Every post cites its sources. No fabricated URLs.
- **Fully autonomous.** Once started, run through all waves without stopping to ask the user.
- **Quality over quantity.** If research is thin, produce fewer posts rather than padding bad content.
