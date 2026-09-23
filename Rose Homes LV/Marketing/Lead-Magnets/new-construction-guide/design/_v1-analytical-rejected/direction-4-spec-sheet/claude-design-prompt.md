# Claude Design brief, Direction 4, Spec Sheet

Paste this whole file. It is self contained. You need no other context.

---

## What you are building

A 39 page, print first, Letter sized buyer guide called **Before You Walk Into the Model Home**, plus a matching landing page. It is a Las Vegas, Henderson, and Clark County new construction guide by **Ryan Rose, Real Broker, LLC**. Cold Facebook traffic downloads it, then prints it, then carries it into a builder's sales office.

**The design thesis, never change it: a house is a spec, so the guide reads like the spec.**
Architectural drafting conventions, not decoration. Every page is a drawing sheet.

---

## Non negotiables

1. **Zero em-dashes** (U+2014) anywhere, including CSS comments. Use commas, periods, or "and".
2. **`Real Broker, LLC` gets a designed slot, never a shrunken footnote.** Nevada law requires a licensee's advertising to name the brokerage. It appears in the cover title block, in every page title block, and in the landing page trust block.
3. **The Nevada licence number is currently unknown and renders literally as `[NOT FOUND]`.** Use `.lic__slot { display:inline-block; min-width:11ch; font-family:"IBM Plex Mono"; }`. `[NOT FOUND]` is 11 characters, so any real licence string of 11 characters or fewer drops in with zero reflow. The cover cell reserves a second line so a longer string wraps inside the cell only.
4. **No `position: fixed` anywhere in the guide file.** A fixed element repeats on every printed page. The title block is `position: absolute` inside a `position: relative` sheet. The landing page may use `position: fixed`.
5. **Bullets and numbered markers use `display: flex` with the marker as a real flex child.** Never `li::before { position: absolute }`. The reference notes strip is CSS multi-column, where an absolute marker lands on the first letter.
6. **Tables need `<caption>`, `<th scope>`, and `thead { display: table-header-group }`.**
7. **Never encode meaning in color alone.** Every accent is paired with a word, a rule weight, or a pattern.
8. **No photography, ever.** This direction has no image dependency. Textures are CSS grids and hatches.
9. **Factual only.** Never invent a price, fee, incentive, or rating. Gaps render as `NOT FOUND` in a HOLD treatment.

---

## Palette, exact hexes

```css
--sheet:#FFFFFF;        /* page stock, zero ink, the only page background */
--ink-900:#10161C;      /* graphite, prose, headlines, data, structural borders */
--ink-700:#2B3640;      /* sheet border, box outlines, section rules */
--ink-600:#46525C;      /* deck, value prop body, diagram annotation */
--ink-500:#5A6672;      /* reference notes, title block labels */
--rule-mid:#7C8994;     /* meaning bearing hairline, passes 3:1 */
--rule-hair:#C3CBD1;    /* decorative hairline only */
--grid-line:#E4E9EC;    /* drafting grid, decorative only */
--fill-01:#EFF3F5;      /* schedule header, detail head, phone head */
--fill-02:#F6F8F9;      /* schedule zebra row */
--redline:#B22A15;      /* revision accent: HOLD, NOT FOUND, section ids, CTA */
--redline-deep:#9E2412; /* redline on tint, button hover and border */
--redline-fill:#FCF0ED; /* HOLD header band */
--dim:#14607A;          /* annotation accent: dimensions, DETAIL, leaders */
--dim-deep:#0F4E63;     /* dim on tint, reference markers, note URLs */
--dim-fill:#E6EFF3;     /* DETAIL header band */
--path-a:#10161C;       /* path tab A, white caps */
--path-b:#5A6672;       /* path tab B, white caps */
--path-c:#EFF3F5;       /* path tab C, ink caps, 2.5px ink border */
```

Lowest text contrast in the system is 5.26:1. Every text pair clears WCAG AA. `--rule-hair` and `--grid-line` sit below 3:1 and **may never be the sole carrier of information.**

**Grayscale warning:** `--redline` and `--dim` both land near gray 90 in black and white. That is accepted, so differentiate by **form**: HOLD gets a 2.5px border plus a 45 degree hatch band plus the word HOLD; DETAIL gets a 1px border plus a flat tint plus the word DETAIL.

---

## Type

Load exactly this:

```
https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600;700&family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Sans+Condensed:wght@400;600&family=IBM+Plex+Serif:ital,wght@0,400;0,600;1,400&display=swap
```

| Role | Family |
|---|---|
| Prose | IBM Plex Serif |
| Headlines, structured text, UI | IBM Plex Sans |
| Data, labels, title block, tags | IBM Plex Mono |
| Schedule place names, reference notes | IBM Plex Sans Condensed |

**Forbidden:** Playfair Display, Montserrat, Bebas Neue. Those belong to other Rose Homes LV systems.

Scale, px at 96dpi:

| px | Line height | Tracking | Use |
|---|---|---|---|
| 61 | 1.015 | -0.021em | Cover title, Plex Sans 600 |
| 25.5 | 1.11 | -0.019em | Page headline, Plex Sans 600 |
| 19 | 1.18 | -0.012em | Subhead, Plex Sans 600 |
| 17 | 1.42 | 0 | Cover subtitle, Plex Serif 400 |
| 14 | 1.36 | 0 | Deck, Plex Serif 400 italic |
| 12.9 | 1.35 | 0 | Body prose, Plex Serif 400 |
| 11.8 | 1.30 | 0 | HOLD block body |
| 11 | 1.34 | 0 | Numbered list, checklist, DETAIL, phone block, soft close |
| 10.7 | 1.1 | 0.10em | Section head bar, Plex Sans 500 caps |
| 10.2 | 1.24 | 0 | Title block values, Plex Mono 500 |
| 9.2 | 1.0 | 0.14em | Drafting tags, Plex Mono 600/700 caps |
| 8.7 | 1.2 | 0 | Schedule cells, Plex Mono |
| 8 | 1.1 | 0.14em | Title block labels, Plex Mono 600 caps |
| 7.1 | 1.26 | 0 | Reference notes, Plex Sans Condensed |

Landing headline: `clamp(30px, 3.55vw, 50px)`, line height 1.07, tracking -0.024em.

---

## Layout system

**Sheet geometry, every page:**

- Trim 8.5in x 11in, `overflow: hidden`.
- Drawing border inset 0.30in: 1.5px `--ink-700`, plus an inner 0.5px `--rule-mid` at +0.055in.
- Coordinate margin inside the border: A to F across top and bottom, 1 to 8 down both sides, 7.4px Plex Mono in `--rule-mid`.
- Live area: left and right 0.54in, top 0.42in, bottom 0.94in.
- Two column body zone, 12px gutter with a `--rule-hair` column rule. Ratios `1.04fr 0.96fr` for prose sheets, `0.475fr 0.525fr` for schedule sheets.
- Spacing scale in px: 2, 4, 6, 9, 10, 13, 19, 26, 36.
- **Radii: 0 everywhere.** A drafting sheet has no rounded corners.

**Title block, the signature. Every footer, no exceptions.**
Full width inside the border, 0.51in tall, bottom 0.365in. `grid-template-columns: 2.02fr 1.30fr 0.86fr 0.72fr 0.60fr`. Top edge 2.5px `--ink-900`, 1px `--ink-700` on the other three sides, cells divided by 0.5px `--rule-mid`. Each cell: an 8px Plex Mono uppercase label in `--ink-500` above a 10.2px Plex Mono value in `--ink-900`.

Cells: `PROJECT` / `ISSUED BY` / `VERIFIED AS OF` / `REV` / `SHEET`. The SHEET cell is filled `--fill-01` with a 15px 700 numeral. On path pages 6 to 17 insert a sixth cell, `PATH`, reading `A · MOVING HERE`, and the sheet value becomes `07 · A`.

The cover title block is the same object at 2.28in tall, carrying `AUTHOR OF RECORD: Ryan Rose`, `BROKERAGE OF RECORD, NEVADA: Real Broker, LLC`, `SHEET: 01 of 39`, `EDITION`, `VERIFIED`, `REVISION CYCLE`, and a full width `NEVADA ADVERTISING COMPLIANCE, NRS 645` row holding the licence slot plus a red `HOLD` tag and the contact line.

---

## Component list

| Component | Spec |
|---|---|
| **Section head bar** | `19.0` in Plex Mono 700 + section name in Plex Sans 500 caps + `SHEET 19 · REV A` right aligned, over a 1.5px `--ink-900` rule. |
| **DETAIL box** | 1px `--dim` border. Header band `--dim-fill` with a white on `--dim` id chip (`DETAIL A`) and a title (`19.1 / ASIDE`). Body 11px. For asides and pull quotes. |
| **HOLD block** | 2.5px `--redline` border. 9px hatch strip on top (`repeating-linear-gradient(-45deg, var(--redline) 0 2px, transparent 2px 6px)`). Header band `--redline-fill` with a white on `--redline` `HOLD` chip and a register line. **This is the NOT FOUND treatment. It must read as a tracked open item, never as an apology.** |
| **NOT FOUND cell** | Inside a table: `--redline-deep` 700, dotted 2px `--redline` underline, and a `△` glyph prefix. The words themselves always print. |
| **Schedule (table)** | Plex Mono 8.7px. Header row `--fill-01`, 9.2px 700 caps, 1px `--ink-700` underline. Rows 1.9px padding, 0.5px `--rule-hair` separators, `--fill-02` zebra. Place names in Plex Sans Condensed. Date columns `white-space: nowrap`. `<caption>` reads `Schedule 19.3 · District payment dates`. |
| **Numbered steps** | Flex row. Marker is a 15px square, 1px `--ink-900` border, 8.4px Plex Mono 700 numeral. |
| **Checklist** | Flex row. Marker is a 13px empty square, 1.5px `--ink-900` border, real checkbox affordance. Step number in `--redline` Plex Mono 700, then a bold Plex Sans step name, then plain explanation. |
| **Phone block** | 1px `--ink-700` border with a 2.5px `--ink-900` left edge. `--fill-01` header. Numbers in Plex Mono 700 with a 1.5px `--redline` underline. |
| **Soft close** | Never a boxed CTA. A general note: `GEN. NOTE 19.5` in `--redline` Plex Mono caps as a flex marker, prose beside it, a 1px rule above. |
| **Reference notes strip** | `column-count: 2`, 14px gap, `--rule-hair` column rule. Header reads `REFERENCE NOTES 01 TO 10` with `VERIFIED 2026-07-25` right aligned. Entries render the literal source text including `[source: <url> | verified: <date>]`, with `source:` and `verified:` in Plex Mono 600 and URLs in `--dim-deep` with `overflow-wrap: anywhere`. **Split the run so every marker resolves on its own sheet.** |
| **Diagram field** | 1px `--ink-700` box. Header with a black `SVG-04` id chip. Inline SVG on a CSS grid ground, with callout leaders (a polyline plus a 2.2r dot at the anchor) and dimension bars with tick ends. Caption strip below in 8px condensed. Every inline SVG needs `role="img"`, `<title>`, and `<desc>`. |
| **Dimension line** | Pure CSS: a 1px `--dim` bar with CSS triangle arrowheads via `::before` and `::after`, a Plex Mono value label, and `--dim` tick ends. Decorative, `aria-hidden`. |
| **Edge tab** | Pages 6 to 17 only. Bleeds off the outer edge, stepped at three vertical thirds, caps set bottom to top and tracked open. No text within 5mm of trim. |

---

## Landing page hero

Two column at 1280px: argument left, three value props as a numbered schedule right. Dashed rail across the top (`repeating-linear-gradient(90deg, var(--ink-900) 0 14px, transparent 14px 28px)`). Eyebrow chips, headline, serif subhead with a 2.5px `--dim` left rule, then the button and microcopy on one row.

**Button:** `--redline` fill, 2.5px `--redline-deep` border, white Plex Sans 600 17px, a Plex Mono arrow glyph. Hover darkens to `--redline-deep` and lifts 2px. Focus visible is a 3px `--dim` outline at 3px offset. Never `transition-all`; animate `transform` and `background-color` only, 160ms, `cubic-bezier(.2,.9,.3,1.2)`.

**Trust block:** a bordered cell grid matching the guide title block. Cell 1 `LICENSEE: Ryan Rose`. Cell 2 `BROKERAGE OF RECORD, NEVADA: Real Broker, LLC`. Full width row 3 carries service area, phone, email, and `Nevada license #[NOT FOUND]` in the fixed width slot.

**No `<form>` in the hero.** The button is `<a href="#contact">` and page JS scrolls to the bottom. Lofty appends its own form at publish. Never post to a webhook, never collect a field.

Below 1024px stack to one column. Below 480px the button goes full width. A `position: fixed` bottom action bar is allowed on mobile here and only here.

---

## Print rules

```css
@page { size: letter; margin: 0; }
```

`print-color-adjust: exact` on every sheet. `break-inside: avoid` on DETAIL, HOLD, schedule, schedule rows, phone block, soft close, notes, diagram, title block, steps, checklist items, and note items. `page-break-after: always` on each sheet except the last. Grid fields drop to `opacity: .72` in print.

---

## Things that must never change

- The title block in every footer, carrying sheet number, revision, and verified-as-of date.
- HOLD as the NOT FOUND treatment, hatch band and all.
- Radius 0, everywhere.
- White page stock. No dark panels, no full bleed fills, no photography, no gradients. Ink stays near 5 percent.
- Two accents only, redline and dimension blue, each with a fixed meaning: redline means open item or act, blue means measured annotation.
- `Real Broker, LLC` in a labelled cell of its own.
- Flexbox list markers.

## Known cost, keep it in view

At the source strip's specified 7pt over 1.35 and body prose at 10.5pt over 1.55, the SID and LID spread runs about 4.2 inches long across two sheets. The preview holds two sheets by setting prose at 9.7pt and notes at 5.3pt. **The correct fix is a third sheet, 20A, not smaller type.** Drawing sets use continuation sheets and this system absorbs one cleanly.
