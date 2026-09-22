# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **New Construction Marketing Automation System** for Ryan Rose, a Las Vegas real estate agent. The `/new-construction [Community Name]` skill researches Clark County, NV communities and generates a complete marketing ecosystem via 10 specialized sub-agents across 6 execution waves, including auto-building the 3 Lofty CRM action plans via Cowork browser automation.

## Architecture

**Skill instructions:** `/Users/ryanrose/.claude/skills/new-construction/`
**Per-community outputs:** `/Users/ryanrose/Downloads/Claude/Rose Homes LV/Content/New-Construction/[community-slug]/`
**Shared blog folder (all communities):** `/Users/ryanrose/Downloads/Claude/Rose Homes LV/Content/New-Construction/all-blogs/`

### Execution Waves

| Wave | Agent(s) | Parallel? | Output |
|------|----------|-----------|--------|
| 1 | Research Agent | No | Research data (held in memory). Now also web-searches 3-5 nearby (1-3 mi) comparison communities for real numbers. |
| 2 | Comparison Analyst | No | Appended to `research-report.md`. Tightened comparison radius to 1-3 mi (was 15 mi). |
| 2.5 | SEO Strategist | No (sequential, blocking) | `seo-package.md` — feeds Wave 3 + Wave 4 with optimized titles, descriptions, OG/Twitter, JSON-LD |
| 3 | Social Content Creator, Buyer Guide Producer, Landing Page Developer, Smart Plan Architect, Blog Writer | Yes (all 5) | Per-community files + blog mini-series (main + per-plan) in shared folder |
| 4 | Master Page Developer | No | `master-landing-page.html` (full rebuild, noir v3 theme) |
| 5 | Lofty Smart Plan Specialist | No | Lofty CRM action plans created via Cowork browser automation (no file output, status report only) |

The Manager (SKILL.md) reads all 16 instruction/template files in Step 0, passes them to each sub-agent, and never writes content directly. The SEO Strategist's output flows into the Buyer Guide Producer, Landing Page Developer, Blog Writer, and Master Page Developer so every HTML page has expert-tuned titles, descriptions, OG/Twitter tags, and JSON-LD schema.

### Key Files

- **SKILL.md** — Orchestrator: defines wave execution, agent spawning, error handling
- **new-construction-reference.md** — Shared market data: builder rankings, pricing, SID/LID, legislation, blog slugs
- **voice-samples.md** — Tone directive used by all content-producing agents
- **smart-plan-template.md** / **landing-page-template.md** — Structure templates for their respective agents
- **buyer-guide-pdf-template.md** — Buyer guide PDF template (inverted light, Delamar pattern)
- **builder-brand-colors.md** / **builder-brand-colors.html** — Canonical accent-color lookup for every active Clark County builder. Markdown for agents; HTML for human visual swatch reference.
- **DO.BBRA - Template/Duties Owed and BBRA.pdf** — Universal PDF attachment for Day 0 smart plan email
- **lofty-smart-plan-specialist.md** — Wave 5 Cowork browser automation agent that builds the 3 action plans directly in Lofty CRM (replaces the previous manual paste of `cowork-build-prompt.md`)

### Per-Community Output (8 files in `[community-slug]/`)

1. `research-report.md` — Research + comparison tables (now includes Section 9: Comparison Communities with real data for 3-5 nearby builds)
2. `seo-package.md` — Optimized titles, meta descriptions, keywords, OG/Twitter, JSON-LD schema for every HTML page produced
3. `social-content.md` — 2 long-form transcripts + 10–12 short scripts. EVERY video has its own Platform Copy block: TikTok description, YouTube description, YouTube tags (≤475 chars), Instagram caption with up to 5 hashtags. All videos posted on YouTube + TikTok + Instagram + Reddit.
4. `buyer-guide.html` — Buyer guide for PDF export (inverted light, Delamar pattern, jazzed-up roadmap timeline). Also serves as the web version of the guide.
5. `buyer-guide.pdf` — Auto-generated PDF, attached to Day 0 email
6. `landing-page.html` — Lofty-compatible, self-contained HTML with lead capture + floor plan zoom lightbox
7. `smart-plan.md` — 30-day Lofty CRM blueprint (3 tracks, 16 touches, Day 35 handoff to Long Term Nurture)
8. `cowork-build-prompt.md` — Backup manual prompt for Cowork (Wave 5 normally automates this end-to-end)

### Blog Mini-Series (in shared `all-blogs/` folder)

- **Main community blog:** `[community-slug].html` (the hub — links inline to each per-plan mini-blog)
- **Per-plan mini-blogs:** `[community-slug]-[plan-slug].html` (one per floor plan, links inline back to main + landing page)
- All communities write into the same folder so the publishing terminal command can push every blog in one pass
- Cross-linking is mandatory: main ↔ each plan blog ↔ landing page + master directory

## Lead Flow & CRM Integration

- Landing page form uses hidden tag `[community-slug]` (no prefix)
- Tag triggers Lofty smart plan: Hot (ASAP + pre-approved), Warm (default/landing page), Nurture (browsing)
- Day 0 email includes DO/BBRA PDF attachment + buyer guide PDF attachment
- Day 0 email links to `buyer-guide.html` (light/PDF-source web version) when a buyer guide URL is included
- Day 0 notification email to ryan@rosehomeslv.com with builder rep draft to copy/paste
- Day 35: auto-triggers existing "Long Term Nurture - Buyer" plan (loops indefinitely)
- All emails end with `#signature#` (Lofty auto-inserts), never hardcoded sign-offs
- Smart plan creation in Lofty is now handled by the **Wave 5 Lofty Smart Plan Specialist** agent, which uses Cowork to drive the Lofty UI directly. `cowork-build-prompt.md` remains as a manual backup if Wave 5 fails.

## Content Rules

- **Clark County, Nevada only** — reject other locations
- **No em-dashes** — use commas, periods, or "and"
- **No fabricated data** — mark gaps as "NOT FOUND"
- **6th grade reading level**, professional but warm tone
- **Texts under 300 characters**, end with a question
- **Landing page HTML** must be self-contained (no external CSS/JS except Google Fonts), Lofty-compatible
- **Design system:** Cream/editorial theme (`#faf8f3` soft off-white background, `#2a2520` warm-charcoal text), Bebas Neue + Inter fonts, builder-specific accent colors (e.g. Pulte `#1b75a1` blue + `#003048` navy). White-knockout Real Broker logo gets `filter: invert(1)` to render dark on cream. Hero uses scrolling lifestyle image strip behind a cream-tinted overlay (rgba(250,248,243,0.85)) so dark text stays readable while photos add ambient texture.
- **Buyer guide PDF** uses inverted light theme (white background, dark text). Canonical reference: `delemar-by-pulte/buyer-guide.html` — single-line `.headline` titles, `.plan-card` floor-plan structure with explicit print break controls.

## Agent Contact Info

- **Ryan Rose** | Real Broker, LLC | 702-747-5921 | ryan@rosehomeslv.com | rosehomeslv.com
- New construction builder commission rate: 4%

## The New Construction HUB (separate from per-community pages)

Lives in `new-construction-hub/`. A different animal from everything else in this folder. The
per-community pages above are single-builder, short, and use one builder `--accent`. The hub is
the **top-of-funnel authority page** for the whole valley: 20 builders, 7 areas, 21 sections,
5 tables, a 22-item sticky table-of-contents rail. Target slug `/las-vegas-new-construction`.

**Slug history, this matters for SEO:** the hub it replaces is live at `/new-construction-hub`
and has been indexed since August 2026. Moving to `/las-vegas-new-construction` needs a 301
redirect from the old slug, or the existing rankings are thrown away. If Lofty has no redirect
feature, publish the new page and leave a short stub at the old slug linking to it. Every
internal link in the workspace was repointed to the new slug on 2026-09-15.

### It ships as TWO embeds, not one

| File | Where it goes |
|---|---|
| `part-1-above-listings.html` | Lofty HTML module **above** the Featured Listings block |
| *(Lofty's native Featured Listings block, built in Lofty's editor)* | between them |
| `part-2-below-listings.html` | Lofty HTML module **below** the Featured Listings block |
| `_preview-stitched.html` | local preview only. Never paste this. Regenerate it after editing either part. |

Why: Lofty's featured-listings block is native and cannot render inside a custom HTML embed,
so the page has to be cut around it. There is no single-file version any more, on purpose. One
source of truth per artifact, so the two halves cannot drift.

**Consequences of the split, all handled, do not "fix" them:**
- **Each embed carries its own rail.** A sticky element cannot escape its own embed's
  container, so one rail cannot span both halves. Two identical rails at the same `--rail-top`
  read as one continuous panel. The first scrolls away as the listings block arrives, the
  second picks up at the same offset.
- **The script is duplicated in both embeds**, guarded by `window.__rhHubInit` so the second
  copy is a no-op, and deferred to `DOMContentLoaded` so whichever copy runs first still sees
  both embeds and wires up both rails.
- **The `<style>` block is duplicated too.** Deliberate, so each embed renders correctly on
  its own if the other fails to load or gets reordered.
- **Part 2's rail uses `rh-toc-title-2`** so the two embeds do not collide on one id.
- The spy re-measures on `window.load`, because Lofty's listing images change page height
  after load and move every heading below them.

### Brand

Tokens come from the **SKOOL Brandkit, "Vector" palette**, which is the source of truth:
`SKOOL Community/Brandkit/Brand-Guide/tokens.css` (v2.0 "Vector"). Do not invent colors here,
and do not reintroduce the Rose Homes Brandkit navy/champagne-gold/Playfair/Montserrat system.
That earlier palette was replaced on this page by Ryan's direction.

**Note:** `SKOOL Community/Brandkit/CLAUDE.md` describes Vector as the Leveraged Agent (Skool)
brand and says not to mix it with the Rose Homes realtor brand. Ryan directed Vector here
anyway, same as on the Rose Homes CEO dashboard. Follow the direction, do not "correct" it.

**The three rules of Vector, do not break them:**
1. **ONE accent, ONE value.** `#1768E5` works as a fill AND as text on white. Never add a
   second accent.
2. **Black is a SURFACE, never a text color.** The pop is structural: a full-bleed true-black
   band butted against white. Body ink is `#050E3D`, not black.
3. **NO warm colors.** No cream, no gold, no sage, no orange.

| Token | Value | Use |
|---|---|---|
| `--dark` / base surface | `#FFFFFF` | primary surface |
| `--dark-surface` | `#F7F8FA` | sunken fill, table rows, rail panel |
| `--inv` | `#000000` | inverted SURFACE only (hero, CTA band) |
| `--line` | `#E4E7EF` | hairlines |
| `--structure` | `#0B3FA8` | structural fills, the hero slab, button hover |
| `--text-dark` / `--text-body` | `#050E3D` | primary text on white, 18.48:1 |
| `--text-meta` | `#55627F` | secondary text, 6.11:1 |
| `--ink-inv` | `#FFFFFF` | text on black, 21:1 |
| `--ink-2-inv` | `#9AA3BC` | secondary text on black, 8.34:1 |
| `--accent` | `#1768E5` | fills, buttons, links. White on it is 5.06:1 |
| `--accent-inv` | `#5B9BFF` | accent AS text on black, 7.58:1 |

**Type is Barlow 800 (display and headings, tracking -0.028em) + Raleway 600 (labels,
eyebrows, stat labels, tracking 0.15em) + Inter (body, line-height 1.6).** Google Fonts URL:

```
https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&family=Raleway:wght@400;500;600;700&display=swap
```

Playfair Display, Montserrat and Bebas Neue are NOT used here. If you see Bebas in
`~/.claude/skills/new-construction/landing-page-template.md`, that template predates this.

### The hero

**White background, photo on the right that DISSOLVES into the page.** No dark panel, no scrim
over the photo, no hard edge anywhere. Ryan rejected three earlier versions in this order:
a blue gradient wash behind the type, then a black type panel, then a hard vertical cut down
the middle. Do not reintroduce any of them.

How it works:
- `.rh-hero` is white. The photo is `position:absolute`, pinned to the right, `width:64%`,
  bleeding to the viewport edge. It sits behind the copy at `z-index:0`.
- `.rh-hero__media::after` carries **three stacked white gradients**: left-to-right (the main
  dissolve), bottom-up, and top-down. The last two stop the photo butting against the
  breadcrumb above and the body copy below.
- **The left-to-right wash stays fully opaque to 28%, then falls to clear at 76%.** That 28%
  stop is load-bearing: it must clear the right edge of the longest line of copy, which is the
  kicker, or the headline ends up sitting on a half-transparent photo. Measured clearance is
  ~78px at 1440. If you lengthen the kicker, re-check it.
- Between 960 and 1279px the photo narrows to 58% and the column to 460px, for the same reason.
- Copy sits in a normal `.rh-container`, so the H1 aligns with the body copy below it.

**Mobile (under 960px):** the hero becomes `display:flex; flex-direction:column`. The photo is a
band on top, `clamp(230px,52vw,340px)` tall (`clamp(200px,48vw,260px)` under 480px), dissolving
downward into the copy. Under 480px the primary CTA goes full width and the two ghost buttons
share the row. `body` already carries `padding-bottom:74px` under 1024px to clear the fixed
mobile CTA bar.

**Colors on white:** kicker, stat numbers and ghost buttons are `--accent-ink` `#1768E5`
(5.06:1), H1 is `--text-dark` `#050E3D` (18.48:1), lede is `--text-body`, stat labels are
`--text-meta` (6.11:1). The `.rh-section--inv` ghost-button override deliberately does NOT
include `.rh-hero` any more.

**The CTA band** further down keeps its black surface, but its old gradient wash was replaced
with a hard 6px accent rule on the left edge.

**Image:** `hero-new-construction.jpg`, already hosted on Ryan's image repo and already used on
the live hub, served through jsDelivr:

```
https://cdn.jsdelivr.net/gh/theleveragedagent86/rhlv-site-images@main/new-construction/
```

Local originals live in `output/local-seo/pages/img/`, with regeneration prompts in
`REGEN-PROMPTS.md` there. That file's negative-prompt list matters: **no saguaro cactus, no red
sandstone mesas.** Saguaros are Sonoran/Arizona, not Nevada, and a local buyer spots it instantly.

### Other traps

- **Builder colors:** `~/.claude/skills/new-construction/builder-brand-colors.md` is canonical.
  The table in `landing-page-template.md` is now a derived copy that points back at it.
- **`overflow-x: hidden` on `html`/`body` kills the sticky rail.** `hidden` computes
  `overflow-y` to `auto`, which makes the root a scroll container that is not the viewport.
  Use `clip`.
- **A boolean rAF latch kills the scroll-spy.** A latch cleared only inside the rAF callback
  stays stuck forever if a frame never fires. Use cancel/re-request.
- **The rail's scroll must live on `.rh-toc__scroll`, not on `.rh-toc` or `.rh-rail`.** If the
  bordered box is itself the scroll container, its bottom border scrolls out of view and the
  panel looks open-ended. The border stays on a clipped flex frame, only the list moves.
- `--rail-top` (24px, how high the rail rides) is deliberately separate from `--anchor-off`
  (88px, scroll-padding that clears Lofty's fixed site nav on anchor jumps). Do not merge them.

### Folder Map — new-construction-hub/

```
new-construction-hub/
├── 0-seo-fields.txt             Lofty page settings: slug, meta title and
│                                description with char counts, canonical, OG,
│                                and the launch checklist (incl. the 301)
├── part-1-above-listings.html   Lofty embed 1: breadcrumb, hero, direct answer,
│                                takeaways, byline, area pills, 20-builder grid,
│                                rail, listings section heading, script, JSON-LD
├── part-2-below-listings.html   Lofty embed 2: why-new through sources (18 H2s),
│                                rail, CTA band, mobile bar, script
├── DESLOP-CHANGES.md            log of the AI-tell cleanup pass on the copy
└── _preview-stitched.html       generated local preview (both parts + a stand-in
                                 for Lofty's listings block). Never paste this.
```

**Maintenance rule:** after editing either part, regenerate `_preview-stitched.html` before
verifying. The two parts are the source of truth, the preview is derived.

The geo spokes (`/henderson-new-construction`, etc.) and the 20 builder pages reuse this
hub's system, not the per-community template.

## The geo spokes (area pages under the hub)

Lives in `geo-spokes/`. Seven area pages at `/<area>-new-construction`, the slugs the live hub
already links to. Same two-embed Lofty architecture and Vector system as the hub, around a
Lofty Featured Listings block filtered to that area.

**These pages are GENERATED. Never hand-edit the HTML.** Each area has a `content.json`;
`_build/build.py` turns it into the embeds. The CSS, the rail/spy script, and the 20-builder
registry (name, color, tier, slug) are read from `new-construction-hub/part-1-above-listings.html`
at build time, so a fix to the hub system reaches every spoke on the next build:

```
python3 geo-spokes/_build/build.py summerlin     # one area
python3 geo-spokes/_build/build.py --all         # every area with a content.json
```

The build fails on em-dashes, unknown builder keys, duplicate ids, broken anchors, inline
`<form>`, `/blogs/` links, leftover NOT FOUND, and SEO fields over length (title 48, since
Lofty appends " | Ryan Rose").

Pipeline: `_RESEARCH-BRIEF.md` (one research agent per area writes `research.md`) then
`_CONTENT-GUIDE.md` (writer turns research into `content.json`). Summerlin is the reference
content.json. Internal blog links must exist in `_build/live-sitemap-*.json`.

### Folder Map — geo-spokes/

```
geo-spokes/
├── _RESEARCH-BRIEF.md       what each area's research.md must contain, sourcing rules
├── _CONTENT-GUIDE.md        content.json schema, voice, section order
├── _build/
│   ├── build.py             generator + validator
│   └── live-sitemap-2026-09-16.json   live rosehomeslv.com URLs, grouped by area
└── <area>/                  summerlin, henderson, north-las-vegas, southwest-las-vegas,
    │                        skye-canyon, centennial-hills, lake-las-vegas
    ├── research.md          sourced facts (input)
    ├── content.json         page content (source of truth)
    ├── part-1-above-listings.html   GENERATED, Lofty embed 1
    ├── part-2-below-listings.html   GENERATED, Lofty embed 2
    ├── _preview-stitched.html       GENERATED, local preview only
    └── 0-seo-fields.txt             GENERATED, Lofty page settings + listings filter
```
