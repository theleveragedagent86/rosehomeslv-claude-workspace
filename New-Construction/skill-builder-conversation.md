# New Construction Skill Builder — Full Conversation Log

**Date:** 2026-03-22 / 2026-03-23
**Participants:** Ryan Rose + Claude (Skill Builder)

---

## Mode Selection

**Q: What would you like to do with the skill builder?**
**A:** Build a new skill

---

## Round 1: Goal & Name

**Q: What does this skill do? Is it the tenant email automation from the open file (classify, draft, route tenant emails), or something different?**
**A:** New construction communities researcher

**Q: What should this skill produce when you invoke it?**
**A:** I would like an extremely detailed and thorough research report, a comparison report inside the research report, and a separate content markdown file that gives a tremendously vast social content (long/short form) video transcripts in my tone of voice/way of talking. Building a buyer guide for each community separately would be fantastic and having different avenues/ways of deploying that would be great (i.e. landing page html code to input into my website [they only take html coding for it], pdf they can get emailed after "fill in your info" lead capture and you build an automation that emails them with a specific lofty smart plan for each community (smart plan would need to be built first with lead capture/tags/etc before deploying the landing page), a shorter blog post on the guide that has a link to the lead capture form for the guide) and that is to name a few. Knowing all possible forms would be fantastic. Maybe build a meta ads strategy that is very low cost for lead capture to "find out more" and they fill out a meta ad lead capture form to get more info and it goes straight to my lofty crm that will automatically start the specific smart plan built that would include texting and emailing immediately.

---

## Round 2: Trigger & Name

**Q: What should we call this skill?**
**A:** `new-construction`

**Q: How would you typically invoke this? What argument would you pass?**
**A:** Community name (e.g., `/new-construction Cadence at Cimarron`)

---

## Round 3: Step-by-Step Process

**Q: When you run `/new-construction [Community Name]`, should it produce ALL outputs in one go, or would you prefer phases?**
**A:** I want it all at once with as many deployed sub-agents as necessary. Each sub-agent will have a VERY specific task to do and needs to have a specific and detailed job duty to produce the absolute best/top notch expert output.

---

## Round 4: Inputs, Outputs & Dependencies

**Q: Where does the research data come from?**
**A:** Web research — Claude searches builder websites, real estate sites, public listings to gather community data.

**Q: For the 'your tone of voice' in social content and video transcripts — do you have existing content samples?**
**A:** Yes, I have samples. I'll provide them shortly.

**Q: For the Lofty smart plans — doc output or API integration?**
**A:** I want it done in a separate doc, but at some point I am going to build a skill/plugin for Claude Cowork to automatically build this for me, since this will be a big undertaking.

**Q: Where are the voice/tone samples?**
**A:** I'll give them to you shortly.

**Q: Where should all the output files go?**
**A:** `/Users/ryanrose/Downloads/Claude/New-Construction/[Community-Name]/` — That path works.

---

## Round 5: Guardrails & Edge Cases

**Q: Geographic focus?**
**A:** Clark County, Nevada

**Q: For the Meta ads strategy — how detailed?**
**A:** Full production-ready: ad copy, creative briefs, audience targeting, budget recs, campaign structure — ready to launch.

---

## Round 6: Confirmation — Skill Summary

### Skill Summary: `new-construction`

**Goal:** Research a Clark County, NV new construction community and produce a complete marketing/lead-gen ecosystem — research report, social content, buyer guides, landing pages, smart plans, blog post, and Meta ads strategy — all in one invocation.

**Trigger:** `/new-construction [Community Name]`
**Arguments:** Community name (e.g., "Cadence at Cimarron", "Summerlin West")

**Process (Subagent Architecture):**

You (Manager) orchestrate **6+ parallel subagents:**

| Agent | Job |
|-------|-----|
| **Research Agent** | Web-searches the community exhaustively: builder(s), floor plans, pricing, lot sizes, HOA, amenities, schools, nearby retail, incentives, model home hours, phase/timeline info, comparable resale data |
| **Comparison Analyst** | Takes research output → builds side-by-side comparison tables (vs other nearby new construction communities) embedded in the research report |
| **Social Content Creator** | Produces long-form video transcripts (YouTube/Reels), short-form hooks, Instagram captions, TikTok scripts — all in Ryan's voice/tone (references voice file) |
| **Buyer Guide Producer** | Creates a comprehensive buyer guide for the community with all research data, formatted for multiple deployment methods |
| **Landing Page Developer** | Converts buyer guide into clean HTML code compatible with Lofty website, with lead capture form integration |
| **Smart Plan Architect** | Designs the full Lofty smart plan: trigger tags, email sequence, text sequence, timing, all copy written — output as a detailed blueprint doc |
| **Blog Writer** | Writes a shorter blog post about the community with CTA linking to the lead capture landing page |
| **Meta Ads Strategist** | Full production-ready Meta ads campaign: ad copy variations, creative briefs, audience targeting specs, budget recommendations, campaign structure, lead form strategy → Lofty CRM flow |

**Inputs:**
- Community name (from argument)
- Web research (live searches)
- Voice/tone reference file (to be provided by Ryan)
- Existing skill references (blog-writer SEO guidelines, ig-ads campaign structures)

**Outputs** (all saved to `/Users/ryanrose/Downloads/Claude/New-Construction/[Community-Name]/`):
- `research-report.md` — Full research + comparison tables
- `social-content.md` — All video transcripts + social posts
- `buyer-guide.md` — Comprehensive buyer guide
- `landing-page.html` — Lofty-compatible HTML with lead capture
- `smart-plan.md` — Full Lofty smart plan blueprint
- `blog-post.md` — SEO blog post with lead capture CTA
- `meta-ads-strategy.md` — Complete campaign package (copy, targeting, budget, structure)

**Dependencies:** WebSearch, WebFetch, voice/tone reference file (TBD)

**Guardrails:**
- Clark County, Nevada only
- Never fabricate pricing, floor plan, or builder data — flag gaps
- Smart plan is a doc blueprint only (no Lofty API integration yet)

---

## Additional Request: Master Landing Page

**Ryan's addition:** Would love to have a full landing page built with schema that has ALL of the communities — each linking to their individual landing page or lead capture. A master directory/hub page for all new construction communities.

This adds a new output and potentially a new subagent:

| Agent | Job |
|-------|-----|
| **Master Page Developer** | Builds and maintains a master HTML landing page with schema markup that lists ALL researched communities, linking to each individual community landing page/lead capture. Updated each time a new community is processed. |

**New output:**
- `/Users/ryanrose/Downloads/Claude/New-Construction/master-landing-page.html` — Master directory of all communities with schema markup

---

## Status: Awaiting Final Confirmation

Ryan needs to confirm the summary (including the master landing page addition) before build phase begins. Voice/tone samples still TBD — Ryan will provide shortly.
