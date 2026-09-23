# Claude Design brief: "Postcard to Workbook"

Paste this whole file into Claude Design to keep exploring this direction. It is self contained.

---

## What you are designing

A 44 page printed lead magnet plus its landing page, for a Las Vegas real estate agent. Title:
**Before You Walk Into the Model Home**. It is a plain spoken buyer guide to new construction in Las
Vegas, Henderson, and Clark County. The audience has already driven past a model home and has not
talked to anyone about it yet.

The content is **protective**, not aspirational. It tells the reader that the sales rep at the model
home works for the builder, that a special assessment can ride along with a home for thirty years,
and that a builder incentive tied to the builder's lender has a cap. The design's job is to make that
feel generous rather than alarming.

## The one idea, do not lose it

> **The front half sells you on the valley. The back half hands you a pen and gets to work.**

- **Pages 1 to 17 are a postcard.** Big saturated photography, deckled photo edges, a real postage
  stamp with bumped edges, a circular cancellation postmark with wavy lines, bright caption strips,
  an illustrated cartoon valley map. Genuinely fun and touristic.
- **Page 18 is the gear change** and it must exist. A designed divider page: two tilted postcards on
  a teal field, then a solid vermillion band carrying the line **"Put the postcard down."**, then a
  ruled paper field with an illustrated valley map and the three reader paths.
- **Pages 19 to 44 are a warm workbook.** Same palette, same type, but the layout becomes fillable:
  checkboxes, ruled write in lines, labeled blanks, worksheet panels with a flag tab in the corner.

The palette and typefaces never change across the seam. Only layout behaviour changes.

## Exact palette, use these hexes

```
--ink            #2A1A20   body prose, table cells, checklist copy
--ink-soft       #6B5560   captions, feet, hints, inline attributions
--paper          #FFF8ED   page stock
--paper-warm     #FDECD5   worksheet panels, diagram box, landing trust block
--rule           #9C8058   FUNCTIONAL ruled lines and component borders (passes 3.00)
--rule-soft      #DCC7AA   DECORATIVE only: row separators, hairlines, ruled paper texture
--sunset         #C22F17   display type, tab chips, divider band, landing button, checkbox outlines
--sunset-br      #E24A22   graphics only, never carries type (stamp perforation)
--marigold       #F5A517   eyebrow chip, landing kicker, step numerals, term bar
--marigold-tint  #FCE9BE   THE WRITE IN FIELD: NOT FOUND panel fill and NOT FOUND chips
--sky            #16697A   subheads, table column headers, escrow box, checkbox outlines
--sky-lt         #59B3C4   mid turquoise field
--sky-tint       #D5EBEF   Q and A aside fill, phone card fill
--cactus         #4C6B2F   "this one is finished": Matured and Paid off cells
--plum           #6B2A5A   figure numbers, phone numbers, brokerage line, map mountains
```

**Semantic rule that must never be broken: amber means a blank you fill in.** Nothing else may use
`--marigold-tint` as a fill.

Banned: Rose Homes navy `#1C2333`, champagne `#C9A86E`, off white `#F7F5F0`.

## Type

```html
<link href="https://fonts.googleapis.com/css2?family=Alfa+Slab+One&family=Bitter:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=Rubik:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
```

| family | job | never |
|---|---|---|
| **Alfa Slab One** 400 | postcard display only: cover title, divider statement, page headlines, write in panel headline, folios, big values, phone numbers | subheads, any running text |
| **Bitter** 400/500/600/700 + italic | question subheads, deck lines, tab chips, flags, field labels, step names, table headers, soft close | body prose |
| **Rubik** 300 to 700 | body prose, table cells, captions, hints, landing body | headlines |

**Print scale, pt.** Cover title 46/0.92/-0.014em. Divider statement 38/0.94. Page headline 20/1.00.
Write in headline 15/1.04. Compare value 12.5. Folio 13. Phone 9. Cover subtitle Bitter 13.4/1.34.
Deck Bitter italic 10/1.30. Section subhead Bitter 700 12.6/1.16. Q and A heading 10.4/1.20. Step
name Bitter 700 8.6. Table row header Bitter 700 7.9. Tab chip and flag Bitter 700 caps 6.8 to 7.4 at
0.15em. Table column header Bitter 700 caps 7 at 0.10em. Field label Bitter 700 caps 5.9 to 6.6.
Body Rubik 9.1/1.45. Q and A body 8.6/1.44. Write in body 8.2/1.38. Checklist 7.95/1.33. Table cell
7.4/1.07. Phone card 7.0/1.28. Attribution Rubik italic 6.9. Caption and foot 6.4 to 6.9. Source
superscript Rubik 600 6.2.

**Landing scale, px.** Headline Alfa Slab `clamp(32px,4.35vw,58px)`/0.99/-0.016em. Subhead Rubik
`clamp(15px,1.35vw,18px)`/1.62. Kicker Bitter 700 caps 12. Prop title Bitter 700 17/1.22. Prop body
Rubik 14/1.52. Button Bitter 700 19. Trust label Bitter 700 caps 11. Trust value Bitter 600 15.

## Layout system

- Trim 8.5in by 11in. Cover margin 0.40in. Guide pages `padding: .38in .48in .3in`, giving a 7.54in
  measure. Two column blocks use a 0.26in gutter.
- Vertical spacing comes only from `.06 / .10 / .14 / .20 / .28 / .40in`.
- Radii: chips 3px, panels 8px, pills 999px. Stamps, postmarks, rules and the table are square.
- Three elevation levels only. Paper, panel (tinted fill plus a border, no shadow), floating (the
  cover photo and divider postcards, which get a real drop shadow because they pretend to be objects).
  Workbook panels never float.
- Folios read across the gutter: verso folio outer left, recto folio outer right.

## Component list

**Postcard half:** deckled photo frame (four scalloped strips of `--paper`), postage stamp (cream
rect with cream circles bulging off every edge, a photo window, a red numeral), postmark (double ring
plus five wavy cancellation lines, rotated about 9 degrees), caption strip (dark gradient with cream
caps type), geography pills, ruled address block, pen note.

**The hinge:** divider page. Tilted photo cards with amber label tabs, solid `--sunset` band with the
Alfa Slab statement, ruled paper field, illustrated valley map, "Three ways to read the back half",
and two blank fields for the reader's name and the lot they are looking at.

**Workbook half:** tab chip and "Bring a pen" mark in the running head; question headline plus italic
deck plus a 3px rule; Q and A aside (`--sky-tint` fill, 4px `--sky` top border); checklist row
(flexbox: checkbox, amber numeral disc, text); **write in panel** (`--marigold-tint` fill, 2.5px
`--sunset` border, `--sunset` flag tab, three labeled blanks with hints); worksheet panel
(`--paper-warm` fill, 2px `--rule` border, `--sky` flag tab, mini blank row); district table;
NOT FOUND chip; compare cards; phone card (`--sky-tint`, 2px dashed `--sky`); soft close (2px
`--sunset` top rule, no box); running foot.

**Landing:** photo background with an ink to vermillion scrim plus SVG grain, amber kicker, Alfa Slab
headline with the last clause in `--marigold`, three cream prop cards with colored left borders and
amber numeral discs, one vermillion button with a 4px darker bottom edge, microcopy, and a
`--paper-warm` trust block set as a five column grid of labeled ruled fields.

## Illustrated map

Build it as inline SVG, flat shapes only, no photorealism. Stylized valley basin, mountain triangles
in `--plum` and `--cactus`, I-15 as a `--sunset` ribbon with a dashed centerline, the 215 as a
`--sky` ribbon, freeway shields, a resort corridor icon of three amber bars, park icons, and a red
pin labeled "your lot". Always print "Not to scale. No community boundaries shown."

## What must never change

1. **Zero em-dashes (U+2014) anywhere**, including CSS comments. Hard failure.
2. **Amber means a blank you fill in.** Never decorate with `--marigold-tint`.
3. **The divider page stays.** Without it the two halves are two different books.
4. **`Real Broker, LLC` is designed for, not tolerated.** It is a labeled ruled field on the cover and
   in the landing trust block, set in `--plum`. Nevada license **S.0185572** appears on the cover
   compliance line and in the trust block.
5. **Facts are load bearing.** Never change or invent a price, number, date, statute, phone number, or
   source. Gaps are marked NOT FOUND and turned into a write in blank, never filled with an estimate.
6. **Sourcing.** Short inline attribution where a fact lands ("Clark County Treasurer, verified July
   2026"), a small superscript numeral, and full URLs only in the numbered appendix at the back. No
   source strip at the foot of every page.
7. **Print discipline.** `@page { size: letter; margin: 0 }`, `print-color-adjust: exact`,
   `break-inside: avoid` on every card, table, and callout, `thead { display: table-header-group }`,
   and **no `position: fixed` in the guide**. The landing page may use it.
8. **Bullets are flexbox rows with a real marker element.** Never `li::before { position: absolute }`.
9. **Accessibility.** Real alt text on every photo. `role="img"` plus `<title>` and `<desc>` on every
   meaningful inline SVG; decorative icons get `aria-hidden="true"`. `<caption>`, `<th scope="col">`,
   `<th scope="row">` on tables. Nothing distinguished by color alone.
10. **Fair housing.** No people in any image. Architecture, landscape, and place only. Never imply an
    image is a specific named community or a specific builder's home.
11. **Every text pair must pass WCAG AA at its actual size and weight**, and every functional non text
    graphic must pass 3.00. Compute the ratios, do not assert them.

## Ideas worth exploring next

Area opener pages built as full bleed postcards with a stamp carrying that area's icon. A recurring
"What locals actually ask" Q and A block in `--sky-tint` on every area page. A back cover that is the
reverse of the cover postcard, with the message area used for the reader's own notes. A tear off
worksheet page perforated at the fold. A one page "take this to the model home" summary card that
repeats every blank in the book.
