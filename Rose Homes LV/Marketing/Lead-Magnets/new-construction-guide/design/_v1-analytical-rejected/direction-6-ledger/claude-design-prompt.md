# Claude Design brief · Direction 6 "Ledger"

Paste this whole file into Claude Design. It is self contained. You need no other context.

---

## What you are building

A 39 page print first buyer guide plus a landing page hero for a Las Vegas real estate agent. The guide explains the hidden costs of buying a newly built home. It is deliberately **off brand** from the agent's usual identity.

**Design thesis, do not deviate:** new construction is a series of line items, and this guide prices every one. Every page is a general ledger row.

---

## Non negotiables

1. **Zero em-dashes (U+2014).** Anywhere, including CSS comments. Use commas, periods, or "and".
2. **`Real Broker, LLC` gets a designed slot,** never shrunk to fine print. Nevada law requires the brokerage name in a licensee's advertising. It appears on the cover byline and in the landing hero trust line.
3. **`[NOT FOUND]` renders literally** wherever the licence number goes. It sits in a monospace inline block with `min-width: 13ch` at the end of its line, inside a bottom anchored band, so a real 9 to 13 character Nevada number drops in with zero reflow.
4. **No `position: fixed` in the guide.** A fixed element repeats on every printed page. The landing page may use it.
5. **Bullets and checkboxes use `display:flex` with the marker as a real flex child.** Never `li::before { position:absolute }`. That bug lands the bullet on the first letter under CSS multi-column.
6. **Tables need `<caption>`, `<th scope>`, `thead { display: table-header-group }`, `break-inside: avoid` on rows.**
7. **No external images.** Any art is CSS only, labelled, self contained. No CDN except Google Fonts.
8. **Never encode meaning in color alone.** Every state carries pattern, position, or words as well.

---

## Palette, exact hexes

```css
--paper:#FAFAF7;        /* page stock, cool bone */
--white:#FFFFFF;        /* knockout boxes */
--ledger:#E8EEE9;       /* figures rail ground, columnar pad green */
--ledger-deep:#D3DFD6;  /* brought / carried forward total bands */
--unknown:#F1EBDD;      /* unpriced value ground, ALWAYS hatched */
--ink:#131A16;          /* primary text, reversed band grounds */
--ink-2:#39443E;        /* deck, secondary prose, rail labels */
--muted:#54605A;        /* audit trail, running heads, folios */
--rule:#BFC9C3;         /* hairlines, non-text */
--rule-strong:#8A968F;  /* column rules, table head rule, non-text */
--debit:#A83A14;        /* money leaving your pocket, markers, NOT FOUND */
--debit-deep:#7A2410;   /* reversed NOT FOUND tag ground */
--credit:#093026;       /* action and settled state, CTA, hero headline */
--credit-2:#0C4438;     /* CTA hover only */
```

Lowest contrast ratio in use is 4.78:1 (`--muted` on `--ledger-deep` at 7.2px/700). Everything else is 5.4:1 or better. **If you introduce a new pair, compute the ratio and keep it at or above 4.5:1.**

**Forbidden colors:** navy `#1C2333`, champagne `#C9A86E`, warm off-white `#F7F5F0` (those are the agent's other brand), and any default framework blue, indigo, or violet.

**Grayscale collisions you must design around:** `--ledger` (92.7% gray) and `--unknown` (92.3%) are identical in black and white. `--debit` (37.2%) and `--muted` (36.5%) are identical. Never let a distinction rest on either pair.

---

## Type

```html
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600;700&family=IBM+Plex+Sans:wght@400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,300..700;1,6..72,300..600&display=swap" rel="stylesheet">
```

- **Newsreader** (display serif): headlines, decks, asides, disclosure headings, soft closes, hero headline, prop headings.
- **IBM Plex Sans** (text): all body prose, lists, table cells, rail item labels.
- **IBM Plex Mono** (figure): every amount, every reference numeral, every date column, every URL, every system label, the licence slot.

`body { font-variant-numeric: tabular-nums lining-nums; }` is mandatory. Every numeral is the same width as every other numeral.

**Never use one family for two roles.** A number set in Plex Sans is a bug in this system.

### Print scale (px at 96dpi)

| Element | Size / leading / tracking |
|---|---|
| Cover title | 78 / 0.95 / -0.032em, Newsreader 600 |
| Page headline | 25.5 / 1.06 / -0.020em, Newsreader 500 |
| Deck | 15 / 1.38, Newsreader italic 400 |
| Subhead | 18 / 1.20 / -0.012em, Newsreader 600 |
| **Body** | **14 / 1.47** (10.5pt), Plex Sans 400 |
| Lists | 13.2 / 1.44, markers Mono 700 |
| Table `td` | 10.2 / 1.18 · `th` 7.5 caps 0.13em Mono 700 |
| Rail item label | 9.5 / 1.30, Plex Sans 400 |
| Rail amount | 10 / 1.0 / -0.01em, Mono 700 |
| Running head | 9.5 caps 0.17em, Mono 500 |
| **Audit trail** | **8.9 / 1.26** Plex Sans, URLs 7.35 / 1.26 Mono |

### Hero scale

Headline 52 / 1.02 / -0.028em (34 at 900px, 30 at 420px). Subhead 16.5 / 1.60. CTA 17 / 600. Prop heading 20 / 1.18. Prop body 13.5 / 1.50. Total figure 17 Mono 700.

---

## Layout system

**Page box:** `8.5in x 11in`, padding `44px 48px 40px`. Live width 720px.

**The ledger grid, identical on every page, verso and recto, never mirrored:**

```
grid-template-columns: 34px 12px 448px 16px 210px;
/*                     ref   gap  text   gap  figures  */
```

Reference on the left, description in the middle, amount on the right. This is a general ledger line, not a book spread. Do not mirror the rails on facing pages.

**Vertical order inside a page:** running head with a hairline under it · content region · audit trail with a 3px topper · folio with a 1px topper.

**Components:**

1. **Figures rail.** Tinted `--ledger` band down the full content region, 1px `--rule-strong` on its left edge and a 0.5px `--rule` amount column rule 70px from its right edge. Line items are `label · amount`, `justify-content: space-between`, 0.5px separator, amount in Mono 700, right aligned.
2. **Brought forward / carried forward bands.** `--ledger-deep` ground. Brought forward sits at the top of the rail. **Carried forward is bottom anchored** with `position:absolute; bottom:0` inside the page box. Both carry two figures: priced items and unpriced items. The carried forward on the last page of a section adds a `Dollar total` row.
3. **The unknown treatment.** `--unknown` ground plus a 45 degree `repeating-linear-gradient` hatch in `rgba(168,58,20,.30)` plus a 0.5px `--debit` border plus the literal words `NOT FOUND` in Mono 700. All four, always. This is the most important component in the system.
4. **Marginal reference apparatus.** Footnote numerals live in the 34px left rail in Mono 600 `--debit`, aligned to the top of the block they cite, right aligned. Inline markers are removed from running prose so the copy reads clean at a 6th grade level. Per row data markers (inside table cells) stay inline as 7px superscripts.
5. **Aside.** 2px `--rule-strong` topper, 0.5px `--rule` foot, Newsreader body, a Mono caps tag above.
6. **Disclosure (the NOT FOUND callout).** 3px `--debit` topper, hatched `--unknown` ground, a reversed `--debit-deep` tag, Newsreader 600 heading. It must read as generosity, not apology. Give it the page's largest heading after the h1.
7. **Data table.** 2px `--ink` above the head, 1px below, 0.5px row separators, 1px close. District column in Mono 700, dates in Mono right aligned, `where` column in `--ink-2`. **No zebra stripe.** Retired states get a 2px `--credit` rule under the words, which survives grayscale as an underline.
8. **Checklist.** 13px square, 1.4px `--rule-strong` border, `--white` fill, flex marker.
9. **Audit trail.** 3px `--ink` topper, `column-count: 3`, 0.5px column rule, entries as flex rows with the numeral in a 10px Mono column. URLs in Mono with `overflow-wrap: anywhere`. Label it `AUDIT TRAIL · SOURCES n TO n` with the verification date right aligned. It is a feature, not fine print.
10. **Phone register.** White box, 1px `--ink` border, lives in the figures rail, numbers in 12px Mono 700 `--debit`.

**Rules, four weights only:** 0.5px hairline · 1px boundary · 2px section · 3px topper, plus **3px double reserved exclusively for totals**. That double rule is the strongest mark in the guide and it is spent on the running cost.

**Radii: 0 everywhere, including buttons.** A ledger has no rounded corners.

**Spacing scale, 4px base:** 4 · 8 · 12 · 16 · 22 · 30 · 40 · 54 · 72.

---

## Landing hero

Top bar: agent name in Mono caps left, `Real Broker, LLC` right with a 1px left rule. Below it a two column grid, `1fr 452px`. Left: eyebrow rule, headline in `--credit`, subhead, CTA, microcopy with a CSS cover thumbnail placeholder, then a trust block under a 2px topper. Right: a `--ledger` statement card with a `LINE · ITEM · PAGE` header, three numbered prop rows (`01 02 03` in `--debit` Mono, page reference right aligned in the amount column), and a `TOTAL PAGES 39` band in 3px double rules.

Ground is `--paper` with a faint `repeating-linear-gradient` ruling at 27px in `rgba(138,150,143,.16)`. Keep it under 0.2 alpha or it reads as a bug.

**Mobile:** DOM order is already the mobile order. At 900px collapse to one column, drop the statement card below the button, move each page reference onto its own line under its prop, hide the thumbnail, make the CTA full width with `justify-content: space-between`. Verify zero horizontal overflow at 375px.

---

## Motion

Only `transform` and `opacity`. Never `transition-all`. CTA: `transition: transform .16s cubic-bezier(.2,.9,.3,1.2), background-color .16s ease`, hover lifts `translateY(-2px)` and shifts to `--credit-2`, active returns to 0. Every interactive element needs hover, `:focus-visible` (3px `--debit` outline, 3px offset), and active. Nothing in the print pages animates.

---

## Things that must never change

- The three column ledger grid, in that order, unmirrored.
- Tabular lining numerals globally, and every amount right aligned.
- Three families for three roles. Numbers are always mono.
- The four part unknown treatment: hatch, border, words, color. Never fewer.
- Carried forward totals bottom anchored, in 3px double rules, reporting priced and unpriced counts separately.
- Zero border radius.
- The audit trail is set as a designed register, never collapsed to a footnote or a link list.
- `Real Broker, LLC` in a bordered slot at 13px or larger.
- Ink coverage at or under about 9 percent mean. Do not add solid dark fills.

## Known constraint to plan around

At 10.5pt the supplied SID and LID copy runs about 1.78 times what two Letter pages hold in this system. Budget four pages for that section, or shed a page elsewhere. Do not solve it by shrinking type below 14px / 10.5pt: this guide is written for cold traffic at a 6th grade reading level.
