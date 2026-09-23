# NRG Research 03 — Geo Sub-Hubs (`/<city>/new-construction/`)

Reverse-engineering of nevadarealestategroup.com's second-tier new-construction pages.
Captured 2026-07-25. Raw HTML in scratchpad `.../scratchpad/nrg/agentC/`.

---

## 0. Discovery — the FULL new-construction URL list

Source: `https://www.nevadarealestategroup.com/sitemap.xml` (single flat sitemap, **no child sitemaps**, 2,823 URLs, `lastmod` all stamped at build time). Confirmed via `robots.txt` which declares exactly one `Sitemap:` line.

### Tier 1 — master hubs (2)

| URL | Region |
|---|---|
| `/new-construction/` | Southern Nevada / Las Vegas metro |
| `/reno-new-construction/` | Northern Nevada / Reno |

Note the naming inconsistency: the Reno master is a **flat** slug (`/reno-new-construction/`), not `/reno/new-construction/`. `/reno/new-construction/` returns **404**.

### Tier 2 — geo sub-hubs, `ncc-` template (8)

Southern Nevada (children of `/new-construction/`):

| URL | Status |
|---|---|
| `/henderson/new-construction/` | 200 |
| `/summerlin/new-construction/` | 200 |
| `/north-las-vegas/new-construction/` | 200 |
| `/centennial-hills/new-construction/` | 200 |
| `/enterprise/new-construction/` | 200 |

Northern Nevada (children of `/reno-new-construction/`):

| URL | Status |
|---|---|
| `/sparks/new-construction/` | 200 |
| `/dayton/new-construction/` | 200 |
| `/fernley/new-construction/` | 200 |

### Tier 2b — outlier

| URL | Status | Note |
|---|---|---|
| `/pahrump/new-construction-homes/` | 200 | **Different template.** Not `ncc-`. This is their generic community/IDX-filter page ("What Do Pahrump Neighborhood Stats Show?", "How Do You Get New New Construction Homes in Pahrump Emailed Daily?" — note the duplicated "New New" bug). Different slug too (`new-construction-homes` not `new-construction`). |

### Confirmed 404s (do NOT exist — every one I probed)

`/las-vegas/new-construction/` · `/boulder-city/new-construction/` · `/spring-valley/new-construction/` · `/skye-canyon/new-construction/` · `/southwest-las-vegas/new-construction/` · `/lake-las-vegas/new-construction/` · `/inspirada/new-construction/` · `/cadence/new-construction/` · `/mountains-edge/new-construction/` · `/green-valley/new-construction/` · `/the-lakes/new-construction/` · `/anthem/new-construction/` · `/seven-hills/new-construction/` · `/reno/new-construction/` · `/pahrump/new-construction/` · `/silverado-ranch/new-construction/` · `/aliante/new-construction/` · `/providence/new-construction/` · `/tule-springs/new-construction/` · `/blue-diamond/new-construction/`

**Takeaway:** the geo tier stops at **city / census-place level**. Sub-communities (Lake Las Vegas, Inspirada, Cadence, Skye Canyon) get a *community* page (`/henderson/cadence/`), not a new-construction sub-hub. Boulder City and Lake Las Vegas only get an **anchor section on the master hub** (`#boulder-city`, `#lake-las-vegas`), not their own page.

### Tier 3 — builder pages (18 live, `/builders/<slug>/`)

`beazer` · `blue-heron` · `century-communities` · `christopher` · `dr-horton` · `harmony` · `kb-home` · `lennar` · `lgi` · `pulte-del-webb` · `richmond-american` · `shea` · `storybook` · `taylor-morrison` · `toll-brothers` · `touchstone` · `tri-pointe` · `woodside`

Sitemap also contains 3 **broken/duplicate** builder URLs not in the canonical 18: `/builders/woodside-homes/`, `/builders/pardee/`, plus duplicate `/builders/toll-brothers/` entries. Worth verifying before copying their model.

### New-construction blog cluster (20 posts, `/blog/<slug>/`)

`new-construction-homes-north-las-vegas-guide-2026` · `new-construction-homes-sparks-builders-guide-2026` · `new-construction-homes-henderson-builders-guide-2026` · `new-construction-homes-reno-builders-guide-2026` · `southwest-las-vegas-new-construction-homes-town-square-2026` · `do-you-need-realtor-new-construction-las-vegas-2026` · `sid-lid-taxes-las-vegas-new-construction-2026` · `new-construction-vs-resale-las-vegas-2026-comparison` · `where-to-buy-new-construction-las-vegas-2026-tier-ranking` · `2-1-buydown-las-vegas-new-construction-2026` · `california-to-las-vegas-new-construction-savings-2026` · `clark-county-property-tax-reassessment-new-construction-2026` · `design-center-budget-las-vegas-new-construction-2026` · `first-time-buyer-new-construction-mistakes-las-vegas-2026` · `hoa-landscape-requirements-new-construction-las-vegas-2026` · `inspirada-final-75-homes-south-henderson-new-construction-2026` · `lot-premium-negotiation-las-vegas-new-construction-2026` · `new-construction-resale-las-vegas-decision-matrix-2026` · `new-construction-timeline-las-vegas-build-reality-2026` · `pre-drywall-inspection-new-construction-las-vegas-2026`

Plus builder-adjacent: `las-vegas-home-builders-compared-2026` · `top-luxury-home-builders-las-vegas-2026` · `builder-closing-cost-credits-las-vegas-2026` · `builder-contract-clauses-negotiate-las-vegas-2026` · `las-vegas-homebuilder-sales` · `10-tips-to-buying-a-new-construction-home` · `new-construction-incentives-las-vegas-may-2026-builder-roundup` · `best-real-estate-agent-for-new-construction-in-las-vegas-...`

> **robots.txt note worth stealing:** NRG explicitly **Allows** GPTBot, ClaudeBot, PerplexityBot, Google-Extended, Applebot-Extended, CCBot, Bytespider, Meta-ExternalAgent etc. (AI-crawler opt-in), while **Disallowing** `/*/new-construction` and `/new-construction` for AhrefsBot / AhrefsSiteAudit / SemrushBot / SiteAuditBot only — an MLS-quota firewall, not an SEO signal.

---

## 1. The shared sub-hub TEMPLATE

CSS namespace is `ncc-*` (the master hub uses `nc-*` — genuinely two different components). Deep-dived `/henderson/new-construction/` and `/summerlin/new-construction/`; template is byte-identical in structure across all 8.

### Exact section order

```
<section class="ncc-hero">                     ← full-bleed image, no id
    <img class="ncc-hero__img">                ← Next.js <Image fill>, /images/homepage/comm-<city>.jpg
    <div class="ncc-hero__scrim">              ← linear-gradient(180deg, rgba(15,23,42,.25), rgba(15,23,42,.78))
    <div class="container ncc-hero__inner">
        <nav aria-label="Breadcrumb" class="ncc-crumb">   Home › Henderson › New Construction
        <span class="ncc-eyebrow">New Construction Homes</span>
        <h1>New Construction Homes in Henderson, NV</h1>
        <div class="ncc-hero__stats">          ← 3 mono-font stat blocks
        <div class="ncc-hero__actions">        ← 2 buttons
        <p class="ncc-byline">Last reviewed June 28, 2026 · By Chris Nevada · Nevada Real Estate Group

<div class="container ncc-body">
    <blockquote class="direct-answer" aria-label="Direct Answer">   ← 1 paragraph, ~60-90 words
    <ul class="key-takeaways">                                      ← 5-6 checkmark bullets

<section id="listings" class="ncc-section">    ← THE ONLY ANCHOR ID ON THE PAGE
    <h2> What New-Construction Homes Are for Sale in {City} Right Now?
    [IDX grid — listing cards, id="listing-card-<MLS#>"]

<section class="ncc-section">   <h2> Which Builders Are Building New Homes in {City}?
                                <table class="ncc-table">   ← Builder / Tier / Communities / Price range
<section class="ncc-section">   <h2> What Are the Best New-Home Communities in {City}?
                                <table class="ncc-table">   ← Community / Builders / From / Status
<section class="ncc-section">   <h2> What Builder Incentives Are Available in {City} in 2026?
<section class="ncc-section">   <h2> Why Buy New Construction in {City}?
<section class="ncc-section ncc-agent">
                                <h2> Do You Need a Realtor to Buy New Construction in {City}?
<section class="ncc-section">   <h2> [LOCALIZED WILDCARD — see below]        ← optional, present on 3 of 5
<section class="ncc-section">   <h2> Frequently Asked Questions
<section class="ncc-section">   <h2> New Construction Guides for {City} Buyers   ← 6 blog/hub links
<section class="ncc-section ncc-cross">        ← "Explore more {City} real estate" (3-4 links)
<section class="ncc-section ncc-cross">        ← 3-column: Browse new construction / {City} real estate / Compare nearby
<section class="ncc-section ncc-related">      ← 4 inline pills, first is "← All Southern Nevada New Construction"
<section class="ncc-section ncc-cta">
    <h2> Ready to Tour New Homes in {City}?
    <form class="ccm__form" action="/api/leads/buyer/" method="POST">
    <aside class="fair-housing-disclosure">
</div>
<section class="footer-cta">   <h2> Ready to make your move?     ← SITEWIDE component, not part of template
```

### Sticky table of contents — **NO**

There is **no TOC on any sub-hub**. Verified three ways:
- No `<nav class="toc">`, no "On This Page" heading, no `<ol class="toc__list">`.
- Zero `position: sticky` declarations in the page's inlined CSS.
- Zero `scroll-mt-*` utilities.
- Only one in-page anchor id exists on the entire document: `id="listings"`. Every other `<section>` is `class="ncc-section"` with **no id**, so the H2s are not linkable.

The only in-page jump link is the hero button `<a href="#listings" class="ncc-btn ncc-btn--gold">Browse New Homes ↓</a>`.

This is a **template gap on NRG's side**, not a deliberate choice — the master hub has a full 18-item TOC and anchor ids on every H2. If Rose Homes LV builds this, add anchor ids + a sticky TOC to the sub-hub and you immediately beat them on sitelinks / AI-answer citability.

### IDX embed — placement and filtering

- **Placement:** section 1, immediately under the hero + direct answer. `<section id="listings">`. This is the very first content block.
- **Provider:** Repliers IDX against GLVAR MLS (`cdn.repliers.io/lasvegas/IMG-...`). Cards are server-rendered into the HTML (crawlable), each `id="listing-card-<MLS#>"`, each linking to `/property/<address-slug>-<mlsid>/`.
- **Area-filtered: YES.** Henderson page returns Henderson-city listings; North Las Vegas returns NLV; Centennial Hills and Enterprise return Las Vegas-city listings scoped to their subdivisions (Stone Haven Mello, Redwood Creek / Windmill Village, Custom Build); Summerlin returns Summerlin-area subdivisions (Willowcrest, West Mesa Estate).
- **New-construction-filtered: NO — and this is their biggest flaw.** The Henderson feed's 24 cards break down by year built:

  | Year built | Count |
  |---|---|
  | 2026 | 4 |
  | 2025 | 2 |
  | 2022 | 1 |
  | 1942–1996 | **15 confirmed pre-2000, plus 2 with a null `yearBuilt`** (QA-corrected from 17) |

  A 1942 two-bedroom on Kansas Avenue and a 1953 house on S Water Street are both sitting under an H2 that asks "What New-Construction Homes Are for Sale in Henderson Right Now?". The copy hedges with "new-construction **and recently-built** homes", but the H1/H2/title promise is not met.

  > ### ⚠️ CORRECTED BY QA (`07-qa-verification.md`, C6d) — the original claim here was WRONG.
  >
  > This section previously stated that the **master hub's feed is properly filtered**. It is
  > **not**. QA independently re-checked the hub's 36 rendered cards and found:
  > - **21 of 36 (58%) are Pahrump listings** — not Las Vegas metro at all
  > - **64% are non-metro**
  > - year built ranges back to **1960**, with 7 cards pre-2020
  >
  > The hub still *displays* the methodology copy quoted below, which makes it worse, not
  > better: the page states a filter it does not apply.
  >
  > On-page claim (verbatim, and unmet): *"187 active LV-metro new-construction listings —
  > single-family homes built 2024 or later… Scanned 289 listings across three
  > new-construction signals (yearBuilt ≥ 2025, "new construction", "brand new") and
  > post-filtered against the listing description…"*

  **So the filter is broken sitewide, not just on sub-hubs.** The hub, the sub-hubs and the
  MLS-backed lifestyle pages all leak. This is a bigger competitive opening than originally
  written, and it is the strongest single argument for our build: a correctly filtered feed
  beats them on every new-construction query.

- **Card count is thin and volatile:** Henderson 24, North Las Vegas 14, Centennial Hills 11, Enterprise 10, **Summerlin 2**. The Summerlin hero literally renders "**2** New-build listings" — on the valley's #1 new-construction master plan. They paper over it with a dedicated H2, "Why Do Most Summerlin New Homes Not Show on the MLS?", which is a smart save but confirms the feed is the weak point.
- **No IDX filter UI** on sub-hubs (no price/beds/sort controls) and no "view all" link into `/search`. It is a static server-rendered grid.
- **Schema:** the grid is wrapped in `ItemList` @id `.../new-construction/#listings` with `numberOfItems: 24` and each item as `RealEstateListing` {name, url, image}.

### Tables

Exactly **2** per full-strength sub-hub, both `class="ncc-table"`, both with `<caption>`:

1. **Builder table** — caption "Active new-construction builders in Henderson, 2026." Columns: `Builder | Tier | Communities | Price range`. Builder name cell is a link to `/builders/<slug>/`. 14 rows on Henderson. Tier vocabulary: Entry / Mid / Luxury / Custom.
2. **Community table** — caption "Featured new-construction communities in Henderson, 2026." Columns: `Community | Builders | From | Status`. Community name links to `/henderson/<community>/`. 7 rows on Henderson. Status strings are editorial and specific: "Selling (12,250 at buildout)", "Final phases (~75 homes)", "New — opened 2026 (940 homes)".

Centennial Hills has only **1** table (community only) — hence its hero rendering the bug **"0+ Active builders"**.

### FAQ

7–8 questions per sub-hub. Marked up as **FAQPage JSON-LD** (Question/Answer). In the DOM they render as `<details>`-style Q/A inside the section — note the questions are **NOT** `<h3>` tags (H3 count on every sub-hub is exactly 4, and all four are footer mega-menu labels: "Start Your Search", "Popular Searches", "Buyer Tools", "Relocation & Special Programs"). So the FAQ has zero heading-level semantics on-page; it lives entirely in schema.

### Forms and CTAs

One `<form class="ccm__form" action="/api/leads/buyer/" method="POST">` in the final `ncc-cta` section. Fields:

| Field | id | name | type |
|---|---|---|---|
| honeypot | — | `website` | text, `tabindex="-1"`, off-screen |
| hidden source | `ccm-source` | `source` | hidden |
| First name | `ccm-first` | `firstName` | text, ph "Jane" |
| Last name | `ccm-last` | `lastName` | text, ph "Doe" |
| Email | `ccm-email` | `email` | email, ph "you@email.com" |
| Phone | `ccm-phone` | `phone` | tel, ph "Phone" |
| Timeline | `ccm-timeline` | `timeline` | select |

Timeline options verbatim: `0–3 months — ready to buy` / `3–6 months — actively looking` / `6–12 months — researching` / `12+ months — just exploring` / `I'm selling, not buying`.

CTAs per page (5 total):
1. Hero primary — `<a href="#listings">Browse New Homes ↓</a>` (gold pill)
2. Hero secondary — `<button class="ccta" data-cta-source="henderson-newconstruction-hero">Get Builder Incentives</button>` (ghost pill, opens modal)
3. Inline phone CTA in the listings lede and in the agent section — `(702) 637-1759`
4. Final CTA — "Talk to a New-Construction Specialist →", `data-cta-source="henderson-newconstruction-cta"`
5. `tel:+17026371759` links in the CTA block and licence footer

**Per-page CTA source attribution** (`{city}-newconstruction-hero` / `{city}-newconstruction-cta`) is worth copying — it makes lead attribution per sub-hub trivial.

### Image usage

- **1 editorial image per page**: the hero, served through `/_next/image/`, `sizes="100vw"`, srcSet 640→1920. Paths: `/images/homepage/comm-henderson.jpg`, `comm-summerlin.jpg`, `comm-north-las-vegas.jpg`, `/images/communities/centennial-hills/centennial-hills-hero.jpg`, `/images/communities/enterprise/enterprise-hero.jpg`. Alt text is descriptive and localized: *"New construction homes in Henderson, Nevada with Black Mountain and master-planned neighborhoods"*.
- **Every other image on the page is an IDX listing photo.** Total `<img>` count tracks card count exactly: Henderson 28, NLV 18, Centennial Hills 15, Enterprise 14, Summerlin 6.
- **No** builder logos, **no** community photos, **no** floor-plan renderings, **no** maps, **no** icons-as-images. That is a soft target — a Rose Homes LV version with real community photography and builder logos would look substantially richer for near-zero extra effort.

### Word count

Body word counts (full document text, scripts/styles stripped — includes nav/footer chrome, so treat as an upper bound; editorial body is roughly 1,400–1,900 words on the LV pages):
Henderson 4,443 · North Las Vegas 3,912 · Enterprise 3,263 · Centennial Hills 3,214 · Summerlin 3,139 · Sparks 2,946 · Dayton 2,829 · Fernley 2,627. Master hub 11,221.

### Schema stack (identical on all 8 sub-hubs)

`WebPage` (with `dateModified`/`datePublished` = 2026-06-28, `primaryImageOfPage`, and a **`SpeakableSpecification`** with `cssSelector: [".direct-answer", ".key-takeaways", ".faq-answer"]`) · `BreadcrumbList` · `RealEstateAgent` (+ `PostalAddress`, `AggregateRating`, `areaServed: City`) · `ItemList` of `RealEstateListing` · `FAQPage` (Question/Answer) · `ImageObject`.

The **`speakable` + `.direct-answer` + `.key-takeaways` combination is the single most copyable idea on the page** — it is an explicit AI-answer-engine play, and it lines up with the AI-crawler opt-ins in robots.txt.

---

## 2. How a sub-hub DIFFERS from the master hub `/new-construction/`

| | Master `/new-construction/` | Sub-hub `/<city>/new-construction/` |
|---|---|---|
| CSS namespace | `nc-*` | `ncc-*` (separate component) |
| Word count | 11,221 | 2,600–4,400 |
| H2 count | 25 | 8–11 |
| Anchor ids on H2s | **Yes, all of them** (`#why-2026`, `#summerlin`, `#henderson`, `#lake-las-vegas`, `#sw-vegas`, `#nlv`, `#nw-vegas`, `#boulder-city`, `#launches-2026`, `#builder-comparison`, `#price-by-submarket`, `#new-vs-resale`, `#step-by-step`, `#incentives`, `#warranties`, `#lot-premiums`, `#faq`, `#builders`, `#lead-form`) | **No** — only `#listings` |
| Sticky TOC | **Yes** — `<nav class="toc" aria-label="Table of contents">`, `<h2 class="toc__title">On This Page</h2>`, `<ol class="toc__list">`, 18 items | **No** |
| Hero | Text hero, no image, `73+ active communities · 18 builders · $290K–$10M · ~25 min read` | Full-bleed photo hero + scrim + 3 mono stat blocks + eyebrow + byline |
| Read-time estimate | Yes ("~25 min read") | No |
| Breadcrumb | 2 levels (Home › New Construction) | 3 levels (Home › {City} › New Construction) |
| IDX feed | Metro-wide, **properly filtered** (yearBuilt ≥ 2025 + "new construction" + "brand new", description post-filter), 187 results, methodology disclosed, 36 cards rendered | City-scoped, **NOT year-filtered**, 2–24 cards, no methodology line |
| Tables | 5 `nc-table` — 2025-26 launches, national vs regional builders, price by submarket, new vs resale, incentives | 2 `ncc-table` — builders, communities |
| FAQ | 12 questions, rendered as real `<h3>` tags, `<section id="faq">` | 7–8 questions, schema-only (no headings) |
| Forms | 2 (`#lead-form` `nc-lead-form` + sitewide footer) | 1 (`ccm__form` in `ncc-cta`) + sitewide footer |
| Images | 66 | 6–28 (1 editorial + IDX) |
| Blog feed | Yes — auto "New construction articles" feed with 3 cards, category eyebrows | No — hand-curated 6-link "New Construction Guides for {City} Buyers" list |
| Direct answer / key takeaways | Has `.direct-answer-block` | Has `blockquote.direct-answer` + `ul.key-takeaways` |

### What the sub-hub ADDS that the master does not have

1. **Photo hero + scrim + stat trio** (`14+ Active builders / 28 New-build listings / 7+ Featured communities`) — the listings number is live from the feed.
2. **3-level breadcrumb + `BreadcrumbList` schema.**
3. **`ncc-cross` / `ncc-related` link clusters** — three named columns of sideways links plus a pill row. The master has none of this.
4. **A dedicated "Do You Need a Realtor to Buy New Construction in {City}?" section** (`ncc-agent`) with the registration ask. On the master this is buried as one FAQ item.
5. **A localized wildcard H2** — a section that exists only where the local story warrants it (see §6).
6. **Per-page CTA source attribution** (`data-cta-source="{city}-newconstruction-hero"`).
7. **`.key-takeaways` checkmark list.**

### What the sub-hub DROPS

TOC, all anchor ids, the price-by-submarket table, the new-vs-resale table, the step-by-step buying process section, the warranties section, the lot-premiums section, the 2025-26 launches table, the national-vs-regional builder comparison, the auto blog feed, the read-time estimate, and the second lead form. Every one of those is a **generic, non-localizable** asset — the split is clean and deliberate: **evergreen education lives on the master, local inventory lives on the sub-hub.**

### How the copy is localized

Not templated string-substitution — it is genuinely rewritten. Evidence:
- H2 phrasing changes shape, not just the noun. Enterprise's H1 is "New Construction Homes in **Enterprise & Southwest Las Vegas**" (dual-targeting the informal name), and its FAQ asks about "Enterprise / SW Las Vegas".
- The intro paragraphs carry specific, checkable local facts: Cadence's 12,250-home buildout, Lake Las Vegas going "from ~6 to 19 active communities", Inspirada's "~75 new homes remaining", KB Home's Meriden at Whitney Ranch "940 homes", Summerlin's villages named individually (Stonebridge, Redpoint, Kestrel, The Cliffs, Reverence).
- Price ranges are per-market: Henderson "mid-$300,000s to $15M-plus", Summerlin "low $500,000s to $2.4M-plus", North Las Vegas "from the $300s", Centennial Hills "from the $400s", Enterprise "$400s to $1M+ guard-gated".
- Schools are named locally (Henderson: "Coronado, Foothill, Green Valley").
- The **incentive numbers are shared** across pages though — "$10,000–$45,000 closing-cost credits", "$15,000–$75,000 design-center allowances", "$150–$350/month on a $600,000 purchase" repeat verbatim. That is the one place the template shows.
- Meta title formula: `{City} New Construction Homes | {2-3 word differentiator}` — "| Builders & Incentives", "| Builders & Villages", "| Builders", "| Skye Canyon & More". Meta description formula: `Browse new construction homes in {City}, NV — {3-4 named communities}. {price anchor}. 2026 incentives...`

---

## 3. Per-page inventory

| URL | Status | H1 | Meta title | Meta description | Words | # H2 | TOC | IDX | # FAQ | # Tables |
|---|---|---|---|---|---|---|---|---|---|---|
| `/new-construction/` *(master)* | 200 | New Construction Homes in Las Vegas | New Construction Homes Las Vegas \| 18 Builders | Browse 73+ new construction communities in Summerlin, Henderson, SW Vegas & more. 18 active builders, $290K–$10M. Builder incentives + floor plans. | 11,221 | 25 | **Yes (18 items)** | Yes (36 cards, filtered) | 12 | 5 |
| `/henderson/new-construction/` | 200 | New Construction Homes in Henderson, NV | Henderson New Construction Homes \| Builders & Incentives | Browse new construction homes in Henderson, NV — Cadence, Inspirada, Lake Las Vegas & MacDonald Highlands. 2026 builder incentives, floor plans, and quick move-in homes. | 4,443 | 11 | No | Yes (24 cards) | 8 | 2 |
| `/summerlin/new-construction/` | 200 | New Construction Homes in Summerlin, NV | Summerlin New Construction Homes \| Builders & Villages | Browse new construction homes in Summerlin — Stonebridge, Redpoint, Kestrel, The Cliffs & Reverence. 8 builders, from the $500s to $2.4M+. 2026 incentives and quick move-in homes. | 3,139 | 11 | No | Yes (**2 cards**) | 8 | 2 |
| `/north-las-vegas/new-construction/` | 200 | New Construction Homes in North Las Vegas, NV | North Las Vegas New Construction Homes \| Builders | Browse new construction homes in North Las Vegas, NV — Villages at Tule Springs, Aliante, Park Highlands & Valley Vista. The valley's most affordable new homes from the $300s. | 3,912 | 11 | No | Yes (14 cards) | 8 | 2 |
| `/centennial-hills/new-construction/` | 200 | New Construction Homes in Centennial Hills, NV | Centennial Hills New Construction \| Skye Canyon & More | Browse new construction homes in Centennial Hills, NW Las Vegas — Skye Canyon, Providence & the Tule Springs frontier. Mountain-view new homes from the $400s. 2026 incentives. | 3,214 | 9 | No | Yes (11 cards) | 7 | **1** |
| `/enterprise/new-construction/` | 200 | New Construction Homes in Enterprise & Southwest Las Vegas | Enterprise & SW Las Vegas New Construction Homes | Browse new construction homes in Enterprise & southwest Las Vegas — Mountain's Edge, Southern Highlands & the SW valley. From the $400s to $1M+ guard-gated. 2026 incentives. | 3,263 | 10 | No | Yes (10 cards) | 7 | 2 |
| `/reno-new-construction/` *(N. NV master)* | 200 | New Construction Homes in Reno & Northern Nevada | New Construction Homes Reno & Northern Nevada \| Builders | Browse new construction communities across Reno, Sparks, Carson Valley, Fernley & Lake Tahoe. National + regional builders, $400K–$5M. Builder incentives + floor plans. | 7,796 | 21 | **Yes** | Yes (24 cards) | 9 | 4 |
| `/sparks/new-construction/` | 200 | New Construction Homes in Sparks, NV | Sparks New Construction Homes \| Kiley Ranch & More | Browse new construction homes in Sparks, NV — Kiley Ranch, Wingfield Springs, D'Andrea & Stonebrook. Value new homes near the Tahoe-Reno Industrial Center. No state income tax. | 2,946 | 9 | No | Yes (8 cards) | 8 | 1 |
| `/dayton/new-construction/` | 200 | New Construction Homes in Dayton, NV | Dayton NV New Construction Homes \| Dayton Valley | Browse new construction homes in Dayton, NV — Dayton Valley and the Carson River corridor. Value new homes between Carson City and Reno. No state income tax. | 2,829 | 8 | No | Yes (11 cards) | 6 | 1 |
| `/fernley/new-construction/` | 200 | New Construction Homes in Fernley, NV | Fernley NV New Construction Homes \| Builders | Browse new construction homes in Fernley, NV — affordable newer tract homes in fast-growing Lyon County, minutes from the Tahoe-Reno Industrial Center. No state income tax. | 2,627 | 8 | No | Yes (8 cards) | 6 | 1 |
| `/pahrump/new-construction-homes/` *(outlier template)* | 200 | New Construction Homes in Pahrump | New Construction Homes in Pahrump NV \| Live MLS | Browse new construction homes in Pahrump NV — live MLS listings built 2024 or newer, from Mountain Falls builder homes to custom builds on acreage. | 2,795 | 7 | No | Yes (6 cards) | 6 | **0** |
| `/las-vegas/new-construction/` | **404** | — | — | — | — | — | — | — | — | — |
| `/boulder-city/new-construction/` | **404** | — | — | — | — | — | — | — | — | — |
| `/lake-las-vegas/new-construction/` | **404** | — | — | — | — | — | — | — | — | — |
| `/spring-valley/`, `/skye-canyon/`, `/southwest-las-vegas/`, `/inspirada/`, `/cadence/`, `/mountains-edge/`, `/green-valley/`, `/the-lakes/`, `/anthem/`, `/seven-hills/`, `/silverado-ranch/`, `/aliante/`, `/providence/`, `/tule-springs/`, `/blue-diamond/` + `/new-construction/` | **404** | — | — | — | — | — | — | — | — | — |

---

## 4. Link graph (real anchor text)

### UP — sub-hub → master

Three separate up-links per page, all pointing at `/new-construction/`:
1. In the "New Construction Guides for {City} Buyers" list: **"Do You Need an Agent for New Construction?"** → `/new-construction/` *(note: the anchor text does not match the destination's own H1 — it is a topical anchor, not a navigational one)*
2. In `ncc-cross` column 1 ("Browse new construction"): **"All Southern Nevada New Construction"** → `/new-construction/`
3. In `ncc-related` pill row, first pill: **"← All Southern Nevada New Construction"** → `/new-construction/`

Plus 4 more from the sitewide top nav (**"New Construction"**) and 3 from the footer.

### DOWN — master → sub-hubs

The master hub has a dedicated `<h2>New Construction by City</h2>` block containing exactly 5 links, anchor text = bare city name:

| Href | Anchor |
|---|---|
| `/henderson/new-construction/` | Henderson |
| `/summerlin/new-construction/` | Summerlin |
| `/north-las-vegas/new-construction/` | North Las Vegas |
| `/centennial-hills/new-construction/` | Centennial Hills |
| `/enterprise/new-construction/` | Enterprise / SW Las Vegas |

`/reno-new-construction/` has the parallel block → `/sparks/new-construction/` (Sparks), `/dayton/new-construction/` (Dayton), `/fernley/new-construction/` (Fernley).

### SITEWIDE FOOTER — the real link-equity engine

Every page on the site (verified on `/henderson/new-construction/` and `/henderson/`) carries a footer column with:

- **"New Construction (all So. NV)"** → `/new-construction/`
- **"Henderson new construction"** → `/henderson/new-construction/`
- **"Summerlin new construction"** → `/summerlin/new-construction/`
- **"North Las Vegas new construction"** → `/north-las-vegas/new-construction/`
- **"Centennial Hills new construction"** → `/centennial-hills/new-construction/`
- **"Enterprise / SW new construction"** → `/enterprise/new-construction/`

Plus **"New Construction Communities"**, **"Las Vegas Home Builders"**, **"New construction"** all → `/new-construction/`.

So all 5 sub-hubs get a sitewide footer link from ~2,800 pages. That is how a 3,000-word page ranks.

### DOWN — sub-hub → builder pages

Two routes:
1. **Every builder-table row's name cell is a link.** Henderson: `/builders/lennar/` (Lennar) · `/builders/kb-home/` (KB Home) · `/builders/pulte-del-webb/` (Pulte / Del Webb) · `/builders/toll-brothers/` (Toll Brothers) · `/builders/dr-horton/` (D.R. Horton) · `/builders/beazer/` (Beazer Homes) · `/builders/tri-pointe/` (Tri Pointe Homes) · `/builders/richmond-american/` (Richmond American) · `/builders/taylor-morrison/` (Taylor Morrison) · `/builders/century-communities/` (Century Communities) · `/builders/blue-heron/` (Blue Heron) · `/builders/woodside/` (Woodside Homes) · `/builders/storybook/` (StoryBook Homes) · `/builders/christopher/` (Christopher Homes).
2. **The "Browse new construction" cross column repeats 2–3 of them** — a hand-picked, per-city selection:
   - Henderson: "Lennar Homes", "Toll Brothers", "KB Home"
   - Summerlin: "Toll Brothers", "Pulte / Del Webb", "Richmond American"
   - North Las Vegas: "D.R. Horton", "KB Home", "Century Communities"
   - Enterprise: "D.R. Horton", "Toll Brothers"
   - Centennial Hills: "Lennar" *(only one — because it has no builder table)*

### DOWN — sub-hub → community pages

Via the community-table name cells, e.g. Henderson: `/henderson/cadence/` (Cadence) · `/henderson/lake-las-vegas/` (Lake Las Vegas) · `/henderson/inspirada/` (Inspirada) · `/henderson/whitney-ranch/` ("Whitney Ranch — Meriden (KB Home)") · `/henderson/macdonald-highlands/` (MacDonald Highlands) · `/henderson/ascaya/` (Ascaya). "Tuscany" is listed in the table with **no link** — a gap.

And via the third cross column: "Lake Las Vegas" → `/henderson/lake-las-vegas/`, "The Cliffs" → `/las-vegas/summerlin-the-cliffs/`, "Aliante" → `/north-las-vegas/aliante/`, "Skye Canyon" → `/las-vegas/skye-canyon/`, "Providence" → `/las-vegas/providence/`, "Mountain's Edge" → `/las-vegas/mountains-edge/`, "Southern Highlands" → `/las-vegas/southern-highlands/`.

### SIDEWAYS — sub-hub ↔ sub-hub ("Compare nearby")

Sparse and asymmetric. Henderson does **not** link to any peer sub-hub. The others do:

| From | To |
|---|---|
| Summerlin | **"Henderson New Construction"** → `/henderson/new-construction/`, **"Las Vegas New Construction"** → `/new-construction/` |
| North Las Vegas | **"Henderson New Construction"**, **"Las Vegas New Construction"** |
| Centennial Hills | **"Summerlin New Construction"**, **"Henderson New Construction"** (both inside the "Browse new construction" column) |
| Enterprise | **"Summerlin New Construction"** (in Browse column), **"Henderson New Construction"** (in the pill row) |
| Henderson | **none** |

So Henderson is the hub-of-the-hub — 4 of 5 peers link to it, it links to none of them. Deliberate PageRank sculpting toward their highest-value market.

### SIDEWAYS — sub-hub → geo service pages (`ncc-cross` column 1)

Consistent 3–4 links, anchor text always "{City} {service}":
**"Henderson Homes for Sale"** → `/henderson/homes-for-sale/` · **"Henderson Condos for Sale"** → `/henderson/condos-for-sale/` · **"Henderson 55+ Communities"** → `/henderson/55-plus-communities/` · **"Sell My House in Henderson"** → `/henderson/sell-my-house/`. Same pattern for Summerlin and North Las Vegas. Centennial Hills and Enterprise drop the 55+ link (no such page exists for them).

### OUT — sub-hub → blog

Fixed 6-link set in "New Construction Guides for {City} Buyers", **identical on all 5 LV sub-hubs** (not localized at all):

| Anchor | Href |
|---|---|
| Do You Need an Agent for New Construction? | `/new-construction/` |
| New Construction vs. Resale in Las Vegas | `/blog/las-vegas-new-construction-vs-resale-2026/` |
| Builder Contract Clauses to Negotiate | `/blog/builder-contract-clauses-negotiate-las-vegas-2026/` |
| Builder Closing-Cost Credits Explained | `/blog/builder-closing-cost-credits-las-vegas-2026/` |
| 10 Tips for Buying New Construction | `/blog/10-tips-to-buying-a-new-construction-home/` |
| Design-Center Budget Guide | `/blog/design-center-budget-las-vegas-new-construction-2026/` |

Plus **one contextual in-body blog link** in the localized wildcard section — Henderson: *"see our guide to the [top Henderson communities](/blog/top-5-henderson-communities/)"*, also repeated as the 4th pill (**"Top Henderson Communities"**).

Note the **missed opportunity**: Henderson's page doesn't link `/blog/new-construction-homes-henderson-builders-guide-2026/` or `/blog/inspirada-final-75-homes-south-henderson-new-construction-2026/`, and North Las Vegas doesn't link `/blog/new-construction-homes-north-las-vegas-guide-2026/` — even though both exist. Their blog cluster is under-wired into the geo tier.

### Gap: parent city page does NOT link down to its own sub-hub

`/henderson/` contains a guide card literally captioned **"GUIDE / Henderson New Construction / Active master-planned builds from Lennar, Toll Br..."** — and it links to **`/new-construction/`** (the metro master), not `/henderson/new-construction/`. The only path from `/henderson/` down to `/henderson/new-construction/` is the sitewide footer. Easy win to fix in our build.

---

## 5. Breadcrumbs and URL taxonomy

### The taxonomy

```
/                                   home
├── /new-construction/              TOPIC HUB (metro-wide, Southern NV)
├── /reno-new-construction/         TOPIC HUB (Northern NV) — flat slug, inconsistent
├── /builders/<builder>/            TOPIC LEAF (18 builders)
├── /communities/                   community index
├── /<city>/                        CITY HUB          e.g. /henderson/, /summerlin/, /north-las-vegas/
│   ├── /<city>/new-construction/   CITY × TOPIC  ← the geo sub-hub
│   ├── /<city>/homes-for-sale/     CITY × TOPIC
│   ├── /<city>/condos-for-sale/    CITY × TOPIC
│   ├── /<city>/just-listed/        CITY × TOPIC
│   ├── /<city>/sell-my-house/      CITY × TOPIC
│   ├── /<city>/55-plus-communities/CITY × TOPIC
│   └── /<city>/<community>/        COMMUNITY LEAF   e.g. /henderson/cadence/, /henderson/anthem/
├── /las-vegas/<community>/         COMMUNITY LEAF under the Las Vegas city segment
│                                   e.g. /las-vegas/skye-canyon/, /las-vegas/mountains-edge/,
│                                        /las-vegas/summerlin-the-cliffs/, /las-vegas/enterprise/
├── /<cross-cutting>/               e.g. /guard-gated-communities/, /luxury-communities/,
│                                        /golf-communities/, /55-plus-communities/
├── /blog/<slug>/                   flat blog, no date, no category segment
├── /property/<address-slug>-<mlsid>/  listing detail (noindex, follow)
└── /search                         IDX search (params robots-blocked)
```

**Trailing slash is mandatory** (`trailingSlash: true` in Next.js — confirmed by robots.txt comments referencing `/search/?`). Every canonical ends in `/`.

**The taxonomy is inconsistent in one important place.** Two of the five geo sub-hubs sit under a city segment that **does not resolve as a page**:

| Segment | Bare URL status |
|---|---|
| `/henderson/` | 200 |
| `/summerlin/` | 200 |
| `/north-las-vegas/` | 200 |
| `/centennial-hills/` | **308 → `/las-vegas/centennial-hills/`** |
| `/enterprise/` | **308 → `/las-vegas/enterprise/`** |

So `/centennial-hills/new-construction/` renders a breadcrumb whose middle crumb ("Centennial Hills" → `/centennial-hills/`) is a **redirect**, while its own body cross-links point to the real page at `/las-vegas/centennial-hills/`. Two URLs for the same concept, and the breadcrumb schema names the redirecting one. Sloppy — and easy for us to avoid by picking one city-segment scheme and sticking to it.

Also note `/las-vegas/enterprise/` (community page) and `/enterprise/new-construction/` (sub-hub) coexist under different parents. And `/summerlin/` is a *city*-level segment while Summerlin villages live at `/las-vegas/summerlin-stonebridge/`, `/las-vegas/summerlin-the-ridges/`, `/las-vegas/summerlin-grand-park/`, `/las-vegas/sun-city-summerlin/`, `/las-vegas/summerlin-the-cliffs/` — i.e. Summerlin's own children are NOT under `/summerlin/`.

### Breadcrumb markup

Visual, inside the hero, above the H1:

```html
<nav aria-label="Breadcrumb" class="ncc-crumb">
  <a href="/">Home</a>
  <span aria-hidden="true"> › </span>
  <a href="/henderson/">Henderson</a>
  <span aria-hidden="true"> › </span>
  <span>New Construction</span>
</nav>
```

Current page is a plain `<span>`, not a link — correct. Separators are `aria-hidden`. No `aria-current="page"` though (minor a11y miss). Styled `font-size: 13px; color: rgba(255,255,255,.85)`.

### Breadcrumb schema

Emitted as JSON-LD, absolute URLs, 3 positions:

```json
{
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type":"ListItem","position":1,"name":"Home","item":"https://www.nevadarealestategroup.com/"},
    {"@type":"ListItem","position":2,"name":"Henderson","item":"https://www.nevadarealestategroup.com/henderson/"},
    {"@type":"ListItem","position":3,"name":"New Construction","item":"https://www.nevadarealestategroup.com/henderson/new-construction/"}
  ]
}
```

The master hub uses the 2-position variant (Home › New Construction). The visual crumb on the master is just `<a href="/">` › `New Construction`.

Also present on every sub-hub: `<link rel="canonical">`, `hrefLang="en-US"` **and** `hrefLang="x-default"` both pointing at the same self URL, and OG/Twitter cards using the hero image.

---

## 6. FAQ questions verbatim — localization pattern

### `/henderson/new-construction/` (8)

1. How many new construction homes are for sale in Henderson?
2. What builders are building new homes in Henderson?
3. What are the best new-construction communities in Henderson?
4. Do I need a realtor to buy new construction in Henderson?
5. What builder incentives are available in Henderson in 2026?
6. **Is Inspirada still selling new construction?**
7. How much do new construction homes cost in Henderson?
8. How long does it take to build a new home in Henderson?

### `/summerlin/new-construction/` (8)

1. How many new construction homes are for sale in Summerlin?
2. What builders are building new homes in Summerlin?
3. **What are the newest Summerlin villages for new construction?**
4. How much do new construction homes cost in Summerlin?
5. Do I need a realtor to buy new construction in Summerlin?
6. What builder incentives are available in Summerlin in 2026?
7. **Is Summerlin new construction a good investment?**
8. How long does it take to build a new home in Summerlin?

### The pattern

**Six slots are fixed and templated** — the city name is the only variable:

| # | Template |
|---|---|
| 1 | How many new construction homes are for sale in {City}? |
| 2 | What builders are building new homes in {City}? *(or "What builders are building in {City}?")* |
| 3 | What are the best new-construction communities in {City}? |
| 4 | Do I need a realtor to buy new construction in {City}? |
| 5 | What builder incentives are available in {City} in 2026? |
| 6 | How much do new construction homes cost in {City}? |
| 7 | How long does it take to build a new home in {City}? *(always last)* |

**1–2 slots are a genuinely local question**, targeting a real long-tail query for that market:

| Page | Local question(s) |
|---|---|
| Henderson | *Is Inspirada still selling new construction?* |
| Summerlin | *What are the newest Summerlin villages for new construction?* · *Is Summerlin new construction a good investment?* |
| North Las Vegas | *Why is North Las Vegas new construction cheaper?* · *Can you use FHA or VA loans on North Las Vegas new construction?* |
| Centennial Hills | *Is Centennial Hills cheaper than Summerlin for new construction?* |
| Enterprise | *Is Southern Highlands still building new homes?* |
| Sparks | *Is new construction cheaper in Sparks than Reno?* |
| Dayton | *Is new construction cheaper in Dayton than Carson City or Reno?* |
| Fernley | *Is Fernley good for industrial-corridor workers?* |

The local slot is almost always one of three archetypes: **(a) is community X still selling?**, **(b) is {City} cheaper than {rival city}?**, **(c) a financing/buyer-profile question specific to the market.**

### The same pattern governs the H2 "wildcard" section

Position 7 (between the realtor section and the FAQ) is an optional localized H2:

| Page | Wildcard H2 |
|---|---|
| Henderson | Is 2026 a Good Time to Buy New Construction in Henderson? |
| Summerlin | Why Do Most Summerlin New Homes Not Show on the MLS? |
| North Las Vegas | Is North Las Vegas a Good Place to Buy New Construction? |
| Sparks | Why Buy New Construction in Sparks Instead of Reno? |
| Centennial Hills | *(none)* |
| Enterprise | *(none)* |
| Dayton / Fernley | *(none)* |

---

## 7. What to copy, what to beat

**Copy:**
- The exact 11-section `ncc` skeleton — it maps cleanly to how a buyer actually researches.
- `blockquote.direct-answer` + `ul.key-takeaways` + `speakable` schema with `cssSelector: [".direct-answer", ".key-takeaways", ".faq-answer"]`. This is the AI-answer play and it costs nothing.
- Sitewide footer column linking every geo sub-hub.
- 3-level breadcrumb + `BreadcrumbList` schema.
- Per-page `data-cta-source="{city}-newconstruction-{hero|cta}"` lead attribution.
- Two tables, both with `<caption>`: builders (Builder / Tier / Communities / Price range) and communities (Community / Builders / From / Status).
- The 6-fixed + 2-local FAQ formula.
- The AI-crawler opt-in robots.txt.

**Beat them on:**
1. **Filter the sub-hub IDX feed by year built.** Theirs is not filtered — 17 of 24 Henderson "new construction" listings were built before 1997. Ours should apply the same `yearBuilt ≥ 2024` + keyword + description post-filter the master hub uses, and print the methodology line.
2. **Add anchor ids to every H2 and a sticky TOC.** They have it on the master and forgot it on the sub-hubs.
3. **Render FAQ questions as real `<h3>`s**, not schema-only.
4. **Real imagery** — builder logos, community photos, plat/site maps. They ship exactly one editorial image per page.
5. **Link the parent city page down to its own sub-hub** with matching anchor text. `/henderson/` currently mis-points its "Henderson New Construction" card at the metro hub.
6. **Wire the blog cluster into the matching geo page.** The 6 guide links are identical across all 5 sub-hubs; the city-specific posts that exist are not linked from the city page.
7. **Pick one city-segment scheme.** Don't ship `/centennial-hills/new-construction/` whose breadcrumb parent 308s to `/las-vegas/centennial-hills/`.
8. **Fill the 404s they left open** — Lake Las Vegas, Skye Canyon, Inspirada, Cadence, Mountain's Edge, Spring Valley, Boulder City all have real search volume and only get an anchor on their master hub.
9. Fix the class of bug that produced Centennial Hills' hero reading **"0+ Active builders"** (stat derived from a table that page doesn't have) and Pahrump's **"New New Construction Homes"** heading.

---

*Sources: raw HTML pulled 2026-07-25 via curl with a desktop UA; sitemap.xml (2,823 URLs); robots.txt. Working files under `.../scratchpad/nrg/agentC/`.*
