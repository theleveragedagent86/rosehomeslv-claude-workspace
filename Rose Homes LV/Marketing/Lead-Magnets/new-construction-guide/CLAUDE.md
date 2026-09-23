# CLAUDE.md, New Construction Buyer Guide (area-wide lead magnet)

A 44-page print-first buyer guide for new construction across **Las Vegas, Henderson, and Clark
County**, plus a Lofty landing page. Fed by cold Facebook traffic. Built and refreshed by the
`/new-construction-guide` skill.

**This is the area-wide, builder-agnostic asset.** It is not the per-community guide. See the
disambiguation table in [../CLAUDE.md](../CLAUDE.md) before writing anything here.

## Hard rules specific to this folder

- **Excludes Pahrump, Mesquite, and Boulder City.** Clark County minus those three. Several source
  files in the wider workspace carry rows for them; they get stripped and logged, never rendered.
- **No em-dashes.** Checked mechanically by `qa-check.py`. Hard build failure, not a style note.
- **Every number traces to `research/fact-ledger.md`.** No writer touches raw research. A claim with
  no cited source and retrieval date does not ship; it ships as the literal string `NOT FOUND`.
  The ledger rejected 431 uncited claims from the internal corpus, which is the point of it.
- **Nevada advertising:** `Real Broker, LLC` and license `S.0185572` appear on the cover, the note
  page, the back matter, and the landing page. NRS 645. Easy to lose precisely because this asset is
  deliberately off-brand.
- **Deliberately not Rose Homes navy and gold** in its researched directions, though Ryan has since
  asked for brand-colored variants as options. Both live under `design/`.
- **Print-first.** Zero `position: fixed` in the guide. Never `position: absolute` inside an
  `li::before`; that bug has shipped twice in this workspace and drops bullets onto the first letter
  under multi-column. Use flexbox bullets.
- **No depictions of people** in generated imagery (fair housing), and never imply a specific named
  community.

## The seven scripts

| Script | What it does |
|---|---|
| `generate-pdf.py` | Renders the guide to PDF over CDP. Hardened fork of the delemar exporter: measured readiness via `document.fonts.ready` plus image `decode()` instead of a fixed sleep, a free port picked at runtime, a throwaway `--user-data-dir`, and graceful teardown. The fixed-sleep original was silently rendering before all 37 font faces loaded. |
| `qa-check.py` | Ten mechanical gates: em-dash (source, PDF text layer, and HTML entities), print CSS, page count and size, blank pages, repeating table headers, accessibility, compliance strings, citations. Exit 1 on any FAIL. |
| `build-compare.py` | Regenerates `design/_compare.html`, a side-by-side of every `design/direction-*` as live scaled iframes. Auto-globs, so it picks up new rounds with no edit. Frames are 2500px wide because a two-page spread is about 2156px and anything narrower clips the right-hand page silently. |
| `build-typeround.py` | Generates rounds 4 through 6 from the round 3 archive by swapping type and, for the geometric layout, recoloring. `python3 build-typeround.py <round>`, default 6. Archives whatever round is live before overwriting `design/direction-*`, and is idempotent when re-run on the round it just built. |
| `build-svg.py` | Generates the thirteen diagrams into `build/svg/`, plus `index.md` and the two review sheets. `python3 build-svg.py` for the set, `python3 build-svg.py 04 09` for a subset. Every diagram is laid out from measured text height, never from hand-guessed y-positions. |
| `build-shell.py` | Generates `build/shell.html`, the document the fragments pour into. Lifts **both** `<style>` blocks out of the winning preview verbatim, in order, and strips only the preview stage chrome. Generated rather than transcribed because the winning file is a base plus an override layer, so hand-copying the CSS would reintroduce the exact bug the design lock exists to catch. |
| `assemble.py` | Builds `new-construction-buyer-guide.html` from the 39 page fragments, and `sources-and-citations.html` alongside it. Owns everything mechanical about citations: global numbering, the per-page source strip, the companion source list, and inlining the diagrams. Hard-fails on an unknown claim-id, an em-dash, or a `position:fixed`. |

Previews need HTTP because `file://` iframes are blocked:

```bash
cd "Rose Homes LV/Marketing/Lead-Magnets/new-construction-guide" && python3 -m http.server 8092 --bind 127.0.0.1
```

Full-page screenshots must go through CDP `Page.captureScreenshot` with `captureBeyondViewport`.
Chrome's `--screenshot` flag hangs on pages this tall.

## Design rounds

Each round renders **identical copy** across every direction (the cover, the SID and LID spread,
and the landing hero) so what is being compared is design and nothing else. The shared payload is
`outline/design-sample-content.md`. Rounds 1 to 4 ran six directions; the rounds after that narrow.

| Folder | Round | Outcome |
|---|---|---|
| `design/_v1-analytical-rejected/` | 1, analytical | Rejected. Ryan tested it on several people: "too analytical and robotic." Root cause was the brief, not the craft; it chased credibility-as-design with imagery forbidden, and typography alone cannot carry warmth. |
| `design/_v2-warm/` | 2, warm, Pozek-inspired | Superseded. Ryan picked pieces out of it rather than a whole: the layout of `direction-1-desert-bloom`, the palette of `direction-5-magazine-briefing`, and that direction's dusk photo-band header. |
| `design/_v3-directed/` | 3, directed | Superseded. Those inherited pieces plus a luxury variant and three using lifted brand navy. Ryan's verdict: direction 6's layout and color, direction 4's type, direction 3's layout, direction 2 "nice but a lot of orange", direction 1 out. |
| `design/_v4-type/` | 4, type | Superseded. One variable at a time: directions 1 to 5 were round 3 direction 6 with only the typeface pairing swapped, direction 6 was round 3 direction 3's layout recolored. Ryan's verdict: the Bodoni Moda and Archivo pairing, shown in both surviving layouts. |
| `design/_v5-layout/` | 5, layout | Superseded. Bodoni Moda and Archivo in both layouts, so the only variable was page architecture. Ryan's verdict: too much orange in both. |
| `design/direction-*/` | 6, less orange | **Decided.** Both layouts, each at two orange strengths, plus the geometric cover title reset to mixed case. Ryan chose `direction-3-geometric-orange-dialed-back` on 2026-07-28. |

**Kill the per-page source strip.** Round 1 died partly on it: 19 entries with full URLs on 34 of 39
pages ate 27 percent of every page before any body copy, and all six directors independently
overran. Attribution is now one short inline line under the paragraph it supports, with full URLs in
a numbered back appendix. Do not reintroduce it.

**The refusal callout is the design test.** 34 of 39 pages carry a `NOT FOUND`. A direction that
cannot make a refusal read as generosity rather than as a gap has failed, whatever else it does well.

**SID and LID needs three pages, not two.** Every director in rounds 2 and 3 overran a two-page
budget once photography was added. Do not solve that by crushing type below 9.5pt.

**Lifting the brand navy forces lifting the gold.** Brand gold `#C9A86E` on the lifted navy
`#304880` computes to 3.94 and fails AA for body text. Use `#D8BB84` (4.81) or brighter.

**Swapping a typeface is not a one-line change.** Round 4 proved three things worth keeping. A
serif at the grotesque's 54pt in a 6.5in measure runs the cover title to three lines and breaks the
accent phrase "Model Home" across a line, so the measure widens to 7.3in and the size drops to 52pt,
48pt for Literata, which is wider still. Tracking is applied as `calc(base + delta)` per selector,
never as one flat value, so the base file's typographic hierarchy survives the swap. And a `.page` is
a fixed 8.5x11in box with `overflow:hidden`, so a wider face pushes the compliance line off the paper
and clips it with no error anywhere: check page fit mechanically after any type change.

**Recoloring direction 3 needs a document-wide substitution, not a `:root` override.** Its inline
SVG diagrams and inline `style` attributes carry hardcoded hexes that no custom property reaches.
Overriding `:root` alone left a plum bar and a teal rail sitting inside a navy layout.

**"Too much orange" was a structural problem, not a saturation one.** Both layouts used the sunset
family for running heads, chips, folios, list markers, card tints, table zebra and photo overlays, so
the page read orange before it read anything else. The fix is handing those roles to the navy family
and leaving orange only where it carries meaning. Two objects stay warm at every strength: the
refusal panel, which is meant to be the loudest thing on the spread, and the primary button. The
`NOT FOUND` token also stays warm, because there the color is the meaning. Every reversed pair the
reduction introduces was computed, worst case 3.94 for lifted gold on `--navy-500`, which is large
display text only.

**The design is decided.** `design/direction-3-geometric-orange-dialed-back` is the reference
render and [build/design-system.md](build/design-system.md) is the frozen contract. Chapter writers
use only the classes listed there. The render wins over the document if they ever disagree.

**Read computed styles, not CSS source, when freezing a generated design.** The winning file is a
base plus an override layer, so the source does not tell you which rule won. Freezing it surfaced
that five display selectors in the geometric layout never received their tracking or weight override
at all: the override list carried class names from the other direction (`.band h1`, `.qt`) that this
one does not use, and bare `.pull` where the layout sets the more specific `.gp .pull`. No error,
no warning, just the grotesque's tight tracking under a high contrast serif on the largest headline
in the guide. Caught with `getComputedStyle`, not by reading the stylesheet.

**One card tint, `#FBEFD3`.** Ryan asked for the light blue cards to take the fill of the
"Sub association" bar in the cost diagram. It is applied to every tinted card, not only the blue
ones, because leaving a second tint behind that no longer encodes anything different is what the
palette rules forbid and it reads as an accident. Note the geometric layout draws that same bar in
`#FBE5DA`, a pinker tint; the ochre one is used in both layouts so they stay comparable.

## How the guide gets built

**One fragment is one printed page.** `build/fragments/p01.html` through `p39.html`, each a bare
`.page` element with no `<head>` or `<style>`. Per-page rather than per-chapter because every page in
this guide is a hard break anyway, so the file boundary and the page boundary agree; because `refresh`
mode regenerates exactly p33, p34, p36 and p37 and should touch nothing else; and because a QA defect
then points at a file instead of a line offset inside a chapter.

```bash
python3 build-shell.py && python3 assemble.py && python3 generate-pdf.py && python3 qa-check.py
```

**Writers never write a source number or a URL.** They write
`<sup class="src" data-claim="tax-assessment-ratio">*</sup>` and leave the foot strip empty.
`assemble.py` numbers globally in document order, fills the strip from the ledger, and generates the
companion source list. Three writers hand-numbering in parallel would collide on the first page they
shared, and a claim-id that is not in the ledger **fails the build**, which is the check that makes
the whole scheme safe.

**Citations ship in two tiers: a one line strip in the page foot, and a printed source appendix on
pages 40 to 44.** `guide-outline.md` rule 4 asks for a full URL in a per-page source strip, and the
frozen design gives that strip one line in a 48px foot that also carries the folio. Those cannot both
be true, so the foot carries the marker range, the source organizations and the verified date, and the
addresses go in the back. This is the decision already recorded under "Kill the per-page source strip"
above, and the design sample's own running foot already pointed at "the source appendix, page 41".

**The appendix is one row per unique source, not per marker.** 364 markers cite only **164 distinct
addresses**, because one statute page or program page backs many separate claims. A row per marker
repeated the same URL up to nine times and ran to 13 pages. Grouping by address is shorter and more
useful: the reader sees every number a given source backs, and the value itself is still in the body
next to its marker. **39 content pages plus 5 appendix pages is where the 44 in the header comes
from**, and `qa-check.py`'s page gate was widened from 32 to 40 to match.

**Size the appendix from a render, never from arithmetic.** The first attempt reasoned that ~94 rows
would fit and that 423 rows over 5 pages therefore produced exactly the 44 the folder already
targeted. That looked like confirmation and was coincidence: a real render overflowed by 870px,
because a wrapped URL at 7pt takes about 43px per row per column, not 10. Two renders at different row
counts solve for the true capacity, which is ~42 rows per page. `APPENDIX_PER_PAGE` carries that
derivation in a comment.

## Publishing

`lofty-constraints.md` is verified against Ryan's live Arroyo page, not inferred. The two that bite:
**no `<form>` element in the embed** (Lofty appends its own and CTAs scroll to it), and the landing
page cannot take the `/new-construction` slug because the New Construction hub is claiming it.

---

## Folder Map, keep this current

```
new-construction-guide/
├── CLAUDE.md              this file
├── generate-pdf.py        CDP renderer, measured readiness
├── qa-check.py            ten mechanical gates, exit 1 on FAIL
├── build-compare.py       regenerates design/_compare.html
├── build-typeround.py     generates rounds 4 to 6 from the round 3 archive
├── build-svg.py           generates the thirteen diagrams into build/svg/
├── build-shell.py         generates build/shell.html from the winning preview
├── assemble.py            fragments + shell -> the guide, and the source companion
├── lofty-constraints.md   verified embed constraints
├── research/
│   ├── internal/          builder-universe · blog-corpus-map · voice-exemplars
│   ├── external/          builder-facts-volume · builder-facts-regional · reputation-findings
│   │                      area-profiles · financing-and-programs · nevada-law
│   ├── fact-ledger.md     the single source of truth, 678 rows
│   └── builder-table.md   20 builders, 150 footnotes, 114 NOT FOUND cells
├── outline/               guide-outline · page-budget · audience-path-map · design-sample-content
├── design/
│   ├── _v1-analytical-rejected/   round 1
│   ├── _v2-warm/                  round 2
│   ├── _v3-directed/              round 3
│   ├── _v4-type/                  round 4, the type round
│   ├── _v5-layout/                round 5, the layout narrowing
│   ├── direction-*/               round 6, the orange reduction
│   └── DECISION.md                the pick, and how every element got there
├── build/
│   ├── design-system.md   LOCKED. the only classes, hexes and type sizes that exist
│   ├── fragment-contract.md  binding on chapter writers: skeletons, citations, rules
│   ├── shell.html         generated. the document fragments pour into
│   ├── data/              builder-table.json
│   ├── fragments/         p01.html .. p39.html, one file per printed page, plus _handback-*.md
│   └── svg/               svg-01..13.svg · index.md · _contact.html · _gray.html
├── assets/                image-manifest.md · ryan-headshot*.png|jpg · img/
├── snapshot/              market-snapshot-2026-Q3.md · archive/
└── qa/                    pages/
```

**Note on `assets/img/`:** the photography is **done**. All fifteen images are generated, reviewed
and installed, and [assets/image-manifest.md](assets/image-manifest.md) carries the prompts, the
review column, the job IDs and the regeneration procedure. The nine opener bands are 3168x1344
(373 dpi at full-bleed Letter), the four area insets and the landing hero are 2400x1792 (282 dpi),
and the cover is 3060x2053 (360 dpi). The nine borrowed 896x1200 relocation-guide photos are still
in the folder because the round 6 preview still points at three of them (`valley.jpg`,
`valley-day.jpg`, `summerlin.jpg`). Leave them until the guide is assembled; the shipping fragments
use the new names and nothing else should reference the old ones.

**Higgsfield unlimited is a browser entitlement the MCP cannot see.** `models_explore` reports
`unlim: {available: false}` and preflights 2k at 2 credits while the same account generates free in
the web app. So imagery gets generated through the browser, not the connector, and two constraints
follow: **4k is not included** (only 1k and 2k carry the Unlimited badge), and unlimited runs are
**one at a time** on the standard queue, roughly 90 to 180 seconds each, with anything submitted
during a running job silently dropped. Harvest the results back through `show_generations`, which
returns clean CloudFront URLs; the in-page URLs are signed and come back redacted. The whole set
cost 3 credits, all of it the cover, which is the only image that needed 4k.

**Say Mojave or you get Sonoran.** Unqualified "desert" gives saguaro and palo verde, which reads as
Phoenix to anyone who lives here, and a red rock prompt without explicit negatives comes back as
Utah canyon country with junipers. Three of fourteen images failed this way on the first pass and
were regenerated. It is the most likely thing to go wrong in a refresh, and it is a geography
failure, not a fair-housing one: no image in the set ever contained a person, signage or an
identifiable community.

**The diagrams are done, and they are inlined, not `<img>`ed.** Thirteen SVGs in `build/svg/`, all
viewBox width 700, each carrying `role="img"`, `aria-labelledby`, `<title>` and `<desc>`. An `<img>`
tag hides that scaffold from a screen reader and defeats print color adjustment, so the assembler
pastes the markup. [build/svg/index.md](build/svg/index.md) lists which page each one belongs to and
reproduces every description for auditing.

Two things that bit during that build and will bite again in a regeneration:

- **Size boxes from measured text, never from a guessed y-position.** The first pass hardcoded
  coordinates for text of unknown wrapped height, and twelve of thirteen diagrams had a collision or
  a clipped panel. Wrapping by character count cannot tell you the resulting height, so it cannot
  tell you where the next element goes. `build-svg.py` now wraps to a **pixel width** and every
  panel returns its own height.
- **Every hex is written out, and every class is `sv-` prefixed.** A `:root` custom property does not
  reach inside an inline SVG, which is the same failure that let a plum bar survive the round 6
  recolor. And an inline `<svg><style>` is **not** scoped in HTML, it leaks to the whole document, so
  a bare `.b` or `.n` would collide with guide classes on the same page.

Render and look at them. `_contact.html` is the color sheet and `_gray.html` is the same set
grayscaled, and the grayscale one is a gate, not a nicety: `audience-path-map.md` warns that a large
share of readers print at home in black and white, and three hues at the same value collapsing into
three identical grays is invisible on screen in color.

**Maintenance rule:** When you add, remove, move, or rename anything here, update this map and the
Folder Map in [../CLAUDE.md](../CLAUDE.md). Archiving a design round means moving it to
`design/_vN-<label>/` and adding a row to the Design rounds table above. If you move this folder,
update `paths.md` in the `/new-construction-guide` skill and every absolute reference in
`~/.claude/skills/` and `~/.claude/plugins/marketplaces/`. Never leave the map or a skill path stale.
