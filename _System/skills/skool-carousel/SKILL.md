---
name: skool-carousel
description: Use when someone asks to write a Skool carousel, a Leveraged Agent carousel, a swipe post for agents, a carousel about an AI workflow, content for the @the.leveraged.agent Instagram, or the ManyChat flow / comment auto-reply / DM keyword automation behind one. Writes cover hook, 9 slides, caption, a paste-ready design brief, and the full automation pack (public comment replies, DM sequence, ManyChat flow spec) for the agent-facing coaching brand. NOT for Rose Homes LV realtor carousels, use ig-carousel for those.
argument-hint: "topic, or a pillar name (listing launch, transactions, open houses, content engine, outbound, skill building)"
---

# Skool Carousel Writer

Writes a save-worthy educational Instagram carousel for **The Leveraged Agent**, Ryan's
Skool community that teaches real estate agents to run their business with AI.

**Audience: working real estate agents.** Not home buyers, not sellers, not Las Vegas
locals. If a slide would make sense to a homebuyer, it is in the wrong skill.

**Brand separation, read this first.** This is the Skool/coaching brand. It is a different
business from Rose Homes LV. Never put realtor branding, Vegas-buyer content, or Rose Homes
colors on this output. For Rose Homes LV carousels use `ig-carousel` instead.

## Grounding files, read before writing

Read these silently. Never ask Ryan for anything they already answer.

| File | What you take from it |
|---|---|
| `SKOOL Community/CLAUDE.md` | brand boundary, audience, voice |
| `SKOOL Community/Brandkit/CLAUDE.md` | logo files and palette for the design brief |
| `SKOOL Community/Mentor-Mining/ryan-built-inventory.md` | **the proof list.** What Ryan actually runs |
| `SKOOL Community/Mentor-Mining/content-queue.md` | ready topics, packaging rules, compliance lines |
| `SKOOL Community/VSL-Script-Main-Page.md` | the offer, the price, the promise, the voice |
| `SKOOL Community/Module-*.md` | what is actually taught, so a carousel never promises content that does not exist |
| `references/manychat-flow.md` | **the automation architecture.** Read before writing the automation pack |

## The proof rule, this is the whole moat

**Every carousel must map to a system Ryan actually runs.** Check
`ryan-built-inventory.md` before writing. If the topic does not map to a live skill or
plugin on that list, say so and offer the nearest topic that does. Ryan's credibility with
agents is "I run this in a real Vegas brokerage," not "I watched a video about it."

If a carousel would require a system marked BUILD QUEUE or BUILT, NOT INSTALLED, flag it
in one line before the output. Do not quietly write it as though it ships today.

## Content pillars

1. **Listing launch** (`listing-marketing`, `listing-video`, `ig-ads`, `listing-description`)
2. **Transactions and ops** (`transaction-coordination`, `daily-checklist`, `weekly-update`)
3. **Open houses** (promo pack, door knock invite, geo ads, circle prospecting, post-OH outbound)
4. **Content engine** (`blog-writer`, `local-news`, `yt-long`, `youtube-manager`, `claude-shorts`)
5. **Lead gen and outbound** (`expired-workflow`, `digital-cannonball`, `reverse-prospecting`, `Reddit`, `inbound-dm-*`)
6. **Skill building** (`skill-builder`, the CLAUDE.md system, "if you have an SOP you have a skill")

## Before you start

1. Required input is a **topic**. Audience is always agents, never ask.
2. If the topic is clear, generate immediately. Zero questions.
3. If no topic is given, ask ONE batched message offering three topics from the pillars
   above that map to live systems, and let Ryan pick or name his own.
4. Never stall. A placeholder beats a question.

## Output, use these exact section names

**COVER HOOK, 3 options**
Three cover-slide hooks. Each earns the first swipe with curiosity, a number, or a stake.
Never clickbait the slides cannot pay off.

**Name the tool.** Per `content-queue.md`, titles naming a specific product or model do
1,165 median views/day versus 476 for those that do not, a 2.4x lift, and naming a tool is
a verifiable fact so it is safe to say. At least one of the three hooks must name a real
tool by name: Claude Code, Claude Cowork, Lofty, Meta, GLVAR, Canva, Excalidraw.

**SLIDES 2 THROUGH 8, headline plus max 20 words each**
Always all seven. One teaching point per slide. Bold headline, then supporting copy of 20
words or fewer. Count the words and show the count in parentheses, e.g. "(18 words)". If
the topic has fewer points than slides, spend the spare slides on a do-this-instead slide
and a recap slide. Never filler. Each slide stands alone and pulls to the next.

**FINAL SLIDE (slide 9)**
The CTA. One action, stated plainly. **Default is a DM keyword**, e.g. 'DM me "TC"'. Ryan
prefers DMs over comments, a DM starts a real conversation and he can answer it once.
Rotate the alternatives sparingly: save this, or the Skool join. Never stack two asks on
one slide. When the CTA is a keyword, also write the AUTOMATION PACK, see below.

**Keyword rules.** One word, 2 to 12 characters, uppercase in the art. Never a word that
shows up in ordinary praise (GREAT, LOVE, THIS, YES, INFO), a false match sends the wrong
lead magnet to someone who was just being nice. Never a keyword already live on another
post. Full rules in `references/manychat-flow.md`.

Nine slides total is deliberate. Instagram allows more, but completion rate is the metric
that drives reach on educational carousels.

**CAPTION**
Expands the core idea in Ryan's voice, ends with the same single CTA, then 5 to 8 hashtags
mixing agent-audience and AI-tool tags. Never Las Vegas local tags, wrong brand.

**DESIGN BRIEF**
Slide by slide, cover through slide 9, paste-ready for Claude Design. One line per slide in
this exact shape, brand baked in:

> **Slide N.** Text: [the exact headline and copy]. Visual: [the visual direction].

Open the brief with a short brand block, colors, fonts, per-slide rules, logo placement, so
the whole thing pastes as one message. **The brand block always states the safe area**,
because it is the rule designers skip: slide padding `152px 64px 166px`, and nothing pinned
to a slide corner. Instagram crops a 4:5 post to a centred 1:1 for the profile grid, so a
corner logo is cut clean off the thumbnail. Numbers and reasoning in
`references/design-loop-prompt.md`. Then append the full contents of
`references/design-loop-prompt.md` to the end of the same message, brief first, that file
second, do not summarize or shorten it. That file carries the measured Vector brand DNA
(hex values, type, grid, radius, shadow, all numbers not adjectives) and the design-loop
instructions (build, then three-lens critic pass, then revise, then re-grade) so Claude
Design self-checks the result before Ryan ever sees it, instead of one-shotting it. Also
save the combined brief plus loop file as a standalone `claude-design-prompt.md` in the
carousel folder, and tell Ryan to attach the Brandkit logo files to that chat, Claude
Design cannot read local paths.

**AUTOMATION PACK** (whenever the CTA is a keyword)
Read `references/manychat-flow.md` first. It carries the canonical architecture, the
character caps, the keyword rules and the build order. Do not invent a different shape.

Three parts, in this order, every time.

*A. COMMENT AUTO-REPLY, 5 rotated variants.* The public reply that posts under a
commenter's comment confirming the DM went out. Under 12 words each, confirm the send and
nothing else, no pitch, no link. Rotate five so the comment section does not read as a bot.
Number them so they paste straight into ManyChat's rotation field.

*B. DM SEQUENCE.* The messages themselves, whether Ryan runs them as Instagram saved
replies by hand or loads them into ManyChat. **Instagram caps a DM at 1000 characters.**
Count every message, print the count in parentheses after each header, and split any
message that runs over. Give each one a shortcut name in the `kw1 / kw2a / kw2b / kw3`
shape so they load as saved replies too.

Structure: a short opener, the deliverable, then a branch question with three answers. The
sequence stops at the question and sends no link until the person responds. That wait is
deliberate, Instagram throttles accounts that fire links at people who have not replied.
Write a separate closing message for each of the three branches, each ending in the real
YouTube and Skool links.

Plain text only. DMs render markdown literally, so no asterisks, no hashes, no dashed
bullets. CAPS section labels and blank lines instead.

*C. MANYCHAT FLOW.* The build spec as an indented tree: trigger, comment reply, each
message node, each delay, the three buttons, the tag on each branch, the 24-hour follow-up.
Name the keyword, the match mode and the three tag names explicitly. Then list anything
that has to be verified live in the builder rather than assumed.

Save the whole pack as `automation-NN-<keyword>.md` in the carousel folder alongside the
design prompt, and update the keyword list so no two live posts share a keyword.

**Why this works**
Two or three sentences. Why this hook angle, why this slide order earns saves, and the one
thing to do with it today.

Deliverable: the copy blocks in chat, the design brief, and the automation pack.

## Slide geometry, and checking it

Every slide is **1080 x 1350**, 4:5, no exceptions and no mixed ratios in one set.

**The safe band.** Instagram crops a 4:5 post to a centred 1:1 for the profile grid,
trimming 135px off the top and 135px off the bottom. Only slide 1 is ever shown there, but
the band applies to **every** slide: the set then lines up as the reader swipes, and any
slide stays safe if it is reordered or posted on its own later. So slide padding is
`152px 64px 166px`, putting content in y 152 to 1184, and **nothing is pinned to a corner**.
A monogram or page number is a child of the top or bottom row, never
`position: absolute; bottom: 40px`, which lands at y1246 and gets cut.

**Reels safe zones do not apply here.** The 220px top and 320px bottom chrome bars in the
published Reels guides are Reels UI. A carousel's dots, handle and caption sit below the
image, so the full 1080 x 1350 is visible in feed. Insetting a carousel for Reels chrome
throws away a third of the slide. If Ryan hands you a Reels safe-zone guide, say this.

**Whenever slides actually get rendered**, and not only briefed, measure them before handing
anything over:

```bash
node ~/.claude/skills/skool-carousel/references/check-slides.mjs Main.dc.html Slide2.dc.html
```

It renders each slide to `png/` at 1080 x 1350 and measures every text and image element
against the band, printing a per-slide bounding box and exiting 1 with the offending element
named if anything falls outside. With no arguments it takes every `*.dc.html` in the folder
alphabetically, so pass the files explicitly when carousel order differs from alphabetical.

**Never report a carousel as finished on a visual read alone.** Rendering and measuring the
first build of this pattern caught two things the eye missed: a corner-pinned monogram cut
off the grid thumbnail, and a list item that wrapped to leave a single orphaned word on its
own line.

## Document format, when Ryan wants this as a document

Governs any .docx this skill produces. It reads like a consultancy deliverable, not a chat
window dump.

- **Title block:** document title, Ryan Rose, The Leveraged Agent, and the date. Nothing else.
- **One H1**, an H2 per section, H3 only inside a section. Never deeper. Reading only the H2s
  should tell you what you are holding.
- **Sections in the order they get used.** What he acts on first sits first.
- **Anything comparable goes in a bordered table.** Options, timings, counts, comparisons.
  A page of bullets looks like notes, a table looks considered.
- **No paragraph longer than 3 sentences,** no wall-of-text page. Long sections become
  bullets or a table.
- **Bold the label, never the sentence.** "**Hook:** ..." not a bolded clause mid-paragraph.
- **Footer on every page:** Ryan Rose | date | page number.
- **White space is the design.** Generous margins, real spacing, nothing crammed.
- **Generate a real downloadable .docx.** Never chat text only.
- **The 3-second test:** someone opening it cold knows what it is, who it is for, and what to
  do first without reading a sentence. If not, the hierarchy is wrong, fix it before delivering.
- Target 1 to 2 pages. Cut to fit, never shrink type or margins to pad.

## Rules

### Quality bar, check before delivering

- **The delete test.** If a sentence can be deleted without losing information, delete it.
- **The any-guru test.** If a line could have been posted by any AI-for-realtors account,
  it is not finished. Rewrite it with the specific skill name, the real number of hours,
  the actual deal on Ryan's board, something only Ryan can say.
- **The so-what test.** Every fact is followed by what to DO about it.
- **No hedging.** Say what you would do.
- **No filler headings.** Nothing whose only job is to announce another section.
- **The band test.** If slides were rendered, `check-slides.mjs` passed. A visual read is
  not evidence.

### Content rules

- **No em-dashes anywhere.** Use commas, periods, or "and". Workspace-wide rule.
- Educational value first. Saves beat likes. No engagement bait.
- Writes copy only. The design happens in Claude Design from the DESIGN BRIEF. Never
  describe a finished design as though you rendered it.
- Voice: direct, revenue-focused, transparent, working agent not course guru. Plain English.
- Banned words: unlock, supercharge, game-changer, revolutionary, secret weapon, leverage
  as a verb. Note "Leveraged" in the brand name is fine, the verb is not.
- Never invent numbers. Only figures from the grounding files or that you found and cited,
  attributed as "per [source], as of [month]".

### Compliance, this brand sells a coaching product

- **No income promises or guarantees.** No "make $X", no earnings claims, no implied
  typical results. Per `content-queue.md`, income-figure packaging also exposes Ryan under
  Nevada license advertising rules and underperformed in the source data anyway.
- Time-saved claims must be tied to a system on the inventory list and framed as Ryan's own
  result, not a promise to the reader.
- If a carousel mentions housing ads, say Meta Special Ad Category, no age, gender, or ZIP
  targeting.
- If a carousel mentions outbound to expireds or FSBOs, say DNC and TCPA scrub first.
- No legal, tax, or lending advice.
- **Fair housing.** Describe properties, lifestyle and amenities, never demographics, never
  who "belongs" somewhere, never steering.
- Anything published publicly is advertising. Ryan holds a Nevada license, so a carousel that
  touches his real estate practice carries "Real Broker, LLC" in the caption. Pure coaching
  content about skills and workflows does not. When unsure, put it in the caption.
- Maximum ONE question message before generating. Batch it. Accept messy input. Sensible
  defaults beat repeat questions. Offer variations AFTER delivering, never before.
- You WRITE and PREPARE. Never post, schedule, or send on Ryan's behalf.
- **Building the ManyChat flow is the one exception, and only when Ryan explicitly asks for
  it in that run.** Then drive the ManyChat web UI in his logged-in Chrome and follow the
  build order in `references/manychat-flow.md`. Three things are never attempted and always
  handed back: signing up, paying, and connecting the Instagram account via OAuth. Screenshot
  after each step, the builder is a drag-and-drop canvas that fails silently. A flow that has
  never been triggered by a real test comment is not finished, do not report it as done.

## End every run with

Post-delivery order, exactly: the carousel, then **Why this works**, then "Want this as a
document?", then "A second topic from your pillars?", then the closing line:

"Paste the design brief into Claude Design, designed carousel in 5 minutes."

If the run produced an automation pack, add one line after that: whether Ryan wants the
ManyChat flow built for him, and the reminder that he handles signup, payment and the
Instagram connection himself.

Never offer any of it before delivering.
