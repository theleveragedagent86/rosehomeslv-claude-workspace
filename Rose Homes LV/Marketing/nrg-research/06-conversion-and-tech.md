# NREG Teardown 06 — Conversion / Utility Pages + Technical Implementation

Source: https://www.nevadarealestategroup.com/
Research date: 2026-07-25 (site data timestamped "Last refresh: Jul 26, 2026")
Agent F. All findings pulled from raw HTML, the compiled CSS chunks, and the client JS bundles.

---

# PART 1 — Conversion & Utility Page Layer

## 1.1 Master table

All 18 target URLs returned **HTTP 200. Zero 404s.**
Site uses `trailingSlash: true`, so every URL is `/path/` with a trailing slash.

| # | URL | Status | H1 | Meta title | Words | Page type | TOC | Primary conversion action |
|---|---|---|---|---|---|---|---|---|
| 1 | `/search/` | 200 | New listings for sale in Las Vegas Metro | Las Vegas Homes for Sale — MLS Search \| Nevada Real Estate Group | 3,075 | **IDX search** (SSR results + client filter bar) | No | Browse → click listing → hit 3-view registration wall → name/email/phone capture |
| 2 | `/search/?view=map` | 200 | (same) | (same, `noindex`) | 3,075 | **IDX search, map mode** (MapLibre GL) | No | Same as above; map is a `data-view="map"` variant of the same route |
| 3 | `/buyers/` | 200 | How to Buy a Home in Las Vegas | Buy a Home in Nevada \| Las Vegas Buyer Guide · NREG | 4,226 | **Long-form pillar guide + hub** | Yes (8 items) | Buyer lead form (`/api/leads/buyer/`) + 3 "starting point" cards routing to search / pre-approval / agent |
| 4 | `/buyers/first-time-buyers/` | 200 | Buying Your First Las Vegas Home — A 2026 Playbook | First Time Home Buyers Guide Las Vegas Nevada 2026 \| NREG | 3,384 | **Long-form guide** | Yes | Buyer form with `needsLender` checkbox → lender handoff |
| 5 | `/buyers/mortgage-calculator/` | 200 | Nevada Mortgage Calculator | Nevada Mortgage Calculator \| Estimate Your Payment \| NREG | 3,098 | **Tool + long-form guide wrapper** | Yes | "Get Real Numbers from a Real Lender" → buyer form w/ `needsLender` |
| 6 | `/buyers/personalized-home-search/` | 200 | Never Miss the Perfect Las Vegas Home | Las Vegas Listing Alerts \| Personalized Home Search \| NREG | 3,208 | **Form landing page + guide** | Yes | Listing-alert signup (saved search) — positioned against Zillow/Realtor.com |
| 7 | `/mortgage-pre-approval-request/` | 200 | Get Pre-Approved for Your Next Home | Get Pre-Approved — Free Nevada Mortgage Pre-Approval \| NREG | 1,508 | **Pure form landing page** | No | Pre-approval request form. Only 1 H2 on the page (the universal footer CTA) |
| 8 | `/compare-listings/` | 200 | Your comparison is empty. | Compare Las Vegas Listings \| NREG | 1,382 | **Utility tool** (`noindex`) | No | Side-by-side compare. Empty-state page; populated via `?ids=<mls,mls>` |
| 9 | `/market-report/` | 200 | Nevada Real Estate Market Reports | Nevada Market Reports — Live MLS Data by City & ZIP 2026 | 1,524 | **Directory / index page** | No | Click through to 20 city reports + 60 ZIP reports; footer lead form |
| 10 | `/home-value-estimator/` | 200 | What's my home worth? | Nevada Home Value Estimator — Free Comp-Based Estimate \| NREG | 2,076 | **Tool (seller lead magnet)** | No | ZIP/beds/sqft → instant comp-based range → "request a free CMA" |
| 11 | `/sellers/` | 200 | Sell Your Las Vegas Home for Top Dollar | Sell Your Las Vegas Home in 21 Days \| NREG · LPT | 4,118 | **Long-form pillar guide + hub** | Yes | Home-valuation form → `/api/leads/seller-valuation/` (the only page with its own endpoint) |
| 12 | `/sellers/7-day-listing-agreement/` | 200 | The 7-Day Listing Agreement | 7-Day Listing Agreement \| Cancel Anytime \| NREG | 2,599 | **Offer / positioning landing page** | Yes | "Ready to List Your Home?" → listing consult |
| 13 | `/moving-to-las-vegas/` | 200 | Moving to Las Vegas in 2026: your complete relocation guide. | Moving to Las Vegas 2026 \| Relocation Guide & Free Consult | 5,188 | **Long-form pillar guide** | Yes (11 items) | Free relocation consult form + embedded CA→NV tax calculator |
| 14 | `/relocation-guide/` | 200 | Your Las Vegas Relocation Guide — Move-In Day in 30 Days | Las Vegas Relocation Guide: 12-Step Playbook \| NREG | 4,047 | **Tactical checklist guide** | Yes | "Get Your Personalized Las Vegas Relocation Plan" form |
| 15 | `/california-tax-savings/` | 200 | California to Nevada Tax Savings Calculator | California to Nevada Tax Savings Calculator 2026 \| NREG | 2,355 | **Interactive calculator** | No | Calculator → "Ready to make the move?" form |
| 16 | `/nellis-afb-relocation-guide/` | 200 | Nellis AFB Relocation Guide 2026 | Nellis AFB Relocation Guide 2026 \| Homes, BAH & PCS | 6,150 | **Niche long-form guide (military)** | Yes | "Get Your Nellis AFB PCS Plan" form |
| 17 | `/reno/` | 200 | Reno Homes For Sale | Reno, Nevada Real Estate: Homes for Sale & Community Guide | **11,886** | **Mega regional hub** (41 H2s, 3 forms) | No | 3 forms: listing alerts, "Talk to a Reno specialist", universal footer |
| 18 | `/about/` | 200 | Nevada's #1 Real Estate Team | About Nevada Real Estate Group — Nevada's #1 Team | 3,559 | **Trust / authority page** | Yes | Universal footer form; heavy proof stacking (RealTrends, 9,061 reviews) |

Bonus (deep-dived for Part 2): `/property/4360-conough-lane-las-vegas-nv-89129-2800048/` — 200, H1 "4360 Conough Lane", 3,234 words, `noindex, follow`.

### Word-count distribution
- Utility/tool pages: 1,382–2,599 words
- Guide pages: 3,000–6,150 words
- Regional mega hub (`/reno/`): 11,886 words

### TOC pattern
10 of 19 pages carry a TOC. Every one is `<nav aria-label="Table of contents">` with an `<h2>On This Page</h2>` and an `<ol>` of pure `#anchor` links. **No JS scroll-spy on guide pages** — it is a plain jump-link block. Two variants exist:
- **Inline-styled variant** (`/buyers/`, `/sellers/`, `/mortgage-calculator/`, `/first-time-buyers/`, `/personalized-home-search/`, `/7-day-listing-agreement/`, `/relocation-guide/`, `/about/`) — all styles inline on the element.
- **Class-based variant** `nav.toc > h2.toc__title + ol.toc__list` (`/moving-to-las-vegas/`, `/nellis-afb-relocation-guide/`) — this is the one that becomes sticky on community pages (see §2.5).

Every section the TOC links to carries `scroll-margin-top: 96px` so anchors clear the 72px sticky nav.

### The universal conversion footer (on 100% of pages)
Every single page ends with the same block: `H2 "Ready to make your move?"` wrapping `<form class="ccm__form" action="/api/leads/buyer/" method="POST">`.

Fields: `firstName`, `lastName`, `email`, `phone`, `timeline` (select), hidden `source`, plus a honeypot `<input name="website">` positioned off-screen at `left:-9999px`.

Timeline options (this is the lead-scoring mechanism):
```
0–3 months — ready to buy
3–6 months — actively looking
6–12 months — researching
12+ months — just exploring
I'm selling, not buying
```
Submit button: `Send →`. Beneath it: `or call (702) 637-1759`, then a trust bar:
> ★★★★★ 9,061+ Reviews · #1 Team in Nevada · 9,600+ Homes Sold · No spam · Reply in 1 hr

Then a full TCPA/SMS consent paragraph naming NREG, Chris Nevada, and LPT Realty (brokerage of record), with "reply STOP to opt out" and "Consent is not a condition of any purchase". Closing line: "⚖ Equal Housing Opportunity · Typical response time: under 30 minutes during business hours (Mon–Sun 8a–8p PT)".

Two phone numbers run site-wide: `+1-702-637-1759` (Southern NV) and `+1-775-277-2120` (Northern NV).

### Lead API endpoints (all discovered)
```
/api/leads/buyer/              ← universal footer form, most page forms
/api/leads/seller-valuation/   ← /sellers/ CMA form only
/api/leads/listing-inquiry/    ← property detail page (tour / email agent)
/api/leads/community/          ← community landing pages
/api/registration/view/        ← metered listing-view tracking
/api/registration/deferred/    ← registration-wall fallback submit
/api/register-login/           ← returning-user login
/api/engage/identify/          ← visitor identification
/api/engage/phone/             ← phone reveal tracking
/api/agent/session             ← detects logged-in NREG agent (bypasses wall)
/api/agent-context             ← AI assistant context
/api/broadcast                 ← Supabase Realtime (Phoenix channels)
/api/track                     ← generic event → dataLayer
```

---

## 1.2 Deep dive: `/buyers/`

4,226 words · 17 H2s · 2 forms · `index, follow` · TOC yes · FAQPage schema with 8 questions.

**Full section outline (document order):**

1. **Hero** — H1 "How to Buy a Home in Las Vegas". Above the TOC there is a "key facts" bullet strip (`›` gold chevron bullets) summarizing the page — an AI-overview / featured-snippet play.
2. **`<nav>` Table of contents** — "On This Page", 8 anchors, 2-col auto-fit grid (`repeat(auto-fit, minmax(200px,1fr))`), cream background, 3px gold left border.
3. **`#paths` — "Where Are You in the Buying Process?"** — 3-card router, each card an `<a>` with a 3px gold top border, opening in a new tab:
   - H3 Browse homes for sale → `/search/?city=Las+Vegas`
   - H3 Get pre-approved → `/mortgage-pre-approval-request/`
   - H3 Talk to an agent → contact
4. **`#market-snapshot` — "What Is the Las Vegas Buyer Market in 2026?"** — live-ish market stats.
5. **`#buying-process` — "How Does the Home Buying Process Work in Nevada?"** — 6 H3 sub-steps, each phrased as a question:
   - How Do You Choose the Right Buyer's Agent?
   - Why Do You Need Mortgage Pre-Approval Before Searching?
   - How Should You Browse Las Vegas Listings?
   - How Do You Make a Competitive Offer in Las Vegas?
   - What Happens During Inspection and Due Diligence?
   - What Should You Expect at Closing in Nevada?
6. **`#what-buyers-spend` — "What Do Nevada Buyers Spend on a Home?"**
7. **`#whats-different` — "What's Different About Buying in Nevada?"**
8. **"Which Type of Las Vegas Buyer Are You?"** — segment router, 4 H2-level blocks: First-Time Buyers / Relocation Buyers / Investor Buyers / Luxury Buyers ($1M+). Each links to its own dedicated page.
9. **"Find the right Las Vegas neighborhood"** — 4 H3 cards: Best for Families / Retirees / Young Professionals / Luxury Buyers.
10. **`#tools` — "Start Your Las Vegas Home Search"** — buyer tool grid.
11. **`#lead-form`** — the primary conversion form. Fields: `firstName`, `lastName`, `email`, `phone`, plus a **`needsLender` checkbox** and hidden `source="/buyers"`. Bordered white card with `box-shadow: var(--shadow-md)`. Submit: "Submit".
12. **`#faq` — "Frequently Asked Questions About Buying a Home in Nevada"** — 8 Q&As, emitted as `FAQPage` JSON-LD.
13. **"Ready to Find Your Nevada Home?"** — mid CTA band.
14. **"Articles for home buyers"** — 3 related blog cards (internal-link farm).
15. **"Ready to make your move?"** — universal `ccm__form` footer.

**Takeaway for Rose Homes LV:** the structure is *router first, education second, form third*. The three "where are you in the process" cards appear before any long prose, so a ready-to-transact visitor converts in one click and a researcher gets the 4,000 words.

---

## 1.3 Deep dive: `/moving-to-las-vegas/`

5,188 words · 16 H2s · 2 forms · TOC yes (11 items, the `nav.toc` class variant) · FAQPage with 10 questions.

**Full section outline:**

1. **Hero** — H1 "Moving to Las Vegas in 2026: your complete relocation guide."
2. **Intro paragraph with dense internal links** — links out to `/relocation-guide/` (12-step checklist), `/moving-to-las-vegas/from-texas/`, `/las-vegas-area-code/`. All inline links styled `color: var(--gold-text); text-decoration: underline`.
3. **`nav.toc` — "On This Page"**, 11 numbered anchors.
4. **`#six-reasons` — "Why are people moving from California to Las Vegas in 2026?"** — cites US Census ACS with an outbound `rel="noopener noreferrer"` link. 6 H3 benefit cards in an auto-fit grid:
   - Zero State Income Tax
   - 3% Property Tax Cap
   - Lower Cost of Luxury
   - No Estate Tax
   - No Corporate Income Tax
   - Homestead Protection
5. **`#tax-savings` — "What does Nevada residency actually save you?"**
6. **"California → Nevada Tax Savings"** — a **live interactive calculator embedded mid-page** (inputs `filing` radio + income). Same component as `/california-tax-savings/`.
7. **`#cost-of-living` — "How does Las Vegas cost of living compare to LA, SF, Seattle, and New York?"** — comparison table.
8. **`#neighborhoods` — "Which Las Vegas neighborhoods are best for relocators?"** — 6 H3 "or" pairs (deliberately a decision aid, not a list):
   - Summerlin or Henderson
   - The Ridges or MacDonald Highlands
   - Sun City Anthem or Sun City Summerlin
   - Lake Las Vegas or Strip high-rises
   - North Las Vegas or Mountains Edge
   - Ascaya or Summerlin custom lots
9. **`#timeline` — "How long does it take to move to Las Vegas?"** — 5 H3 phases: Financial planning / In-person tour trip / Offer + escrow / Move + close / Residency setup.
10. **`#surprises` — "What surprises new Las Vegas residents most?"**
11. **`#summerlin-vs-henderson` — "What's the difference between Summerlin and Henderson?"**
12. **`#hidden-costs` — "What hidden costs should you budget for moving to Las Vegas?"**
13. **`#resources` — "Read before you move"** — 7 H3 blog cards (the biggest internal-link block on the page).
14. **`#consult` — "Get a personalized Las Vegas relocation plan"** — conversion form.
15. **`#faq` — "Frequently Asked Questions"** — 10 H3 questions, all in FAQPage schema.
16. **"Ready to make Nevada home?"** — CTA band.
17. **"Las Vegas relocation articles"** — 3 more blog cards.
18. **"Ready to make your move?"** — universal footer form.

**Takeaway:** this page is the template for a relocation pillar. Note the double blog-card block (one mid-page at `#resources`, one at the bottom) and the calculator embedded *inside* the narrative rather than living only on its own URL.

---

## 1.4 Deep dive: `/market-report/`

1,524 words · only 3 H2s · 1 form · `index, follow` · **no TOC** · no FAQ schema.

This is deliberately a **thin directory / index page**, not a content page. Its whole job is to distribute crawl equity and clicks to 84 child report pages.

**Full section outline:**

1. **H1** "Nevada Real Estate Market Reports"
2. **Sub-deck** (the only real prose):
   > "Real Nevada market data with 12-month trend graphs — median price, days on market, and closed sales — pulled from the MLS through Repliers IDX and refreshed daily. Pick a city or community below, or browse every ZIP code across the valley plus Pahrump."
3. **CTA link:** "Browse all 60 ZIP-code reports →" → `/market-report/zip/...`
4. **H2 "Southern Nevada"** — 10 cards, each labeled *City report* or *Community report*:
   - Las Vegas, Henderson, North Las Vegas, Boulder City, Pahrump, Mesquite (city reports)
   - Summerlin, Green Valley, Mountains Edge, Lake Las Vegas (community reports)
5. **H2 "Northern Nevada"** — 10 cards:
   - Reno, Sparks, Carson City, Minden, Gardnerville, Fallon, Dayton, Fernley, Incline Village (city reports)
   - Lake Tahoe (community report)
6. **Closing line** with dual phone numbers:
   > "Every city report shows live median price, days on market, closed sales, and a 12-month trend. For a personal, address-specific analysis of your home, get in touch or call (702) 637-1759 in the south / (775) 277-2120 in the north."
7. **"Ready to make your move?"** — universal footer form.

**URL patterns underneath:**
```
/market-report/cities/<slug>/     ← 20 city + community reports
/market-report/zip/<zip>/         ← 60 ZIP reports (61 /zip/ URLs in sitemap)
```
Sitemap counts 84 URLs under `/market-report`.

**Takeaway:** a market-report hub does not need to be long. 1,500 words and a clean two-region card grid is enough, because the SEO value lives in the 84 child pages.

---

## 1.5 The registration wall (the real conversion engine)

Found in `js/0_u._m-mmdh9..js`. This is the single most important conversion mechanic on the site and it is not visible in the HTML.

**How it works:**
- Every listing detail view calls `meterListingView(mls)`.
- Unique MLS numbers viewed are stored in `localStorage` under `nreg_viewed_listings` (capped to the last 100), and mirrored to a 30-day cookie `nreg_vc`.
- Each view also fires `POST /api/registration/view/` with `{ mls, anonId }` using `keepalive: true`.
- Threshold: **3 free listing views** (`NEXT_PUBLIC_FREE_VIEWS_ORGANIC ?? 3`, `NEXT_PUBLIC_FREE_VIEWS_PAID ?? 3`, paid floored at 1). Paid vs organic is read from a traffic-source cookie with a `PAID_ATTRIBUTION_WINDOW_DAYS: 30` window.
- On the 4th unique listing, `walled: true` fires a modal. GA event `gate_wall_shown` with `traffic_source` + `threshold`.
- The modal has a `"teaser"` state before the full `"register"` state.
- Bypass conditions: cookie `nreg_ml=1` (member logged in), or `GET /api/agent/session` returning an `agent` (NREG's own agents don't get walled). Result cached in `sessionStorage` as `nreg_gate_agent`.
- Registration submits name / email / phone to `/api/registration/deferred/` with `trafficSource`, `firstUtm`, `registeredListingMls`, `anonId`. Success fires `gate_registration_completed`.
- Optional OTP step: `NEXT_PUBLIC_OTP_TRIGGER ?? "registration"`. The consent copy states the phone number **is the account sign-in**.
- First-touch UTM is preserved in `sessionStorage` (`FIRST_UTM`) so the lead record carries original attribution, not last-click.

**Compare cart** (same layer): `localStorage` key `nreg.compareCart.v1`, **max 4 listings**, custom event `nreg-compare-cart-change`, and `compareUrl()` builds `/compare-listings?ids=<mls,mls,mls>`.

---

# PART 2 — Technical Implementation

## 2.a The IDX provider — how listings are actually delivered

### Verdict: **Repliers API, consumed server-side by a custom Next.js app. There is no third-party IDX widget, no iframe, and no client-side listing fetch.**

This is the single most important finding for the rebuild: **there is nothing here you can swap a Lofty IDX embed into.** The listing markup is NREG's own React components, server-rendered from the Repliers REST API at build/ISR time.

### Evidence

**1. Image CDN is Repliers, proxied through the Next.js image optimizer:**
```
https://cdn.repliers.io/lasvegas/IMG-2803023_13098538367214474338.jpg?class=large
```
served as
```
/_next/image/?url=https%3A%2F%2Fcdn.repliers.io%2Flasvegas%2FIMG-...jpg%3Fclass%3Dlarge&w=1920&q=75
```
The `lasvegas` path segment is the Repliers board/tenant slug.

**2. A build-time warning string left in the bundle** (`js/07rv_s7-pd5t7.js`) names the integration outright:
```js
console.warn(`[repliers] build-time MLS fetches skipped (${a?"SANDBOX_MODE":"SKIP_BUILD_MLS default"}) — pages build with fallback markup; ISR fills real data at runtime. Set BUILD_FETCH_MLS=1 to re-enable build fetching.`)
```
Env flags: `SKIP_BUILD_MLS`, `BUILD_FETCH_MLS`, `SANDBOX_MODE`, plus `VERCEL_BUILDING` / `CI` / `NEXT_PHASE` guards.

**3. Repliers' JSON object shape is used verbatim** in the map-marker code (`js/0qz8kfyz.7nbg.js`):
```js
let h = n.images?.[0] ? `https://cdn.repliers.io/${n.images[0].replace(/^\/+/,"")}?class=medium` : "/images/hero/homepage-hero.jpg",
    p = n.details?.numBedrooms ?? 0,
    d = (Number(n.details?.numBathrooms)||0) + .5*(Number(n.details?.numBathroomsHalf)||0)
```
`details.numBedrooms` / `numBathrooms` / `numBathroomsHalf` / `mlsNumber` / `images[]` are all Repliers API fields.

**4. The sort dropdown exposes Repliers' `sortBy` enum directly:**
```
priceAsc · priceDsc · createdOnDesc · createdOnAsc · updatedOnDesc · daysOnMarketAsc · daysOnMarketDesc · sqftDesc
```
(`priceDsc` — Repliers' own misspelling of "desc" — is a fingerprint.)

**5. `repliersUpdatedOn` appears 24 times in the search HTML** (once per card), i.e. the raw Repliers timestamp field is carried into the render.

**6. The API base URL and key are NOT in any client bundle.** No `api.repliers.io`, no `REPLIERS_*` env var reaches the browser. All MLS calls happen in React Server Components / route handlers on Vercel. Good security posture, and the reason none of this is reproducible by copying markup.

**7. Rendering is verifiably server-side.** Changing query params changes the *server HTML*:

| URL | H1 (from SSR HTML) | Result count | Cards in HTML |
|---|---|---|---|
| `/search/` | New listings for sale in Las Vegas Metro | 13,561 | 24 |
| `/search/?city=Henderson&minPrice=500000` | Homes for sale in Henderson, NV | 2,231 | 24 |
| `/search/?view=map` | New listings for sale in Las Vegas Metro | 13,561 | 24 |

**8. The MLS is GLVAR.** Site-wide disclaimer, verbatim:
> Information deemed reliable but not guaranteed. The data relating to real estate for sale on this website appears in part through the Greater Las Vegas Association of REALTORS® (GLVAR) MLS Internet Data Exchange (IDX) program. All listing data is provided by participating IDX brokerages and is for the personal, non-commercial use of consumers identifying prospective properties to purchase. Listing brokerages and their associates are noted next to each listing. Property information is refreshed regularly; the broker is not responsible for any typographical errors, misinformation, misprints, and shall be held totally harmless from any damages arising from reliance upon this data. Last refresh: Jul 26, 2026.

Rendered as `<section class="search-mls-attribution" role="contentinfo" aria-label="MLS data disclaimer">`.

`/market-report/` states it plainly: *"pulled from the MLS through Repliers IDX and refreshed daily."*
`/home-value-estimator/` states: *"Live Nevada MLS data via Repliers IDX."*

### The exact container markup (what a Lofty embed would replace)

Full nesting on `/search/`:

```html
<div id="main-content" tabindex="-1">
  <main class="nreg-search-page" data-view="list">          <!-- data-view="list" | "map" -->

    <!-- React Suspense boundary: the filter bar is a CLIENT component, streamed in -->
    <!--$?--><template id="B:0"></template>
      <div class="search-filters-skeleton" aria-hidden="true"></div>
    <!--/$-->
    <!--$?--><template id="B:1"></template><!--/$-->

    <div class="results-header" data-pending="false">
      <div class="container">
        <div class="results-header-row">
          <div class="results-count">
            <span>Showing <strong>1–24</strong> of <strong>13,561</strong></span>
          </div>
          <div class="results-actions">
            <div class="view-toggle" role="group" aria-label="View" data-pending="false">
              <button type="button" class="view-toggle-btn" data-active="true"  aria-pressed="true">▦ List</button>
              <button type="button" class="view-toggle-btn" data-active="false" aria-pressed="false">◉ Map</button>
            </div>
            <button type="button" class="save-search-btn">🔔 Save this search</button>
            <label class="results-sort">
              <span class="visually-hidden">Sort</span>
              <select aria-label="Sort listings by">…8 options…</select>
            </label>
          </div>
        </div>
      </div>
    </div>

    <section class="search-results-section"
             data-instant-pending="false"
             style="transition:opacity 120ms ease"
             aria-busy="false">
      <div class="container">
        <ul class="listing-grid" role="list">
          <li><article id="listing-card-2803023" data-mls="2803023" class="search-listing-card is-spotlight">…</article></li>
          <!-- ×24 -->
        </ul>
        <nav class="search-pagination" aria-label="Pagination" data-pending="false">
          <button type="button" disabled class="page-btn">← Prev</button>
          <button type="button" class="page-btn" data-current="true" aria-current="page">1</button>
          <button type="button" class="page-btn" data-current="false">2</button>
          <button type="button" class="page-btn" data-current="false">3</button>
          <span class="page-ellipsis" aria-hidden="true">…</span>
          <button type="button" class="page-btn" data-current="false">566</button>
          <button type="button" class="page-btn">Next →</button>
        </nav>
      </div>
    </section>

    <section class="search-mls-attribution" role="contentinfo" aria-label="MLS data disclaimer">…</section>
  </main>
</div>
```

**Data attributes to note:** `data-view`, `data-pending`, `data-instant-pending`, `data-active`, `data-current`, `data-mls`, `aria-busy`. The `data-pending` / `aria-busy` pair drives an opacity transition during filter changes so results dim instead of flashing.

### Full listing-card markup

```html
<article id="listing-card-2803023" data-mls="2803023" class="search-listing-card is-spotlight">

  <div class="search-card-image">
    <img alt="7731 W Diablo Drive — Las Vegas"
         decoding="async" data-nimg="fill" loading="lazy"
         sizes="(max-width: 600px) 100vw, (max-width: 900px) 50vw, (max-width: 1440px) 33vw, 25vw"
         srcSet="/_next/image/?url=https%3A%2F%2Fcdn.repliers.io%2F…&w=256&q=75 256w, …1920w"
         src="/_next/image/?url=https%3A%2F%2Fcdn.repliers.io%2F…&w=1920&q=75"
         style="position:absolute;height:100%;width:100%;left:0;top:0;right:0;bottom:0;object-fit:cover;color:transparent"/>

    <button type="button" class="card-photo-arrow card-photo-arrow-prev" aria-label="Previous photo">…</button>
    <button type="button" class="card-photo-arrow card-photo-arrow-next" aria-label="Next photo">…</button>

    <div class="card-photo-dots" aria-hidden="true">
      <button type="button" class="card-photo-dot is-active" aria-label="Photo 1 of 5"></button>
      …
    </div>

    <div class="search-card-badges">
      <span class="search-card-badge badge-new">NEW</span>
    </div>
    <span class="search-card-spotlight" aria-label="Spotlight listing (Chris Nevada / LPT Realty)">★ SPOTLIGHT</span>
    <span class="search-card-photocount" aria-hidden="true">📷 34</span>
    <button type="button" class="card-save-heart" aria-label="Save this listing">…</button>
  </div>

  <div class="search-card-body">
    <div class="search-card-price-row">
      <div class="search-card-price-left">
        <span class="search-card-price">$470,000</span>
      </div>
      <span class="search-card-proptype" aria-label="Property type: House">
        <span class="proptype-dot" aria-hidden="true"></span>House
      </span>
    </div>

    <div class="search-card-monthly"
         title="Estimated PITI — 20% down, 6.00% APR, 30-year fixed, taxes and insurance included">
      Est. $2,654/mo
    </div>

    <div class="search-card-statblock">
      <div class="stat-cell"><svg class="lucide lucide-bed-double stat-icon"/><span class="stat-text"><strong class="stat-num">3</strong> Beds</span></div>
      <div class="stat-cell"><svg class="lucide lucide-bath stat-icon"/><span class="stat-text"><strong class="stat-num">3.5</strong> Baths</span></div>
      <div class="stat-cell"><svg class="lucide lucide-ruler stat-icon"/>
        <div class="stat-text stat-text-stack">
          <span><strong class="stat-num">1,622</strong> Sq. Ft.</span>
          <span class="stat-text-muted"><strong class="stat-num">0.09</strong> Acres</span>
        </div>
      </div>
      <div class="stat-cell"><svg class="lucide lucide-house stat-icon"/><span class="stat-text">Built in <strong class="stat-num">2018</strong></span></div>
    </div>

    <div class="search-card-address-row">
      <div class="search-card-address-block">
        <div class="search-card-address">7731 W Diablo Drive</div>
        <div class="search-card-city">Las Vegas, NV, 89113</div>
        <div class="search-card-subdivision">Aragon Phase 3</div>
      </div>
      <button type="button" class="card-email-btn">Email Agent</button>
    </div>

    <button type="button" class="card-tour-btn">Tour this home</button>
  </div>

  <div class="search-card-footer">
    <span class="search-card-mls">MLS #2803023 · Listed today</span>
    <span class="search-card-brokerage">Listing courtesy of LPT Realty, LLC</span>
  </div>

  <a class="search-card-stretched-link" aria-label="7731 W Diablo Drive, $470,000"
     href="/property/7731-w-diablo-drive-las-vegas-nv-89113-2803023/">
    <span class="sr-only">View 7731 W Diablo Drive, Las Vegas, NV, 89113 — $470,000</span>
  </a>
</article>
```

Design details worth copying regardless of IDX provider:
- **Est. monthly payment on the card** (`Est. $2,654/mo`) with the assumption set in the `title` attribute — 20% down, 6.00% APR, 30-yr fixed, PITI.
- **Lot acreage stacked under sqft** in the same stat cell.
- **Subdivision name** as a third address line.
- **`is-spotlight` modifier** puts the team's own listings ahead visually — "★ SPOTLIGHT" with an aria-label disclosing it is a Chris Nevada / LPT Realty listing.
- **Stretched link** pattern: the whole card is clickable via one absolutely-positioned `<a>`, which keeps the inner buttons (save, email, tour, photo arrows) individually focusable and keyboard-accessible.
- Icons are **Lucide** inline SVG (`class="lucide lucide-bed-double"`), not an icon font.

### Listing card + grid CSS (real values)

```css
.listing-grid{
  display:grid;
  grid-template-columns:minmax(0,1fr);
  gap:12px;margin:0;padding:0;list-style:none
}
/* responsive steps */
@media(min-width:…){ .listing-grid{grid-template-columns:repeat(2,minmax(0,1fr))} }
@media(min-width:…){ .listing-grid{grid-template-columns:repeat(3,minmax(0,1fr))} }
@media(min-width:…){ .listing-grid{grid-template-columns:repeat(4,minmax(0,1fr))} }

.search-listing-card{
  position:relative;display:flex;flex-direction:column;overflow:hidden;
  background:var(--white);color:inherit;text-decoration:none;
  border:1px solid #00000012;border-radius:8px;
  contain:layout;
  transition:transform .15s, box-shadow .15s, border-color .15s
}
.search-listing-card:hover,.search-listing-card.is-hovered{
  border-color:#0000001a;
  transform:translateY(-2px);
  box-shadow:0 10px 28px #0000001a
}
.search-listing-card:hover .card-photo-arrow,
.search-listing-card:focus-within .card-photo-arrow{opacity:1}

.search-card-image{position:relative;width:100%;aspect-ratio:4/3;background:#0000000a}
.search-card-image .card-photo-arrow{
  position:absolute;top:50%;transform:translateY(-50%);
  z-index:2;width:32px;height:32px;
  display:inline-flex;align-items:center;justify-content:center;
  opacity:0;background:#ffffffeb;border:0;border-radius:999px;
  color:var(--navy,#1b2a4a);cursor:pointer;
  box-shadow:0 2px 10px #0000002e;
  transition:opacity .15s, transform .15s, background .15s
}
.search-card-body{padding:12px 14px 6px}
.search-card-price{
  font-family:var(--font-mulish),sans-serif;
  font-size:28px;font-weight:700;line-height:1.1;
  letter-spacing:-.01em;color:var(--navy)
}
```

Search page shell:
```css
.nreg-search-page{
  background:var(--cream,#faf8f5);min-height:100vh;
  font-family:var(--font-mulish),"Inter",system-ui,-apple-system,sans-serif
}
.search-filters{
  position:sticky;top:var(--nav-h,72px);z-index:30;
  background:var(--white,#fff);border-bottom:1px solid #00000014;padding:16px 0;
  box-shadow:0 1px #0000000a, 0 8px 18px -16px #0000002e;
  transition:opacity .2s, box-shadow .2s
}
.search-filters-skeleton{border-bottom:1px solid #00000014;min-height:200px}
@media(max-width:…){ .search-filters-skeleton{min-height:260px} }
@media(max-width:…){ .search-filters-skeleton{min-height:304px} }
.results-header{background:var(--cream,#faf8f5);border-bottom:1px solid #0000000d;padding:18px 0;transition:opacity .2s}
.search-results-section{padding:32px 0 56px}
.view-toggle{display:inline-flex;overflow:hidden;background:var(--white);border:1px solid #0000001f;border-radius:6px;transition:opacity .2s}
.save-search-btn{background:var(--gold,#c9a96e);color:var(--white);border:0;border-radius:6px;padding:8px 16px;font-size:13px;font-weight:600;cursor:pointer;transition:filter .15s}
```

### Map view
- **MapLibre GL JS** (`.maplibregl-map`, `new s.Map({...})`, `NavigationControl({showCompass:false})`), lazy-loaded via dynamic `import()` and gated behind an `IntersectionObserver` with `rootMargin: "200px"` so the map bundle only downloads when scrolled near.
- **Tiles: MapTiler.** `https://api.maptiler.com/maps/${styleName}/style.json?key=<public key>` — the key is exposed client-side (normal for MapTiler, but note it is a billable public key).
- Style switcher (`.ldp-map-styletabs`) with "street" mapped to MapTiler's `map` style; minor/street/service/tertiary road lines are recolored to `#B9B9B9` at runtime and text halos widened to `1.6` — a deliberate desaturation so listing pins pop.
- Markers dispatch hover events (`dispatchHover(mlsNumber,"map")`) that cross-highlight the matching card via `.search-listing-card.is-hovered`.

### Implication for the Rose Homes LV rebuild

You cannot replicate this by pasting an embed. Two realistic paths:

1. **Lofty IDX (their native search).** You keep Lofty's markup and lose all of the above: spotlight ordering, est. monthly payment on card, subdivision line, acreage stacking, compare cart, and the 3-view registration wall (Lofty has its own forced-registration, configurable, but not this exact metering). Accept Lofty's card and spend the effort on the *content* pages instead, which is where NREG's actual SEO moat is.
2. **Match NREG's architecture.** Requires a Repliers (or equivalent GLVAR IDX/RETS) data licence plus a Next.js app on Vercel. That is a build project, not a page project.

**Recommended:** path 1 for `/search/`, and rebuild the *guide/tool/hub* layer (Part 1) in Lofty landing pages, since none of that layer depends on IDX at all. See `08-lofty-porting-constraints.md`.

---

## 2.b Property detail page template

Example: `/property/4360-conough-lane-las-vegas-nv-89129-2800048/`

### URL slug pattern
```
/property/<street-address-slug>-<city-slug>-<state>-<zip>-<mlsNumber>/
```
e.g. `4360-conough-lane` + `las-vegas` + `nv` + `89129` + `2800048`.
The canonical is the full slug, but the JSON-LD `@id`/`url` use the short form `/property/<mls>` — so a short URL almost certainly 301s to the full slug.

### Indexing posture — the key strategic decision
```html
<meta name="robots" content="noindex, follow"/>
<link rel="canonical" href="https://www.nevadarealestategroup.com/property/4360-conough-lane-las-vegas-nv-89129-2800048/"/>
```
`/property/` URLs appear **0 times in sitemap.xml**. Their own robots.txt explains the reasoning at length (see §2.f) — they used to robots-block these, Google indexed ~643 of them anyway from backlinks, and the only fix was to *allow* crawling and serve `noindex`.

### Section outline (14 H2s)
| # | Section | Anchor |
|---|---|---|
| 1 | Hero: address, price, badges, photo mosaic, tabs, est. payment pill | — |
| 2 | About 4360 Conough Lane | `#overview` |
| 3 | Location (MapLibre, lazy) | `#location` |
| 4 | Property Details | `#details` |
| 5 | Property History | — |
| 6 | Tax & Financial | — |
| 7 | Mortgage Calculator (interactive) | `#mortgage` |
| 8 | California → Nevada Tax Savings (same calculator as the guide pages) | `#ca-tax-savings` |
| 9 | Schools (GreatSchools ratings) | `#schools` |
| 10 | Inside the Las Vegas Market | `#demographics` |
| 11 | Recent sold comps in ZIP 89129 | — |
| 12 | Similar Listings | — |
| 13 | Frequently Asked Questions | — |
| 14 | Why Work With Us? | — |
| 15 | Ready to make your move? (universal footer form) | — |

Layout: `.ldp-twocol` = `grid-template-columns: minmax(0,1fr) 340px` with a **sticky right rail** (`.ldp-twocol-rail { position:sticky; top:100px }`) holding the tour/contact form. On mobile the rail becomes `order:-1; position:static` (form moves *above* the content) and a fixed bottom action bar appears.

Component families (all `ldp-` prefixed, ~160 classes): `ldp-hero-*`, `ldp-herostat-*`, `ldp-substickyhdr-*`, `ldp-toursidebar-*`, `ldp-pricehist__*`, `ldp-prophistory__*`, `ldp-comps-*`, `ldp-agentmodule-*`, `ldp-urgency-*`, `ldp-mobilebar-*`, `ldp-contactbanner__*`, `ldp-saveheart`, `ldp-map-*`.

Notable hero badges: `ldp-hero-badge--newconstruction`, `ldp-hero-badge--openhouse`. Urgency module: `ldp-urgency-flame`, `ldp-urgency-chip`, `ldp-urgency-times`.

### Schema (JSON-LD, one `@graph` block)
```
WebSite            (+ SearchAction → /search/?q={search_term_string})
ImageObject        (#logo)
RealEstateAgent    (#nreg — full NAP, geo, openingHours "Mo-Su 08:00-20:00", areaServed City[] w/ containedInPlace Clark County)
Person             (#chris-nevada — jobTitle, identifier "S.181401", hasCredential
                    EducationalOccupationalCredential recognizedBy GovernmentOrganization
                    "Nevada Real Estate Division", 11 sameAs links incl. Zillow, FastExpert, red.nv.gov)
RealEstateListing  (#listing — name, description = full MLS remarks, datePosted, image[] from cdn.repliers.io)
BreadcrumbList     (Home → Las Vegas → MLS #2800048)
FAQPage            (#faq — 10 Q&As, about → #listing,
                    speakable.cssSelector: [".ldp-faq-q", ".ldp-faq-a"])
```

The FAQ answers are **generated from listing data**, not hand-written — e.g. the schools answer enumerates 8 zoned schools with GreatSchools ratings and closes with "Clark County School District boundaries can change year to year — confirm current zoning before you write an offer." The HOA answer reads "has no HOA reported on the listing — there are no monthly association dues on record." This is a per-listing programmatic FAQ layer and is a strong pattern to copy for any listing template.

Other head tags: `og:image` points straight at `https://cdn.repliers.io/lasvegas/IMG-2800048_0.jpg?class=large`; `twitter:card = summary_large_image`.

---

## 2.c Site platform

**Next.js 16.2.0 (App Router, Turbopack build) + React 19.3.0-canary, deployed on Vercel. Backend/auth/realtime is Supabase. There is no CMS in the classic sense — content is in code.**

### Evidence

| Signal | Value |
|---|---|
| `server:` header | `Vercel` |
| Next.js-specific headers | `x-nextjs-prerender: 1`, `x-nextjs-stale-time: 300`, `x-matched-path: /buyers` |
| Vary header | `vary: rsc, next-router-state-tree, next-router-prefetch, next-router-segment-prefetch` (App Router RSC) |
| CDN cache | `x-vercel-cache: HIT`, `age: 36753` |
| Asset paths | `/_next/static/chunks/*.js`, `/_next/static/media/*.woff2`, `/_next/image/?url=…` |
| Deployment id | every asset carries `?dpl=dpl_GZAh5K3bnphFH8yyfeFDmC4uWZ6K` |
| Bundler | a chunk literally named `turbopack-0gcrj2i3ou6ra.js` |
| React version string in bundle | `19.3.0-canary-3f0b9e61-20260317` |
| Next version string in bundle | `16.2.0` |
| Server Actions | `createServerReference` present in the bundle (the home-value form has no `action` attr and posts via a Server Action) |
| Streaming SSR | `<!--$?--><template id="B:0"></template>` Suspense boundaries; `BAILOUT_TO_CLIENT_SIDE_RENDERING` templates in the nav |
| Config | `trailingSlash: true` (confirmed by robots.txt comments and every URL) |
| **Not** WordPress | `/wp-json/` → **403**, no `meta generator`, no `wp-content` anywhere |
| No headless CMS | `/studio/` → **404**, `/admin/` → **404** (both are robots-blocked as if reserved, but not deployed) |
| Backend | **Supabase** — 65 `supabase` references in the bundle, `supabaseUrl` / `supabaseKey`, `SupabaseAuthClient`, `supabase.auth.token`, `supabase.gotrue-js.locks.debug`, `*.supabase.co` |
| Realtime | Phoenix Channels (`phx_join`, `phx_reply`, `phx_ref`, `phx_leave`) = Supabase Realtime, reached via `/api/broadcast` |
| Maps | MapLibre GL JS + MapTiler tiles |
| Icons | Lucide (inline SVG) |
| Analytics | GTM `GTM-W9BG6VB9` + GA4 `G-D7B1463Y0S`, custom events pushed to `window.dataLayer` via a `/api/track` helper |
| PWA | `/manifest.webmanifest` present, `apple-touch-icon` |

**Caching strategy:** HTML is `cache-control: public, max-age=0, must-revalidate` at the browser but served from Vercel's edge cache (`x-vercel-cache: HIT`, ages of 10+ hours observed) with `x-nextjs-stale-time: 300`. Property pages are ISR with `revalidate = 864000` (**10 days**) — stated explicitly in their own robots.txt comments, deliberately so that crawler traffic hits cache and does not burn Repliers/MLS API quota. `/_next/image/` responses are `public, max-age=31536000, must-revalidate`.

---

## 2.d Site-wide CSS / design system

Three global stylesheets are loaded on every page, plus route-specific chunks (6 CSS chunks total, ~616 KB uncompressed across all routes):

```
/_next/static/chunks/0_nc1eonl2f1h.css   (64.5 KB)  ← base/reset + Tailwind preflight
/_next/static/chunks/0as0ckk54covc.css   (288.6 KB) ← design tokens + global components
/_next/static/chunks/0uyhgk7_6scb-.css   (62.9 KB)
/_next/static/chunks/0q2itjgzj5wpt.css              ← LDP (property detail) only
/_next/static/chunks/11e2dohxp.8gt.css              ← route-specific
/_next/static/chunks/16z1kroqp1k29.css              ← route-specific
```

### Complete `:root` token set (verbatim)

```css
:root{
  /* --- brand core --- */
  --navy:#2b221a;            /* NOT navy — it's a deep warm brown */
  --navy-deep:#1a1410;
  --navy-light:#3a3025;
  --gold:#d4b27c;
  --gold-hover:#b89460;
  --gold-light:#e8d4b0;
  --gold-text:#7a5b2a;       /* AA-safe gold for body text */
  --brand-rust:#9c5f4e;
  --brand-rust-hover:#7a4a3d;

  /* --- neutrals --- */
  --white:#fff;
  --cream:#f7f4ee;
  --cream-warm:#ede7da;
  --stone:#7a7368;
  --ink:#0a0a0a;
  --ink-muted:#4a4a4a;
  --text-primary:#0a0a0a;
  --text-secondary:#4a4a4a;
  --text-faint:#4a4a4a;
  --border:#e8e2d6;
  --border-light:#e8e2d6;
  --border-dim:#d4b27c2e;    /* gold @ 18% */
  --line:#e8e2d6;
  --line-dark:#2a2a2a;

  /* --- dark surfaces --- */
  --dark:#1a1410;
  --dark-2:#2b221a;
  --dark-3:#3a3025;
  --dark-4:#14100d;
  --dark-bg:#2b221a;
  --dark-bg-2:#3a3025;
  --dark-text:#f7f4ee;
  --dark-text-muted:#9a9388;
  --charcoal:#211913;
  --surface-dark:#0a0a0a;
  --surface-black:#000;
  --surface-light-warm:#f7f7f7;
  --white-50:#ffffff80;
  --white-70:#f7f4eec7;

  /* --- semantic --- */
  --positive:#3d6b4a;
  --success:#3d6b4a;
  --success-soft:#e4ede7;
  --urgency:#e63946;
  --urgency-soft:#fce5e8;

  /* --- type --- */
  --font-serif:"Cormorant Garamond", Georgia, serif;
  --font-sans:"Inter", "Helvetica Neue", Arial, sans-serif;
  --font-cond:var(--font-barlow-cond), "Arial Narrow", sans-serif;
  --font-body:var(--font-barlow), system-ui, sans-serif;
  --font-ui:var(--font-roboto), system-ui, sans-serif;
  --font-mono:ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;

  /* fluid type scale */
  --text-xs:clamp(.75rem, .7rem + .25vw, .875rem);      /* 12 → 14px */
  --text-sm:clamp(.875rem, .8rem + .35vw, 1rem);        /* 14 → 16px */
  --text-base:clamp(1rem, .95rem + .25vw, 1.125rem);    /* 16 → 18px */
  --text-lg:clamp(1.125rem, 1rem + .75vw, 1.5rem);      /* 18 → 24px */
  --text-xl:clamp(1.5rem, 1.2rem + 1.25vw, 2.25rem);    /* 24 → 36px */
  --text-2xl:clamp(2rem, 1.2rem + 2.5vw, 3.5rem);       /* 32 → 56px */

  /* --- layout --- */
  --nav-h:72px;
  --container:1240px;
  --spacing:.25rem;          /* 4px base unit (Tailwind v4 style) */

  /* --- radius: essentially SQUARE --- */
  --radius:0;
  --radius-sm:2px;
  --radius-md:0;
  --radius-lg:0;
  --radius-xl:0;

  /* --- shadows (all pure-black, very low alpha) --- */
  --shadow-sm:0 1px 3px #0a0a0a0a;      /* black @ 4%  */
  --shadow-md:0 4px 16px #0a0a0a14;     /* black @ 8%  */
  --shadow-lg:0 12px 40px #0a0a0a1f;    /* black @ 12% */
  --shadow-card:0 2px 8px #0a0a0a0a;
  --shadow-hover:0 8px 24px #0a0a0a14;
  --shadow-deep:0 20px 60px #0a0a0a1f;

  --transition:.2s ease;
}
```

### Property-detail sub-theme (`0q2itjgzj5wpt.css`)
The LDP has its **own softer token layer** that re-aliases the globals and, notably, **reintroduces rounded corners** (the rest of the site is square):
```css
--ldp-ink:var(--navy);          --ldp-navy:var(--navy);      --ldp-navy-deep:var(--navy-deep);
--ldp-bone:var(--cream);        --ldp-bonelite:#fbf9f4;      --ldp-white:var(--white);
--ldp-gold:var(--gold);         --ldp-goldhover:var(--gold-hover,#b89460);
--ldp-goldlt:var(--gold-light,#e8d4b0);  --ldp-goldtext:var(--gold-text,#7a5b2a);
--ldp-gray100:#ece9e1;  --ldp-gray200:#d9d5c8;  --ldp-gray400:#8c8775;  --ldp-gray600:#5a5648;
--ldp-green:#0b6e4f;
--ldp-radius-btn:8px;   --ldp-radius-card:12px;
--ldp-shadow:0 1px 3px #2b221a0f, 0 4px 16px #2b221a0a;   /* brown-tinted, not black */
--ldp-shadow-lg:0 8px 32px #2b221a1f;
```
The LDP shadows are tinted with `--navy` (`#2b221a`) rather than pure black — that is the "color-tinted shadow" trick, and it is worth stealing.

### Fonts — 9 families, all self-hosted via `next/font` (zero Google Fonts requests)

All served from `/_next/static/media/*.woff2`, `font-display: optional`, with generated `*-Fallback` metric-matched fallbacks and per-subset `unicode-range` splitting (latin, latin-ext, cyrillic, cyrillic-ext, vietnamese).

| Family | Weights | Styles | Role |
|---|---|---|---|
| **Barlow** | 400, 500, 600 | normal | `--font-body` — default `<body>` font |
| **Barlow Condensed** | 300, 500, 600, 700 | normal | `--font-cond` — condensed display/stats |
| **Cormorant Garamond** | 400, 500, 600, 700 | normal + italic | `--font-serif` — all section H2s |
| **Inter** | 400, 500, 600, 700 | normal | `--font-sans` — eyebrows, labels, form UI |
| **Mulish** | 400, 500, 600, 700, 800 | normal | search page + LDP body font, listing prices |
| **Roboto** | 300, 400, 500 | normal | `--font-ui` — nav button |
| **Fraunces** | 400, 500, 600 | normal + italic | `--font-fraunces` — accent display |
| **Libre Caslon Display** | 400 | normal | `--font-display` |
| **JetBrains Mono** | 400, 500 | normal | data/tabular |

Only 3 woff2 files are `<link rel="preload">`ed on `/search/` — the rest load on demand.

**Typography pairing rule in practice:** Cormorant Garamond (serif) for section headings, Inter (sans) for uppercase-tracked eyebrows/labels, Barlow or Mulish for body. Three families per page, not two.

### Container / layout
```css
.container{max-width:1200px;margin:0 auto;padding:0 24px;width:100%}   /* global default */
.container{max-width:1800px;margin:0 auto;padding:0 24px}              /* wide (search results) */
.ldp-container{max-width:1280px;margin:0 auto;padding:0 24px}          /* property detail */
@media(max-width:…){ .ldp-container{padding:0 16px} }
```
`--container: 1240px` is declared as a token but individual sections override with inline `max-width` — commonly **880px** (TOC/prose), **1100px** (card grids), **1200px** (default), **1800px** (search).

Section rhythm: `padding: 72px 0` on guide sections, `56px 0` → `80px 0` on LDP sections, `scroll-margin-top: 96px` on every anchored section.

### Breakpoints (by frequency of use)
```
max-width: 1100px | 1024px | 1023px | 1000px | 900px | 860px | 768px | 767px |
           760px  |  720px |  640px |  600px | 560px |  520px | 480px
min-width: 40rem(640) | 48rem(768) | 64rem(1024) | 80rem(1280)
also: (prefers-reduced-motion: reduce/no-preference), (hover: hover), (hover: none)
```
The heaviest-used are **768px, 640px, 900px, 720px, 600px**. This is not a tidy 4-step system — it is per-component, which is a mild maintainability warning if you copy it.

### Key component styles
```css
body{
  background:var(--white);color:var(--text-primary);
  font-family:var(--font-body);font-size:var(--text-base);
  line-height:1.6;-webkit-font-smoothing:antialiased;
  max-width:100vw;overflow-x:clip;position:relative
}

.section-label{                    /* the gold eyebrow above every H2 */
  display:inline-block;
  font-family:var(--font-sans);font-size:13px;font-weight:700;
  letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold-text);margin-bottom:12px
}

.gold-rule{                        /* 48px gold underline beneath the eyebrow */
  display:block;width:48px;height:2px;
  background:var(--gold);margin-bottom:16px
}

.btn-gold{
  display:inline-flex;align-items:center;gap:8px;
  min-height:44px;padding:13px 28px;
  background:var(--gold);color:var(--navy);
  border-radius:var(--radius-md);       /* = 0, square */
  font-size:14px;font-weight:700;letter-spacing:.04em;text-transform:uppercase;
  transition:background var(--transition), transform var(--transition)
}

.btn-nav{                          /* the rust "Call" button in the header */
  display:inline-flex;align-items:center;gap:8px;
  padding:10px 32px;
  background:var(--brand-rust);color:#fff;
  border:2px solid var(--brand-rust);border-radius:0;
  font-family:var(--font-ui);font-size:18px;font-weight:600;
  text-transform:none;letter-spacing:0;white-space:nowrap;
  transition:background var(--transition), border-color var(--transition), transform var(--transition)
}

.ccm__form{display:grid;grid-template-columns:1fr 1fr;gap:16px 18px}
@media(max-width:…){ .ccm__form{grid-template-columns:1fr} }
.ccm__send{
  padding:16px 32px;border:none;border-radius:999px;   /* the ONE pill on the site */
  background:var(--gold);color:var(--navy);
  font-family:var(--font-sans);font-size:15px;font-weight:600;cursor:pointer;
  transition:background-color .22s, color .22s
}
```

**Design-system summary in one line:** warm brown + antique gold + rust, square corners everywhere except the property-detail page and the one pill-shaped submit button, serif headings over sans eyebrows, whisper-quiet shadows (4–12% black), 44px minimum touch targets, `.2s ease` transitions.

---

## 2.e Sticky table-of-contents component

There are **three distinct TOC/scroll-nav implementations**. Only one has real scroll-spy.

### (1) Guide-page TOC — static, no JS, not sticky

Markup (`/moving-to-las-vegas/`, `/nellis-afb-relocation-guide/`):
```html
<nav class="toc" aria-label="Table of contents">
  <h2 class="toc__title">On This Page</h2>
  <ol class="toc__list">
    <li><a href="#six-reasons">Why Las Vegas beats coastal markets</a></li>
    <li><a href="#tax-savings">Nevada residency tax savings</a></li>
    …
  </ol>
</nav>
```

CSS:
```css
.toc{
  margin:0 0 40px;padding:22px 26px;
  background:var(--cream);
  border-left:2px solid var(--gold)
}
.toc__title{
  margin:0 0 12px;
  font-family:var(--font-sans);font-size:11px;font-weight:700;
  letter-spacing:.14em;text-transform:uppercase;
  color:var(--gold-hover)
}
.toc__list{
  columns:2;column-gap:28px;
  margin:0;padding-left:22px;list-style:decimal
}
.toc__list li{margin-bottom:6px;break-inside:avoid}
.toc__list a{
  color:var(--navy);font-size:14px;line-height:1.6;text-decoration:none
}
.toc__list a:hover{
  color:var(--gold-hover);
  text-decoration:underline;
  text-decoration-color:var(--gold)
}

/* MOBILE: collapse to one column */
@media (max-width:…){ .toc__list{columns:1} }
```

An older `<details>`-based variant also exists in the CSS (used on legacy blog templates):
```css
.toc{background:var(--cream);border-radius:var(--radius-lg);max-width:720px;margin:0 0 32px;padding:16px 20px;font-size:14px}
.toc summary{cursor:pointer;color:var(--navy);font-weight:600}
.toc ul{margin:12px 0 0;padding:0;list-style:none}
.toc li{margin:6px 0}
.toc a{color:var(--navy);text-decoration:none}
.toc a:hover{color:var(--gold);text-decoration:underline}
```

And an IDX-landing-page variant:
```css
.idxlp-toc{background:#fffcf6;border:1px solid #dcd2c3;border-radius:12px;margin:0 0 24px;padding:18px 22px}
.idxlp-toc .toc-heading{
  margin:0 0 10px;font-family:var(--font-sans);font-size:12px;font-weight:600;
  letter-spacing:.12em;text-transform:uppercase;color:var(--gold,#c9a96e)
}
.idxlp-toc ol{display:grid;grid-template-columns:repeat(2,1fr);gap:6px 24px;margin:0;padding-left:1.2rem}
.idxlp-toc a{color:var(--navy,#1b2a4a);font-size:14px;text-decoration:none}
.idxlp-toc a:hover{color:var(--gold,#c9a96e);text-decoration:underline}
@media (max-width:…){ .idxlp-toc ol{grid-template-columns:1fr} }
```

### (2) Sticky floating TOC — **CSS-only, triggered by `:has()`**

This is the clever one. The same `.toc` markup becomes a fixed right-rail widget **with no JS and no extra class**, purely because the page contains a community card or new-construction table:

```css
:is(body:has(.community-card) .toc, body:has(.nc-table) .toc){
  position:fixed;
  right:24px;
  top:calc(var(--nav-h,72px) + 24px);
  z-index:8;
  width:250px;
  max-height:calc(100vh - var(--nav-h,72px) - 60px);
  overflow-y:auto;
  margin:0;padding:18px 20px;
  background:var(--cream);
  border-left:3px solid var(--gold);
  font-size:13px;
  box-shadow:0 4px 14px #0a0a0a0f
}
:is(body:has(.community-card) .toc .toc__list, body:has(.nc-table) .toc .toc__list){
  columns:1;padding-left:18px
}
:is(body:has(.community-card) .toc__list li, body:has(.nc-table) .toc__list li){
  margin-bottom:4px
}
:is(body:has(.community-card) .toc__list a, body:has(.nc-table) .toc__list a){
  font-size:13px;line-height:1.45
}
```
Mobile behavior: the enclosing media query drops it back to the static in-flow block (`columns:1`), so it never fixed-positions over a phone screen. **No active-section highlighting** — it is a persistent jump list, nothing more.

### (3) Property-detail sticky sub-header — the real scroll-spy

Component source (deminified from `js/03rz0adw2vm~e.js`, module 556468):

```js
const SECTIONS = [
  { id: "overview",  label: "Overview" },
  { id: "location",  label: "Location" },
  { id: "details",   label: "Property Details" },
  { id: "mortgage",  label: "Mortgage Calculator" },
  { id: "schools",   label: "Schools" }
];

export default function SubStickyHeader({ listing }) {
  const [active, setActive] = useState("overview");

  useEffect(() => {
    const io = new IntersectionObserver(
      entries => {
        const visible = entries
          .filter(e => e.isIntersecting)
          .sort((a, b) => b.intersectionRatio - a.intersectionRatio);
        if (visible[0]?.target.id) setActive(visible[0].target.id);
      },
      { rootMargin: "-140px 0px -50% 0px", threshold: [0, 0.25, 0.5] }
    );
    for (const s of SECTIONS) {
      const el = document.getElementById(s.id);
      if (el) io.observe(el);
    }
    return () => io.disconnect();
  }, []);

  const baths = listing.bathsFull + 0.5 * listing.bathsHalf;

  return (
    <div className="ldp-substickyhdr">
      <div className="ldp-container ldp-substickyhdr-inner">
        <div className="ldp-substickyhdr-summary">
          <span className="ldp-substickyhdr-addr">{listing.streetAddress}</span>
          <span className="ldp-substickyhdr-price">${listing.price.toLocaleString()}</span>
          <span className="ldp-substickyhdr-meta">
            {listing.beds} bd · {baths} ba · {listing.sqft.toLocaleString()} sqft
          </span>
        </div>
        <nav className="ldp-substickyhdr-tabs" aria-label="Page sections">
          {SECTIONS.map(s => (
            <a key={s.id} href={`#${s.id}`}
               className="ldp-substickyhdr-tab"
               data-active={active === s.id ? "true" : "false"}>
              {s.label}
            </a>
          ))}
        </nav>
        <div className="ldp-substickyhdr-actions">
          <ShareButton listing={listing} variant="pill" />
          <SaveHeart mlsNumber={listing.mlsNumber} variant="pill" />
        </div>
      </div>
    </div>
  );
}
```

The `rootMargin: "-140px 0px -50% 0px"` is the important number: it shrinks the observation window to start 140px below the viewport top (clearing the sticky nav + sub-header) and end at the vertical midpoint, so "active" means "this section owns the upper half of the screen." Sorting by `intersectionRatio` descending breaks ties when two sections are both visible.

CSS:
```css
.ldp-substickyhdr{
  position:sticky;top:0;z-index:40;
  padding:12px 0;
  background:var(--ldp-white);
  border-bottom:1px solid var(--ldp-gray100);
  box-shadow:0 4px 12px #2b221a0a
}
.ldp-substickyhdr-tabs{
  flex:auto;display:flex;gap:4px;
  overflow-x:auto;                 /* mobile: horizontal scroll */
  scrollbar-width:none;-ms-overflow-style:none
}
.ldp-substickyhdr-tabs::-webkit-scrollbar{display:none}
.ldp-substickyhdr-tab{
  padding:8px 12px;border:0;border-radius:6px;background:0 0;
  font-family:inherit;font-size:13px;font-weight:500;
  color:var(--ldp-gray600);
  white-space:nowrap;text-decoration:none;cursor:pointer
}
.ldp-substickyhdr-tab:hover,
.ldp-substickyhdr-tab[data-active=true]{
  color:var(--ldp-ink);
  background:var(--ldp-bone)
}
```

Companion mobile action bar (property pages only):
```css
.ldp-mobilebar{
  display:none;                                   /* desktop */
  position:fixed;bottom:0;left:0;right:0;z-index:50;
  gap:10px;
  padding:12px 14px calc(12px + env(safe-area-inset-bottom));
  background:var(--ldp-white);
  box-shadow:0 -4px 20px #2b221a1a;
  transform:translateZ(0);will-change:transform
}
@media (max-width:…){ .ldp-mobilebar{display:flex} }   /* "Tour" + "Contact" buttons */
```

Sticky right rail:
```css
.ldp-twocol{display:grid;grid-template-columns:minmax(0,1fr) 340px;gap:40px;align-items:start}
.ldp-twocol-rail{position:sticky;top:100px;align-self:start}
@media (max-width:…){
  .ldp-twocol{grid-template-columns:1fr;gap:28px}
  .ldp-twocol-rail{order:-1;position:static}       /* form jumps above content on mobile */
}
```

**Recommendation for Rose Homes LV:** copy pattern (1) for guide pages (dead simple, works in Lofty's HTML blocks), and copy pattern (3)'s `IntersectionObserver` + `rootMargin: "-140px 0px -50% 0px"` + `data-active` scheme if you want a real scroll-spy — it is ~20 lines of vanilla JS and does not need React.

---

## 2.f Performance / SEO technical

### Images
- **All images go through the Next.js optimizer** (`/_next/image/?url=…&w=…&q=75`), including remote Repliers CDN images.
- **Format: AVIF via content negotiation.** Verified: request with `Accept: image/avif,image/webp,*/*` returns `content-type: image/avif`, `vary: Accept`. Source files on the CDN are `.jpg`; the browser never sees a JPEG if it supports AVIF.
- **Quality `q=75`**, srcset widths `256 / 384 / 640 / 750 / 828 / 1080 / 1200 / 1920`.
- `sizes="(max-width: 600px) 100vw, (max-width: 900px) 50vw, (max-width: 1440px) 33vw, 25vw"` on listing cards — matches the 1/2/3/4-column grid exactly.
- **Cache: `public, max-age=31536000, must-revalidate`** (1 year) on optimized images, edge-cached.
- **Lazy loading:** `loading="lazy"` + `decoding="async"` on essentially everything below the fold — 24/24 listing images on `/search/`, 20 on the homepage. Only the homepage uses `fetchPriority="high"` (2 instances — the LCP hero).
- Layout stability: `data-nimg="fill"` with an explicit `aspect-ratio: 4/3` wrapper, so CLS is ~0 on the grid.

### JS loading
- 24 JS chunks on `/search/` (~1.3 MB uncompressed total across the routes sampled), aggressive code-splitting via Turbopack.
- Router prefetch uses its own `IntersectionObserver` with `rootMargin: "200px"` — links prefetch when they get within 200px of the viewport.
- MapLibre is dynamically `import()`ed and additionally gated behind a `rootMargin: "200px"` observer, so the map bundle never downloads on a list-view session.
- A generic `<LazyMount>` wrapper (`IntersectionObserver` + `minHeight` placeholder + `aria-busy`) defers below-fold client components.
- Count-up stat animations are also `IntersectionObserver`-driven (`data-count-target`, `data-count-prefix`, `data-count-suffix`, `data-count-decimals`, `data-count-comma`) and self-disable via `dataset.animated = "1"`.
- `@media (prefers-reduced-motion: reduce)` blocks appear 5 times in the global CSS.

### Canonical strategy
Every page emits a self-referencing canonical. The interesting part is the **`noindex` layer**:

| Page class | robots meta | In sitemap? |
|---|---|---|
| Guide / hub / tool pages | `index, follow` | Yes |
| `/search/` (bare) | `index, follow` | Yes |
| `/search/?view=map` and any parameterized `/search/?…` | **`noindex, follow`**, canonical → `/search/` | No |
| `/compare-listings/` | **`noindex, follow`** | No |
| `/property/<slug>/` | **`noindex, follow`** | No (0 of 2,823) |

### robots.txt — unusually well engineered, 11.7 KB, heavily commented

Quoting the operative reasoning (their own comments, condensed):
> `/property/*` is NO LONGER robots-blocked (changed 2026-07-03). Those pages are transient (listings sell + go off-market) and we don't want them indexed — but robots-blocking is the WRONG tool for that: it stopped Google crawling them, yet Google indexed ~half of them anyway from backlinks ("Indexed, though blocked by robots.txt", 643 URLs). Robots blocks crawling, not indexing; the only way Google DROPS a page is to crawl it and see a noindex tag.
> MLS-quota-safe: the page is ISR-cached 10 days (revalidate=864000), so crawls hit cache, not fresh Repliers calls.
> `/search?` AND `/search/?` (both slash forms — trailingSlash:true renders the links as `/search/?city=…`, which `/search?` alone does NOT match) … those filter views are noindex AND each render fans out to a count probe + bulk listing pagination. Crawlers exploring `?city=…&filter=…` combos = a crawl-trap that burns the MLS quota.
> NOTE: robots.txt has no inheritance — a bot obeys ONLY its most-specific matching group, so the Disallow block is repeated in every group on purpose.

Default group:
```
User-agent: *
Allow: /
Disallow: /studio/
Disallow: /admin/
Disallow: /api/
Disallow: /idx-demo
Disallow: /idx-demo/
Disallow: /search?
Disallow: /search/?
Disallow: /reno/search
Allow: /data/las-vegas-market
Allow: /data/reno-market
Disallow: /data/
```

**27 named user-agent groups.** AI crawlers are explicitly *opted in* (Allow: /) with the same trap-blocking: `GPTBot`, `ChatGPT-User`, `OAI-SearchBot`, `ClaudeBot`, `Claude-Web`, `anthropic-ai`, `PerplexityBot`, `Perplexity-User`, `Google-Extended`, `Applebot`, `Applebot-Extended`, `Amazonbot`, `Meta-ExternalAgent`, `Bytespider`, `CCBot`, `cohere-ai`, `DuckAssistBot`, `Diffbot`, `YouBot`, `Bingbot`, `msnbot`.

SEO-tool crawlers are throttled hard (`AhrefsBot`, `AhrefsSiteAudit`, `SemrushBot`, `SiteAuditBot`, `Screaming Frog SEO Spider`) with extra `Disallow` on `/property/`, `/*/homes-for-sale`, `/*/new-construction`, `/homes-with-`, `/open-houses-`, `/recently-reduced-`, `/guard-gated-communities`, etc.

Note the `/data/` carve-out: client-side map-boundary GeoJSON is Disallowed (robots doesn't gate browser fetches, so maps still work), **except** two citable "Data-PR" pages — `/data/las-vegas-market` and `/data/reno-market` — Allow-carved in every group so journalists and Google can read them.

### Sitemap
- **Single flat `/sitemap.xml`** — not an index. **2,823 URLs.**
- Every entry has `<lastmod>` (ISO 8601 with ms, all set to the same build timestamp `2026-07-25T15:02:48.326Z`), `<changefreq>`, and `<priority>`.
- Homepage: `changefreq: daily`, `priority: 1`. Hub pages: `changefreq: weekly`.
- Distribution by first path segment:

| Segment | URLs |
|---|---|
| `/las-vegas/…` | 763 |
| `/blog/…` | 708 |
| `/henderson/…` | 393 |
| `/reno/…` | 161 |
| `/north-las-vegas/…` | 112 |
| `/market-report/…` | 84 |
| `/zip/…` | 61 |
| `/sparks/…` | 46 |
| `/compare/…` | 38 |
| `/gardnerville/…` | 36 |
| `/carson-city/…` | 35 |
| `/incline-village/…` | 28 |
| `/builders/…` | 27 |
| `/schools/…` | 26 |
| `/dayton/…` | 24 |
| `/high-rise-condos/…` | 23 |
| `/lake-tahoe/…` | 17 |
| `/stateline/…` | 16 |
| `/pahrump/…` | 15 |
| `/minden/…` | 14 |
| `/fernley/`, `/boulder-city/` | 12 each |
| `/guides/…` | 11 |
| `/fallon/…` | 11 |
| `/summerlin/…` | 8 |
| `/property/…` | **0** |

### AI / LLM discoverability
Two machine-readable content maps, linked from `<head>` on every page:
```html
<link rel="alternate" type="text/plain" href="/llms.txt"/>
<link rel="alternate" type="text/plain" href="/llms-full.txt"/>
```
`/llms.txt` is 18 KB, sectioned like:
- "Live listings by city (transactional hubs — live MLS counts, medians, neighborhood tables)"
- "Market data (locked monthly MLS statistics — free to cite with attribution)"

This is a deliberate AI-citation play, paired with the AI-crawler allow-list in robots.txt and the `speakable` cssSelector in the FAQ schema.

### hreflang / AMP
- **No hreflang.** (`<link rel="alternate">` tags exist on 16 pages but they are the two `llms.txt` links, not language alternates.) Site is `inLanguage: "en-US"` only.
- **No AMP.** Zero `amphtml` references anywhere.

### Other head-level items
- `<link rel="manifest" href="/manifest.webmanifest">` (PWA)
- `<link rel="preconnect">` + `<link rel="dns-prefetch">` to `https://images.unsplash.com` (they use Unsplash for some editorial imagery)
- `strict-transport-security: max-age=63072000` (2 years)
- `access-control-allow-origin: *` on HTML

---

# Appendix — Prioritized takeaways for the Rose Homes LV rebuild

**Do copy (cheap, high leverage, no IDX dependency):**
1. The universal `ccm__form` footer on every page, with the **timeline select as lead-scoring** and the trust bar above the consent text.
2. The **"Where are you in the process?" 3-card router** at the top of every pillar guide, above the prose.
3. `FAQPage` schema on every guide (6–18 questions), plus programmatic per-listing FAQs if you control the listing template.
4. The `nav.toc` "On This Page" block on any page over ~2,500 words, with `scroll-margin-top: 96px` on anchored sections.
5. The `/market-report/` model: a thin 1,500-word directory hub feeding 80+ programmatic child pages.
6. `llms.txt` + `llms-full.txt` + an AI-crawler allow-list in robots.txt.
7. `noindex, follow` on listing detail pages, and **crawlable, not robots-blocked** — their comment block is a hard-won lesson worth inheriting.
8. Est. monthly payment on the listing card with the assumptions in a `title` attribute.

**Cannot copy without a data licence + custom app:**
- Everything under `/search/` and `/property/`. Repliers + Next.js SSR, API key server-side only. A Lofty IDX embed is a different product with different markup; plan to accept Lofty's search UI and differentiate on the content layer.

**Watch out:**
- Their breakpoint set is ad hoc (15 distinct max-widths). Define 4 and stick to them.
- The MapTiler key is exposed client-side. If you copy the map approach, budget for a keyed tile provider and restrict it by referrer.

---

*Research artifacts (raw HTML, CSS chunks, JS chunks) in `/private/tmp/claude-501/-Users-ryanrose-Downloads-Claude/6477daa7-6c35-4157-844e-8990af0dce0e/scratchpad/nrg-f/`.*
