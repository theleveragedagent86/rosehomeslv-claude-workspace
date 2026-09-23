# Local SEO Audit — rosehomeslv.com

Date: 2026-07-29 · Business type: Real estate agent (Ryan Rose, Real Broker LLC) · Customer travel: goes-to-customer (wide radius OK) · Platform: **Lofty (Chime)** hosted

## Summary
Solid foundation: clean nav, connected Google Business Profile (Maps CID present), real community/area pages with auto Place/City schema, and a genuinely unique blog (the real ranking moat). The biggest wins are cheap and systemic: fix the site-wide 3-H1 template bug, cut over-long SEO titles (all 70+ chars, truncating in search), add RealEstateAgent + AggregateRating + FAQ schema, expand the thin "Areas" set to cover the workspace's target communities, and build intent pages (New Construction, Luxury, Relocation, 55+) that don't exist yet. Biggest risk: the Lofty area pages are auto-generated and thin/templated (928 words of mostly demographics), so scaling them without unique local narrative risks the de-index problem. The blog is what keeps it safe.

**Platform reality:** This is NOT WordPress or static, so the video's "move to GitHub/Vercel/Cloudflare" advice does not apply. Ryan's real levers on Lofty are: per-page SEO title/meta, the blog (`/blog/<slug>`), Lofty landing pages, Lofty Area pages, homepage modules, and any custom-code/header injection Lofty allows for schema.

## Findings

### 1. Hero
- **Current:** Homepage hero leads with brand + tagline. No physical address above the fold, no map embed, no numeric review rating shown.
- **Fix:** Add the Real Broker LV office address + a Google Map embed near the top; surface the Google star rating/review count as a trust badge (feeds AggregateRating schema).
- **Why:** Address-above-fold + map + visible rating are core local trust and NAP-consistency signals; Lofty allows a custom homepage module for this.

### 2. Practitioner / agent pages
- **Current:** Single About/About Me page. No structured agent bio page with Person schema.
- **Fix:** Build a proper "Ryan Rose, Las Vegas Realtor" bio page (or upgrade About) with Person + RealEstateAgent schema, specialties linking to intent pages, and reviews.
- **Why:** Ranks for name searches ("Ryan Rose realtor Las Vegas") and anchors E-E-A-T/entity signals across the site.

### 3. Neighborhood / area pages
- **Current:** Only 4 in nav: Southern Highlands, Macdonald Highlands, Summerlin, Henderson. Area pages carry Place + City schema and a "Nearby Locations" block (good), but content is ~928 words of mostly Lofty-auto demographics/market data — thin on unique local narrative, no FAQ.
- **Fix:** (a) Expand to the workspace target communities: Spring Valley, Centennial Hills, North Las Vegas, Skye Canyon, Green Valley, plus Mountain's Edge, Inspirada, Cadence, Lake Las Vegas, Aliante. (b) Add a unique 150–300 word human intro + an FAQ block to each area page so it isn't pure template. (c) Interlink each area page to its blog cluster (already have Silverstone Ranch posts, etc.).
- **Why:** More qualified geo coverage; the unique intro + FAQ is what keeps templated area pages out of the sandbox.

### 4. Schema markup
- **Current:** Homepage has only `Organization` (duplicated twice). Area pages have `Place`+`City`. **Missing:** RealEstateAgent/LocalBusiness with NAP+geo+hours, AggregateRating (despite a Reviews section), FAQPage, BreadcrumbList, Person.
- **Fix:** Add a site-wide `RealEstateAgent` block (name "Ryan Rose", phone +1-702-747-5921, url, `worksFor` Real Broker LLC, GBP `sameAs`), `AggregateRating` from real Google reviews, `Person` on the bio page, `FAQPage` wherever FAQs are added, `BreadcrumbList` on area/intent pages. De-dupe the double Organization.
- **Why:** Rich results + AI-answer-engine eligibility; the current setup leaves the strongest realtor entity signal (RealEstateAgent) on the table. Implement via Lofty header/custom-code injection or on landing pages.

### 5. Interlinking structure
- **Current:** Nav covers Buy/Sell/Areas/Calculators. Area pages auto-link nearby areas. But there is no intent×community linking and the blog cluster isn't systematically linked from the matching area pages.
- **Fix (realtor version of the "game over" model):** Treat buyer intents as the "services": New Construction, Luxury, Relocation, First-Time Buyer, 55+/Active Adult, Investment. Put the top ones in the nav. Then interlink: intent page → community versions ("New Construction in Summerlin"), community page → its intent pages + its blog posts + its live listings. Keep intent pages location-neutral in the H1, push geo to the community versions.
- **Why:** Creates one-to-one intent+geo targeting and funnels authority from blog → area → listings. Highest-leverage item.

### 6. Service / intent pages
- **Current:** Buy and Sell exist (mostly IDX/valuation tools, little content). No content pages for New Construction (which Ryan actively does), Luxury, Relocation, 55+, Investment, First-Time/VA.
- **Fix:** Build a content page per intent, targeting adjacent terms (e.g. New Construction → "new build homes", "builder incentives", "new home communities Las Vegas") with unique copy + FAQ. Link down to community versions.
- **Why:** Captures high-intent non-brand search the current tool-only Buy/Sell pages can't rank for.

### 7. FAQs
- **Current:** No FAQ anywhere (homepage, area pages, intent pages).
- **Fix:** Add an FAQ block to the homepage, each area page, and each intent page. Mine questions from real buyer/seller scenarios (HOA fees, school ratings, commute, new-build incentives, closing costs) — factual only. Pair with FAQPage schema.
- **Why:** Free longtail capture + AI-answer-engine citations; also a natural slot for localized content.

### 8. Anti-boilerplate / indexing safety
- **Current:** Lofty area pages share a heavy template; scaling them 1:1 risks near-duplicate thin pages.
- **Fix:** Every new area page needs the unique intro + FAQ (#3). Phase new communities in over weeks, not all at once. Let the blog carry the unique-depth load.
- **Why:** Templated mass pages get de-indexed/sandboxed; unique local sections + phasing avoid it.

### 9. Platform / shippability
- **Current:** Lofty (Chime). Title tags are 70 chars sitewide (truncating); homepage meta description contains an **em dash** (violates workspace no-em-dash rule); 3 `<h1>`s on every page (header tagline + "Rose Homes LV" render as H1 alongside the real page H1).
- **Fix:** (a) Rewrite every SEO title to ≤60 chars, keyword-first, "| Ryan Rose" retained. (b) Replace the em dash in the homepage meta description. (c) Fix the theme so only the page's real heading is `<h1>` (demote the tagline + logo to `<p>`/`<span>` or H2) — this is a Lofty theme setting/custom CSS/JS fix. (d) Add schema via Lofty custom-code injection.
- **Why:** Title truncation kills CTR; multiple H1s dilute the on-page topic signal; the em dash breaks the brand content rule.

## Missing pages to create
| Page | Type | Primary keyword | Links to | Priority |
|------|------|-----------------|----------|----------|
| New Construction (hub) | Intent | new construction homes Las Vegas | community versions, builders, listings | High |
| Luxury Homes (hub) | Intent | Las Vegas luxury homes | Macdonald Highlands, Summerlin, listings | High |
| Relocation Guide | Intent | moving to Las Vegas | all area pages, cost-of-living blog | High |
| Ryan Rose bio | Practitioner | Ryan Rose realtor Las Vegas | intents, reviews, contact | High |
| Spring Valley / Centennial Hills / North LV / Skye Canyon / Green Valley | Area | homes for sale in <community> | intents, blog cluster, listings | Med |
| 55+/Active Adult, First-Time Buyer, Investment | Intent | <intent> homes Las Vegas | community versions | Med |
| New Construction in Summerlin / Skye Canyon / Cadence (etc.) | Intent×geo | new construction <community> | parent intent + area page | Lower (phase in) |

## Schema to add
- **RealEstateAgent** (site-wide) — name/phone/url/worksFor available; office street address = confirm from Real Broker (NOT FOUND on page).
- **AggregateRating** — pull rating + count from the connected Google Business Profile (NOT FOUND on page as text; do not invent).
- **Person** (Ryan) on bio page.
- **FAQPage** on homepage + area + intent pages (once FAQs written).
- **BreadcrumbList** on area/intent pages.
- De-duplicate the two `Organization` blocks on the homepage.

## Build Order (what to ship, in sequence)
1. **Quick technical wins (site-wide, no new pages):** fix 3-H1 template bug; rewrite all SEO titles to ≤60 chars; remove em dash from homepage meta; de-dupe Organization schema.
2. **Homepage trust + schema:** add address + map embed + visible Google rating to hero; inject RealEstateAgent + AggregateRating schema.
3. **Ryan Rose bio page** with Person schema + review pull.
4. **Core intent hubs** (location-neutral): New Construction, Luxury, Relocation — full unique copy + FAQ + schema, added to nav.
5. **Enrich existing 4 area pages:** unique intro + FAQ + schema; link each to its blog cluster + relevant intent pages.
6. **New area pages, phased:** batch 1 = Spring Valley, Centennial Hills, North Las Vegas (unique intro + FAQ each); later batches for the rest.
7. **Intent×community pages,** phased, each linked one-to-one (e.g. New Construction in Summerlin → New Construction hub + Summerlin area page).
8. **Ongoing:** blog cluster per community via `blog-writer`; keep FAQ/longtail expanding.

Sequence rule honored: technical + hub/foundation pages first, geo long-tail phased in last so publishing looks organic and nothing links to a page before it exists.
