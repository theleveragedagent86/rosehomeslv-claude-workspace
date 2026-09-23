# Nevada Real Estate Group — Master Site Architecture & URL Inventory

**Source:** `https://www.nevadarealestategroup.com/sitemap.xml`
**Captured:** 2026-07-25
**URLs listed in sitemap: 2,823 — but only 2,129 are unique (694 duplicates, 24.6%)**

This is the **QA ground-truth document**. Every other research file in this folder
(`01`–`06`) is verified against this one.

---

## 1. What this site actually is

Not a normal agent website. It is a **programmatic SEO machine** built on
**Next.js + Sanity CMS + Repliers MLS/IDX**, generating ~2,800 indexed pages from a
structured content dataset. The `/new-construction/` page Ryan liked is the **top of a
deliberate 4-tier pyramid**, not a standalone page.

### Evidence of the tech stack (from `robots.txt`, verbatim signals)
> **QA-CORRECTED 2026-07-25.** Counts in this file were verified by the QA pass in
> `07-qa-verification.md`. Corrections applied inline below: blog count 708 → **885**,
> builder pages 18 → **20**, NC-adjacent blogs 177 → **31**. Stack adds **Supabase Auth**.

| Signal | Meaning |
|---|---|
| `generateMetadata`, `revalidate=864000`, "ISR-cached 10 days" | **Next.js App Router** |
| `Disallow: /studio/` | **Sanity CMS** (Sanity Studio mounts at `/studio`) |
| "fresh **Repliers** calls", "GLVAR MLS / Repliers IDX" | **Repliers** is the MLS/IDX provider |
| `trailingSlash: true` | Next.js config — every URL ends in `/` |
| Legacy `/property-search/*` 301 → `/search` | Migrated **off Sierra Interactive** |
| `Disallow: /search?` + `/search/?` | Faceted-search crawl trap deliberately blocked |
| `/data/las-vegas-market` Allow-carved | Data-PR pages built for journalist citation |

**Takeaway for us:** their `robots.txt` is an engineering changelog written in comments.
It confirms they treat MLS API quota as a real cost and cache aggressively. Our Lofty
build has no such constraint since Lofty serves its own IDX.

---

## 2. The 4-tier spider web (THE core finding)

```
TIER 1  HUB            /new-construction/                     ← the page Ryan sent
                        ~25 min read, 18 builders, 73+ communities

TIER 2  GEO SUB-HUBS   /{area}/new-construction/              ← 9 total
                        localized clone of the hub

TIER 3  ENTITY PAGES   /builders/{builder}/                   ← 18 builder pages
                        /{city}/{neighborhood}/               ← ~1,200 community pages

TIER 4  SUPPORT        /blog/{slug}/                          ← 708 posts (177 NC-adjacent)
                        /compare/{a}-vs-{b}/                  ← 38 comparison pages
                        /guides/{topic}/                      ← 10 evergreen guides
                        /market-report/, /zip/, /schools/      ← data pages
```

Every tier links **up** to the hub and **down** to its children. That is the "spider web"
Ryan identified, and it is the entire SEO strategy: the hub absorbs authority from ~200
supporting pages and ranks for the head term.

---

## 3. Complete `new-construction` URL set (11 pages)

Breakdown: **2 masters** (`/new-construction/` for Las Vegas, `/reno-new-construction/`
for Northern Nevada), **8 geo sub-hubs** on the `/{area}/new-construction/` pattern, and
**1 outlier** (`/pahrump/new-construction-homes/`, which uses a different template).

| URL | Tier | Market |
|---|---|---|
| `/new-construction/` | **1 — master hub** | Las Vegas metro |
| `/henderson/new-construction/` | 2 | Henderson |
| `/summerlin/new-construction/` | 2 | Summerlin |
| `/north-las-vegas/new-construction/` | 2 | North Las Vegas |
| `/centennial-hills/new-construction/` | 2 | Centennial Hills |
| `/enterprise/new-construction/` | 2 | Enterprise / SW LV |
| `/reno-new-construction/` | 2 | Reno *(root-level, inconsistent slug)* |
| `/sparks/new-construction/` | 2 | Sparks |
| `/dayton/new-construction/` | 2 | Dayton |
| `/fernley/new-construction/` | 2 | Fernley |
| `/pahrump/new-construction-homes/` | 2 | Pahrump *(inconsistent slug)* |

**Slug inconsistency noted:** `/reno-new-construction/` and
`/pahrump/new-construction-homes/` break the `/{area}/new-construction/` pattern. Do NOT
replicate this — pick one pattern and hold it.

**`/builders/` is absent from the sitemap but returns 200** (verified by Agent B). It is a
near-duplicate of the hub and is `rel=canonical`-ed to `/new-construction/`, so it is
deliberately excluded from the sitemap rather than missing. The 18 builder pages are
therefore not orphaned: they are reachable from the hub's builder card grid and from a
builder chip grid repeated on every builder page.

---

## 4. Complete builder page set (20 pages — QA-corrected from 18)

`/builders/` + one of:
`beazer` · `blue-heron` · `century-communities` · `christopher` · `dr-horton` · `harmony`
· `kb-home` · `lennar` · `lgi` · `pulte-del-webb` · `richmond-american` · `shea`
· `storybook` · `taylor-morrison` · `toll-brothers` · `touchstone` · `tri-pointe` · `woodside`

Plus 2 more, confirmed live by QA: **`/builders/pardee/`** (a real, distinct 20th builder
page) and **`/builders/woodside-homes/`**.

**`woodside` and `woodside-homes` are two separate live pages, each self-canonical.** This
is not a sitemap duplicate, it is **active keyword cannibalization** on their own site: two
indexable URLs competing for the same builder query. Do not replicate.

**Sitemap also lists 7 builders twice** (beazer, century-communities, kb-home, lennar,
richmond-american, toll-brothers, tri-pointe), part of the wider 694-URL duplication.

---

## 5. The repeatable page templates (what makes 2,800 pages possible)

### 5a. City × intent matrix
Each city slug gets a fixed set of intent children. Counts of each suffix across the site:

| Intent suffix | Count | Example |
|---|---|---|
| `just-listed` | 23 | `/boulder-city/just-listed/` |
| `sell-my-house` | 23 | `/summerlin/sell-my-house/` |
| `homes-for-sale` | 20 | `/centennial-hills/homes-for-sale/` |
| `real-estate-agent` | 15 | `/summerlin/real-estate-agent/` |
| `new-construction` | 9 | `/henderson/new-construction/` |
| `condos-for-sale` | 9 | `/enterprise/condos-for-sale/` |
| `55-plus-communities` | 6 | `/north-las-vegas/55-plus-communities/` |

Fully-built example — **Summerlin** has all 8:
`/summerlin/` · `/summerlin/homes-for-sale/` · `/summerlin/condos-for-sale/`
· `/summerlin/new-construction/` · `/summerlin/just-listed/` · `/summerlin/sell-my-house/`
· `/summerlin/real-estate-agent/` · `/summerlin/55-plus-communities/`

Boulder City instead gets **feature**-intent children — `gated-community-homes`,
`lakeview-homes`, `no-hoa-homes`, `rv-parking-homes`, `homes-with-swimming-pool`,
`historical-homes`, `lake-mead-view-properties`. So the intent set is **market-adapted**,
not uniform.

### 5b. Neighborhood/community pages — the bulk of the site
| City namespace | Page count |
|---|---|
| `/las-vegas/{neighborhood}/` | **762** |
| `/henderson/{neighborhood}/` | **393** |
| `/north-las-vegas/{neighborhood}/` | **112** |
| `/reno/{neighborhood}/` | 161 |
| `/sparks/`, `/gardnerville/`, `/carson-city/`, `/dayton/` etc. | ~200 combined |

These are hyper-granular — not just "Summerlin" but `aventura-summerlin`,
`eagle-hills-summerlin`, `country-club-hills-summerlin`, and every single Inspirada and
Lake Las Vegas sub-village (`alterra-at-inspirada`, `bella-fiore-at-lake-las-vegas`,
`carmona-at-inspirada`…). Sub-village pages are the direct SEO capture layer for new
construction — a buyer searching a specific builder neighborhood lands here.

### 5c. Comparison pages — 38 total
Pattern `/compare/{a}-vs-{b}/`, almost all **hub-and-spoke against Summerlin**:
`henderson-vs-summerlin`, `anthem-vs-summerlin`, `inspirada-vs-summerlin`,
`mountains-edge-vs-summerlin`, `aliante-vs-summerlin`, `cadence-vs-summerlin`,
`centennial-hills-vs-summerlin`, `lake-las-vegas-vs-summerlin`, `skye-canyon-vs-summerlin`,
`providence-vs-summerlin`, `rhodes-ranch-vs-summerlin`, `southern-highlands-vs-summerlin`…

They picked **one anchor entity (Summerlin)** and compared everything to it. Cheap to
produce, captures a large long-tail of "X vs Y" queries. **Highly replicable for us.**

### 5d. Data pages
- `/market-report/` → `/market-report/cities/{city}/` (84 pages) + `/market-report/zip-codes/`
- `/zip/` → `/zip/{zipcode}/` (61 pages: 89101, 89102, 89103…)
- `/schools/` → `/schools/{school-slug}/` (26 pages: `palo-verde-high-school`,
  `sig-rogich-middle-school`, `goolsby-elementary-school`…)

### 5e. Evergreen guides — 10 total
`/guides/` + `best-neighborhoods-las-vegas` · `las-vegas-cost-of-living` ·
`las-vegas-property-tax` · `las-vegas-short-term-rentals` · `las-vegas-vs-phoenix` ·
`nevada-down-payment-assistance` · `nevada-tax-advantages` · `safest-neighborhoods-las-vegas`
· `summerlin-schools` · `summerlin-vs-henderson`

### 5f. Lifestyle / feature filter pages (root level)
`/55-plus-communities/` · `/golf-communities/` · `/guard-gated-communities/` ·
`/high-rise-condos/` · `/homes-with-casitas-mother-in-law-suites/` · `/homes-with-pools/` ·
`/homes-with-rv-garages/` · `/las-vegas-condos-for-sale/` · `/las-vegas-luxury-homes/` ·
`/las-vegas-single-story-homes/` · `/las-vegas-townhomes/` · `/luxury-communities/` ·
`/luxury-condos-las-vegas/` · `/luxury-homes-over-1-million/` · `/luxury-homes-over-3-million/`
· `/luxury-homes-over-5-million/` · `/open-houses-las-vegas/` · `/recently-reduced-las-vegas/`

Note the **price-ladder pattern**: over-1M / over-3M / over-5M. Three pages from one idea.

### 5g. Agent/brand landing pages
`/realtor-las-vegas/` · `/realtor-henderson/` · `/realtor-north-las-vegas/` ·
`/realtor-summerlin/` · `/realtor-reno/` · `/realtor-sparks/` · `/realtor-carson-city/` ·
`/realtor-incline-village/` — plus `/about/`, `/reviews/`, `/press/`, `/join-the-team/`,
`/real-estate-agents/`, `/author/chris-nevada/`

### 5h. Relocation / conversion pages
`/moving-to-las-vegas/` · `/moving-to-henderson/` · `/moving-to-summerlin/` ·
`/moving-to-reno/` · `/relocation-guide/` · `/california-tax-savings/` ·
`/nellis-afb-relocation-guide/` · `/home-value-estimator/` · `/cash-offer/` · `/cma/` ·
`/mortgage-pre-approval-request/` · `/buyers/` · `/sellers/` · `/contact/`

---

## 6. Blog cluster sizing

**QA-corrected figures:**
- **885 blog posts live on the site**
- **707 appear in the sitemap → 178 posts are orphaned from the sitemap entirely.**
  Google can only find them via internal links. This is a real hygiene bug, not a rounding
  difference.
- **31 posts are genuinely new-construction-topical** (25 by strict slug match on
  `new-construction|builder|incentive|lot-premium|design-center|pre-drywall|buydown`).
  The earlier "177" figure was a **broad** count that included any post mentioning a geo
  term (summerlin, henderson, cadence, skye…) and overstates the true NC cluster by ~6x.
  **Use 31.**

### Confirmed pure new-construction posts (21 found by slug)
```
/blog/new-construction-homes-north-las-vegas-guide-2026/
/blog/new-construction-homes-henderson-builders-guide-2026/
/blog/new-construction-homes-sparks-builders-guide-2026/
/blog/new-construction-homes-reno-builders-guide-2026/
/blog/southwest-las-vegas-new-construction-homes-town-square-2026/
/blog/do-you-need-realtor-new-construction-las-vegas-2026/
/blog/sid-lid-taxes-las-vegas-new-construction-2026/
/blog/new-construction-vs-resale-las-vegas-2026-comparison/
/blog/new-construction-resale-las-vegas-decision-matrix-2026/
/blog/where-to-buy-new-construction-las-vegas-2026-tier-ranking/
/blog/2-1-buydown-las-vegas-new-construction-2026/
/blog/california-to-las-vegas-new-construction-savings-2026/
/blog/clark-county-property-tax-reassessment-new-construction-2026/
/blog/design-center-budget-las-vegas-new-construction-2026/
/blog/first-time-buyer-new-construction-mistakes-las-vegas-2026/
/blog/hoa-landscape-requirements-new-construction-las-vegas-2026/
/blog/inspirada-final-75-homes-south-henderson-new-construction-2026/
/blog/lot-premium-negotiation-las-vegas-new-construction-2026/
/blog/new-construction-timeline-las-vegas-build-reality-2026/
/blog/pre-drywall-inspection-new-construction-las-vegas-2026/
```

**Naming convention is rigid:** `{topic}-{market}-{year}`. Every slug ends in `-2026`.
That is a deliberate freshness signal, and it means they re-slug annually.

**Every FAQ answer on the hub has a matching blog post.** The hub FAQ asks about lot
premiums → `/blog/lot-premium-negotiation-las-vegas-new-construction-2026/`. Asks about
design center budgets → `/blog/design-center-budget-las-vegas-new-construction-2026/`.
Asks whether you need an agent → `/blog/do-you-need-realtor-new-construction-las-vegas-2026/`.

**That is the reusable playbook: the hub FAQ is the blog editorial calendar.**

---

## 7. Sitemap hygiene issues (things NOT to copy)

1. **Duplicate URLs — 694 of 2,823 entries (24.6%) are dupes.** Only 2,129 URLs are
   unique. A large Northern-Nevada block (Carson City, Dayton, Gardnerville, Reno,
   Sparks) plus `/market-report/`, `/market-report/zip-codes/` and 7 builder URLs are
   each listed twice. Looks like two sitemap generators (a Las Vegas set and a Reno set)
   concatenated without dedupe. This wastes crawl budget and is a straightforward bug.
2. **`woodside` vs `woodside-homes`** — two URLs for one builder.
3. **Slug pattern breaks** — `/reno-new-construction/` and `/pahrump/new-construction-homes/`.
4. **No `/builders/` index** — 18 pages with no directory parent.
5. **`lastmod` is identical (`2026-07-25T15:02:48.326Z`) on every single URL** — the
   sitemap is regenerated wholesale on each build, so `lastmod` carries zero signal.
   Google discounts this.
6. **Two `/55-plus-communities/` variants** — `/55-plus-communities/` and
   `/55-plus-communities-las-vegas/` compete for the same query.

---

## 8. What we replicate for Rose Homes LV

| Their asset | Our version | Priority |
|---|---|---|
| `/new-construction/` hub | Master NC hub, Lofty landing page | **P0** |
| 5 LV-metro geo sub-hubs | Henderson, Summerlin, NLV, Skye Canyon, Southwest | **P1** |
| 18 builder pages | Same 18 builders, LV-only | **P1** |
| Sticky TOC component | Reusable across hub + spokes | **P0** |
| Repliers IDX feed | **Lofty IDX embed** | **P0** |
| 21 NC blog posts | 15–20 posts, one per hub FAQ | **P2** |
| 38 `/compare/` pages | Anchor on Summerlin, same trick | **P3** |
| 1,200 neighborhood pages | Skip — not feasible, and low ROI without their data pipeline | — |

**Architecture decision to make:** Lofty landing pages vs Lofty blog posts. Their tiers 1–3
are custom Next.js routes; on Lofty we get landing pages (`/page-slug`) and blogs
(`/blog/<slug>`, singular — the plural `/blogs/` 404s). Hub + sub-hubs + builder pages
should be **landing pages**; the support cluster should be **blog posts**.

---

## 9. Files in this research folder

| File | Contents | Agent |
|---|---|---|
| `00-master-sitemap-architecture.md` | This file — URL inventory, QA ground truth | orchestrator |
| `01-hub-page-teardown.md` | Full section/copy/CSS teardown of `/new-construction/` | A |
| `02-builder-pages.md` | 18 builder pages, shared template, link graph | B |
| `03-geo-subhubs.md` | `/{area}/new-construction/` template | C |
| `04-community-lifestyle-pages.md` | Community + lifestyle filter templates | D |
| `05-blog-cluster.md` | Blog template + topical cluster map + our topic list | E |
| `06-conversion-and-tech.md` | IDX embed spec, CMS, design tokens, TOC code | F |
| `07-qa-verification.md` | Cross-check of all of the above | QA |
