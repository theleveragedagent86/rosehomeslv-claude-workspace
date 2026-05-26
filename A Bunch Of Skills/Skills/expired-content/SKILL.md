---
name: expired-content
description: "Use when someone asks to create expired listing blog posts, generate content for expired listings, write blogs targeting homeowners whose listings didn't sell, or run the expired content workflow."
argument-hint: "[general, spreadsheet path, or neighborhood/area name]"
---

## What This Skill Does

Creates SEO-optimized blog posts targeting homeowners whose listings didn't sell. Uses a multi-agent orchestration system identical to the blog-writer skill but focused on expired listing content. Builds topical authority for Ryan Rose as the expert who helps sellers relist and sell homes that failed the first time.

**Website:** www.rosehomeslv.com
**Landing Page:** www.rosehomeslv.com/why-it-didnt-sell
**Blog Index:** www.rosehomeslv.com/blogs
**Expert/Author:** Ryan Rose, Las Vegas Real Estate Expert
**Blog Category:** Home Didn't Sell

**Supporting files in this skill directory:**
- [research-agent.md](research-agent.md) — Research Agent instructions
- [organizer-agent.md](organizer-agent.md) — Organizer Agent instructions
- [content-producer.md](content-producer.md) — Content Producer Agent instructions
- [templates.md](templates.md) — Blog post structure and SEO package format
- [content-rules.md](content-rules.md) — Content verification and formatting rules
- [seo-guidelines.md](seo-guidelines.md) — SEO/AEO/GEO strategy

---

## Language Strategy: Homeowner-First Vocabulary

**Critical rule for ALL agents:** Homeowners do NOT search "expired listing." That is realtor jargon. The majority of post titles, slugs, H2 headers, and body copy must use **homeowner language**. The term "expired listing" should appear sparingly (~20% of posts) for exact-match SEO coverage.

### Homeowner search phrases (USE THESE)
- "my house didn't sell"
- "why isn't my house selling"
- "home won't sell"
- "no offers on my home"
- "house sat on market too long"
- "took my house off the market"
- "relisting my home"
- "home didn't get any offers"
- "house back on market"
- "switching real estate agents"
- "home not selling what to do"
- "how to sell a home that didn't sell"

### Realtor jargon (USE SPARINGLY — ~20% of posts max)
- "expired listing"
- "days on market" / "DOM"
- "listing agreement"
- "MLS status"

---

## Architecture

You are the **Manager**. You orchestrate three types of sub-agents:

1. **Research Agent** (1 instance) — Gathers factual data about expired listings, market conditions, and area-specific info
2. **Organizer Agent** (1 instance) — Creates topics, batches, geo-tier assignments, and the Slug Registry
3. **Content Producers** (up to 5 per wave, parallel) — Each writes a batch of 5 posts + SEO package

**You never write blog posts yourself.** You only orchestrate, track progress, and save the master topic list.

---

## Invocation Modes

The skill supports 3 modes based on the argument passed:

### Mode 1: `/expired-content general`
Generates ALL foundation + geo-modified posts:
- ~10 foundation posts (no geo modifier)
- ~15 Tier 1 city posts (Las Vegas, Henderson, North Las Vegas)
- ~60 Tier 2 area posts (Summerlin, Southern Highlands, Mountains Edge, etc.)
- **Total: ~85 posts**

### Mode 2: `/expired-content [spreadsheet path]`
Reads an expired listings spreadsheet/CSV, extracts unique neighborhoods, generates Tier 3 neighborhood-specific posts:
- Parses the subdivision/neighborhood column
- Includes ALL neighborhoods (even those with only 1 expired listing)
- Deduplicates against Tier 1/2 areas
- **Total: ~30-50 posts depending on data**

### Mode 3: `/expired-content [neighborhood/area name]`
Generates expired-specific posts for a single neighborhood or area:
- 1-3 posts for the specified area
- Uses homeowner language titles

---

## Geo-Modifier Strategy

### Tiered geo targeting
Core homeowner topics get geo-modified versions at multiple levels:

**Tier 1 — Cities:** Las Vegas, Henderson, North Las Vegas
**Tier 2 — Major areas:** Summerlin, Southern Highlands, Mountains Edge, Centennial Hills, Skye Canyon, Aliante, Inspirada, Cadence, Anthem, Green Valley, Lake Las Vegas, Rhodes Ranch, Tuscany Village, Providence, Summerlin South
**Tier 3 — Neighborhoods/subdivisions:** Extracted from expired spreadsheet data

### Which topics get geo variants
- **High-value topics** (5-8 core topics) get Tier 1 + Tier 2 variants
  - e.g., "Why Your [Area] Home Isn't Selling", "Home Didn't Sell in [Area]. What to Do Next"
- **Medium-value topics** get Tier 1 only
  - e.g., "How to Choose a New Agent in [City]"
- **Niche/educational topics** stay general (no geo variant)
  - e.g., "What Does It Mean When a Listing Expires?" — universal content

### Content differentiation
Geo-modified posts are NOT just find-and-replace. Each geo variant must include:
- Area-specific market context (median price, average DOM, market conditions)
- At least 1 area-specific detail (local market trend, seasonal pattern, characteristic)
- Area name in slug, title, H1, meta description

---

## Workflow

### Step 0: Initialize

Determine the invocation mode from the argument. Set the output directory:
```
/Users/ryanrose/Downloads/Claude/Claude Blogs/EXPIRED LISTINGS/
```

Create the directory if it does not exist.

---

### Step 1: Spawn Research Agent

Read the file `research-agent.md` from this skill directory.

Use the **Agent tool** to spawn a single `general-purpose` sub-agent with this prompt structure:

```
You are a Research Agent for the expired-content system.

[FULL CONTENTS OF research-agent.md]

Mode: [general / spreadsheet / single area]
Area to research (if applicable): [AREA NAME]

Return your findings in the exact structured format specified in the instructions.
```

Wait for the Research Agent to complete. Store its entire output as `RESEARCH_DATA`.

---

### Step 2: Spawn Organizer Agent

Read the file `organizer-agent.md` from this skill directory.

Use the **Agent tool** to spawn a single `general-purpose` sub-agent with this prompt structure:

```
You are an Organizer Agent for the expired-content system.

[FULL CONTENTS OF organizer-agent.md]

Here is the research data to organize:

[RESEARCH_DATA]

Mode: [general / spreadsheet / single area]
Geo Tier: [which tiers to generate for]

The existing blog files directory to check for slug conflicts: /Users/ryanrose/Downloads/Claude/Claude Blogs/
The live website to check for slug conflicts: https://www.rosehomeslv.com/blogs/

Create the master topic list, batch assignments, and verified Slug Registry.
```

Wait for the Organizer Agent to complete. Store its output as `ORGANIZED_DATA`.

Save the master topic list to the output directory as `master-topic-list.md`.

Briefly display to the user: the total topic count, total batch count, and batch theme names. Then immediately proceed to Step 3.

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

2. For each batch in the wave, spawn a **Content Producer agent** using the Agent tool with `general-purpose` type. Use this prompt structure for each:

```
You are a Content Producer Agent for the expired-content system.

[FULL CONTENTS OF content-producer.md]

=== YOUR ASSIGNMENT ===

Topic Area: Expired Listings / Home Didn't Sell
Geo Area (if applicable): [AREA NAME or "General"]
Batch Number: [B]
Post Number Range: [start]-[end] (e.g., posts 6-10)

Your 5 Topics:
[Topic table for this batch from ORGANIZED_DATA — post number, title, slug, category]

=== SLUG REGISTRY (for internal linking) ===

[FULL Slug Registry table from ORGANIZED_DATA — all topics, all batches]

=== RESEARCH DATA ===

[Relevant sections of RESEARCH_DATA for this batch's topics]

=== CONTENT RULES ===

[FULL CONTENTS OF content-rules.md]

=== TEMPLATES ===

[FULL CONTENTS OF templates.md]

=== SEO GUIDELINES ===

[FULL CONTENTS OF seo-guidelines.md]

=== LANDING PAGE CTA (REQUIRED IN EVERY POST) ===

Place a prominent H2 section immediately after the opening hook. Link to www.rosehomeslv.com/why-it-didnt-sell with curiosity-driven wording. Rotate these variations across posts:

- "Find Out Exactly Why Your Home Didn't Sell"
- "What Your Last Agent Won't Tell You About Why It Didn't Sell"
- "The Real Reasons Your Las Vegas Home Is Still on the Market"
- "Get Your Free Listing Autopsy Before You Relist"
- "Before You Hire Another Agent, Read This"

Example:
<h2>Find Out Exactly Why Your Home Didn't Sell</h2>
<p>Most homeowners never get a straight answer. Ryan Rose offers a <a href="https://www.rosehomeslv.com/why-it-didnt-sell">free Home Sale Diagnostic</a> that breaks down exactly what went wrong and how to fix it. No pressure, no obligation.</p>

This is IN ADDITION TO the 3 related blog links at the bottom and the standard CTA section.

=== SOURCE ATTRIBUTION ===

At the bottom of every post, add 1-2 source citations in small italic text.
Format: <p style="font-size: 0.85em; font-style: italic;">Source: <a href="[url]">[Source Name]</a></p>

=== FOOTER LINKS ===

Include in the Call to Action section:
- Contact: https://www.rosehomeslv.com/contact
- Home Worth: https://www.rosehomeslv.com/home-worth

=== OUTPUT DIRECTORY ===

Save all files to: [OUTPUT DIRECTORY PATH]

Write all 5 posts and the SEO package, save them as files, and return your summary.
```

3. **Spawn ALL batch agents for this wave in a single response** (parallel Agent tool calls). This is critical for performance — do NOT spawn them one at a time.

4. Wait for all agents in the wave to complete.

5. Verify the expected output files exist by checking the output directory.

6. Display a brief progress summary:
```
Wave [X] complete: [N] posts written (posts [start]-[end])
Total progress: [completed]/[total] posts
```

7. **Immediately proceed to the next wave.** Do NOT ask the user for permission.

---

### Step 4: Final Report + ZIP

After all waves are complete:

1. Display:
```
Blog writing complete:
- Total posts: [N]
- Total batches: [B]
- SEO packages: [B]
- Master topic list: master-topic-list.md
- All files saved to: [OUTPUT DIRECTORY PATH]
```

2. Create a ZIP file containing all output:
```bash
cd "[OUTPUT DIRECTORY]" && zip -r expired-listings-content.zip *.html *.md
```

3. Display the ZIP file path.

---

### Error Handling

If a Content Producer agent fails (returns an error or does not produce expected files):

1. **Automatically retry** that batch by spawning a new Content Producer with the same prompt
2. Allow up to **2 retry attempts** per batch
3. Only alert the user if a batch fails after 2 retries
4. Continue with remaining waves regardless of individual batch failures

---

## Core Principles

- **Homeowner language first.** Write for frustrated sellers, not real estate agents.
- **The slug is the most important ranking factor.** All slugs are verified unique by the Organizer Agent.
- **Answer first.** Put the most important information at the very start. Never bury the lead.
- **One blog, one specific topic.** Keep posts focused.
- **No filler.** Every sentence must serve the reader.
- **Facts only.** All information must be verifiable.
- **Landing page CTA in every post.** Drive traffic to www.rosehomeslv.com/why-it-didnt-sell.
- **Internal linking.** Every post includes 3 related blog links using the Slug Registry.
- **Ryan Rose positioning.** Expert in selling homes that didn't sell the first time. Never forced or salesy.
- **Blog category:** "Home Didn't Sell" for all posts.
- **Fully autonomous.** Once started, run through all waves without stopping to ask the user.
- **ZIP output.** Bundle all files into a .zip at the end.
