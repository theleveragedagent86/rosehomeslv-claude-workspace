# Transcript and Output Templates — Local News

Templates for video transcripts, Instagram captions, YouTube descriptions, blog structure, and Reddit posts. All agents reference these for consistent formatting.

---

## Video Transcript Templates

### 10-Second Script (25-35 words)

```
[HOOK: Surprising fact or quick question, 1 sentence]
[KEY DETAIL: The one thing people need to know, 1 sentence]
[COMMENT QUESTION: Thought-provoking opinion question tied to the story, 1 sentence]
```

CTA: End with the comment question only. No mid-video CTA, no share prompt. Not enough time.

### 20-Second Script (50-65 words)

```
[HOOK: Attention-grabbing opening, 1 sentence]
[CONTEXT: What happened and where, 1-2 sentences]
[MID-CTA: "Follow for more local news like this" or similar, 1 short sentence]
[PAYOFF: The detail people will remember, 1 sentence]
[SHARE + COMMENT: "Send this to someone in [area]" + thought-provoking question, 2 sentences]
```

### 30-Second Script (75-90 words)

```
[HOOK: Strong opening question or surprising statement, 1 sentence]
[SETUP: Background context, 2 sentences]
[MID-CTA: "Hit follow so you don't miss what's happening in Vegas" or similar, 1 short sentence]
[DEVELOPMENT: Key details and what it means for locals, 2-3 sentences]
[SHARE: "Share this with someone who needs to see this" or similar, 1 sentence]
[COMMENT QUESTION: Specific opinion-driving question tied to the story, 1 sentence]
```

### Mid-Video CTA Examples (pick one, vary across stories)
- "Follow for more local news like this."
- "Hit follow so you don't miss what's happening in Vegas."
- "Follow me for the local stories that actually matter."
- "If you live in Vegas, you should be following for stuff like this."

### Share CTA Examples (pick one, vary across stories)
- "Send this to someone in [specific area] who needs to see this."
- "Share this with anyone thinking about living in Vegas."
- "Tag someone who would have an opinion on this."
- "Send this to a friend in [Henderson/Summerlin/etc.]."

### Comment Question Examples (must be specific to the story)
- "Do you think parents should be held responsible for their kids' actions on e-bikes? Let me know in the comments."
- "Would you eat at a restaurant inside a gas station? Drop your take below."
- "Should CCSD be spending money on this when teachers are underpaid? Comment what you think."
- "Is this development good for the neighborhood or is it going to cause more traffic? What do you think?"
- "Would you pay $15 for a burger at this new spot? Tell me in the comments."

---

## Instagram Caption Template

```
[HOOK LINE — first line visible before "...more". Attention-grabbing, 1 sentence. Emoji optional.]

[BODY — 2-3 sentences. Key facts from the story. Why it matters to locals.]

[CTA — soft engagement. "Tag someone who needs to know" or "Drop a [emoji] if you agree" or similar.]

#LasVegas #VegasNews #ClarkCounty #LasVegasRealEstate #VegasLocal [3-5 story-specific hashtags]
```

---

## YouTube Shorts Description Template

```
[TITLE LINE — matches or closely mirrors the video hook]

[2-3 sentence summary of the story and why it matters to Las Vegas residents.]

Follow for more Las Vegas news you need to know.

Ryan Rose | Real Broker, LLC | 702-747-5921
rosehomeslv.com
```

---

## Blog Post HTML Template

```html
<article>
  <h1>[Blog Title]</h1>
  <!-- NO dateline or byline. Content starts immediately after H1. -->
  <p>[Opening: directly answer the topic in 1-2 sentences. Key fact first.]</p>
  <p>[1-2 more sentences expanding context.]</p>

  <img src="[direct URL]" alt="[descriptive alt text]" />

  <h2>[What Happened]</h2>
  <p>[3-4 paragraphs with facts, names, dates, locations]</p>

  <img src="[direct URL]" alt="[descriptive alt text]" />

  <h2>[Why It Matters to Las Vegas Residents]</h2>
  <p>[3-4 paragraphs on local impact]</p>

  <h2>[Background and History]</h2>
  <p>[3-4 paragraphs of deeper context]</p>

  <img src="[direct URL]" alt="[descriptive alt text]" />

  <h2>[What Happens Next]</h2>
  <p>[2-3 paragraphs on implications and timeline]</p>

  <h2>[Ryan's Take]</h2>
  <p>[1-2 paragraphs, local expert perspective]</p>

  <img src="[direct URL]" alt="[descriptive alt text]" />

  <h2>[What You Can Do]</h2>
  <p>[2-3 paragraphs, actionable info for residents]</p>

  <p>Have questions about how this affects your home or neighborhood? <a href="https://www.rosehomeslv.com/contact">Reach out to Ryan Rose</a> or text/call <a href="tel:7027475921">702-747-5921</a> anytime.</p>

  <h2>Sources</h2>
  <p><a href="[URL]">[Publication Name]</a></p>

  <h2>Related Stories</h2>
  <p><a href="https://www.rosehomeslv.com/blog/[slug]">[Title]</a></p>
  <p><a href="https://www.rosehomeslv.com/blog/[slug]">[Title]</a></p>
  <p><a href="https://www.rosehomeslv.com/blog/[slug]">[Title]</a></p>
</article>
```

### NewsArticle Schema Template

```json
{
  "@context": "https://schema.org",
  "@type": "NewsArticle",
  "headline": "[Blog Title]",
  "description": "[Meta Description, max 150 chars]",
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
  "datePublished": "[YYYY-MM-DD]",
  "dateModified": "[YYYY-MM-DD]",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://www.rosehomeslv.com/blog/[slug]"
  },
  "about": {
    "@type": "Place",
    "name": "[Area within Clark County]",
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "[City]",
      "addressRegion": "NV",
      "addressCountry": "US"
    }
  },
  "keywords": "[Full keyword string, max 500 chars]"
}
```

---

## Reddit Post Template

```
Title: [Local News] [Conversational headline]

Body:
[Lead with the most interesting detail, 1-2 sentences]

[Context and key facts, 1-2 paragraphs]

[Why it matters to locals, 1 paragraph]

I made a quick video on this one too, check my profile if you want the visual breakdown.

Full story with more details: https://www.rosehomeslv.com/blog/[slug]

[Engagement question to close]
```

Flair mapping:
- Government/Development stories: "Educational" or "Market Data"
- Restaurant/Business stories: "Neighborhood Guide"
- School Board stories: "Educational"

---

## Spreadsheet Format

| # | Category | County/Area | Headline | Story Summary | Source | URL | Date | Viral Potential | Blog Slug | Video Length |
|---|----------|-------------|----------|---------------|--------|-----|------|-----------------|-----------|-------------|

Viral Potential values: Red (highest), Orange (high), Yellow (medium), Green (lower)
