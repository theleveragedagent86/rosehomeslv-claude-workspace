---
name: digital-cannonball
description: Use when someone asks to create a digital cannonball, generate a prospecting page for an expired listing, build a cannonball page for a property, create a digital marketing pitch for an expired homeowner, or make an online version of the cannonball mailer.
argument-hint: "required: property address (e.g., 9270 Swift Current Dr Las Vegas NV 89178)"
---

## What This Skill Does

Generates a personalized, self-contained HTML prospecting page for an expired or off-market listing. The page includes a property analysis with hero photo, listing history timeline, marketing comparison, comparable sales data, market conditions, a 12-step relaunch plan, and Ryan's contact info. Output is a single `index.html` file that can be texted or emailed to the homeowner.

**Agent:** Ryan Rose
**Brokerage:** Real Broker, LLC
**Phone:** 702-747-5921
**Email:** ryan@rosehomeslv.com
**Website:** rosehomeslv.com

**Supporting files in this skill directory:**
- [research-agent.md](research-agent.md) — Property Research Agent instructions
- [content-writer.md](content-writer.md) — Content Writer Agent instructions
- [html-generator.md](html-generator.md) — HTML Generator Agent instructions
- [html-template.md](html-template.md) — Full HTML/CSS/JS template with placeholders
- [content-rules.md](content-rules.md) — Voice, tone, and formatting rules
- [design-tokens.md](design-tokens.md) — CSS design system reference

---

## Architecture

You are the **Manager**. You orchestrate three sub-agents across three sequential waves:

1. **Research Agent** — Searches Zillow for the property, extracts all listing data, photos, price history, comps, and market stats
2. **Content Writer Agent** — Generates all narrative text sections using the research data
3. **HTML Generator Agent** — Assembles the final HTML page from the template + research data + written content

**You never write content or HTML yourself.** You orchestrate, validate, and assemble.

---

## Workflow

### Step 0: Initialize

1. Parse `$ARGUMENTS` for the property address. If no address is provided, ask the user for one and stop.

2. Normalize the address into a URL-safe slug for the folder name:
   - Lowercase
   - Replace spaces with hyphens
   - Remove commas, periods, and special characters
   - Example: "9270 Swift Current Dr Las Vegas NV 89178" → "9270-swift-current-dr-las-vegas-nv-89178"

3. Set the output directory:
   ```
   /Users/ryanrose/Downloads/Claude/Digital Cannonballs/[address-slug]/
   ```
   Create this directory if it does not exist.

4. Read ALL supporting files from this skill directory and store each as a variable:
   - `RESEARCH_INSTRUCTIONS` ← contents of research-agent.md
   - `CONTENT_WRITER_INSTRUCTIONS` ← contents of content-writer.md
   - `HTML_GENERATOR_INSTRUCTIONS` ← contents of html-generator.md
   - `HTML_TEMPLATE` ← contents of html-template.md
   - `CONTENT_RULES` ← contents of content-rules.md
   - `DESIGN_TOKENS` ← contents of design-tokens.md

---

### Step 1: Spawn Research Agent (Wave 1 — sequential, blocking)

Spawn a single `general-purpose` agent with this prompt:

```
You are the Property Research Agent.

## Your Instructions
[Paste RESEARCH_INSTRUCTIONS here]

## Property Address
[The address from $ARGUMENTS]

## Today's Date
[Current date in YYYY-MM-DD format]

Go. Search for this property on Zillow and extract all data as specified in your instructions.
```

**Wait for the agent to complete.** Store the output as `RESEARCH_DATA`.

**Validation gate:** Before proceeding, confirm the research data contains at minimum:
- Property address (confirmed found on Zillow, Realtor.com, or Redfin)
- Beds and baths
- List price or last known price
- At least one photo URL (from any of the three portals)

If all three photo URLs are missing, proceed anyway (the template has a gradient fallback). If the address itself was not found on any source, stop and tell the user: "I could not find this property on Zillow, Redfin, or Realtor.com. Please provide a direct URL to the listing."

Save the research data to `[OUTPUT_DIR]/research-data.md` for reference.

---

### Step 2: Spawn Content Writer Agent (Wave 2 — sequential, blocking)

Spawn a single `general-purpose` agent with this prompt:

```
You are the Content Writer Agent for a digital cannonball prospecting page.

## Your Instructions
[Paste CONTENT_WRITER_INSTRUCTIONS here]

## Content Rules
[Paste CONTENT_RULES here]

## Research Data
[Paste RESEARCH_DATA here]

Write all sections as specified in your instructions. Return the complete structured output.
```

**Wait for the agent to complete.** Store the output as `CONTENT_DATA`.

**Validation gate:** Confirm the content includes at minimum:
- OVERVIEW_LEDE
- MARKETING_HEADLINE
- DEMAND_HEADLINE
- PLAN_STEPS (12 steps in 4 acts)
- CONTACT_HEADLINE

If any critical section is missing, ask the content writer to regenerate it.

---

### Step 3: Spawn HTML Generator Agent (Wave 3 — sequential, blocking)

Spawn a single `general-purpose` agent with this prompt:

```
You are the HTML Generator Agent for a digital cannonball prospecting page.

## Your Instructions
[Paste HTML_GENERATOR_INSTRUCTIONS here]

## HTML Template
[Paste HTML_TEMPLATE here — the full template from html-template.md, including the code block markers]

## Design Tokens
[Paste DESIGN_TOKENS here]

## Research Data
[Paste RESEARCH_DATA here]

## Written Content
[Paste CONTENT_DATA here]

## Output Directory
[OUTPUT_DIR path]

Replace every {{PLACEHOLDER}} token in the template with the corresponding data from the research and written content. Build all HTML fragments (timeline items, comp rows, listed-vs-launched items, plan acts). Save the final file to [OUTPUT_DIR]/index.html.
```

**Wait for the agent to complete.**

---

### Step 4: Verify and Report

1. Confirm `index.html` exists in the output directory:
   ```bash
   ls -la "[OUTPUT_DIR]/index.html"
   ```

2. Check file size (should be 15-60 KB for a typical page):
   ```bash
   wc -c "[OUTPUT_DIR]/index.html"
   ```

3. Scan for leftover placeholders:
   ```bash
   grep -c '{{' "[OUTPUT_DIR]/index.html"
   ```
   If any `{{` tokens remain, report them as warnings.

4. Report to the user:
   ```
   Digital cannonball complete!

   Property: [Full address]
   Output: [OUTPUT_DIR]/index.html
   File size: [X KB]

   To preview, start the local server and open:
   http://localhost:8091/Digital%20Cannonballs/[slug]/index.html

   Or open the file directly in a browser.
   ```

---

## Error Handling

| Error | Action |
|-------|--------|
| Property not found on Zillow | Search MLS Matrix by address instead. Ask user for a direct URL if both fail. |
| MLS Matrix not logged in | Stop and tell user: "MLS Matrix is not logged in. Please log in at las.mlsmatrix.com and try again." |
| MLS listing not found by number | Try searching by address on MLS Matrix dashboard. The MLS number might be wrong. |
| No photo URL found | Proceed; template has gradient fallback |
| No comps found | Proceed; template shows "No comparable sales data available" |
| Market stats not found | Proceed; template shows "N/A" for missing stats |
| Content writer missing sections | Re-spawn content writer with specific missing sections |
| HTML generator leaves placeholders | Report as warnings; user can edit manually |
| Output directory creation fails | Ask user to create it manually |
| WebFetch returns 403 on Zillow | Expected. Use the browser (Claude in Chrome) instead. See research-agent.md Step 2. |
| Zillow hero image is Street View | Use MLS Matrix photo instead (Step 2b). Street View URLs break outside Zillow. |
| JavaScript image extraction blocked | Do NOT use JavaScript to extract image URLs. Always use right-click > "Open image in new tab". |

---

## Known Issues Log

These are problems encountered during development. They are documented here so the agents do not repeat the same mistakes.

### 1. Zillow blocks all non-browser access (403)
**Problem:** WebFetch on any Zillow URL returns HTTP 403.
**Solution:** Always use Claude in Chrome browser tools (navigate, read_page, javascript_tool, screenshot) to extract data from Zillow. Never use WebFetch for Zillow.

### 2. Hero photo extraction is tricky for off-market properties
**Problem:** Off-market properties on Zillow show a Google Street View image as the hero. The image URL is a Google Maps API call with Zillow's domain-restricted API key and signed signature. This URL:
- Returns 403 when fetched via curl or WebFetch
- Returns 403 when navigated to directly in a browser tab
- Cannot be extracted via JavaScript (blocked as cookie/query string data)
- Cannot be exported via canvas (CORS tainted canvas error)

**Solution (primary):** Use MLS Matrix (las.mlsmatrix.com) to get the actual MLS listing photos. The research agent searches by MLS number in Step 2b, opens the Photos tab, clicks the first photo full-size, then right-clicks > "Open image in new tab" to get a direct URL from `media.las.mlsmatrix.com`. These URLs work in any `<img>` tag.

**Solution (fallback):** If MLS Matrix is unavailable (session expired, listing not in LVR), right-click the hero image on Zillow, select "Open image in new tab." Use that URL as-is, but note it may not work for off-market Street View images.

### 4. MLS Matrix as primary photo source
**Problem:** Zillow, Realtor.com, and Redfin all strip MLS listing photos from off-market/expired properties, leaving only satellite or Street View images. Realtor.com and Redfin are also blocked by Claude's browser safety restrictions and bot protection.
**Solution:** MLS Matrix retains the original MLS listing photos for all LVR listings regardless of status. The research agent now uses MLS Matrix (Step 2b) as the primary photo source. Ryan keeps his MLS session logged in so the agent can access it directly.

### 5. JavaScript image extraction is blocked
**Problem:** Using `javascript_tool` to extract image `src` attributes returns `[BLOCKED: Cookie/query string data]` because MLS image URLs contain query parameters that trigger the filter.
**Solution:** Always use the right-click > "Open image in new tab" method. The URL appears in the new tab's address bar and can be read from the tab context. Never attempt JS-based image URL extraction.

### 3. Side navigation section numbering
**Problem:** The nav originally had 7 items (01-07) with the hero as item 01. This caused a mismatch: clicking nav "02" jumped to the Overview section (which is labeled "01 / Overview" on the page).
**Solution:** Nav has 6 items (01-06) matching the 6 content sections. The hero section is not in the nav. This is already fixed in the template.

---

## Notes

- This skill produces a static HTML file. It does not require a server to function (can be opened as a local file), but fonts load best when served over HTTP.
- The page is designed to be shared via text message or email as a URL. Host it on any static file server, or share the HTML file directly.
- Each run creates a new folder under `Digital Cannonballs/`. Previous runs are not overwritten.
- The page includes `noindex, nofollow` meta tags to prevent search engine indexing.
