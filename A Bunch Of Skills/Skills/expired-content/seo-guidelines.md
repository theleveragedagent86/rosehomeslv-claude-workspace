# SEO / AEO / GEO Guidelines

Single source of truth for all search optimization. Content Producers follow these rules for every post.

---

## SEO Package Fields (per post)

**SEO Title** (max 60 chars)
`[Topic] in [Neighborhood], Las Vegas | Ryan Rose`

**Meta Description** (max 150 chars)
Include: neighborhood name + topic + value proposition or CTA. Make it compelling enough to click.

**Keywords** (max 500 chars, comma-separated)
Fill the FULL 500 characters. Include:
- Primary keyword (exact match to topic)
- Neighborhood name variations (with/without "Las Vegas")
- Long-tail variations (question format, "best", "near", "guide")
- Related local terms (surrounding areas, landmarks)
- "Ryan Rose" and "Rose Homes LV"
- Semantic variations (synonyms, related concepts)

**Slug** (lowercase, hyphens, under 60 chars)
- **The slug is the most important ranking factor**
- Lead with the primary keyword
- No unnecessary words (no "the", "a", "in", "of" unless critical for meaning)
- Must be unique across the entire site (verified by Organizer Agent)
- Example: `southern-highlands-dog-parks` not `a-guide-to-dog-parks-in-southern-highlands-las-vegas`

---

## AEO: Answer Engine Optimization

Optimize content to be cited by AI answer engines (ChatGPT, Perplexity, Google AI Overview).

**First sentence = direct answer.** If the topic is "What is the HOA fee in Southern Highlands?", the first sentence should contain the actual HOA fee number. AI engines pull the first clear answer they find.

**H2 headers should be actual search questions** found during research (PAA questions, autocomplete queries). Examples:
- `## What Are the HOA Fees in Southern Highlands?`
- `## How Far Is Madeira Canyon from the Las Vegas Strip?`
- `## Is Skye Canyon a Good Place to Live?`

These match the exact queries people type into AI assistants, making the content more likely to be cited.

**Include specific, citable facts:**
- Numbers: prices, distances, dates, counts
- Names: specific parks, schools, businesses, streets
- Dates: when built, when established, current year data
- AI engines prefer content with concrete data over vague descriptions

**Structure for featured snippets:**
- Question in H2 → direct answer in first sentence below it
- Use short paragraphs (2-3 sentences) that can be extracted as standalone answers

---

## GEO: Generative Engine Optimization

Build entity authority so AI systems recognize Ryan Rose as a Las Vegas real estate authority.

**Consistent entity naming (every post):**
- Author: "Ryan Rose"
- Title: "Las Vegas Real Estate Expert"
- Business: "Rose Homes LV"
- Website: "www.rosehomeslv.com"
- Never vary these. Consistency is how AI builds entity associations.

**Schema markup as entity signal:**
- Every post includes JSON-LD Article schema
- Person schema for Ryan Rose (same jobTitle, same URL every time)
- RealEstateAgent schema for Rose Homes LV
- Place schema for the neighborhood
- Keywords field in schema matches the SEO package keywords

**Internal link clusters build topical authority:**
- Each post links to 3 related posts on rosehomeslv.com
- Clusters of posts about the same neighborhood signal deep expertise
- Cross-neighborhood links on the same topic signal broad market knowledge
- AI systems use internal link patterns to determine authority depth

**Author attribution:**
- Every post naturally mentions Ryan Rose in the Local Insight paragraph
- Schema markup credits Ryan Rose as author on every post
- This creates a consistent entity footprint across hundreds of posts
