---
name: yt-thumbnail
description: "Use when someone asks to design a YouTube thumbnail, make thumbnails for a video, batch thumbnails for the week, A/B test a thumbnail, redesign or refresh an old video's thumbnail, audit click-through rate on the back catalog, or generate a title and thumbnail package."
argument-hint: "video title or topic (e.g. 'new construction traps in Las Vegas'), or 'refresh' to audit the back catalog"
---

# YouTube Thumbnail Designer

Turns a video topic into finished, upload-ready thumbnails: a written strategy brief, an
AI-generated location plate, Ryan's real face at the right expression, brand typography
rendered in HTML, and a 120px proof of what the feed actually shows.

**Trigger:** `/yt-thumbnail [topic]`

Two modes:
- **Design** (default), a new video's thumbnail package: 2 concepts + 2–3 paired titles.
- **Refresh**: audit published videos by click-through rate and redesign the losers.
  See [references/refresh-loop.md](references/refresh-loop.md).

**Supporting files:**
- [references/strategy-brief.md](references/strategy-brief.md), the five questions and the competitive check, answered before any design
- [references/design-rules.md](references/design-rules.md), the squint standard, word counts, colour, banned list
- [references/refresh-loop.md](references/refresh-loop.md), back-catalog CTR audit and diagnosis checklist
- `brands/*.json`: colour, type and plate-style tokens per channel
- `templates/*.html`: the three layouts
- `render.mjs`: Playwright renderer

---

## Before you start

**Pick the brand.** Ryan runs two channels and they must never share design tokens:

| Brand file | Channel | Audience |
|---|---|---|
| `rose-homes` (default) | Rose Homes LV | Las Vegas buyers and sellers |
| `leveraged-agent` | The Leveraged Agent | Agents, Skool community |

If the topic is real estate in Las Vegas, it is `rose-homes`. If it is about AI, systems,
or running an agent business, it is `leveraged-agent`. When genuinely unclear, ask.

**Set up a working folder** at
`Rose Homes LV/Content/Thumbnails/<slug>/` (or `SKOOL Community/Scripts/Thumbnails/<slug>/`
for the other brand). Everything for this video lives there.

---

## Workflow

### Step 1, Write the brief (gate)

Work through all five questions in [references/strategy-brief.md](references/strategy-brief.md)
and run the competitive check. Save `brief.md`.

**Do not skip to designing.** Question 5 produces the physical expression description that
Step 3 needs, and the competitive check decides the colour direction. Without them this is
a template filler, not a designer.

### Step 2, Generate the plate

The plate is the photographic background. Use Higgsfield `generate_image`:

- Model `nano_banana_pro`, `aspect_ratio: "16:9"`, `resolution: "2k"`. Roughly 2 credits.
- Build the prompt from the brand's `plateStyle` and `seasonNotes` plus the specific place.
- Always end the prompt with: `No text, no logos, no people, no watermarks.`
  Text baked into the plate cannot be edited and will fight the headline.

Download the result into the working folder as `plate-<name>.png`.

### Step 3, Expression (optional, needs approval)

The stock cutout at `assets/ryan-cutout.png` is Ryan's real headshot with the background
removed. It has **one expression: smiling**. That is right for reassuring topics and wrong
for warnings, which is the single most common reason a thumbnail reads as inauthentic.

To generate a different expression, use the saved Element:

```
element id: cf5b602a-f8b4-41da-9568-b13356f3d77b   (name: ryan-rose)
model:      nano_banana_pro, aspect_ratio "3:4", resolution "2k", count 2
prompt:     Chest-up studio portrait of <<<cf5b602a-f8b4-41da-9568-b13356f3d77b>>>.
            Same man, same face, same navy blazer and blue check shirt.
            Expression: <the physical description from brief.md question 5>.
            Clean even studio lighting, plain flat light-grey seamless backdrop,
            sharp focus on the eyes. Photographic, not illustrated. No text, no logos.
```

Then run `remove_background` on the chosen result and save it as `cutout-<expression>.png`.

**Approval gate.** This produces an AI image of a real person. Show Ryan both variants and
get an explicit yes before it goes into a thumbnail that will be published. If he has not
approved this specific image, use the stock cutout instead. Never publish a generated
likeness on his say-so from a previous video.

### Step 4, Write the spec and render

Write `spec-<variant>.json` in the working folder. Fields common to every template:
`brand`, `template`, `out`, and optionally `cutout` (defaults to the stock one),
`kicker`, `disclaimer` (defaults to the brand's).

Headline markup, where supported: `[[word]]` renders in the accent colour, `~~word~~`
renders struck through in red, `\n` forces a line break.

**`face-right`**: the workhorse. Copy left, Ryan right.
```json
{ "brand": "rose-homes", "template": "face-right", "kicker": "Las Vegas · 2026",
  "headline": "The New Build\n[[Trap]]", "badge": "$38K Lost",
  "plate": "plate-newbuild.png", "out": "newbuild-a" }
```

**`big-number`**: one stat carries it. Market updates, price points, counts.
```json
{ "brand": "rose-homes", "template": "big-number", "kicker": "Henderson · August",
  "stat": "$381[[K]]", "delta": "4.2%", "direction": "down",
  "label": "What [[Actually]] Sold", "plate": "plate-henderson.png", "out": "henderson-a" }
```

**`vs-split`**: comparisons. Two plates, gold seam, VS badge. Use `|` to add a gold subline.
```json
{ "brand": "rose-homes", "template": "vs-split", "kicker": "Which One Wins?",
  "left": "Summerlin|from $520K", "right": "Henderson|from $445K",
  "plateLeft": "plate-summerlin.png", "plateRight": "plate-henderson.png",
  "out": "summerlin-vs-henderson" }
```

Render:

```bash
node "/Users/ryanrose/Downloads/Claude/_System/skills/yt-thumbnail/render.mjs" spec-a.json
```

Playwright is resolved automatically from `SKOOL Community/hyperframes-student-kit`, so
this runs from any directory. Three files come out next to the spec:

- `<out>.png`: 2560x1440 master
- `<out>-1280.jpg`: the upload file, 1280x720, warns if it exceeds YouTube's 2MB limit
- `<out>-squint.png`: 120px proof

### Step 5, Check the squint proof (gate)

**Read `<out>-squint.png` before showing Ryan anything.** Judge it against the squint
standard in [references/design-rules.md](references/design-rules.md). If the headline is
not readable at 120px, cut words and re-render. Do not present a thumbnail you have not
looked at small.

### Step 6, Deliver

Always deliver **two distinct concepts**, not two tweaks of one. Different layout or
different argument, so the A/B test is worth running. With them:

- 2–3 titles engineered to pair with each thumbnail (see `strategy-brief.md`)
- The brief, so the reasoning is on the record
- Which concept you would ship, and why

---

## Notes

- Every stat on a thumbnail must be defensible in the video and sourced. Brokerage, MLS
  and fair-housing advertising rules apply to thumbnails exactly as they do to copy.
- YouTube overlays the duration badge bottom-right. The templates keep that corner clear.
- Regenerate `assets/ryan-cutout.png` whenever Ryan shoots a new headshot: crop chest-up
  with ffmpeg, upload to Higgsfield, `remove_background`, save the RGBA result.
- If Ryan ever shoots 5–20 varied photos, train a Higgsfield **Soul** instead of using the
  Element. Souls are identity-trained rather than reference-matched and hold likeness far
  better across expressions. That is the upgrade path for this skill.
