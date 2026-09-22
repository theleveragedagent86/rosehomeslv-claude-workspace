# Build the graphics package for: What Builders Won't Tell You: New Construction Mistakes in Las Vegas

## Context
You are building a graphics overlay package for a 16:9 1920x1080 long-form YouTube video for Ryan Rose (Rose Homes LV). Ryan films himself on camera reading the script, and these graphics get cut into his footage. Do not render a full talking-head video, only the graphic elements listed below.

This is a punchy, cautionary "watch out for this" video about new construction in Las Vegas. The tone of the graphics should be high-energy and bold: confident, attention-grabbing stat and warning cards that make a viewer stop and pay attention, while staying clean and on Ryan's brand. Think alert-style emphasis (clear accent color pops, strong number sizing, decisive motion) without looking like clickbait or a scam-warning meme. Stay professional and trustworthy.

## Setup
- Invoke the /hyperframes skill family first (/hyperframes, /hyperframes-cli, /gsap, /hyperframes-registry). Do not hand-write GSAP from memory.
- Read MOTION_PHILOSOPHY.md at the hyperframes-student-kit workspace root, and the Rose Homes Brandkit at /Users/ryanrose/Downloads/Claude/SKOOL Community/hyperframes-student-kit/Rose Homes Brandkit/. Use Ryan's brand fonts and colors, not the Skool sample theme.
- Scaffold a 16:9 1920x1080 at 30fps project at /Users/ryanrose/Downloads/Claude/SKOOL Community/hyperframes-student-kit/video-projects/ytlong-new-construction-mistakes-las-vegas/. Run all CLI from inside it.
- Confirm exact block names before building with: npx hyperframes catalog --type block. The block names below are suggestions; match them to what the catalog actually exposes (for example yt-lower-third, data-chart, logo-outro).

## Graphic elements to build
Build one composition per row. Every row maps to a [GFX: ...] cue in the final script, in script order. There are 24 cues and 0 NOT FOUND placeholders.

| # | Script beat (approx timestamp) | Cue type | Exact on-screen text / data | Source | Suggested block | On-screen duration |
|---|--------------------------------|----------|------------------------------|--------|-----------------|--------------------|
| 1 | 0:00 cold open | title-card | Title: "What Builders Won't Tell You" Subtitle: "New Construction Mistakes in Las Vegas" | n/a (title) | kinetic title-card, brand fonts | 3 to 4 s |
| 2 | 0:25 intro / who I am | lower-third | Name: "Ryan Rose" Descriptor: "Real Broker, LLC" | n/a (identity) | yt-lower-third | 5 to 6 s |
| 3 | 0:40 section 1 open | chapter | "1 - Who Actually Represents You" | n/a (section) | chapter / section title card | 2.5 to 3 s |
| 4 | 0:40 into section 1 | transition | Medium energy push or whip-pan into chapter 1 | n/a | push / whip-pan shader transition | 0.5 to 0.8 s |
| 5 | 0:50 rep represents builder | stat | Big label: "BUILDER" Caption: "Who the on-site sales rep legally represents" | Hank Miller Team | big-label/stat card (word, not number) | 4 to 5 s |
| 6 | 1:10 your agent is free | stat | Big number: "$0" Caption: "What your own buyer's agent costs you" | Felix Homes | big-number stat card, eased count-up to $0 hold | 4 to 5 s |
| 7 | 1:20 the catch | list | "Register your agent on the FIRST visit" / "They work for you, not the builder" / "It costs you nothing" | Felix Homes; homesforsale.vegas; hendersonredevelopment.com | animated bullet list, staggered | 6 to 7 s |
| 8 | 1:35 section 2 open | chapter | "2 - Lot Premiums and Upgrade Markups" | n/a (section) | chapter / section title card | 2.5 to 3 s |
| 9 | 1:35 into section 2 | transition | Medium energy push or whip-pan into chapter 2 | n/a | push / whip-pan shader transition | 0.5 to 0.8 s |
| 10 | 1:50 what drives lot premiums | list | "View" / "Corner lot" / "Cul-de-sac" / "No back neighbor" | n/a (examples in script) | animated bullet list, staggered, icon-style | 5 to 6 s |
| 11 | 2:15 design center markup | stat | Big number: "50% to 100%" Caption: "Las Vegas builder upgrade markup vs. doing the work after closing" | rosehomeslv.com, 2025 | big-number stat card, count-up emphasis, bold warning accent | 5 to 6 s |
| 12 | 2:50 section 3 open | chapter | "3 - The Rate Buydown Trap" | n/a (section) | chapter / section title card | 2.5 to 3 s |
| 13 | 2:50 into section 3 | transition | High energy: cinematic-zoom or glitch into chapter 3 | n/a | cinematic-zoom / glitch shader transition | 0.6 to 0.9 s |
| 14 | 3:10 why builders buy down rates | stat | Big label: "PROTECTS APPRAISALS" Caption: "Why builders fund rate buydowns instead of cutting price" | Bankrate, 2025-11-25 | big-label/stat card (phrase, not number) | 4 to 5 s |
| 15 | 3:25 the risk | broll | Split screen. Left: "LOWER RATE" Right: "SAME HIGH PRICE" | n/a (illustrative) | two-panel split-screen motion graphic | 4 to 5 s |
| 16 | 3:45 the lender question | quote | Pull quote: "Can a builder make me use their lender?" Attribution: "common buyer question" | common buyer question (RESPA 12 CFR 1024.15; BuilderOnline; Silberman Law Firm context) | pull-quote card with attribution | 4 to 5 s |
| 17 | 4:15 section 4 open | chapter | "4 - The Fine Print That Costs You" | n/a (section) | chapter / section title card | 2.5 to 3 s |
| 18 | 4:15 into section 4 | transition | Medium energy push or whip-pan into chapter 4 | n/a | push / whip-pan shader transition | 0.5 to 0.8 s |
| 19 | 4:25 contract protections | compare | Two columns. Left header: "Resale contract" with "Appraisal protection: renegotiate or walk." Right header: "Builder contract" with "Usually no appraisal contingency." Topic line: "Buyer protections" | Geraghty Law Office; Homes.com | two-column comparison card | 6 to 7 s |
| 20 | 4:40 what builder contracts lack | list | "No appraisal contingency" / "Weaker inspection terms" / "Sometimes binding arbitration" | Geraghty Law Office; Homes.com | animated bullet list, staggered, warning accent | 6 to 7 s |
| 21 | 5:05 section 5 open | chapter | "5 - Your Game Plan" | n/a (section) | chapter / section title card | 2.5 to 3 s |
| 22 | 5:05 into section 5 | transition | Calm: blur or crossfade into chapter 5 | n/a | blur / crossfade shader transition | 0.5 to 0.8 s |
| 23 | 5:15 the three moves | list | "Bring your own agent on visit one" / "Skip the design-center markup on cosmetics" / "Compare the builder's loan to an outside lender" | script summary of sources above | animated bullet list, staggered, numbered 1-2-3 | 7 to 8 s |
| 24 | 5:50 close | cta-card | Line: "Bring your own agent. Read the fine print. Shop the loan." Phone: "702-747-5921" Web: "rosehomeslv.com" | Ryan Rose contact | logo-outro / branded CTA card | 5 to 6 s |

### B-roll motion-graphic references (use as supporting overlays where helpful; not separate timed cues unless you choose to render them)
- Exterior and interior of a Las Vegas model home, sales rep greeting visitors at a welcome desk.
- New-build communities in Summerlin, Skye Canyon, and Henderson; fresh streets and signage.
- A sample loan estimate document, blurred, with the APR line highlighted.
- Design-center showroom: flooring samples, cabinet and lighting displays.
- A corner lot and a no-back-neighbor lot to illustrate lot premiums.
- A contract on a table, pen hovering over a signature line, then a hand pausing to read.

## Design rules
- Keep the intro short and value-first, no long branded sting.
- One idea per graphic. Strip decoration so a number, phrase, or comparison reads at a glance. Animate simply (count-ups, bars from zero, eased entrances), keep motion subtle even though the tone is high-energy. Energy comes from bold sizing, decisive timing, and accent-color pops, not busy motion.
- This is a cautionary video. Use a clear warning/emphasis accent from the brand palette on the stat and list cards so the "watch out" beats land, but keep the base look clean and trustworthy. No alarmist red sirens or meme styling.
- Show graphics on transitions and supporting points, just after the line they reinforce. Hide them during Ryan's most important lines so they do not compete with his face.
- Captions: white text on a semi-transparent black band, WCAG contrast at least 4.5:1, no more than ~32 characters per line, no more than 2 to 3 lines, on screen about 3 to 7 seconds, bottom-center and clear of lower-thirds.
- Keep all text inside title-safe margins and large enough to read on a phone.
- Brand consistency: same fonts, colors, lower-third style, music family throughout.
- Outro carries the single soft CTA (702-747-5921, rosehomeslv.com) plus a next-video hand-off to the full new-construction process walkthrough and the new-versus-resale breakdown.
- No em-dashes in any on-screen text.
- Factual only. Do not invent numbers, sources, or claims beyond what the table above carries from the script.

## Output
- Overlays (lower-thirds, stat cards, list cards, compare card, quote card, captions): transparent WebM (npx hyperframes render --format webm).
- Full-frame interludes (title card, chapter cards, split-screen b-roll graphic, CTA outro): MP4.
- Put renders in renders/, and write a graphics-shot-list.md mapping each of the 24 graphics to its script beat, approximate timestamp, and placement.

## Render contract (do not break)
- Root div needs id, data-composition-id, data-start="0", data-width, data-height.
- Timed visible elements need class="clip", except <video> and <audio>.
- Every timed element needs data-start, data-duration, data-track-index. Same-track clips cannot overlap.
- Exactly one paused GSAP timeline per composition on window.__timelines["<data-composition-id>"], key matching exactly.
- Never animate width/height/top/left on a <video>; wrap and animate the wrapper.
- Determinism: no Date.now(), no unseeded Math.random(), no render-time network fetches.

## Workflow (mandatory gates)
1. Invoke /hyperframes, read the brand and motion philosophy, and confirm block names with npx hyperframes catalog --type block.
2. Build a composition for every one of the 24 elements above.
3. npx hyperframes lint, then inspect for overflow.
4. Live preview: npx hyperframes preview, hand Ryan the URL, wait for explicit sign-off before any render.
5. Draft render, then read each frame to verify (no cropping, overflow, low-contrast captions, wrong colors). Fix and re-verify.
6. Final render. Captions are generated from Ryan's real recorded audio after he films, via npx hyperframes transcribe. Do not fabricate caption timing before the footage exists.
