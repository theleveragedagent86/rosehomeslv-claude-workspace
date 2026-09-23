# NRG Research 04: Community / Neighborhood Pages + Lifestyle Filter Pages

Source: https://www.nevadarealestategroup.com/
Captured: 2026-07-25 (raw HTML via curl, all pages fetched successfully)
Scope: 26 community pages + 12 lifestyle/filter pages

**Headline finding: there are exactly TWO templates in this tier, and they are radically different.**

1. **The Community page** ("cp-" template): a 49-section, ~11,000 to 12,800 word, 40-H2 monster. Byte-for-byte identical section order across all 24 community pages. No table of contents. IDX is a small 8-card client-hydrated teaser, not a full search.
2. **The Lifestyle/Filter page**: four sub-variants, three of which are thin (1,500 to 5,300 words) content wrappers around either a live server-rendered MLS feed or a community directory grid.

---

## 0. Platform notes (applies to everything below)

- **Next.js App Router** (`/_next/image/`, RSC payload in `self.__next_f`), server-rendered HTML. Not WordPress, not Lofty, not IDX Broker.
- **IDX vendor: Repliers**, sourced from GLVAR. Meta description on `/guard-gated-communities/` says verbatim: `"Updated every 30 minutes from GLVAR via Repliers IDX."`
- **Search URL grammar** (this is the whole IDX filtering system): `/search/?city=<City>&q=<Community>&priceMin=<n>&priceMax=<n>` plus `/search/?view=map`.
- **Lead capture**: every form POSTs to `/api/leads/buyer/` with a hidden `interest` field, e.g. `<input type="hidden" name="interest" value="lake-las-vegas-lead"/>`. Honeypot field named `website` on every form.
- **No iframes anywhere** except the GTM noscript pixel. No Google Maps embed, no Walk Score widget, no third-party school widget. Every "map" and "chart" is hand-built HTML/CSS.
- **Bare-slug community URLs 308-redirect to the city-scoped canonical.** Verified: `/ascaya/` to `/henderson/ascaya/`, `/seven-hills/` to `/henderson/seven-hills/`, `/rhodes-ranch/`, `/southern-highlands/`, `/red-rock-country-club/`, `/the-summit-club/` all to `/las-vegas/...`. The `/communities/` hub and `/golf-communities/` still link to the bare slugs, so they are eating a redirect hop on hundreds of internal links.

---

## 1. THE COMMUNITY PAGE TEMPLATE

Deep dives: `/henderson/lake-las-vegas/`, `/las-vegas/skye-canyon/`, `/henderson/inspirada/`.

### 1.1 Structural verdict

All three pages have **the identical 49-section DOM sequence**. I diffed the full `<section>` class list across all 24 community pages: **22 of 24 are byte-identical in section order.** The only two exceptions are the geo hubs `/summerlin/` and `/north-las-vegas/`, which have 48 sections (they drop the "More communities in this city" block, because they *are* the city).

So `/summerlin/` and `/north-las-vegas/` are NOT a separate geo-hub template. They run the exact same community template as `/henderson/inspirada/`.

### 1.2 Exact section order (49 sections, in DOM order)

Module classes are `cp-modNN`. Note the numbers are out of sequence, which tells you the modules are a **reusable library assembled per page**, not a linear document.

| # | Section class | Anchor id | H2 / purpose |
|---|---|---|---|
| 1 | `cp-hero` | (none) | H1 + eyebrow + "Last updated · N min read · By Chris Nevada" + 2 CTAs over full-bleed image |
| 2 | `cp-mod08` | (none) | 4 stat tiles ("at a glance" strip), each with value + label + source |
| 3 | `cp-mod10` | (none) | E-E-A-T authorship block: Written by / Data reviewed by / Last updated |
| 4 | `cp-mod05` | (none) | "What Should You Know About X at a Glance?" 5 key takeaways |
| 5 | `cp-section--listings` | `#listings` | "Where Can I Find X Homes for Sale?" **IDX teaser (8 cards)** |
| 6 | `cp-mod20` | (none) | "How Many X Homes Sell in Each Price Range?" 6 price bands |
| 7 | `cp-section--directory` | (aria `browse-by-feature-heading`) | "How Can You Find an X Home by Village, Type & Price?" |
| 8 | `cp-mod28` | `#listing-alerts` | "How Can You Get New X Listings First?" **lead form #1** |
| 9 | `cp-section--schools` | `#schools` | "How Are the Schools in X?" tabbed school cards + ranked table |
| 10 | `cp-mod14` | (none) | "Is X Safe?" |
| 11 | `cp-section--intro` | (none) | "What's It Like Living in X, NV?" + Where Is X + glance card |
| 12 | `cp-mod06` | (none) | "How Does X Score?" 6-category letter-grade report card |
| 13 | `cp-mod-qa` | (none) | Standalone Q&A: "Is X a good place to live?" |
| 14 | `cp-section--demographics` | (none) | "Who Lives in X?" (dark section) |
| 15 | `cp-mod16` | (none) | "How Fast Is the X Area Growing?" population bar chart 2010 to 2030 |
| 16 | `cp-mod17` | (none) | "How Does X Score for Livability?" 6 score rings |
| 17 | `cp-mod22` | (none) | "How Is the X Real Estate Market Trending?" 3 sparkline charts |
| 18 | `cp-mod23` | (none) | "How competitive is X right now?" 0-100 competitiveness gauge |
| 19 | `cp-section--buyer-fit` | `buyer-fit-title` | "Who Should Buy a Home in X?" 6 buyer-type cards |
| 20 | `cp-mod24` | (none) | "How Do X's Top 6 Villages Compare?" comparison table |
| 21 | `cp-mod25` | (none) | "What's Inside X's Top Villages?" submarket deep dives |
| 22 | `cp-mod26` | (none) | "What Does the X Market Look Like Within ZIP NNNNN?" ZIP tier table |
| 23 | `cp-mod29` | (none) | "Which Statistics Define X Real Estate?" 8 sourced stat cards |
| 24 | `cp-mod36` | (none) | "Why Does X Stand Apart From Its Peers?" 5 differentiators |
| 25 | `cp-mod37` | (none) | "What Are the Top 10 Reasons to Buy a Home in X?" |
| 26 | `cp-mod39` | (none) | **"Who Builds New Homes in X?" the new-construction module** |
| 27 | `cp-mod40` | (none) | "What Outdoor Amenities Does X Offer?" |
| 28 | `cp-mod41` | (none) | "What Does a Weekend in X Look Like?" 4 lifestyle stats |
| 29 | `cp-mod21` | (none) | "Can You Tour X Homes This Weekend?" open-house CTA |
| 30 | `cp-mod42` | (none) | Standalone Q&A: "What does an HOA cost in X?" |
| 31 | `cp-section--relocation` | (none) | "Should I Move to X?" California-buyer pitch (dark section) |
| 32 | `cp-mod48` | (none) | "How to relocate to X in 8 steps" (HowTo schema) |
| 33 | `cp-mod12` | (none) | "What Drives the X Economy?" 4 stats + top employers |
| 34 | `cp-mod45` | (none) | "How Does X Compare to [City], Las Vegas & [Peer]?" 4-column table |
| 35 | `cp-section--mortgage` | `#mortgage-calculator` | "What Will X Cost You Each Month?" calculator + `#cp-cost-panel-0/1/2` |
| 36 | `cp-mod47` | (none) | "How Easy Is Getting Around From X?" drive times + transport modes |
| 37 | `cp-mod49` | (none) | Standalone Q&A: "How long does it take to close on a home in X?" |
| 38 | `cp-mod32` | (none) | Standalone Q&A: "What down payment do you need to buy in X?" |
| 39 | `cp-section--faq` | (none) | "What Do X Buyers Most Frequently Ask?" the 18-answer FAQ accordion |
| 40 | `cp-mod54` | (none) | "What Else Do People Ask About X?" 8 People-Also-Ask cards |
| 41 | `cp-mod51` | (none) | "Why Is Nevada Real Estate Group the #1 Real Estate Team in Nevada?" |
| 42 | `cp-section--contact` | `#cp-contact` | "Want to Talk to an X Real Estate Expert?" **lead form #2** |
| 43 | `cp-mod55` | (none) | "Which Communities Are Within 30 Minutes of X?" 6 nearby links |
| 44 | `cp-section` | (none) | "More communities in this city" (the A-Z sibling link block) |
| 45 | `cp-mod56` | `#letter-a`..`#letter-z` | "Which X Villages Can You Explore A-Z?" |
| 46 | `cp-mod57` | (none) | "What Else Should You Read About X?" 4 related-resource cards |
| 47 | `cp-mod58` | (none) | "Where Does This X Data Come From?" sources and methodology |
| 48 | `cp-section--fair-housing` | (none) | Fair-housing + brokerage disclaimer |
| 49 | `footer-cta` | (none) | "Ready to make your move?" **lead form #3** |

### 1.3 Sticky table of contents: NO

**There is no TOC on any community page.** I grepped every page for `class="toc*"`, `jump-nav`, `page-nav`, `section-nav`, `anchor-nav`. Zero hits on all 24 community pages. The only anchor ids in the whole document are `#listings`, `#listing-alerts`, `#schools`, `#mortgage-calculator`, `#cp-contact`, `#cp-cost-panel-0/1/2`, and the `#letter-X` jumps inside module 45.

This is a genuine weakness in their build. A ~9,000–10,500-word page with ~39 H2s and no TOC. **We should add one.**

> ### CORRECTED BY QA (`07-qa-verification.md`, C1)
>
> The original line here claimed `/55-plus-communities/` was "the only page on the whole
> site that has a real TOC." That is wrong. There are **two distinct TOC components**:
>
> | Component | Markup | Where it appears | Goes fixed? |
> |---|---|---|---|
> | **A — BEM** | `h2.toc__title` + `ol.toc__list` | `/new-construction/` (18 links), `/builders/` (byte-identical clone), `/55-plus-communities/` (11 links) | **Yes**, right rail at ≥1024px |
> | **B — details** | `<details><summary>` + `ol.toc-list` | **every blog post** | **Never** |
>
> Sub-hubs, community pages, builder pages and all other lifestyle pages have **no TOC at all**.
>
> The rail rule is:
> ```css
> @media (min-width:1024px){
>   :is(body:has(.community-card) .toc, body:has(.nc-table) .toc){
>     position:fixed; right:24px; …
>   }
> }
> ```
> The `.community-card` selector is what misled this file and `05-blog-cluster.md` into
> saying "community pages." That class only ever appears on `/55-plus-communities/`.
>
> **Zero scroll-spy exists.** The only `IntersectionObserver` across 36 JS chunks is
> Next.js link prefetch.

### 1.4 IDX embed placement and filtering

- **Placement:** section 5 of 49, roughly 12% down the page, immediately after the "at a glance" takeaways. Anchor `#listings`.
- **Type:** client-hydrated. Server HTML ships 8 grey skeleton `<li>` cards inside `<div class="cp-search-listings" aria-busy="true" aria-live="polite">` with `<ul class="listing-grid">`. Listings are fetched after hydration. **Zero listing content in the server HTML**, so those cards contribute nothing to SEO.
- **Community-filtered? Yes, but crudely.** All the surrounding "browse" links use `/search/?city=Henderson&q=Inspirada&priceMin=...&priceMax=...`. It is a free-text `q=` match against the MLS, not a polygon or subdivision-code filter. NRG openly admits the limitation in their own copy on `/henderson/inspirada/`:

  > "the MLS does not tag listings by village, so tier-level math would be guesswork"

- **Honest-scoping language** is baked into the copy everywhere: they repeatedly say the numbers are ZIP-area, not plan-only. Example H2: "What Does the Inspirada Market Look Like Within ZIP 89044?"
- The intro paragraph above the IDX grid is a hand-written direct answer with a live count and a citation link, e.g. "Lake Las Vegas listed 27 active homes across ZIP 89011 in June 2026 according to Las Vegas REALTORS."

### 1.5 Tables on a community page (4 real `<table>`-style data grids)

1. **Ranked school table** (module 9). Columns: Rank / School / Type / Grades / GreatSchools rating / Neighborhood + drive time / Homes Near (price floor).
2. **ZIP tier table** (module 22, `cp-mod26`). Columns: ZIP / Primary Area / Median Price / $ per Sq Ft / Days on Market / Active / YoY. Cells they cannot source are literally printed as `n/a*` with a footnote explaining why.
3. **Village comparison table** (module 20, `cp-mod24`). Top 6 enclaves side by side.
4. **Community comparison table** (module 34, `cp-mod45`). Rows: Median List Price, Active Listings, Days on Market, Established (year), HOA Range, Crime Index, Open Space, New Construction, Best For. Columns: the community, its parent city, Las Vegas, one peer community.

HOA is NOT a table on most pages. It is a standalone Q&A block (`cp-mod42`) plus, on some pages only, an "HOA Fees by Village Tier" card list (`cp-mod30`, present on Lake Las Vegas, absent on Inspirada and Skye Canyon).

### 1.6 FAQ

**18 `Question` entities in FAQPage JSON-LD on every single community page.** Not 17, not 19. Eighteen, on all 24. They are split across two visible modules:

- `cp-faq2` (section 39): headed "X FAQ - 18 Answers", one hero question with a big stat callout ("What is the median home price in X?" answered with a `$539K` display figure), then 9 or 10 accordion items.
- `cp-mod54` (section 40): "What Else Do People Ask About X?", 8 People-Also-Ask style cards answered in 2 to 3 sentences.

Plus 4 additional standalone single-question sections rendered as their own `<section>` with `aria-label="Question: ..."`: `cp-mod-qa` (is it a good place to live), `cp-mod42` (HOA cost), `cp-mod49` (time to close), `cp-mod32` (down payment). These are AI-answer bait, each one a self-contained "Quick Answer" block.

### 1.7 Forms (3 per page, all to `/api/leads/buyer/`)

| Form | Class | Location | Fields |
|---|---|---|---|
| Listing alerts | `cp-mod28__form` | section 8 | Full name, Email, Phone, Max price (select: Any / Under $400K / Under $600K / Under $850K / Under $1.5M / $1.5M+) |
| Main contact | `cp-form` | section 42 | First, Last, Email, Phone, Questions/Comments, Timeline (0-3 / 3-6 / 6-12 / 12+ months / Just researching) + hidden `interest=<slug>-lead` |
| Footer CTA | `ccm__form` | section 49 | First, Last, Email, Phone, Timeline + hidden `ccm-source` |

Every form carries a long TCPA consent paragraph naming "Nevada Real Estate Group, Chris Nevada, and LPT Realty (the brokerage of record)".

### 1.8 Map embeds: NONE

No iframe, no Leaflet, no Mapbox, no Google Maps embed. The "Where Is X" block (`cp-ov-loc`, inside section 11) is a paragraph of prose plus 5 drive-time chips. There is exactly one outbound `maps.google.com` text link on the whole page.

### 1.9 Image galleries: NONE

`/las-vegas/skye-canyon/` ships **10 `<img>` tags total** for a 11,722-word page:
- 1 hero (`/images/communities/skye-canyon/skye-canyon-hero.jpg`, Next.js `fill`, `fetchPriority=high`, 6-width srcset)
- 1 author headshot (`/images/team/chris-nevada.jpg`)
- 4 school "campus" stock photos (`/images/schools/campus-28-biophilic.jpg` etc), explicitly disclaimed on-page: "Campus photos are representative imagery"
- 1 second author headshot
- 3 footer logos (EHO, REALTOR)

Community pages run 9 to 12 images. This is a **text-first, schema-heavy SEO play**, not a visual community showcase.

### 1.10 Word counts

Range 10,183 to 12,771 words in `<main>`. Median ~11,650. The hero says "27 min read". Full table in section 3 below.

### 1.11 Schema.org (32 distinct @types on every community page)

`AdministrativeArea, AggregateRating, Answer, Article, BreadcrumbList, City, ContactPoint, Country, CreativeWork, Dataset, EducationalOccupationalCredential, FAQPage, GeoCoordinates, HowTo, HowToStep, ImageObject, ItemList, ListItem, MonetaryAmount, Organization, Person, Place, PostalAddress, PropertyValue, Question, Rating, RealEstateAgent, Review, SpeakableSpecification, State, Thing, WebPage, WebSite`

Breadcrumb is 3 levels: `Home > Las Vegas > Skye Canyon` (item URLs `/`, `/las-vegas/`, `/las-vegas/skye-canyon/`).

---

## 2. THE LIFESTYLE / FILTER PAGE TEMPLATES

There is no single lifestyle template. There are **four**, and the difference is exactly the question you asked: is it a filtered IDX feed with a wrapper, or is it editorial?

### Variant A: "rr-" live IDX feed hub (the answer to "mostly a filtered feed?" is YES for these)

Pages: `/guard-gated-communities/`, `/luxury-condos-las-vegas/`, `/homes-with-pools/`, `/homes-with-casitas-mother-in-law-suites/`, `/homes-with-rv-garages/`, `/recently-reduced-las-vegas/`. (`/open-houses-las-vegas/` is the same shape with `oh-` classes.)

Section order (max version, `/guard-gated-communities/`):
1. `rr-hero` - breadcrumb trail + "Live MLS Feed · Updated Every 30 Min" badge + H1 + 90-word direct-answer paragraph with a live count + a scan-methodology line
2. `rr-listings-section` - **server-rendered live listing cards**, not skeletons
3. `rr-directory-section` - the community directory grid, grouped by city
4. `rr-content-section` - 4 paragraphs of editorial
5. `rr-faq-section` - 5 to 8 Q&As
6. `rr-cta-section` - conversion pitch
7. blog feed (`hub-blog-feed-heading`) - 3 related posts
8. `footer-cta`

Only two anchor ids on the entire page: `nav`, `main-content`. **No TOC.**

The key structural difference from the community template: **the listings are in the server HTML.** Each card carries address, price, beds, baths, sq ft, acres, year built, subdivision name, MLS number, list date, and "Listing courtesy of [brokerage]". Badges: `NEW`, `PENDING`, `PRICE REDUCED $20k`, photo count. Plus an estimated monthly payment per card ("Est. $1,693/mo").

Their filter method is a documented fan-out, stated openly in the hero:

> "We fan-out search four MLS phrasings (guard gated, gated community, private gated, country club) and dedupe by MLS number so every active listing shows in one feed. 139 unique active listings match right now."

And the footnote: "Scanned 171 listings across four guard-gated queries · refreshes every 30 min · sorted by most recent update."

**This is a keyword search over MLS free text, and it leaks.** Live proof from the guard-gated feed I captured: it returned `2212 Wengert Avenue, Las Vegas, NV 89104` (a 1953 build at $299,900 in a non-gated east-side tract) and `2120 Iroquois Avenue, Pahrump, NV 89048`. Pahrump is 60 miles away and not in the Las Vegas metro. If we build this, we need a curated subdivision whitelist, not free-text matching.

Word counts: 2,813 to 5,282. H2 count: 2 to 6. FAQs: 0 to 8. `/recently-reduced-las-vegas/` and `/open-houses-las-vegas/` have **zero FAQPage schema**, they are pure feeds.

### Variant B: "communities-hub" directory page (no IDX at all)

Pages: `/luxury-communities/`, `/golf-communities/`, `/high-rise-condos/`.

Sections: direct-answer summary block, `communities-hub` (a city-grouped directory of community links with price ranges), one editorial section, `#faq`, navy CTA, blog feed, footer CTA.

1,558 to 1,896 words, 6 H2s, 7 to 8 FAQs, 5 images, 1 form, **no listings**. These are pure internal-link routers. `/golf-communities/` links to 38 individual community pages and nothing else.

### Variant C: long-form editorial guide WITH a TOC (the only TOC on the site)

Page: `/55-plus-communities/`. 5,057 words, 15 H2s, 10 FAQs, no IDX.

This is the **only** page in my entire sample with a real sticky-style table of contents (`<h2 class="toc__title">On This Page</h2>` + `toc__list`), and correspondingly the only one with a full anchor-id spine:

`#why-55-plus`, `#all-communities`, `#sun-city-comparison`, `#hopa-rules`, `#buyer-profiles`, `#hoa-structures`, `#true-cost`, `#hidden-surprises`, `#resale-vs-new`, `#consult`, `#faq`, plus `#faq-1` through `#faq-10`.

H2s are all question-shaped: "Why is Las Vegas the top 55+ relocation destination?", "What is HOPA and how does the 80/20 age rule work?", "When should you buy resale vs new construction in a 55+ community?"

**This is the variant we should copy for our lifestyle pages.** It is the best-built page in the tier.

### Variant D: unstructured long-form (anomaly)

Page: `/las-vegas-luxury-homes/`. 3,986 words, **28 H2s**, only 4 H3s, only 2 `<section>` wrappers, 3 images, no IDX, no TOC. Reads as an ungoverned wall of H2s: "The Ridges - Sub-Village Detail", "Entry Luxury ($1M-$2M) - Market Dynamics", "Ultra-Luxury ($10M+) - Single-Buyer-Driven Market". It also exposes a whole `/high-rise-condos/<tower>/` URL family (`/high-rise-condos/one-queensridge-place/`, `/waldorf-astoria-residences/`, `/veer-towers/`, etc). Do not copy this one, but do note the sub-page family it reveals.

### And one more: `/communities/` (the tier hub itself)

5,188 words, 15 H2s, 8 FAQs, no IDX, no TOC. Has an "On this page" H2 but no `toc` class, so it is a plain list not a component. Structure: buyer's-guide editorial, then 7 giant directory blocks with anchor ids `#summerlin` (154 communities), `#henderson` (204), `#las-vegas` (243), `#north-las-vegas` (57), `#high-rise-&-condos` (26), `#builders` (10), `#luxury` (105, sub-split into `$5M+ Trophy` 32 / `$3M+ Ultra` 34 / `$1M+` 39). Then FAQ, market reports, head-to-head comparison, outlying communities, blog feed.

**580+ community pages claimed in the meta title.** This hub is the link-equity distributor for the entire third tier.

---

## 3. INVENTORY TABLE (all 38 pages)

**Zero 404s. All 38 URLs returned HTTP 200.**

| URL | Status | H1 | Meta title | Words | TOC | IDX | #H2 | #FAQ |
|---|---|---|---|---|---|---|---|---|
| `/communities/` | 200 | Las Vegas Communities & Neighborhoods | Las Vegas Communities \| 580+ Neighborhoods Guide | 5,188 | no | no | 15 | 8 |
| `/summerlin/` | 200 | Summerlin Homes For Sale | Summerlin, Las Vegas: Homes for Sale & Community Guide | 10,183 | no | yes (8-card teaser) | 40 | 18 |
| `/north-las-vegas/` | 200 | North Las Vegas Homes For Sale | North Las Vegas Homes for Sale \| Nevada Real Estate Group | 10,740 | no | yes (8-card teaser) | 40 | 18 |
| `/las-vegas/southern-highlands/` | 200 | Southern Highlands Homes For Sale | Southern Highlands Homes for Sale - Las Vegas NV Community Guide | 11,326 | no | yes (8-card teaser) | 40 | 18 |
| `/las-vegas/mountains-edge/` | 200 | Mountains Edge Homes For Sale | Mountains Edge Homes for Sale - Las Vegas NV Community Guide | 11,673 | no | yes (8-card teaser) | 40 | 18 |
| `/las-vegas/enterprise/` | 200 | Enterprise Homes For Sale | Enterprise Homes for Sale - Las Vegas NV Community Guide | 11,843 | no | yes (8-card teaser) | 40 | 18 |
| `/las-vegas/spring-valley/` | 200 | Spring Valley Homes For Sale | Spring Valley Homes for Sale - Las Vegas NV Community Guide | 11,551 | no | yes (8-card teaser) | 40 | 18 |
| `/las-vegas/rhodes-ranch/` | 200 | Rhodes Ranch Homes For Sale | Rhodes Ranch Homes for Sale - Las Vegas NV Community Guide | 11,301 | no | yes (8-card teaser) | 40 | 18 |
| `/las-vegas/skye-canyon/` | 200 | Skye Canyon Homes For Sale | Skye Canyon Homes for Sale - Las Vegas NV Community Guide | 11,722 | no | yes (8-card teaser) | 40 | 18 |
| `/las-vegas/downtown-las-vegas/` | 200 | Downtown Las Vegas Homes For Sale | Downtown Las Vegas Homes for Sale - Las Vegas NV Community Guide | 12,771 | no | yes (8-card teaser) | 40 | 18 |
| `/henderson/anthem/` | 200 | Anthem Homes For Sale | Anthem Homes for Sale - Henderson NV Community Guide | 11,187 | no | yes (8-card teaser) | 40 | 18 |
| `/henderson/green-valley/` | 200 | Green Valley Homes For Sale | Green Valley Homes for Sale - Henderson NV Community Guide | 11,270 | no | yes (8-card teaser) | 40 | 18 |
| `/henderson/seven-hills/` | 200 | Seven Hills Homes For Sale | Seven Hills Homes for Sale - Henderson NV Community Guide | 11,467 | no | yes (8-card teaser) | 40 | 18 |
| `/henderson/macdonald-highlands/` | 200 | MacDonald Highlands Homes For Sale | MacDonald Highlands Homes for Sale - Henderson NV Community Guide | 11,646 | no | yes (8-card teaser) | 40 | 18 |
| `/henderson/lake-las-vegas/` | 200 | Lake Las Vegas Homes For Sale | Lake Las Vegas Homes for Sale - Waterfront Resort Living | 11,354 | no | yes (8-card teaser) | 40 | 18 |
| `/henderson/inspirada/` | 200 | Inspirada Homes For Sale | Inspirada Homes for Sale - Henderson NV Community Guide | 11,211 | no | yes (8-card teaser) | 40 | 18 |
| `/henderson/cadence/` | 200 | Cadence Homes For Sale | Cadence Homes for Sale - Henderson NV Community Guide | 11,370 | no | yes (8-card teaser) | 40 | 18 |
| `/henderson/ascaya/` | 200 | Ascaya Homes For Sale | Ascaya Homes for Sale - Henderson NV Luxury Estates | 11,654 | no | yes (8-card teaser) | 40 | 18 |
| `/las-vegas/summerlin-the-ridges/` | 200 | The Ridges Homes For Sale | The Ridges Homes for Sale, Summerlin NV | 12,315 | no | yes (8-card teaser) | 40 | 18 |
| `/las-vegas/the-peaks/` | 200 | The Peaks Homes For Sale | The Peaks Homes for Sale, Summerlin NV | 12,073 | no | yes (8-card teaser) | 40 | 18 |
| `/las-vegas/summerlin-grand-park/` | 200 | Grand Park Homes For Sale | Grand Park Homes for Sale, Summerlin NV | 11,850 | no | yes (8-card teaser) | 40 | 18 |
| `/las-vegas/summerlin-stonebridge/` | 200 | Stonebridge Homes For Sale | Stonebridge Homes for Sale, Summerlin NV | 11,998 | no | yes (8-card teaser) | 40 | 18 |
| `/las-vegas/sun-city-summerlin/` | 200 | Sun City Summerlin Homes For Sale | Sun City Summerlin Homes for Sale \| Nevada Real Estate Group | 12,194 | no | yes (8-card teaser) | 40 | 18 |
| `/las-vegas/red-rock-country-club/` | 200 | Red Rock Country Club Homes For Sale | Red Rock Country Club Homes for Sale, Summerlin NV | 12,218 | no | yes (8-card teaser) | 40 | 18 |
| `/las-vegas/the-summit-club/` | 200 | The Summit Club Homes For Sale | The Summit Club Homes for Sale, Summerlin NV | 12,271 | no | yes (8-card teaser) | 40 | 18 |
| `/trilogy-sunstone/` | 200 | Trilogy Sunstone - Shea Homes 55+ in Skye Canyon. | Trilogy Sunstone \| Shea Homes 55+ Community in Skye Canyon | 1,891 | no | no | 8 | 7 |
| `/guard-gated-communities/` | 200 | Las Vegas Guard-Gated Communities | Guard-Gated Communities in Las Vegas - Live MLS Feed \| NREG | 5,282 | no | **yes (server-rendered live feed)** | 6 | 8 |
| `/luxury-communities/` | 200 | Las Vegas Luxury Real Estate | Luxury Real Estate Las Vegas \| Nevada Real Estate Group | 1,896 | no | no | 6 | 8 |
| `/golf-communities/` | 200 | Golf Course Communities in Las Vegas | Golf Course Communities in Las Vegas \| Nevada Real Estate Group | 1,701 | no | no | 6 | 7 |
| `/high-rise-condos/` | 200 | High-Rise Condos in Las Vegas | High-Rise Condos in Las Vegas \| Luxury Towers \| NREG | 1,558 | no | no | 6 | 7 |
| `/luxury-condos-las-vegas/` | 200 | Luxury Condos in Las Vegas | Luxury Condos in Las Vegas - Live MLS Feed \| NREG | 4,811 | no | **yes (server-rendered live feed)** | 5 | 5 |
| `/55-plus-communities/` | 200 | 55+ Active Adult Communities in Las Vegas | 55+ Communities Las Vegas - 21 Active Adult Options | 5,057 | **YES** | no | 15 | 10 |
| `/homes-with-pools/` | 200 | Las Vegas Homes for Sale with Pools | Homes for Sale with Pools - Las Vegas, NV \| NREG | 4,024 | no | **yes (server-rendered live feed)** | 3 | 4 |
| `/homes-with-casitas-mother-in-law-suites/` | 200 | Las Vegas Homes with Casitas & Mother-in-Law Suites | Homes with Casitas & Mother-in-Law Suites - Las Vegas, NV \| NREG | 4,232 | no | **yes (server-rendered live feed)** | 3 | 5 |
| `/homes-with-rv-garages/` | 200 | Las Vegas Homes for Sale with RV Garages | Homes for Sale with RV Garages - Las Vegas, NV \| NREG | 4,202 | no | **yes (server-rendered live feed)** | 3 | 5 |
| `/las-vegas-luxury-homes/` | 200 | Luxury Homes for Sale in Las Vegas | Las Vegas Luxury Homes for Sale - $2M to $30M+ | 3,986 | no | no | 28 | 8 |
| `/recently-reduced-las-vegas/` | 200 | Recently Reduced Las Vegas Homes | Recently Reduced Las Vegas Homes - Live Price-Drop Feed \| NREG | 2,813 | no | **yes (server-rendered live feed)** | 2 | 0 |
| `/open-houses-las-vegas/` | 200 | Las Vegas Open Houses | Las Vegas Open Houses This Weekend - Live MLS Feed \| NREG | 3,267 | no | **yes (server-rendered live feed)** | 4 | 0 |

Notes on the table:
- "8-card teaser" = `cp-search-listings` skeleton, hydrated client-side, 8 newest listings. Not in server HTML.
- "server-rendered live feed" = full listing cards present in the raw HTML, dozens per page (43 to 65 images per page is the tell).
- FAQ counts are `Question` entities in FAQPage JSON-LD, which for community pages equals the visible count across `cp-faq2` + `cp-mod54`.

---

## 4. LINK GRAPH

### 4.1 What a community page links to (measured on `/henderson/inspirada/`, 156 links in `<main>`)

| Target family | Count | Notes |
|---|---|---|
| `/search/?...` | 29 | The IDX. Every price band, property type, and village card routes here. |
| `/henderson/` + sibling community pages | 25 | Parent city hub + ~20 sibling/sub-community pages |
| External citations | 55 | LVR (12), City of Henderson (10), Census (7), FBI (5), BLS (4), GreatSchools (3), Clark County, NV Legislature, BLM, Freddie Mac, RTC, DMV, CA FTB, NV Report Card, Walk Score |
| `/builders/<name>/` | 9 | The new-construction module |
| `/zip/89044/` | 5 | ZIP hub page family |
| In-page `#` anchors | 7 | The A-Z letter jumps only |
| `/buyers/first-time-buyers/` | 3 | |
| `/moving-to-las-vegas/` | 3 | |
| `/blog/...` | 3 | |
| `/las-vegas/` | 2 | |
| `/new-construction/` | 1 | Fallback when a builder has no `/builders/` page |
| `/mortgage-pre-approval-request/` | 1 | |
| `/boulder-city/` | 1 | Nearby-community module |

### 4.2 Real anchor text, community page to new-construction network

From `/henderson/inspirada/` module `cp-mod39` ("Who Builds New Homes in Inspirada?"), each builder is a card that links to `/builders/<slug>/`:

- `/builders/toll-brothers/` -> "Luxury & Move-Up | Toll Brothers | 3,000-4,500+ sq ft premium homes, the top of the plan | Communities: Inspirada Luxury Collection | Price Range: From $800K"
- `/builders/lennar/` -> "Family & Mid-Market | Lennar | Open-concept production homes with bundled-features pricing | Communities: Sunrise Heights and active phases | From $450K"
- `/builders/century-communities/` -> "First-Time & Family | Century Communities | Value-oriented new construction inside the plan | From $450K"
- `/new-construction/` -> "Entry & Family | Beazer | Energy-efficient floor plans; availability varies by phase" (Beazer has no builder page, so it falls back to the hub)

Also from the village-comparison module (`cp-mod24`): `/builders/toll-brothers/` with anchor "Best for Luxury Buyers ->" and "Browse Inspirada Luxury Collection homes ->", `/builders/lennar/` with "Browse Sunrise Heights homes ->".

From `/las-vegas/skye-canyon/` `cp-mod39`, builders without a `/builders/` page all fall back to `/new-construction/` with the builder name as part of the anchor: "Move-Up & Semi-Custom Shea Homes...", "Family & Move-Up Woodside Homes...", "Family & Move-Up Taylor Morrison...".

From `cp-mod57` ("What Else Should You Read About X?") the anchor is a card:
> "NEW CONSTRUCTION | Las Vegas New Construction Hub | Builders, communities, incentives, and the new-build..."

### 4.3 Links to `/new-construction/` by page

| Page | Links to `/new-construction/` |
|---|---|
| `/las-vegas/skye-canyon/` | 12 |
| `/henderson/cadence/` | 8 |
| `/henderson/macdonald-highlands/` | 8 |
| `/henderson/ascaya/` | 6 |
| `/las-vegas/summerlin-the-ridges/` | 5 |
| `/las-vegas/enterprise/` | 4 |
| `/communities/` | 3 |
| `/las-vegas/summerlin-grand-park/` | 2 |
| `/henderson/inspirada/`, `/las-vegas/mountains-edge/`, `/las-vegas/southern-highlands/`, `/las-vegas/summerlin-stonebridge/`, `/guard-gated-communities/`, `/homes-with-pools/`, `/homes-with-casitas-mother-in-law-suites/` | 1 each |
| `/summerlin/`, `/north-las-vegas/`, and 10 other community pages | **0** |

Interpretation: `/new-construction/` links are **not systematic**. They appear as a fallback when a named builder lacks a `/builders/` page. Communities with lots of unlinked builders (Skye Canyon: Shea, Woodside, Taylor Morrison) link to the hub a lot; communities where every builder has a page link to it zero times. **This is an accidental link pattern, not an architecture.** We should make it deliberate.

### 4.4 Builder-page link volume across the 38 pages

`/builders/lennar/` 31, `/builders/toll-brothers/` 26, `/builders/kb-home/` 14, `/builders/pulte-del-webb/` 14, `/builders/richmond-american/` 12, `/builders/tri-pointe/` 10, `/builders/century-communities/` 9, `/builders/taylor-morrison/` 5, `/builders/dr-horton/` 5, `/builders/woodside/` 2, `/builders/beazer/` 2, `/builders/shea/` 2, `/builders/blue-heron/` 2, `/builders/touchstone/` 1.

### 4.5 Community-to-community linking (four separate mechanisms)

1. **`cp-mod55` "Which Communities Are Within 30 Minutes of X?"** 6 curated cards. Real anchors from Skye Canyon: "View Tule Springs (Villages at) ->" (`/north-las-vegas/tule-springs/`), "View Aliante ->", "View Summerlin West ->" (`/las-vegas/summerlin-west/`), "View Summerlin (full master plan) ->" (`/summerlin/`), "View North Las Vegas (citywide) ->", "View Las Vegas (citywide) ->".
2. **"More communities in this city"** section: a long alphabetical run of sibling links continuing from the current community's letter. From Skye Canyon: `/las-vegas/skye-canyon-boulder-hills/` ("Boulder Hills at Skye Canyon"), `/las-vegas/skye-canyon-ridgeline/`, `/las-vegas/skye-hills/`, `/las-vegas/snowlee-court/`, `/las-vegas/soho-lofts/`, `/las-vegas/south-mountain-at-mountains-edge/`, `/las-vegas/southern-highlands/`, `/las-vegas/southern-highlands-augusta-canyon/`, `/las-vegas/southern-highlands-country-club/`, `/las-vegas/southern-highlands-golf-estates/`, `/las-vegas/southern-highlands-portofino/`, `/las-vegas/southern-highlands-the-estates/`, and closes with "Las Vegas homes for sale" -> `/las-vegas/homes-for-sale/`.
3. **`cp-mod56` A-Z** with `#letter-X` in-page jumps plus "Las Vegas (parent city)".
4. **`cp-mod24` / `cp-mod34`** village cards, which mostly go to `/search/?...` but route sub-neighborhoods to their own pages: `/henderson/inspirada-mesa-del-sol/`, `/henderson/inspirada-nevada-trails/`, `/henderson/lake-las-vegas-south-shore/`, `/henderson/lago-vista-at-lake-las-vegas/`, `/henderson/kalos-at-cadence/`.

**Confirmed: there is a fourth tier of sub-neighborhood pages** under each community, at `/city/<community>-<subneighborhood>/`. Verified 200: `/henderson/inspirada-mesa-del-sol/`.

### 4.6 Community pages link OUT to the lifestyle pages

From `/henderson/seven-hills/` module 7 (the "browse by feature" directory), real anchor text:

- `/luxury-communities/` -> "Double Guard-Gated · Custom Estates | Terracina | $2M-$7M+ | 1 active"
- `/guard-gated-communities/` -> "Gated · Elevated View Lots | The Pinnacle | Semi-custom & custom | 3 active"
- `/55-plus-communities/` -> "55+ · Active Adult | Sun City Anthem (ZIP neighbor) | $400K-$1M | 94 active"
- `/guard-gated-communities/` -> "Gated · Established | MacDonald Ranch / The Canyons (ZIP neighbor)"
- Under the "By Lifestyle" heading: `/guard-gated-communities/` -> "Guard-Gated (Seven Hills proper) 57", `/55-plus-communities/` -> "55+ (Sun City Anthem, ZIP neighbor) 94", `/luxury-communities/` -> "Luxury $2M+ (ZIP-area) 37"

So the lifestyle pages receive links from **inside the community pages' By-Lifestyle directory block**, with live listing counts as part of the anchor text. That is the mechanism we need to replicate.

### 4.7 The tier hierarchy, as built

```
/                                         (home)
└── /communities/                         (tier-3 hub, 580+ communities, 7 directory blocks)
    ├── /summerlin/                       (geo hub, runs the FULL community template)
    ├── /henderson/                       (geo hub)
    ├── /las-vegas/                       (geo hub)
    ├── /north-las-vegas/                 (geo hub, full community template)
    │   └── /henderson/inspirada/         (community page, 49 sections)
    │       └── /henderson/inspirada-mesa-del-sol/   (tier-4 sub-neighborhood)
    ├── /zip/89044/                       (parallel ZIP hub family)
    └── lifestyle filters:
        /guard-gated-communities/  /55-plus-communities/  /golf-communities/
        /luxury-communities/  /high-rise-condos/  /luxury-condos-las-vegas/
        /homes-with-pools/  /homes-with-casitas-mother-in-law-suites/
        /homes-with-rv-garages/  /las-vegas-luxury-homes/
        /recently-reduced-las-vegas/  /open-houses-las-vegas/

/new-construction/                        (single hub)
├── /summerlin/new-construction/          (200 - geo-level NC page EXISTS)
├── /henderson/new-construction/          (200 - geo-level NC page EXISTS)
└── /builders/<slug>/                     (14 builder pages linked from community pages)
```

---

## 5. NEW-CONSTRUCTION ARCHITECTURE (the decision-relevant finding)

**Answer: NRG uses an in-page SECTION, not a separate per-community page. There is no community-level `/x/new-construction/` URL anywhere.**

Probed and confirmed:

| URL | Status |
|---|---|
| `/las-vegas/skye-canyon/new-construction/` | **404** |
| `/henderson/inspirada/new-construction/` | **404** |
| `/henderson/lake-las-vegas/new-construction/` | **404** |
| `/summerlin/new-construction/` | **200** |
| `/henderson/new-construction/` | **200** |

So the pattern is:

- **Geo level (city / master-plan hub): dedicated `/x/new-construction/` page exists.** At least for Summerlin and Henderson.
- **Community level: no dedicated page.** Instead every one of the 24 community pages carries `cp-mod39`, section 26 of 49, titled **"Who Builds New Homes in X?"** (or "Who Builds New Homes in and Around X?" where the builders are adjacent rather than inside the plan).

`cp-mod39` structure, per builder card:
- Segment label ("Luxury & Move-Up", "Family & Mid-Market", "First-Time & Family", "Entry & Family")
- Builder name (the link)
- One-line product description
- **Communities:** which neighborhoods/phases that builder is selling
- **Price Range:** "From $800K"
- Links to `/builders/<slug>/`, or `/new-construction/` if no builder page exists

They also thread new construction through the rest of the page rather than quarantining it:
- `cp-mod32` (down payment Q&A): "New-construction buyers should also budget earnest and design-center deposits, which builders structure differently from resale escrow."
- `cp-mod49` (time to close): "Quick move-in homes can close in 30-60 days, while to-be-built Toll Brothers, Lennar, or Century Communities homes commonly run four to ten months."
- `cp-mod16` (growth): names the active builders and discusses build-out end-state.
- `cp-mod45` (comparison table) has a literal **"New Construction"** row: "Active - 4 national builders" vs "Very High (Inspirada, Cadence)" vs "Moderate" vs "Mostly built out · resale".
- `cp-mod21` (open houses): "builder model homes are open daily across the active phases".
- `cp-faq2` includes "Is Skye Canyon still building new homes?" as a top-5 FAQ.
- Buyer-protection line appears verbatim in `cp-mod39`: "builder sales offices represent the builder, not you, bring your own agent to the first visit; it costs you nothing."

**Recommendation for our architecture:** mirror this. One `/new-construction/` hub, geo-level `/summerlin/new-construction/` and `/henderson/new-construction/` style pages, `/builders/<slug>/` pages, and an in-page new-construction module on each community page. Do NOT build `/community/new-construction/` pages, they would cannibalize the community page and split the topical authority. But unlike NRG, make the community-page module link to the hub **every time**, not just as a builder-page fallback.

---

## 6. DATA BLOCKS AND THE FIELDS WE WOULD NEED TO POPULATE

To build one community page at NRG parity you need roughly **190 discrete data fields per community**. Grouped:

### 6.1 Identity / plan record (from developer or city, ~12 fields)
`community name`, `parent city`, `parent-city slug`, `ZIP code(s)`, `neighborhood/region descriptor` ("northwest Las Vegas at the base of the Spring Mountains"), `master-plan acreage`, `open-space acreage`, `year founded / groundbreaking`, `developer name`, `homes delivered to date`, `build-out status`, `hero image + alt text`.

### 6.2 Market data (LVR/GLVAR, per ZIP, ~22 fields)
`median list price`, `median sold price`, `median days on market`, `DOM 12-month range`, `active listing count`, `closings per month`, `annual closings`, `12-month sold-price band`, `peak month + count`, `competitiveness score 0-100` + label, plus price-band counts and active counts for 6 bands (Under $400K / $400-500K / $500-600K / $600-800K / $800K-$1M / $1M+), plus per-submarket `From $`, `DOM`, `active`, `$ per sq ft` for 4 to 6 submarkets.

### 6.3 Schools (GreatSchools + Nevada Report Card, ~7 fields x 5 to 6 schools)
Per school: `name`, `GreatSchools rating /10`, `type` (Zoned public / Public charter / Private), `grade span`, `enrollment`, `student-teacher ratio`, `neighborhood + drive time`, `"Homes Near" price floor`, `tab category` (Elementary / Middle / High / Private & Charter), `Top Rated` flag. Plus the ranked comparison table (rank + star rendering). They use stock campus photos with an explicit disclaimer, which we can copy to avoid a photo-sourcing problem.

### 6.4 HOA (~6 fields)
`monthly dues range` (low/high), `what the master association funds` (prose list), `whether sub-associations layer on top`, `special assessments` (SID/LID in NV, billed with property taxes, not the HOA statement), `guard-gate status and its dues impact`, `escrow due-diligence checklist` (dues, reserves, transfer fees, special-assessment history). Optionally the `cp-mod30` "HOA Fees by Village Tier" card list: tier name + dues band + what it covers. Present on Lake Las Vegas, absent on Inspirada and Skye Canyon, so it is optional.

### 6.5 Amenities (`cp-mod40`, ~5 fields x 8 amenities)
Per amenity: `proximity badge` (IN-COMMUNITY / AT HOME / ~15 MIN / UP-CORRIDOR), `name`, `size or scale` ("~20 acres", "7,500 sq ft", "Plan-wide"), `activity tags` ("Splash pad · Courts · Trails"), `access` (Residents/public, HOA members, Free, Free/NF fees), `2-sentence description`.

### 6.6 Commute (`cp-mod47`, ~2 fields x 8 destinations + 4 modes)
Per destination: `drive time` ("~20 min", "5-10 min"), `destination name`, `route` ("I-215 -> I-15 north"). Standard destination set: Strip, Harry Reid Airport, nearest mall/errands corridor, a civic venue, the local commercial corridor, a trailhead/outdoor destination, downtown of the parent city, Downtown Las Vegas. Plus 4 transport modes (Driving, RTC Transit, Cycling & Trails, Rideshare), each with an honest 1 to 2 sentence assessment including cost ("airport runs cost roughly $30-$45").

### 6.7 Livability grades (`cp-mod06` + `cp-mod17`, ~14 fields)
Six categories: Safety, Schools, Cost of Living, Amenities, Outdoor Access, Commute. Each gets a **letter grade** (A+/A/A-/B+/B/B-/C+), a **numeric score 0-100**, and a 1 to 2 sentence justification with a named source. Plus an `Overall Livability` composite. Methodology footnote: "6 weighted categories on a 4.0-equivalent scale."

### 6.8 Demographics + growth (`cp-mod16`, ~10 fields)
`parent-city population (Census)`, `2010 / 2020 / current / 2030-projected` series for the bar chart, `median household income`, `income vs county median %`, `median age`, `homeownership rate`. They always disclose that the Census does not tabulate master plans separately and show citywide figures instead.

### 6.9 Economy (`cp-mod12`, ~10 fields)
4 stat tiles (income, income-vs-county, commute-to-jobs time, freeway access) + 5 to 6 `Top Area Employers`, each with name + one-line description.

### 6.10 Comparison table (`cp-mod45`, 9 rows x 4 columns = 36 cells)
Rows: Median List Price, Active Listings, Days on Market, Established, HOA Range, Crime Index, Open Space, New Construction, Best For. Columns: this community, parent city, Las Vegas, one peer community.

### 6.11 Builders (`cp-mod39`, ~5 fields x 3 to 5 builders)
Covered in section 5 above.

### 6.12 E-E-A-T / sourcing (`cp-mod10` + `cp-mod58`, ~10 fields)
`author name + title + license number`, `years in market`, `last reviewed date + reviewer`, `data reviewer`, `last updated`, `next review date`. Plus 9 to 10 named sources with a one-line description of exactly what each supplies and a live outbound link: Las Vegas REALTORS, US Census QuickFacts, the city, Clark County Assessor, NRS 361.471, FBI UCR, BLS, GreatSchools, plus one or two community-specific (NPS, BLM, RTC).

This sourcing discipline is the single most copyable thing on the site. Every number on the page is footnoted to a primary source, and where they cannot source a number they print `n/a*` with an explanation rather than inventing one. That directly matches our own no-fabrication rule.

---

## 7. TAKEAWAYS FOR OUR BUILD

1. **The community page is the product.** ~11,650 words, 40 question-shaped H2s, 18 FAQ entities, 32 schema types, 3 lead forms, ~10 images. Everything else in this tier is a router into it.
2. **Every H2 is a question.** Not one descriptive heading. This is an AI-answer / featured-snippet strategy, reinforced by the four standalone single-question `<section>`s with `aria-label="Question: ..."`.
3. **Copy the template, fix the TOC.** Their biggest miss: no table of contents on an 11k-word page. `/55-plus-communities/` proves they know how (`toc__list` + full anchor spine); they just never applied it to the community template. We should ship a sticky TOC with an id on every one of the 49 sections.
4. **Only 6 anchor ids on an 11k-word page** is the same miss. Give every section a real id.
5. **The IDX teaser is SEO-dead.** 8 skeleton cards, nothing in server HTML. Their lifestyle pages server-render full listing cards. If we can only server-render one, do it on the community pages.
6. **Their free-text MLS filtering leaks badly.** A Pahrump listing showed up in the "Las Vegas guard-gated" feed. Curate a subdivision whitelist per filter page.
7. **They redirect bare slugs but still internally link to them.** Hundreds of internal links eating a 308. Link to canonicals directly.
8. **New construction: in-page module, not a sub-page, at community level. Dedicated page at geo level.** Adopt this, but make the hub link systematic.
9. **Honest-scoping copy is a trust asset.** They repeatedly say "these are ZIP-area figures, not plan-only" and print `n/a*` rather than guessing. Adopt wholesale.
10. **No em-dash note for our version:** NRG's copy is saturated with em-dashes. Our workspace rule bans them. Rewrite, do not lift.

---

*Raw HTML for all 38 pages retained at `/private/tmp/claude-501/.../scratchpad/nrg/` for the duration of this session.*
