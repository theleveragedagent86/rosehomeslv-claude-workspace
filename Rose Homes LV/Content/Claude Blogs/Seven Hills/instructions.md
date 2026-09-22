# Seven Hills Henderson Blog Project: Instructions

## Project Overview
Creating a comprehensive SEO/AEO optimized blog library for Seven Hills Henderson to establish Ryan Rose as the definitive local expert for this community on rosehomeslv.com.

## Key Reference
- **Website:** www.rosehomeslv.com
- **Blog URL pattern:** www.rosehomeslv.com/blog/[slug] (NOTE: /blog/ not /blogs/)
- **Expert/Author:** Ryan Rose, Las Vegas Real Estate Expert
- **Community:** Seven Hills, Henderson, NV 89052

## Blog Post HTML Format (Match Live Site Exactly)
The CMS renders the blog title as the page heading automatically. The HTML body content we provide follows this exact structure:

```html
<h2>Explore More Las Vegas Communities</h2>

<p><a href="https://www.rosehomeslv.com/blog/[slug-1]">[Title of Related Post 1]</a></p>

<p><a href="https://www.rosehomeslv.com/blog/[slug-2]">[Title of Related Post 2]</a></p>

<p><a href="https://www.rosehomeslv.com/blog/[slug-3]">[Title of Related Post 3]</a></p>

<hr/>

<p>[Direct answer paragraph, front-loaded value, includes neighborhood name]</p>

<h2>[Section Heading]</h2>

<p>[Content paragraph...]</p>

<h2>Local Expert Insight</h2>

<p>[Ryan Rose perspective paragraph...]</p>

<h2>[CTA Heading]</h2>

<p>[Soft call to action, 1 to 2 sentences]</p>

<script type="application/ld+json">
{ ... schema markup ... }
</script>
```

### CRITICAL FORMAT RULES
1. **NO H1 tag in body content** — the CMS renders the blog title as H1 automatically
2. **Explore More section** uses `<h2>Explore More Las Vegas Communities</h2>` as header
3. **Each related link** is wrapped in its own `<p>` tag with an `<a>` tag inside
4. **Links use /blog/ NOT /blogs/** in the URL path
5. **`<hr/>` separator** between the Explore More links and the body content
6. **No links anywhere below the `<hr/>`** — only in the Explore More section at top
7. **Schema markup** goes at the very bottom inside `<script type="application/ld+json">`

## Content Rules
- 400 to 600 words per post
- ONE specific topic per post
- NEVER use emdashes or dashes in content
- No FAQ sections
- No bullet points in main content unless listing specific amenities
- All facts must be 100% verifiable
- Crime/safety statistics MUST include source links (e.g., SafeWise, BestPlaces, NeighborhoodScout, AreaVibes)
- All data should reference 2025/2026 sources where available
- Conversational but professional tone
- Active voice preferred
- Short paragraphs (3 to 4 sentences max)

## SEO Package (per batch)
Each batch of posts gets one SEO file containing per post:
- **SEO Title:** Max 60 characters
- **Meta Description:** Max 150 characters
- **Keywords:** Max 500 characters total (including all spaces and commas; aim to fill but MUST stay under 500)
- **Slug:** Lowercase, hyphens, under 60 characters
- **AI Image Prompt:** Detailed description for Gemini/nanobanana

## Schema Markup Template
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
  "datePublished": "[PUBLISH DATE]",
  "dateModified": "[PUBLISH DATE]",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://www.rosehomeslv.com/blog/[SLUG]"
  },
  "about": {
    "@type": "Place",
    "name": "[NEIGHBORHOOD NAME]",
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "Henderson",
      "addressRegion": "NV",
      "addressCountry": "US"
    }
  },
  "keywords": "[KEYWORDS — must be under 500 characters total]"
}
```

## Batch Workflow
- 5 posts per batch
- Research PAA, autocomplete, related searches first
- Create master topic list
- Prioritize most searched/valuable topics
- Verify all facts via web research
- Deliver blog HTML files + SEO package document
- Continue with next batch on "ready" signal

## Related Blogs Selection Priority
1. Same neighborhood, different topic
2. Same topic, different neighborhood
3. Geographically adjacent neighborhoods

## Source Data
All research data is compiled in the markdown file: `compass_artifact_wf-bd5b5760-5c3f-4a89-859f-00f20768a3d7_text_markdown.md`

## Completed Posts
- Post 1: What Is Seven Hills Henderson (seven-hills-henderson)
