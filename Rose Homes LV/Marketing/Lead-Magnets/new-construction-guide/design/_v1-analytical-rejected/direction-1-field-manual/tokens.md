# Direction 1: Field Manual, design tokens

**Thesis:** a tool you carry into the model home, not a brochure you read on the couch.

Two ink colors and one paper. Everything else is a tint or a rule weight. The system is
built so a home laser printer, a phone screen, and a commercial press all produce the same
document, and so a reader can write on it with a ballpoint.

---

## 1. Color

| Token | Hex | Role |
|---|---|---|
| `--ink` | `#101418` | Maximum ink. Bars, display type, heavy rules, checkbox strokes, table header ground, numbered markers. |
| `--text` | `#2A3138` | Body prose, table cells, callout body. The only color running text is ever set in. |
| `--muted` | `#5A646D` | Source log entries and URLs, field labels, figure captions, running head secondary. |
| `--signal` | `#8F2D08` | Signal on paper. Citation numerals, beat lines, the kicker rule, NOT FOUND cell marks, write-in block labels. Never used for running text. |
| `--signal-bright` | `#E8641A` | Signal on dark ground only. Landing button fill, cover masthead rule, cover nameplate border, hero eyebrow and brokerage line. |
| `--signal-tint` | `#F7E9DF` | Field for the aside and the NOT FOUND callout. 6 percent tint of the signal hue. |
| `--paper` | `#FFFFFF` | Page stock. Interior pages are white. |
| `--rail` | `#EFEEE9` | Note rail field. The tint that tells a reader "this column is yours." |
| `--zebra` | `#F5F4F0` | Table alternate row. Deliberately 2 L\* off paper so it never fights the source log below it. |
| `--rule` | `#C6C4BC` | Ruled writing lines, table hairlines, figure frames. Non-text, no contrast requirement. |
| `--night` | `#14181D` | Cover ground and landing hero ground. The only two places dark ground appears. |
| `--night-muted` | `#C9D0D7` | Secondary text on `--night`. |

**Scaffolding, not part of the palette:** the preview page sits on `#6b6b6b` so white stock
reads as paper. That gray never appears in a printed or published file.

### Why this palette

Graphite plus one high visibility signal orange is the color language of equipment: aviation
checklists, inspection clipboards, survey stakes, hazard plates. It is the opposite of a real
estate brochure, which is the point. It is also the most conversion honest palette available
here, because the single accent means there is never a question about what to click or what
to look at. One accent, one button, one answer.

It is deliberately far from Rose Homes LV. No navy, no champagne gold, no warm off white.
A reader who has seen Ryan's listing marketing will not think this is the same document,
and that separation is useful: the guide is meant to read as a reference, not as an ad.

---

## 2. WCAG contrast, computed

Computed with the WCAG 2.1 relative luminance formula in `python3`, not asserted.
AA thresholds used: **4.5:1** for normal text, **3:1** for large text, where large means
24px+ at any weight or 18.66px+ at weight 700. A weight of 600 is not treated as bold,
so 600 weights are held to the 4.5 threshold even above 18.66px.

| fg token | fg hex | bg token | bg hex | size / weight | ratio | AA needs | result |
|---|---|---|---|---|---|---|---|
| `--text` | #2A3138 | `--paper` | #FFFFFF | 14px / 400 | **13.17** | 4.5 | PASS |
| `--text` | #2A3138 | `--rail` | #EFEEE9 | 10.5px / 400 | **11.33** | 4.5 | PASS |
| `--text` | #2A3138 | `--signal-tint` | #F7E9DF | 11.5px / 400 | **11.08** | 4.5 | PASS |
| `--text` | #2A3138 | `--zebra` | #F5F4F0 | 11.5px / 400 | **11.96** | 4.5 | PASS |
| `--ink` | #101418 | `--paper` | #FFFFFF | 34px / 700 | **18.50** | 3.0 | PASS |
| `--ink` | #101418 | `--paper` | #FFFFFF | 11.5px / 600 | **18.50** | 4.5 | PASS |
| `--ink` | #101418 | `--rail` | #EFEEE9 | 15.5px / 700 | **15.92** | 4.5 | PASS |
| `--ink` | #101418 | `--signal-tint` | #F7E9DF | 26px / 700 | **15.57** | 3.0 | PASS |
| `--ink` | #101418 | `--signal-bright` | #E8641A | 22px / 700 | **5.52** | 3.0 | PASS |
| `--muted` | #5A646D | `--paper` | #FFFFFF | 9.33px / 400 | **6.04** | 4.5 | PASS |
| `--muted` | #5A646D | `--paper` | #FFFFFF | 8.3px / 400 | **6.04** | 4.5 | PASS |
| `--muted` | #5A646D | `--rail` | #EFEEE9 | 8.5px / 600 | **5.20** | 4.5 | PASS |
| `--signal` | #8F2D08 | `--paper` | #FFFFFF | 21px / 700 | **8.25** | 3.0 | PASS |
| `--signal` | #8F2D08 | `--paper` | #FFFFFF | 8.5px / 600 | **8.25** | 4.5 | PASS |
| `--signal` | #8F2D08 | `--paper` | #FFFFFF | 10px / 600 | **8.25** | 4.5 | PASS |
| `--signal` | #8F2D08 | `--signal-tint` | #F7E9DF | 8px / 600 | **6.94** | 4.5 | PASS |
| `--paper` | #FFFFFF | `--ink` | #101418 | 9.5px / 600 | **18.50** | 4.5 | PASS |
| `--paper` | #FFFFFF | `--ink` | #101418 | 12px / 700 | **18.50** | 4.5 | PASS |
| `--paper` | #FFFFFF | `--night` | #14181D | 64px / 700 | **17.82** | 3.0 | PASS |
| `--paper` | #FFFFFF | `--night` | #14181D | 19px / 400 | **17.82** | 4.5 | PASS |
| `--paper` | #FFFFFF | `--night` | #14181D | 70px / 700 | **17.82** | 3.0 | PASS |
| `--signal-bright` | #E8641A | `--night` | #14181D | 22px / 600 | **5.32** | 4.5 | PASS |
| `--signal-bright` | #E8641A | `--night` | #14181D | 11px / 600 | **5.32** | 4.5 | PASS |
| `--signal-bright` | #E8641A | `--night` | #14181D | 14px / 600 | **5.32** | 4.5 | PASS |
| `--night-muted` | #C9D0D7 | `--night` | #14181D | 11.5px / 400 | **11.45** | 4.5 | PASS |
| `--night-muted` | #C9D0D7 | `--night` | #14181D | 18px / 400 | **11.45** | 4.5 | PASS |
| `--night-muted` | #C9D0D7 | `--night` | #14181D | 12.5px / 500 | **11.45** | 4.5 | PASS |

**Lowest ratio actually used: 5.20:1.** Zero failures. There is no pair in this system that
sits between 4.5 and 5.2, so a future tint shift of a few percent will not push anything under.

**Pairs that are deliberately never made.** `--signal` is never set on `--night`
(2.20:1) and `--signal-bright` is never set on `--paper` (3.54:1, fails normal text).
The signal color has a light-ground variant and a dark-ground variant and they do not swap.
Enforce this in review.

---

## 3. Grayscale ladder

Every token converted to CIE L\* so a black and white laser print can be predicted.

| token | hex | grayscale L\* |
|---|---|---|
| `--ink` | #101418 | 6.1 |
| `--night` | #14181D | 8.0 |
| `--text` | #2A3138 | 19.9 |
| `--signal` | #8F2D08 | 33.4 |
| `--muted` | #5A646D | 41.8 |
| `--signal-bright` | #E8641A | 58.4 |
| `--rule` | #C6C4BC | 79.1 |
| `--signal-tint` | #F7E9DF | 93.2 |
| `--rail` | #EFEEE9 | 94.0 |
| `--zebra` | #F5F4F0 | 96.2 |
| `--paper` | #FFFFFF | 100.0 |

Five of the six ink tones are separated by 8 to 21 L\*, which survives a home laser printer.
The collision is at the light end: `--signal-tint` 93.2 and `--rail` 94.0 are the same gray.
**Mitigation, and it is structural, not chromatic:** every tinted panel carries a 2px `--ink`
border or a solid `--ink` header bar, so the boundary between a callout and the rail is a
black line, never a tone change. Do not remove those borders to "clean up" the design.

---

## 4. Type

**Google Fonts, single request:**

```
https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700&family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap
```

| Role | Family | Weights loaded |
|---|---|---|
| Display: cover title, headlines, subheads, rail headings, button, table headers | **Barlow Condensed** | 500, 600, 700 |
| Body: all running prose, callout body, table cells, checklist text | **IBM Plex Sans** | 400, 500, 600, 700 |
| Data: source log, URLs, dates, phone numbers, district ids, all labels, license slot | **IBM Plex Mono** | 400, 500, 600 |

**Why this pairing.** Barlow Condensed is a low contrast grotesk drawn from California public
signage. It sets a nine word cover title at 64px on one page without a second line break, it
reads as stenciled equipment lettering rather than as a luxury serif, and it has a full
lowercase and five weights, which Bebas Neue does not. IBM Plex Sans was drawn for technical
documentation and holds up at 10.5pt with generous leading, which is exactly the 6th grade
reading level requirement. IBM Plex Mono is its designed companion, so the source log, the
dates, and the phone numbers sit in the same skeleton as the body instead of looking bolted on.
A monospace is not decoration here: it is what makes a URL and a parcel number readable, and
it is what makes a blank field look like a field.

Distance from Rose Homes LV is total: no Playfair Display, no Montserrat, no Bebas Neue.

### Type scale

| Use | Family | px | Line height | Tracking | Weight |
|---|---|---|---|---|---|
| Cover title | Barlow Condensed | 98 | 0.86 | -0.005em | 700, uppercase |
| Cover byline name | Barlow Condensed | 38 | 0.95 | 0.005em | 700, uppercase |
| Cover subtitle | IBM Plex Sans | 19 | 1.42 | 0 | 400 |
| Cover geography | Barlow Condensed | 22 | 1.0 | 0.13em | 600, uppercase |
| Cover brokerage line | IBM Plex Mono | 14 | 1.0 | 0.13em | 600, uppercase |
| Cover credibility, legal | IBM Plex Mono | 11.5 | 1.85 | 0.02em | 400 |
| Cover eyebrow, plate labels | IBM Plex Mono | 9 to 11 | 1.0 | 0.22 to 0.26em | 600, uppercase |
| Page headline | Barlow Condensed | 34 | 0.93 | -0.008em | 700 |
| Deck | IBM Plex Sans | 14.5 | 1.36 | 0 | 500 |
| **Body prose** | **IBM Plex Sans** | **14 (10.5pt)** | **1.45** | **0** | **400** |
| Beat line | Barlow Condensed | 21 | 1.04 | 0.005em | 700, uppercase |
| Subhead | Barlow Condensed | 19 | 1.0 | 0.09em | 700, uppercase |
| Rail heading | Barlow Condensed | 15.5 | 1.04 | 0.03em | 700, uppercase |
| Rail list body | IBM Plex Sans | 10.5 | 1.30 | 0 | 400 |
| Checklist body | IBM Plex Sans | 10.5 | 1.34 | 0 | 400 |
| Aside body | IBM Plex Sans | 11.5 | 1.40 | 0 | 400 |
| Callout head | Barlow Condensed | 26 | 0.94 | -0.005em | 700 |
| Callout body | IBM Plex Sans | 11.5 | 1.40 | 0 | 400 |
| Table header | Barlow Condensed | 12 | 1.15 | 0.03em | 700, uppercase |
| Table cell | IBM Plex Sans | 11.5 | 1.15 | 0 | 400 |
| Table date, district id | IBM Plex Mono | 10 to 11.5 | 1.15 | -0.01em | 400 to 600 |
| Phone number | IBM Plex Mono | 12.5 | 1.36 | 0.01em | 600 |
| **Source log entry** | **IBM Plex Sans** | **9.33 (7pt)** | **1.32** | **0** | **400** |
| Source log URL | IBM Plex Mono | 8.3 | 1.32 | 0 | 400 |
| Citation numeral | IBM Plex Mono | 8.5 | 0 (superscript) | 0 | 600 |
| Rail label, field label | IBM Plex Mono | 7.5 to 8.5 | 1.0 | 0.16 to 0.22em | 600, uppercase |
| Figure caption | IBM Plex Mono | 7.2 | 1.42 | 0.04em | 600, uppercase |
| Hero headline | Barlow Condensed | clamp(40, 4.9vw, 70) | 0.94 | -0.01em | 700, uppercase |
| Hero subhead | IBM Plex Sans | 18 | 1.58 | 0 | 400 |
| Hero button | Barlow Condensed | 22 | 1.0 | 0.09em | 700, uppercase |
| Hero microcopy | IBM Plex Mono | 12.5 | 1.0 | 0.06em | 500 |
| Hero trust line | IBM Plex Mono | 13 | 1.85 | 0.02em | 400, brokerage at 600 |
| Value prop title | Barlow Condensed | 19 | 1.1 | 0.02em | 700, uppercase |
| Value prop body | IBM Plex Sans | 13 | 1.5 | 0 | 400 |

**The 10.5pt floor.** `page-budget.md` sets 10.5pt over 1.55 as the body standard and forbids
shrinking type to fit. This direction holds 10.5pt for every word of running prose and takes
its leading down to 1.45 rather than its size down. Structured content (table cells, checklist
items, the rail list) sets between 10.5 and 11.5pt, which is normal for tabular matter and is
not "shrinking the body."

---

## 5. Spacing, rules, radii

**Spacing scale, 4pt base.** `4 / 8 / 12 / 16 / 22 / 30 / 40 / 56`. Nothing between steps.
Vertical rhythm inside a text column runs on 7 to 12px block gaps; anything larger is a
structural break and gets a rule.

**Rule weights.** Five, and each one means something.

| Token | Weight | Means |
|---|---|---|
| `--hair` | 0.5pt | Table row separators, source log column rule. Data only. |
| `--thin` | 1px | Ruled writing lines, figure frames, plate dividers. |
| `--med` | 2px | Block boundary: a callout edge, a table header underline, a rail note divider, the running head rule. |
| `--heavy` | 3px | Column boundary: the top of the rail, the top of the source log band, the left bar on the soft close. |
| `--bar` | 5px | Signal bar. The kicker above a headline, the left edge of an aside, the cover masthead rule. |

**Radii.** `0` everywhere in the guide. `2px` on the landing button only, which is the single
concession to a screen affordance. A field manual does not have rounded corners.

**Page geometry, Letter.**

```
trim            8.5in x 11in
margin top      0.34in
margin bottom   0.30in
margin outer    0.36in
margin inner    0.50in   (binding side, wider)
live measure    7.64in x 10.36in
column rail     2.47in   (36 percent, always on the OUTER edge)
column gap      0.22in
column main     4.95in   (64 percent, always toward the gutter)
running head    0.34in band, 2px --ink rule beneath
source log band 1.24in (page 19) / 1.52in (page 20), 3px --ink rule above, 2 columns
```

The rail mirrors: on a verso page it sits left, on a recto page it sits right. A closed,
folded guide therefore has writing space at both thumbs.

---

## 6. Print rules

```css
@page { size: letter; margin: 0; }
```

- Every page container is a fixed `8.5in x 11in` box with `page-break-after: always`.
  Nothing relies on content flow.
- `print-color-adjust: exact` and `-webkit-print-color-adjust: exact` on `*` inside
  `@media print`, so the rail tint, the callout ground, and the black bars actually print.
- `break-inside: avoid` on: callouts, asides, the phone block, the write-in block, figures,
  every `li` in a checklist or numbered list, every table row, every source log entry,
  every fill-in field, and the landing card.
- `thead { display: table-header-group }` and `tfoot { display: table-footer-group }` so a
  long table repeats its header if it ever breaks. `<caption>` is set and visible as
  `TABLE 19.1 · DISTRICT PAYMENT SCHEDULE`.
- **No `position: fixed` anywhere in the guide panels.** A fixed element repeats on every
  printed page and `qa-check.py` fails the build on it. The landing hero may use it; this
  direction does not need to.
- Bullets and numbered markers use the flexbox pattern: `display: flex` with the marker as a
  real flex child (`flex: 0 0 <size>`) and the text as `flex: 1 1 auto; min-width: 0`.
  **Never `li::before { position: absolute }`.** Under CSS multi-column an absolute marker
  lands on the first letter of the text. That bug has shipped twice in this workspace.
- Tab and rail text keeps a 5mm safety from trim so a 3mm home printer variance does not
  clip it.
- Images: none exist. Placeholders are CSS only (gradient, hatch, flat tone) with a visible
  caption naming what belongs there and an `aria-label` on the block. No external URLs.
- Inline SVG carries `role="img"`, `<title>`, `<desc>`, and `aria-labelledby`.

---

## 7. The `[NOT FOUND]` license slot

```css
.slot{
  display: inline-block;
  min-width: 10.5ch;                 /* holds "S.0123456" and longer */
  text-align: left;
  font-family: 'IBM Plex Mono', monospace;
  font-weight: 600;
  border-bottom: 1px solid var(--signal-bright);  /* --signal on light ground */
  padding-bottom: 1px;
}
```

Rendered literally as `[NOT FOUND]`. Because it is an inline-block with a fixed `min-width` in
`ch` of a monospace face, dropping a real license number in changes nothing above or below it.
The cover nameplate and the hero trust plate do not reflow. The underline is doing double duty:
it is the direction's blank-field affordance, so an unfilled compliance slot reads as a form
waiting to be completed rather than as a typo.

`Real Broker, LLC` is not a footnote anywhere. On the cover it is a 14px mono line in
`--signal-bright` directly under Ryan's name inside a bordered nameplate. In the hero it sits
inside a bordered plate whose label bar reads `LICENSED NEVADA BROKERAGE`, with the brokerage
name itself set in the accent at 600 weight and tracked open. Both are the second most
prominent object in their block.

---

## 8. Three-path wayfinding, system level

Not exercised on the sample spread, which is a shared core page, but the system is:

- **The rail is the tab.** On pages 6 to 17 the rail's outer edge carries a bleed tab block at
  one of three vertical positions: Path A top third, Path B middle third, Path C bottom third.
- **Three values plus three fills, never three hues.**
  A = solid `--ink` (L\* 6). B = `--muted` (L\* 42) with a 45 degree 6px hatch.
  C = `--paper` with a 2px `--ink` border and a 3px dot grid.
  A grayscale print keeps all three distinct on both value and pattern.
- Tab text bottom-to-top, Barlow Condensed 700, 11px, 0.22em tracking, 5mm off trim.
- Every path page carries the text label `PATH A · MOVING HERE` at the head of the rail as
  real text at 9px mono. It is never print-only, so a phone reader sees it.
- The folio in the source log band gains the path letter in a hairline box next to the black
  folio square: `6` `A`.
- Page 5's branch selector sets the three choices as three rail-style cards using the same
  three fills, so the reader learns the code before they meet the tabs.
