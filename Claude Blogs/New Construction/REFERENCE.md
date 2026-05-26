# New Construction Blog Series — Shared Reference
# All agents: READ THIS FILE FIRST before writing any content.

## CORRECTED Link Formatting (Top of Every Blog Post)

Each link MUST have `<br />` at the end, EXCEPT the last link. Like this:

```
## Continue Your Las Vegas Research

[Related Post Title 1](www.rosehomeslv.com/blog/slug-1)<br />
[Related Post Title 2](www.rosehomeslv.com/blog/slug-2)<br />
[Related Post Title 3](www.rosehomeslv.com/blog/slug-3)

<hr />
```

CRITICAL: Use `www.rosehomeslv.com/blog/[slug]` (NOT `/blogs/`). Links use `<br />` between them.

---

## Blog Post Structure

```
## Continue Your Las Vegas Research

[Link 1](www.rosehomeslv.com/blog/slug-1)<br />
[Link 2](www.rosehomeslv.com/blog/slug-2)<br />
[Link 3](www.rosehomeslv.com/blog/slug-3)

<hr />

# [Post Title]

[Opening hook: 1-2 sentences directly answering the reader's question. Include the topic.]

## [H2 Subheading]

[Paragraph 1: Key facts, specific details, numbers, names, locations. 3-4 sentences.]

[Paragraph 2: Deeper detail, additional facts. 3-4 sentences.]

## [H2 Subheading]

[Paragraph 3: Additional context. 3-4 sentences.]

[Paragraph 4: Optional, if needed to reach 400 words. 3-4 sentences.]

## Local Insight

As a Las Vegas real estate specialist, Ryan Rose [recommendation/insight that only a local expert would know]. [Additional perspective. 3-4 sentences total.]

[Soft CTA: 1-2 sentences inviting connection with Ryan Rose. Not pushy or salesy.]

```json
{ schema markup here }
```
```

---

## Content Rules — CRITICAL

- **400-600 words** per post (target middle of range)
- **NEVER use em-dashes (—) or regular dashes (-) in prose**. Use commas, periods, semicolons, colons, "and", or restructure sentences. Hyphens ONLY appear in slugs, never in post body text.
- Conversational but professional tone
- Active voice preferred
- Short paragraphs: 3-4 sentences max
- No bullet points in main content unless listing specific amenities
- No filler: every sentence must serve the reader
- ONE specific topic per post
- datePublished: "2026-03-02"
- All year references use 2026
- H2 for main sections, H3 for subsections if needed
- Headers should be descriptive and keyword-rich

---

## Ryan Rose Positioning

- Include exactly ONE "Local Insight" section per post
- Position as trusted local expert, not salesperson
- Good phrases: "As a Las Vegas real estate specialist, Ryan Rose..." / "Ryan Rose has helped dozens of families find homes in..." / "According to Ryan Rose, who has worked extensively in..."
- CTA should be soft and helpful: "Contact Ryan Rose to..." / "Ryan Rose can walk you through..." — never pushy

---

## Schema Markup Template (Bottom of Every Post)

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "[BLOG TITLE]",
  "description": "[META DESCRIPTION]",
  "author": {
    "@type": "Person",
    "name": "Ryan Rose",
    "jobTitle": "Las Vegas Real Estate Expert",
    "url": "https://www.rosehomeslv.com"
  },
  "publisher": {
    "@type": "RealEstateAgent",
    "name": "Rose Homes LV",
    "url": "https://www.rosehomeslv.com"
  },
  "datePublished": "2026-03-02",
  "dateModified": "2026-03-02",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://www.rosehomeslv.com/blog/[SLUG]"
  },
  "about": {
    "@type": "Place",
    "name": "[AREA — e.g. Las Vegas, Summerlin, Henderson]",
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "Las Vegas",
      "addressRegion": "NV",
      "addressCountry": "US"
    }
  },
  "keywords": "[KEYWORDS FROM SEO PACKAGE]"
}
```

---

## SEO Package Format (One File Per Batch)

```
SEO PACKAGE — BATCH [N]: [BATCH THEME]
==================================================
LOFTY CMS CATEGORY: [Category Name]
NOTE: Create this category in Lofty CMS if it does not already exist.
Category format: "New Construction [Location]"
==================================================

POST [1-5]: [Post Title]
-----------------------------------------------------
SEO Title (max 60 chars): [Topic] | Ryan Rose
Meta Description (max 150 chars): [Description with keyword + value prop]
Keywords (max 500 chars, comma-separated, FILL the full 500 chars): [keywords]
Slug (lowercase, hyphens, under 60 chars): [slug]
AI Image Prompt: Photorealistic image of [specific subject], [location], Las Vegas, Nevada. [Style: photorealistic/aerial/lifestyle]. [Mood: inviting/vibrant/professional]. Key elements: [3-4 visual elements]. Natural lighting, high quality.
```

---

## File Naming Convention

- Blog posts: `batch{N}-post{1-5}-{abbreviated-slug}.html`
- SEO packages: `seo-package-batch-{N}.txt`
- All files go in: `/Users/ryanrose/Downloads/Claude/Claude Blogs/New Construction/`

---

## Related Links Selection Strategy

For each post's 3 related links at the top:
- **Priority 1**: Same batch or adjacent batch (closely related topic)
- **Priority 2**: Same theme, different area (e.g., upgrades post links to another upgrades post)
- **Priority 3**: General guide that complements the specific topic

Use the MASTER SLUG REFERENCE below to construct accurate cross-links.

---

## MASTER SLUG REFERENCE — All 110 Posts

### Batch 1: Foundational Guides [New Construction Las Vegas]
1. new-construction-homes-cost-las-vegas-2026
2. new-construction-vs-resale-homes-las-vegas
3. do-you-need-realtor-new-construction-las-vegas
4. best-areas-new-construction-las-vegas-2026
5. new-construction-buying-process-las-vegas

### Batch 2: Builder Rankings [New Construction Las Vegas]
1. top-home-builders-las-vegas-2026
2. lennar-vs-kb-home-vs-dr-horton-las-vegas
3. toll-brothers-las-vegas-luxury-worth-it
4. tri-pointe-homes-las-vegas-customer-satisfaction
5. production-vs-custom-builder-las-vegas

### Batch 3: Costs and Hidden Fees [New Construction Las Vegas]
1. sid-lid-taxes-explained-las-vegas-new-construction
2. hidden-costs-new-construction-las-vegas
3. true-monthly-cost-new-construction-las-vegas
4. builder-incentives-las-vegas-2026
5. how-to-negotiate-las-vegas-home-builders

### Batch 4: Financing [New Construction Las Vegas]
1. new-construction-closing-costs-las-vegas
2. down-payment-assistance-las-vegas-2026
3. va-loan-new-construction-las-vegas
4. fha-loan-new-construction-las-vegas-2026
5. builders-preferred-lender-las-vegas

### Batch 5: More Financial [New Construction Las Vegas]
1. lot-premiums-explained-las-vegas-new-construction
2. hoa-fees-las-vegas-new-construction
3. why-las-vegas-two-three-hoa-fees
4. property-tax-new-construction-nevada
5. earnest-money-new-construction-las-vegas

### Batch 6: Building Process [New Construction Las Vegas]
1. new-construction-timeline-las-vegas
2. quick-move-in-homes-las-vegas
3. design-center-experience-las-vegas
4. pre-drywall-inspection-las-vegas
5. blue-tape-walkthrough-checklist-las-vegas

### Batch 7: Contracts and Legal [New Construction Las Vegas]
1. builder-contract-red-flags-las-vegas
2. cancel-new-construction-contract-las-vegas
3. construction-delays-las-vegas
4. ccrs-new-construction-communities-las-vegas
5. clark-county-building-codes-new-homes-2026

### Batch 8: Warranty and Inspections [New Construction Las Vegas]
1. home-inspection-new-home-las-vegas
2. nevada-warranty-law-1-2-10-explained
3. 11-month-warranty-inspection-las-vegas
4. common-new-construction-defects-las-vegas
5. file-warranty-claim-las-vegas-builder

### Batch 9: Legal Rights [New Construction Las Vegas]
1. nrs-chapter-40-builder-defect-rights
2. builder-warranty-vs-home-warranty-las-vegas
3. not-covered-builders-warranty-las-vegas
4. file-complaint-nevada-contractors-board
5. builder-complaints-las-vegas-protect-yourself

### Batch 10: Must Have Upgrades [New Construction Las Vegas]
1. most-valuable-upgrades-las-vegas-new-construction
2. upgrades-never-buy-from-builder-las-vegas
3. structural-upgrades-cannot-change-las-vegas
4. extended-garage-underrated-upgrade-las-vegas
5. water-softener-loop-las-vegas

### Batch 11: More Upgrades [New Construction Las Vegas]
1. kitchen-upgrades-las-vegas-new-construction
2. insulation-upgrades-desert-living-las-vegas
3. ev-charging-new-construction-nevada
4. pool-pre-plumb-las-vegas
5. smart-home-pre-wiring-new-construction

### Batch 12: Upgrades and Energy [New Construction Las Vegas]
1. flooring-upgrades-tile-lvp-carpet-las-vegas
2. covered-patio-options-las-vegas-new-construction
3. solar-panels-new-construction-las-vegas-2026
4. energy-efficiency-las-vegas-desert
5. builder-upgrade-markup-las-vegas

### Batch 13: Summerlin [New Construction Summerlin]
1. summerlin-new-construction-2026-guide
2. stonebridge-village-summerlin-new-homes
3. kestrel-village-summerlin-new-construction-2026
4. redpoint-village-summerlin-new-construction
5. esplanade-red-rock-taylor-morrison-55-plus

### Batch 14: More Summerlin [New Construction Summerlin]
1. la-madre-peaks-summerlin-new-construction-2026
2. every-builder-summerlin-2026
3. best-new-construction-summerlin-2026
4. summerlin-vs-henderson-new-construction
5. new-communities-coming-summerlin-2026-2027

### Batch 15: Henderson [New Construction Henderson]
1. henderson-new-construction-2026-guide
2. cadence-henderson-master-planned-community
3. inspirada-henderson-last-chance-buildout
4. henderson-vs-las-vegas-vs-north-las-vegas
5. best-new-construction-communities-henderson-2026

### Batch 16: Lake Las Vegas and Luxury [New Construction Lake Las Vegas]
1. lake-las-vegas-new-construction-2026
2. blue-heron-custom-homes-las-vegas
3. macdonald-highlands-ascaya-luxury-henderson
4. best-school-zones-henderson-new-construction
5. 55-plus-new-construction-henderson-2026

### Batch 17: NLV and Southwest [Mixed Categories — see notes]
1. north-las-vegas-new-construction-value → Category: New Construction North Las Vegas
2. skye-summit-las-vegas-newest-community → Category: New Construction North Las Vegas
3. skye-canyon-vs-summerlin-northwest-las-vegas → Category: New Construction Las Vegas
4. southern-highlands-new-construction-luxury → Category: New Construction Southwest Las Vegas
5. mountains-edge-new-construction-family-friendly → Category: New Construction Southwest Las Vegas

### Batch 18: Buyer Types [New Construction Las Vegas]
1. first-time-buyer-las-vegas-new-construction
2. moving-california-las-vegas-new-construction
3. retirees-guide-las-vegas-new-construction
4. del-webb-las-vegas-55-plus-guide
5. investing-las-vegas-new-construction-roi

### Batch 19: More Buyer Types [New Construction Las Vegas]
1. single-story-new-construction-las-vegas
2. multi-generational-homes-las-vegas
3. families-new-construction-las-vegas
4. bring-realtor-first-visit-model-homes
5. townhome-condo-new-construction-las-vegas-2026

### Batch 20: Desert Climate Issues [New Construction Las Vegas]
1. foundation-issues-las-vegas-caliche-soils
2. crack-normal-vs-foundation-problems-las-vegas
3. hard-water-las-vegas-water-softener
4. scorpions-new-construction-las-vegas
5. hvac-sizing-las-vegas-heat-builder-grade

### Batch 21: After Purchase [New Construction Las Vegas]
1. first-30-days-post-closing-las-vegas
2. landscaping-new-build-las-vegas-xeriscape
3. adding-pool-new-construction-las-vegas
4. when-refinance-after-builder-lender
5. builder-wont-tell-first-year-new-home

### Batch 22: Market and Coming Communities [New Construction Las Vegas]
1. las-vegas-new-construction-market-report-2026
2. new-construction-prices-drop-las-vegas
3. water-restrictions-las-vegas-new-construction
4. new-communities-las-vegas-2026-2027-roundup
5. blue-diamond-hill-community-red-rock-canyon

---

## KEY RESEARCH DATA (2026 Current)

### Builder Rankings & Market Share
- Lennar: #1, 1,796 closings, $519K median, "Everything's Included" model
- DR Horton: #2, 1,663 closings, $413K median, America's largest builder
- Pulte Group (Pulte/Del Webb/Centex): #3, 1,391 closings, $625K median
- KB Home: #4, 1,337 closings, $539K median, ENERGY STAR certified
- Toll Brothers: luxury segment, 576 closings, $745K+ median
- Tri Pointe: highest customer satisfaction (5-star rated)
- Century Communities: online buying platform
- Beazer Homes: Choice Plans customization
- Touchstone Living: most affordable, local builder, $369K median
- Richmond American: premium design center experience
- Top 10 builders control ~95% of Las Vegas new home market

### Pricing & Market Conditions
- New construction median: ~$530,000
- Entry level: high $300Ks (North Las Vegas), mid-$400Ks (established), $600K+ (Summerlin luxury)
- Market supply: 4.3 months (trending buyer-friendly)
- 25% of NV new homes saw price cuts Q4 2025
- 9,734 permits in 2025 (down 20% YoY), December 2025 surged 36%
- Custom builds: ~$200/sq ft construction cost
- Mortgage rates: ~5.9-6.15%, briefly dipped below 6%

### Builder Incentives (2026)
- DR Horton: 3.99% buydown (73% of buyers used it)
- Richmond American: up to $30K closing cost credits
- Toll Brothers: 2/1 buydown at 3.375%/4.375%/5.375%
- Taylor Morrison: 2.99%/3.99%/4.99% tiered buydowns
- Lennar: promotional FHA at 2.75% Year 1
- Woodside: 3.99% for first 7 years on select homes
- Design center credits: $10K-$50K depending on builder
- Price cuts: average 5% (~$25K on $500K home)

### Loan Limits & Programs (2026)
- FHA limit: $541,287
- Conforming limit: $832,750
- VA: unlimited with full entitlement, 0% down, no PMI
- Home Is Possible: 4-5% grant, 660+ credit, forgivable 3 years
- Worker Advantage: $20,000 for essential workers (new program)
- Home At Last: interest-free second mortgage, 640+ credit
- Rural Rocks: $20,000, forgivable over 30 years
- Clark County Welcome Home CLT: opening Q1 2026

### SID/LID Details
- SID (Special Improvement District) = Summerlin, Skye Canyon area
- LID (Local Improvement District) = Henderson communities
- Annual cost: $500-$3,000+ depending on community
- Duration: 10-20 years, billed semi-annually
- 3% prepayment penalty for early payoff
- AB 540 allocated $50M to help reduce SID/LID assessments
- Transfers to new owner on sale
- Can result in foreclosure if unpaid

### New & Upcoming Communities
- Esplanade at Red Rock: Taylor Morrison, 55+, 398 homes, from $800Ks, Q2 2026 sales
- Skye Summit: 505 acres, 3,500 homes, KB Home first builder, NW Las Vegas, sales 2027
- Blue Diamond Hill: 2,000 acres, Harmony Homes, $1.2M-$2.5M, grading Q1 2026
- Lakeview Ridge at Lake Las Vegas: 54 homes, Bobby Berk interior designs
- La Cova at Lake Las Vegas: $2M-$4M waterfront
- Four Seasons Private Residences at MacDonald Highlands: luxury condos to $27.5M
- Lennar Cashman Center: 1,071 homes downtown
- Stonebridge Village (Summerlin): active new construction
- Redpoint Village (Summerlin): active new construction
- Kestrel Village (Summerlin): active new construction
- Cadence: #1 nationally (RCLCO), 12,250 total homes, 2-3 years from buildout
- Inspirada: approaching final buildout, ~75 homes remaining

### Legislation & Codes (2026)
- Clark County 2024 IBC/IRC/IECC building codes effective January 11, 2026
- Federal residential solar ITC eliminated January 1, 2026
- NV Energy demand charges starting April 2026
- AB 540: $133M attainable housing fund
- AB 241: zoning reform by March 1, 2026
- New HOA transparency laws (financial disclosure, EV charging protections)
- Nevada EV-ready garage requirement: 40-amp, 208/240V dedicated circuit

### Property Tax
- Nevada assesses at 35% of taxable value
- Primary residence increases capped at 3% annually
- Effective rate: ~0.48-0.55%
- Zero state income tax
- Transfer tax: $5.10 per $1,000

### Warranty & Legal
- Nevada 1-2-10 warranty: Year 1 workmanship, Year 2 mechanical, Years 3-10 structural
- NRS 624.602: builders must provide min 1-year warranty
- NRS Chapter 40: 10-year statute of repose, 90-day builder response, mediation required
- 9 out of 10 new homes have at least one significant issue on inspection
- Pre-drywall inspection: $200-$400
- Final inspection: $310-$730
- Average structural warranty claim exceeds $40,000
- Complaints: Del Webb/Lake Las Vegas homes "crumbling" (soil), Beazer/Colton Ranch sinking foundations

### Desert Climate Data
- Las Vegas water hardness: ~17 grains/gallon (very hard)
- Summer attic temps: 140-155F
- AC runs 10-11 months/year
- 25 scorpion species in greater Las Vegas
- Caliche layer makes basements impossible
- No supplemental tax bills (unlike California)
- Grass prohibited in all new properties since April 2022
- SNWA offers $3/sq ft rebate for turf removal
- 310+ sunny days annually

### Buyer Demographics
- California relocators: 47% of Las Vegas-bound moves, ~50,000/year
- Average CA household saves $585,000 in housing + $20K-$40K/year income tax
- Clark County population: ~2,488,043, growing ~1.82%/year
- Tariff impacts: $7,500-$17,500 added per home
- Brightline high-speed rail under construction (LA to Las Vegas)

### 55+ Communities with New Construction
- Del Webb at Lake Las Vegas: from mid-$400s
- Del Webb at North Ranch: North Las Vegas, near VA Hospital
- Heritage at Stonebridge by Lennar: Summerlin, mid-$400s to mid-$800s
- Trilogy Sunstone by Shea Homes: from low $300s
- Esplanade at Red Rock by Taylor Morrison: from $800Ks, Q2 2026
