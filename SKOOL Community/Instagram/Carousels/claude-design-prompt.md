# Claude Design Brief: Carousel 01, Transaction Coordination

This is the **DESIGN BRIEF** in the format the source `carousel-writer` skill specifies:
per slide, the exact text and the visual direction, brand baked in. Paste the block below
into Claude Design as one message.

**Brand: v2.0 "Vector"** (adopted 2026-08-19). Do not attach the logo PNGs, every logo file
is still v1 cream/teal/gold artwork and is off-palette. Use the typographic wordmark
described below until the logos are regenerated.

---

## PASTE THIS INTO CLAUDE DESIGN

> Build a 9-slide Instagram carousel, each slide exactly 1080 x 1350 px (4:5), as one
> self-contained HTML file with inline CSS and inline SVG. Render all nine so I can
> screenshot them.
>
> **Brand: The Leveraged Agent.** Coaching community teaching real estate agents to run
> their business with AI. Calm, confident, technical field-manual feel. Educational, never
> promotional.
>
> **Colors, exact, nothing else:** white `#FFFFFF` base, sunken fill `#F7F8FA`, hairline
> `#E4E7EF`, TRUE black `#000000` as a full-bleed surface only and never as text, navy ink
> `#050E3D`, secondary ink `#55627F`, one accent `#1768E5` (works as fill and as text on
> white), and `#5B9BFF` as the accent on black. On black slides text is `#FFFFFF` with
> `#9AA3BC` secondary. No warm colors, no second darker accent, no gradients, no shadows.
>
> **Fonts, Google Fonts:** Barlow 800 headlines at letter-spacing `-0.028em`, line-height
> 1.02. Raleway 600 for labels and eyebrows only, uppercase, letter-spacing `0.15em`. Inter
> 400/500 body at line-height 1.6. No serifs. The 800-to-400 weight gap is the entire
> hierarchy.
>
> **Layout, every slide:** 92px top / 88px side / 150px bottom padding. Copy top-left,
> headline max 12ch (14ch at the smaller size), body max 21ch. A 14px full-bleed accent rule
> along the very bottom of every slide (`#1768E5` on white, `#5B9BFF` on black).
>
> **Illustration is required.** Every slide carries one inline-SVG line illustration in the
> lower half. Rounded caps and joins, mixed stroke weights (9px primary, 6-7px secondary,
> 4-5px detail), white fills on shapes that must occlude what sits behind them, accent fill
> used sparingly on exactly one element. Keep all SVG geometry inside the 88px side margins,
> `svg{overflow:visible}` will silently let art escape the margin. No photos, no icon fonts,
> no emoji, no clipart.
>
> **Wordmark:** "THE LEVERAGED AGENT" in Raleway 600, 23px, uppercase, `0.15em` tracking,
> bottom-left of every slide, "AGENT" in the accent color.
>
> **Structure:** slides 1, 7 and 9 are full-bleed TRUE black. The rest are white. That
> black-against-white cut is the pop, not the accent color.
>
> **Slide 1, cover, black.** Eyebrow "AI TRANSACTION COORDINATOR". Headline: "I have 3 deals
> on my board. Claude writes every email." with "3 deals" and "every" in `#5B9BFF`. Visual:
> three folders on a baseline, the two on the left in muted outline, the third larger, filled
> dark navy with an accent outline and short spark lines radiating off its top corner.
> "SWIPE" in Raleway 600 bottom-right.
>
> **Slide 2.** Eyebrow "01". Headline: **A transaction is not one job, it is 17 deadlines** /
> "Inspection, appraisal, loan docs, HOA, walkthrough, signing. Miss one date and you are the
> reason it fell apart." Visual: 17 pin markers standing on a navy baseline, varying heights,
> all in hairline grey except one that has snapped, a short stub still standing with the rest
> of the pin lying on the line in accent blue and three small break marks above it. Label
> "ONE MISSED" beneath it.
>
> **Slide 3.** Eyebrow "02". Headline: **The folder is the system** / "One folder per deal.
> Contract, addenda, dates, contacts. Claude reads that folder before it writes anything."
> Visual: a large accent-outlined folder, three grey sheets fanned out of its mouth at
> slightly different angles, four pill-shaped tabs inside it reading Contract, Addenda,
> Dates, Contacts, and a magnifier inside the folder on the right.
>
> **Slide 4.** Eyebrow "03". Headline: **Dates come from the contract, not your memory** /
> "Drop the executed contract in. The skill pulls every deadline and builds the calendar in
> one pass." Visual: a contract page on the left, an accent arrow flowing right into a month
> grid with three cells filled accent.
>
> **Slide 5.** Eyebrow "04". Headline: **Every email you send twice is a template** / "Escrow
> opening, inspection notice, appraisal update, clear to close. Written once, reused on all
> three deals." Visual: one accent envelope tilted on top of a stack of grey ones, three
> accent motion lines running right into three stacked folders labeled DEAL 1, DEAL 2,
> DEAL 3.
>
> **Slide 6.** Eyebrow "05". Headline: **The CC list is part of the template** / "Listing
> agent and their TC on every transaction email. Build it into the file so you never forget."
> Visual: a compose-window mock with a title bar reading NEW MESSAGE, then TO / CC / SUBJ
> rows. The CC row is a full-width accent block reading "Listing agent + their TC" with two
> overlapping white avatar circles at its right end.
>
> **Slide 7, black.** Eyebrow "06". Headline: **Do this instead of a spreadsheet** / "A
> spreadsheet stores dates. A skill reads the contract, writes the email, and tells you what
> is late." Visual: split frame, left a dim grey grid labeled SPREADSHEET, right a panel
> outlined in `#5B9BFF` labeled SKILL containing a chevron prompt.
>
> **Slide 8.** Eyebrow "07". Headline: **Start with your ugliest deal** / "Pick the file you
> are most behind on. Build the folder today. The next deal inherits the whole thing."
> Visual: a messy pile of tilted grey pages on the left, an accent arrow labeled TODAY
> pointing right into one clean accent-outlined folder carrying a large "1".
>
> **Slide 9, final, black.** Headline: DM me "TC" and I will send you the folder structure I
> use. Visual: "TC" set very large in `#5B9BFF`, the CTA line beneath in Barlow 800 white.
> Nothing else.
>
> Use my copy verbatim. Do not add slides, taglines, handles, page numbers, or any color
> outside the palette above.

---

## Iterating

One instruction at a time, it holds the rest steady.

- "Slide 4 has dead space between the copy and the visual. Pull the visual up."
- "Slide 3's fanned sheets are breaking the folder outline. Redraw them behind it."
- "Regenerate slide 9 only. Everything else stays."

## Reusing for the next carousel

The brand block is locked. Replace only the per-slide lines, then paste:

> Same layout, colors, fonts, illustration style and black/white rhythm as before. Rebuild
> the nine slides with this content: [paste new slide lines]

## Local alternative

`render.html` and `shoot.mjs` in this folder build the same thing with Playwright. Run
`node shoot.mjs`, PNGs land in `png/`. Use Claude Design when you want fresh visual
directions to compare. Use the local build when you want the exact locked layout back in ten
seconds. `render-v1-archive.html` is the retired v1 cream/teal/gold version, kept for
reference only, do not ship from it.
