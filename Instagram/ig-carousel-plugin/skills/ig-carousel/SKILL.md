---
name: ig-carousel
description: Use when someone asks to create Instagram carousel content, build a monthly carousel, create a C&C carousel, make a Coffee and Contracts post, build a monthly Las Vegas guide carousel, create Instagram slide content, or create content for a specific calendar date (e.g. "do May 3rd"). Looks up the matching Canva template via Claude in Chrome (cowork) when a date is provided.
argument-hint: "month name, specific date, or Canva template link (e.g., 'June 2026' or 'May 3 2026')"
---

## What This Skill Does

Creates copy-paste-ready content for Instagram carousel posts from Coffee & Contracts monthly Canva templates. Researches real Las Vegas events, restaurant openings, seasonal activities, and verified housing market stats, then outputs a slide-by-slide markdown document with an IG caption.

**Account:** @rosehomeslv
**Website:** rosehomeslv.com
**Expert:** Ryan Rose, Las Vegas Real Estate Expert

**Supporting files in this skill directory:**
- [research-events.md](research-events.md) — Events Research Agent instructions
- [research-local.md](research-local.md) — Local Openings/Lifestyle Research Agent instructions
- [research-market.md](research-market.md) — Housing Market Stats Research Agent instructions
- [content-assembler.md](content-assembler.md) — Content Assembler Agent instructions
- [caption-writer.md](caption-writer.md) — Caption Writer Agent instructions
- [slide-templates.md](slide-templates.md) — Exact output format per slide type
- [cc-monthly-template-map.md](cc-monthly-template-map.md) — Default C&C slide map and type registry
- [content-rules.md](content-rules.md) — Content rules for carousel output

**Cowork dependency (Daily Post Mode):** Daily Post Mode uses Claude in Chrome MCP tools (`mcp__Claude_in_Chrome__*`) to navigate the user's Canva projects folder, open the matching template, and read the actual slide placeholders. Requires Claude in Chrome connected to a browser session signed into canva.com.

---

## Architecture

You are the **Manager**. You orchestrate five sub-agents:

1. **Events Research Agent** — Finds 10+ verified Las Vegas events for the target month
2. **Local Research Agent** — Finds restaurant/business openings and bucket list items
3. **Market Stats Research Agent** — Pulls verified housing market statistics with sources
4. **Content Assembler Agent** — Formats research into slide-by-slide copy-paste blocks
5. **Caption Writer Agent** — Writes the Instagram caption

**You never write slide content or captions yourself.** You orchestrate, validate, and assemble the final output file.

The skill operates in two modes, decided in Step 0:

- **Monthly Guide Mode** — Build the full "In Las Vegas Guide" carousel (events, openings, market stats). All five sub-agents run.
- **Daily Post Mode** — Generate content for a single calendar date (e.g. "May 3"). The skill reads the monthly Template Links spreadsheet, uses Claude in Chrome (cowork) to open the matching Canva template from the user's Canva projects folder, reads the actual placeholders in that template, then generates copy that fits. Research agents only run if the post type calls for fresh data (e.g. "Neighborhood Roundup", "Local Guide").

---

## Workflow

### Step 0: Initialize

1. Parse `$ARGUMENTS` to determine mode:
   - **Monthly Guide Mode** if input is a month name (e.g., "June", "June 2026") or a Canva template link with no date
   - **Daily Post Mode** if input is a specific date (e.g., "May 3", "May 3 2026", "do March 15", "the one for May 3rd")
   - If ambiguous or empty, ask the user.

2. Determine the target month and year. If only a month name is given, use the current year. Store as `TARGET_MONTH` (e.g., "June 2026"). For Daily Post Mode also store `TARGET_DATE` (e.g., "May 3 2026") and skip ahead to the **Daily Post Mode** section below after this step.

3. If a Canva link was provided (starts with `https://www.canva.com/`), store it as `CANVA_LINK`. Otherwise set `CANVA_LINK` to "not provided."

4. **(Monthly Guide Mode only)** Read `cc-monthly-template-map.md` from this skill directory.

5. **(Monthly Guide Mode only)** Present the default slide map to the user:

   ```
   The standard C&C Monthly Edit template uses these slides:

   Slide 13 — Cover
   Slide 16 — Events
   Slide 17 — New & Coming Soon
   Slide 18 — Bucket List
   Slide 21 — Housing Market
   Slide 22 — CTA / Closing

   Are these the right slide numbers for this month's template, or do I need to adjust any?
   ```

   Wait for confirmation. If the user provides different numbers, update the slide map. Store the confirmed map as `SLIDE_MAP`.

6. Set the output path:
   - **Monthly Guide Mode:** `/Users/ryanrose/Downloads/Claude/Instagram/Coffee and Contracts/[TARGET_MONTH] Carousel Content.md`
   - **Daily Post Mode:** `/Users/ryanrose/Downloads/Claude/Instagram/Coffee and Contracts/Daily Posts/[TARGET_MONTH] [DAY] [POST_TYPE].md` (create the `Daily Posts/` subdirectory if missing)

---

### Daily Post Mode: Look Up Calendar Entry and Open Canva Template via Cowork

This section runs only in **Daily Post Mode**. Skip to Step 1 if you're in Monthly Guide Mode.

#### D.1 — Read the calendar entry

1. Resolve the calendar spreadsheet path:
   ```
   /Users/ryanrose/Downloads/Claude/Instagram/Coffee and Contracts/[TARGET_MONTH] Template Links.xlsx
   ```
   Sheet name follows pattern `[TARGET_MONTH] Templates` (e.g., "May 2026 Templates").

2. Read the spreadsheet (use Python + openpyxl via Bash) and find the row matching `TARGET_DATE`. Extract:
   - `FORMAT` (column C: "Feed Post" or "Reel Template")
   - `POST_TYPE` (column D: e.g., "Personal Brand Builder", "Authority Builder", "Listing Feature")
   - `CONTENT_PILLAR` (column E: "Brand Authority", "Local & Relocation", "Listings & Neighborhoods")
   - `GO_TO_PAGE` (column F)
   - `CANVA_LINK` (column G)

3. If the row is missing or columns are blank/`TBD`, tell the user which fields are missing and ask whether to proceed with manual hints or stop.

#### D.2 — Open the matching Canva template via Claude in Chrome (cowork)

The user's Canva templates live in their Canva projects folder. Use Claude in Chrome MCP tools (`mcp__Claude_in_Chrome__*`) to find and open the right template.

1. **Check Claude in Chrome is connected.** Call `mcp__Claude_in_Chrome__list_connected_browsers`. If no browser is connected, tell the user: "Claude in Chrome isn't connected. Open Chrome with the Claude extension and reconnect, then re-run this." Stop.

2. **Resolve the Canva projects folder.** Check memory for a stored Canva projects URL (`reference_canva_projects_folder.md`). If not stored:
   - Ask the user once: "What's the URL of your Canva projects folder where the Coffee & Contracts templates live?"
   - Save the answer as a reference memory.

3. **Navigate.** Use `mcp__Claude_in_Chrome__navigate` to the projects folder URL.

4. **Locate the right design.**
   - For **Feed Posts**: If `CANVA_LINK` from the spreadsheet is a real URL (not "TBD"), navigate directly there. Otherwise use `mcp__Claude_in_Chrome__find` or `mcp__Claude_in_Chrome__get_page_text` to search the projects folder for a design titled something like "Coffee & Contracts [TARGET_MONTH]" or "C&C [TARGET_MONTH] Multi-Design". Click into it.
   - For **Reel Templates**: search for a design titled like "[POST_TYPE] Reel [TARGET_MONTH]" or "C&C Reel [TARGET_MONTH] [POST_TYPE]". The Reel template is a separate file referenced as "Reel (separate file)" in the calendar.
   - If multiple candidates, list the top 3 with thumbnails and ask the user to pick.

5. **Navigate to the correct page (Feed Posts only).**
   - Once inside the Canva editor, use `mcp__Claude_in_Chrome__javascript_tool` or `mcp__Claude_in_Chrome__find` to locate the page-number input at the bottom-right of the editor.
   - Enter `GO_TO_PAGE` and submit.
   - Confirm the page jumped by reading the page indicator.

6. **Capture the template.** Use `mcp__Claude_in_Chrome__preview_screenshot` (or `mcp__Claude_Preview__preview_screenshot` if that's what's connected) and `mcp__Claude_in_Chrome__get_page_text` to capture:
   - All visible text placeholders on the slide(s)
   - Any sticky-note prompts (yellow "Head to the AI prompt" notes)
   - The slide layout (single image vs. carousel, headline + body + CTA structure, etc.)
   - Number of pages in the design (if it's a multi-slide carousel)

   Store as `TEMPLATE_CONTEXT`.

#### D.3 — Generate copy that fits the actual template

1. Decide whether research agents are needed:
   - `Local Guide`, `Local Shareable`, `Neighborhood Roundup`, `Listing Roundup` → run **Local Research Agent** for that day's topic
   - `Authority Builder`, `Personal Brand Builder` → no research agent; pull from Ryan's brand voice and Las Vegas market context
   - `Listing Feature`, `Sold Case Study` → ask the user which listing/sale to feature
   - `Market Update` posts (if any) → run **Market Stats Research Agent**

2. Spawn the **Content Assembler Agent** with:
   - `TEMPLATE_CONTEXT` (the actual placeholders from Canva)
   - The post's `POST_TYPE` and `CONTENT_PILLAR`
   - Any research results from step D.3.1
   - The standard content rules (`content-rules.md`)
   - Instruction: produce copy that fits each placeholder in the captured template, slide by slide.

3. Spawn the **Caption Writer Agent** with the assembled slide content. The caption should match the post type and pillar.

4. Save the output to the Daily Post Mode output path from Step 0.

5. Final report should include: link to the Canva design, the template page number, and a paste-ready copy block.

---

### Step 1: Spawn Research Agents (parallel) — Monthly Guide Mode

Read these files from this skill directory:
- `research-events.md`
- `research-local.md`
- `research-market.md`
- `content-rules.md`

Spawn **three agents in parallel** using the Agent tool (all `general-purpose` type):

**Agent 1 — Events Research Agent:**

```
You are an Events Research Agent for the ig-carousel system.

[FULL CONTENTS OF research-events.md]

[FULL CONTENTS OF content-rules.md]

Target month: [TARGET_MONTH]
City: Las Vegas, NV

Return your findings in the exact structured format specified in the instructions. Use WebSearch and WebFetch to research. Be thorough, check multiple sources, and verify all dates.
```

**Agent 2 — Local Research Agent:**

```
You are a Local Research Agent for the ig-carousel system.

[FULL CONTENTS OF research-local.md]

[FULL CONTENTS OF content-rules.md]

Target month: [TARGET_MONTH]
City: Las Vegas, NV

Return your findings in the exact structured format specified in the instructions. Use WebSearch and WebFetch to research. Be thorough and verify all openings against official sources.
```

**Agent 3 — Market Stats Research Agent:**

```
You are a Housing Market Stats Agent for the ig-carousel system.

[FULL CONTENTS OF research-market.md]

[FULL CONTENTS OF content-rules.md]

Target month: [TARGET_MONTH]
City: Las Vegas, NV / Clark County

Return your findings in the exact structured format specified in the instructions. Use WebSearch and WebFetch to research. Cross-reference every stat across at least 2 sources. Never fabricate numbers.
```

Wait for all three agents to complete. Store outputs as `EVENTS_DATA`, `LOCAL_DATA`, `MARKET_DATA`.

**Validate research quality before proceeding:**
- **Events:** Confirm at least 10 events found with dates, times, and venues. If fewer than 10, note it in the final report but proceed.
- **Local openings:** Confirm at least 4 verified items. If fewer, note it but proceed.
- **Market stats:** Confirm these are all present with source citations: median sold price, days on market, list-to-sale ratio, inventory. If any stat is missing, flag it prominently. The user may need to pull from their own MLS access.

---

### Step 2: Spawn Content Assembler Agent

Read these files from this skill directory:
- `content-assembler.md`
- `slide-templates.md`

Spawn a single `general-purpose` agent:

```
You are a Content Assembler for the ig-carousel system.

[FULL CONTENTS OF content-assembler.md]

[FULL CONTENTS OF slide-templates.md]

SLIDE MAP (confirmed by user):
[SLIDE_MAP — list each slide number and its type]

RESEARCH DATA — EVENTS:
[EVENTS_DATA — full output from the Events Research Agent]

RESEARCH DATA — LOCAL OPENINGS & LIFESTYLE:
[LOCAL_DATA — full output from the Local Research Agent]

RESEARCH DATA — HOUSING MARKET:
[MARKET_DATA — full output from the Market Stats Research Agent]

Target month: [TARGET_MONTH]
City: Las Vegas
Canva link: [CANVA_LINK]
Contact info: Ryan Rose | Rose Homes LV | Real Broker, LLC | 702-747-5921 | rosehomeslv.com

Assemble the slide-by-slide content document following the templates exactly. No em-dashes. Every stat must cite its source.
```

Store output as `SLIDE_CONTENT`.

---

### Step 3: Spawn Caption Writer Agent

Read `caption-writer.md` from this skill directory.

Spawn a single `general-purpose` agent:

```
You are a Caption Writer for the ig-carousel system.

[FULL CONTENTS OF caption-writer.md]

SLIDE CONTENT (for context on what's in the carousel):
[SLIDE_CONTENT — full output from the Content Assembler]

Target month: [TARGET_MONTH]
City: Las Vegas
Account: @rosehomeslv

Write the Instagram caption following the structure and rules specified. No em-dashes. Stats and event details must match the slide content exactly.
```

Store output as `CAPTION`.

---

### Step 4: Assemble Final Output and Save

Combine everything into a single markdown file. Use this structure:

```markdown
# [TARGET_MONTH] — In Las Vegas Guide
## Copy-paste content for Canva slides [list slide numbers from SLIDE_MAP]

> Canva template: [CANVA_LINK]
> Generated: [today's date]
> Tip: in Canva, use Cmd+F to bulk replace `[City Name]` → `Las Vegas` and `[Previous Month]` → `[Month]`. Then paste the per-slide content below.

---

[SLIDE_CONTENT — all slides in order]

---

## CAPTION (for the post itself)

[CAPTION]

---

## SOURCES (for your own verification)

[Aggregate all source URLs from all three research agents into a single list, grouped by category: Events, Local/Dining, Housing Market]
```

Write this file to the output path set in Step 0.

---

### Step 5: Final Report

Display a summary to the user:

```
Carousel content ready for [TARGET_MONTH]:

📄 Output: [output file path]
🎨 Canva: [CANVA_LINK or "not provided"]
📊 Slides: [list of slide numbers and types]
🎟 Events: [count] verified
🍽 Openings: [count] verified
📈 Market stats: [status — "all verified with sources" or list any gaps]

[If any data quality flags exist:]
⚠️ Notes:
- [list flags, e.g., "Only 8 events found", "Days on market stat from single source"]

Next steps:
1. Open the Canva template
2. Cmd+F: replace [City Name] → Las Vegas
3. Cmd+F: replace [previous month] → [target month]
4. Paste each slide's content from the output file
5. Delete yellow "Head to the AI prompt" sticky notes
6. Choose a cover image ([suggestion from events research])
7. Pull fresh MLS stats day-of if you want zip-level accuracy
8. Post with the caption from the bottom of the file
```

---

## Core Principles

1. **Factual only.** Never fabricate events, stats, restaurant names, or dates. Mark anything unverified as `[NOT FOUND]`.
2. **No em-dashes.** This is the #1 formatting rule. Use commas, periods, or "and."
3. **Source everything.** Every market stat needs a source citation. Every event needs a verified date.
4. **Match the May 2026 format.** The output file should look identical in structure to `/Users/ryanrose/Downloads/Claude/Instagram/Coffee and Contracts/May 2026 Carousel Content.md`.
5. **Short text for Canva.** Slides have limited space. Events get 3 lines each. Bucket list items get 2-3 sentences. Market narrative gets 2 short paragraphs.
6. **Las Vegas focus.** All content is Las Vegas / Clark County. Henderson, Summerlin, Spring Valley, Centennial Hills, North Las Vegas, Skye Canyon, Green Valley, Boulder City.
