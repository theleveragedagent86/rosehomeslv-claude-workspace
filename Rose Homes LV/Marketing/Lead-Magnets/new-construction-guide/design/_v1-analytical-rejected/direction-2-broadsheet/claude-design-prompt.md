# Claude Design brief: BROADSHEET

Paste this whole file into Claude Design. It is self-contained. Assume no other context.

---

## What you are building

A **39-page print-first buyer guide** plus a **landing page**, for a Las Vegas real estate agent, aimed at people buying a newly built home from a production builder. The audience is cold traffic from Facebook. They are nervous and they distrust real estate marketing. Reading level is sixth grade.

**The design thesis, and you must not drift from it:**

> This is reporting on builders, not marketing from a realtor.

Newspaper typesetting discipline. Serif headline stack with real hierarchy, hairline rules, kickers above headlines, pull callouts, and a visible dateline on every verified fact. The guide's credibility is the product: it carries about 150 footnotes and 114 honest `NOT FOUND` cells, and the apparatus of sourcing is designed to be beautiful rather than hidden. Restrained colour. Ink as structure. Think a serious newspaper's investigative section, not a brochure.

**This project is deliberately off-brand.** Do not use navy `#1C2333`, champagne gold `#C9A86E`, or warm off-white `#F7F5F0`. Do not use Playfair Display, Montserrat, or Bebas Neue. Those belong to other assets.

---

## Colour, exact hexes

```css
:root{
  --paper:      #FFFFFF;  /* page stock, pure white */
  --newsprint:  #F2F2EF;  /* light band: table zebra rows, figure layers */
  --stock:      #E5E6E1;  /* heavy band: table header, phone block, Path C tab */

  --ink:        #14171A;  /* primary text, headlines, heavy rules, Path A tab */
  --ink-2:      #333A40;  /* decks, table body, callout body */
  --ink-3:      #5C646C;  /* agate: source strip, datelines, running heads, folios */

  --rule-hair:  #BFC3BE;  /* decorative hairline ONLY, 1.78:1, never sole meaning */
  --rule:       #8E938D;  /* functional rule, 3.13:1 on paper */
  --rule-heavy: #14171A;

  --spot:       #7A2019;  /* the ONE spot colour, oxblood */
  --spot-deep:  #5E1C16;  /* CTA hover and pressed */
  --spot-wash:  #F7EFED;  /* NOT FOUND panel wash */

  --path-a:     #14171A;  /* grayscale 23  */
  --path-b:     #7A2019;  /* grayscale 65  */
  --path-c:     #E5E6E1;  /* grayscale 229, carries ink text */
}
```

**One spot colour. There is no second accent.** Oxblood is spent on: kickers, the cover eyebrow, footnote figures, NOT FOUND cells and panels, phone numbers, VERIFIED stamps, the soft-close closing line, and the CTA. Nothing else.

All pairs computed and passing AA. Lowest text ratio in the system is 5.36:1. Key ratios: ink on paper 17.99, ink-2 on paper 11.54, ink-3 on paper 6.01, spot on paper 10.25, paper on spot 10.25, rule on paper 3.13 (non-text).

---

## Type

Load exactly this:

```html
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;0,6..72,700;1,6..72,400;1,6..72,600;1,6..72,700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;0,8..60,700;1,8..60,400&display=swap" rel="stylesheet">
```

| Role | Family | Never use it for |
|---|---|---|
| Display | **Newsreader** | body prose, tables, anything under 12px |
| Body | **Source Serif 4** | headlines, kickers, labels, tables of furniture |
| Furniture | **IBM Plex Sans** | running prose |

Newsreader is the high-contrast news serif that does all the shouting. Source Serif 4 is the low-contrast workhorse underneath it. IBM Plex Sans handles every piece of machinery: kickers, running heads, datelines, table headers, source strip, folios, buttons, labels.

### Scale, px at 96dpi (print pt in brackets)

**Cover:** title 68 [51] / 0.96 / -0.028em Newsreader 700 · subtitle 19 [14.3] / 1.36 Newsreader 400 italic · credibility strapline 16.5 [12.4] Newsreader 600 italic · byline name 25 [18.8] Newsreader 600 · eyebrow 10 [7.5] Plex 700 caps +0.30em · geography 10.5 [7.9] Plex 600 caps +0.24em · brokerage plate 11.5 [8.6] Plex 600 caps +0.17em · edition 9.5 [7.1] / 1.62 Plex 400 · compliance 9 [6.8] / 1.70 Plex 400.

**Interior:** headline 35 [26.3] / 1.02 / -0.024em Newsreader 700 · section head 24 [18] Newsreader 700 · deck 14.5 [10.9] / 1.33 Newsreader 400 italic · subhead 16.5 [12.4] Newsreader 700 · **body 13.1 [9.8] / 1.39 Source Serif 4 400** · beat line 14.2 Newsreader 600 · pull callout 13 / 1.36 Newsreader · NOT FOUND head 19.5 [14.6] Newsreader 700 italic · NOT FOUND body 11.6 / 1.36 Source Serif · table body 8.6 [6.5] / 1.20 Source Serif · table id 9.4 Plex 700 · table header 7 [5.3] Plex 700 caps +0.11em · table caption 7.2 Plex 700 caps +0.16em · phone body 11.5 Source Serif · phone number 12 Plex 700 · soft close 12.3 / 1.31 Newsreader · kicker 8.5 [6.4] Plex 700 caps +0.22em · running head 7.5 Plex 600 caps +0.19em · folio 9 Plex 700 caps +0.14em · **source strip 6.2 [4.7] / 1.23 Plex 400** · strip head 6.8 Plex 700 caps +0.22em · VERIFIED stamp 6.2 Plex 700 caps +0.08em · footnote figure 7.5 Plex 600 superior · cutline 8.5 / 1.45 Plex 400.

**Landing page:** headline `clamp(34px, 4.4vw, 62px)` / 0.99 / -0.03em Newsreader 700 · subhead `clamp(16px, 1.42vw, 20px)` / 1.42 Newsreader 400 italic · prop head `clamp(17px, 1.5vw, 20px)` Newsreader 700 · prop body `clamp(14px, 1.05vw, 15px)` / 1.52 Source Serif · CTA 16 Plex 700 caps +0.13em · trust line 12 / 1.85 Plex.

---

## Layout system

**Page box:** exactly `8.5in x 11in`. Margins top `0.34in`, bottom `0.30in`, outer `0.44in`, inner `0.50in`. Tight, like a newspaper.

**Grid:** three columns on almost every interior page, gutter `0.19in`, giving a `2.30in` measure at about **35 characters per line**. That is a newspaper measure and it is also the right measure for a sixth-grade reader. Use CSS `column-count: 3; column-fill: auto` and `column-span: all` for full-measure objects.

**Spread:** two facing pages read as one canvas. Mirror the margins, mirror the running head (outer edge), mirror the folio (bottom outer corner). Both feet carry a source strip, so the strips form a continuous band across the gutter.

**Vertical order on a page:** running head with a dateline stamp, kicker over the headline, headline, deck, 3px ink rule, three-column body region, source strip under a 3px double rule, folio.

**Spacing scale:** `2 4 6 8 12 16 20 26 34 44 58` px.

**Rules:** hairline 0.5 to 1px `--rule-hair` decorative only · thin 1px `--rule` · medium 1.5 to 2px ink · heavy 3px ink · 3px double ink for the source strip top · banner 7px ink plus 2.5px spot on the cover only · callout 5px spot top and 2px spot bottom.

**Radii: zero everywhere, including buttons.** A rounded corner is a software convention and this document is arguing it is a printed record.

---

## Component list

1. **Running head.** Flex row, mono-feel Plex caps at the outer edge, a boxed `VERIFIED 2026-07-25` stamp at the inner edge, 1px ink rule under.
2. **Kicker.** Plex 700 caps in `--spot`, sits directly above the headline.
3. **Headline block.** Kicker, headline, deck, 3px ink rule. Full measure across all columns.
4. **Beat line.** A one-sentence paragraph set in Newsreader 600 instead of the body face. Used for lines like "Often that somebody is you."
5. **Pull callout.** 3px ink top rule, 1px ink bottom rule, an `ASIDE` tag in Plex caps, body in Newsreader. No fill.
6. **NOT FOUND panel.** `--spot-wash` fill, 5px `--spot` top rule, 2px bottom rule, a reversed `NOT FOUND REGISTER · ITEM n` stamp, Newsreader 700 italic head, two-column body. Spans all columns. One per page maximum.
7. **NOT FOUND cell.** Inside tables: Plex 700 caps 7px `--spot` with a 1.5px `--spot` underline. **Always prints the words NOT FOUND.**
8. **Data table.** `table-layout: fixed` with a `<colgroup>`. `<caption>` above, in Plex caps, ending with a `VERIFIED` date in spot. `<thead>` on `--stock` with a 2px ink rule above and 1px below. Zebra rows in `--newsprint`. Last row gets a 2px ink bottom rule. Long tables double up as two half-width tables side by side, each with its own `<caption>` and `<thead>`.
9. **Numbered list.** Flex rows. Marker is a Plex 700 tabular figure in `--spot` in a fixed 13px right-aligned flex child.
10. **Checklist.** Flex rows, a real 9px square with a 1.25px ink border as the first flex child, 1px hairline separators, 1px ink rule above the first item.
11. **Phone block.** `--stock` fill, 3px ink rules top and bottom, heading in Plex caps, numbers in Plex 700 `--spot`.
12. **Soft close.** 1.5px `--spot` top rule, two short paragraphs in Newsreader, last line italic in `--spot`. Never a boxed CTA.
13. **Figure.** 2px ink top rule, a caption row with the figure number bold and a right-aligned status note in spot, then the schematic. Full measure.
14. **Source strip.** 3px double ink top rule, a `SOURCES` head with an entry range on the right, then a three-column list of flex rows: spot figure, claim text, URL in `--ink-2`, `VERIFIED yyyy-mm-dd` stamp in spot. URLs print **without `https://` and without `www.`**, full path retained, `overflow-wrap: anywhere`.
15. **Folio.** Bottom outer corner, Plex 700, with a small muted section label beside it.
16. **Photo well.** CSS-only halftone placeholder plus a cutline below it naming the shot. Never link an external image.
17. **CTA button.** Square, `--spot` fill, white Plex 700 caps. Landing page only.

---

## The three-path wayfinding system

Pages 6 to 17 branch into three reader paths and rejoin at 18.

| Path | Tab fill | Text | Grayscale | Folio | Tab position |
|---|---|---|---|---|---|
| A, moving here from out of state | `--path-a` | white | 23 | `6 · A` to `9 · A` | top third |
| B, moving up inside the valley | `--path-b` | white | 65 | `10 · B` to `13 · B` | middle third |
| C, your first new build | `--path-c` | ink | 229 | `14 · C` to `17 · C` | bottom third |

Distinguish by **value, never by hue alone.** The tab bleeds off the outer edge with no text within 5mm of the trim. Redundancy is mandatory: the folio letter and the running head both name the path, so a tab that fails to print costs nothing. On screen the tab is replaced by a text path label above the headline, in Plex 700 caps at 8.5px with `0.22em` tracking, in the path ink. That label must never be print-only.

---

## Motion

Screen only. The guide has none.

- Animate `transform` and `opacity` only. **Never `transition-all`.**
- CTA: `transition: background-color .16s cubic-bezier(.2,.8,.3,1), transform .16s cubic-bezier(.2,.8,.3,1)`.
- Hover to `--spot-deep`. Active `translateY(1px)`. Focus-visible `outline: 3px solid var(--ink); outline-offset: 3px`.

---

## Things that must never change

1. **Zero em-dashes (U+2014) in any file**, including CSS comments. Checked mechanically. Use commas, periods, or "and".
2. **`Real Broker, LLC` gets a designed slot, never small print.** Nevada law requires a licensee's advertising to identify the brokerage. On the cover it is a bordered plate opposite the byline. On the landing page it is a bordered inline plate inside the trust line. Do not shrink it.
3. **The licence number renders literally as `[NOT FOUND]`** until Ryan supplies it, in a fixed-width slot so a real number drops in with no reflow:
   ```css
   .license-slot{ display:inline-block; min-width:11.5ch; text-align:center;
     font-variant-numeric:tabular-nums lining-nums; font-weight:600;
     color:var(--spot); border-bottom:1.5px solid var(--spot); }
   ```
   Verified: swapping `[NOT FOUND]` for `B.0197712` changes the slot width by zero pixels.
4. **No `position: fixed` anywhere in the guide.** A fixed element repeats on every printed page. It is permitted on the landing page only.
5. **Bullets and list markers are flex children.** Never `li::before { position: absolute }`. Under CSS multi-column an absolute marker lands on the first letter, and this system runs three columns nearly everywhere. This bug has shipped twice in this workspace.
6. **Tables need `<caption>`, `<th scope="col">`, and `thead { display: table-header-group }`** so the header repeats when a table breaks across pages.
7. **Print CSS is mandatory:** `@page { size: letter; margin: 0 }`, `print-color-adjust: exact` on every tinted surface, `break-inside: avoid` on every callout, card, table, figure, phone block, and list item.
8. **Never encode meaning in colour alone.** Every NOT FOUND cell prints the words. Every path is named in two other places.
9. **One spot colour.** Do not add a second accent, a success green, or a warning amber. If something needs emphasis, use weight, caps, rule, or position.
10. **No images are available.** Render photography as CSS-only halftone placeholders with a cutline naming the intended shot. Never link an external image URL or a placeholder service.
11. **Cover carries no price, rate, incentive, or builder name.** It must still be true in six months.
12. **The landing page has no `<form>`.** Lofty appends its own form at publish. The button is `<a href="#contact">` and page JS scrolls to the bottom.

---

## Known constraint you will hit

The sample interior spread runs **roughly 1.5 Letter pages of copy per leaf** at 10.5pt. It only fits at 9.8pt body with the source strip at 4.7pt. If you are given copy that overruns, **say so and quote the number.** Do not silently cut, and do not drop below 9.8pt body. The correct fix is an extra page.
