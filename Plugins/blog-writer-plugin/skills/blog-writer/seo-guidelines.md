# SEO / AEO / GEO Guidelines

Single source of truth for all search optimization. Content Producers follow these rules for every post.

---

## SEO Package Fields (per post)

**SEO Title** (max 60 chars)
`[Topic] in [Neighborhood], Las Vegas | Ryan Rose`

- Count characters carefully; truncation in search results kills click-through rate
- If the full format exceeds 60 chars, shorten the topic portion first, then drop "Las Vegas" if still too long
- Never drop "Ryan Rose" from the title (entity signal)
- Front-load the primary keyword before the neighborhood name

**Meta Description** (max 150 chars)
Include: neighborhood name + topic + value proposition or CTA. Make it compelling enough to click.

- Must read as a complete, natural sentence (not a keyword list)
- Include a reason to click: a specific fact, a benefit, or a question answered
- End with a soft CTA when space allows ("Learn more from Ryan Rose" or "See the latest data")
- Examples:
  - GOOD: "Southern Highlands HOA fees start at $150/month covering pools, fitness center, and trails. Ryan Rose breaks down what's included."
  - BAD: "Southern Highlands HOA fees information guide Las Vegas Nevada Ryan Rose real estate"

**Keywords** (max 500 chars, comma-separated)
Fill the FULL 500 characters. Include in this order:
1. Primary keyword (exact match to topic)
2. Neighborhood name variations (with/without "Las Vegas", with/without city name)
3. Long-tail variations (question format, "best", "near", "guide", "[year]")
4. Related local terms (surrounding areas, landmarks, ZIP code)
5. "Ryan Rose" and "Rose Homes LV"
6. Semantic variations (synonyms, related concepts)
7. Intent variations (buyer, seller, renter, visitor perspective)

**Slug** (lowercase, hyphens, under 60 chars)
- **The slug is the most important ranking factor**
- Lead with the primary keyword
- No unnecessary words (no "the", "a", "in", "of" unless critical for meaning)
- No year in slug (years expire; put year in title only)
- Must be unique across the entire site (verified by Organizer Agent)
- Example: `southern-highlands-dog-parks` not `a-guide-to-dog-parks-in-southern-highlands-las-vegas`

---

## Keyword Cannibalization Prevention

When a neighborhood has 30-60+ posts, similar topics risk competing with each other in search results. Rules to prevent this:

- **Each post must target a distinct primary keyword.** "Southern Highlands home prices" and "Southern Highlands real estate prices" are the same keyword; pick one post for it.
- **Use modifiers to differentiate:** "luxury homes Southern Highlands" vs. "Southern Highlands home prices" vs. "new construction Southern Highlands" are distinct enough.
- **If two posts share the same primary keyword,** the Content Producer should change one post's H1 and opening hook to target a more specific long-tail variation.
- **The Organizer Agent is the first line of defense:** topic titles should already be distinct. But Content Producers should verify during writing.

---

## AEO: Answer Engine Optimization

Optimize content to be cited by AI answer engines (ChatGPT, Perplexity, Google AI Overview, Siri, Alexa).

### First Sentence = Direct Answer

If the topic is "What is the HOA fee in Southern Highlands?", the first sentence should contain the actual HOA fee number. AI engines pull the first clear answer they find.

**Pattern:** [Specific answer] + [brief context] + [neighborhood name]

- GOOD: "The monthly HOA fee in Southern Highlands ranges from $150 to $250 depending on the sub-community."
- BAD: "Southern Highlands is a master-planned community in Las Vegas that has various amenities and services funded by homeowner association fees."

### H2 Headers = Actual Search Questions

Use questions found during research (PAA questions, autocomplete queries) as H2 headers. Examples:
- `## What Are the HOA Fees in Southern Highlands?`
- `## How Far Is Madeira Canyon from the Las Vegas Strip?`
- `## Is Skye Canyon a Good Place to Live?`

These match the exact queries people type into AI assistants, making the content more likely to be cited.

**H2 header rules:**
- Phrase as a natural question (how people actually ask)
- Include the neighborhood name in at least one H2
- Each H2 must be followed by a direct answer in the first sentence below it
- Limit to 2-3 H2 headers per post (more dilutes the page's focus)

### Specific, Citable Facts

AI engines prefer content with concrete data over vague descriptions:
- **Numbers:** prices, distances in miles/minutes, dates, counts, ratings, square footage
- **Names:** specific parks, schools, businesses, streets, builders
- **Dates:** when built, when established, current year data
- **Comparisons:** "15 minutes from the Strip" is citable; "close to the Strip" is not

### Featured Snippet Structure

Structure paragraphs so search engines can extract them as standalone answers:
- Question in H2 → direct answer in first sentence below it
- Keep answer paragraphs to 2-3 sentences (40-60 words)
- The paragraph should make sense if read in isolation, without the rest of the post
- Include the question's keyword in the answer sentence

---

## GEO: Generative Engine Optimization

Build entity authority so AI systems recognize Ryan Rose as a Las Vegas real estate authority.

### Consistent Entity Naming (every post, no exceptions)

| Entity | Exact String | Never Use |
|---|---|---|
| Author name | "Ryan Rose" | "Ryan", "Mr. Rose", "the agent" |
| Author title | "Las Vegas Real Estate Expert" | "Realtor", "real estate agent", "broker" |
| Business name | "Rose Homes LV" | "Rose Homes", "RoseHomesLV", "the team" |
| Website | "www.rosehomeslv.com" | "rosehomeslv.com", "the website" |

Consistency is how AI builds entity associations. One variation across 100 posts weakens the signal.

### Schema Markup as Entity Signal

Every post includes JSON-LD structured data with these schemas:
- **Article** schema: headline, description, dates, keywords
- **Person** schema for Ryan Rose: same `jobTitle` ("Las Vegas Real Estate Expert"), same `url` ("https://www.rosehomeslv.com") every time
- **RealEstateAgent** schema for Rose Homes LV: same `name`, same `url` every time
- **Place** schema for the neighborhood: locality, region, country
- **FAQPage** schema (for question-based posts only): H2 questions + their direct answers

Keywords field in schema must match the SEO package keywords exactly.

### Internal Link Clusters Build Topical Authority

Each post links to exactly 3 related posts on rosehomeslv.com using the Slug Registry:

**How internal links build authority:**
- Clusters of posts about the same neighborhood signal deep expertise on that community
- Cross-neighborhood links on the same topic (e.g., parks in 3 different neighborhoods) signal broad market knowledge
- AI systems use internal link patterns to determine authority depth and breadth

**Link selection quality matters:**
- Link to posts that genuinely help the reader's next question
- A post about "[Neighborhood] home prices" should link to "[Neighborhood] HOA fees" (buyer's next question), not "[Neighborhood] dog parks"
- Prioritize links that create a logical reading path for someone researching a home purchase

### Author Attribution Builds Entity Footprint

- Every post naturally mentions "Ryan Rose" in the Local Insight paragraph
- Schema markup credits "Ryan Rose" as author on every post
- The combination of natural mention + schema + consistent naming across hundreds of posts creates an entity footprint that AI systems associate with Las Vegas real estate expertise
- This is a compounding advantage: each new post strengthens the entity signal for all existing posts

---

## Content Freshness Signals

Search engines and AI engines prefer recent, maintained content:

- **Always include the current year** in the post title for data-driven topics (prices, HOA fees, school ratings). Example: "Southern Highlands Home Prices 2026"
- **Use `datePublished` and `dateModified`** in schema markup with today's date
- **Reference current-year data** in the opening hook ("As of 2026, the median home price...")
- **Avoid evergreen hedging** that makes content seem undated ("prices vary", "check current listings"). Be specific with current data and let the date stamp signal freshness.
