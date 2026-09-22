---
name: blog-writer
description: Use when someone asks to create blog posts, write a blog post, generate real estate content, write about a Las Vegas neighborhood or community, or create content for Rose Homes LV.
argument-hint: [neighborhood or community name]
---

## What This Skill Does

Creates SEO-optimized blog posts about Las Vegas area residential real estate communities and neighborhoods. Builds topical authority for Ryan Rose as the premier Las Vegas real estate expert. Content is optimized for both traditional Google search and AI/LLM platforms (ChatGPT, Perplexity, Google AI Overview).

**Website:** www.rosehomeslv.com
**Blog Index:** www.rosehomeslv.com/blogs
**Expert/Author:** Ryan Rose, Las Vegas Real Estate Expert

For post structure templates, SEO package format, and schema markup, see [templates.md](templates.md).
For formatting rules and content verification requirements, see [content-rules.md](content-rules.md).

---

## Workflow

When given a neighborhood or community name (from `$ARGUMENTS` or conversation), run the full batch workflow below.

### Step 1: Comprehensive Research

Search for real, current information about the neighborhood using web search:

- Search `"[Neighborhood] Las Vegas"` and capture all "People Also Ask" questions
- Search `"[Neighborhood] real estate"`, `"[Neighborhood] homes"`, `"[Neighborhood] living"`
- Note Google autocomplete suggestions for the neighborhood name
- Note "Related Searches" at bottom of results
- Find the official community/HOA website
- Identify all parks, schools, restaurants, shopping centers, and attractions in or near the area

### Step 2: Build Master Topic List

Compile ALL potential blog topics. Present this list to the user before writing. Each item below = a separate blog post:

- Each "People Also Ask" question that could stand alone
- Each individual park (one post per park)
- Each individual school (one post per school)
- Each notable restaurant or restaurant category
- Each shopping center or retail area
- Each attraction or point of interest
- Real estate angles: market overview, home styles, prices, investment potential, new construction
- Lifestyle angles: commute times, safety/crime stats, demographics, community vibe, pet-friendly, retiree-friendly
- Community features: HOA info, golf memberships, trails, specific streets or sub-neighborhoods
- Specific "is/what/how/where" questions about the area

**Present the master list with a count** (e.g., "47 potential blog posts identified") and ask the user if they want to proceed with Batch 1 or adjust priorities.

### Step 3: Write Batch of 5 Blog Posts

Select the 5 most valuable topics (prioritize highest search intent) and write each post following this structure:

1. **Opening Hook** (1-2 sentences): Directly answer what the reader wants to know. Include the neighborhood name. Establish relevance immediately.
2. **Core Content** (3-4 paragraphs): Factual, verifiable information only. Include specific details (numbers, names, locations). Naturally mention Ryan Rose as the local expert. Use H2 subheadings if needed.
3. **Local Insight** (1 paragraph): Ryan Rose's perspective or recommendation. Something only a local expert would know. Personal touch that builds trust.
4. **Call to Action** (1-2 sentences): Soft invitation to connect with Ryan Rose. Not pushy or salesy.
5. **Related Blogs Section**: Header + 3 internal links (see [templates.md](templates.md) for format and link selection strategy).
6. **Schema Markup**: JSON-LD block at end of post (see [templates.md](templates.md) for template).

**Content rules:** 400-600 words per post. One specific topic per post. No filler. See [content-rules.md](content-rules.md) for all formatting rules.

### Step 4: Create SEO Package Document

After writing all 5 posts, create a single SEO package document containing, for each post:

- SEO Title (max 60 chars): `[Topic] in [Neighborhood], Las Vegas | Ryan Rose`
- Meta Description (max 150 chars): neighborhood + topic + CTA
- Keywords (max 500 chars, comma-separated, fill the full 500 chars)
- Slug (lowercase, hyphens, under 60 chars): `neighborhood-name-topic`
- AI Image Prompt (for Gemini/Nanobanana): photorealistic description with location, style, mood, Las Vegas/neighborhood characteristics

### Step 5: Deliver and Continue

- Present all 5 blog posts
- Present the SEO package document
- List remaining topics from the master topic list
- Ask: "Ready for Batch 2?"
- Continue in batches of 5 until the user stops or all topics are exhausted

---

## Core Principles

- **The slug is the most important ranking factor.** Keep it concise and keyword-focused.
- **Answer first.** Put the most important information at the very start. Never bury the lead.
- **One blog, one specific topic.** "Dog Parks in Southern Highlands" not "Parks in Southern Highlands."
- **No filler.** Every sentence must serve the reader.
- **Facts only.** All information must be verifiable from official or reputable sources.
- **Unlimited posts per community.** A single neighborhood can have 50-100+ posts.
- **Internal linking.** Every post includes 3 related blog links.
- **Ryan Rose positioning.** Naturally woven in as local expert, never forced or salesy.
