# Build the graphics package for: Buying New Construction in Las Vegas: The Full Process

## Context
You are building a graphics overlay package for a 16:9 1920x1080 long-form YouTube video for Ryan Rose (Rose Homes LV). Ryan films himself on camera, and these graphics get cut into his footage. Do not render a full talking-head video, only the graphic elements listed below. Video runtime is about 13 minutes.

## Setup
- Invoke the /hyperframes skill family first (/hyperframes, /hyperframes-cli, /gsap, /hyperframes-registry). Do not hand-write GSAP from memory.
- Read MOTION_PHILOSOPHY.md at the hyperframes-student-kit workspace root, and the Rose Homes Brandkit at /Users/ryanrose/Downloads/Claude/SKOOL Community/hyperframes-student-kit/Rose Homes Brandkit/. Use Ryan's brand fonts and colors, not the Skool sample theme.
- Scaffold a 16:9 1920x1080 at 30fps project at /Users/ryanrose/Downloads/Claude/SKOOL Community/hyperframes-student-kit/video-projects/ytlong-buying-new-construction-las-vegas/. Run all CLI from inside it.
- Confirm exact block names with `npx hyperframes catalog --type block` before building. The "Suggested block" column below is a starting point, not a guarantee.

## Graphic elements to build
One row per [GFX: ...] cue from the script, in script order. Timestamps are approximate across the ~13-minute runtime. Carry the exact on-screen text and source as written.

| # | Script beat (approx timestamp) | Cue type | Exact on-screen text / data | Source | Suggested block | On-screen duration |
|---|---|---|---|---|---|---|
| 1 | Hook open (0:00) | chapter | Chapter 1: The $30,000 Mistake | n/a | chapter title card | 3 to 4 s |
| 2 | "fifty to a hundred percent more" (0:10) | stat | Big number 50 to 100%, label "builder flooring markup vs. after closing" | rosehomeslv.com/blog/new-construction-upgrades-worth-it-las-vegas | big-number card, eased count-up | 4 to 6 s |
| 3 | "that's just one room" (0:25) | broll | Motion graphic: design center samples, countertops and flooring tiles | n/a | motion-graphic interlude (MP4) | 4 to 6 s |
| 4 | "But here's the part nobody tells you" (0:45) | transition | Medium shader transition (push / whip-pan) | n/a | shader transition | 0.6 to 1 s |
| 5 | "What I'm Promising You" (0:55) | chapter | Chapter 2: What I'm Promising You | n/a | chapter title card | 3 to 4 s |
| 6 | "I'm Ryan Rose" (1:05) | lower-third | Name "Ryan Rose", descriptor "Real Broker, LLC | Las Vegas" | n/a | yt-lower-third registry block | 5 to 6 s |
| 7 | "Here's my promise" (1:18) | title-card | The full process, start to finish | n/a | kinetic title card | 3 to 4 s |
| 8 | "I'm going to walk it in order" (1:35) | list | Bullets: First visit; Community and builder; Design center; The build; Walkthrough and closing | n/a | animated bullets, stagger | 6 to 8 s |
| 9 | "stick around" (1:50) | broll | Motion graphic: buyer hesitating at a model-home door | n/a | motion-graphic interlude (MP4) | 4 to 6 s |
| 10 | "Your First Visit and Your Agent" (2:10) | chapter | Chapter 3: Your First Visit and Your Agent | n/a | chapter title card | 3 to 4 s |
| 11 | "this is where that expensive mistake lives" (2:20) | transition | Medium shader transition (push / whip-pan) | n/a | shader transition | 0.6 to 1 s |
| 12 | "the friendly person who greets you" (2:30) | broll | Motion graphic: model-home sales office, staff at a desk | n/a | motion-graphic interlude (MP4) | 4 to 6 s |
| 13 | "the rule that trips people up" (2:50) | stat | Big text "First visit only", label "when your agent must register" | hendersonredevelopment.com; neighborhoodsinlasvegas.com | big-number / big-text card | 4 to 6 s |
| 14 | "If you walk in alone" (3:05) | title-card | Walk in alone first, and your agent can be locked out | n/a | kinetic title card | 4 to 5 s |
| 15 | "Having your own agent costs you nothing" (3:25) | stat | Big number $0, label "what your own agent costs you" | homesforsale.vegas/new-construction-realtors | big-number card, count-up to 0 / pop-in | 4 to 6 s |
| 16 | "Think about it this way" (3:45) | quote | Pull quote "On-site staff represent the builder, not the buyer." Attribution: neighborhoodsinlasvegas.com | neighborhoodsinlasvegas.com | pull-quote card | 5 to 7 s |
| 17 | "I had a buyer last year" (4:05) | broll | Motion graphic: buyer and agent shaking hands outside a model | n/a | motion-graphic interlude (MP4) | 4 to 6 s |
| 18 | "if you remember one thing" (4:35) | transition | High shader transition (cinematic-zoom / glitch) | n/a | shader transition | 0.8 to 1.2 s |
| 19 | "Choosing Community and Builder" (4:50) | chapter | Chapter 4: Choosing Community and Builder | n/a | chapter title card | 3 to 4 s |
| 20 | "Las Vegas isn't one new-home market" (5:00) | map | Las Vegas valley map with master-planned communities marked | n/a | location / map graphic (MP4) | 5 to 7 s |
| 21 | "the top seller... was Cadence" (5:20) | stat | Big number 311, label "Cadence net sales, No. 1 valley master plan, Q1 2026" | reviewjournal.com, May 9, 2026 | big-number card, eased count-up | 4 to 6 s |
| 22 | "Summerlin came in second" (5:35) | compare | Two columns: Cadence 311 vs Summerlin 276. Header "Q1 2026 net sales" | reviewjournal.com, May 9, 2026 | two-column comparison | 6 to 8 s |
| 23 | "You've also got Inspirada..." (6:00) | list | Bullets: Cadence; Summerlin; Inspirada; Skye Canyon; Tule Springs | n/a | animated bullets, stagger | 6 to 8 s |
| 24 | "the whole valley sold 2,239 new homes" (6:20) | stat | Two figures: 2,239 sales and $502,990 median. Label "valley new homes, Q1 / March 2026" | reviewjournal.com (Home Builders Research) | big-number card (lead with 2,239, median small) | 5 to 7 s |
| 25 | "several builders compete" (6:45) | list | Bullets: Lennar; KB Home; Pulte; Toll Brothers; Richmond American; DR Horton | n/a | animated bullets, stagger | 6 to 8 s |
| 26 | "that competition is good for you" (7:05) | broll | Motion graphic: two model homes side by side | n/a | motion-graphic interlude (MP4) | 4 to 6 s |
| 27 | "Now comes the fun part" (7:25) | transition | Medium shader transition (push / whip-pan) | n/a | shader transition | 0.6 to 1 s |
| 28 | "Contract, Design Center, and Upgrades" (7:35) | chapter | Chapter 5: Contract, Design Center, and Upgrades | n/a | chapter title card | 3 to 4 s |
| 29 | "First you'll sign the builder's contract" (7:45) | broll | Motion graphic: buyer signing a contract at a desk | n/a | motion-graphic interlude (MP4) | 4 to 6 s |
| 30 | "Expect that deposit to run" (7:55) | compare | Two columns: New build deposit 5 to 10% vs Typical resale earnest money. Header "deposit at signing" | houzeo / StyleCraft synthesis | two-column comparison | 6 to 8 s |
| 31 | "Then comes the design center" (8:15) | broll | Motion graphic: design center wall of finishes, cabinets, fixtures | n/a | motion-graphic interlude (MP4) | 4 to 6 s |
| 32 | "Remember that flooring number" (8:35) | stat | Big number 50 to 100%, label "builder flooring markup" | rosehomeslv.com/blog/new-construction-upgrades-worth-it-las-vegas | big-number card, eased count-up | 4 to 6 s |
| 33 | "So here's the simple rule" (8:50) | title-card | Some upgrades wait. Some can't. | n/a | kinetic title card | 3 to 4 s |
| 34 | "Structural choices... before they pour" (9:05) | stat | Big text "Before the foundation pour", label "when structural options lock in" | homesforsale.vegas/builder-options | big-number / big-text card | 4 to 6 s |
| 35 | "Your finish selections usually happen" (9:25) | stat | Big text "8 to 12 weeks before closing", label "when design selections are made" | homesforsale.vegas/builder-options (search synthesis) | big-number / big-text card | 4 to 6 s |
| 36 | "My honest advice" (9:45) | broll | Motion graphic: couple comparing two flooring samples | n/a | motion-graphic interlude (MP4) | 4 to 6 s |
| 37 | "The crew breaks ground" (10:05) | transition | High shader transition (cinematic-zoom / glitch) | n/a | shader transition | 0.8 to 1.2 s |
| 38 | "The Build, Inspections, and Warranty" (10:15) | chapter | Chapter 6: The Build, Inspections, and Warranty | n/a | chapter title card | 3 to 4 s |
| 39 | "plan on about six to twelve months" (10:25) | stat | Big text "6 to 12 months", label "production home build time, contract to closing" | rosehomeslv.com/blog/new-construction-timeline-las-vegas-2026 | big-number / big-text card | 4 to 6 s |
| 40 | "don't expect dirt to fly the day you sign" (10:40) | stat | Big text "30 to 90 days", label "wait after signing before ground breaks" | rosehomeslv.com/blog/new-construction-timeline-las-vegas-2026 | big-number / big-text card | 4 to 6 s |
| 41 | "From there it moves in phases" (11:00) | list | Bullets: Months 1-2 permits; 3-4 foundation and framing; 5-6 rough-in; 7-9 finishes; 10-12 inspections and close | n/a | animated bullets, stagger | 7 to 9 s |
| 42 | "a tip that saves a lot of stress" (11:25) | stat | Big text "30 to 60 days", label "buffer to add past the builder's projected date" | rosehomeslv.com/blog/new-construction-timeline-las-vegas-2026 | big-number / big-text card | 4 to 6 s |
| 43 | "the first big moment" (11:50) | broll | Motion graphic: framed house, exposed studs and wiring before drywall | n/a | motion-graphic interlude (MP4) | 4 to 6 s |
| 44 | "This happens while the framing... is exposed" (12:00) | title-card | See it before the walls hide it | n/a | kinetic title card | 4 to 5 s |
| 45 | "The second big moment" (12:20) | broll | Motion graphic: buyer placing blue tape on a wall imperfection | n/a | motion-graphic interlude (MP4) | 4 to 6 s |
| 46 | "a few days before closing... blue tape" (12:30) | stat | Big text "A few days before closing", label "blue tape walkthrough timing" | rocketmortgage.com/learn/blue-tape-walkthrough | big-number / big-text card | 4 to 6 s |
| 47 | "you're not on your own" (12:50) | list | Bullets: 1 year workmanship; 2 years systems; 10 years structural | 2-10.com (1-2-10 style warranty) | animated bullets, stagger | 6 to 8 s |
| 48 | "I want to be straight with you" (13:10) | title-card | Warranty terms vary by builder, so read yours | n/a | kinetic title card | 4 to 5 s |
| -- | "Nevada law gives homeowners a window" (13:25) | (NOT FOUND) | PLACEHOLDER. No graphic. The Nevada statute-of-repose hard number for construction-defect claims is unresolved in research (6 vs 10 year conflict). Do not build a stat card here. Leave a gap the editor fills only after Ryan confirms the current statute. | research gap | none | n/a |
| 49 | "Closing and Your Action Plan" (13:35) | chapter | Chapter 7: Closing and Your Action Plan | n/a | chapter title card | 3 to 4 s |
| 50 | "let's bring it home" (13:45) | transition | Medium shader transition (push / whip-pan) | n/a | shader transition | 0.6 to 1 s |
| 51 | "Plan for closing costs" (13:55) | stat | Big text "2 to 5%", label "new-construction closing costs in Las Vegas" | rosehomeslv.com/blog/new-construction-closing-costs-las-vegas | big-number / big-text card | 4 to 6 s |
| 52 | "watch one line item" (14:05) | stat | Big text "$5.10 per $1,000", label "Nevada transfer tax" | rosehomeslv.com/blog/new-construction-closing-costs-las-vegas | big-number / big-text card | 4 to 6 s |
| 53 | "Now the good news" (14:25) | stat | Big number up to $30,000, label "2026 builder closing-cost incentive with a preferred lender" | rosehomeslv.com/blog/new-construction-closing-costs-las-vegas | big-number card, eased count-up | 4 to 6 s |
| 54 | "here are your three takeaways" (14:50) | list | Bullets: Bring your agent first; Spend on structure not finishes; Show up for both walks | n/a | animated bullets, stagger | 7 to 9 s |
| 55 | "if you want a real person" (15:15) | cta-card | 702-747-5921 | rosehomeslv.com (with Rose Homes LV logo) | n/a | logo-outro / branded CTA card | 6 to 8 s |
| 56 | "The One Thing to Remember" (15:35) | chapter | Chapter 8: The One Thing to Remember | n/a | chapter title card | 3 to 4 s |
| 57 | "remember this" (15:45) | title-card | Bring your agent on visit one | n/a | kinetic title card | 4 to 5 s |
| 58 | "can be one of the best things" (16:00) | broll | Motion graphic: keys handed over at a brand-new front door | n/a | motion-graphic interlude (MP4) | 4 to 6 s |

## Design rules
- Keep the intro short and value-first, no long branded sting.
- One idea per graphic. Strip decoration so a number or chart reads at a glance. Animate simply (count-ups, bars from zero, eased), keep motion subtle.
- Show graphics on transitions and supporting points, just after the line they reinforce. Hide them during Ryan's most important lines so they do not compete with his face.
- Captions: white text on a semi-transparent black band, WCAG contrast at least 4.5:1, no more than about 32 characters per line, no more than 2 to 3 lines, on screen about 3 to 7 seconds, bottom-center and clear of lower-thirds.
- Keep all text inside title-safe margins and large enough to read on a phone.
- Brand consistency: same fonts, colors, lower-third style, music family throughout.
- Outro carries the single soft CTA (702-747-5921, rosehomeslv.com) plus a next-video hand-off.
- No em-dashes in any on-screen text.

## Render contract (do not break)
- Root div needs id, data-composition-id, data-start="0", data-width, data-height.
- Timed visible elements need class="clip", except <video> and <audio>.
- Every timed element needs data-start, data-duration, data-track-index. Same-track clips cannot overlap.
- Exactly one paused GSAP timeline per composition on window.__timelines["<data-composition-id>"], key matching exactly.
- Never animate width/height/top/left on a <video>; wrap and animate the wrapper.
- Determinism: no Date.now(), no unseeded Math.random(), no render-time network fetches.

## Output
- Overlays (lower-thirds, stat cards, captions): transparent WebM (npx hyperframes render --format webm).
- Full-frame interludes (intro, chapter cards, b-roll graphics, outro): MP4.
- Put renders in renders/, and write a graphics-shot-list.md mapping each graphic to its script beat and placement.

## Workflow (mandatory gates)
1. Invoke /hyperframes, read the brand and motion philosophy.
2. Build a composition for every element above.
3. npx hyperframes lint, then inspect for overflow.
4. Live preview: npx hyperframes preview, hand Ryan the URL, wait for explicit sign-off before any render.
5. Draft render, then read each frame to verify (no cropping, overflow, low-contrast captions, wrong colors). Fix and re-verify.
6. Final render. Captions sync to Ryan's real audio after he films, via npx hyperframes transcribe.
