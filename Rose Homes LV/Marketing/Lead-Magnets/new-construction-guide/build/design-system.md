# Design system, locked

Frozen from [`design/direction-3-geometric-orange-dialed-back/preview.html`](../design/direction-3-geometric-orange-dialed-back/preview.html),
chosen 2026-07-28. See [`design/DECISION.md`](../design/DECISION.md).

**The render is the contract.** Every value below was read out of the rendered page with
`getComputedStyle`, not transcribed from the CSS source, because the winning file is a base plus an
override layer and the source alone does not tell you which rule won. If this document and the
render ever disagree, the render is right.

**Chapter writers may use only the classes in the inventory at the bottom.** No writer invents a
class, a hex, or a type size. A component that does not exist yet is a request to this document, not
a local improvisation.

---

## Color

Names below are canonical. The winning file still carries a few legacy token names from the
direction it grew out of, listed in the third column so the mapping is never guessed.

### Ground and ink

| Token | Hex | Role | Legacy name |
|---|---|---|---|
| `--paper` | `#F7F5F0` | the page ground everywhere | |
| `--paper-2` | `#EDE9E0` | second surface, table zebra, neutral card | |
| `--cream` | `#FBF8F2` | cover panel ground | |
| `--white` | `#FFFFFF` | reversed text, phone number chips | |
| `--ink` | `#1C2436` | all body text | |
| `--muted` | `#5F5A52` | attributions, captions, figure captions | |
| `--rule` | `#847B6D` | hairlines. 3.83 on paper, decorative only | |
| `--rule-strong` | `#5F5A52` | heavier hairlines and inset outlines | |

### Navy, the structural family

| Token | Hex | Role | Legacy name |
|---|---|---|---|
| `--navy-600` | `#304880` | subhead glyph squares | |
| `--navy-700` | `#2C3F6B` | headings on paper, list markers, icon chips | `--agave` |
| `--navy-800` | `#28375A` | running head tags, left folio, cover chips | `--dusk` |
| `--navy-900` | `#242F4A` | deep navy panels | `--agave-d` |
| `--navy-950` | `#141A27` | right folio, cover mark | |
| `--navy-tint` | `#E4E9F2` | **diagram rung only.** Never a card. | `--tint-agave` |

### Warm, the accent family

Orange is an accent, not a structure. It is allowed in exactly four places: the refusal panel, the
primary button, the cost diagram's rungs, and the `NOT FOUND` token. Everywhere else that used to be
warm is now navy. This is the thing round 6 existed to fix; do not undo it component by component.

| Token | Hex | Role |
|---|---|---|
| `--sunset` | `#D24018` | refusal panel, primary button. Fill only, never text on paper |
| `--clay` | `#B8360F` | text weight sunset. 5.39 on paper, 5.15 on the card tint |
| `--coral` | `#E9714A` | cost diagram rung only |
| `--ochre` | `#EFA00B` | cost diagram rung, cover credential pill. Fill only, never text |
| `--card-tint` | `#FBEFD3` | **the single card tint.** Every tinted callout card |
| `--tint-clay` | `#FBE5DA` | `NOT FOUND` token background only |
| `--gold` | `#D8BB84` | lifted gold. Type only on `--navy-900` and darker |
| `--gold-brand` | `#C9A86E` | Ryan's brand gold. Seal squares, fills only |

### Path identity, the three branching paths

Added when the diagrams were built. `audience-path-map.md` requires the three edge tabs to survive a
home black and white printer, and warns that different hues at the same value collapse into three
identical grays. So the three paths are separated by **value**, not hue, and the third one inverts:
two dark tabs with reversed type and one pale tab with dark type is unmistakable in grayscale in a
way that three navies never would be.

| Path | Token | Hex | Type on it | Ratio | Grayscale role |
|---|---|---|---|---|---|
| A, moving here | `--path-a` | `#304880` | `--paper` | 8.15 | mid |
| B, moving up | `--path-b` | `#141A27` | `--paper` | 16.02 | darkest |
| C, first build | `--path-c` | `#EDE9E0` | `--ink` | 12.80 | lightest, carries a 2pt `--navy-950` outer rule so it still reads as a tab |

Path is never carried by color alone. Every path element also prints the letter and the tab words
(`PATH A · MOVING HERE`, `PATH B · MOVING UP`, `PATH C · FIRST BUILD`), which is the same redundancy
the running head and folio letter already provide.

### Computed contrast, worst cases

| Pair | Ratio | Verdict |
|---|---|---|
| `--ink` on `--card-tint` | 13.57 | AA and AAA |
| `--ink` on `--paper-2` | 12.79 | AA and AAA |
| `--navy-700` on `--paper` | 9.49 | AA and AAA |
| `--navy-700` on `--card-tint` | 9.06 | AA and AAA |
| `--paper` on `--navy-800` | 10.80 | AA and AAA |
| `--gold` on `--navy-800` | 6.37 | AA |
| `--muted` on `--card-tint` | 5.99 | AA |
| `--clay` on `--card-tint` | 5.15 | AA |
| `--gold` on `--navy-500` (`#375498`) | 3.94 | **large display text only** |

Nothing is encoded by color alone anywhere in this system. Status tokens carry a literal word, a
glyph and a rule weight in addition to their color.

---

## Type

`Bodoni Moda` display, `Archivo` text, both from Google Fonts.

```
family=Bodoni+Moda:ital,opsz,wght@0,6..96,400..900;1,6..96,400..900
&family=Archivo:ital,wdth,wght@0,62..125,100..900;1,62..125,100..900
```

Display weight is **700 large, 600 medium**, never 800. Bodoni's thick strokes get heavy fast, and
at 800 the thin strokes go brittle by comparison.

Every display selector is tracked at `calc(base + .022em)`. The delta is added rather than replacing,
so the hierarchy the layout established survives. A high contrast serif does not want the tracking a
grotesque wants, and a single flat value would flatten the hierarchy along with the tightness.

### Display scale, as rendered

| Element | Class | Size | Weight | Tracking |
|---|---|---|---|---|
| Cover title | `.cover-title` | 46pt, mixed case | 700 | -.008em |
| Section opener headline | `.op-h` | 31pt | 700 | -.008em |
| Landing hero headline | `.hero h1` | clamped, 56px at 1280 | 700 | -.008em |
| Pull line | `.gp .pull` | 23pt | 700 | -.012em |
| Refusal headline | `.refuse h3` | 21pt | 700 | -.006em |
| Opener sub line | `.gp .op-line` | 19pt | 600 | -.002em |
| Declarative answer | `.a` | 15pt (`.a.sm` 12.6pt) | 600 | +.002em |
| Lead-in headline | `.gp .hit` | 14.5pt | 600 | 0 |
| Folio | `.folio` | 15pt | 700 | +.002em |
| Phone number | `.phone-num` | 11.6pt | 600 | +.002em |
| Landing prop heading | `.prop h3` | 15px | 600 | +.007em |

### Text scale, as rendered

| Role | Class | Size and leading |
|---|---|---|
| Body | `.gp p` | 9.5pt / 1.5 |
| Card body | `.card p` | 9.4pt / 1.44 |
| Numbered list item | `.nlist .t` | 9.5pt / 1.45 |
| Checklist item | `.chk .t` | 8.2pt / 1.36 |
| Table cell | `table.sid td` | 8pt / 1.2 |
| Table row header | `table.sid tbody th` | 8pt / 1.2, weight 800 |
| Table column header | `table.sid th[scope=col]` | 6.2pt / 1, caps, +.05em |
| Attribution | `.attr` | 7.4pt / 1.42, weight 600 |
| Figure caption | `.figcap` | 7.2pt / 1.38, weight 600 |

**Never set body copy below 9.5pt to solve a fit problem.** The fix is page budget. SID and LID
takes three pages, not two; every director who tried two overran.

---

## Geometry

| Token | Value |
|---|---|
| Page | 8.5in x 11in, `overflow:hidden` |
| Print page box | 8.5in x **10.96in**, not 11in. At exactly 11in Chrome pushes a sub-pixel sliver onto the next sheet and you get a blank page between every real one |
| `--pad` | .55in |
| Radii | `--r-xs` 3pt, `--r-sm` 6pt, `--r-md` 10pt, `--r-lg` 16pt, `--r-xl` 26pt |
| Two column grid | `.cols`, `minmax(0,1fr) minmax(0,1fr)`, 18pt gap |

---

## Citations, the two tier contract

`guide-outline.md` rule 4 asks for a full URL in a per-page source strip. The frozen design gives
that strip **one line inside a 48px foot** that also carries the folio. The guide cites **254 unique
URLs**. Those two facts cannot both be satisfied, so the citation architecture is split, and this
section is the ruling. It was decided here rather than improvised in a fragment because three writers
working in parallel would otherwise invent three different schemes.

**Writers never write a source number and never write a URL.** Both are generated.

| Tier | Where | Who writes it |
|---|---|---|
| Body marker | `<sup class="src" data-claim="tax-assessment-ratio">*</sup>` right after the fact | the chapter writer, by claim-id |
| Foot strip | `.srcnote` in the page foot: marker range, the source organizations, the verified date | `assemble.py`, from the ledger |
| Full URL | the companion source list, one row per marker: number, claim-id, statement, value, URL, verified date | `assemble.py`, from the ledger |

**Why a companion file and not an appendix.** 254 URLs set at 7pt is four to five extra Letter pages,
which pushes the guide to 43 and fails the 32 to 40 page gate in `qa-check.py`. The companion ships
in the same download, is named on p2 and p39, and regenerates from the ledger mechanically, which
also makes the quarterly refresh free. A reader who wants to check a number still gets a URL and a
date for every single one.

**Numbering is global and mechanical, 1 to N in document order.** A writer who hand-numbered would
collide with the other two writers on the first page they shared. The marker's `data-claim` is the
only thing that has to be right, and `assemble.py` fails the build on a `data-claim` that is not in
the ledger. That check is the reason the scheme is safe.

**The builder table keeps its own printed footnote run** on p32 to p35, because `builder-table.md`
already carries one and the plan's verification gate names it specifically: every cell resolves to a
URL and a verified date, or to the literal `NOT FOUND`.

---

## Class inventory, the allowed set

### Page scaffolding
`page` · `spread` · `pad` · `cols` · `gp` · `body` · `two` · `sm`

### Running heads and folios
`band` · `tone` · `head` · `rh-a` · `rh-b` · `foot` · `foot-l` · `foot-r` · `folio` · `srcnote`

### Prose and headings
`op-eyebrow` · `op-h` · `op-line` · `op-deck` · `op-body` · `hit` · `a` · `pull` · `attr` · `src`

### Question subheads
`q` with one of `q-clay` · `q-agave` · `q-ink` · `q-white`

### Cards and lists
`card` with one of `card-clay` · `card-coral` · `card-agave` · `card-dusk` ·
`nlist` · `n` · `t` · `chk` · `box`

*(The four card modifiers now render the same tint. They are kept as separate names because the
markup already distinguishes them and collapsing them is a find-and-replace, not a design decision.
Do not rely on them looking different.)*

### The refusal callout
`refuse` · `ribbon` · `beat` · `split`

### Tables and status tokens
`tbl-wrap` · `sid` · `tok` with `tok-nf` or `tok-done`

### Figures
`fig` · `figcap` · `legend`

### Contact and close
`phone-row` · `who` · `phone-num` · `close` · `mk`

### Cover
`cover-photo` · `cover-top` · `cover-panel` · `cover-eyebrow` · `cover-title` · `cover-sub` ·
`chip` with `chip-sunset` · `chip-coral` · `chip-agave` · `mark` · `sq` · `seam` · `geo` · `cred` ·
`byline` · `byname` · `brokerage` · `edition` · `compliance` · `lic` · `lift` · `scrim` · `dissolve`

### Landing page
`hero-frame` · `frame-1280` · `frame-375` · `hero` · `hero-nav` · `brand` · `broker` · `hero-grid` ·
`hero-eyebrow` · `sub` · `props` · `prop` with `prop-1` · `prop-2` · `prop-3` · `ic` · `cta-row` ·
`btn` · `micro` · `trust` · `lock` · `hero-art` · `hero-photo` · `map-card`

### Added for the shipping guide, in `build/shell.html`
The preview only had to show three pages and a hero. These are the pieces a 39 page document needs
and a 3 page sample did not. They are generated into the shell by `build-shell.py`, so they are part
of the contract, not a local improvisation.

`skip` · `toc` with `lbl` · `dots` · `pg` · `grp` · `tab` with `tab-a` · `tab-b` · `tab-c` ·
`tearout` · `fig narrow`

- **`tab-a/b/c`** are the path edge tabs. `audience-path-map.md` requires a reader to find their path
  from the edge of the closed stack, so the three are separated by **value** and the pale one inverts
  with a 2pt outer rule. Every hex is written out, because a `:root` custom property is no more
  reliable here than it was inside the inline SVGs.
- **`fig`** now sizes an **inlined** `<svg>`. `build/svg/index.md` requires inlining rather than
  `<img>`, so `role="img"`, `<title>` and `<desc>` reach a screen reader and print color adjustment
  reaches the fills. `wide` spans both grid columns. `narrow` is the 236px width the preview used.
- **`a`** is styled for the first time here. The preview contained no links, so nothing styled them
  and all 21 anchors in the guide rendered default browser blue.

### Diagram sizing, the rule that was measured

Every diagram is authored at **viewBox width 700** and its smallest label is **8 design units**.
Rendered at width `W`, that label prints at `6 x (W / 710)` points. The printed page measure is 710px.

| Placement | Rendered width | Smallest label | Verdict |
|---|---|---|---|
| full measure | 710px | 6.0pt | legible |
| 85 percent | 604px | 5.1pt | floor, acceptable |
| one `.cols` column | 343px | 2.9pt | **illegible** |
| `.fig narrow` | 236px | 2.0pt | **illegible for a 700 wide diagram** |

**A 700 wide diagram may not sit inside a `.cols` column, and may not take `.fig narrow`.** Four did
in the first pass and printed labels between 2.9 and 3.2pt. Neither an inline `style="width:3.3in"`
nor `narrow` is a legitimate way to make a diagram fit a page; if it does not fit, the page has too
much on it, and the fix is on the page.

### Preview stage only, never in the shipping guide
`stage` · `cap` · `rail` · `spread`

These are **stripped by `build-shell.py`** and are not present in the shipping document. If one shows
up in a fragment it will render unstyled.

---

## Hard rules

- **Zero `position: fixed`** anywhere in the guide. It is print-first.
- **Never `position: absolute` inside an `li::before`.** That bug has shipped twice in this
  workspace and drops bullets onto the first letter under multi-column. Both list components here
  use flexbox markers; keep it that way.
- **`break-inside: avoid`** on `.card`, `.refuse`, `.tbl-wrap`, `.fig`, `.chk li`, `.nlist li`,
  `.close`, `.prop` and `table.sid`. Already set; do not remove.
- **`thead { display: table-header-group }`** so the builder table repeats its header across page
  breaks.
- **No em-dashes.** Mechanically checked. A build failure, not a style note.
- **Check page fit mechanically after any type or copy change.** A `.page` is a fixed box with
  `overflow:hidden`, so overset text vanishes with no error anywhere. The compliance line falling
  off the cover is the failure mode that already happened once.
