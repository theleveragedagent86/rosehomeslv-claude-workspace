# NRG Research 02 — Builder Page Cluster

Target: `https://www.nevadarealestategroup.com/builders/*`
Researched: 2026-07-25 (Agent B)
Method: raw HTML fetch of all 18 pages + `/builders/` index, parsed for headings, JSON-LD, links, forms.

---

## 0. TL;DR

- **All 18 builder URLs return HTTP 200.** No 404s.
- `/builders/` (index) returns **200 but is NOT a real index** — it serves the hub page content (`<h1>New Construction Homes in Las Vegas`, 9,642 words) with `<link rel="canonical" href="https://www.nevadarealestategroup.com/new-construction/">`. So it is a **duplicate alias canonicalized to the hub**. The real hub is `/new-construction/`.
- **There is one rigid shared template.** All 18 pages have **exactly 8 H2s, in identical order, with the builder name token-substituted.** Zero deviation across all 18.
- **No sticky table of contents on builder pages.** The "On This Page" TOC component exists only on the hub `/new-construction/`.
- **No IDX / MLS listing feed on builder pages.** The only `IDX`/`MLS` strings are the sitewide footer legal disclosure (`<details class="footer-idx">`). The live listing feed ("Active New-Construction Homes For Sale Right Now") lives only on the hub.
- **Zero `<table>` elements on any builder page.** All tabular-looking content is CSS grid card markup.
- **Link graph is a fully-connected mesh, not hub-and-spoke.** Every builder page links to all 18 builder pages including itself.
- Tech: **Next.js** (App Router, `/_next/static/chunks/`, turbopack), Vercel (`dpl_` deploy param), GTM `GTM-W9BG6VB9`.

---

## 1. The Shared Template

Deep-dived: **dr-horton** (national volume, 18 communities, $308K–$822K), **blue-heron** (luxury custom, 10 communities, $1.5M–$10M+), **touchstone** (entry-level, 3 communities, $305K–$471K). All three are the same component tree with different data.

### 1.1 Exact section order (H1 → H2, in DOM order inside `<main>`)

| # | Level | Pattern | dr-horton actual |
|---|---|---|---|
| — | breadcrumb | `Home › New Construction › {Builder}` | Home › New Construction › D.R. Horton |
| — | **H1** | `{Builder} Homes in Las Vegas` | D.R. Horton Homes in Las Vegas |
| — | hero sub | `{N} active communities · {Builder}` + CTA row + warning badge | `18 active communities · D.R. Horton` / Tour with NREG / Call / All Builders / `⚠️ Critical · Read Before Visiting` |
| 1 | **H2** | `Visiting {Builder}? Your timing decides who represents you.` | identical |
| | H3 | `Walk in alone` (✗ column, 5 bullets) | identical |
| | H3 | `Register with NREG first` (✓ column, 4 bullets + trust line) | identical |
| 2 | **H2** | `{Builder} Communities in Las Vegas ({N})` | D.R. Horton Communities in Las Vegas (18) |
| | H3 | `{City} {n} communities` — one per city, desc by count | North Las Vegas 10 / Henderson 5 / Las Vegas 3 |
| 3 | **H2** | `About {Builder} in Las Vegas` | 3–4 prose paragraphs, ~300 words |
| | H3 | `Get Builder Incentives & Floor Plans` (the lead form) | identical on all 18 |
| 4 | **H2** | `Frequently Asked Questions About {Builder}` | 6 × H3 questions |
| 5 | **H2** | `{Builder} and new-construction articles` | 3 × H3 blog cards |
| 6 | **H2** | `Other Las Vegas builders` | 18-chip grid |
| 7 | **H2** | `Related Reading` (+ Trademark & Affiliation Notice) | 3 shared blog links + `/new-construction/` |
| 8 | **H2** | `Find {Builder} Homes in Las Vegas` | final CTA, Call + Email Us |

**Verified identical H2 order and phrasing across all 18 pages.** The only variables are the builder name string and the community count integer.

### 1.2 Anchor IDs

Sparse. Only **four** IDs exist in the whole page:

```
nav#nav          class="nav-internal"     (sitewide header)
div#main-content                          (skip-link target)
section#lead-form                         (the incentives form)
section#faq                               (FAQ block)
```

The H2/H3 headings themselves carry **no `id` attributes** — which is exactly why there is no TOC. Only 3 in-page anchor hrefs exist: `#main-content` (skip link) and `#lead-form` ×2.

### 1.3 Heading pattern

- **1 × H1**, always `{Builder} Homes in Las Vegas` (kb-home is the one variant: "KB Home New Construction in Las Vegas").
- **8 × H2**, fixed order above.
- **12–17 × H3**, all nested under H2s 1, 2, 3, 4, 5. Never any H4+.
- H3 distribution: 2 (compare columns) + N (city groups) + 1 (form) + 5–6 (FAQ) + 3 (blog cards).

### 1.4 Sticky TOC — NO

Builder pages have **no TOC component**. Confirmed by absence of heading `id`s and absence of `#`-anchor nav. The hub `/new-construction/` has an `On This Page` H2 block; the spokes deliberately do not.

### 1.5 IDX embed — NO

No IDX embed, no listing feed, no map, no iframe (the only `<iframe>` is the hidden GTM noscript pixel). Builder pages are pure static content + forms. The community grid is hand-curated internal links, not an MLS query.

### 1.6 Tables — NO

`<table>` count = **0** on all 18. `<details>` count = 0 inside `<main>` (the 2 page-level `<details>` are the footer IDX disclosure and a footer nav accordion). FAQ answers are **always-visible divs**, not accordions — good for snippet extraction.

### 1.7 Forms — 2 per page

**Form 1 — `<form class="nc-lead-form">`** (inside `#lead-form`, under H3 "Get Builder Incentives & Floor Plans"):

| field | type | required |
|---|---|---|
| `builder` | hidden (pre-filled with builder name) | — |
| `source` | hidden | — |
| `website` | text (honeypot) | — |
| `firstName` / `lastName` | text | yes |
| `email` | email | yes |
| `phone` | tel | yes |
| `area` | select — Summerlin / Henderson / SW LV / NLV / Lake Las Vegas / Boulder City / NW–Skye Canyon / Open to all | yes |
| `budget` | select — Under $400K / $400–600K / $600–800K / $800K–1.2M / $1.2–2M / $2M+ | yes |
| `timeline` | select — 30 days / 1–3mo / 3–6mo / 6–12mo / Just researching | yes |
| `notes` | textarea, prefilled `I'm interested in {Builder} new construction homes.` | no |

**Form 2 — `<form class="ccm__form" action="/api/leads/buyer/" method="POST">`** — sitewide footer buyer form (name/email/phone/timeline + honeypot).

Both use a `website` honeypot field. Consent line names "Nevada Real Estate Group, Chris Nevada, and LPT Realty (the brokerage of record)".

### 1.8 CTA blocks

CTAs repeat aggressively — phone appears **4×** per page:

1. Hero: `Tour with NREG` (→ `#lead-form`), `Call (702) 637-1759`, `All Builders` (→ `/new-construction/`)
2. Section 1 close: `REGISTER FREE NOW` (→ `#lead-form`), `CALL (702) 637-1759`
3. Section 3: the lead form itself
4. Section 8: `Call (702) 637-1759`, `Email Us` (→ `mailto:info@nevadagroup.com`)

Plus sitewide footer: `Talk to a Buyer's Agent → /buyers/`, `Get Free Home Value → /home-value-estimator/`, Reno line (775) 277-2120.

---

## 2. Per-Builder Inventory (all 18)

TOC = sticky table of contents. IDX = live listing feed. All meta descriptions are unique. All pages: **0 tables, 8 H2s, 2 forms, no TOC, no IDX**.

| URL | Status | H1 | Meta title | Meta desc len | Words (main) | H2s | TOC | IDX | FAQs | Tables | Price range quoted | Communities |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `/builders/dr-horton/` | 200 | D.R. Horton Homes in Las Vegas | D.R. Horton Homes in Las Vegas \| Nevada Real Estate Group | 147 | 1,694 | 8 | No | No | 6 | 0 | $308K–$822K | 18 |
| `/builders/lennar/` | 200 | Lennar Homes in Las Vegas | Lennar Las Vegas \| Everything's Included Homes | 145 | 1,825 | 8 | No | No | 6 | 0 | $300K–$800K+ | 41 |
| `/builders/kb-home/` | 200 | KB Home New Construction in Las Vegas | KB Home Las Vegas \| Built-to-Order Construction | 141 | 1,921 | 8 | No | No | 6 | 0 | $300K–$700K+ | 41 |
| `/builders/pulte-del-webb/` | 200 | Pulte and Del Webb in Las Vegas | Pulte & Del Webb Las Vegas \| New Builds & 55+ Homes | 140 | 2,052 | 8 | No | No | 6 | 0 | Pulte $450K–$900K+; Del Webb $300K–$700K | 60 |
| `/builders/toll-brothers/` | 200 | Toll Brothers Homes in Las Vegas | Toll Brothers Las Vegas \| Luxury New Construction | 136 | 1,894 | 8 | No | No | 6 | 0 | $550K–$2M+ | 49 |
| `/builders/taylor-morrison/` | 200 | Taylor Morrison Homes in Las Vegas | Taylor Morrison Homes Las Vegas \| New Construction | 202 | 1,808 | 8 | No | No | 6 | 0 | $400Ks–$1M+ | 38 |
| `/builders/richmond-american/` | 200 | Richmond American Homes in Las Vegas | Richmond American Homes Las Vegas \| New Builds | 142 | 1,730 | 8 | No | No | 6 | 0 | $350K–$700K+ | 24 |
| `/builders/tri-pointe/` | 200 | Tri Pointe Homes in Las Vegas | Tri Pointe Homes Las Vegas \| New Construction Builder | 125 | 1,573 | 8 | No | No | **5** | 0 | $500Ks–$900K+ | 3 |
| `/builders/woodside/` | 200 | Woodside Homes in Las Vegas | Woodside Homes Las Vegas \| New Construction Builder | 134 | 1,542 | 8 | No | No | **5** | 0 | $300Ks–$700K+ | 12 |
| `/builders/beazer/` | 200 | Beazer Homes in Las Vegas | Beazer Homes Las Vegas \| Energy-Efficient Builder | 187 | 1,663 | 8 | No | No | 6 | 0 | $300Ks–$600K+ | 13 |
| `/builders/century-communities/` | 200 | Century Communities Homes in Las Vegas | Century Communities Las Vegas \| Skye Canyon Builder | 197 | 1,749 | 8 | No | No | 6 | 0 | $300K–$600K+ | 38 |
| `/builders/lgi/` | 200 | LGI Homes in Las Vegas | LGI Homes in Las Vegas \| CompleteHome \| Nevada Real Estate Group | 155 | 1,569 | 8 | No | No | 6 | 0 | $290K–$450K | 1 |
| `/builders/shea/` | 200 | Shea Homes in Las Vegas | Shea Homes in Las Vegas \| Trilogy Sunstone 55+ \| NREG | 143 | 1,609 | 8 | No | No | 6 | 0 | $399,990–$705K+ | 20 |
| `/builders/blue-heron/` | 200 | Blue Heron Homes in Las Vegas | Blue Heron Homes in Las Vegas \| Vegas Modern \| NREG | 149 | 1,740 | 8 | No | No | 6 | 0 | $1.5M–$10M+ | 10 |
| `/builders/christopher/` | 200 | Christopher Homes in Las Vegas | Christopher Homes in Las Vegas \| SkyVu \| Nevada Real Estate Group | 153 | 1,548 | 8 | No | No | 6 | 0 | $2M–$8M | 10 |
| `/builders/harmony/` | 200 | Harmony Homes in Las Vegas | Harmony Homes in Las Vegas \| Vista Cielo \| NREG | 163 | 1,517 | 8 | No | No | 6 | 0 | $200Ks–$471K | 1 |
| `/builders/storybook/` | 200 | StoryBook Homes in Las Vegas | StoryBook Homes in Las Vegas \| Cadence \| Nevada Real Estate Group | 152 | 1,507 | 8 | No | No | 6 | 0 | $350K–$565K | 1 |
| `/builders/touchstone/` | 200 | Touchstone Living Homes in Las Vegas | Touchstone Living in Las Vegas \| Independence \| NREG | 155 | 1,575 | 8 | No | No | 6 | 0 | $305K–$471K | 3 |
| `/builders/` | 200 | *(New Construction Homes in Las Vegas)* | New Construction Homes Las Vegas \| 18 Builders | — | 9,642 | 20+ | **Yes** | **Yes** | many | — | — | 18 builders |

**Word count band: 1,507–2,052. Mean ~1,700.** Tight and deliberate — even a 1-community builder (LGI, Harmony, StoryBook) gets ~1,520 words. They pad with the About narrative and FAQs rather than skipping sections.

### City grouping per builder (H3s under section 2)

| Builder | City groups |
|---|---|
| dr-horton | North Las Vegas 10 / Henderson 5 / Las Vegas 3 |
| lennar | Las Vegas 19 / Henderson 12 / North Las Vegas 10 |
| kb-home | Las Vegas 17 / North Las Vegas 13 / Henderson 11 |
| pulte-del-webb | Henderson 30 / Las Vegas 23 / North Las Vegas 7 |
| toll-brothers | Las Vegas 36 / Henderson 13 |
| taylor-morrison | Las Vegas 27 / Henderson 8 / North Las Vegas 3 |
| richmond-american | Henderson 10 / Las Vegas 8 / North Las Vegas 6 |
| tri-pointe | Las Vegas 3 |
| woodside | Las Vegas 8 / Henderson 4 |
| beazer | Henderson 6 / Las Vegas 4 / North Las Vegas 3 |
| century-communities | Las Vegas 26 / North Las Vegas 5 / Henderson 5 / Boulder City 1 / Pahrump 1 |
| lgi | Las Vegas 1 |
| shea | Las Vegas 16 / Henderson 3 / North Las Vegas 1 |
| blue-heron | Henderson 8 / Las Vegas 2 |
| christopher | Henderson 7 / Las Vegas 3 |
| harmony | Las Vegas 1 |
| storybook | Henderson 1 |
| touchstone | Henderson 2 / Las Vegas 1 |

Cities are sorted **descending by community count**, and the H3 pluralizes correctly ("1 community" vs "3 communities").

---

## 3. Internal Linking Pattern — the Link Graph

### 3.1 Outbound link budget per page (measured, inside `<main>`)

| Page | Builder links | Self-link | Community pages | Blog posts | `/new-construction/` | `tel:` | Anchors | External | **Total** |
|---|---|---|---|---|---|---|---|---|---|
| dr-horton | 18 | Yes | 18 | 6 | 3 | 4 | 2 | 3 | 59 |
| lennar | 18 | Yes | 41 | 6 | 3 | 4 | 2 | 3 | 82 |
| kb-home | 18 | Yes | 41 | 6 | 3 | 4 | 2 | 3 | 82 |
| pulte-del-webb | 18 | Yes | 60 | 6 | 3 | 4 | 2 | 3 | 101 |
| toll-brothers | 18 | Yes | 49 | 6 | 3 | 4 | 2 | 3 | 90 |
| taylor-morrison | 18 | Yes | 38 | 6 | 3 | 4 | 2 | 3 | 79 |
| richmond-american | 18 | Yes | 24 | 6 | 3 | 4 | 2 | 3 | 65 |
| tri-pointe | 18 | Yes | 3 | 6 | 3 | 4 | 2 | 3 | 44 |
| woodside | 18 | Yes | 12 | 6 | 3 | 4 | 2 | 3 | 53 |
| beazer | 18 | Yes | 13 | 6 | 3 | 4 | 2 | 3 | 54 |
| century-communities | 18 | Yes | 38 | 6 | 3 | 4 | 2 | 3 | 79 |
| lgi | 18 | Yes | 1 | 6 | 3 | 4 | 2 | 3 | 42 |
| shea | 18 | Yes | 20 | 6 | 3 | 4 | 2 | 3 | 61 |
| blue-heron | 18 | Yes | 10 | 6 | 3 | 4 | 2 | 3 | 51 |
| christopher | 18 | Yes | 10 | 6 | 3 | 4 | 2 | 3 | 51 |
| harmony | 18 | Yes | 1 | 6 | 3 | 4 | 2 | 3 | 42 |
| storybook | 18 | Yes | 1 | 6 | 3 | 4 | 2 | 3 | 42 |
| touchstone | 18 | Yes | 3 | 6 | 3 | 4 | 2 | 3 | 44 |

**Invariants:** every page emits exactly 18 builder links, 6 blog links, 3 hub links, 4 tel links, 2 anchors, 3 external. Only the community-link count varies.

### 3.2 Shape: fully-connected mesh, NOT hub-and-spoke

The `Other Las Vegas builders` grid (H2 #6) is **byte-identical on all 18 pages** — same 18 links, same order, and it **includes a self-link**. Verified: union of builder links = 18, and every page's set is identical.

```
                    /new-construction/  (hub, canonical target of /builders/)
                       ▲   ▲   ▲
                       │   │   │   ← 3 links back from EVERY spoke
       ┌───────────────┴───┴───┴────────────────┐
       │                                        │
  ┌────┴─────┐   fully-connected K18 mesh  ┌────┴─────┐
  │dr-horton │◄──────────────────────────►│blue-heron│
  └────┬─────┘   (every builder links to  └────┬─────┘
       │          every other builder,          │
       │          incl. itself)                 │
       ▼                                        ▼
  198 distinct community pages  ◄─── 82 of these are shared by 2+ builders
  (e.g. /cadence/ ← 8 builders)       116 are exclusive to one builder
       │
       ▼
  3 shared "Related Reading" blogs (on all 18) + 3 rotating builder-specific blogs
```

**Builder ↔ builder order in the chip grid** (same on every page, roughly by market size, not alphabetical):
`lennar, kb-home, pulte-del-webb, toll-brothers, dr-horton, richmond-american, taylor-morrison, tri-pointe, century-communities, beazer, shea, lgi, blue-heron, christopher, woodside, harmony, storybook, touchstone`

### 3.3 Link back to `/new-construction/` — 3 per page

1. **Breadcrumb** — `Home › New Construction › {Builder}` (also in BreadcrumbList JSON-LD)
2. **Hero CTA button** — `All Builders`
3. **Related Reading footer** — `All Las Vegas New Construction Communities`

Note the JSON-LD breadcrumb uses the **un-trailing-slashed** form `https://www.nevadarealestategroup.com/new-construction` while the HTML `href` uses `/new-construction/`. Minor inconsistency worth avoiding in a clone.

### 3.4 Community-page cross-linking (the real spider web)

The 18 builder pages collectively link to **198 distinct community pages**. Community pages are flat root-level URLs (`/cadence/`, `/summerlin-west/`, `/skye-canyon/`) — **not** nested under `/communities/`.

- **82 community pages are shared by 2+ builders** — this is what creates the mesh density.
- **116 are exclusive to a single builder.**

Most-shared community pages:

| Shares | Community page | Linked from |
|---|---|---|
| 8 | `/cadence/` | dr-horton, lennar, toll-brothers, taylor-morrison, richmond-american, woodside, century-communities, storybook |
| 6 | `/summerlin-west-stonebridge-area/` | lennar, pulte-del-webb, toll-brothers, taylor-morrison, woodside, shea |
| 6 | `/summerlin-west/` | lennar, pulte-del-webb, toll-brothers, taylor-morrison, woodside, shea |
| 5 | `/heartland-tule-springs/` | dr-horton, lennar, kb-home, richmond-american, century-communities |
| 5 | `/north-las-vegas/` | dr-horton, lennar, kb-home, pulte-del-webb, richmond-american |
| 5 | `/centennial-hills-north/` | lennar, kb-home, pulte-del-webb, taylor-morrison, century-communities |
| 5 | `/summerlin-grand-park/` | lennar, kb-home, pulte-del-webb, toll-brothers, taylor-morrison |
| 5 | `/skye-canyon/` | lennar, taylor-morrison, woodside, century-communities, shea |
| 5 | `/north-las-vegas-park-highlands/` | lennar, kb-home, taylor-morrison, richmond-american, shea |
| 5 | `/summerlin-redpoint-square/` | toll-brothers, taylor-morrison, tri-pointe, woodside, shea |

Each community link's anchor text embeds the **price range**: `Cadence$350K–$800K`, `Aurora Heights$336K–$425K`. Some add a parent master-plan label: `Villas at Seven HillsSeven Hills$450K–$750K`.

### 3.5 Blog linking — 3 shared + 3 rotating

**Section 7 "Related Reading" — identical on all 18 pages (18×3 = 54 links):**
- `/blog/vegas-new-build-700k-vs-summerlin-2026/` — "$710K Vegas Build vs Summerlin: Better Value 2026?"
- `/blog/las-vegas-home-prices-2026-up/` — "Las Vegas Home Prices 2026: Up or Down?"
- `/blog/las-vegas-homebuilder-sales/` — "Las Vegas Homebuilder Sales"

**Section 5 "{Builder} and new-construction articles" — 3 cards, builder-relevant first then filler:**

| Frequency | Blog URL | Role |
|---|---|---|
| 11× | `/blog/new-construction-homes-north-las-vegas-guide-2026/` | filler |
| 11× | `/blog/new-construction-incentives-las-vegas-may-2026-builder-roundup/` | filler |
| 11× | `/blog/best-real-estate-agent-for-new-construction-in-las-vegas-your-2026-guide-.../` | filler |
| 6× | `/blog/new-construction-homes-sparks-builders-guide-2026/` | filler |
| 5× | `/blog/new-construction-homes-henderson-builders-guide-2026/` | filler |
| 1× | `/blog/dr-horton-plan-2538-heartland-manor-north-las-vegas-2026/` | dr-horton exclusive |
| 1× | `/blog/dr-horton-plan-2660-symmetry-falls-cadence-henderson-2026/` | dr-horton exclusive |
| 1× | `/blog/meriden-kb-home-henderson-new-master-plan-2026/` | kb-home exclusive |
| 1× | `/blog/del-webb-sierra-canyon-reno-active-adult-guide-2026/` | pulte-del-webb exclusive |
| 1× | `/blog/christopher-homes-blue-heron-toll-brothers-summerlin-comparison-2026/` | 3-builder comparison post |
| 1× | `/blog/taylor-morrison-sinatra-model-summerlin-2026/` | taylor-morrison exclusive |
| 1× | `/blog/richmond-american-elm-lexington-chase-las-vegas-2026/` | richmond-american exclusive |
| 1× | `/blog/tri-pointe-vela-plan-3-inspirada-henderson-2026/` | tri-pointe exclusive |
| 1× | `/blog/vista-cielo-harmony-homes-las-vegas-affordable-2026/` | harmony exclusive |
| 1× | `/blog/watercolor-touchstone-living-las-vegas-snhba-community-2026/` | touchstone exclusive |

Plus `/blog/` ("See all blog posts →"). **The tactic: write ONE model/plan-specific blog per builder, then backfill the remaining 2 card slots with 5 evergreen new-construction guides.** Only 10 of 18 builders have an exclusive post; the rest run 3 fillers.

### 3.6 Non-builder outbound

- `https://red.nv.gov/` ×2 (Nevada Real Estate Division, license verification) — trust signal in the Trademark Notice
- `https://www.nevadarealestategroup.com` (self, absolute, in the notice)
- `/terms-of-use/`, `/privacy-policy/` (in the form consent line)
- `mailto:info@nevadagroup.com`, `tel:+17026371759`

---

## 4. Full Content Skeleton — `/builders/dr-horton/` (verbatim-ish)

Clone this outline.

**Breadcrumb:** `Home › New Construction › D.R. Horton`

**H1: D.R. Horton Homes in Las Vegas**
> Hero. Sub-line `18 active communities · D.R. Horton`. Three buttons: `Tour with NREG` (#lead-form), `Call (702) 637-1759`, `All Builders` (/new-construction/). Badge: `⚠️ Critical · Read Before Visiting`.

**H2: Visiting D.R. Horton? Your timing decides who represents you.**
> The conversion engine of the page, placed above everything else. A two-column ✗/✓ comparison of registering with the agent before touring the model home.

> **H3: Walk in alone** — ✗ column, 5 bullets: "D.R. Horton's sales agent represents them, not you"; "No one reviews the contract on your behalf"; "You pay full price on lot premiums & upgrades"; "D.R. Horton keeps the commission they would've paid your agent"; "Forfeit representation on that home — permanently".

> **H3: Register with NREG first** — ✓ column, 4 bullets: "Independent buyer-agent on your side"; "Contract reviewed before you sign anything"; "We negotiate incentives, lot premiums, upgrades"; "$0 cost to you — D.R. Horton pays our commission". Trust strip: "30-second registration · No spam · No pressure · Special Offers! Up to $50K Savings!". Closing line: "Bottom line: Register before your first D.R. Horton visit. It's free, fast, and the only way to keep representation." Buttons `REGISTER FREE NOW` + `CALL (702) 637-1759`. Eyebrow for next section: `Active Communities`.

**H2: D.R. Horton Communities in Las Vegas (18)**
> Community grid, grouped by city, cities ordered by descending count. Each card = community name + price range, linking to a root-level community page.

> **H3: North Las Vegas 10 communities** — Aliante Corridor $300K–$500K; Aurora Heights $336K–$425K; Craig Road Corridor $300K–$500K; El Dorado Springs $300K–$500K; Eldorado $300K–$500K; Heartland at Tule Springs $350K–$550K; Meadowbrook $385K–$515K; North Las Vegas $250K–$600K; North Valley $300K–$500K; Tule Springs $300K–$500K.

> **H3: Henderson 5 communities** — Cadence $350K–$800K; Heartland $335K–$495K; Horizon Ridge Corridor $400K–$800K; Saint Rose Parkway Corridor $350K–$800K; Villas at Seven Hills (Seven Hills) $450K–$750K.

> **H3: Las Vegas 3 communities** — Centennial Hills $350K–$700K; Centennial Springs $400K–$650K; Garden at Centennial Hills (Centennial Hills) $400K–$650K. Eyebrow for next: `Builder Profile`.

**H2: About D.R. Horton in Las Vegas**
> ~300 words of genuine builder narrative. Opens with corporate credentials ("D.R. Horton, Inc. (NYSE: DHI) has been the nation's largest homebuilder by volume for over two decades, delivering more than 90,000 homes per year across 33 states"), then the sub-brand strategy (Express Homes, low $300,000s), then geographic concentration by corridor, then named community series. Specific, checkable, non-generic.

> **H3: Get Builder Incentives & Floor Plans** — the `#lead-form` section. Copy: "We'll send you the latest 2026 builder incentives, floor plans, and price sheets for communities matching your criteria. Free, no obligation." Fields per §1.7. Notes textarea pre-filled `I'm interested in D.R. Horton new construction homes.` Consent line naming the brokerage + Terms/Privacy links.

**H2: Frequently Asked Questions About D.R. Horton** (`#faq`)
> 6 questions, answers always visible (no accordion), mirrored exactly into FAQPage JSON-LD.

> **H3: What is D.R. Horton's price range in Las Vegas?** — "$308,000 (Express Homes/entry-level in North Las Vegas) to $822,000 (Symmetry Summit at Cadence in Henderson)."
> **H3: What is Express Homes by D.R. Horton?** — entry-level sub-brand, simplified plans, included appliances, concentrated in North Las Vegas.
> **H3: Where does D.R. Horton build in Las Vegas?** — names actual communities per corridor (Heartland at Tule Springs, Kalea Bay, Valley Vista, Sky Falls, Juno Pointe / Symmetry at Cadence / Cambria Bay, Tempo Trails).
> **H3: What warranty does D.R. Horton offer?** — 10-year structural / 2-year systems / 1-year workmanship, cites "Nevada's NRS 116B minimums."
> **H3: Does D.R. Horton offer builder incentives?** — closing cost credits $15,000–$35,000, rate buydowns via DHI Mortgage, appliance upgrades.
> **H3: Should I use a buyer's agent when buying from D.R. Horton?** — the conversion FAQ, present on all 18. "The builder pays the agent's commission — it costs you nothing." Eyebrow for next: `Read Next`.

**H2: D.R. Horton and new-construction articles**
> 3 blog cards, each with a `buying tips` category chip, title, and a ~120-char truncated excerpt ending in `…`.

> **H3: D.R. Horton Plan 2538 Heartland Manor North Las Vegas 2026**
> **H3: D.R. Horton Plan 2660 at Symmetry Falls Cadence 2026**
> **H3: New Construction Homes in North Las Vegas: 2026 Guide**
> Then `See all blog posts →` → `/blog/`.

**H2: Other Las Vegas builders**
> Flat chip grid, all 18 builders including D.R. Horton itself. No images, just text links.

**H2: Related Reading**
> 3 evergreen blog links + `All Las Vegas New Construction Communities` → `/new-construction/`. Then the **Trademark & Affiliation Notice**: "Nevada Real Estate Group is an independent licensed Nevada real estate brokerage (License S.181401) and is not affiliated with, endorsed by, or sponsored by D.R. Horton or any of its parents, subsidiaries, or affiliates. D.R. Horton and all related names, logos, product and service names, designs, and slogans are trademarks of D.R. Horton or its respective owners. Use of these marks on this page is for [nominative/identification purposes]…" with a `verify at red.nv.gov` link. **This is the legal shield for ranking on a competitor's trademark — copy this pattern.**

**H2: Find D.R. Horton Homes in Las Vegas**
> Final CTA band: "Nevada Real Estate Group works with every major builder in Las Vegas. Get expert guidance on floor plans, incentives, upgrades, and contract negotiation." Buttons `Call (702) 637-1759` + `Email Us`.

---

## 5. Schema / JSON-LD

**Exactly 5 blocks on every one of the 18 pages, same order, same types, no exceptions:**

| # | `@type` | Notes |
|---|---|---|
| 1 | `BreadcrumbList` | 3 items: Home → New Construction → {Builder}. ~419 bytes. |
| 2 | `Article` | `headline`, `description`, `image` (og jpg), `datePublished`/`dateModified` **both `2026-05-02` on all 18**, `author` = Person "Chris Nevada" (`/about`), `publisher` = Organization NREG + logo, `mainEntityOfPage`. ~754 bytes. |
| 3 | `ItemList` | `name` = "{Builder} Communities in Las Vegas", `numberOfItems` = community count, `itemListElement` = ListItem[] with `position`, `name`, `url` (absolute, **no trailing slash**). Sizes 1–60. |
| 4 | `FAQPage` | `speakable` present (voice-search optimization), `mainEntity` = 6 Question objects (5 for tri-pointe and woodside) with `acceptedAnswer.text`. 1:1 with the visible H3 FAQ block. ~2,650 bytes. |
| 5 | `RealEstateAgent` | `@id` = `https://www.nevadarealestategroup.com/#realestateagent` (sitewide node, repeated on every page). Includes `name`, `url`, `logo`, `image`, `telephone +17026371759`, `email info@NevadaGroup.com`, `priceRange "$$"`, `address` (8945 W Russell Rd Suite 170, Las Vegas NV 89148), `geo` (36.0879, -115.2952), `hasMap`, `openingHoursSpecification` (Mon–Sun 08:00–20:00), `areaServed` = 3 City nodes (Las Vegas, Henderson, North Las Vegas), `hasCredential` (Real Estate License), `aggregateRating`. |

**Notably absent:** no `Product`, no `Offer`, no `Place`/`Residence`, no `LocalBusiness` beyond RealEstateAgent, no `HowTo`, no `VideoObject`. No `Organization` for the builder itself (deliberate — avoids implying affiliation).

**Head meta (dr-horton, representative):**
```html
<link rel="canonical" href="https://www.nevadarealestategroup.com/builders/dr-horton/"/>
<meta name="robots" content="index, follow"/>
<meta property="og:type" content="article"/>
<meta property="og:image" content="https://www.nevadarealestategroup.com/og/builders/dr-horton.jpg"/>  <!-- 1200x630, per-builder -->
<meta name="twitter:card" content="summary_large_image"/>
```
Full OG + Twitter card set including `og:image:alt`, `twitter:image:width/height`. Per-builder OG images at the predictable path `/og/builders/{slug}.jpg`.

---

## 6. Reusable Patterns Worth Stealing

**Strong — copy these:**

1. **The "Visiting {Builder}? Your timing decides who represents you." section above the fold.** This is the single best idea on the page. It weaponizes the builder-registration rule into the lead magnet, and it is the *first* H2 — before communities, before the builder profile. Two-column ✗/✓ with "Forfeit representation on that home — permanently" is the fear hook, "$0 cost to you — the builder pays our commission" is the objection killer.

2. **Trademark & Affiliation Notice.** Explicit disclaimer + license number + `red.nv.gov` verification link. This is what makes ranking on "D.R. Horton Las Vegas" defensible. Non-optional if Rose Homes LV builds this.

3. **Price range baked into every community link's anchor text** (`Cadence$350K–$800K`). Free long-tail relevance and it makes the grid scannable without a table.

4. **City-grouped community grid, sorted by descending count**, with correct singular/plural. Cheap to template, reads as authoritative.

5. **Per-builder OG image at `/og/builders/{slug}.jpg`.** Predictable, scriptable.

6. **FAQPage with `speakable`** and answers rendered as plain visible divs, not `<details>` accordions. Better for AI-overview and featured-snippet extraction.

7. **Hidden `builder` field + pre-filled `notes` textarea** on the lead form, so every lead arrives attributed to a builder with intent captured.

8. **Fully-connected builder mesh + shared community pages.** 18 pages × 18 links = 324 internal builder links from one cluster, and 198 community pages get link equity. Trivially cheap PageRank sculpting.

9. **One model/plan-specific blog per builder** (e.g. "D.R. Horton Plan 2538 Heartland Manor") feeding the section-5 card grid. Highly specific long-tail with almost no competition.

10. **Comparison FAQ across builders** — touchstone has "How does Touchstone compare to LGI Homes?", and there is a 3-builder comparison blog (`christopher-homes-blue-heron-toll-brothers-summerlin-comparison-2026`). Cross-builder comparison is a content vein they've only lightly mined.

**Gaps — where Rose Homes LV can beat them:**

- **No comparison tables at all.** Zero `<table>` elements. A real builder-vs-builder spec table (warranty terms, included features, incentive type, design-studio model, build time) would be a genuine differentiator and a snippet magnet.
- **No floor plan section.** Plans are only mentioned in prose and in one blog per builder. No plan grid, no sq-ft/bed/bath data, no plan schema.
- **No incentive table.** Incentives are prose inside one FAQ ("$15,000-$35,000 closing cost credits, DHI Mortgage buydowns"). A dated, per-builder incentive table would out-rank this and give a reason to re-crawl.
- **No IDX feed on spokes.** Live "homes available now from {Builder}" would add freshness the static pages lack.
- **No sticky TOC on spokes**, so 1,700-word pages have no in-page navigation and no jump-link sitelinks in SERPs.
- **`datePublished` = `dateModified` = 2026-05-02 on all 18.** Never updated since launch. Freshness is an easy win.
- **8 of 18 builders have no exclusive blog** (lennar, toll-brothers, woodside, beazer, century-communities, lgi, shea, storybook) — those run 3 generic fillers.
- Minor: JSON-LD breadcrumb/ItemList URLs omit the trailing slash while HTML hrefs include it.

---

## 7. Raw Artifacts

HTML snapshots (18 builder pages + `/builders/` index) and the parser used:
`/private/tmp/claude-501/-Users-ryanrose-Downloads-Claude/6477daa7-6c35-4157-844e-8990af0dce0e/scratchpad/builders/*.html`
`/private/tmp/claude-501/-Users-ryanrose-Downloads-Claude/6477daa7-6c35-4157-844e-8990af0dce0e/scratchpad/parse.py`
(Scratchpad is session-scoped; re-fetch with the curl UA in the task brief if needed.)
