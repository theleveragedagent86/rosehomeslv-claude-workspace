---
name: publish-blogs
description: Use when someone asks to post, publish, or upload blog posts to Lofty, the Lofty CMS, or the Rose Homes LV website. Formats content and provides a step-by-step publishing checklist.
argument-hint: [optional: file path to .html or .md file]
---

## What This Skill Does

Prepares blog post content for publishing to the Lofty CMS web dashboard and outputs a step-by-step checklist with all content ready to copy-paste into each field. Works with blog content already in the conversation (e.g., from the blog-writer skill) or from a file path passed as an argument.

**Website:** www.rosehomeslv.com
**Blog Index:** www.rosehomeslv.com/blogs

---

## Step 1: Gather Content

**If `$ARGUMENTS` is provided:** Read the file at that path.

**If no argument:** Use the blog post content already in the conversation. If multiple posts are present (e.g., a batch from blog-writer), ask: "Publish all posts in this batch, or just one? If one, which?"

---

## Step 2: Prepare Each Post

For each post being published, extract and prepare the following:

### A. Title
- Extract the H1 heading from the content
- This is entered in the **Title** field in Lofty (NOT included in the HTML body)

### B. HTML Body
- If content is Markdown: convert to clean HTML
- Remove the H1 title tag (it goes in the Title field separately)
- Remove any JSON-LD `<script type="application/ld+json">` block (Lofty handles schema separately)
- Keep: paragraphs as `<p>` tags, H2/H3 headers, links, any formatting
- The related blogs section should use `<p>` tags with `<a href="">` links

**Markdown to HTML conversion rules:**
- `# Heading` → omit (it's the title)
- `## Heading` → `<h2>Heading</h2>`
- `### Heading` → `<h3>Heading</h3>`
- Regular paragraph → `<p>text</p>`
- `**bold**` → `<strong>bold</strong>`
- `[text](url)` → `<a href="url">text</a>`
- Blank lines between paragraphs → separate `<p>` tags

### C. SEO Data
Look for the SEO package in the conversation (from blog-writer output). Extract:
- **Meta Title** (max 60 chars)
- **Meta Keywords** (up to 500 chars)
- **Meta Description** (max 150 chars)
- **Slug** (lowercase, hyphens, under 60 chars)
- **Category** (the neighborhood/community name, e.g., "Southern Highlands", "Summerlin")

If any SEO data is missing, ask the user to provide it before continuing.

---

## Step 3: Output the Publishing Checklist

For each post, output a clearly formatted checklist. Use this exact format:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PUBLISH: [Post Title]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[ ] 1. Click "+ Add New" to create a new blog post

[ ] 2. TITLE FIELD — paste:
[exact title text]

[ ] 3. SOURCE CODE HTML — click the </> icon, then paste:
[full HTML body — no H1, no JSON-LD]

[ ] 4. Click SAVE in the source code modal

[ ] 5. Click the SETTINGS tab, then set:
    • URL Slug: [slug]
    • Category: [neighborhood name]

[ ] 6. Click the SEO tab, then for each field:
    (Use Ctrl+A to select all text before typing/pasting)

    • Meta Title — paste:
    [meta title]

    • Meta Keywords — paste:
    [keywords]

    • Meta Description — paste:
    [meta description]

[ ] 7. Click POST NOW to publish

[ ] 8. If a confirmation dialog appears, click OK

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Step 4: Slug Conflict Handling

After outputting the checklist, always include this note:

> **If nothing happens when you click Post Now:** The URL slug already exists.
> Append `1` to the end of the slug (e.g., `southern-highlands-parks` → `southern-highlands-parks-1`) and try again.
> If it still fails, try `2`, then `3`, and so on.

---

## Step 5: Multiple Posts

If publishing a batch of multiple posts:
- Output the checklist for Post 1 first
- After the checklist, ask: "Ready for Post 2?"
- Continue one at a time until all posts are published
- Track which posts have been published in the conversation

---

## Notes

- Always use Ctrl+A before pasting into Lofty's SEO fields to clear default variables
- The HTML body must NOT contain the `<h1>` title tag — Lofty adds this from the Title field
- The HTML body must NOT contain `<script type="application/ld+json">` blocks
- Category = the neighborhood/community name (e.g., "Summerlin", "Henderson", "Green Valley")
- If the user has the blog-writer SEO package in context, pull all SEO data from there automatically
