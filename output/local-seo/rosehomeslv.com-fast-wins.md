# rosehomeslv.com — Fast Wins (paste-ready)

Build-order steps 1–2. All titles ≤60 chars, keyword-first, "Ryan Rose" retained. No em dashes. Schema uses your real NAP + socials; two fields are marked FILL IN because they are not on the site (do not invent them).

---

## 1. SEO Titles (Lofty → each page's SEO settings)

| Page | Recommended title (≤60) | Chars |
|------|--------------------------|-------|
| Home | `Las Vegas Homes for Sale \| Ryan Rose, Realtor` | 45 |
| All Listings | `Las Vegas Homes & Condos for Sale \| Ryan Rose` | 45 |
| Featured Listings | `Featured Las Vegas Listings \| Ryan Rose` | 39 |
| Sold Listings | `Recently Sold Las Vegas Homes \| Ryan Rose` | 41 |
| Sell / Sell My Home | `Sell Your Las Vegas Home \| Ryan Rose, Realtor` | 45 |
| Home Valuation | `What's My Las Vegas Home Worth? \| Ryan Rose` | 43 |
| About Me | `About Ryan Rose \| Las Vegas Realtor` | 35 |
| Contact | `Contact Ryan Rose \| Las Vegas Realtor` | 37 |
| Affordability Calculator | `Home Affordability Calculator \| Ryan Rose LV` | 44 |
| Mortgage Calculator | `Las Vegas Mortgage Calculator \| Ryan Rose` | 41 |
| Blog index | `Las Vegas Real Estate Blog \| Ryan Rose` | 39 |
| Southern Highlands | `Southern Highlands Homes for Sale \| Ryan Rose` | 45 |
| Macdonald Highlands | `MacDonald Highlands Homes for Sale \| Ryan Rose` | 46 |
| Summerlin | `Summerlin Homes for Sale \| Ryan Rose, Realtor` | 45 |
| Henderson | `Henderson NV Homes for Sale \| Ryan Rose` | 39 |

Current titles were all 70 chars and truncating in Google (e.g. "…Ryan Rose with R…").

---

## 2. Homepage meta description (remove the em dash)

**Current (has em dash, breaks brand rule):**
> Explore Las Vegas homes for sale, including luxury and new listings. Buy or sell with Ryan Rose at Rose Homes Las Vegas—trusted local real estate expertise.

**Replace with (150 chars, no em dash):**
> Explore Las Vegas homes for sale, including luxury and new listings. Buy or sell with Ryan Rose at Rose Homes LV, your trusted local real estate expert.

---

## 3. RealEstateAgent schema (Lofty → global header/custom code)

De-dupe the two `Organization` blocks first, then add this. Address and rating are confirmed from the Google Business Profile (CID 3319912745156653211) as of 2026-08-10, so they match your GBP character-for-character. Only the image URL still needs filling.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "RealEstateAgent",
  "name": "Ryan Rose",
  "alternateName": "Rose Homes LV",
  "url": "https://www.rosehomeslv.com/",
  "image": "https://www.rosehomeslv.com/{{HEADSHOT_OR_LOGO.jpg}}",
  "telephone": "+1-702-747-5921",
  "email": "ryan@rosehomeslv.com",
  "priceRange": "$$$",
  "worksFor": { "@type": "RealEstateOrganization", "name": "Real Broker, LLC" },
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "9580 W Sahara Ave Ste 200",
    "addressLocality": "Las Vegas",
    "addressRegion": "NV",
    "postalCode": "89117",
    "addressCountry": "US"
  },
  "areaServed": [
    { "@type": "City", "name": "Las Vegas" },
    { "@type": "City", "name": "Henderson" },
    { "@type": "City", "name": "North Las Vegas" },
    { "@type": "Place", "name": "Summerlin" },
    { "@type": "Place", "name": "Spring Valley" },
    { "@type": "Place", "name": "Centennial Hills" },
    { "@type": "Place", "name": "Skye Canyon" },
    { "@type": "Place", "name": "Green Valley" }
  ],
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "5.0",
    "reviewCount": "5",
    "bestRating": "5"
  },
  "sameAs": [
    "https://www.facebook.com/Rose-Homes-Las-Vegas-Urban-Nest-Realty-407399952453552",
    "https://www.linkedin.com/in/ryanroselvnv",
    "https://twitter.com/TheRealRyanRose",
    "https://www.instagram.com/rosehomeslv",
    "https://www.youtube.com/channel/UCYZaWMyGaFHjqTM8lb5wZyw",
    "https://www.tiktok.com/@rosehomeslv?lang=en",
    "https://maps.google.com/maps?cid=3319912745156653211"
  ]
}
</script>
```

> Rating and count are real (verified on the GBP 2026-08-10). Re-check them whenever new reviews land, and update the markup. Never let the markup claim more than the profile shows.

---

## 4. FAQPage schema (homepage)

Two requirements: (a) the same Q&As must also appear as **visible text** on the homepage (Google requires the content be on-page), and (b) then add this block. All answers below are factual.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What areas does Ryan Rose serve?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ryan Rose serves Las Vegas and the surrounding Clark County communities, including Henderson, Summerlin, Spring Valley, Centennial Hills, North Las Vegas, Skye Canyon, and Green Valley." }
    },
    {
      "@type": "Question",
      "name": "How do I find out what my Las Vegas home is worth?",
      "acceptedAnswer": { "@type": "Answer", "text": "Request a free home valuation on rosehomeslv.com, or contact Ryan Rose directly at 702-747-5921 for a comparative market analysis of your home." }
    },
    {
      "@type": "Question",
      "name": "Does Ryan Rose help with new construction homes?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes. Ryan works with buyers on new construction and builder communities across the Las Vegas valley, in addition to resale homes." }
    },
    {
      "@type": "Question",
      "name": "How can I contact Ryan Rose?",
      "acceptedAnswer": { "@type": "Answer", "text": "Call or text Ryan at 702-747-5921 or email ryan@rosehomeslv.com. Ryan Rose is a licensed Realtor with Real Broker, LLC." }
    },
    {
      "@type": "Question",
      "name": "What makes working with Ryan Rose different?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ryan takes a no-pressure, honest approach, focused on giving you the information you need to make the right decision whether you are buying or selling." }
    }
  ]
}
</script>
```

**Visible FAQ copy to add to the homepage (Lofty custom section):**
- **What areas does Ryan Rose serve?** Ryan Rose serves Las Vegas and the surrounding Clark County communities, including Henderson, Summerlin, Spring Valley, Centennial Hills, North Las Vegas, Skye Canyon, and Green Valley.
- **How do I find out what my Las Vegas home is worth?** Request a free home valuation on rosehomeslv.com, or contact Ryan Rose directly at 702-747-5921 for a comparative market analysis of your home.
- **Does Ryan Rose help with new construction homes?** Yes. Ryan works with buyers on new construction and builder communities across the Las Vegas valley, in addition to resale homes.
- **How can I contact Ryan Rose?** Call or text Ryan at 702-747-5921 or email ryan@rosehomeslv.com. Ryan Rose is a licensed Realtor with Real Broker, LLC.
- **What makes working with Ryan Rose different?** Ryan takes a no-pressure, honest approach, focused on giving you the information you need to make the right decision whether you are buying or selling.

---

## Where to paste in Lofty
- **Titles + meta description:** Lofty site editor → each page → SEO / page settings (Meta Title, Meta Description). The area pages (Southern Highlands, etc.) have their own SEO fields.
- **Schema (both blocks):** Lofty → Site Settings → Advanced / Custom Code (header injection). RealEstateAgent can be global (site-wide); FAQPage should be homepage-only if Lofty allows per-page code, otherwise keep it on the global header only while the FAQ lives on the homepage.
- **H1 fix (separate task):** the triple-H1 is a theme issue — the header tagline and "Rose Homes LV" logo are marked as `<h1>`. Needs a Lofty theme/custom-CSS change to demote them; flagged for a follow-up.
- After pasting, validate both schema blocks in Google's Rich Results Test.
```
