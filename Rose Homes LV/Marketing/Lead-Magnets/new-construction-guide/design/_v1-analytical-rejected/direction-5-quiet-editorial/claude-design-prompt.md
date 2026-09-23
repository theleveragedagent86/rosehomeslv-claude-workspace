# Claude Design brief: Quiet Editorial

Paste this whole file into Claude Design. It is self contained. You need no other context.

---

## What you are building

A 39 page print first buyer guide called **Before You Walk Into the Model Home**, plus its landing page. It is a free PDF lead magnet for a Las Vegas real estate agent. The reader is a suspicious cold Facebook visitor who has already driven past a model home and has not talked to anyone yet.

**Design direction: Quiet Editorial. Calm, expensive, unhurried. The opposite of a sales flyer.** Magazine feature discipline. A lot of air. The persuasion is tonal: someone laying out a page this slowly is not in a hurry to close you.

---

## Palette. Use these hexes exactly

```
--paper        #FCFBF9   page stock, a cool white
--paper-tint   #F0EEE8   one step up. Diagram layer blocks only
--sand         #F2EAE0   RESERVED. See the rule below
--print-wash   #EDEAE3   ink-lean substitute for an atmospheric field
--ink          #1D2321   primary text, a deep graphite green
--ink-2        #3D4642   secondary text, decks, table data
--muted        #545C58   apparatus, running heads, folios, sources, captions
--caption-field #EDEAE3  caption text set over an atmospheric field
--clay         #9C4A2C   the single accent
--clay-deep    #7E3A20   accent at small sizes and on hover
--rule         #C9C7BE   hairline separators, decorative only
--rule-strong  #86887F   meaningful graphics, checkbox borders, diagram boundaries
--field-1      #232B28   atmospheric field, darkest
--field-2      #38423B
--field-3      #55503F
--field-4      #6A5E4E   atmospheric field, warmest
```

**The sand rule.** `--sand` is never decorative. It marks a NOT FOUND callout, meaning "a number we refused to invent", and nothing else in all 39 pages. Do not use it for a tip box, a quote, or a CTA.

Every pair above has been verified against WCAG AA. The lowest text ratio in the system is 5.73:1. If you introduce a new pair, compute the ratio before shipping it.

---

## Type. Load exactly this

```html
<link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:ital,wght@0,400..700;1,400..700&family=Newsreader:ital,opsz,wght@0,6..72,200..600;1,6..72,200..600&display=swap" rel="stylesheet">
```

- **Newsreader** carries every word a reader actually reads: titles, decks, body, lists, checklists, callouts, phone number stat blocks, the hero headline and value props.
- **Instrument Sans** is confined to things a reader looks up: table cells, running heads, folios, source URLs, labels, eyebrows, the button.

Leave optical sizing on `auto`. Fallbacks `Georgia, "Times New Roman", serif` and `"Helvetica Neue", Arial, sans-serif`.

### Print type scale

| element | size | line height | tracking | family, weight |
|---|---|---|---|---|
| Cover title | 42pt | 1.04 | -0.021em | Newsreader 300 |
| Cover eyebrow | 8.5pt | 1.2 | 0.22em caps | Instrument Sans 500 |
| Cover subtitle | 12.5pt | 1.5 | 0 | Newsreader 300 |
| Byline name | 15pt | 1.2 | 0 | Newsreader 400 |
| Brokerage slot | 9.5pt | 1.3 | 0.155em caps | Instrument Sans 600 |
| Edition, compliance | 7.5pt | 1.8 | 0 | Instrument Sans 400 |
| Running head | 7pt | 1 | 0.185em caps | Instrument Sans 500 |
| Folio | 9.5pt | 1 | 0 | Newsreader 400 |
| Page headline | 27pt | 1.06 | -0.018em | Newsreader 300 |
| Deck | 12.5pt | 1.42 | 0 | Newsreader 300 italic |
| **Body prose** | **10.5pt** | **1.55** | 0 | Newsreader 400 |
| Subhead | 14.5pt | 1.2 | -0.008em | Newsreader 500 |
| Numbered list marker | 18pt | 1 | tabular | Newsreader 200, `--clay` |
| Aside label | 7pt | 1.2 | 0.2em caps | Instrument Sans 600 |
| Aside body | 9.5pt | 1.48 | 0 | Newsreader 400 |
| NOT FOUND headline | 26pt | 1.12 | -0.016em | Newsreader 300 italic |
| NOT FOUND body | 10pt | 1.52 | 0 | Newsreader 400 |
| Table column head | 6.6pt | 1.2 | 0.15em caps | Instrument Sans 600 |
| Table row head, data | 8.5pt | 1.25 | tabular | Instrument Sans 600 / 400 |
| Checklist item | 10.5pt | 1.5 | 0 | Newsreader 400, step name 600 |
| Phone number stat | 20pt | 1 | -0.012em tabular | Newsreader 300 |
| Source register entry | 7pt | 1.3 | 0 | Instrument Sans 400 |
| Superscript source ref | 6.2pt | 0 | 0 | Instrument Sans 600, `--clay-deep` |
| Field caption | 7.5pt | 1.5 | 0.09em | Instrument Sans 400 |

### Landing hero type scale

Masthead 12px/600/0.19em caps · Eyebrow 11.5px/600/0.22em caps · H1 `clamp(34px,3.95vw,50px)`/1.06/-0.022em Newsreader 300 · Subhead 18px/1.6 Newsreader 300 · Button 15px/600/0.075em caps · Microcopy and trust 13px/1.85 · Value prop index 38px Newsreader 200 clay · Value prop title 18.5px Newsreader 500 · Value prop body 15.5px/1.6 Newsreader 400.

---

## Layout system

### The page grid, this is the direction

```
trim              8.5in x 11in
margins           top 0.80in, bottom 0.72in, outer 0.75in, inner 0.75in
text box          7.00in x 9.48in
main measure      4.20in  (about 62 characters at 10.5pt Newsreader)
gutter            0.35in
apparatus column  2.45in
```

**The main measure sits toward the spine. The 2.45in apparatus column sits on the outer edge, mirrored across the gutter.** On a facing spread the two reading columns meet in the middle, which carries the reader across the gutter. Every callout, diagram, phone block, note and edge tab lives out at the trim where it can be ignored.

Full width objects are rare and earn it: the twenty row district table, the NOT FOUND callout, the source register.

### Spacing scale, 3pt base

`3 · 6 · 9 · 12 · 18 · 24 · 36 · 48 · 72` pt. Never use a value outside it.

### Rules

Hairline separators 0.5pt `--rule`. Aside top 1.25pt `--ink`. Table head and foot 0.75pt `--ink`. Checkbox and diagram boundary 0.75pt `--rule-strong`. **The heaviest rule in the system is 2pt `--clay` and it appears only on a NOT FOUND callout and the hero trust block.** Seven weights total across 39 pages.

### Radii and shadows

**Radius 0 everywhere. No shadow anywhere in the guide.** The only permitted `box-shadow` is on the page box inside `@media screen`, purely so paper trim reads on a gray screen background.

---

## Component list

1. **Cover.** Full bleed atmospheric field occupying the top 5in, then all type on paper below. Nothing is ever reversed out of a field. Foot block: byline name, brokerage slot, edition block right aligned, compliance line under a hairline.
2. **Atmospheric field.** CSS gradient only until real photography exists, with a caption naming the photograph that would go there. Stack: caption scrim, warm horizon glow, second warm glow from below, dark corner, base linear gradient. A 0.5pt horizon hairline at 63 percent.
3. **Running head.** One line, outer aligned, no page number. Recto carries the section name, verso carries `Before You Walk Into the Model Home · 2026`.
4. **Folio.** Bottom outer corner, Newsreader 9.5pt. Carries the path letter on path pages: `6 · A`.
5. **Page headline plus deck.** Headline max 5.2in, deck italic max 4.5in, both above the two column region.
6. **Aside callout.** Lives in the apparatus column. **Rules only, no fill.** 1.25pt ink top, hairline bottom, 7pt caps label.
7. **NOT FOUND callout.** `--sand` fill, 2pt `--clay` top rule, 26pt italic headline, two internal text columns, a 7pt caps register line at the foot. On a light page it may float in the leftover space with `margin: auto`.
8. **Data table.** Real `<caption>`, `th scope="col"` on every header, `th scope="row"` on the key column, `thead { display: table-header-group }`, `break-inside: avoid` on every row. Hairline row rules, no zebra stripe.
9. **NOT FOUND table cell.** 6.6pt Instrument Sans 600, 0.14em caps, `--muted`, with a 0.5pt dotted `--rule-strong` underline. Never colour alone.
10. **Numbered list.** Large light `--clay` numeral as a flex marker.
11. **Checklist.** A real 10pt square with a 0.75pt `--rule-strong` border as a flex marker, bold step name, regular explanation.
12. **Phone block.** Caps label, a line of context in Newsreader 9pt, then the number as a **20pt standalone stat block** with tabular figures.
13. **Diagram placeholder.** CSS only, real text labels, a caption naming the asset id.
14. **Source register.** 7pt over 1.3, `columns: 2`, `--clay-deep` numerals, full URLs with `word-break: break-all` on the URL span only.
15. **Soft close.** Hairline top, two short paragraphs, second one italic. Never a boxed CTA.
16. **Hero.** Masthead, eyebrow, headline, subhead, button, microcopy, trust line in the left column; atmospheric field in the right; three value props full width beneath with large index numerals.
17. **Button.** Solid `--clay`, `--paper` label, radius 0, no shadow. Hover `--clay-deep`. Focus visible: 2px `--clay-deep` outline, 4px offset.

---

## Motion rules

Only `transform` and `opacity` ever animate. Never `transition-all`. One easing: `cubic-bezier(.2,.8,.2,1)` at 180ms. The button lifts 1px on hover and drops 1px on active, and that is the entire motion vocabulary. The guide itself has no motion at all.

---

## Things that must never change

1. **`Real Broker, LLC` gets a designed slot, never a footnote.** Nevada law requires a licensee's advertising to identify the brokerage. On the cover it sits under `Ryan Rose` in 9.5pt Instrument Sans 600 at 0.155em caps, on a 1.25pt `--clay` rule, the only clay rule on the cover. In the hero it is set in `--ink` at 600 weight inside the trust line, under a 2px clay rule.
2. **The license slot must never reflow.** Render `[NOT FOUND]` literally inside `.lic-slot { display:inline-block; min-width:11ch; text-align:left; font-variant-numeric:tabular-nums; }` and keep it at the end of its own line. `[NOT FOUND]` is 11 characters, longer than any real Nevada number, so a real number drops in with zero geometry change. This is verified. Do not break it.
3. **Zero em-dashes (U+2014) in any file, including CSS comments.** Checked mechanically.
4. **No `position: fixed` anywhere in the guide.** It repeats on every printed page. The landing page may use it and currently does not.
5. **Bullets use the flexbox pattern.** Marker as a real flex child with `flex: 0 0 auto`. Never `li::before { position: absolute }`. Under CSS multi column that bug drops the marker onto the first letter, and the source register uses `columns: 2`.
6. **Nothing is ever reversed out of an atmospheric field**, which is what makes the ink-lean swap lossless.
7. **A caption over any field needs the scrim.** `linear-gradient(to top, rgba(8,12,10,.82) 0%, rgba(8,12,10,.68) 20%, rgba(8,12,10,0) 42%)` as the topmost background layer. Without it the caption measures 4.17:1 and fails AA.
8. **Do not use the Rose Homes LV brand.** No navy `#1C2333`, no champagne gold `#C9A86E`, no warm off white `#F7F5F0`, no Playfair Display, no Montserrat, no Bebas Neue. This guide is deliberately its own thing.
9. **Never invent a number.** Any missing fact renders literally as `NOT FOUND` and gets the sand treatment if it is a callout, the dotted caps treatment if it is a table cell.
10. **Print correctness.** `@page { size: letter; margin: 0 }`, page boxes at `height: 10.99in` in print because exactly 11in emits a blank sheet after every page, `.page:last-of-type { break-after: auto }`, wrappers set to `display: contents` in print so they contribute no height, and `print-color-adjust: exact` on every tinted surface.

---

## The ink-lean build

Add `class="ink-lean"` to `<html>`. Every atmospheric field becomes a `--print-wash` panel inside a `--rule` hairline and captions drop to `--muted`. Cover ink density falls from 37.65 percent to 5.16 percent. Ship the default build as the emailed PDF and the lean build as the printer friendly download.

---

## Three path wayfinding

Pages 6 to 17 branch three ways. Edge tabs bleed off the **outer** edge, inside the 2.45in apparatus column, at three stepped vertical positions: Path A top third, Path B middle third, Path C bottom third. **Separate the three by value, not hue:** `--ink` gray 34, `--muted` gray 90, `--rule-strong` gray 135. Three hues at one value collapse into three identical grays on a home printer. Keep 5mm of text safety from the trim. Every path page also carries a text path label above the headline and the path letter in the folio, so the path is stated three times and no single failure loses it.

---

**Em-dashes in this file: zero.**
