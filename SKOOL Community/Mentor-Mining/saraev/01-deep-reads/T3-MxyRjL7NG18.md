# AGENTIC WORKFLOWS: Build & Sell AI Automations (2026)

- **id:** MxyRjL7NG18 · **url:** https://youtube.com/watch?v=MxyRjL7NG18
- **tier:** T3-TEACHING
- **published:** 2025-12-21 · **views:** 295,904 · **views/day:** 1,315 · **runtime:** 341.7 min

## Hook (0:00–0:20)
> "Hey, welcome to the definitive guide on agentic workflows for business. Now, agentic workflows have the potential to bring about what I think is one of the largest wealth transfers in human history. But very few people are currently talking about how to practically use them to improve their financial means. That's what this video is going to show you how to do."

**Mechanism:** Threat plus authority-claim. He names a wealth transfer already in motion and positions the viewer as either capturing it or being captured by it, then immediately reads a 15-item curriculum so the viewer knows exactly what the 5.7 hours buy.

## Thesis
Raw LLMs are probabilistic and therefore unusable for real business work, so you wrap them in a three-layer deterministic framework (directives, orchestration, execution), and the arbitrage goes to whoever builds that wrapper before the market learns it.

## Beats
| ts | beat | what he's doing |
|---|---|---|
| 0:00 | hook + curriculum read | threat frame, then 15-item promise to justify the runtime |
| 1:07 | credibility drop | "$160,000 a month in combined revenue", consulted for billion-dollar businesses |
| 2:15 | the "overhang" | contrarian premise: everyone is using a straw on the ocean |
| 4:21 | arbitrage window | urgency lever, the window is open now and closing |
| 4:56 | demo 1 (cold open proof) | autonomous meal-prep outreach, proof before any teaching |
| 7:44 | "river of value" metaphor | abstract economic frame to raise the stakes above tooling |
| 9:07 | horizontal leverage | reframe: not 100% of 1 role, but 90% of 10,000 roles |
| 11:45 | n8n nodes vs bullet points | side-by-side visual that kills the old paradigm |
| 14:08 | why now: intelligence, tools, cost | pre-empts "this is hype", anchors on price collapse |
| 23:47 | knowledge ladder | docs to chats to agents, sets the mental model |
| 29:58 | PTMRO loop | names the mechanism, gives it a memorable acronym |
| 52:31 | five identical prompts, five answers | manufactures the problem the framework will solve |
| 59:15 | compound error math | 90% five times equals 59%, the numeric spine of the whole course |
| 62:31 | DO framework reveal | the payoff, delivered only after an hour of setup |
| 66:58 | LLM sort vs Python sort | 30 seconds vs 53 milliseconds, proof by stopwatch |
| 69:52 | IDE demystification | de-risks the technical objection with a cockpit analogy |
| 94:54 | workspace + folder structure | the actual buildable artifact, directives / executions / .env |
| 108:37 | dental client case | live proof: $2M/yr agency converted in 15 minutes |
| 129:39 | build 1 live: onboarding email | first hands-on build, deliberately trivial |
| 138:27 | build 2 live: ClickUp CRM wrapper | shows two paths (MCP vs API) and picks the better one |
| 155:21 | MCP explained, then undercut | teaches it, then argues against using it (token cost) |
| 188:10 | build 3 live: lead scraper | his flagship demo, LinkedIn Sales Nav to Google Sheet |
| 203:08 | five parallel Claude instances | the "search space" flex, 5x tests for a couple of dollars |
| 213:28 | order-of-magnitude rule | anti-tinkering rule, only optimize for 10x |
| 220:47 | self-annealing | the emotional centerpiece, systems that harden over time |
| 226:20 | employee A vs employee B | analogy that sells autonomy to business owners |
| 268:36 | webhooks + cron on Modal | moves work off the desk and into the cloud |
| 294:47 | parallel agents + sub agents | scaling chapter, then honest limits (3 to 4 max) |
| 300:40 | day-in-the-life triple demo | proof of the "using" phase, not the building phase |
| 340:50 | CTA | hard close on Maker School with a money-back guarantee |

## System demoed
Several, all inside the DO (directive, orchestration, execution) framework: a workspace with a `/directives` folder of markdown SOPs, an `/executions` folder of one-job Python scripts, an `.env` for keys, and an `agents.md` / `claude.md` / `gemini.md` system prompt injected every session.

- **[4:56] Autonomous cold outreach.** Prompt only, no framework. Model searches meal-prep companies, finds emails, sends five personalized emails via an MCP. 20 minutes of work in under 15 seconds.
- **[28:15] Lead scrape agent.** "Scrape me 200 HVAC owners in the US", model self-adjusts filters mid-run on a low match rate, uploads to Google Sheet, "almost 200 emails".
- **[37:48] Silence-cutting video editor.** Plan mode, then build, then test on a 1-minute clip, then pivot to voice activity detection. Working in one back-and-forth.
- **[66:58] Sort-a-list bake-off.** Native LLM sort roughly 30 seconds, Python script 53 milliseconds. The argument for pushing deterministic work into code.
- **[88:13 / 102:40] Proposal generator.** Sales call transcript in, PandaDoc-style [sic?] proposal out plus a follow-up email via MCP. "The actual workflow here took me maybe 15 minutes to set up."
- **[129:39] Client onboarding email flow.** Gmail app password, `onboard_client.md` directive, execution script, template.
- **[138:27] ClickUp CRM wrapper.** Built twice, once via official ClickUp MCP, once via raw API + directives. API version wins because it can set custom fields.
- **[151:57] Claude Skills weather report.** Downloads a Canva PDF template, drops it in, model builds a `generate-report` skill with YAML front matter and produces a formatted PDF.
- **[176:11] Custom MCP server** for leftclick.ai exposing five tools (company overview, services, booking link, case studies, search site).
- **[188:10] LinkedIn lead gen pipeline.** Sales Navigator URL to Vain [sic?] scrape to AnyMailFinder [sic?] enrichment to Google Sheets. 231 prospects, 139 valid emails. Self-anneals through an API failure, then gets parallelized.
- **[203:08] Five-instance parallel build.** Five Claude Code instances each build the same lead-gen workflow a different way in separate `tmp/` folders, then he merges the winners into main.
- **[251:34] Completion-chime hook** so he knows when a background agent finishes.
- **[285:49 / 290:51] Modal deployment.** Execution scripts (no LLM) pushed to Modal as a webhook URL, and separately as a cron schedule. Logging to a dedicated `agentic-cloud-log` Slack channel.
- **[326:49] Two sub agents.** A `reviewer` sub agent that grades scripts with fresh context, and a `document` sub agent with read-all / write-directives-only permission that keeps directives in sync with drifted scripts.

## Who it's for
Someone running or working inside a small service business who already knows drag-and-drop automation (n8n [sic?], Make, Zapier) and now feels it is obsolete, plus the aspiring AI-automation consultant who wants to sell this into other people's companies. He is explicit that this is not for hobbyists: "This course has a business focus." Secondary audience is the operator with existing SOPs who wants to convert them into agents.

## Economic argument
He argues on four numbers: his own revenue, the cost of intelligence, the cost of errors, and the cost of building.

Credibility: [1:07] "I build two AI based service agencies to $160,000 a month in combined revenue. I've also consulted for a couple of billion-dollar businesses with AI."

Cost of intelligence: [21:17] "When Claude Opus 4.5 dropped, it went from a cost of about $15 or $75 depending on input or output per 1 million tokens to five or $25 depending on input or output for 1 million tokens. That's a 3x reduction." And [26:34] "As of today I think of models like a mid-tier developer. They're 100K a year or so in terms of their like capability. But if you think about it, I'm spending 20 bucks a month for this, which is 240 bucks a year, which is over 400 times cheaper."

Cost of errors: [61:17] "imagine if you were a business that made $100,000 a month and you sent a wrong invoice 5% of the time. What sort of impact do you think you that would have to your business? Do you think that would have a 5% impact to your business? No, that would have like a 95% impact on your business."

Proof of deployment: [108:37] "a company that I'm currently working with right now does marketing specifically for dental practices and they do about $2 million a year," and [109:07] "within 15 minutes we had turned this into dough and we now have a workspace that you know the director managers and myself can use to do like 90% of the economically valuable work."

Cost of building: [207:57] "this allows you to do 5x the tests for like just a couple of dollars per workflow build. Way cheaper than anything um that N8, make.com or Zapier would have charged you just for like development and testing costs alone." And on hosting, [287:01] "I've used Modal now for like at least two weeks, maybe three, and I've used 4 cents out of the $5 available."

## CTA
- **What:** Two asks. Soft: grab his system prompts and prompt templates from "the link at the very top of the description". Hard: join Maker School, "my 90-day accountability roadmap that guarantees you your first customer for AI automation or agentic workflow consulting businesses... you will have your first customer or I'll give you your money back. More generally, it's just a great community. We have over 2,000 fantastically talented and capable people in there."
- **Where:** 130:54 and 285:20 (resource link), 301:23 (context mention of Maker School), 340:50 to 341:23 (the close)
- **How hard:** soft mention twice mid-roll, hard close with a guarantee in the final 60 seconds. Zero pitching across the middle 4 hours.

## Title + thumbnail pattern
"ALL-CAPS CATEGORY NAME: Build & Sell <thing> (YEAR)" → category-ownership plus dual outcome. He coins the category ("I've kind of coined the term" at 305:11), claims it in caps, promises both the skill and the monetization, and year-stamps it so it reads as current. The runtime itself is the thumbnail promise: definitive-guide positioning.

## Transferable to realtors?
- **Verdict:** ADAPTABLE
- **Why:** The architecture transfers almost intact. A realtor workspace with `/directives` holding markdown SOPs (listing launch, escrow milestones, open house follow-up), `/executions` holding scripts, a self-annealing clause in CLAUDE.md, and Modal cron for weekly seller reports is a direct rebuild of Ryan's existing setup and would make an excellent Skool module spine. What does not transfer is the demo layer: LinkedIn Sales Navigator scraping, Apollo enrichment, and cold-email blasts are B2B plays that collide with DNC/TCPA and MLS data rules on the consumer side, so the lead-gen half needs a full real estate substitution (MLS hotsheet, expireds, CRM triggers) rather than a rename.
