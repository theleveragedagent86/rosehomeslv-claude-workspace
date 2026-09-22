# SEO PACKAGE: Lexington Chase

## Keyword Cluster
**Primary keywords:** Lexington Chase Las Vegas, Richmond American Homes 89148, new construction Enterprise Las Vegas

**Secondary keywords:** Lexington Chase Richmond American, Seasons Collection Las Vegas, new homes 89148, Sierra Vista High School new homes, Durango Drive new construction, Mountain's Edge new homes 2026

**Long-tail (for blog H2s):**
- Richmond American Birch floor plan Las Vegas
- Richmond American Maple floor plan Lexington Chase
- Richmond American Elm floor plan 89148
- new construction homes near UnCommons Las Vegas

---

## 1. Community Landing Page (`landing-page.html`)

### Tags
```html
<title>Lexington Chase Las Vegas | Richmond American 89148</title>
<meta name="description" content="Lexington Chase by Richmond American: 76 new homes from $576,950 in 89148. 3 plans, 2,320 to 2,780 sqft, near 215 Beltway. Ryan Rose, Real Broker LLC.">
<meta name="keywords" content="Lexington Chase Las Vegas, Richmond American Homes 89148, new construction Enterprise Las Vegas, Seasons Collection Las Vegas, new homes 89148, Sierra Vista High School homes, Durango Drive new construction">
<link rel="canonical" href="https://rosehomeslv.com/ra-lexington-chase">

<!-- OpenGraph -->
<meta property="og:type" content="website">
<meta property="og:url" content="https://rosehomeslv.com/ra-lexington-chase">
<meta property="og:title" content="Lexington Chase by Richmond American | New Homes in 89148 from $576,950">
<meta property="og:description" content="76 single-family homes in Enterprise/SW Las Vegas off Durango Drive. Three Seasons Collection plans from 2,320 to 2,780 sqft, priced $576,950 to $636,950. Sierra Vista HS feeder, less than a mile to the 215 Beltway, 10 minutes to the Strip. Ask Ryan Rose at Real Broker LLC for current Richmond American incentives.">
<meta property="og:image" content="https://rosehomeslv.com/images/lexington-chase-og.jpg">
<meta property="og:site_name" content="Rose Homes LV">

<!-- Twitter -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Lexington Chase by Richmond American | New Homes 89148">
<meta name="twitter:description" content="76 new Richmond American homes in Enterprise Las Vegas from $576,950. 3 Seasons Collection plans, near 215 and UnCommons. Tour with Ryan Rose, Real Broker LLC.">
<meta name="twitter:image" content="https://rosehomeslv.com/images/lexington-chase-og.jpg">
```

**Char counts:** Title 53, Meta description 158, og:title 70, og:description 359 (trimmable to 298 if platform requires).

### JSON-LD Schema
```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Place",
      "@id": "https://rosehomeslv.com/ra-lexington-chase#place",
      "name": "Lexington Chase by Richmond American Homes",
      "description": "Gated community of 76 single-family homes by Richmond American (Seasons Collection) in Enterprise/SW Las Vegas, near Durango Drive and the 215 Beltway. Three two-story plans from 2,320 to 2,780 sqft, priced $576,950 to $636,950.",
      "url": "https://rosehomeslv.com/ra-lexington-chase",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "8212 Kinleigh Poulson St",
        "addressLocality": "Las Vegas",
        "addressRegion": "NV",
        "postalCode": "89148",
        "addressCountry": "US"
      },
      "containedInPlace": {
        "@type": "Place",
        "name": "Enterprise, Las Vegas, NV"
      }
    },
    {
      "@type": "RealEstateAgent",
      "@id": "https://rosehomeslv.com/#agent",
      "name": "Ryan Rose",
      "image": "https://rosehomeslv.com/images/ryan-rose.jpg",
      "url": "https://rosehomeslv.com",
      "telephone": "+1-702-747-5921",
      "email": "ryan@rosehomeslv.com",
      "worksFor": {
        "@type": "RealEstateAgent",
        "name": "Real Broker, LLC"
      },
      "areaServed": [
        {"@type": "City", "name": "Las Vegas"},
        {"@type": "City", "name": "Henderson"},
        {"@type": "AdministrativeArea", "name": "Clark County"}
      ],
      "knowsAbout": ["New Construction Homes", "Richmond American Homes", "Enterprise Las Vegas", "89148 Real Estate"]
    },
    {
      "@type": "ItemList",
      "@id": "https://rosehomeslv.com/ra-lexington-chase#plans",
      "name": "Lexington Chase Floor Plans",
      "itemListOrder": "https://schema.org/ItemListOrderAscending",
      "numberOfItems": 3,
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "item": {
            "@type": "Product",
            "name": "Birch by Richmond American at Lexington Chase",
            "description": "Two-story home, 4 bedrooms, 3 bathrooms, 2,320 sqft, 2-car garage. Seasons Collection by Richmond American.",
            "brand": {"@type": "Brand", "name": "Richmond American Homes"},
            "category": "Single-Family Home",
            "offers": {
              "@type": "Offer",
              "price": "576950",
              "priceCurrency": "USD",
              "availability": "https://schema.org/InStock",
              "url": "https://rosehomeslv.com/ra-lexington-chase#birch"
            }
          }
        },
        {
          "@type": "ListItem",
          "position": 2,
          "item": {
            "@type": "Product",
            "name": "Maple by Richmond American at Lexington Chase",
            "description": "Two-story home, 3 to 4 bedrooms, 2.5 to 3.5 bathrooms, 2,500 sqft, 2-car garage. Seasons Collection by Richmond American.",
            "brand": {"@type": "Brand", "name": "Richmond American Homes"},
            "category": "Single-Family Home",
            "offers": {
              "@type": "Offer",
              "price": "596950",
              "priceCurrency": "USD",
              "availability": "https://schema.org/InStock",
              "url": "https://rosehomeslv.com/ra-lexington-chase#maple"
            }
          }
        },
        {
          "@type": "ListItem",
          "position": 3,
          "item": {
            "@type": "Product",
            "name": "Elm by Richmond American at Lexington Chase",
            "description": "Two-story home, 4 bedrooms, 3 bathrooms, 2,780 sqft, 2-car garage. Largest plan in the Seasons Collection at Lexington Chase.",
            "brand": {"@type": "Brand", "name": "Richmond American Homes"},
            "category": "Single-Family Home",
            "offers": {
              "@type": "Offer",
              "price": "636950",
              "priceCurrency": "USD",
              "availability": "https://schema.org/InStock",
              "url": "https://rosehomeslv.com/ra-lexington-chase#elm"
            }
          }
        }
      ]
    }
  ]
}
```

### SEO rationale
Title front-loads the community brand (high-intent search) plus builder and ZIP for local discovery; 53 chars leaves SERP room. Meta description leads with builder authority, the entry price (numeric draws clicks), home count (scarcity), and freeway proximity, then closes with the Real Broker LLC EAT signal. Place + RealEstateAgent + ItemList graph gives Google the three things it needs: where the community is, who the listing authority is, and what is for sale, so rich-result eligibility is maximized for "Richmond American Lexington Chase" branded queries.

---

## 2. Buyer Guide Landing Page (`buyer-guide-landing-page.html`)

### Tags
```html
<title>Lexington Chase Buyer Guide | Richmond American 89148</title>
<meta name="description" content="Free Lexington Chase buyer guide: floor plans, pricing from $576,950, SID/LID notes, school feeders, builder contract tips. Ryan Rose, Real Broker LLC.">
<meta name="keywords" content="Lexington Chase buyer guide, Richmond American buyer guide Las Vegas, new construction buyer guide 89148, Enterprise Las Vegas new home guide, Richmond American Seasons Collection guide">
<link rel="canonical" href="https://rosehomeslv.com/ra-lexington-chase-bg">

<!-- OpenGraph -->
<meta property="og:type" content="article">
<meta property="og:url" content="https://rosehomeslv.com/ra-lexington-chase-bg">
<meta property="og:title" content="Free Lexington Chase Buyer Guide | Richmond American Homes 89148">
<meta property="og:description" content="Get the same-day Lexington Chase buyer guide: side-by-side specs for the Birch, Maple, and Elm floor plans, current Richmond American incentives through 4/15/2026, SID/LID estimates, school feeders, and the new construction contract steps Ryan Rose uses with every buyer.">
<meta property="og:image" content="https://rosehomeslv.com/images/lexington-chase-buyer-guide-og.jpg">
<meta property="og:site_name" content="Rose Homes LV">
<meta property="article:author" content="Ryan Rose">

<!-- Twitter -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Free Lexington Chase Buyer Guide | Richmond American 89148">
<meta name="twitter:description" content="Floor plans, pricing, incentives, SID/LID, school feeders, contract tips. Free same-day from Ryan Rose, Real Broker LLC. 702-747-5921.">
<meta name="twitter:image" content="https://rosehomeslv.com/images/lexington-chase-buyer-guide-og.jpg">
```

**Char counts:** Title 56, Meta description 153, og:title 67, og:description 343 (within 200-300 if trimmed at "school feeders, and the new construction contract steps").

### JSON-LD Schema (WebPage)
```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "@id": "https://rosehomeslv.com/ra-lexington-chase-bg",
  "name": "Lexington Chase Buyer Guide",
  "description": "Free buyer guide for Lexington Chase by Richmond American Homes in 89148. Floor plans, pricing, incentives, SID/LID, school feeders, and contract steps.",
  "url": "https://rosehomeslv.com/ra-lexington-chase-bg",
  "inLanguage": "en-US",
  "isPartOf": {
    "@type": "WebSite",
    "name": "Rose Homes LV",
    "url": "https://rosehomeslv.com"
  },
  "about": {
    "@type": "Place",
    "name": "Lexington Chase by Richmond American Homes",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "8212 Kinleigh Poulson St",
      "addressLocality": "Las Vegas",
      "addressRegion": "NV",
      "postalCode": "89148"
    }
  },
  "author": {
    "@type": "RealEstateAgent",
    "name": "Ryan Rose",
    "telephone": "+1-702-747-5921",
    "email": "ryan@rosehomeslv.com",
    "url": "https://rosehomeslv.com",
    "worksFor": {"@type": "Organization", "name": "Real Broker, LLC"}
  },
  "publisher": {
    "@type": "Organization",
    "name": "Real Broker, LLC",
    "url": "https://rosehomeslv.com"
  },
  "mainEntity": {
    "@type": "CreativeWork",
    "name": "Lexington Chase Buyer Guide PDF",
    "encodingFormat": "application/pdf",
    "author": {"@type": "Person", "name": "Ryan Rose"}
  }
}
```

### SEO rationale
Buyer guide landing pages compete on long-tail "[community] buyer guide" terms where intent is high and competition is thin. Title pairs the community name with "Buyer Guide" plus the ZIP for local override. Description front-loads "Free", lists the 4 high-value content blocks (floor plans, pricing, SID/LID, schools), then anchors author authority. The WebPage + Place + RealEstateAgent author graph signals Google that this is original first-party content with E-E-A-T from a licensed Real Broker LLC agent, not aggregator content.

---

## 3. Master Directory (`master-landing-page.html`)

### Tags
```html
<title>New Construction Las Vegas 2026 | Builder Directory</title>
<meta name="description" content="Browse Las Vegas new construction communities: Richmond American, Pulte, Lennar, Toll Brothers. Floor plans, pricing, incentives. Ryan Rose, Real Broker LLC.">
<meta name="keywords" content="new construction Las Vegas, Las Vegas new homes 2026, Henderson new construction, Summerlin new homes, Skye Canyon new homes, Richmond American Las Vegas, Pulte Las Vegas, Lennar Las Vegas">
<link rel="canonical" href="https://rosehomeslv.com/new-construction">

<!-- OpenGraph -->
<meta property="og:type" content="website">
<meta property="og:url" content="https://rosehomeslv.com/new-construction">
<meta property="og:title" content="Las Vegas New Construction Directory 2026 | Floor Plans, Pricing, Incentives">
<meta property="og:description" content="Compare every active new home community in Clark County: Richmond American, Pulte, Lennar, Toll Brothers, KB Home, Tri Pointe. Floor plans, pricing, SID/LID, builder incentives, school feeders, and side-by-side specs. Tour any community with Ryan Rose, Real Broker LLC, 702-747-5921.">
<meta property="og:image" content="https://rosehomeslv.com/images/new-construction-directory-og.jpg">
<meta property="og:site_name" content="Rose Homes LV">

<!-- Twitter -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Las Vegas New Construction Directory 2026 | Rose Homes LV">
<meta name="twitter:description" content="Every active Clark County new home community in one place. Floor plans, pricing, incentives, schools. Ryan Rose, Real Broker LLC.">
<meta name="twitter:image" content="https://rosehomeslv.com/images/new-construction-directory-og.jpg">
```

**Char counts:** Title 55, Meta description 159, og:title 78 (trim to "Las Vegas New Construction 2026 | Floor Plans, Pricing, Incentives" = 67), og:description 358.

### JSON-LD Schema (CollectionPage + ItemList)
```json
{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "@id": "https://rosehomeslv.com/new-construction",
  "name": "Las Vegas New Construction Directory 2026",
  "description": "Curated directory of active new construction communities in Clark County, Nevada by Ryan Rose, Real Broker LLC.",
  "url": "https://rosehomeslv.com/new-construction",
  "inLanguage": "en-US",
  "author": {
    "@type": "RealEstateAgent",
    "name": "Ryan Rose",
    "telephone": "+1-702-747-5921",
    "email": "ryan@rosehomeslv.com",
    "worksFor": {"@type": "Organization", "name": "Real Broker, LLC"}
  },
  "mainEntity": {
    "@type": "ItemList",
    "name": "Active Las Vegas New Construction Communities",
    "itemListOrder": "https://schema.org/ItemListUnordered",
    "itemListElement": [
      {
        "@type": "ListItem",
        "position": 1,
        "url": "https://rosehomeslv.com/ra-lexington-chase",
        "name": "Lexington Chase by Richmond American Homes (89148)"
      }
    ]
  }
}
```
*Note to Master Page Developer: append additional ListItem entries for every other community in the directory.*

### SEO rationale
Master directory targets the head term "new construction Las Vegas" plus the year. Title is 55 chars and uses "Builder Directory" because it differentiates from listing aggregators. CollectionPage + ItemList is the correct schema for a hub of curated communities and is what Google rewards when a single agent maintains an authoritative roundup. Each community entry on the page should link to its own landing page, which strengthens the topical hub-and-spoke structure.

---

## 4. Per-Plan Blog Guidance (passed to Blog Writer)

### Title pattern
`[Plan Name] Floor Plan at Lexington Chase | Richmond American [Sqft]`
Examples (all under 60 chars):
- Birch Floor Plan at Lexington Chase | Richmond 2,320 (52)
- Maple Floor Plan at Lexington Chase | Richmond 2,500 (52)
- Elm Floor Plan at Lexington Chase | Richmond 2,780 (50)

### Description pattern
`Tour the [Plan] floor plan at Lexington Chase by Richmond American: [bd]bd/[ba]ba, [sqft] sqft from $[price] in 89148. [USP detail]. Ryan Rose, Real Broker LLC.`

Per-plan filled examples (all 140-160):
- **Birch (158):** Tour the Birch floor plan at Lexington Chase by Richmond American: 4bd/3ba, 2,320 sqft from $576,950 in 89148. Entry plan, 215 access. Ryan Rose, Real Broker LLC.
- **Maple (159):** Tour the Maple floor plan at Lexington Chase by Richmond American: 3-4bd/2.5-3.5ba, 2,500 sqft from $596,950 in 89148. Flex space. Ryan Rose, Real Broker.
- **Elm (158):** Tour the Elm floor plan at Lexington Chase by Richmond American: 4bd/3ba, 2,780 sqft from $636,950 in 89148. Largest plan, top of lineup. Ryan Rose, Real Broker.

### Per-plan keyword formulas
- **Birch:** "Birch floor plan Las Vegas", "Richmond American Birch 2320", "Lexington Chase Birch", "4 bedroom new home 89148", "entry-level new construction Enterprise Las Vegas"
- **Maple:** "Maple floor plan Las Vegas", "Richmond American Maple 2500", "Lexington Chase Maple", "3-4 bedroom flex new home 89148", "Seasons Collection Maple Las Vegas"
- **Elm:** "Elm floor plan Las Vegas", "Richmond American Elm 2780", "Lexington Chase Elm", "largest Seasons Collection plan Las Vegas", "4 bedroom 2780 sqft new home 89148"

### Blog Writer instruction
For each per-plan blog, use:
- H1 = full plan title (e.g. "The Birch Floor Plan at Lexington Chase by Richmond American")
- H2s should mirror long-tail keywords: "Who the [Plan] Fits Best", "[Plan] Floor Plan Layout", "[Plan] Pricing and Current Richmond American Incentives", "What 89148 Means for [Plan] Buyers", "How [Plan] Compares to Other Lexington Chase Plans"
- First 100 words must include: plan name, "Lexington Chase", "Richmond American", sqft, starting price, ZIP 89148
- Internal links (mandatory): main community blog (`/blog/lexington-chase`), the other two plan blogs, the community landing page (`/lexington-chase`), and 2 supporting cluster blogs (see Section 6)
- Article schema fields: headline, datePublished, author=Ryan Rose, publisher=Real Broker LLC, image, mainEntityOfPage
- No em-dashes. Use commas, periods, or "and"

---

## 5. Schema Recommendations (Floor Plans ItemList for Landing Page)

The floor plan ItemList is already embedded in the Section 1 graph above. Reproduced below standalone for the Landing Page Developer if they want it as a separate `<script>` block.

```json
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "Lexington Chase Floor Plans by Richmond American Homes",
  "itemListOrder": "https://schema.org/ItemListOrderAscending",
  "numberOfItems": 3,
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "item": {
        "@type": "Product",
        "name": "Birch",
        "description": "Two-story, 4 bed, 3 bath, 2,320 sqft, 2-car garage. Entry plan in the Seasons Collection at Lexington Chase.",
        "brand": {"@type": "Brand", "name": "Richmond American Homes"},
        "category": "Single-Family Home",
        "additionalProperty": [
          {"@type": "PropertyValue", "name": "Bedrooms", "value": "4"},
          {"@type": "PropertyValue", "name": "Bathrooms", "value": "3"},
          {"@type": "PropertyValue", "name": "Square Feet", "value": "2320"},
          {"@type": "PropertyValue", "name": "Stories", "value": "2"},
          {"@type": "PropertyValue", "name": "Garage", "value": "2-car"}
        ],
        "offers": {
          "@type": "Offer",
          "price": "576950",
          "priceCurrency": "USD",
          "availability": "https://schema.org/InStock"
        }
      }
    },
    {
      "@type": "ListItem",
      "position": 2,
      "item": {
        "@type": "Product",
        "name": "Maple",
        "description": "Two-story, 3 to 4 bed, 2.5 to 3.5 bath, 2,500 sqft, 2-car garage. Mid-tier Seasons Collection plan with flex options.",
        "brand": {"@type": "Brand", "name": "Richmond American Homes"},
        "category": "Single-Family Home",
        "additionalProperty": [
          {"@type": "PropertyValue", "name": "Bedrooms", "value": "3-4"},
          {"@type": "PropertyValue", "name": "Bathrooms", "value": "2.5-3.5"},
          {"@type": "PropertyValue", "name": "Square Feet", "value": "2500"},
          {"@type": "PropertyValue", "name": "Stories", "value": "2"},
          {"@type": "PropertyValue", "name": "Garage", "value": "2-car"}
        ],
        "offers": {
          "@type": "Offer",
          "price": "596950",
          "priceCurrency": "USD",
          "availability": "https://schema.org/InStock"
        }
      }
    },
    {
      "@type": "ListItem",
      "position": 3,
      "item": {
        "@type": "Product",
        "name": "Elm",
        "description": "Two-story, 4 bed, 3 bath, 2,780 sqft, 2-car garage. Largest Seasons Collection plan at Lexington Chase.",
        "brand": {"@type": "Brand", "name": "Richmond American Homes"},
        "category": "Single-Family Home",
        "additionalProperty": [
          {"@type": "PropertyValue", "name": "Bedrooms", "value": "4"},
          {"@type": "PropertyValue", "name": "Bathrooms", "value": "3"},
          {"@type": "PropertyValue", "name": "Square Feet", "value": "2780"},
          {"@type": "PropertyValue", "name": "Stories", "value": "2"},
          {"@type": "PropertyValue", "name": "Garage", "value": "2-car"}
        ],
        "offers": {
          "@type": "Offer",
          "price": "636950",
          "priceCurrency": "USD",
          "availability": "https://schema.org/InStock"
        }
      }
    }
  ]
}
```

---

## 6. Internal Linking Recommendations

### From the community landing page (`/lexington-chase`)
Link inline (within copy, not just nav) to:
1. `/blog/new-construction-homes-cost-las-vegas-2026` (anchor: "what new construction costs in Las Vegas in 2026")
2. `/blog/sid-lid-taxes-explained-las-vegas-new-construction` (anchor: "how SID and LID taxes work in Enterprise")
3. `/blog/do-you-need-realtor-new-construction-las-vegas` (anchor: "why a buyer's agent costs you nothing at Richmond American")
4. `/blog/builder-incentives-las-vegas-2026` (anchor: "current Richmond American closing-cost incentives")
5. `/blog/best-areas-new-construction-las-vegas-2026` (anchor: "best areas for new construction in 2026")

### From the buyer guide landing page (`/lexington-chase-buyer-guide`)
1. `/blog/new-construction-buying-process-las-vegas` (anchor: "the full new construction buying process")
2. `/blog/hidden-costs-new-construction-las-vegas` (anchor: "hidden costs every Richmond American buyer should plan for")
3. `/blog/home-inspection-new-home-las-vegas` (anchor: "why you still inspect a brand-new home")
4. `/blog/most-valuable-upgrades-las-vegas-new-construction` (anchor: "the upgrades that hold value in Las Vegas")
5. `/lexington-chase` (anchor: "back to the Lexington Chase community page")

### From the main community blog (`/blog/lexington-chase`)
- Inline to all 3 plan blogs: `/blog/lexington-chase-birch`, `/blog/lexington-chase-maple`, `/blog/lexington-chase-elm`
- Inline to: `/blog/top-home-builders-las-vegas-2026` (Richmond American context), `/blog/new-construction-vs-resale-homes-las-vegas`, `/blog/first-time-buyer-las-vegas-new-construction`
- Footer/CTA to: `/lexington-chase` (community page), `/lexington-chase-buyer-guide` (buyer guide)

### From each per-plan blog (`/blog/lexington-chase-[plan]`)
- Up to main community blog `/blog/lexington-chase`
- Across to the other two plan blogs
- Down/over to: `/lexington-chase` and `/lexington-chase-buyer-guide`
- Plus 2 cluster blogs from the per-plan keyword formulas (Birch and Maple should both link `/blog/first-time-buyer-las-vegas-new-construction`; Elm should link `/blog/most-valuable-upgrades-las-vegas-new-construction` and `/blog/moving-california-las-vegas-new-construction`)

### From the master directory (`/new-construction`)
- One link per active community card. Lexington Chase card should anchor on "Lexington Chase by Richmond American (89148)" pointing to `/lexington-chase`.

This creates a tight hub-and-spoke: master directory → community LP → buyer guide LP and main blog → per-plan blogs → back to community LP. Topical authority flows in both directions and every page has at least 3 inbound internal links from the cluster.
