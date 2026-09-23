# Content guide: writing an area page (geo spoke)

You write ONE file: `geo-spokes/<area>/content.json`. You never write HTML pages. The build
script turns content.json into the two Lofty embeds, the preview, and the SEO sheet:

    python3 "/Users/ryanrose/Downloads/Claude/Rose Homes LV/Content/New-Construction/geo-spokes/_build/build.py" <area>

Run it until it prints `OK, no validation errors`. It fails on em-dashes, unknown builder
keys, duplicate ids, broken anchors, over-length SEO fields, and leftover NOT FOUND.

**The reference implementation is `geo-spokes/summerlin/content.json`.** Match its structure,
section order, tone, and density. Read it fully before you start.

## Inputs
- `geo-spokes/<area>/research.md`: your ONLY source of facts. If a fact is not in it, it
  does not go on the page. If research says NOT FOUND, cut the claim, do not soften it into a
  guess ("around", "roughly" on an unsourced number is still a guess).
- `geo-spokes/_build/live-sitemap-2026-09-16.json`: the live rosehomeslv.com URLs. Internal
  blog links must be `/blog/<slug>` where `<slug>` appears in this file's area lists. Never
  link a blog slug that is not in this file. 2 to 5 blog links total, placed where they help.
- Hub copy for tone: `new-construction-hub/part-2-below-listings.html`.

## Voice (Ryan Rose, Rose Homes LV)
- 6th-grade reading level. Short sentences. Plain words. Professional but warm.
- No em-dashes or en-dashes. Use commas, periods, "and", or "to" for ranges ("$500,000s to $600,000s").
- No "premier", "exclusive", "nestled", "boasts", "stunning", "vibrant", "whether you're".
- Factual only. Every price in a table carries its source date in the table note.
- Soft CTAs. Invite, don't push.
- Clark County, Nevada only.
- Write prices the way the source publishes them ("from the high $600,000s").

## Schema

```jsonc
{
  "area": "Summerlin",                        // display name
  "slug": "summerlin-new-construction",       // MUST match the hub link exactly
  "place_name": "Summerlin, Las Vegas, Nevada",
  "locality": "Las Vegas",                    // Las Vegas | Henderson | North Las Vegas
  "updated_iso": "2026-09-16", "updated_text": "September 16, 2026",
  "reviewed_text": "September 2026",
  "read_minutes": 12,                         // ~220 words per minute of body copy
  "seo": {
    "title": "...",        // <= 48 chars. Lead with "<Area> New Construction Homes" or close.
    "description": "...",  // 140-160 chars, a real hook, one concrete fact
    "keywords": "...",     // <= 100 chars, comma separated
    "og_title": "...", "og_description": "..."   // optional
  },
  "hero": {
    "kicker": "Rose Homes LV &middot; <short location>",   // keep SHORT, <= ~45 chars (hero layout)
    "h1": "New Construction Homes in <Area>",
    "sub": "...",                              // 1-2 sentences
    "stats": [["12", "Neighborhoods selling"], ...],   // exactly 4, each sourced in research
    "image": {"src": "...", "alt": "...", "width": 900, "height": 672},
    "secondary_cta": "Browse neighborhoods",   // label of the 2nd hero button (goes to 1st section)
    "mobile_label": "Neighborhoods"            // short label for the mobile bar
  },
  "answer": "...",        // 90-130 words. Direct answer: what, where, who builds, price span, the one tip.
  "takeaways": ["...", ...],   // 5 or 6, specific to THIS area
  "part1_sections": [ SECTION, SECTION ],     // exactly 2: neighborhoods table, then builders
  "listings": {
    "h2": "New construction homes for sale in <Area> right now",
    "lede": "...",
    "lofty_filter": "..."   // exact instructions for Ryan: area/city/ZIP/subdivision + Year Built >= 2025
  },
  "part2_sections": [ SECTION, ... ],         // 5 to 7, see order below
  "faq": [["question?", "answer"], ...],       // 6 to 8. Answers 2-3 sentences, may contain <a>
  "cta": {"h2": "...", "p": "..."},
  "sources": [["Label", "https://..."], ...]   // every external source used on the page
}
```

SECTION = `{"id": "kebab-id", "toc": "Short rail label", "h2": "Question-style heading?", "blocks": [BLOCK, ...]}`

BLOCK is a one-key object:
- `{"lede": "html"}` first paragraph of a section, larger type
- `{"p": "html"}` paragraph. Inline `<a>`, `<strong>`, `<em>` allowed.
- `{"h3": "text"}`
- `{"ul": ["html", ...]}` / `{"ol": [...]}`
- `{"facts": [["Label", "html"], ...]}` the grey fact box (like the hub's area boxes)
- `{"table": {"head": [...], "rows": [[...], ...], "note": "html"}}`
- `{"builders": {"cards": [{"key": "toll-brothers", "note": "area-specific note"}], "note": "html"}}`
  Valid keys: beazer, blue-heron, century-communities, christopher, dr-horton, harmony, kb-home,
  lennar, lgi, meritage, pulte-del-webb, richmond-american, shea, signature, storybook,
  taylor-morrison, toll-brothers, touchstone, tri-pointe, woodside.
  Card notes say what that builder is doing IN THIS AREA (neighborhood names, product, price).
  A builder active in the area but not in that list goes in the section's note text instead.
- `{"pills": [["Label", "/href"], ...]}`
- `{"note": "html"}` small grey note

## Section order

part1_sections:
1. `neighborhoods`: "Which new neighborhoods are selling in <Area> right now?" lede, table
   (Neighborhood | Builder | Village or master plan | Home type | Size | Starts from), note with
   the as-of date and "prices change with every release".
2. `builders`: "Which builders are building in <Area>?" lede, builders cards, note.

part2_sections (skip one only if research has nothing solid for it):
3. `where`: where in the area building is happening (facts boxes per village/master plan)
4. `prices`: what it costs and what drives the spread
5. `monthly-costs`: HOA, SID/LID, property tax (Nevada 3% cap on primary residence increases)
6. `schools`: CCSD zoned schools table, with "confirm with CCSD zoning, boundaries change"
7. `location`: commute and what's nearby
8. `watch-outs`: what to know before buying new here (ul)
9. `your-agent`: why bring your own agent to a model home in this area. Short, 2 paragraphs, link
   `/las-vegas-new-construction#why-ryan`.

Ids must not collide with: listings, faq, other-areas, sources, contact, answer, guide, guide-2.

## Done means
- build prints OK
- every number traces to research.md
- no claim that research marked NOT FOUND
- 2-5 internal blog links, all present in the live sitemap file
- report back: word count of body copy, number of neighborhoods in the table, anything in
  research you left out and why
