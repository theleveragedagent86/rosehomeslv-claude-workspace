# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **New Construction Marketing Automation System** for Ryan Rose, a Las Vegas real estate agent. The `/new-construction [Community Name]` skill researches Clark County, NV communities and generates a complete marketing ecosystem via 10 specialized sub-agents across 6 execution waves, including auto-building the 3 Lofty CRM action plans via Cowork browser automation.

## Architecture

**Skill instructions:** `/Users/ryanrose/.claude/skills/new-construction/`
**Per-community outputs:** `/Users/ryanrose/Downloads/Claude/New-Construction/[community-slug]/`
**Shared blog folder (all communities):** `/Users/ryanrose/Downloads/Claude/New-Construction/all-blogs/`

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
