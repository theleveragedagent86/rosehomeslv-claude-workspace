# Claude design prompt, Direction 3, Sunset Geometric

Paste this whole file into Claude to keep building in this direction. It is self contained. It carries
every hex, the full type scale, the layout rules, and the traps that have already been hit here.

---

## The one sentence

You are extending **Sunset Geometric**, a design direction for a 44 page print first Las Vegas new
construction buyer guide by Ryan Rose. It is a screen printed desert poster that happens to be a
disclosure document. Direction 5's sunset palette, direction 1's page architecture, and **not one
serif in the whole book.**

The reader is a nervous first time new construction buyer who has already driven past a model home
and has not talked to anyone about it yet. Warm, plain, protective. Never a SaaS landing page.

---

## Absolute rules, these are build failures

1. **Zero em-dashes.** Not in HTML, not in CSS comments, not in your prose. Use commas, periods, or
   the word "and". This is checked mechanically.
2. **No `position: fixed` anywhere in the guide panels.**
3. **Never `position: absolute` inside an `li::before`.** Every bullet, numeral and checkbox is a
   flexbox row with a real `<span>` marker. That bug has shipped twice in this workspace and silently
   drops bullets onto the first letter under multi column.
4. **Never `transition: all`.** Animate `transform` and `box-shadow` only.
5. **Compute every contrast ratio in Python** from sRGB relative luminance. Do not assert one.
6. **Nothing is encoded by colour alone.** A `NOT FOUND` cell carries the literal words plus a glyph.
7. **Never invent a fact.** No price, rate, incentive, square footage, HOA amount or school rating
   that is not in `research/fact-ledger.md`. A gap ships as the literal string `NOT FOUND`.
8. **Nevada advertising.** `Ryan Rose`, `Real Broker, LLC`, licence `S.0185572`, `702-747-5921`,
   `ryan@rosehomeslv.com`, `rosehomeslv.com` appear on the cover, the back matter and the landing page.
9. **No depictions of people** in any imagery, fair housing. **Never imply a specific named community.**
10. **Clark County only.** No Pahrump, no Mesquite, no Boulder City.
11. Single self contained HTML file, one inline `<style>` block, one Google Fonts link.

---

## Palette, every hex with its role

```css
:root{
  /* paper */
  --paper:  #FBF6ED;   /* guide paper, full bleed on every page and the cover panel */
  --cream:  #FDF8F1;   /* landing ground, reverse type on dusk and ink, the refusal ribbon tag */
  --white:  #FFFFFF;   /* reverse type on sunset, clay, agave, agave-d. Phone number pills */

  /* ink */
  --ink:    #2B1D23;   /* warm plum black, never neutral. All body prose, soft close, brand pills */
  --muted:  #6B584E;   /* inline attributions, captions, folio notes, landing microcopy */

  /* the sunset family, carried over from direction 5 */
  --sunset: #D24018;   /* the loud one. Refusal panel, numeral circles, running heads, folios, button */
  --clay:   #9E3A1F;   /* sunset at TEXT weight. Every small coloured word in the book */
  --coral:  #E9714A;   /* secondary block. INK TEXT ONLY */
  --ochre:  #EFA00B;   /* desert sun. Credibility band, glyph squares. INK TEXT ONLY */

  /* the two cool notes */
  --agave:   #166A62;  /* stops the page going all orange. Light text only */
  --agave-d: #0F4F49;  /* agave at text weight. Escrow bracket, superscripts, Matured token */
  --dusk:    #4A2B52;  /* the deep block. Table headers, phone card, folio 20, focus ring */

  /* tints */
  --tint-clay:  #F3E6D6;
  --tint-coral: #FBE2D6;
  --tint-agave: #DCEBE7;

  /* warm rules, never a neutral gray */
  --rule:        #977C61;   /* hairlines, 3.63 on paper */
  --rule-strong: #7C6349;   /* load bearing outlines, 5.22 on paper */
}
```

### Colour rules that cannot be broken

1. **White or cream type never sits on `--coral` or `--ochre`.** They compute 3.03 and 2.16 in reverse.
2. **`--ochre` is never type on light paper** (2.01) and never a bare fill on paper. An ochre or coral
   shape sitting on paper carries a `--rule-strong` inset rule, which reads 5.22 and does the boundary
   work the fill cannot.
3. **`--sunset` is never small text.** It computes 4.35 on paper and 4.43 on cream. Allowed at 18pt
   and up, or 14pt bold and up. Small coloured text is always `--clay` at 6.34.
4. **`--clay` 91, `--muted` 92 and `--agave` 95 are grayscale twins.** Never use two of them to
   distinguish two things from each other.
5. **The three tints are grayscale identical** at 231 and 232. Same rule. They never meet in one
   component, and every tint card also opens with a coloured square glyph and a worded label.
6. **There is no neutral gray anywhere.** Every rule, tint and muted value is warm. That is a large
   part of why a palette this saturated still reads friendly.

### The ratios you inherit, all computed

Worst normal text in the system is **white on `--sunset` at 4.68**. Worst of any kind is
**`--rule` on `--paper` at 3.63**, a decorative hairline. Key pairs:

| pair | ratio | pair | ratio |
|---|---|---|---|
| ink on paper | 14.97 | white on sunset | 4.68 |
| clay on paper | 6.34 | cream on dusk | 11.30 |
| agave-d on paper | 8.73 | cream on ink | 15.26 |
| muted on paper | 6.23 | ink on ochre | 7.45 |
| ink on tint-clay | 13.13 | ink on coral | 5.32 |
| clay on tint-clay | 5.55 | white on agave | 6.42 |
| sunset on paper | 4.35 LARGE ONLY | clay on cream | 6.45 |

If you change any colour, recompute the whole table in Python. Do not assert a ratio.

---

## Type

```html
<link href="https://fonts.googleapis.com/css2?family=Karla:wght@300..800&family=Syne:wght@400..800&display=swap" rel="stylesheet">
```

```css
--display: "Syne", "Trebuchet MS", "Helvetica Neue", sans-serif;
--text:    "Karla", "Helvetica Neue", Arial, sans-serif;
```

- **Syne 700 and 800.** Geometric display with strange bones, a flat shouldered `a`, a wide `w`. Set
  at 15pt and up with tracking from -0.02em to -0.034em. It reads as a poster, not as a UI font.
- **Karla 400 to 800.** Grotesque, tall x height, open apertures. Holds at 5.9pt in a table token and
  still looks human at 9.5pt in body prose.

**The split is semantic. Syne says the thing. Karla explains the thing.** A reader learns in one page
that anything in Syne is a claim and anything in Karla is the evidence for it.

**There is no serif and no italic in this system.** Syne ships no italic, so emphasis is carried by
weight, by caps, and by colour, never by slant. Where an editorial direction would set an italic
phrase, this direction sets a separate display line in `--sunset`.

### Guide scale, points, print 1 to 1

| role | face | size / leading | tracking |
|---|---|---|---|
| cover title | Syne 800 caps | 36 / 1.00 | -0.032em |
| cover eyebrow | Karla 800 caps | 8.6 / 1.0 | 0.22em |
| cover subtitle | Karla 400 | 12.4 / 1.45 | 0 |
| cover byline name | Syne 700 | 21 / 1.0 | -0.02em |
| credibility band | Karla 800 | 9.6 / 1.3 | 0.005em |
| compliance line | Karla 500 | 7.4 / 1.5 | 0 |
| section headline | Syne 800 | 31 / 1.02 | -0.030em |
| headline accent line | Syne 700 | 19 / 1.14 | -0.024em, `--sunset` |
| deck | Karla 500 | 12 / 1.45 | 0 |
| question subhead | Karla 800 caps | 8.6 / 1.2 | 0.15em, with an 8.5pt colour square |
| answer line | Syne 700 | 15 / 1.14 | -0.02em, small variant 12.6 |
| lead hit line | Syne 700 | 14.5 / 1.16 | -0.022em, `--clay` |
| pull line | Syne 800 | 23 / 1.02 | -0.034em, FULL MEASURE ONLY |
| refusal headline | Syne 800 | 21 / 1.04 | -0.028em, reversed on sunset |
| refusal ribbon | Karla 800 caps | 7.4 / 1.0 | 0.18em, clay on a cream tag |
| **body prose** | **Karla 400** | **9.5 / 1.50** | **0. This is the floor, never go under it** |
| numbered list | Karla 400 | 9.5 / 1.45 | numeral 9.4 / 800 in a 16pt filled circle |
| card body | Karla 400 | 9.4 / 1.44 | 8.5 in the narrowest card |
| checklist step | Karla 400 | 8.2 / 1.36 | 0 |
| phone number | Syne 700 | 11.6 / 1.16 | -0.02em, tabular |
| soft close | Karla 400 | 9.2 / 1.45 | emphasis in ochre 800 |
| table column head | Karla 800 caps | 6.2 / 1.0 | 0.05em |
| table cell | Karla 400 | 8 / 1.2 | tabular. Row head 800 |
| status token | Karla 800 caps | 5.9 / 1.0 | 0.04em |
| inline attribution | Karla 600 | 7.4 / 1.42 | 0.015em |
| superscript source | Karla 800 | 6.2 / 1.0 | 0.02em, `--agave-d` |
| running head chip | Karla 800 caps | 7.4 / 1.0 | 0.18em |
| folio | Syne 800 | 15 / 1.0 | in a 0.48in by 0.40in tile |
| figure caption | Karla 600 | 7.2 / 1.38 | 0 |

### Landing scale, px and container query units

| role | face | size |
|---|---|---|
| eyebrow chip | Karla 800 caps | 11, 0.16em |
| H1 | Syne 800 | `clamp(34px, 4.4cqw, 56px)` / 1.02, -0.032em |
| subhead | Karla 400 | `clamp(15px, 1.35cqw, 18px)` / 1.58, max 36em |
| value prop heading | Syne 700 | 15 / 1.25, -0.015em |
| value prop body | Karla 400 | 13 / 1.55 |
| button | Karla 800 | 17 |
| microcopy | Karla 600 | 13 |
| trust detail | Karla 500 | 12.5 / 1.6 |

---

## THE TRAP THAT ALREADY BIT THIS FILE. READ BEFORE ADDING A COMPONENT.

The base prose rule is `.gp p`, specificity **(0,1,1)**, and it uses the `font` shorthand:

```css
.gp p{ margin:0 0 7pt; font:400 9.5pt/1.5 var(--text); }
```

A paragraph component selected by a single class is **(0,1,0)**. It loses, and the shorthand silently
resets its size, weight and family to 9.5pt Karla 400. Seven components shipped in that state in the
first build: `.q`, `.hit`, `.attr`, `.pull`, `.op-eyebrow`, `.op-line`, `.op-deck`. The pull line was
authored at 23pt Syne 800 and was rendering at 9.5pt Karla 400. It did not look broken. It looked bland.

**Scope every paragraph component as `.gp .name`, which is (0,2,0) and wins.** Components that are
not paragraphs are unaffected and stay at one class: `.a` on an `h2`, `.figcap` on a `figcaption`,
`.nlist .t` and `.chk .t` on spans.

**Verify with `getComputedStyle`, never with your eyes.** After any type change, read back
`fontSize`, `fontWeight` and `fontFamily` for every component and diff it against the scale above.

---

## Layout

### Page geometry

Trim `8.5in x 11in`. Side margin `--pad: .55in`. Foot `48px`. In print set `.page{height:10.96in}`,
because at exactly 11in Chrome pushes a sub pixel sliver onto the next sheet and emits a blank page
after every guide page. Zero the preview rig's `line-height` in print for the same reason.

**Every full bleed edge is a whole CSS pixel, never an inch.** A fractional element height makes
Chrome antialias the boundary and leaves a visible hairline seam where a photograph meets the paper.

| element | value |
|---|---|
| cover photo | 536px |
| cover seam ribbon | 16px at `bottom:557px` |
| cover panel | 557px, radius 26pt on the top corners |
| section opener photo | 320px |
| opener text block top | 272px, which is 85 percent down the photo |
| running head photo band | 52px |
| page foot | 48px |

### The section opening header device, this is the thing Ryan asked for by name

Full bleed photograph, its bottom edge dissolving into the page paper, a small colour eyebrow in caps
above, a big Syne headline sitting inside the faded zone, then a second display line in `--sunset`.

**One alpha layer, tone and dissolve in the same ramp. No `mix-blend-mode`.** A blend mode leaves a
seam where the photo meets the paper. This does not:

```css
.opener{ position:absolute; inset:0 0 auto 0; height:320px; overflow:hidden; background:var(--paper); }
.opener img{ width:100%; height:100%; object-fit:cover; object-position:50% 52%; }
.opener .dissolve{
  position:absolute; inset:0;
  background:linear-gradient(180deg,
    rgba(74,43,82,.42)    0%,
    rgba(74,43,82,.20)   28%,
    rgba(158,58,31,.16)  50%,
    rgba(251,246,237,.30) 64%,
    rgba(251,246,237,.80) 76%,
    rgba(251,246,237,1)   90%);
}
```

Type begins at 272px on the 320px block, which is 85 percent, where the paper stop interpolates to
0.9286. Worst case underneath is a pure black photograph, giving a composite of `#E9E4DC`. Ink on
that is 12.74, clay 5.39, sunset 3.70. **If you soften the ramp or move the type up, recompute all
three.** Use `valley.jpg`, the dusk city lights shot, or another wide horizon.

### The page architecture inherited from direction 1

- Rounded full bleed photo headline block at the top of a section, headline reversed out or sitting in
  the fade.
- **Question subhead, answer line.** A friendly question in coloured caps preceded by a small square
  glyph, answered by a short declarative line set larger underneath in Syne. This pairing is the
  direction's signature and it should appear four to six times per spread.
- Tinted rounded callout cards, two abreast, each opening with a small coloured square glyph.
- A numbered list where each numeral sits in a filled `--sunset` circle, flexbox, never `::before`.
- **Short inline attribution set small and quiet directly under the paragraph it supports**, for
  example "Clark County Treasurer and Clark County Public Works, verified July 2026". **Never a per
  page source strip.** Full URLs live in a numbered back appendix. Round one died partly on the strip.
- The refusal callout as the single loudest object on the spread.
- A stacked bar diagram of the monthly payment with one item visibly outside the escrow bracket.
- A dense multi row district table.
- Folios reading across the gutter: verso folio right aligned with a `11pt 3pt 3pt 11pt` radius,
  recto folio left aligned with the mirror radius, in different colours.

### The refusal callout, the design test

Thirty four of thirty nine pages carry a `NOT FOUND`. **If a refusal reads as a hole rather than as
generosity, the direction has failed**, whatever else it does well.

Here it is a solid `--sunset` panel at 16pt radius, a cream pill ribbon reading a phrase in the
author's voice, a 21pt Syne headline, and the body split into **two columns so the panel is wide and
confident rather than tall and apologetic.** Nothing else on the spread competes with it.

### Status tokens, never colour alone

```css
.tok{ display:inline-flex; align-items:center; gap:4pt;
      font:800 5.9pt/1 var(--text); letter-spacing:.04em; text-transform:uppercase;
      padding:2pt 4pt 1.8pt 3pt; border-radius:2pt 4pt 4pt 2pt; white-space:nowrap; }
.tok i{ width:5pt; height:5pt; border-radius:1.2pt; display:block; }
.tok-nf   { color:var(--clay);    border-left:2.6pt solid var(--clay); }
.tok-nf i { border:1.4pt solid var(--clay); background:transparent; }  /* HOLLOW */
.tok-done { color:var(--agave-d); border-left:2.6pt solid var(--agave-d);
            text-transform:none; letter-spacing:.02em; }
.tok-done i{ background:var(--agave-d); }                              /* FILLED */
```

Hollow versus filled is what survives a monochrome laser, because clay and agave are four gray levels
apart. The literal words carry the meaning. The colour is decoration.

### Radii

| token | value | used on |
|---|---|---|
| `--r-xs` | 3pt | table header corners |
| `--r-sm` | 6pt | phone number pills |
| `--r-md` | 10pt | every tinted card, the soft close strip |
| `--r-lg` | 16pt | the refusal panel |
| `--r-xl` | 26pt | the cover panel top corners |
| pill | 999px | every chip, running head, numeral circle, the landing button |

The only square corners in the direction are the cover seam ribbon, the folio tiles, and the glyph
squares in the question subheads. Roundness plus colour volume is what carries the warmth, because
there is no serif to do it.

### Spacing

Guide, points: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 18. Nothing between.
Landing, px: 8, 10, 12, 13, 14, 16, 18, 19, 24, 26.

---

## How this stays warm and does not become a tech startup

Four things, and if you drop any one of them it drifts:

1. **Colour volume, not colour accents.** The refusal panel is a solid sunset field roughly a fifth of
   its page. The cover credibility band is a slab of ochre bleeding off the left edge. The cover seam
   is four saturated bands. Poster palette at poster scale, not a UI theme with an accent colour.
2. **Round geometry everywhere.** See the radii table.
3. **Photography at full bleed and large.** The opener photo is a third of a page. The cover photo is
   half the cover. Photography is what makes this feel like a guide rather than a disclosure.
4. **Not one neutral gray.** `#977C61` instead of `#999999` changes the whole temperature of a page.

---

## Print rules

```css
@page{ size:letter; margin:0; }
html{ -webkit-print-color-adjust:exact; print-color-adjust:exact; }
@media print{
  .page{ height:10.96in; }
  .stage{ line-height:0; }  .rail{ line-height:normal; }
}
```

- `break-inside: avoid` and `page-break-inside: avoid` on `.card`, `.refuse`, `.tbl-wrap`,
  `table.sid`, `.fig`, `.chk li`, `.nlist li`, `.close`, `.prop`.
- `thead{ display:table-header-group }` on every table, plus `table-layout:fixed` with an explicit
  `<colgroup>` so paired table halves keep identical column widths.
- Every `<img>` carries real alt text. Every inline `<svg>` carries `role="img"`, `<title>` and
  `<desc>`, and a diagram's `<desc>` describes the argument, not the shapes.
- Every table carries `<caption>`, `<th scope="col">` and `<th scope="row">`.

### Economy override for a home printer, one rule

```css
:root{ --paper:#FFFFFF; --cream:#FFFFFF; --tint-clay:#FFFFFF; --tint-coral:#FFFFFF; --tint-agave:#FFFFFF; }
.card{ border:1pt solid var(--rule-strong); }
```

Removes the paper flood and all three tint fills, about 40 percent of the toner. Every ratio still
passes because white is lighter than paper in every pair. The refusal panel and the photography are
deliberately left alone. They are the two things a reader remembers.

---

## Landing page constraints, they are not negotiable

- The landing page is a **Lofty HTML embed**. **No `<form>` element.** Lofty appends its own form
  below the embed. The CTA is `<a href="#contact">` and page JS scrolls to the bottom.
- **No hardcoded GA or Pixel tags.** Lofty injects those at publish.
- `position: fixed` is safe on the landing page and forbidden in the guide. Two files, two opposite
  rules.
- Use **container queries**, not media queries, so the hero can be previewed at 1280px and 375px side
  by side in one document. Every grid track must be `minmax(0, ...)`. A bare `1fr` has
  `min-width: auto` and will blow the hero out at 375px.
- Interaction: hover, focus-visible and active on every clickable element. Animate `transform` and
  `box-shadow` only. The focus ring is `3.5px solid var(--dusk)` at `outline-offset: 4px`, which is
  11.30 on cream.

---

## Verify your own work, in this order

1. `grep` every file you wrote for the em-dash character, the en-dash character, and both of their
   HTML entity forms, the named one and the numeric one. Expect zero of all four. Write the search
   patterns from character codes at run time rather than typing the entities into a file, or your own
   checklist trips the gate. That happened here.
2. `grep` for `position:fixed`, `li::before` and `transition:all` in the guide. Zero.
3. Recompute every contrast pair in Python. Report the worst normal text pair honestly.
4. Serve over HTTP, not `file://`, then measure over CDP after `document.fonts.ready` and after every
   image resolves `decode()`. Take the lowest bottom edge of any leaf content element against the top
   of the foot rule. Measure again with `Emulation.setEmulatedMedia: print` for the real 10.96in box.
5. Read back `getComputedStyle` for every type component and diff it against the scale above.
6. Screenshot each panel with CDP `Page.captureScreenshot` and a `clip` box. Chrome's `--screenshot`
   flag hangs on pages this tall.
7. Convert a spread to grayscale and confirm the refusal panel is still the loudest object and the
   hollow versus filled tokens are still distinguishable.
