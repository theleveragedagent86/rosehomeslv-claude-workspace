# NRG Research 05: The Blog Cluster Behind `/new-construction/`

**Source:** `https://www.nevadarealestategroup.com/`
**Captured:** 2026-07-25
**Method:** full `/blog/` index harvest (885 post cards, all rendered server-side on page 1, pagination is client-side only), cross-checked against `sitemap.xml` (708 `/blog/` URLs, a strict subset of the index). 173 Las Vegas metro new-construction-adjacent posts were downloaded in full and parsed for schema, headings, tables, links, and citations. Raw HTML in scratchpad `.../scratchpad/nrg/pages/`.

---

## 0. Headline numbers

| Metric | Value |
|---|---|
| Total blog posts on the site | **885** (708 in sitemap, so the sitemap is missing 177 posts) |
| NC-adjacent posts, Las Vegas metro | **173** |
| NC-adjacent posts, Northern Nevada (Reno/Sparks/Carson) | ~13 more |
| Total NC-adjacent, site-wide | **~186 of 885 (21%)** |
| Median schema `wordCount` | **4,591** (p10 3,943 / p90 5,670 / range 3,493 to 6,157) |
| Posts with a table of contents | **173 of 173 (100%)** |
| Posts linking to `/new-construction/` in-body | **140 of 173 (81%)** |
| Median H2 count | **15** |
| Median FAQ questions | **7** (always 6 to 9, never fewer, never more) |
| Median tables per post | **3** (range 3 to 8) |
| Inline figures per post | **4** (162 of 173 have exactly 4) |
| Median internal links in body | **26** |
| Median external citations in body | **24** |
| Posts with a YouTube embed | 27 of 173 (all post-dated July 2026) |
| Author | **Chris Nevada** on every single post |
| Publish date range of the NC cluster | Oct 2021 to Jul 2026, but **93% published Apr–Jul 2026** |

The whole NC blog cluster was built in roughly a 90 day sprint. May 11, 2026 alone produced **24 NC posts** in one day, and July 19, 2026 produced **13 builder-model posts** in one day. This is programmatic templated publishing, not organic blogging.

---

## 1. THE BLOG POST TEMPLATE

Every post is the same component. I deep-dove five: the Inspirada community spotlight, the incentives roundup, the "best agent for new construction" service post, the KB Home Plan 3095 model post (newest template revision), and the where-to-buy tier ranking. The DOM class inventory is identical across all of them.

### 1.1 Exact section order (top to bottom)

| # | Block | CSS hook | Notes |
|---|---|---|---|
| 1 | **Full-bleed hero image** | `figure.blog-post-hero.hero-figure` | 16:9, `max-width:1400px`, `object-fit:cover`, `fetchPriority="high"`. Filename always equals the slug: `/images/blog/<slug>.jpg`. Alt text is a long descriptive keyword string ending in "Nevada Real Estate Group buyer guide". |
| 2 | **Hero caption** | `.hero-caption` | One italic line, often "Photo: Nevada Real Estate Group editorial." |
| 3 | **Breadcrumb** | `nav.blog-breadcrumb` | Home › Blog › Post Title |
| 4 | **Category eyebrow** | `.blog-card-category` | One of 10 categories (Buying Guides, Community Spotlight, Market Updates, News, Neighborhood Guides, Relocating, Selling Guides, Investment, Lifestyle) |
| 5 | **H1** | `h1.blog-post-title` | Serif, one per page, matches schema `headline` exactly |
| 6 | **Author box** | `.blog-author` | 56x56 headshot, "By Chris Nevada", "License S.181401", then `<time>` published, "· Updated" `<time>`, "· NN min read". All three metadata items on one line. |
| 7 | **Excerpt / dek** | `p.blog-post-excerpt` | 60 to 90 words, duplicates the meta description |
| 8 | **Table of contents** | `nav.toc > ol.toc-list` | See 1.2 |
| 9 | **Team-credibility aside** | `aside.blog-nreg-experience` | Cream box, gold left border, italic serif. Eyebrow "A note from the NREG team", then a production-stats paragraph (9,600+ career closings, $4.85B volume, 789 transactions in 2025), then a byline footer line. Same copy block reused across posts with the topic swapped. |
| 10 | **Direct Answer** | `blockquote.direct-answer` | Cream box, 4px gold left border. Opens with bold "Direct Answer:" then a 180 to 320 word summary that answers the title question completely, densely entity-linked. Sometimes doubled (a long one plus a one-sentence restatement). |
| 11 | **Key Takeaways** | `ul.key-takeaways` | Pale yellow box (`#fffaeb`, border `#fde6a8`), 4 to 6 bullets |
| 12 | **Authority paragraph** | plain `<p>` | "Across our 789 closings in 2025 … According to Las Vegas REALTORS …" Ties their own transaction volume to a public data source. |
| 13 | **Inline inventory CTA** | plain `<p>` | Bold "Want to see real inventory?" then a text link to `/<city>/homes-for-sale/`. **This is the only IDX touch inside the post body. There is no embedded IDX widget, no listing grid, no iframe.** |
| 14 | **Body: 13 to 18 H2 sections** | `.blog-post-body` | See 1.3 |
| 15 | **FAQ block** | `details.faq-item-blog` x 6-9 | Native `<details>/<summary>` accordions, `h3.faq-question` inside the summary, `.faq-answer` div. Gold border when open, "+" that rotates to "x". Mirrors `FAQPage` schema 1:1. |
| 16 | **"Which Industry Authorities Inform This Analysis?"** | H2 | 4 to 6 paragraphs, each literally starting "According to <linked authority>," followed by one hard statistic |
| 17 | **"Which Sources Inform This Analysis?"** | H2 | Bulleted list of 12 to 16 government/industry sources with outbound links and a one-line description each |
| 18 | **Hub link paragraph** | plain `<p>` | "For broader Las Vegas context, see our **new construction hub**, **luxury communities**, **Summerlin community guide**, and **Henderson community guide**." This is the deliberate authority pass-back. |
| 19 | **Compensation + freshness disclosure** | plain `<p>` | "NREG represents buyers at no cost to the buyer, the builder pays our commission" plus "All pricing data reflects <Month Year> conditions" |
| 20 | **About the Author** | `.blog-trust-block` | H3 "About This Article", then a 7-item bulleted E-E-A-T block: Author + license + `red.nv.gov` verify link, Brokerage + street address, Contact phone/email, MLS membership, Region focus, Compliance (Equal Housing / Fair Housing Act / NRS 645), **Last reviewed: <date>** |
| 21 | **Lead form** | `.blog-lead-form` | H3 "Talk to a Las Vegas real estate specialist", sub "Confidential consultation. No spam. We respond within 1 business hour, 8a-8p PT." Name / Phone / Email / Message, honeypot field, full TCPA-SMS consent paragraph, gold "Request Consultation" button. Hidden input carries `source=blog-<slug>`. |
| 22 | **"Related Reading"** | `section.related-posts` | Exactly **3** image cards. **Automated, not editorial: all 173 posts show the same 3 cards, which are the 3 newest posts site-wide.** |
| 23 | **"More from the Nevada Real Estate Group blog"** | `nav` | **6** text links. Also automated: they are the 6 alphabetically-adjacent post titles. Zero topical relevance. |
| 24 | **Fair Housing disclosure** | `aside.fair-housing-disclosure` | |
| 25 | **Footer: "← Back to Blog"** | `.blog-post-footer` | |
| 26 | **Sticky mobile CTA bar** | `.sticky-mobile-cta` | Fixed bottom, black bar, gold "Call Chris" + outlined "Free Consultation". Mobile only. |

### 1.2 The table of contents

**Yes, and on desktop it goes sticky, but conditionally.**

- Default: an inline boxed TOC directly under the author box. Cream background, 3px gold left border, uppercase 11px eyebrow, **two-column decimal ordered list**, `max-width:720px`.
- **CORRECTED BY QA (`07-qa-verification.md`, C1):** the two bullets above describe the
  **hub's** TOC (Component A: `h2.toc__title` + `ol.toc__list`, cream box, gold border,
  two-column decimal list). **Blog posts do not use that component and never go fixed.**
  Blog posts use Component B: `<details><summary>` + `ol.toc-list`, inline only, at every
  breakpoint. It receives none of the Component A styling rules.
- The fixed rail activates only via
  `@media (min-width:1024px){:is(body:has(.community-card) .toc, body:has(.nc-table) .toc){position:fixed;right:24px;…}}`
  which is true on exactly three pages: `/new-construction/`, `/builders/`, and
  `/55-plus-communities/`. **Community pages have no TOC at all** — the `.community-card`
  class appears only on `/55-plus-communities/`, which is what caused the original error here.
- The TOC lists **H2s only**. FAQ H3s are excluded. The list ends at "Which Industry Authorities…", so "Related Reading" and "More from the blog" are outside it.

### 1.3 Heading pattern

- **One H1.** Serif, `text-wrap:balance`, matches schema headline.
- **13 to 18 H2s**, median 15. **Almost every H2 is phrased as a question a buyer would type**, and the first word is a question word: What / Why / How / Who / Where / Which. Examples from the tier-ranking post: "What Defines a 'Top' New Construction Community in Las Vegas in 2026?", "How Do Builder Incentives Actually Work in Las Vegas in 2026?", "What Are the Hidden Costs Most New Construction Buyers Miss?"
- **H3s are almost exclusively the FAQ questions.** Body H3s are rare. Median H3 count equals the FAQ count.
- Under each H2: 2 to 4 paragraphs, then frequently a table or a bolded lead-in line ("Builder mix takeaway.", "Practical buyer guidance.", "Standing inventory advantage.") followed by a short paragraph. That bolded-lead-in device does the work a pull quote would.

### 1.4 What they do NOT have

- **No pull quotes.** `blockquote` is used only for the Direct Answer box (1 to 2 per post), never for a decorative quote.
- **No IDX embed inside the post.** Only a text link to a city `/homes-for-sale/` page.
- **No comments, no social share bar, no newsletter popup inside the article.**
- **No author bio card with credentials beyond the trust block.** The author box at the top is compact (photo + name + license + dates + read time).
- **No "last updated" callout in the body**, only in the author line and in the trust block's "Last reviewed".

### 1.5 Media

- Exactly **4 inline `<figure>` blocks** in 162 of 173 posts (5 in the other 11). Each figure image is **wrapped in a link**, `a.blog-figure__link`, usually pointing at `/new-construction/` or a builder or community page. Hover lifts and scales. Every figure has an italic figcaption that doubles as a mini-CTA ("NREG works with every major Las Vegas builder…").
- **Tables:** median 3, up to 8 in the incentives roundup. Styled `.blog-data-table`, navy `<thead>`, zebra rows, gold hover tint, horizontal scroll on mobile. A `--comparison` modifier turns the first column into a row header. Newer posts add a `caption` element styled as a source note.
- **Video:** the July 2026 posts add one `.blog-video-embed` YouTube iframe, usually mid-article after the pricing section. 27 of 173.

### 1.6 Schema (JSON-LD)

**One `<script type="application/ld+json">` per page containing an `@graph` with 7 nodes**, identical structure on every post:

1. `WebSite` (with `SearchAction`)
2. `ImageObject` (the logo)
3. `RealEstateAgent` (the brokerage: NAP, geo, `openingHours`, `areaServed` array of Clark County cities)
4. `Person` (Chris Nevada, `@id` `#chris-nevada`)
5. **`BlogPosting`** with: `headline`, `description`, `datePublished`, **`dateModified`**, **`wordCount`** (a real count, 3.5k to 6.2k), `image` array (3 crops: 16:9, 4:3, 1:1), **`keywords` array of exactly 25 terms**, `inLanguage`, `author` `@id` ref, `publisher` `@id` ref, `isPartOf`, `mainEntityOfPage`, `articleSection`, and a **`speakable`** SpeakableSpecification with `cssSelector: [".direct-answer", ".key-takeaways", ".faq-answer"]`
6. `BreadcrumbList` (Home / Blog / Post)
7. **`FAQPage`** with 6 to 9 `Question` entities matching the on-page accordions exactly

Note `articleSection` in schema does **not** always match the visible category chip. The chip is the CMS category ("Community Spotlight"), the schema often says "Buying Tips".

The `speakable` selectors are the tell: this template is engineered for AI answer engines and voice assistants first, human readers second. Their robots.txt explicitly opts in every AI crawler, and the Direct Answer / Key Takeaways / FAQ triple is the extraction surface.

### 1.7 Reading time

Displayed in the author line and on every blog index card as "NN min read". Range across the NC cluster: 8 to 26 minutes, but 145 of 173 say 18 to 22. It is computed, not authored (it tracks `wordCount` at roughly 230 wpm).

---

## 2. FULL INVENTORY

173 Las Vegas metro new-construction-adjacent posts, grouped by theme, newest first inside each group.

Column notes: **Words** is the schema `wordCount`. **Int. links** counts every internal `<a>` inside `.blog-post-body` (excluding nav, footer, related-posts). **Links to hub / spokes** shows whether the body links to `/new-construction/` plus which builder and geo entity pages it feeds.

### A. Builder model / floor-plan spotlight  (26 posts)

| URL (`/blog/…`) | Title | Pub | Updated | Words | TOC | H2s | FAQ | Tables | Int. links | Primary keyword | Links to hub / spokes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `lennar-rocco-nextgen-lake-las-vegas-price-drop-2026` | Lennar Rocco Next Gen at Lake Las Vegas: $147K Drop 2026 | 2026-07-24 | 2026-07-24 | 3962 | Y | 16 | 7 | 3 | 28 | Lennar Rocco Next Gen | NC hub; geo: henderson, las-vegas, luxury-communities, summerlin |
| `lennar-ganon-next-gen-rv-garage-lone-mountain-2026` | Lennar Ganon Next Gen w/ RV Garage in Lone Mountain 2026 | 2026-07-21 | 2026-07-21 | 4033 | Y | 14 | 7 | 3 | 23 | Lennar Ganon Next Gen | NC hub; geo: luxury-communities, summerlin |
| `century-residence-1831-bluffs-lake-las-vegas-2026` | Century Residence 1831 at Lake Las Vegas Henderson 2026 | 2026-07-19 | 2026-07-19 | 3911 | Y | 14 | 6 | 4 | 21 | Century Residence 1831 | NC hub; builders: century-communities; geo: henderson, las-vegas |
| `dr-horton-plan-2538-heartland-manor-north-las-vegas-2026` | D.R. Horton Plan 2538 Heartland Manor North Las Vegas 2026 | 2026-07-19 | 2026-07-19 | 4170 | Y | 16 | 6 | 4 | 20 | D.R. Horton Plan 2538 | NC hub; builders: dr-horton; geo: las-vegas, north-las-vegas |
| `dr-horton-plan-2660-symmetry-falls-cadence-henderson-2026` | D.R. Horton Plan 2660 at Symmetry Falls Cadence 2026 | 2026-07-19 | 2026-07-19 | 3936 | Y | 15 | 6 | 4 | 18 | D.R. Horton Plan 2660 | NC hub; builders: dr-horton; geo: henderson |
| `dr-horton-plan-2754-multi-gen-cadence-henderson-2026` | D.R. Horton Plan 2754 Multi-Gen at Cadence Henderson 2026 | 2026-07-19 | 2026-07-19 | 4023 | Y | 15 | 6 | 4 | 19 | D.R. Horton Plan 2754 | NC hub; builders: dr-horton; geo: henderson, las-vegas |
| `kb-home-plan-2124-open-layout-las-vegas-2026` | KB Home Plan 2124: Open Layout Las Vegas New Home 2026 | 2026-07-19 | 2026-07-19 | 3988 | Y | 15 | 6 | 4 | 21 | KB Home Plan 2124 | NC hub; geo: las-vegas |
| `kb-home-plan-2320-peaks-at-meriden-henderson-2026` | KB Home Plan 2320: Peaks at Meriden Henderson 2026 | 2026-07-19 | 2026-07-19 | 4143 | Y | 16 | 6 | 5 | 21 | KB Home Plan 2320 | NC hub; geo: henderson, las-vegas |
| `kb-home-plan-2469-landings-inspirada-henderson-2026` | KB Home Plan 2469: Landings at Inspirada Henderson 2026 | 2026-07-19 | 2026-07-19 | 3882 | Y | 15 | 6 | 4 | 20 | KB Home Plan 2469 | NC hub; geo: henderson, las-vegas |
| `kb-home-plan-3095-reserves-cloudbreak-ridge-summerlin-2026` | KB Home Plan 3095 at Cloudbreak Ridge Summerlin 2026 | 2026-07-19 | 2026-07-19 | 4201 | Y | 15 | 6 | 5 | 18 | KB Home Plan 3095 | NC hub; geo: las-vegas, summerlin |
| `lennar-astor-model-cadence-henderson-2026` | Lennar Astor Model: 3-Story Cadence Home Henderson 2026 | 2026-07-19 | 2026-07-19 | 3979 | Y | 16 | 6 | 5 | 18 | Lennar Astor model | NC hub; geo: henderson, las-vegas |
| `lennar-greg-next-gen-mockingbird-summerlin-2026` | Lennar Greg Next Gen: Mockingbird Summerlin Home 2026 | 2026-07-19 | 2026-07-19 | 3974 | Y | 15 | 6 | 5 | 18 | Lennar Greg Next Gen | NC hub; geo: las-vegas, summerlin |
| `lennar-jan-model-downstairs-suite-las-vegas-2026` | Lennar Jan Model: Rare Downstairs Suite Home Las Vegas 2026 | 2026-07-19 | 2026-07-19 | 3949 | Y | 16 | 6 | 5 | 17 | Lennar Jan model | NC hub; geo: las-vegas, summerlin |
| `lennar-justin-next-gen-home-southwest-las-vegas-2026` | Lennar Justin Next Gen Multigen Home Las Vegas 2026 | 2026-07-19 | 2026-07-19 | 3998 | Y | 15 | 7 | 4 | 17 | Lennar Justin Next Gen | NC hub; geo: las-vegas |
| `lennar-peter-model-first-floor-primary-summerlin-2026` | Lennar Peter Model: First-Floor Primary Suite Summerlin 2026 | 2026-07-19 | 2026-07-19 | 3971 | Y | 16 | 6 | 5 | 17 | Lennar Peter model | NC hub; geo: las-vegas, luxury-communities, summerlin |
| `richmond-american-darius-newbridge-rv-garage-las-vegas-2026` | Richmond American Darius at Newbridge Las Vegas 2026 | 2026-07-19 | 2026-07-19 | 4040 | Y | 15 | 6 | 3 | 18 | Richmond American Darius | NC hub; builders: richmond-american; geo: las-vegas |
| `richmond-american-elm-lexington-chase-las-vegas-2026` | Richmond American Elm at Lexington Chase Las Vegas 2026 | 2026-07-19 | 2026-07-19 | 3912 | Y | 15 | 6 | 4 | 19 | Richmond American Elm | NC hub; builders: richmond-american; geo: las-vegas |
| `taylor-morrison-sinatra-model-summerlin-2026` | Taylor Morrison Sinatra Model: Summerlin Resort Luxury 2026 | 2026-07-19 | 2026-07-19 | 4348 | Y | 15 | 7 | 5 | 18 | Taylor Morrison Sinatra model | NC hub; geo: las-vegas, luxury-communities, summerlin |
| `toll-brothers-westcliff-glenrock-summerlin-west-2026` | Toll Brothers Westcliff at Glenrock Summerlin 2026 | 2026-07-19 | 2026-07-19 | 4008 | Y | 15 | 6 | 4 | 20 | Toll Brothers Westcliff | NC hub; builders: toll-brothers; geo: las-vegas, luxury-communities, summerlin |
| `tri-pointe-aberdeen-plan-3-gated-summerlin-west-2026` | Tri Pointe Aberdeen Plan 3 Gated Summerlin West 2026 | 2026-07-19 | 2026-07-19 | 3836 | Y | 15 | 6 | 4 | 19 | Tri Pointe Aberdeen | NC hub; builders: tri-pointe; geo: las-vegas, summerlin |
| `tri-pointe-vela-plan-3-inspirada-henderson-2026` | Tri Pointe Vela Plan 3 at Inspirada Henderson 2026 | 2026-07-19 | 2026-07-19 | 3985 | Y | 15 | 6 | 4 | 20 | Tri Pointe Vela | NC hub; builders: tri-pointe; geo: henderson, las-vegas |
| `woodside-cedar-plan-2-ashwood-cadence-henderson-2026` | Woodside Cedar Plan 2 at Ashwood Cadence Henderson 2026 | 2026-07-19 | 2026-07-19 | 3842 | Y | 14 | 6 | 4 | 20 | Woodside Cedar Plan 2 | NC hub; builders: woodside; geo: henderson, las-vegas |
| `juniper-model-summerlin-earthquake-resistant-home-2026` | Juniper Model: Earthquake-Resistant Summerlin Home 2026 | 2026-07-06 | 2026-07-06 | 3987 | Y | 15 | 7 | 4 | 16 | earthquake resistant homes Las Vegas | NC hub; geo: henderson, luxury-communities, summerlin |
| `samuel-next-gen-decano-southwest-las-vegas-2026` | Samuel Next Gen at Decano: Southwest Las Vegas 2026 | 2026-07-06 | 2026-07-06 | 3986 | Y | 14 | 8 | 4 | 15 | Samuel Next Gen | NC hub; geo: enterprise/new-construction |
| `the-henry-eleanor-nextgen-single-story-las-vegas-2026` | The Henry's Eleanor Next Gen: Southwest Las Vegas 2026 | 2026-07-05 | 2026-07-05 | 4039 | Y | 12 | 8 | 3 | 19 | The Henry Las Vegas | NC hub; geo: mountains-edge |
| `triad-springs-lennar-carol-model-las-vegas-2026` | The Carol Model at Triad Springs by Lennar (Las Vegas 2026) | 2026-07-05 | 2026-07-05 | 3973 | Y | 15 | 8 | 4 | 16 | Triad Springs Lennar | NC hub; geo: enterprise/new-construction |

### B. Builder comparison / brand roundup  (8 posts)

| URL (`/blog/…`) | Title | Pub | Updated | Words | TOC | H2s | FAQ | Tables | Int. links | Primary keyword | Links to hub / spokes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `las-vegas-home-builders-compared-2026` | Las Vegas Home Builders Compared: 2026 Buyer's Guide | 2026-07-10 | 2026-07-10 | 3493 | Y | 13 | 7 | 3 | 20 | home-builders | NC hub; geo: henderson, luxury-communities, north-las-vegas, summerlin |
| `tri-pointe-homes-las-vegas-communities-2026` | Tri Pointe Homes Las Vegas Communities Guide 2026 | 2026-06-20 | 2026-06-20 | 4379 | Y | 13 | 7 | 6 | 20 | Tri Pointe Homes | NC hub; geo: henderson, las-vegas, north-las-vegas, summerlin |
| `top-luxury-home-builders-las-vegas-2026` | Top Luxury Home Builders in Las Vegas 2026 | 2026-05-18 | 2026-06-14 | 5416 | Y | 16 | 6 | 3 | 31 | Las Vegas real estate | NC hub; geo: henderson, las-vegas, luxury-communities, summerlin |
| `christopher-homes-blue-heron-toll-brothers-summerlin-comparison-2026` | Christopher Homes vs Blue Heron vs Toll Brothers: Which Luxury Builder W | 2026-05-11 | 2026-05-11 | 5303 | Y | 14 | 9 | 3 | 52 | Christopher Homes | NC hub; builders: toll-brothers; geo: henderson, lake-las-vegas, las-vegas, summerlin |
| `villages-tule-springs-heartland-dr-horton-comparison-2026` | Villages at Tule Springs vs Heartland: Which D.R. Horton NLV Community I | 2026-05-11 | 2026-05-26 | 4722 | Y | 14 | 9 | 3 | 53 | Tule Springs Las Vegas | NC hub; builders: dr-horton; geo: cadence, henderson, inspirada, las-vegas |
| `vista-cielo-harmony-homes-las-vegas-affordable-2026` | Vista Cielo by Harmony Homes: Las Vegas's Most Affordable New Constructi | 2026-05-11 | 2026-05-27 | 5022 | Y | 14 | 9 | 3 | 35 | Vista Cielo | NC hub; builders: dr-horton, harmony, kb-home, lennar; geo: aliante, henderson, las-vegas, luxury-communities |
| `watercolor-touchstone-living-las-vegas-snhba-community-2026` | Watercolor by Touchstone Living: SNHBA Community of the Year 2025 Breakd | 2026-05-11 | 2026-05-27 | 4990 | Y | 15 | 9 | 3 | 49 | Watercolor Las Vegas | NC hub; builders: kb-home, lennar, pulte-del-webb, richmond-american; geo: aliante, cadence, henderson, inspirada |
| `touchstone-living-las-vegas-homes-2026` | Touchstone Living Homes in Las Vegas: Independence, Watercolor & What Bu | 2026-05-08 | 2026-05-08 | 5592 | Y | 16 | 8 | 6 | 42 | Touchstone Living | NC hub; builders: dr-horton, harmony, kb-home, lennar; geo: centennial-hills, henderson, las-vegas, luxury-communities |

### C. Incentives, credits & builder negotiation  (7 posts)

| URL (`/blog/…`) | Title | Pub | Updated | Words | TOC | H2s | FAQ | Tables | Int. links | Primary keyword | Links to hub / spokes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `mortgage-rate-buydown-vs-rate-lock-nevada-2026` | Rate Buydowns vs Rate Locks in Nevada: Which Saves More 2026 | 2026-07-08 | 2026-07-08 | 4056 | Y | 12 | 6 | 3 | 20 | rate buydown vs rate lock | NC hub |
| `2-1-buydown-las-vegas-new-construction-2026` | The 2-1 Rate Buydown Explained: Is the Builder Actually Paying for It? ( | 2026-05-11 | 2026-05-27 | 5262 | Y | 15 | 9 | 5 | 29 | 2-1 buydown | NC hub; builders: dr-horton, kb-home, lennar, pulte-del-webb; geo: cadence, henderson, inspirada, las-vegas |
| `builder-closing-cost-credits-las-vegas-2026` | How Much Do Builder Closing Cost Credits Actually Save You in Las Vegas? | 2026-05-11 | 2026-05-27 | 4841 | Y | 14 | 9 | 8 | 28 | builder closing cost credits | NC hub; builders: dr-horton, kb-home, lennar, pulte-del-webb; geo: henderson, las-vegas, north-las-vegas, summerlin |
| `builder-contract-clauses-negotiate-las-vegas-2026` | Builder Contract Red Flags: 12 Clauses to Negotiate Before You Sign in L | 2026-05-11 | 2026-05-28 | 5973 | Y | 18 | 9 | 3 | 35 | builder contract clauses | NC hub; builders: dr-horton, kb-home, lennar, pulte-del-webb; geo: aliante, henderson, las-vegas, summerlin |
| `design-center-budget-las-vegas-new-construction-2026` | Design Center Budgeting in Las Vegas: How to Spend $30K Without Wasting  | 2026-05-11 | 2026-05-27 | 5503 | Y | 14 | 9 | 3 | 25 | design center | NC hub; builders: dr-horton, kb-home, lennar, pulte-del-webb; geo: henderson, las-vegas, north-las-vegas, summerlin |
| `lot-premium-negotiation-las-vegas-new-construction-2026` | Lot Premium Negotiation in Las Vegas New Construction: What's Actually N | 2026-05-11 | 2026-05-27 | 5173 | Y | 15 | 9 | 3 | 90 | lot premium | NC hub; builders: dr-horton, kb-home, lennar, pulte-del-webb; geo: aliante, anthem, cadence, henderson |
| `new-construction-incentives-las-vegas-may-2026-builder-roundup` | New Construction Incentives in Las Vegas: May 2026 Builder Roundup | 2026-05-11 | 2026-05-27 | 4841 | Y | 14 | 9 | 8 | 28 | builder closing cost credits | NC hub; builders: dr-horton, kb-home, lennar, pulte-del-webb; geo: henderson, las-vegas, north-las-vegas, summerlin |

### D. New-construction process / how-to  (11 posts)

| URL (`/blog/…`) | Title | Pub | Updated | Words | TOC | H2s | FAQ | Tables | Int. links | Primary keyword | Links to hub / spokes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `are-home-warranties-worth-it-las-vegas-2026` | Are Home Warranties Worth It in Las Vegas? 2026 Guide | 2026-07-04 | 2026-07-04 | 3984 | Y | 13 | 8 | 3 | 21 | home warranty Las Vegas | NC hub; geo: centennial-hills, henderson, las-vegas, north-las-vegas |
| `do-you-need-realtor-new-construction-las-vegas-2026` | Do You Need a Realtor for New Construction? Las Vegas 2026 | 2026-07-04 | 2026-07-04 | 3988 | Y | 15 | 8 | 4 | 16 | realtor for new construction | NC hub; geo: cadence, henderson, north-las-vegas, skye-canyon |
| `spec-vs-custom-vs-production-homes-las-vegas-2026` | Spec vs Custom vs Production Homes in Las Vegas 2026 | 2026-06-02 | 2026-06-02 | 3847 | Y | 16 | 7 | 4 | 22 | spec homes las vegas | NC hub; geo: henderson, luxury-communities, summerlin |
| `best-real-estate-agent-for-new-construction-in-las-vegas-your-2026-guide-to-builder-negotiations-and-expert-representation` | Best Real Estate Agent for New Construction in Las Vegas: Your 2026 Guid | 2026-05-28 | 2026-07-14 | 5842 | Y | 18 | 7 | 5 | 48 | Las Vegas real estate | geo: anthem, cadence, henderson, inspirada |
| `10-tips-to-buying-a-new-construction-home` | 10 Tips To Buying A New Construction Home | 2026-05-11 | 2026-05-11 | 5620 | Y | 15 | 9 | 4 | 37 | first-time buyer | NC hub; builders: dr-horton, kb-home, lennar, pulte-del-webb; geo: cadence, henderson, inspirada, las-vegas |
| `first-time-buyer-new-construction-mistakes-las-vegas-2026` | The 7 Mistakes First-Time New Construction Buyers Make in Las Vegas (and | 2026-05-11 | 2026-05-11 | 5620 | Y | 15 | 9 | 4 | 37 | first-time buyer | NC hub; builders: dr-horton, kb-home, lennar, pulte-del-webb; geo: cadence, henderson, inspirada, las-vegas |
| `nevada-new-home-warranty-1-2-10-year-coverage-2026` | Nevada's New Home Warranty Explained: What 1/2/10 Year Coverage Actually | 2026-05-11 | 2026-05-11 | 5670 | Y | 14 | 9 | 3 | 40 | Nevada new home warranty | NC hub; builders: dr-horton, kb-home, lennar, pulte-del-webb; geo: centennial-hills, henderson, las-vegas, luxury-communities |
| `new-construction-timeline-las-vegas-build-reality-2026` | Build Time Reality: Why Your '6 Month' New Home Will Actually Take 9-11  | 2026-05-11 | 2026-05-27 | 5770 | Y | 14 | 9 | 4 | 50 | new construction timeline | NC hub; builders: dr-horton, kb-home, lennar, pulte-del-webb; geo: aliante, henderson, las-vegas, luxury-communities |
| `pre-drywall-inspection-new-construction-las-vegas-2026` | The Pre-Drywall Inspection: Why You Need a Third-Party Inspector on Your | 2026-05-11 | 2026-05-27 | 5366 | Y | 15 | 9 | 3 | 23 | pre-drywall inspection | NC hub; builders: dr-horton, kb-home, lennar, pulte-del-webb; geo: henderson, las-vegas, luxury-communities, summerlin |
| `build-from-scratch-in-summerlin` | Building a Custom Home in Summerlin, NV: The Ultimate Guide for 2026 | 2026-03-05 | 2026-07-12 | 4271 | Y | 15 | 7 | 4 | 25 | Las Vegas real estate | NC hub; geo: luxury-communities, summerlin, summerlin/new-construction |
| `build-from-scratch-in-las-vegas` | How to Build a Custom Home in Las Vegas: The Ultimate 2026 Guide | 2026-03-04 | 2026-07-13 | 4432 | Y | 15 | 7 | 5 | 32 | Las Vegas real estate | NC hub; geo: henderson, las-vegas, luxury-communities, summerlin |

### E. New build vs resale comparison  (5 posts)

| URL (`/blog/…`) | Title | Pub | Updated | Words | TOC | H2s | FAQ | Tables | Int. links | Primary keyword | Links to hub / spokes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `las-vegas-new-construction-vs-resale-2026` | Las Vegas New Construction vs Resale: Which Wins in 2026? | 2026-05-17 | 2026-06-14 | 4426 | Y | 15 | 6 | 3 | 28 | Las Vegas real estate | NC hub; geo: centennial-hills, henderson, las-vegas, luxury-communities |
| `new-construction-vs-resale-las-vegas-2026-comparison` | New Construction vs Resale Las Vegas 2026 Comparison | 2026-05-17 | 2026-06-14 | 4426 | Y | 15 | 6 | 3 | 28 | Las Vegas real estate | NC hub; geo: centennial-hills, henderson, las-vegas, luxury-communities |
| `new-construction-resale-las-vegas-decision-matrix-2026` | New Construction vs Resale in Las Vegas: When Each One Actually Wins (20 | 2026-05-11 | 2026-05-27 | 5629 | Y | 14 | 9 | 5 | 32 | new construction vs resale | NC hub; builders: dr-horton, kb-home, lennar, pulte-del-webb; geo: aliante, anthem, cadence, henderson |
| `new-construction-vs-resale-las-vegas-2026-decision` | New Construction vs. Resale in Las Vegas: The 2026 Decision | 2026-05-11 | 2026-05-27 | 5629 | Y | 14 | 9 | 5 | 32 | new construction vs resale | NC hub; builders: dr-horton, kb-home, lennar, pulte-del-webb; geo: aliante, anthem, cadence, henderson |
| `vegas-new-build-700k-vs-summerlin-2026` | Vegas New Build $700K vs Summerlin: Better Value in 2026? | 2026-05-02 | 2026-05-02 | 5778 | Y | 20 | 8 | 6 | 22 | Las Vegas real estate | NC hub; geo: centennial-hills, henderson, las-vegas, luxury-communities |

### F. Cost, tax & fee explainers  (12 posts)

| URL (`/blog/…`) | Title | Pub | Updated | Words | TOC | H2s | FAQ | Tables | Int. links | Primary keyword | Links to hub / spokes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `how-much-money-to-buy-a-house-in-summerlin-2026` | How Much Money to Buy a House in Summerlin in 2026? | 2026-07-16 | 2026-07-16 | 5734 | Y | 15 | 7 | 3 | 22 | Las Vegas real estate | NC hub; geo: henderson, las-vegas, luxury-communities, north-las-vegas |
| `sid-lid-balance-las-vegas-resale-homes-buyer-guide-2026` | SID and LID Balance on Las Vegas Resale Homes 2026 | 2026-07-13 | 2026-07-13 | 5381 | Y | 16 | 7 | 4 | 25 | Las Vegas real estate | NC hub; geo: henderson, las-vegas, mountains-edge, providence |
| `selling-your-henderson-home-process-costs-2026` | Selling Your Henderson Home: 2026 Process & Costs Guide | 2026-07-12 | 2026-07-12 | 5013 | Y | 15 | 7 | 4 | 37 | Las Vegas real estate | NC hub; geo: henderson, las-vegas, luxury-communities |
| `nevada-property-tax-cap-3-vs-8-percent-2026` | Nevada Property Tax Cap: 3% vs 8% in Clark County 2026 | 2026-06-14 | 2026-06-14 | 4379 | Y | 16 | 7 | 4 | 35 | Las Vegas real estate | NC hub; geo: henderson, las-vegas, north-las-vegas, summerlin |
| `sid-lid-taxes-las-vegas-new-construction-2026` | SID and LID Taxes Las Vegas New Construction 2026 | 2026-05-19 | 2026-05-27 | 5891 | Y | 18 | 6 | 3 | 30 | Las Vegas real estate | NC hub; geo: cadence, henderson, inspirada, mountains-edge |
| `las-vegas-closing-costs-2026-buyer-seller-breakdown` | Las Vegas Closing Costs 2026 Buyer and Seller Breakdown | 2026-05-17 | 2026-06-14 | 4356 | Y | 15 | 6 | 5 | 37 | Las Vegas real estate | NC hub; geo: anthem, cadence, centennial-hills, henderson |
| `las-vegas-property-tax-guide` | Las Vegas Property Taxes 2026: What Clark County Homeowners Actually Pay | 2026-05-17 | 2026-07-14 | 5708 | Y | 18 | 7 | 5 | 35 | Las Vegas real estate | NC hub; geo: 55-plus-communities, centennial-hills, henderson, las-vegas |
| `las-vegas-property-taxes-explained-2026` | Las Vegas Property Taxes Explained 2026 Buyer Guide | 2026-05-17 | 2026-07-14 | 5708 | Y | 18 | 7 | 5 | 35 | Las Vegas real estate | NC hub; geo: 55-plus-communities, centennial-hills, henderson, las-vegas |
| `clark-county-property-tax-reassessment-new-construction-2026` | Why Your Property Tax Bill Doubles in Year 2 of a New Build (Clark Count | 2026-05-11 | 2026-05-11 | 5380 | Y | 15 | 9 | 3 | 38 | Clark County property tax | NC hub; builders: dr-horton, lennar; geo: cadence, henderson, inspirada, lake-las-vegas |
| `sid-lid-fees-cadence-inspirada-henderson-2026` | SID and LID Fees Explained: The Hidden $7K-$20K on Your Cadence or Inspi | 2026-05-11 | 2026-05-11 | 5325 | Y | 15 | 9 | 3 | 39 | SID LID fees | NC hub; geo: aliante, anthem, cadence, henderson |
| `las-vegas-home-costs-2026` | What Homes Actually Cost in Las Vegas Right Now: 2026 Market Update | 2026-03-05 | 2026-07-14 | 5078 | Y | 15 | 7 | 4 | 27 | Las Vegas real estate | NC hub; geo: henderson, las-vegas, luxury-communities, north-las-vegas |
| `property-taxes-summerlin` | Summerlin Property Taxes: A 2026 Homeowner's Guide | 2026-03-05 | 2026-07-12 | 4126 | Y | 15 | 7 | 4 | 21 | Las Vegas real estate | NC hub; geo: henderson, las-vegas, luxury-communities, summerlin |

### G. HOA, legal & compliance  (7 posts)

| URL (`/blog/…`) | Title | Pub | Updated | Words | TOC | H2s | FAQ | Tables | Int. links | Primary keyword | Links to hub / spokes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `new-nevada-housing-laws-2026-adu-hoa-rules` | New Nevada Housing Laws in 2026: ADUs, HOAs & Rules | 2026-07-20 | 2026-07-20 | 4210 | Y | 14 | 7 | 3 | 19 | Las Vegas real estate | NC hub; geo: henderson, las-vegas, luxury-communities, north-las-vegas |
| `hoa-fees-henderson-2026` | Henderson HOA Fees Explained: What to Expect in 2026 | 2026-06-30 | 2026-06-30 | 3615 | Y | 13 | 7 | 3 | 24 | Las Vegas real estate | NC hub; geo: 55-plus-communities, henderson, luxury-communities, summerlin |
| `henderson-hoa-special-assessments-reserve-study-guide-2026` | Henderson HOA Special Assessments & Reserves 2026 | 2026-06-21 | 2026-06-21 | 4918 | Y | 15 | 6 | 3 | 27 | Las Vegas real estate | geo: henderson, las-vegas |
| `henderson-homes-with-no-hoa-where-to-buy-2026` | Henderson Homes With No HOA: Where to Buy in 2026 | 2026-06-21 | 2026-06-21 | 5182 | Y | 13 | 6 | 3 | 11 | Las Vegas real estate | geo: henderson, las-vegas |
| `hoa-landscape-requirements-new-construction-las-vegas-2026` | The HOA Dirt-to-Landscape Surprise: Budget $10K-$25K After Closing in La | 2026-05-11 | 2026-05-27 | 5294 | Y | 15 | 9 | 5 | 41 | HOA landscape Las Vegas | NC hub; builders: dr-horton, kb-home, lennar, pulte-del-webb; geo: cadence, henderson, inspirada, las-vegas |
| `nevada-hoa-fines-your-nrs-116` | Nevada HOA Fines: Your NRS 116 Rights in 2026 | 2026-04-29 | 2026-04-29 | 5753 | Y | 25 | 6 | 3 | 24 | Nevada HOA rules | NC hub; geo: henderson, las-vegas, north-las-vegas, summerlin |
| `hoa-fees-summerlin` | Summerlin HOA Fees Explained: 2026 Rates & Cost Guide | 2026-03-05 | 2026-07-12 | 4044 | Y | 16 | 7 | 4 | 21 | Las Vegas real estate | NC hub; geo: henderson, las-vegas, luxury-communities, summerlin |

### H. 55+ / active-adult new build  (7 posts)

| URL (`/blog/…`) | Title | Pub | Updated | Words | TOC | H2s | FAQ | Tables | Int. links | Primary keyword | Links to hub / spokes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `solera-at-anthem-henderson-55-plus-active-adult-guide-2026` | Solera at Anthem Henderson: Guard-Gated 55+ Guide 2026 | 2026-07-25 | 2026-07-25 | 5120 | Y | 14 | 8 | 3 | 21 | Las Vegas real estate | NC hub; geo: 55-plus-communities, aliante, anthem, henderson |
| `siena-summerlin-shea-homes-55-plus-active-adult-guide-2026` | Siena Summerlin Shea Homes 55+ Active Adult Guide 2026 | 2026-05-25 | 2026-05-28 | 3762 | Y | 15 | 7 | 4 | 22 | Las Vegas real estate | geo: anthem, henderson, las-vegas, luxury-communities |
| `trilogy-sunstone-northwest-las-vegas-55-plus-buyers-guide-2026` | Trilogy Sunstone Northwest Las Vegas 55-Plus Guide 2026 | 2026-05-24 | 2026-05-26 | 4094 | Y | 15 | 7 | 3 | 18 | Las Vegas real estate | geo: aliante, anthem, centennial-hills, henderson |
| `sun-city-anthem-henderson-55-plus-active-adult-master-plan-guide-2026` | Sun City Anthem Henderson: 2026 Active Adult Guide | 2026-05-22 | 2026-05-28 | 4658 | Y | 14 | 7 | 3 | 26 | Las Vegas real estate | geo: 55-plus-communities, aliante, anthem, centennial-hills |
| `sun-city-summerlin-55-plus-active-adult-master-plan-guide-2026` | Sun City Summerlin: 2026 Active Adult Master-Plan Guide | 2026-05-22 | 2026-05-27 | 4662 | Y | 14 | 7 | 3 | 24 | Las Vegas real estate | geo: 55-plus-communities, aliante, anthem, cadence |
| `heritage-stonebridge-regency-summerlin-55-plus-comparison-2026` | Heritage at Stonebridge vs Regency at Summerlin: The 55+ New Build Showd | 2026-05-11 | 2026-05-27 | 4893 | Y | 14 | 9 | 3 | 35 | Heritage at Stonebridge | NC hub; builders: lennar, toll-brothers; geo: 55-plus-communities, henderson, las-vegas, summerlin |
| `55-plus-communities-las-vegas-complete-guide-2026` | 55+ Communities in Las Vegas: Every Active-Adult Community Ranked for 20 | 2026-05-10 | 2026-07-09 | 4522 | Y | 14 | 8 | 4 | 35 | 55 plus communities Las Vegas | builders: lennar, toll-brothers; geo: 55-plus-communities, aliante, anthem, cadence |

### I. Market data & construction news  (10 posts)

| URL (`/blog/…`) | Title | Pub | Updated | Words | TOC | H2s | FAQ | Tables | Int. links | Primary keyword | Links to hub / spokes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `summerlin-real-estate-market-report-june-2026` | Summerlin Real Estate Market Report June 2026 | 2026-07-18 | 2026-07-18 | 4131 | Y | 15 | 7 | 4 | 20 | Summerlin real estate | NC hub; geo: henderson, luxury-communities, summerlin |
| `new-master-planned-communities-las-vegas-pipeline-2026` | New Master-Planned Communities in Las Vegas: 2026 Pipeline | 2026-07-10 | 2026-07-10 | 3943 | Y | 14 | 7 | 3 | 26 | master-planned-communities | NC hub; geo: henderson, north-las-vegas, summerlin |
| `north-las-vegas-housing-market` | North Las Vegas Housing Market: Prices & Forecast 2026 | 2026-07-08 | 2026-07-09 | 4781 | Y | 18 | 7 | 4 | 30 | North Las Vegas housing market | NC hub; geo: henderson, north-las-vegas, summerlin |
| `las-vegas-construction-boom` | Las Vegas Is in the Middle of a $30 Billion Construction Boom | 2026-04-30 | 2026-04-30 | 4187 | Y | 15 | 6 | 3 | 28 | Las Vegas real estate | NC hub; geo: centennial-hills, henderson, las-vegas, luxury-communities |
| `las-vegas-home-prices-2026-up` | Las Vegas Home Prices 2026: Up or Down? | 2026-04-30 | 2026-07-13 | 4519 | Y | 15 | 7 | 6 | 29 | Las Vegas real estate | NC hub; geo: centennial-hills, henderson, las-vegas, luxury-communities |
| `las-vegas-homebuilder-sales` | Las Vegas Homebuilder Sales Drop in Early 2026: What It Means for Buyers | 2026-04-30 | 2026-04-30 | 4219 | Y | 14 | 6 | 3 | 27 | Las Vegas real estate | NC hub; geo: centennial-hills, henderson, las-vegas, luxury-communities |
| `las-vegas-sports-boom-real-estate` | NBA Arena, A's Ballpark, and the Stadium District: How Sports Are Reshap | 2026-04-30 | 2026-05-27 | 4162 | Y | 15 | 6 | 3 | 29 | Las Vegas real estate | NC hub; geo: centennial-hills, henderson, las-vegas, luxury-communities |
| `summerlin-housing-market-2026` | Summerlin Housing Market 2026: Median Price Hits $682K as Demand Outpace | 2026-01-23 | 2026-07-14 | 6006 | Y | 15 | 7 | 4 | 41 | Las Vegas real estate | NC hub; geo: henderson, las-vegas, luxury-communities, north-las-vegas |
| `summerlin-housing-market` | Summerlin Housing Market 2026: Prices and Trends | 2026-01-23 | 2026-07-14 | 6006 | Y | 15 | 7 | 4 | 41 | Las Vegas real estate | NC hub; geo: henderson, las-vegas, luxury-communities, north-las-vegas |
| `las-vegas-housing-market-2026` | Las Vegas Housing Market 2026 Forecast: Will Prices Rise? | 2026-01-22 | 2026-07-14 | 5803 | Y | 15 | 7 | 4 | 51 | Las Vegas real estate | NC hub; geo: henderson, las-vegas, luxury-communities, north-las-vegas |

### J. Where-to-buy rankings & geo NC hubs  (8 posts)

| URL (`/blog/…`) | Title | Pub | Updated | Words | TOC | H2s | FAQ | Tables | Int. links | Primary keyword | Links to hub / spokes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `new-construction-homes-henderson-builders-guide-2026` | New Construction Homes in Henderson: 2026 Builders Guide | 2026-07-12 | 2026-07-12 | 4769 | Y | 15 | 7 | 4 | 32 | Las Vegas real estate | NC hub; builders: dr-horton, kb-home, lennar, pulte-del-webb; geo: henderson, henderson/new-construction, las-vegas, luxury-communities |
| `new-construction-homes-north-las-vegas-guide-2026` | New Construction Homes in North Las Vegas: 2026 Guide | 2026-07-12 | 2026-07-12 | 5299 | Y | 16 | 7 | 4 | 44 | Las Vegas real estate | NC hub; builders: century-communities, dr-horton, kb-home, lennar; geo: henderson, las-vegas, luxury-communities, north-las-vegas |
| `southwest-las-vegas-new-construction-homes-town-square-2026` | Southwest Las Vegas New Construction Near Town Square 2026 | 2026-07-05 | 2026-07-05 | 4271 | Y | 16 | 8 | 4 | 23 | Southwest Las Vegas new construction | NC hub; geo: enterprise/new-construction, las-vegas |
| `master-planned-communities-las-vegas-ranked-2026` | Las Vegas Master-Planned Communities Ranked 2026 | 2026-07-02 | 2026-07-02 | 3990 | Y | 17 | 7 | 4 | 27 | Las Vegas real estate | NC hub; geo: cadence, henderson, inspirada, las-vegas |
| `north-las-vegas-master-plans-ranked-guide-2026` | North Las Vegas Master Plans Ranked 2026 | 2026-07-02 | 2026-07-02 | 3859 | Y | 16 | 6 | 4 | 20 | Las Vegas real estate | NC hub; geo: aliante, henderson, las-vegas, north-las-vegas |
| `new-home-developments-in-las-vegas` | The Insider’s Guide to New Home Developments in Las Vegas, NV (2026) | 2026-05-18 | 2026-06-14 | 5046 | Y | 17 | 6 | 3 | 28 | Las Vegas real estate | NC hub; geo: cadence, henderson, inspirada, lake-las-vegas |
| `where-to-buy-new-construction-las-vegas-2026-tier-ranking` | Where to Buy New Construction in Las Vegas 2026 Tier Ranking | 2026-05-17 | 2026-06-14 | 4709 | Y | 16 | 8 | 5 | 29 | Las Vegas real estate | NC hub; geo: cadence, henderson, inspirada, las-vegas |
| `new-home-developments-in-summerlin` | New Home Developments in Summerlin: The 2026 Buyer's Guide | 2026-03-05 | 2026-06-16 | 4750 | Y | 11 | 7 | 3 | 11 | Las Vegas real estate | NC hub; geo: henderson, las-vegas, summerlin |

### K. Relocation-driven new construction  (2 posts)

| URL (`/blog/…`) | Title | Pub | Updated | Words | TOC | H2s | FAQ | Tables | Int. links | Primary keyword | Links to hub / spokes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `moving-to-north-las-vegas-relocation-guide-2026` | Moving to North Las Vegas: 2026 Relocation Guide | 2026-07-12 | 2026-07-12 | 5027 | Y | 16 | 7 | 3 | 41 | Las Vegas real estate | NC hub; geo: henderson, las-vegas, north-las-vegas, north-las-vegas/new-construction |
| `california-to-las-vegas-new-construction-savings-2026` | California Refugees: How Much New Construction in Las Vegas Saves You vs | 2026-05-11 | 2026-05-27 | 5348 | Y | 14 | 9 | 8 | 56 | California to Las Vegas | NC hub; builders: dr-horton, kb-home, lennar, pulte-del-webb; geo: aliante, cadence, henderson, inspirada |

### L. Community / master-plan spotlight  (70 posts)

| URL (`/blog/…`) | Title | Pub | Updated | Words | TOC | H2s | FAQ | Tables | Int. links | Primary keyword | Links to hub / spokes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `rebecca-place-community-land-trust-las-vegas-2026` | Rebecca Place: Las Vegas Community Land Trust Homes 2026 | 2026-07-21 | 2026-07-21 | 4005 | Y | 14 | 7 | 3 | 17 | Las Vegas real estate | geo: centennial-hills, las-vegas, north-las-vegas, providence |
| `cloudbreak-ridge-kb-home-summerlin-new-homes-2026` | Cloudbreak Ridge by KB Home in Summerlin 2026 | 2026-07-17 | 2026-07-17 | 4114 | Y | 14 | 7 | 4 | 18 | summerlin | NC hub; geo: henderson, luxury-communities, summerlin |
| `north-las-vegas-schools-guide-homebuyers-2026` | North Las Vegas Schools: A Homebuyer's Guide for 2026 | 2026-07-12 | 2026-07-12 | 5727 | Y | 15 | 7 | 3 | 30 | Las Vegas real estate | geo: henderson, las-vegas, north-las-vegas, north-las-vegas/new-construction |
| `building-adu-casita-clark-county-rules-2026` | Building an ADU or Casita in Clark County: 2026 Rules | 2026-07-09 | 2026-07-09 | 3563 | Y | 12 | 7 | 3 | 17 | adu | NC hub; geo: henderson, luxury-communities, summerlin |
| `las-vegas-single-story-next-gen-homes-2026` | Las Vegas Single Story Next Gen Homes for Sale 2026 | 2026-07-03 | 2026-07-03 | 4593 | Y | 15 | 8 | 4 | 27 | single story homes Las Vegas | NC hub; geo: cadence, henderson, las-vegas, north-las-vegas |
| `henderson-nevada-complete-community-guide-2026` | Henderson Nevada: Complete Community Guide 2026 | 2026-06-30 | 2026-07-14 | 5629 | Y | 19 | 8 | 5 | 39 | Las Vegas real estate | NC hub; geo: 55-plus-communities, cadence, henderson, inspirada |
| `rent-vs-buy-in-summerlin-2026` | Rent vs. Buy in Summerlin (2026): Which Actually Wins? | 2026-06-28 | 2026-06-28 | 4901 | Y | 16 | 8 | 4 | 24 | Las Vegas real estate | geo: las-vegas, summerlin |
| `kestrel-redpoint-summerlin-new-villages-buyers-guide-2026` | Kestrel & Redpoint: Summerlin New Villages 2026 | 2026-06-21 | 2026-06-21 | 5471 | Y | 16 | 6 | 3 | 43 | Las Vegas real estate | NC hub; builders: kb-home, lennar, pulte-del-webb, richmond-american; geo: henderson, las-vegas, luxury-communities, summerlin |
| `las-vegas-real-estate-investing-strategies-2026` | Las Vegas Real Estate Investing in 2026: Strategies and ROI | 2026-05-29 | 2026-05-29 | 4040 | Y | 14 | 8 | 3 | 20 | Las Vegas real estate investing | NC hub; geo: henderson, las-vegas, mountains-edge, north-las-vegas |
| `top-10-reasons-to-live-in-north-las-vegas-2026` | Top 10 Reasons to Live in North Las Vegas in 2026 | 2026-05-28 | 2026-07-12 | 4648 | Y | 16 | 7 | 5 | 33 | Las Vegas real estate | NC hub; geo: henderson, las-vegas, luxury-communities, north-las-vegas/new-construction |
| `casitas-mother-in-law-suites-las-vegas-2026-guide` | Casitas & Mother-in-Law Suites , Las Vegas 2026 Guide | 2026-05-27 | 2026-05-27 | 4267 | Y | 13 | 7 | 3 | 21 | Las Vegas real estate | NC hub; geo: henderson, las-vegas, summerlin |
| `rv-garage-homes-las-vegas-2026-buyers-guide` | RV Garage Homes in Las Vegas , A 2026 Buyer's Guide | 2026-05-27 | 2026-05-27 | 5156 | Y | 15 | 7 | 3 | 23 | Las Vegas real estate | geo: aliante, las-vegas, mountains-edge, north-las-vegas |
| `mesa-ridge-summerlin-toll-brothers-guard-gated-luxury-guide-2026` | Mesa Ridge Summerlin Toll Brothers Gated Luxury Guide 2026 | 2026-05-25 | 2026-05-28 | 3747 | Y | 15 | 7 | 4 | 21 | Las Vegas real estate | geo: henderson, las-vegas, luxury-communities, summerlin |
| `spanish-hills-las-vegas-guard-gated-luxury-estates-guide-2026` | Spanish Hills Las Vegas Gated Luxury Estates Guide 2026 | 2026-05-25 | 2026-05-27 | 4145 | Y | 16 | 7 | 4 | 31 | Las Vegas real estate | geo: anthem, henderson, luxury-communities, summerlin |
| `what-one-million-buys-you-summerlin-las-vegas-2026` | What $1 Million Buys You in Summerlin Las Vegas 2026 | 2026-05-25 | 2026-05-28 | 4177 | Y | 14 | 7 | 3 | 28 | Las Vegas real estate | geo: anthem, henderson, lake-las-vegas, las-vegas |
| `desert-shores-northwest-las-vegas-lakefront-buyers-guide-2026` | Desert Shores Northwest Las Vegas Lakefront Guide 2026 | 2026-05-24 | 2026-05-27 | 4631 | Y | 16 | 7 | 3 | 16 | Las Vegas real estate | geo: centennial-hills, henderson, lake-las-vegas, las-vegas |
| `summerlin-las-vegas-master-plan-complete-buyers-guide-2026` | Summerlin Las Vegas Master Plan Complete Buyers Guide 2026 | 2026-05-24 | 2026-05-27 | 4045 | Y | 14 | 8 | 3 | 22 | Las Vegas real estate | geo: cadence, henderson, las-vegas, summerlin |
| `the-lakes-west-las-vegas-lakefront-buyers-guide-2026` | The Lakes West Las Vegas Lakefront Buyers Guide 2026 | 2026-05-24 | 2026-05-27 | 3982 | Y | 14 | 8 | 3 | 21 | Las Vegas real estate | geo: henderson, lake-las-vegas, las-vegas, summerlin |
| `veer-towers-las-vegas-strip-luxury-condos-buyers-guide-2026` | Veer Towers Las Vegas Strip Luxury Condos Buyers Guide 2026 | 2026-05-24 | 2026-05-28 | 3809 | Y | 12 | 8 | 3 | 20 | Las Vegas real estate | geo: henderson, las-vegas, north-las-vegas, summerlin |
| `whitney-ranch-henderson-family-master-plan-buyers-guide-2026` | Whitney Ranch Henderson Family Master Plan Buyers Guide 2026 | 2026-05-24 | 2026-05-27 | 4312 | Y | 15 | 7 | 3 | 22 | Las Vegas real estate | geo: aliante, anthem, cadence, henderson |
| `providence-northwest-las-vegas-master-plan-guide-2026` | Providence Northwest Las Vegas Master Plan Guide 2026 | 2026-05-23 | 2026-05-26 | 4414 | Y | 15 | 7 | 3 | 24 | Las Vegas real estate | NC hub; geo: aliante, cadence, centennial-hills, henderson |
| `reverence-summerlin-pulte-luxury-guide-2026` | Reverence Summerlin Pulte Master Plan Guide 2026 | 2026-05-23 | 2026-05-23 | 4863 | Y | 16 | 7 | 3 | 22 | Las Vegas real estate | NC hub; geo: centennial-hills, henderson, luxury-communities, north-las-vegas |
| `stonebridge-summerlin-toll-brothers-master-plan-guide-2026` | Stonebridge Summerlin Toll Brothers Master Plan Guide 2026 | 2026-05-23 | 2026-05-23 | 4514 | Y | 16 | 7 | 3 | 20 | Las Vegas real estate | NC hub; geo: henderson, las-vegas, luxury-communities, north-las-vegas |
| `centennial-hills-las-vegas-northwest-family-master-plan-guide-2026` | Centennial Hills Las Vegas: 2026 Northwest Family Guide | 2026-05-22 | 2026-05-28 | 4601 | Y | 14 | 7 | 3 | 17 | Las Vegas real estate | geo: aliante, centennial-hills, henderson, las-vegas |
| `queensridge-gated-estates-las-vegas-luxury-guide-2026` | Queensridge Gated Estates Las Vegas: 2026 Luxury Guide | 2026-05-22 | 2026-05-27 | 4683 | Y | 14 | 7 | 3 | 24 | Las Vegas real estate | geo: henderson, las-vegas, luxury-communities, summerlin |
| `seven-hills-henderson-guard-gated-rio-secco-buyers-guide-2026` | Seven Hills Henderson: 2026 Rio Secco Buyer's Guide | 2026-05-22 | 2026-05-28 | 4714 | Y | 14 | 7 | 3 | 20 | Las Vegas real estate | geo: anthem, henderson, lake-las-vegas, las-vegas |
| `spanish-trail-las-vegas-gated-country-club-buyers-guide-2026` | Spanish Trail Las Vegas: 2026 Gated Country Club Guide | 2026-05-22 | 2026-05-27 | 4663 | Y | 14 | 7 | 3 | 23 | Las Vegas real estate | geo: anthem, henderson, lake-las-vegas, las-vegas |
| `the-cliffs-summerlin-west-village-buyers-guide-2026` | The Cliffs Summerlin West: 2026 Village Buyer's Guide | 2026-05-22 | 2026-05-27 | 4591 | Y | 14 | 7 | 3 | 19 | Las Vegas real estate | NC hub; geo: henderson, las-vegas, luxury-communities, summerlin |
| `the-paseos-summerlin-established-village-buyers-guide-2026` | The Paseos Summerlin: 2026 Established Village Guide | 2026-05-22 | 2026-05-28 | 4639 | Y | 14 | 7 | 3 | 23 | Las Vegas real estate | NC hub; geo: henderson, las-vegas, luxury-communities, north-las-vegas |
| `tuscany-henderson-gated-golf-master-plan-buyers-guide-2026` | Tuscany Henderson: 2026 Gated Golf Master-Plan Guide | 2026-05-22 | 2026-05-28 | 4373 | Y | 13 | 7 | 3 | 24 | Las Vegas real estate | geo: anthem, cadence, henderson, inspirada |
| `lake-las-vegas-henderson-waterfront-master-plan-buyers-guide-2026` | Lake Las Vegas: 2026 Waterfront Henderson Master-Plan Guide | 2026-05-21 | 2026-05-28 | 4552 | Y | 14 | 7 | 3 | 22 | Las Vegas real estate | geo: anthem, henderson, lake-las-vegas, las-vegas |
| `aliante-north-las-vegas-master-plan-buyers-guide-2026` | Aliante North Las Vegas: 2026 Master-Plan Buyer's Guide | 2026-05-20 | 2026-05-21 | 4566 | Y | 14 | 6 | 3 | 26 | Las Vegas real estate | NC hub; geo: aliante, henderson, las-vegas, luxury-communities |
| `anthem-henderson-master-plan-buyers-guide-2026` | Anthem Henderson: 2026 Buyer's Guide to the 4,775-Acre Plan | 2026-05-20 | 2026-05-20 | 4065 | Y | 15 | 6 | 3 | 25 | Las Vegas real estate | geo: henderson, las-vegas, luxury-communities |
| `green-valley-ranch-henderson-family-master-plan-buyers-guide-2026` | Green Valley Ranch: 2026 Henderson Family Master-Plan Guide | 2026-05-20 | 2026-05-20 | 5299 | Y | 14 | 7 | 3 | 31 | Las Vegas real estate | NC hub; geo: anthem, cadence, henderson, las-vegas |
| `inside-ascaya-henderson-hilltop-estate-buyers-guide-2026` | Inside Ascaya: A 2026 Guide to Henderson Hilltop Estates | 2026-05-20 | 2026-05-27 | 6087 | Y | 16 | 7 | 5 | 34 | Las Vegas real estate | NC hub; geo: anthem, henderson, lake-las-vegas, las-vegas |
| `inspirada-henderson-buyers-lifestyle-guide-2026` | Inspirada Henderson: A 2026 Buyer's Lifestyle Guide | 2026-05-20 | 2026-05-28 | 3681 | Y | 12 | 6 | 3 | 29 | Las Vegas real estate | NC hub; geo: anthem, cadence, henderson, inspirada |
| `living-in-cadence-henderson-buyers-lifestyle-guide-2026` | Living in Cadence Henderson: A 2026 Buyer's Lifestyle Guide | 2026-05-20 | 2026-05-28 | 3573 | Y | 12 | 6 | 3 | 26 | Las Vegas real estate | NC hub; geo: anthem, cadence, henderson, inspirada |
| `macdonald-ranch-henderson-foothills-master-plan-guide-2026` | MacDonald Ranch: 2026 Henderson Foothills Master-Plan Guide | 2026-05-20 | 2026-05-28 | 5427 | Y | 15 | 7 | 3 | 34 | Las Vegas real estate | NC hub; geo: anthem, henderson, inspirada, las-vegas |
| `mountains-edge-southwest-las-vegas-master-plan-buyers-guide-2026` | Mountains Edge: 2026 Southwest Las Vegas Master-Plan Guide | 2026-05-20 | 2026-05-28 | 4540 | Y | 14 | 6 | 3 | 25 | Las Vegas real estate | geo: anthem, henderson, inspirada, las-vegas |
| `peccole-ranch-las-vegas-established-master-plan-guide-2026` | Peccole Ranch: 2026 Established Las Vegas Master-Plan Guide | 2026-05-20 | 2026-05-20 | 4396 | Y | 13 | 6 | 3 | 23 | Las Vegas real estate | geo: henderson, las-vegas, luxury-communities, summerlin |
| `ridges-summerlin-custom-build-lot-selection-guide-2026` | The Ridges Summerlin: 2026 Custom Build & Lot Guide | 2026-05-20 | 2026-05-28 | 4624 | Y | 13 | 6 | 4 | 24 | Las Vegas real estate | geo: henderson, las-vegas, luxury-communities, summerlin |
| `skye-canyon-northwest-las-vegas-master-plan-buyers-guide-2026` | Skye Canyon: 2026 Northwest Las Vegas Master-Plan Guide | 2026-05-20 | 2026-05-21 | 4585 | Y | 14 | 6 | 3 | 23 | Las Vegas real estate | NC hub; geo: centennial-hills, las-vegas, north-las-vegas, skye-canyon |
| `southern-highlands-las-vegas-enclave-tier-buyers-guide-2026` | Southern Highlands: 2026 Guide to Every Enclave & Tier | 2026-05-20 | 2026-05-21 | 4378 | Y | 14 | 6 | 4 | 27 | Las Vegas real estate | NC hub; geo: henderson, las-vegas, luxury-communities, summerlin |
| `las-vegas-new-home-communities-developments-2025-2026` | Las Vegas New Home Communities Map 2025-2026 | 2026-05-18 | 2026-06-14 | 5046 | Y | 17 | 6 | 3 | 28 | Las Vegas real estate | NC hub; geo: cadence, henderson, inspirada, lake-las-vegas |
| `henderson-vs-summerlin-2026-side-by-side` | Henderson vs Summerlin 2026: Side-by-Side Comparison | 2026-05-17 | 2026-06-14 | 4445 | Y | 16 | 6 | 4 | 24 | Las Vegas real estate | NC hub; geo: centennial-hills, henderson, las-vegas, luxury-communities |
| `las-vegas-real-estate-commissions-after-nar-settlement-2026` | Las Vegas Real Estate Commissions After NAR Settlement 2026 | 2026-05-17 | 2026-06-14 | 4526 | Y | 15 | 6 | 5 | 34 | Las Vegas real estate | NC hub; geo: centennial-hills, henderson, las-vegas, luxury-communities |
| `ascension-peaks-summerlin-toll-brothers-appreciation-2026` | Ascension at The Peaks: Why Toll Brothers Buyers Are Up $130K-$415K Sinc | 2026-05-11 | 2026-05-27 | 5043 | Y | 14 | 9 | 4 | 40 | Ascension at The Peaks | NC hub; builders: toll-brothers; geo: henderson, inspirada, lake-las-vegas, las-vegas |
| `cadence-henderson-new-homes-buildout-status-2026` | Cadence Was the #3 New Home Community in America in 2025 , Should You St | 2026-05-11 | 2026-05-27 | 4967 | Y | 14 | 9 | 3 | 78 | Cadence Henderson | NC hub; builders: dr-horton, kb-home, lennar, pulte-del-webb; geo: anthem, cadence, henderson, inspirada |
| `cliffs-kestrel-redpoint-summerlin-villages-comparison-2026` | The Cliffs vs Kestrel vs Redpoint: Which Summerlin Village Is Right for  | 2026-05-11 | 2026-05-27 | 5158 | Y | 15 | 9 | 5 | 90 | Summerlin villages | NC hub; builders: kb-home, pulte-del-webb, taylor-morrison, toll-brothers; geo: aliante, henderson, las-vegas, summerlin |
| `esplanade-red-rock-summerlin-taylor-morrison-2026` | Esplanade at Red Rock: What Taylor Morrison's Luxury Resort Brand Brings | 2026-05-11 | 2026-05-27 | 4805 | Y | 14 | 9 | 3 | 51 | Esplanade at Red Rock | NC hub; builders: lennar, taylor-morrison, toll-brothers; geo: aliante, anthem, henderson, las-vegas |
| `inspirada-final-75-homes-south-henderson-new-construction-2026` | Inspirada's Final 75 Homes: Last Window to Buy New in South Henderson (2 | 2026-05-11 | 2026-05-27 | 5144 | Y | 14 | 9 | 3 | 87 | Inspirada Henderson | NC hub; builders: dr-horton, kb-home, lennar, pulte-del-webb; geo: aliante, anthem, cadence, henderson |
| `lake-las-vegas-new-communities-expansion-2026` | Lake Las Vegas Went from 5 to 19 New Communities in 18 Months , Here's W | 2026-05-11 | 2026-05-27 | 5550 | Y | 14 | 9 | 4 | 100 | Lake Las Vegas | NC hub; builders: kb-home, lennar, pulte-del-webb, richmond-american; geo: aliante, anthem, cadence, henderson |
| `macdonald-highlands-ascaya-henderson-custom-build-comparison-2026` | MacDonald Highlands vs Ascaya: Building Custom in Henderson's Two Top Gu | 2026-05-11 | 2026-05-28 | 5229 | Y | 14 | 9 | 3 | 56 | MacDonald Highlands | NC hub; geo: aliante, henderson, lake-las-vegas, las-vegas |
| `meriden-kb-home-henderson-new-master-plan-2026` | Meriden by KB Home: What to Know About Henderson's Newest 940-Home Maste | 2026-05-11 | 2026-05-27 | 5141 | Y | 15 | 9 | 3 | 77 | Meriden Henderson | NC hub; builders: dr-horton, kb-home, lennar, pulte-del-webb; geo: anthem, cadence, henderson, inspirada |
| `valley-vista-north-las-vegas-top-master-plan-2026` | Why Valley Vista Made the Top 10 US Selling Master Plans in 2025 (2026 B | 2026-05-11 | 2026-05-27 | 5032 | Y | 14 | 9 | 3 | 89 | Valley Vista | NC hub; builders: kb-home, lennar, pulte-del-webb, richmond-american; geo: aliante, cadence, centennial-hills, henderson |
| `should-you-buy-las-vegas-home-2026-honest-take` | Should You Buy a Las Vegas Home in 2026? Honest Take | 2026-05-08 | 2026-07-13 | 5124 | Y | 18 | 7 | 5 | 39 | las vegas real estate 2026 | NC hub; builders: pulte-del-webb, toll-brothers; geo: henderson, inspirada, las-vegas, north-las-vegas |
| `four-seasons-henderson-luxury-high-rise` | Four Seasons Private Residences Rising in Henderson: What a Billion-Doll | 2026-04-30 | 2026-04-30 | 4616 | Y | 13 | 8 | 4 | 31 | Las Vegas luxury homes | NC hub; geo: centennial-hills, henderson, las-vegas, luxury-communities |
| `summerlin-master-planned-community-why-live-here` | Summerlin Master-Planned Community: Why Live Here in 2026 | 2026-04-30 | 2026-05-25 | 4475 | Y | 18 | 6 | 3 | 33 | Summerlin homes | NC hub; geo: centennial-hills, henderson, las-vegas, luxury-communities |
| `top-5-henderson-communities` | Top 5 Henderson Communities to Live in 2026 | 2026-04-28 | 2026-05-27 | 4656 | Y | 22 | 8 | 3 | 30 | Henderson real estate | NC hub; geo: anthem, cadence, henderson, inspirada |
| `top-real-estate-agents-in-henderson-for-retirees-2026-guide-chris-nevada` | Top Real Estate Agents in Henderson for Retirees / 2026 Guide / Chris Ne | 2026-04-21 | 2026-07-12 | 4574 | Y | 16 | 7 | 5 | 28 | Las Vegas real estate | geo: henderson, henderson/new-construction, las-vegas, luxury-communities |
| `what-2-million-dollar-luxury-home-buys-summerlin-vs-henderson-2026` | What $2 Million Buys: Summerlin vs Henderson Luxury 2026 | 2026-04-19 | 2026-07-04 | 3812 | Y | 14 | 8 | 4 | 27 | Las Vegas real estate | geo: cadence, henderson, lake-las-vegas, luxury-communities |
| `best-real-estate-agent-in-north-las-vegas-your-2026-guide-to-working-with-the-right-professional` | Best Real Estate Agent in North Las Vegas: 2026 Guide | 2026-04-10 | 2026-07-12 | 4233 | Y | 12 | 8 | 4 | 31 | Las Vegas real estate | NC hub; geo: aliante, anthem, centennial-hills, henderson |
| `pricing-strategies-in-summerlin` | Real Estate Pricing Strategies in Summerlin, NV | 2026-03-05 | 2026-07-12 | 4792 | Y | 16 | 7 | 4 | 22 | Las Vegas real estate | NC hub; geo: henderson, las-vegas, luxury-communities, north-las-vegas |
| `who-is-best-real-estate-agent-summerlin-2026` | Who Is the Best Real Estate Agent in Summerlin in 2026? | 2026-03-03 | 2026-07-14 | 5381 | Y | 17 | 7 | 5 | 33 | Las Vegas real estate | NC hub; geo: las-vegas, luxury-communities, summerlin, summerlin/new-construction |
| `las-vegas-history` | History of Las Vegas: From Railroads to Real Estate Empires | 2026-02-09 | 2026-07-13 | 4372 | Y | 16 | 7 | 3 | 19 | Las Vegas real estate | NC hub; geo: henderson, las-vegas, luxury-communities, summerlin |
| `las-vegas-vs-north-las-vegas` | Las Vegas vs North Las Vegas: Safety, Cost & Homes 2026 | 2026-02-09 | 2026-06-25 | 6157 | Y | 16 | 7 | 4 | 43 | Las Vegas real estate | NC hub; geo: henderson, las-vegas, luxury-communities, north-las-vegas |
| `summerlin-history` | The Story of Summerlin: From Desert Floor to Premier Community | 2026-02-09 | 2026-07-12 | 4065 | Y | 15 | 7 | 3 | 22 | Las Vegas real estate | NC hub; geo: las-vegas, luxury-communities, summerlin, summerlin/new-construction |
| `summerlin-vs-lake-las-vegas` | Summerlin vs. Lake Las Vegas: Two Visions of Luxury Living | 2026-02-09 | 2026-07-12 | 4602 | Y | 14 | 7 | 5 | 20 | Las Vegas real estate | NC hub; geo: henderson, luxury-communities, summerlin |
| `best-neighborhoods-summerlin-2026` | What Are the Best Neighborhoods in Summerlin in 2026? | 2026-01-23 | 2026-07-14 | 6135 | Y | 17 | 7 | 4 | 31 | Las Vegas real estate | NC hub; geo: henderson, las-vegas, luxury-communities, north-las-vegas |
| `homebuyer-programs-in-summerlin` | Financial Assistance and Homebuyer Programs in Summerlin, NV | 2026-01-22 | 2026-06-16 | 5963 | Y | 18 | 8 | 3 | 10 | Las Vegas real estate | geo: henderson, las-vegas, north-las-vegas, summerlin |

---

## 3. THE TOPICAL CLUSTER MAP

The 173 posts sort into 12 themes. Each theme exists to feed a specific tier of the pyramid.

```
                       TIER 1   /new-construction/   (the money page)
                                       ▲
        ┌──────────────┬───────────────┼───────────────┬──────────────┐
        │              │               │               │              │
   TIER 2 geo      TIER 3 builder  TIER 3 community  /55-plus-    /luxury-
   /henderson/     /builders/*     /summerlin/,      communities/  communities/
   /new-construction/  (18 pages)  /cadence/, etc.
        ▲              ▲               ▲
        │              │               │
   ═════╧══════════════╧═══════════════╧══════════════════════════════
   TIER 4  THE BLOG CLUSTER  (173 posts)
```

| # | Theme | Posts | What it feeds | Representative posts |
|---|---|---|---|---|
| **A** | **Builder model / floor-plan spotlight** | **26** | `/builders/<builder>/` + the community page + `/new-construction/` | `lennar-greg-next-gen-mockingbird-summerlin-2026`, `kb-home-plan-3095-reserves-cloudbreak-ridge-summerlin-2026`, `dr-horton-plan-2660-symmetry-falls-cadence-henderson-2026`, `tri-pointe-vela-plan-3-inspirada-henderson-2026` |
| **L** | **Community / master-plan spotlight** | **70** | the community entity page + the geo sub-hub | `summerlin-las-vegas-master-plan-complete-buyers-guide-2026`, `skye-canyon-northwest-las-vegas-master-plan-buyers-guide-2026`, `valley-vista-north-las-vegas-top-master-plan-2026`, `cadence-henderson-new-homes-buildout-status-2026` |
| **F** | **Cost, tax & fee explainers** | **12** | `/new-construction/` + `/guides/las-vegas-property-tax/` | `sid-lid-taxes-las-vegas-new-construction-2026`, `sid-lid-fees-cadence-inspirada-henderson-2026`, `clark-county-property-tax-reassessment-new-construction-2026`, `las-vegas-closing-costs-2026-buyer-seller-breakdown` |
| **D** | **NC process / how-to** | **11** | `/new-construction/` + `/buyers/` | `new-construction-timeline-las-vegas-build-reality-2026`, `pre-drywall-inspection-new-construction-las-vegas-2026`, `do-you-need-realtor-new-construction-las-vegas-2026`, `nevada-new-home-warranty-1-2-10-year-coverage-2026` |
| **I** | **Market data & construction news** | **10** | `/new-construction/` + `/market-report/` | `las-vegas-homebuilder-sales`, `las-vegas-construction-boom`, `new-master-planned-communities-las-vegas-pipeline-2026`, `summerlin-housing-market-2026` |
| **B** | **Builder comparison / brand roundup** | **8** | all 18 `/builders/*` pages at once | `las-vegas-home-builders-compared-2026`, `top-luxury-home-builders-las-vegas-2026`, `christopher-homes-blue-heron-toll-brothers-summerlin-comparison-2026`, `tri-pointe-homes-las-vegas-communities-2026` |
| **J** | **Where-to-buy rankings & geo NC hubs** | **8** | every geo sub-hub simultaneously | `where-to-buy-new-construction-las-vegas-2026-tier-ranking`, `new-construction-homes-henderson-builders-guide-2026`, `new-construction-homes-north-las-vegas-guide-2026`, `master-planned-communities-las-vegas-ranked-2026` |
| **C** | **Incentives, credits & builder negotiation** | **7** | `/new-construction/` (highest-intent cluster) | `new-construction-incentives-las-vegas-may-2026-builder-roundup`, `builder-closing-cost-credits-las-vegas-2026`, `2-1-buydown-las-vegas-new-construction-2026`, `lot-premium-negotiation-las-vegas-new-construction-2026`, `builder-contract-clauses-negotiate-las-vegas-2026`, `design-center-budget-las-vegas-new-construction-2026` |
| **G** | **HOA, legal & compliance** | **7** | `/new-construction/` + community pages | `nevada-hoa-fines-your-nrs-116`, `hoa-landscape-requirements-new-construction-las-vegas-2026`, `henderson-hoa-special-assessments-reserve-study-guide-2026`, `new-nevada-housing-laws-2026-adu-hoa-rules` |
| **H** | **55+ / active-adult new build** | **7** | `/55-plus-communities/` + `/builders/pulte-del-webb/` | `sun-city-summerlin-55-plus-active-adult-master-plan-guide-2026`, `siena-summerlin-shea-homes-55-plus-active-adult-guide-2026`, `solera-at-anthem-henderson-55-plus-active-adult-guide-2026` |
| **E** | **New build vs resale comparison** | **5** | `/new-construction/` + `/search/` | `new-construction-vs-resale-las-vegas-2026-comparison`, `new-construction-resale-las-vegas-decision-matrix-2026`, `vegas-new-build-700k-vs-summerlin-2026` |
| **K** | **Relocation-driven new construction** | **2** | `/moving-to-las-vegas/`, `/california-tax-savings/` | `california-to-las-vegas-new-construction-savings-2026` |

### The three-layer intent stack

The cluster is deliberately built across three funnel depths, and each layer links up to the same hub:

1. **Awareness / research** (themes I, J, L, B, H): "where should I buy", "which builder", "what's the market doing". 96 posts. Largest volume, lowest intent, most linked-to by other posts.
2. **Consideration** (themes E, D, F, G): "new build vs resale", "how long does it take", "what will the taxes be", "what can the HOA fine me for". 35 posts. This is where the hub link density is highest.
3. **Transaction-adjacent** (themes A, C, K): "this exact floor plan", "this month's incentives", "what do I negotiate". 35 posts. Lowest volume, highest commercial intent, freshest dates. **Theme C is the crown jewel: `new-construction-incentives-las-vegas-may-2026-builder-roundup` is a dated monthly-refresh post, and it is the one they surface first in the hub's "Read Next" block.**

### What the hub's "Read Next" block actually pulls

The hub `/new-construction/` has a section headed **"Read Next / New construction articles"** with 3 cards, hand-picked (unlike the blog's automated version):
- `/blog/new-construction-incentives-las-vegas-may-2026-builder-roundup/` (theme C, monthly refresh)
- `/blog/best-real-estate-agent-for-new-construction-in-las-vegas-your-2026-guide-to-builder-negotiations-and-expert-representation/` (theme D, the conversion post)
- `/blog/inspirada-final-75-homes-south-henderson-new-construction-2026/` (theme L, urgency/scarcity)

One from each intent layer. That is the pattern to copy.

Elsewhere in the hub body it also links to: `las-vegas-construction-boom`, `las-vegas-homebuilder-sales`, `las-vegas-home-prices-2026-up`, `las-vegas-housing-market`, `las-vegas-home-costs-2026`, `summerlin-housing-market-2026`, `top-5-henderson-communities`, `las-vegas-property-tax-guide`, `nevada-hoa-fines-your-nrs-116`, `vegas-new-build-700k-vs-summerlin-2026`, `best-time-to-sell-a-house`, `how-nevada-real-estate-group-markets`. Sixteen blog links total on the hub page.

Note: the hub link `/blog/las-vegas-cost-of-living/` does not exist as a blog post. The cost-of-living page lives at `/guides/las-vegas-cost-of-living/`. Their in-body cost link is `/blog/las-vegas-home-costs-2026/`.

---

## 4. INTERNAL LINKING RULES (inferred from 173 posts)

### 4.1 Volume

| Rule | Measured value |
|---|---|
| Internal links inside the article body | **median 26**, mean 29, range 10 to 100 |
| Of those, sitting **inline in prose** | **median 23** (88%) |
| Of those, sitting in an **end block** | median 1, mean 2.7 (12%) |
| **Blog-to-blog** links per post | **median 3 unique**, mean 3.4, max 6. Only 1 post of 173 has zero. |
| External citations inside the body | **median 24** |
| Links to `/new-construction/` | present in **140 of 173 (81%)**, and when present it appears **2 to 3 times** |

### 4.2 Where they sit

- **Inline prose is the primary vehicle.** Roughly 9 of every 10 internal links are inside a sentence in the running copy. The Direct Answer box alone typically carries 6 to 8 entity links in its first 200 words. This is the single biggest structural difference from a normal agent blog.
- **Figures are links.** All 4 inline images are wrapped in `a.blog-figure__link` pointing at a hub, builder, or community page. Free link equity, zero anchor text.
- **The end block is small and specific.** The "Which Sources Inform This Analysis?" H2 is followed by one sentence: "For broader Las Vegas context, see our [new construction hub], [luxury communities], [Summerlin community guide], and [Henderson community guide]." That is the deliberate authority pass-back, and it is the same four targets on almost every post.
- **"Related Reading" (3 cards) and "More from the blog" (6 links) are automated and topically useless.** All 173 posts show the same 3 newest posts, and the 6 text links are alphabetical neighbors by title. Do not model your related-posts logic on this; it is the weakest part of their build.

### 4.3 Anchor text style

**Median anchor length is 2 words, and the dominant pattern is the bare entity name.** They link the proper noun the first (and often every) time it appears.

Top anchors across the cluster: `Summerlin` (199), `Henderson` (185), `Las Vegas` (153), `Toll Brothers` (98), `Cadence` (92), `KB Home` (82), `Inspirada` (79), `North Las Vegas` (78), `MacDonald Highlands` (70), `Lennar` (68), `Pulte` (61), `D.R. Horton` (61), `Tri Pointe` (61).

Secondary pattern, transactional anchors: `Summerlin homes for sale` (60), `Henderson homes for sale` (44). Tertiary, descriptive hub anchors: `new construction` (47), `new construction hub` (25), `Las Vegas New Construction Buyer Guide` (28), `luxury communities` (58), `guard-gated communities` (51).

No keyword-stuffed anchors, no "click here", no naked URLs. Anchors are never longer than the entity name plus a qualifier.

### 4.4 Top internal targets (all 173 posts combined)

| Rank | Target | Links | Tier |
|---|---|---|---|
| 1 | `/summerlin/` | 340 | community |
| 2 | `/henderson/` | 294 | geo |
| 3 | **`/new-construction/`** | **268** | **hub** |
| 4 | `/las-vegas/` | 216 | geo |
| 5 | `/luxury-communities/` | 131 | vertical hub |
| 6 | `/north-las-vegas/` | 105 | geo |
| 7 | `/builders/toll-brothers/` | 102 | builder |
| 8 | `/guard-gated-communities/` | 91 | vertical hub |
| 9 | `/cadence/` | 84 | community |
| 10 | `/macdonald-highlands/` | 84 | community |
| 11-18 | `/builders/lennar/` 83, `/builders/kb-home/` 83, `/builders/pulte-del-webb/` 69, `/builders/dr-horton/` 68, `/builders/tri-pointe/` 67, `/builders/taylor-morrison/` 55, `/builders/richmond-american/` 42, `/builders/touchstone/` 26 | | builder |
| conversion | `/buyers/` 81, `/sellers/` 75, `/buyers/first-time-buyers/` 66, `/contact/` 54, `/mortgage-pre-approval-request/` 21 | | conversion |

Most-linked blog posts (the cluster's internal "mini-hubs"): `builder-closing-cost-credits-las-vegas-2026` (20 inbound), `cadence-henderson-new-homes-buildout-status-2026` (16), `design-center-budget-las-vegas-new-construction-2026` (13), `cliffs-kestrel-redpoint-summerlin-villages-comparison-2026` (12), `sid-lid-fees-cadence-inspirada-henderson-2026` (12), `2-1-buydown-las-vegas-new-construction-2026` (11), `clark-county-property-tax-reassessment-new-construction-2026` (11), `lot-premium-negotiation-las-vegas-new-construction-2026` (11).

### 4.5 The rules to copy

1. **Every NC post links to `/new-construction/` at least twice**, once inside the Direct Answer box and once in the end-block sentence. Target 100%, not their 81%.
2. **Link every builder name and every community name on first mention**, using the bare name as anchor. If the entity page does not exist yet, build it before writing the post.
3. **Aim for 20 to 30 internal links per 4,500 word post**, roughly 1 per 175 words, at least 85% of them inline.
4. **3 to 5 blog-to-blog links per post**, all inline, all to posts in an adjacent theme (a community post links to the incentives and SID/LID posts, not to another community post).
5. **Wrap all inline images in links** to the hub or a builder page.
6. **One fixed end-block sentence** on every post pointing at the hub plus 3 vertical hubs. Same four targets every time.
7. **Match external citation volume to internal**, roughly 1:1. Their median is 26 internal to 24 external.

---

## 5. TWENTY BLOG TOPICS FOR ROSE HOMES LV

Ordered by priority. Assumes the Rose Homes LV hub is `/new-construction/` with geo spokes at `/new-construction/henderson/`, `/new-construction/summerlin/`, `/new-construction/north-las-vegas/`, `/new-construction/skye-canyon/`, `/new-construction/centennial-hills/`, `/new-construction/southwest-las-vegas/`, plus builder entity pages. Post URLs follow the confirmed Rose Homes LV pattern `/blog/<slug>` (singular `blog`).

| # | Suggested title | Target keyword | Links to |
|---|---|---|---|
| 1 | New Construction Incentives in Las Vegas: [Month] [Year] Builder Roundup | las vegas new construction incentives | `/new-construction/` + every builder page. **Refresh monthly, keep the same slug, bump `dateModified`.** The single highest-value post in the cluster. |
| 2 | Do You Need a Realtor for New Construction in Las Vegas? | do you need a realtor for new construction las vegas | `/new-construction/`, `/buyers/`. The conversion post. Answer: the builder pays the commission, the sales rep works for the builder. |
| 3 | New Construction vs Resale in Las Vegas: The 2026 Decision Matrix | new construction vs resale las vegas | `/new-construction/` + `/search/`. Include a real side-by-side table. |
| 4 | Builder Closing Cost Credits in Las Vegas: What They Actually Save You | builder closing cost credits las vegas | `/new-construction/`. Show the math on a $500K home, including the preferred-lender rate spread. |
| 5 | The 2-1 Buydown on a Las Vegas New Build: The Real Math | 2-1 buydown las vegas new construction | `/new-construction/`, `/buyers/mortgage-calculator/` equivalent. |
| 6 | SID and LID Assessments on Las Vegas New Builds: The Hidden $7K to $20K | sid lid las vegas new construction | `/new-construction/`, `/new-construction/henderson/`. Cadence, Inspirada, Skye Canyon, Valley Vista all carry these. Cite Clark County. |
| 7 | Clark County Property Taxes on a New Build: Year One vs Year Two | new construction property tax clark county | `/new-construction/`. The reassessment shock post. Cite the Clark County Assessor and the 3% vs 8% abatement cap. |
| 8 | Design Center Budgeting: What Las Vegas New Build Buyers Actually Spend | new home design center cost las vegas | `/new-construction/`. Base price vs as-built price. |
| 9 | Lot Premiums in Las Vegas New Construction: What to Pay For, What to Skip | lot premium new construction las vegas | `/new-construction/`, `/new-construction/summerlin/`. |
| 10 | Pre-Drywall Inspection on a Las Vegas New Build: Why It Matters | pre drywall inspection las vegas | `/new-construction/`, builder pages. |
| 11 | Skye Canyon New Homes 2026: Builders, Prices, and What's Left | skye canyon new homes | `/new-construction/skye-canyon/`, builder pages. Skye Canyon is under-covered by NRG (only 46 links, one guide) and is a real Rose Homes LV opening. |
| 12 | North Las Vegas New Construction Under $450K: Valley Vista and Villages at Tule Springs | north las vegas new construction homes | `/new-construction/north-las-vegas/`. The affordability angle NRG buries. |
| 13 | Summerlin West New Villages: Kestrel, Redpoint, and Cloudbreak Ridge Compared | summerlin west new homes | `/new-construction/summerlin/`, `/builders/kb-home/`, `/builders/toll-brothers/`. |
| 14 | Cadence Henderson New Homes: 2026 Build-Out Status and What's Still Selling | cadence henderson new homes | `/new-construction/henderson/`. Include remaining-inventory counts. |
| 15 | Las Vegas Home Builders Compared: Lennar vs KB Home vs D.R. Horton vs Richmond American | las vegas home builders compared | `/new-construction/` + all four builder pages. The single best link-equity distributor in the cluster. |
| 16 | Builder Contract Clauses Las Vegas Buyers Should Negotiate | builder purchase agreement negotiation las vegas | `/new-construction/`, `/buyers/`. Arbitration, delay, escalation, appraisal-gap clauses. |
| 17 | How Long Does It Take to Build a Home in Las Vegas? 2026 Timeline Reality | new construction timeline las vegas | `/new-construction/`. Dirt-start vs standing inventory. |
| 18 | Nevada New Home Warranty: What 1-2-10 Coverage Actually Covers | nevada new home warranty | `/new-construction/`. Cite NRS 40 (Chapter 40 constructional defects) and the Nevada State Contractors Board. |
| 19 | Moving From California to a Las Vegas New Build: What You Actually Save | california to las vegas new construction | `/new-construction/`, relocation guide. Nevada has no state income tax, cite the Nevada Department of Taxation. |
| 20 | HOA Landscape and Design Rules on Las Vegas New Builds: What You Can and Cannot Do | hoa landscape requirements las vegas new construction | `/new-construction/`, community pages. Cite NRS 116 and the SNWA turf restrictions. |

**Publishing order that mirrors their sequencing:** 1, 2, 3, 4 first (highest commercial intent, feeds the hub immediately), then 6, 7, 8, 9, 10, 16, 17, 18 (the cost and process explainers that become internal mini-hubs), then 11 to 15 (geo and builder posts that need the entity pages live first), then 5, 19, 20.

---

## 6. EDITORIAL VOICE, SOURCING, AND DATA DENSITY

### 6.1 Voice

- **First-person plural, institutional.** "we", "our", "our team" appears a median of **15 times per post**. Never "I". The brand, not the agent, is the narrator, even though a named person is the byline.
- **Authority-by-volume.** Nearly every post repeats the same production stats: "9,600+ career closings", "$4.85B+ cumulative volume", "789 transactions in 2025", "$440M+ in production", "#1-ranked Nevada team". It appears in the `blog-nreg-experience` aside and again in the authority paragraph. Repetitive by design.
- **Question-answer register.** H2s are search queries. Body copy answers them directly in the first sentence, then supports with data. Textbook AEO writing.
- **Structured hedging on numbers.** "approximately", "roughly", "typically", "in the 0.40 to 0.55% band". They give a range and attribute it rather than assert a single figure.
- **Named-device paragraph openers.** Bolded 2-to-4-word lead-ins ("Builder mix takeaway.", "Practical buyer guidance.", "Standing inventory advantage.") instead of subheads. Cheap scannability.
- **Reading level is higher than Rose Homes LV's standard.** Long compound sentences, industry vocabulary (SID/LID, absorption, months of supply, secondary tax rate) usually defined on first use.
- **Heavy em-dash usage: median 54 per post, up to 121.** Flag: this directly conflicts with the Rose Homes LV workspace rule. Copy the structure, not the punctuation. Every em-dash in their copy maps cleanly to a comma, a period, or "and".

### 6.2 Sourcing and citation style

**Yes, they cite heavily, and yes they cite Clark County, Census, and Freddie Mac.** Median **24 external citations per post**, all `target="_blank" rel="noopener noreferrer"`, always linked on the organization's name rather than a URL.

Citation domain frequency across the 173 posts:

| Source | Links | Used for |
|---|---|---|
| `clarkcountynv.gov` (Assessor + Building & Fire Prevention) | 426 | tax rates, parcel data, permit counts |
| `lasvegasrealtors.com` (GLVAR) | 339 | closed sales, median price, months of supply |
| `census.gov` (ACS) | 302 | migration, household, housing-unit data |
| `leg.state.nv.us` (NRS) | 211 | NRS 116 (HOAs), NRS 624 (contractors), NRS 645 |
| `freddiemac.com/pmms` | 188 | 30-year fixed rate |
| `tax.nv.gov` (NV Dept of Taxation) | 176 | property tax assessment, abatement caps |
| `bls.gov` | 159 | payroll jobs, construction labor, CPI |
| `ccsd.net` | 152 | attendance zones |
| `fhfa.gov` | 142 | Las Vegas-Paradise HPI |
| `greatschools.org` | 138 | school ratings |
| `red.nv.gov` | 113 | license verification (E-E-A-T, not data) |
| `howardhughes.com` / `summerlin.com` | 133 | Summerlin master plan quarterly reports |
| `hud.gov` | 78 | housing market data |
| `mba.org`, `nar.realtor`, `nahb.org` | 154 | industry stats |
| `cityofhenderson.com` | 61 | Henderson permits and planning |
| `consumerfinance.gov` | 57 | loan-cost consumer guidance |
| `nvcontractorsboard.com` | 47 | builder license lookup |
| builder sites (`kbhome.com`, `lennar.com`, `drhorton.com`) | 100+ | floor plans, standard features |
| `bea.gov`, `blm.gov`, `fhwa.dot.gov`, `housing.nv.gov`, `pewresearch.org` | 150+ | supporting |

**FRED is not used.** They go to the primary agency (BLS, BEA, FHFA, Census) rather than the St. Louis Fed aggregator.

**Two-block citation pattern, and this is the part worth copying exactly:**
1. **"Which Industry Authorities Inform This Analysis?"**, 4 to 6 paragraphs, each opening literally with "According to <linked source>," followed by one specific number in context. "According to" appears a **median of 11 times per post**, so roughly half of those are in-body and half are in this block.
2. **"Which Sources Inform This Analysis?"**, a plain bulleted list of 12 to 16 sources with a one-line description of what each supplies. Same list on most posts, lightly customized.

Then a **freshness and compensation disclosure** ("All pricing and builder data reflects <Month Year> market conditions verified across active NREG transactions and Clark County recorded sales"), and the **"About This Article" trust block** with license number, brokerage address, MLS membership, compliance statement, and "Last reviewed" date.

### 6.3 How data-heavy the posts are

Very. Per post, median:

| Data marker | Median per post | Range |
|---|---|---|
| Dollar figures (`$X,XXX`) | **91** | 30 to 343 |
| Percentage figures | **15** | 0 to 156 |
| "According to" attributions | **11** | 5 to 30 |
| Tables | **3** | 3 to 8 |
| External citations | **24** | ~14 to 41 |
| Body words | **~4,400** | 3,282 to 5,934 |

Roughly **one dollar figure every 48 words.** Prices are almost always given as a **range with a qualifier**, not a point estimate: "$525K to $745K", "approximately 0.40 to 0.55%", "typically $15,000 to $40,000 in closing credits". Every table has at least one column of hard numbers, and the newest posts add a caption crediting the source under the table.

**Practical implication for Rose Homes LV:** matching this template means each post needs a real data-gathering pass (GLVAR monthly stats, Clark County Assessor tax rates, builder price sheets, Freddie Mac PMMS) before writing. The workspace "factual only, mark gaps as NOT FOUND" rule applies with force here. Do not fabricate a price range to fill a table.

---

## 7. WHAT TO COPY, WHAT TO SKIP

**Copy:**
- The 26-block page skeleton, especially Direct Answer + Key Takeaways + FAQ accordions with `speakable` schema. That triple is the AI-answer-engine extraction surface and their robots.txt shows it is intentional.
- Question-phrased H2s, 13 to 18 of them, with a TOC that lists H2s only.
- The two-block citation pattern and the "About This Article" trust block with license verification link.
- `dateModified` on everything, plus a visible "Updated" date and "Last reviewed" line.
- Inline entity linking at ~1 link per 175 words, bare-name anchors, images wrapped in links.
- The fixed end-block sentence pointing back at the hub.
- The dated monthly incentives roundup as the flagship recurring post.

**Skip:**
- Their em-dash habit (workspace rule).
- Automated "Related Reading" and "More from the blog" blocks. Hand-pick 3 topically adjacent posts instead. Theirs are literally identical on all 173 posts.
- Publishing 24 posts in a single day. Their `dateModified` values already show them backfilling updates to mask the burst.
- The duplicate-content risk: several pairs are near-identical (`new-construction-vs-resale-las-vegas-2026-comparison` vs `new-construction-vs-resale-las-vegas-2026-decision` vs `las-vegas-new-construction-vs-resale-2026`, and `world-class-dining-las-vegas-luxury-communities` vs `world-class-dining-near-las-vegas-luxury-communities`). Their sitemap also carries 694 duplicate URLs. Do not replicate that.
- The schema/visible-category mismatch (`articleSection: "Buying Tips"` under a chip that says "Community Spotlight").
