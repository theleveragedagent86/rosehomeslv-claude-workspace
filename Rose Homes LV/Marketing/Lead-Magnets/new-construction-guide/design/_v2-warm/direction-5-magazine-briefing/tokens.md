# Direction 5 · Magazine to Briefing · Design Tokens

**Thesis:** a lifestyle magazine that quietly turns into the clearest briefing document you have ever been handed.

Two registers, one voice. **Part one** is a saturated desert magazine. **Part two** is a warm briefing
built from exactly two hues pulled out of part one, at lower saturation, on a tighter grid, with the
photography shrunk to a supporting band. Round corners, the friendly type, and the color all survive
the transition. Nothing gets colder, only denser.

Every ratio below was computed with `python3`, not asserted. **81 pairs, zero FAIL. Worst normal text
ratio: 4.68.**

---

## 1. Palette

### 1a. Part one, the magazine half

| token | hex | role |
|---|---|---|
| `--mag-sunset` | `#D24018` | primary saturated block. Eyebrow flags, the landing button, the first value-prop chip. Carries white text at 4.68. |
| `--mag-coral` | `#E9714A` | secondary block. **Ink text only.** White on coral is 3.03 and is banned. |
| `--mag-ochre` | `#EFA00B` | desert sun. Seals, chips, the handoff arrow, accent caps on dark. **Ink text only** on light. |
| `--mag-agave` | `#166A62` | the cool note that keeps the palette from going all-orange. Light text only. |
| `--mag-dusk` | `#4A2B52` | the deep block. Cover lower two thirds, photo tints. Same hue that becomes `--brief-plum`. |
| `--mag-sand` | `#F8EFE2` | magazine paper and reverse text on dusk. |
| `--mag-cream` | `#FDF8F1` | brightest paper. Landing hero ground. |

### 1b. Part two, the briefing half

The whole back half runs on **two hues**: clay, pulled down from `--mag-sunset`, and plum, carried
straight over from `--mag-dusk`. Nothing else. That is the visible promise of the transition page.

| token | hex | role |
|---|---|---|
| `--brief-paper` | `#FBF6ED` | briefing paper. Slightly cooler and lighter than magazine sand so the page turn is felt. |
| `--brief-clay` | `#9E3A1F` | hue one. Callouts, eyebrows, phone numbers, italic emphasis, checklist numerals. |
| `--brief-plum` | `#4A2B52` | hue two. Table headers, aside rules, diagram escrow block. |
| `--brief-tint` | `#F3E6D6` | clay at low strength. Table zebra, checklist panel, path chips. |
| `--brief-plum-tint` | `#EDE6EE` | plum at low strength. The "Between us" aside only. |
| `--brief-muted` | `#6B584E` | inline attributions, folios, captions, the NOT FOUND token. |

### 1c. Shared

| token | hex | role |
|---|---|---|
| `--ink` | `#2B1D23` | all body text. A warm plum-black, never a neutral black. |
| `--white` | `#FFFFFF` | cards that must sit above `--brief-paper` (diagram, compare, phone box). |
| `--rule` | `#977C61` | every visible border. 3.63 on paper, 3.18 on tint, so it clears non-text contrast everywhere it lands. Drawn at 0.5pt to 0.75pt so it stays warm and light. |
| `--rule-strong` | `#7C6349` | load-bearing outlines only: checkbox squares, phone box, table foot rule. |

**Two blended rules are also computed in the table below**, because they are drawn with alpha:
the cover footer rule (`--mag-sand` at 45 percent over `--mag-dusk`, resolves to `#988393`) and the
handoff divider inside the NOT FOUND callout (`--white` at 62 percent over `--brief-clay`, resolves to `#DAB4AA`).

### Colour rules that must not be broken

1. **White text never sits on `--mag-coral` or `--mag-ochre`.** Ink only. Both fail AA in reverse.
2. **`--mag-ochre` is never text on any light paper.** 2.01 on brief-paper. It is a fill, or ink-on-ochre.
3. **`--brief-tint` and `--brief-plum-tint` are grayscale identical** (`#E8E8E8` both). They may never be
   used to distinguish two things from each other. They belong to different components and never meet.
4. **Nothing is encoded in colour alone.** The `NOT FOUND` cells carry the literal words, an italic, a
   dotted underline, and a hollow-circle glyph. The three reader paths carry letters, not hues.

---

## 2. Computed WCAG contrast, every pair actually used

Computed in Python from sRGB relative luminance, `(L1 + 0.05) / (L2 + 0.05)`, rounded to two decimals.
Threshold is 4.50 for normal text, 3.00 for text at 18pt or 14pt bold and above, 3.00 for non-text
(WCAG 1.4.11).

| fg | bg | ratio | size / weight | AA threshold | verdict | where |
|---|---|---|---|---|---|---|
| `--mag-cream` | `--mag-dusk` | **11.30** | 50pt / 800 | 3.00 (large) | PASS | cover title, Petrona 800 |
| `--mag-sand` | `--mag-dusk` | **10.48** | 13pt / 400 | 4.50 | PASS | cover subtitle and credibility line |
| `--mag-ochre` | `--mag-dusk` | **5.52** | 9.2pt / 800 | 4.50 | PASS | cover geography line and REAL BROKER, LLC |
| `--mag-sand` | `--mag-dusk` | **10.48** | 7.4pt / 400 | 4.50 | PASS | cover compliance line, license S.0185572 |
| `--white` | `--mag-sunset` | **4.68** | 9pt / 800 | 4.50 | PASS | cover eyebrow flag, caps |
| `--ink` | `--mag-ochre` | **7.45** | 22pt / 800 | 4.50 | PASS | cover seal, the numeral 39 |
| `--ink` | `--mag-sand` | **14.15** | 6.4pt / 800 | 4.50 | PASS | part one strip label, cover foot |
| `--ink` | `--brief-tint` | **13.13** | 6.4pt / 800 | 4.50 | PASS | part two strip label, cover foot |
| cover-rule (sand 45% over dusk) | `--mag-dusk` | **3.41** | n/a | 3.00 (non-text) | PASS | cover footer rule, non-text |
| `--brief-clay` | `--brief-paper` | **6.34** | 8pt / 800 | 4.50 | PASS | transition eyebrow, END OF PART ONE |
| `--ink` | `--brief-paper` | **14.97** | 36pt / 700 | 3.00 (large) | PASS | transition headline, Petrona 700 |
| `--brief-clay` | `--brief-paper` | **6.34** | 36pt / 700 | 3.00 (large) | PASS | transition headline italic phrase |
| `--ink` | `--brief-paper` | **14.97** | 12pt / 400 | 4.50 | PASS | transition deck |
| `--brief-plum` | `--white` | **11.94** | 13pt / 700 | 4.50 | PASS | transition card headings |
| `--ink` | `--white` | **16.12** | 8.6pt / 400 | 4.50 | PASS | transition card body |
| `--white` | `--brief-clay` | **6.82** | 7pt / 800 | 4.50 | PASS | WHAT CHANGES pill, caps |
| `--ink` | `--brief-tint` | **13.13** | 8.4pt / 800 | 4.50 | PASS | reader path chips |
| `--brief-clay` | `--brief-tint` | **5.55** | 7.4pt / 700 | 4.50 | PASS | PATH A B C labels, caps |
| `--ink` | `--brief-paper` | **14.97** | 9.5pt / 400 | 4.50 | PASS | briefing body prose, Petrona |
| `--ink` | `--brief-paper` | **14.97** | 10.9pt / 400 | 4.50 | PASS | briefing deck and page headline |
| `--brief-clay` | `--brief-paper` | **6.34** | 26pt / 700 | 3.00 (large) | PASS | headline italic phrase, subhead accents |
| `--brief-clay` | `--brief-paper` | **6.34** | 14pt / 700 | 4.50 | PASS | pull beat line, Petrona italic |
| `--brief-muted` | `--brief-paper` | **6.23** | 7.1pt / 500 | 4.50 | PASS | inline attribution line |
| `--brief-muted` | `--brief-paper` | **6.23** | 7pt / 500 | 4.50 | PASS | folio and appendix pointer |
| `--ink` | `--brief-plum-tint` | **13.17** | 8.3pt / 400 | 4.50 | PASS | Between us aside body |
| `--brief-plum` | `--brief-plum-tint` | **9.75** | 7.2pt / 800 | 4.50 | PASS | Between us label, caps |
| `--white` | `--brief-clay` | **6.82** | 8pt / 800 | 4.50 | PASS | numbered list markers 1 to 5 |
| `--white` | `--brief-clay` | **6.82** | 8pt / 400 | 4.50 | PASS | NOT FOUND callout body |
| `--white` | `--brief-clay` | **6.82** | 20pt / 700 | 3.00 (large) | PASS | NOT FOUND callout heading |
| `--ink` | `--mag-ochre` | **7.45** | 7pt / 800 | 4.50 | PASS | NOT FOUND eyebrow chip, caps |
| `--white` | `--brief-clay` | **6.82** | 8pt / 800 | 4.50 | PASS | handoff line inside the callout |
| handoff-rule (white 62% over clay) | `--brief-clay` | **3.60** | n/a | 3.00 (non-text) | PASS | handoff divider, non-text |
| `--ink` | `--mag-ochre` | **7.45** | 8pt / 800 | 4.50 | PASS | handoff arrow glyph on ochre disc |
| `--white` | `--brief-plum` | **11.94** | 6.4pt / 800 | 4.50 | PASS | table column headers, caps |
| `--ink` | `--brief-paper` | **14.97** | 7.3pt / 400 | 4.50 | PASS | table cells, odd rows |
| `--ink` | `--brief-tint` | **13.13** | 7.3pt / 400 | 4.50 | PASS | table cells, even rows |
| `--ink` | `--brief-paper` | **14.97** | 7.6pt / 800 | 4.50 | PASS | table row header, district number |
| `--brief-muted` | `--brief-tint` | **5.46** | 7.1pt / 600 | 4.50 | PASS | NOT FOUND cell token, italic |
| `--brief-muted` | `--brief-paper` | **6.23** | 7.1pt / 600 | 4.50 | PASS | NOT FOUND cell token, italic |
| `--brief-clay` | `--brief-paper` | **6.34** | 6.6pt / 800 | 4.50 | PASS | table caption, caps |
| `--rule` | `--brief-paper` | **3.63** | n/a | 3.00 (non-text) | PASS | table row rule, card borders, non-text |
| `--rule` | `--brief-tint` | **3.18** | n/a | 3.00 (non-text) | PASS | table row rule on zebra fill, non-text |
| `--rule` | `--white` | **3.91** | n/a | 3.00 (non-text) | PASS | card borders on white, non-text |
| `--rule` | `--mag-cream` | **3.70** | n/a | 3.00 (non-text) | PASS | landing trust divider, non-text |
| `--rule-strong` | `--brief-paper` | **5.22** | n/a | 3.00 (non-text) | PASS | table foot rule, non-text |
| `--rule-strong` | `--brief-tint` | **4.57** | n/a | 3.00 (non-text) | PASS | checkbox square outline, non-text |
| `--rule-strong` | `--white` | **5.62** | n/a | 3.00 (non-text) | PASS | phone box outline, non-text |
| `--brief-clay` | `--white` | **6.82** | 10.4pt / 700 | 4.50 | PASS | compare card value, district 151 |
| `--brief-plum` | `--white` | **11.94** | 10.4pt / 700 | 4.50 | PASS | compare card value, district 819 |
| `--brief-muted` | `--white` | **6.71** | 7pt / 800 | 4.50 | PASS | compare card district label, caps |
| `--ink` | `--white` | **16.12** | 7.2pt / 600 | 4.50 | PASS | compare card note and diagram labels |
| `--ink` | `--brief-tint` | **13.13** | 7.3pt / 400 | 4.50 | PASS | checklist step text |
| `--brief-clay` | `--brief-tint` | **5.55** | 7.3pt / 800 | 4.50 | PASS | checklist step numerals and label |
| `--ink` | `--brief-tint` | **13.13** | 13pt / 700 | 4.50 | PASS | checklist heading, Petrona |
| `--ink` | `--white` | **16.12** | 7.3pt / 400 | 4.50 | PASS | phone block body |
| `--brief-clay` | `--white` | **6.82** | 10.8pt / 700 | 4.50 | PASS | phone numbers, Petrona |
| `--brief-plum` | `--white` | **11.94** | 7.2pt / 800 | 4.50 | PASS | SAVE THESE TWO NUMBERS label |
| `--ink` | `--brief-paper` | **14.97** | 9pt / 400 | 4.50 | PASS | soft close line |
| `--brief-clay` | `--brief-paper` | **6.34** | 9pt / 600 | 4.50 | PASS | soft close italic offer |
| `--mag-cream` | `--brief-plum` | **11.30** | 7.2pt / 700 | 4.50 | PASS | diagram, principal and interest block |
| `--ink` | `--brief-plum-tint` | **13.17** | 7.2pt / 700 | 4.50 | PASS | diagram, tax and insurance blocks |
| `--ink` | `--brief-tint` | **13.13** | 7.2pt / 700 | 4.50 | PASS | diagram, association blocks |
| `--white` | `--brief-clay` | **6.82** | 8.6pt / 800 | 4.50 | PASS | diagram, special assessment block |
| `--brief-plum` | `--white` | **11.94** | 6pt / 800 | 4.50 | PASS | diagram, dotted box label |
| `--brief-muted` | `--white` | **6.71** | 6pt / 800 | 4.50 | PASS | diagram, term and outside labels |
| `--ink` | `--mag-cream` | **15.26** | 54pt / 800 | 3.00 (large) | PASS | landing hero H1 |
| `--brief-clay` | `--mag-cream` | **6.45** | 54pt / 800 | 3.00 (large) | PASS | landing hero H1 italic phrase |
| `--ink` | `--mag-cream` | **15.26** | 17pt / 400 | 4.50 | PASS | landing hero subhead |
| `--ink` | `--mag-sand` | **14.15** | 18pt / 700 | 4.50 | PASS | landing hero value prop heading |
| `--ink` | `--mag-sand` | **14.15** | 13.5pt / 400 | 4.50 | PASS | landing hero value prop body |
| `--ink` | `--mag-coral` | **5.32** | 16pt / 800 | 4.50 | PASS | landing hero chip numeral 1 |
| `--ink` | `--mag-ochre` | **7.45** | 16pt / 800 | 4.50 | PASS | landing hero chip numeral 2 |
| `--mag-sand` | `--mag-agave` | **5.63** | 16pt / 800 | 4.50 | PASS | landing hero chip numeral 3 |
| `--white` | `--mag-sunset` | **4.68** | 17pt / 800 | 4.50 | PASS | landing hero button label |
| `--brief-muted` | `--mag-cream` | **6.35** | 13pt / 600 | 4.50 | PASS | landing hero microcopy and contact details |
| `--brief-clay` | `--mag-cream` | **6.45** | 11.5pt / 800 | 4.50 | PASS | landing hero REAL BROKER, LLC |
| `--ink` | `--mag-cream` | **15.26** | 19pt / 700 | 4.50 | PASS | landing hero name lockup |
| `--brief-clay` | `--mag-sand` | **5.99** | 10.5pt / 800 | 4.50 | PASS | landing hero quote label |
| `--ink` | `--mag-sand` | **14.15** | 19pt / 600 | 4.50 | PASS | landing hero pull quote |
| `--brief-plum` | `--mag-cream` | **11.30** | n/a | 3.00 (non-text) | PASS | button focus ring, non-text |
| `--mag-ochre` | `--brief-clay` | **3.15** | n/a | 3.00 (non-text) | PASS | eyebrow chip fill on the callout, non-text |
**Result: 81 pairs, 0 FAIL.** The tightest normal-text pair in the book is white on `--mag-sunset` at
**4.68**, used for the cover eyebrow flag and the landing page button label.

---

## 3. Grayscale behaviour

Home printers matter here. Every token converted to its luminance-equivalent gray:

| token | hex | luminance-equivalent gray |
|---|---|---|
| `--mag-sunset` | `#D24018` | `#747474` |
| `--mag-coral` | `#E9714A` | `#949494` |
| `--mag-ochre` | `#EFA00B` | `#B0B0B0` |
| `--mag-agave` | `#166A62` | `#5F5F5F` |
| `--mag-dusk` | `#4A2B52` | `#373737` |
| `--mag-sand` | `#F8EFE2` | `#F0F0F0` |
| `--mag-cream` | `#FDF8F1` | `#F9F9F9` |
| `--brief-paper` | `#FBF6ED` | `#F6F6F6` |
| `--brief-clay` | `#9E3A1F` | `#5B5B5B` |
| `--brief-plum` | `#4A2B52` | `#373737` |
| `--brief-tint` | `#F3E6D6` | `#E8E8E8` |
| `--brief-plum-tint` | `#EDE6EE` | `#E8E8E8` |
| `--brief-muted` | `#6B584E` | `#5C5C5C` |
| `--rule` | `#977C61` | `#818181` |
| `--rule-strong` | `#7C6349` | `#676767` |
| `--ink` | `#2B1D23` | `#212121` |
| `--white` | `#FFFFFF` | `#FFFFFF` |
**What this means in practice.** The briefing half was built to survive this. `--brief-clay` goes to
`#5B5B5B` and `--brief-plum` to `#373737`: 1.75 apart, distinguishable but not reliable, which is why
they are never used to encode a difference. The two tints both flatten to `#E8E8E8`, which is why they
never appear in the same component. Structure in the table comes from a filled header band, alternating
row fills, and column alignment, not from hue. Printed on a black-and-white laser at page 4 of the PDF,
the SID and LID spread loses nothing but warmth.

The magazine half loses more, and it is supposed to: `--mag-sunset` (`#747474`) and `--mag-agave`
(`#5F5F5F`) sit close in gray. Part one is decorative colour, so nothing rides on telling them apart.

---

## 4. Type

**Single Google Fonts request:**

```html
<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:ital,wght@0,300..800;1,400..600&family=Petrona:ital,wght@0,400..800;1,400..600&display=swap" rel="stylesheet">
```

- **Petrona** (display and prose serif). Warm, high contrast at heavy weights, slightly quirky in the
  bowls, and almost nobody uses it. It reads editorial without reading luxury. It sets the cover, every
  headline, every callout heading, and all body prose in both halves.
- **Hanken Grotesk** (sans). Neutral but genuinely friendly: open apertures, a single-storey `g` feel in
  the lighter weights, and it holds up at 6pt in a table caption. It sets all apparatus: labels,
  eyebrows, lists, tables, checklists, attributions, folios, diagram callouts, the landing UI.

**The split is semantic, not decorative.** Prose is serif. Apparatus is sans. A reader learns in three
pages that Petrona is Ryan talking and Hanken Grotesk is the machinery.

```
--serif: "Petrona", Georgia, "Times New Roman", serif;
--sans:  "Hanken Grotesk", "Helvetica Neue", Arial, sans-serif;
```

### Full print scale (pt, for the 8.5in x 11in pages)

| role | family | size / leading | weight | tracking |
|---|---|---|---|---|
| cover title | Petrona | 50 / 0.95 | 800 (italic 700 for the accent phrase) | -0.028em |
| cover subtitle | Hanken | 13 / 1.5 | 400 | 0 |
| cover geography line | Hanken | 9.2 / 1 | 800 caps | 0.20em |
| cover credibility line | Petrona italic | 11.5 / 1.45 | 400 | 0 |
| cover byline name | Petrona | 21 / 1 | 700 | -0.015em |
| REAL BROKER, LLC | Hanken | 9.2 caps | 800 | 0.20em |
| cover compliance line | Hanken | 7.4 / 1.5 | 400 | 0.015em |
| transition headline | Petrona | 36 / 1.02 | 700 | -0.022em |
| section headline (spread) | Petrona | 26 / 1.04 | 700 | -0.02em |
| deck | Hanken | 10.9 / 1.46 | 400 | 0 |
| subhead | Petrona | 14 to 17 / 1.12 | 700 | 0 |
| body prose | Petrona | 9.5 / 1.48 | 400 | 0 |
| pull beat line | Petrona italic | 14 / 1.18 | 700 | 0 |
| aside body | Hanken | 8.3 / 1.46 | 400 | 0 |
| numbered list | Hanken | 8.3 / 1.44 | 400, names 800 | 0 |
| callout heading | Petrona | 20 / 1.06 | 700 | -0.018em |
| callout body | Hanken | 8.0 / 1.44 | 400 | 0 |
| eyebrow / label | Hanken | 7.0 to 7.4 caps | 800 | 0.14 to 0.19em |
| table caption | Hanken | 6.6 caps | 800 | 0.11em |
| table column head | Hanken | 6.4 caps | 800 | 0.05em |
| table cell | Hanken | 7.3 / 1.22, tabular-nums | 400 (row head 800 at 7.6) | 0 |
| NOT FOUND token | Hanken italic | 7.1 | 600 | 0.05em |
| checklist step | Hanken | 7.3 / 1.36 | 400, names 800 | 0 |
| phone number | Petrona | 10.8, tabular-nums | 700 | -0.01em |
| soft close | Petrona | 9 / 1.4 | 400, offer 600 italic | 0 |
| inline attribution | Hanken | 7.1 / 1.4 | 500, source names 800 | 0.01em |
| superscript ref | Hanken | 6.4 | 800 | 0 |
| folio | Petrona 12 / Hanken 7 caps | 700 / 800 | 0.16em |
| diagram labels | Hanken | 6.0 to 8.6 | 600 to 800 | 0 to 0.5 |

### Landing hero scale (px)

| role | family | size | weight |
|---|---|---|---|
| flag chip | Hanken | 11 caps, 0.16em | 800 |
| H1 | Petrona | `clamp(34px, 3.5vw, 54px)` / 1.02, -0.028em (30px under 560px) | 800, italic 800 accent |
| subhead | Hanken | 17 / 1.58, max 44ch | 400 |
| prop heading | Petrona | 18 / 1.18 | 700 |
| prop body | Hanken | 13.5 / 1.52 | 400 |
| chip numeral | Petrona | 16 | 800 |
| button | Hanken | 17 | 800 |
| microcopy | Hanken | 13.5 | 600 |
| trust name | Petrona | 19 | 700 |
| trust brokerage | Hanken | 11.5 caps, 0.19em | 800 |
| trust detail | Hanken | 12.5 / 1.65 | 500 |
| pull quote | Petrona italic | 19 / 1.34 | 600 |

---

## 5. Spacing, geometry, grid

**Spacing scale (pt, print):** 3, 5, 7, 9, 11, 13, 16, 20, 26, 36. Nothing between values.
**Spacing scale (px, web):** 6, 8, 12, 14, 18, 22, 26, 30, 38, 52.

**Radii.** Round corners are the thing that carries warmth across the transition. They do not shrink
in part two.

| token | value | used on |
|---|---|---|
| `--r-chip` | 3pt | flags, table header corners, small pills |
| `--r-card` | 7pt | asides, diagram card, compare cards, phone box, transition cards |
| `--r-big` | 12pt | the NOT FOUND callout and the checklist panel, the two largest objects on the spread |
| pill | 999px | eyebrow chips, path chips, the landing button |

**Page geometry.**

- Trim `8.5in x 11in`. Margins `0.5in` all round (`--pad-page`). Spread gutter `0.32in`.
- Photo band on briefing spreads: `0.78in`, full bleed, and it is **one photograph split across the
  gutter** (`width: 17.32in`, page 20 offset `margin-left: -8.82in`). This is the main device that makes
  the spread read as one canvas.
- Page 19 is three bands: headline block, then a 2-column text grid (`minmax(0,1fr) minmax(0,1fr)`,
  16pt gap), then a bottom zone of `minmax(0,1fr) minmax(0,1.5fr)` holding the diagram card and the
  NOT FOUND callout.
- Page 20 is: header block, a paired table (`minmax(0,1fr) minmax(0,1fr)`, 14pt gap, two 10-row tables),
  legend, compare strip, prose, the checklist in a 2x2 grid, then phone box beside the soft close.
- Every grid track is `minmax(0, ...)`. `1fr` alone has `min-width: auto` and will blow out the landing
  hero at 375px. That bug was found and fixed here.

**Cover geometry.** Photo occupies the top `5.9in`; the dusk block occupies the bottom `5.55in` and
overlaps the photo by `0.35in`. The eyebrow flag straddles the seam at `5.18in`, the ochre seal sits on
the photo at `3.72in`. A `0.3in` two-part strip runs along the very bottom edge and is the only place
the cover admits that the book has two personalities.

---

## 6. Print rules

```css
@page { size: letter; margin: 0; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
```

- `break-inside: avoid` on: `.diagram`, `.notfound`, `.aside`, `.check-wrap`, `.phones`, `.compare`,
  `.trans-card`, `table.sid`, and every `li`.
- `thead { display: table-header-group }` on every table.
- Guide pages set `height: 10.96in` in print, not 11in. At exactly 11in Chrome pushes a sub-pixel sliver
  onto the next sheet and you get a blank page after every spread. Also zero the preview rig's
  `padding` and `line-height` in print, or a 6px stage padding lands on the following sheet. Both bugs
  were hit and fixed here; the direction prints clean at 4 guide pages plus 2 hero pages.
- **No `position: fixed` anywhere in the guide panels.** The landing panel does not use it either.
- Bullets and checklists are flexbox (`display:flex` with a marker `<span>`), never
  `li::before { position: absolute }`.
- Tables carry `<caption>`, `<th scope="col">`, `<th scope="row">`, and `table-layout: fixed` with an
  explicit `<colgroup>` so the two halves of the paired table keep identical column widths.

---

## 7. Photography treatment

| image | where | treatment |
|---|---|---|
| `cover.jpg` | cover, top 5.9in | sunset multiply at 20 percent fading to dusk at 52 percent, plus an ochre radial lift at the top right |
| `valley.jpg` | transition page, top 4.15in | dusk 10 percent to clay 10 percent, dissolving to solid `--brief-paper` at the bottom so the photo hands off to the page rather than being cropped by it |
| `valley-day.jpg` | the spread band, one image across both pages | dusk 30 percent to clay 16 percent to `--brief-paper` at 94 percent |
| `summerlin.jpg` | landing hero art column | `filter: saturate(.8) contrast(1.05) sepia(.16)` plus a sunset-to-dusk multiply and a bottom-up dusk scrim |

Every `<img>` carries real alt text. The page 20 half of the split band is `alt="" aria-hidden="true"`
because it is the continuation of a photo already described on page 19. Both inline SVGs carry
`role="img"`, `<title>`, and `<desc>`, and the `<desc>` on the diagram describes the argument, not the
shapes.

---

## 8. Interaction states (landing panel only)

```css
.btn { transition: transform .16s cubic-bezier(.34,1.56,.64,1), box-shadow .16s ease; }
.btn:hover        { transform: translateY(-2px); }
.btn:focus-visible{ outline: 3px solid var(--brief-plum); outline-offset: 3px; }  /* 11.09 on cream */
.btn:active       { transform: translateY(1px); }
```

Only `transform` and `box-shadow` animate. No `transition: all`. The button is
`<a href="#contact">`; there is no `<form>` in the embed, per the Lofty constraint.
