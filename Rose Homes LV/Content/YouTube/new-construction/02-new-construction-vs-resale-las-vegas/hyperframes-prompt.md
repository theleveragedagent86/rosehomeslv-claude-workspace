# Build the graphics package for: New Construction vs. Resale in Las Vegas: How to Choose

## Context
You are building a graphics overlay package for a 16:9 1920x1080 long-form YouTube video for Ryan Rose (Rose Homes LV). Ryan films himself on camera reading the script, and these graphics get cut into his footage. Do not render a full talking-head video, only the graphic elements listed below. The video runs about 8 minutes. The theme is a fair, side-by-side comparison of new construction versus resale homes in the Las Vegas valley, so the two-column comparison cards are the visual backbone of this package. Treat new construction as one consistent visual side and resale as the other side, every time they appear.

## Setup
- Invoke the /hyperframes skill family first (/hyperframes, /hyperframes-cli, /gsap, /hyperframes-registry). Do not hand-write GSAP from memory.
- Read MOTION_PHILOSOPHY.md at the hyperframes-student-kit workspace root, and the Rose Homes Brandkit at /Users/ryanrose/Downloads/Claude/SKOOL Community/hyperframes-student-kit/Rose Homes Brandkit/. Use Ryan's brand fonts and colors, not the Skool sample theme.
- Scaffold a 16:9 1920x1080 at 30fps project at /Users/ryanrose/Downloads/Claude/SKOOL Community/hyperframes-student-kit/video-projects/ytlong-new-construction-vs-resale-las-vegas/. Run all CLI from inside it.
- Confirm exact block names before you build with: npx hyperframes catalog --type block. The suggested blocks below are guidance, not literal names.

## Visual system for the two sides (use this everywhere new vs resale appears)
- New construction side: assign one brand accent color, a "new build" icon motif (a fresh house outline or a sun over a young tree), and always place it on the LEFT column.
- Resale side: assign a second, clearly different brand-approved color, a "resale" icon motif (a house with a mature tree), and always place it on the RIGHT column.
- Keep the left = new, right = resale order consistent across every compare card, the list cards, and the outro split-screen so viewers learn the visual shorthand.

## Graphic elements to build
One row per [GFX] cue in the script. All 26 cues are represented. There are 0 NOT FOUND placeholders in this script.

| # | Script beat (approx timestamp) | Cue type | Exact on-screen text / data | Source | Suggested block | On-screen duration |
|---|--------------------------------|----------|-----------------------------|--------|-----------------|--------------------|
| 1 | Hook open, 0:00 to 0:10 | stat | Two big numbers side by side: "Over $500,000" labeled "New home (median)" and "About $475,000" labeled "Existing home (median)". Caption under: "About $30,000 more for new". One idea: new costs more up front. | VEGAS INC / LVR 2026 | Big-number / stat card, eased count-up on both figures | 5 to 6 s |
| 2 | After hook line, 0:10 | title-card | "New vs. Resale" line 1, "How to Choose" line 2 | n/a | Kinetic title card, brand fonts, short hold | 2 to 3 s |
| 3 | Into intro, ~0:30 | transition | Medium energy push or whip-pan into the intro | n/a | Shader transition (push / whip-pan) | 0.4 to 0.7 s |
| 4 | "I'm Ryan Rose", ~0:35 | lower-third | "Ryan Rose" name, "Real Broker, LLC" descriptor | n/a | yt-lower-third registry block | 4 to 5 s |
| 5 | Before Section 1, ~1:05 | transition | Calm crossfade or blur into chapter 1 | n/a | Shader transition (blur / crossfade) | 0.5 to 0.8 s |
| 6 | Start Section 1, ~1:10 | chapter | Eyebrow "1" and title "Price and what's included" | n/a | Chapter / section title card | 2.5 to 3 s |
| 7 | Median price line, ~1:20 | compare | LEFT (New): "$500,000+ median". RIGHT (Resale): "About $475,000 median". Header "Median price". | VEGAS INC / LVR 2026 | Two-column comparison | 5 to 6 s |
| 8 | Price per sq ft line, ~1:35 | stat | Big number "$258 / sq ft" with subhead "Resale, down 5% year over year" and small line "Most areas $180 to $220". One idea: resale per-foot cost. | Redfin 2026 | Big-number stat card, count-up to 258 | 5 to 6 s |
| 9 | Window coverings line, ~1:55 | stat | Big number "$150 to $300 per window" subhead "Blinds, often not included on new" | LV Window Coverings Center 2026 | Big-number stat card, count-up on range | 4 to 5 s |
| 10 | Backyard line, ~2:10 | stat | Big number "$3,900 to $26,000" subhead "Typical backyard finishing on a new build" | Homeyou 2026 | Big-number stat card, count-up on range | 4 to 5 s |
| 11 | End Section 1, ~2:35 | transition | Medium push into Section 2 | n/a | Shader transition (push / whip-pan) | 0.4 to 0.7 s |
| 12 | Start Section 2, ~2:40 | chapter | Eyebrow "2" and title "Location, lot, and your timeline" | n/a | Chapter / section title card | 2.5 to 3 s |
| 13 | Rim vs core line, ~2:50 | map | Simple stylized Las Vegas valley map. Highlight the rim/edges labeled "New construction" with pins near Skye Canyon (north) and newer Henderson. Highlight the built-out center labeled "Resale" with pins near Green Valley and Spring Valley. | Vice Realty / Skye Canyon 2026 | Location / map graphic | 6 to 7 s |
| 14 | Landscaping and services line, ~3:05 | compare | LEFT (Rim new build): "Modern wiring", "Fresh floor plan", "Young trees, more sun". RIGHT (Core resale): "Grown trees and shade", "Established shops and schools". Header "Rim new build vs Core resale". | Vice Realty / Skye Canyon 2026 | Two-column comparison, staggered rows | 6 to 7 s |
| 15 | Timeline question, ~3:30 | broll | Motion graphic: calendar pages flipping fast, then a moving truck pulling up to a house. Light caption "Move in months, or weeks?" | n/a | Motion-graphic interlude (full frame) | 4 to 5 s |
| 16 | After client story, ~4:05 | transition | High energy cinematic zoom or glitch into Section 3 | n/a | Shader transition (cinematic-zoom / glitch) | 0.5 to 0.8 s |
| 17 | Start Section 3, ~4:10 | chapter | Eyebrow "3" and title "Repairs, warranties, and peace of mind" | n/a | Chapter / section title card | 2.5 to 3 s |
| 18 | Warranty line, ~4:20 | list | Two-item compare-style list. LEFT (New): "Builder warranty, a builder to call". RIGHT (Resale): "Rely on a good inspection, optional home warranty". Header "Who has your back?" | Rose Homes blog / Vice Realty 2026 | Animated bullets with stagger, two-column layout | 6 to 7 s |
| 19 | Summer heat line, ~4:45 | broll | Motion graphic: Las Vegas summer heat shimmer rising over a rooftop, an AC unit running. Light caption "Vegas heat is brutal on AC, water heaters, plumbing". | n/a | Motion-graphic interlude (full frame) | 4 to 5 s |
| 20 | End Section 3, ~5:20 | transition | Medium push into the takeaways section | n/a | Shader transition (push / whip-pan) | 0.4 to 0.7 s |
| 21 | Start takeaways, ~5:25 | chapter | Eyebrow "4" and title "Monthly costs and how to decide" | n/a | Chapter / section title card | 2.5 to 3 s |
| 22 | HOA range line, ~5:30 | stat | Big number "$29 to $3,800 / month" subhead "Las Vegas HOA range, tied to amenities" | Julia Grambo 2026 | Big-number stat card, count-up on range | 5 to 6 s |
| 23 | HOA structure line, ~5:45 | compare | LEFT (New master plan): "Skye Canyon about $83/mo", "Summerlin about $69 to $76/mo plus about $37 council", "Cadence about $40 to $100/mo". RIGHT (Older neighborhood): "Light HOA, or none at all". Header "HOA structure". | Skye Canyon / RJ / Julia Grambo 2026 | Two-column comparison | 7 to 8 s |
| 24 | Decision steps, ~6:15 | list | Three numbered bullets: "1. Add up the real cost, not the sticker", "2. Match it to your timeline", "3. Decide who handles repairs". | n/a | Animated bullets with stagger | 6 to 7 s |
| 25 | Outro one-thing line, ~7:10 | broll | Motion graphic split screen: a new-build street with bare lots and skinny trees on the left, crossfading to an established tree-lined street on the right. Reinforces "no better home, only the better fit". | n/a | Motion-graphic interlude (full frame), left = new, right = resale | 5 to 6 s |
| 26 | Final CTA, ~7:40 | cta-card | "Ryan Rose, Real Broker LLC", "702-747-5921", "rosehomeslv.com", soft line "I'll run your real numbers on both paths." | n/a | logo-outro or branded CTA card | 5 to 7 s |

## Design rules
- Keep the intro short and value-first, no long branded sting. The title card (row 2) is a quick hold, not a full intro animation.
- One idea per graphic. Strip decoration so a number or chart reads at a glance. Animate simply (count-ups, bars or rows from zero, eased), keep motion subtle.
- Show graphics on transitions and supporting points, just after the line they reinforce. Hide them during Ryan's most important lines (the client story and the closing "one thing to take with you") so they do not compete with his face.
- Keep the new vs resale visual system identical across rows 1, 7, 14, 18, 23, and 25 so the comparison reads instantly.
- Captions: white text on a semi-transparent black band, WCAG contrast at least 4.5:1, no more than about 32 characters per line, no more than 2 to 3 lines, on screen about 3 to 7 seconds, bottom-center and clear of lower-thirds.
- Keep all text inside title-safe margins and large enough to read on a phone.
- Brand consistency: same fonts, colors, lower-third style, music family throughout.
- Outro carries the single soft CTA (702-747-5921, rosehomeslv.com) plus a next-video hand-off to Ryan's full new-construction buying process video.
- No em-dashes in any on-screen text. Use commas, periods, or "and".
- Factual only. Use only the numbers and labels in the table above. Do not invent prices, square footage, HOA amounts, or sources.

## Output
- Overlays (lower-third, stat cards, compare cards, list cards, map, captions): transparent WebM (npx hyperframes render --format webm).
- Full-frame interludes (title card, chapter cards, b-roll motion graphics, outro CTA): MP4.
- Put renders in renders/, and write a graphics-shot-list.md mapping each graphic to its script beat and placement.

## Render contract (do not break)
- Root div needs id, data-composition-id, data-start="0", data-width, data-height.
- Timed visible elements need class="clip", except <video> and <audio>.
- Every timed element needs data-start, data-duration, data-track-index. Same-track clips cannot overlap.
- Exactly one paused GSAP timeline per composition on window.__timelines["<data-composition-id>"], key matching exactly.
- Never animate width/height/top/left on a <video>; wrap and animate the wrapper.
- Determinism: no Date.now(), no unseeded Math.random(), no render-time network fetches.

## Workflow (mandatory gates)
1. Invoke /hyperframes, read the brand and motion philosophy.
2. Build a composition for every element above (26 in total).
3. npx hyperframes lint, then inspect for overflow, especially the multi-row compare cards (rows 14 and 23) which hold the most text.
4. Live preview: npx hyperframes preview, hand Ryan the URL, wait for explicit sign-off before any render.
5. Draft render, then read each frame to verify (no cropping, overflow, low-contrast captions, wrong colors, consistent left = new / right = resale). Fix and re-verify.
6. Final render. Captions sync to Ryan's real recorded audio after he films, via npx hyperframes transcribe. Do not generate caption timing before filming.
