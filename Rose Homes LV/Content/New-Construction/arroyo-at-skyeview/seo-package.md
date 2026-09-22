# SEO PACKAGE: Arroyo at Skyeview

## Keyword Cluster (use across all pages)

**Primary keywords (highest intent):**
1. Arroyo at Skyeview
2. Arroyo at Skyeview Century Communities
3. Arroyo at Skyeview townhomes
4. Skye Canyon townhomes
5. Century Communities Skye Canyon

**Secondary keywords (supporting):**
- new construction townhomes Las Vegas
- Skye Canyon new homes
- new construction 89166
- NW Las Vegas townhomes
- townhomes under $400k Las Vegas
- Century Communities Las Vegas
- Skye Canyon Century Communities
- affordable new construction Las Vegas

**Long-tail (for blog H2s and body copy):**
- Beverly floor plan Arroyo at Skyeview
- Captiva floor plan Arroyo at Skyeview
- Delray floor plan Arroyo at Skyeview
- cheapest new construction in Skye Canyon
- Arroyo at Skyeview HOA fees
- Arroyo at Skyeview SID tax
- new townhomes near US-95 Las Vegas
- 3 bedroom townhomes Skye Canyon
- Skye Canyon schools Bryan Elementary
- Arroyo at Skyeview floor plans and prices
- Arroyo at Skyeview vs single-family Skye Canyon
- new construction townhomes near Aspire Coffee
- townhomes near Smith's Marketplace Skye Canyon
- Arroyo at Skyeview buyer incentives 2026

---

## 1. Community Landing Page (`landing-page.html`)

### Tags
```html
<title>Arroyo at Skyeview Townhomes | From $372,990 Skye Canyon</title>
<meta name="description" content="Arroyo at Skyeview by Century Communities: 3 new townhome plans from $372,990 in Skye Canyon NW Las Vegas. 3 bed, 2.5 bath, low SID. Get the free buyer guide.">
<meta name="keywords" content="Arroyo at Skyeview, Skye Canyon townhomes, Century Communities Las Vegas, new construction 89166, NW Las Vegas townhomes, townhomes under 400k Las Vegas, Skye Canyon new homes, Arroyo at Skyeview floor plans">
<link rel="canonical" href="https://rosehomeslv.com/arroyo-at-skyeview">

<!-- OpenGraph -->
<meta property="og:type" content="website">
<meta property="og:title" content="Arroyo at Skyeview Townhomes by Century Communities | From $372,990 in Skye Canyon">
<meta property="og:description" content="The most affordable new construction in Skye Canyon. Arroyo at Skyeview offers 3 two-story townhome floor plans (Beverly, Captiva, Delray) from $372,990 in NW Las Vegas 89166. 3 bed, 2.5 bath, low SID, master amenities included. Rate buydowns and closing cost help available.">
<meta property="og:url" content="https://rosehomeslv.com/arroyo-at-skyeview">
<meta property="og:image" content="https://rosehomeslv.com/images/arroyo-at-skyeview-hero.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:site_name" content="Rose Homes LV">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Arroyo at Skyeview | New Townhomes from $372,990 in Skye Canyon">
<meta name="twitter:description" content="Century Communities townhomes in NW Las Vegas 89166. 3 plans, 3 bed, 2.5 bath, low SID, master amenities. Free buyer guide from Ryan Rose, Real Broker LLC.">
<meta name="twitter:image" content="https://rosehomeslv.com/images/arroyo-at-skyeview-hero.jpg">
```

### JSON-LD Schema

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Place",
      "@id": "https://rosehomeslv.com/arroyo-at-skyeview#place",
      "name": "Arroyo at Skyeview",
      "description": "New construction townhome community by Century Communities inside the Skye Canyon master plan in NW Las Vegas. The most affordable new build in Skye Canyon with three two-story floor plans from $372,990.",
      "url": "https://rosehomeslv.com/arroyo-at-skyeview",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "8912 Vanhoy Creek St",
        "addressLocality": "Las Vegas",
        "addressRegion": "NV",
        "postalCode": "89166",
        "addressCountry": "US"
      },
      "containedInPlace": {
        "@type": "Place",
        "name": "Skye Canyon"
      },
      "amenityFeature": [
        {"@type": "LocationFeatureSpecification", "name": "Skye Fitness center"},
        {"@type": "LocationFeatureSpecification", "name": "Resort-style pool"},
        {"@type": "LocationFeatureSpecification", "name": "Parks and trails"},
        {"@type": "LocationFeatureSpecification", "name": "Aspire Coffee on-site"},
        {"@type": "LocationFeatureSpecification", "name": "Bryan Elementary (CCSD 9/10 rating) nearby"}
      ]
    },
    {
      "@type": "RealEstateAgent",
      "@id": "https://rosehomeslv.com/#agent",
      "name": "Ryan Rose",
      "url": "https://rosehomeslv.com",
      "telephone": "+1-702-747-5921",
      "email": "ryan@rosehomeslv.com",
      "image": "https://rosehomeslv.com/images/ryan-rose-headshot.jpg",
      "worksFor": {
        "@type": "RealEstateOrganization",
        "name": "Real Broker, LLC"
      },
      "areaServed": [
        {"@type": "Place", "name": "Skye Canyon"},
        {"@type": "Place", "name": "Las Vegas"},
        {"@type": "Place", "name": "Clark County, NV"},
        {"@type": "Place", "name": "Henderson"},
        {"@type": "Place", "name": "North Las Vegas"}
      ],
      "knowsAbout": [
        "New construction homes Las Vegas",
        "Skye Canyon new construction",
        "Century Communities Las Vegas",
        "Townhome buyer representation",
        "SID and LID taxes Las Vegas"
      ]
    }
  ]
}
```

### ItemList schema for floor plans (3 plans)

```json
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "Arroyo at Skyeview Floor Plans",
  "url": "https://rosehomeslv.com/arroyo-at-skyeview",
  "numberOfItems": 3,
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "item": {
        "@type": "Product",
        "name": "Beverly Floor Plan at Arroyo at Skyeview",
        "description": "Two-story townhome by Century Communities. 1,531 sq ft, 3 bedrooms, 2.5 bathrooms in Skye Canyon, NW Las Vegas.",
        "brand": {"@type": "Brand", "name": "Century Communities"},
        "category": "New construction townhome",
        "offers": {
          "@type": "Offer",
          "price": "372990",
          "priceCurrency": "USD",
          "availability": "https://schema.org/InStock",
          "url": "https://rosehomeslv.com/arroyo-at-skyeview"
        }
      }
    },
    {
      "@type": "ListItem",
      "position": 2,
      "item": {
        "@type": "Product",
        "name": "Captiva Floor Plan at Arroyo at Skyeview",
        "description": "Two-story townhome by Century Communities. 1,643 sq ft, 3 bedrooms, 2.5 bathrooms in Skye Canyon, NW Las Vegas.",
        "brand": {"@type": "Brand", "name": "Century Communities"},
        "category": "New construction townhome",
        "offers": {
          "@type": "Offer",
          "price": "382990",
          "priceCurrency": "USD",
          "availability": "https://schema.org/InStock",
          "url": "https://rosehomeslv.com/arroyo-at-skyeview"
        }
      }
    },
    {
      "@type": "ListItem",
      "position": 3,
      "item": {
        "@type": "Product",
        "name": "Delray Floor Plan at Arroyo at Skyeview",
        "description": "Two-story townhome by Century Communities. 1,729 sq ft, 3 bedrooms, 2.5 bathrooms in Skye Canyon, NW Las Vegas.",
        "brand": {"@type": "Brand", "name": "Century Communities"},
        "category": "New construction townhome",
        "offers": {
          "@type": "Offer",
          "price": "392990",
          "priceCurrency": "USD",
          "availability": "https://schema.org/InStock",
          "url": "https://rosehomeslv.com/arroyo-at-skyeview"
        }
      }
    }
  ]
}
```

### SEO rationale
Century's own page buries the price and product type behind brand-first language. Our title front-loads the community name, the price hook ($372,990) and the master plan (Skye Canyon) in 58 characters, and the description packs builder, plan count, price, beds/baths, low SID, and the free buyer guide into 154 characters, giving searchers the three things they care about (price, location, what to do next) before they click.

---

## 2. Master Directory (`master-landing-page.html`)

### Tags
```html
<title>New Construction Homes Las Vegas 2026 | Builder Communities Guide</title>
<meta name="description" content="Compare new construction homes in Las Vegas and Clark County NV. Browse Skye Canyon, Summerlin, Henderson and more, with builder pricing, plans, and free buyer guides.">
<meta name="keywords" content="new construction Las Vegas, new homes Clark County NV, new construction townhomes Las Vegas, new construction Skye Canyon, Las Vegas builders 2026, new homes 89166, new construction Henderson, Summerlin new homes">
<link rel="canonical" href="https://rosehomeslv.com/new-construction-las-vegas">

<!-- OpenGraph -->
<meta property="og:type" content="website">
<meta property="og:title" content="New Construction Homes in Las Vegas 2026 | Communities, Builders, Prices">
<meta property="og:description" content="Your full directory of new construction communities in Las Vegas and Clark County NV. Compare Century Communities, Lennar, KB Home, Richmond American and more across Skye Canyon, Summerlin, Henderson and North Las Vegas. Floor plans, prices, incentives, and free buyer guides from Ryan Rose, Real Broker LLC.">
<meta property="og:url" content="https://rosehomeslv.com/new-construction-las-vegas">
<meta property="og:image" content="https://rosehomeslv.com/images/new-construction-las-vegas-hero.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:site_name" content="Rose Homes LV">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="New Construction Homes Las Vegas 2026 | Communities Directory">
<meta name="twitter:description" content="Compare every major new construction community in Las Vegas. Builders, plans, prices, incentives, and free buyer guides from Ryan Rose, Real Broker LLC.">
<meta name="twitter:image" content="https://rosehomeslv.com/images/new-construction-las-vegas-hero.jpg">
```

### JSON-LD Schema

```json
{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "name": "New Construction Homes in Las Vegas 2026",
  "url": "https://rosehomeslv.com/new-construction-las-vegas",
  "description": "Directory of active new construction communities across Las Vegas and Clark County NV, organized by builder, master plan, and price.",
  "isPartOf": {
    "@type": "WebSite",
    "name": "Rose Homes LV",
    "url": "https://rosehomeslv.com"
  },
  "about": [
    {"@type": "Thing", "name": "New construction homes"},
    {"@type": "Place", "name": "Las Vegas, NV"},
    {"@type": "Place", "name": "Clark County, NV"}
  ],
  "author": {
    "@type": "RealEstateAgent",
    "name": "Ryan Rose",
    "telephone": "+1-702-747-5921",
    "email": "ryan@rosehomeslv.com",
    "worksFor": {"@type": "RealEstateOrganization", "name": "Real Broker, LLC"}
  },
  "mainEntity": {
    "@type": "ItemList",
    "name": "Las Vegas New Construction Communities",
    "description": "Assembled by the Master Page Developer from each community landing page in this workspace.",
    "itemListElement": []
  }
}
```

Note to Master Page Developer: populate `mainEntity.itemListElement` with one ListItem per community card on the page, each pointing at the community's canonical URL (for example `https://rosehomeslv.com/arroyo-at-skyeview`, `https://rosehomeslv.com/sierra-at-skyeview`, `https://rosehomeslv.com/skyeview-terra`).

### SEO rationale
Master directory targets the high-volume head term "new construction Las Vegas" rather than any one community, and the description signals comprehensive coverage (multiple builders, multiple master plans, free buyer guides) so it competes with builder aggregator sites instead of any single builder's listing page.

---

## 3. Per-Plan Blog Guidance (passed to Blog Writer)

### Title pattern
`[Plan Name] at Arroyo at Skyeview | [Sqft] sq ft from $[Price] in NW Las Vegas`

### Description pattern
`The [Plan Name] floor plan at Arroyo at Skyeview offers [sqft] sq ft, [beds] beds, [baths] baths from $[price]. [Top feature]. Get the free Arroyo buyer guide from Ryan Rose, Real Broker LLC.`

### Per-plan keyword formulas
- `[Plan Name] floor plan Arroyo Skyeview`
- `[Plan Name] Arroyo at Skyeview price`
- `[Plan Name] Century Communities Las Vegas`
- `[Plan Name] townhome Skye Canyon`

### Plan-specific guidance

#### Beverly (1,531 sf, 3 bed, 2.5 bath, from $372,990)

**Title (60 chars):**
`Beverly at Arroyo at Skyeview | 1,531 sf from $372,990 NW LV`

**Description (152 chars):**
`The Beverly floor plan at Arroyo at Skyeview offers 1,531 sq ft, 3 beds, 2.5 baths from $372,990. Most affordable new build in Skye Canyon. Free buyer guide.`

**Keywords:**
- Beverly floor plan Arroyo Skyeview
- Beverly Arroyo at Skyeview price
- Beverly Century Communities Las Vegas
- Beverly townhome Skye Canyon
- entry-level new townhome Las Vegas 89166
- cheapest new construction Skye Canyon

**H2 ideas:**
1. Beverly floor plan: what you get for $372,990
2. Two-story townhome layout: 3 beds and 2.5 baths in 1,531 sq ft
3. Why the Beverly is the cheapest way into Skye Canyon
4. What the HOA and SID look like on the Beverly

#### Captiva (1,643 sf, 3 bed, 2.5 bath, from $382,990)

**Title (60 chars):**
`Captiva at Arroyo at Skyeview | 1,643 sf from $382,990 NW LV`

**Description (153 chars):**
`The Captiva floor plan at Arroyo at Skyeview offers 1,643 sq ft, 3 beds, 2.5 baths from $382,990. Mid-size townhome in Skye Canyon 89166. Free buyer guide.`

**Keywords:**
- Captiva floor plan Arroyo Skyeview
- Captiva Arroyo at Skyeview price
- Captiva Century Communities Las Vegas
- Captiva townhome Skye Canyon
- 3 bedroom new townhome NW Las Vegas
- Skye Canyon townhomes under $390k

**H2 ideas:**
1. Captiva floor plan: the middle option at Arroyo at Skyeview
2. How the extra 112 sq ft over the Beverly changes the layout
3. Captiva pricing, HOA, and SID breakdown
4. Who the Captiva is built for: small families and roommates

#### Delray (1,729 sf, 3 bed, 2.5 bath, from $392,990)

**Title (60 chars):**
`Delray at Arroyo at Skyeview | 1,729 sf from $392,990 NW LV`

**Description (151 chars):**
`The Delray floor plan at Arroyo at Skyeview offers 1,729 sq ft, 3 beds, 2.5 baths from $392,990. Largest townhome plan in Skye Canyon 89166. Free buyer guide.`

**Keywords:**
- Delray floor plan Arroyo Skyeview
- Delray Arroyo at Skyeview price
- Delray Century Communities Las Vegas
- Delray townhome Skye Canyon
- largest townhome Arroyo at Skyeview
- 1700 sq ft new townhome Las Vegas

**H2 ideas:**
1. Delray floor plan: the largest townhome at Arroyo at Skyeview
2. 1,729 sq ft, 3 beds, 2.5 baths: what fits inside
3. Is the Delray worth $20K more than the Beverly?
4. Total monthly cost on a Delray with current incentives

### Main community blog guidance (`arroyo-at-skyeview.html`)

**Title (59 chars):**
`Arroyo at Skyeview Guide 2026 | Townhomes from $372,990 LV`

**Description (154 chars):**
`Arroyo at Skyeview by Century Communities: 3 townhome plans from $372,990 in Skye Canyon NW Las Vegas. Schools, HOA, SID, incentives, and a free buyer guide.`

**Keywords:**
- Arroyo at Skyeview
- Arroyo at Skyeview Century Communities
- Arroyo at Skyeview floor plans
- Skye Canyon townhomes
- new construction 89166
- Century Communities Skye Canyon
- Arroyo at Skyeview HOA
- Arroyo at Skyeview SID

**H2 ideas:**
1. Arroyo at Skyeview at a glance: builder, plans, prices
2. The three floor plans: Beverly, Captiva, Delray side by side
3. Why Arroyo is the most affordable new build in Skye Canyon
4. Schools and amenities: Bryan Elementary, Skye Fitness, Aspire Coffee
5. The real monthly cost: HOA, SID, and current rate buydowns
6. Is Arroyo at Skyeview right for you? Buyer profile and tradeoffs

---

## 4. Schema Recommendations for Landing Page Developer

Include three schema blocks on `landing-page.html`, each in its own `<script type="application/ld+json">`:

1. The Place + RealEstateAgent `@graph` block from section 1 (community identity and author authority).
2. The ItemList of 3 floor plans (Beverly, Captiva, Delray) from section 1 (so Google can build rich product results for plans and prices).
3. Optional: a BreadcrumbList tying the page back to the master directory.

Suggested BreadcrumbList:

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://rosehomeslv.com"},
    {"@type": "ListItem", "position": 2, "name": "New Construction Las Vegas", "item": "https://rosehomeslv.com/new-construction-las-vegas"},
    {"@type": "ListItem", "position": 3, "name": "Arroyo at Skyeview", "item": "https://rosehomeslv.com/arroyo-at-skyeview"}
  ]
}
```

---

## 5. Internal Linking Recommendations

- Master directory: https://rosehomeslv.com/new-construction-las-vegas
- Related blogs:
  - www.rosehomeslv.com/blog/new-construction-homes-cost-las-vegas-2026 (link from the pricing or "real monthly cost" section)
  - www.rosehomeslv.com/blog/top-home-builders-las-vegas-2026 (link from any mention of Century Communities)
  - www.rosehomeslv.com/blog/sid-lid-taxes-explained-las-vegas-new-construction (link from the SID callout, this community's low ~$138/year SID is a key selling point)
  - www.rosehomeslv.com/blog/best-areas-new-construction-las-vegas-2026 (link from Skye Canyon / NW Las Vegas section)
  - www.rosehomeslv.com/blog/new-construction-vs-resale-homes-las-vegas (link from the "is this right for you" section)
  - www.rosehomeslv.com/blog/hidden-costs-new-construction-las-vegas (link from the HOA + SID + closing cost discussion)
  - www.rosehomeslv.com/blog/builder-incentives-las-vegas-2026 (link from the rate buydown / $5K closing cost incentive callout)
  - www.rosehomeslv.com/blog/first-time-buyer-las-vegas-new-construction (link from the Beverly plan section, since it is the entry-level option)
- Sibling Skyeview communities (cross-link from "explore other Skyeview communities" or comparison section):
  - https://rosehomeslv.com/sierra-at-skyeview
  - https://rosehomeslv.com/skyeview-terra
