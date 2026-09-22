# /reddit-posts -- Complete Weekly Posting Skill for r/VegasRealtor

Generate a weekly batch of 21 Reddit posts for r/VegasRealtor (3 posts per day, 7 days), run QA against source blogs, update the tracker, and update memory files.

---

## Trigger Phrases

"reddit posts", "next list of posts", "next week's posts", "weekly posts", "give me the next batch", "run /reddit-posts"

---

## Identity

- **Name:** Ryan Rose
- **Business:** Rose Homes LV (Las Vegas real estate)
- **Reddit Account:** u/Silver_Artichoke_812 (display name: "Ryan Rose with Rose Homes LV")
- **Subreddit:** r/VegasRealtor (owned/moderated by Ryan)
- **Posting method:** Ryan posts manually from the batch file. No automation scripts are in use.

---

## Overview

Each weekly batch produces exactly 21 posts: 3 posts per day for 7 consecutive days.

| Time | Post Type | Source |
|------|-----------|--------|
| 10:00 AM | Content calendar post | Original content (topic rotates by day of week) |
| 1:00 PM | Blog repurpose post | From the Claude Blogs library |
| 4:00 PM | Blog repurpose post | From the Claude Blogs library |

That means each week has **7 content calendar posts** and **14 blog repurpose posts**.

---

## Step-by-Step Workflow

### Step 1: Determine the Next Week

Read the tracker at `/Reddit/repurposed-blogs.md` and find the last date entry. The next batch starts the day after the last batch ended. The week always runs 7 consecutive days regardless of which day of the week it starts on.

### Step 2: Determine Which Blog Directories Come Next

Read the "Already-Used Blog Files" section at the bottom of this document (or the live tracker) to find where the rotation left off. Each week uses 14 blog repurpose slots. Continue from where the last batch stopped, cycling through the 41 directories in order. When you reach directory 41, loop back to directory 1 and advance to the next post round.

### Step 3: Find the Correct Blog File for Each Directory

Blog files live in: `/Claude/Claude Blogs/<DIRECTORY_NAME>/`

To find the next unused file from a directory:
1. Check the "Already-Used Blog Files" list below (and the live tracker) for all files already used from that directory
2. List the HTML files in the directory (ignore `.md` files like `master-topic-list.md` and `seo-package-*.md`)
3. The next unused HTML file is your target

**File naming is inconsistent across directories.** Files may be named `post1-`, `post2-`, `01-`, `02-`, `03-`, `batch1-post1-`, or other patterns. Do NOT rely on filename numbering to determine order. Track usage by exact filename in the tracker.

### Step 4: Extract the Canonical URL from Each Blog File

Search each HTML blog file for the canonical URL. Look for:
- `@id` field in JSON-LD schema: `"@id": "https://www.rosehomeslv.com/blog/slug-here"`
- Or `<link rel="canonical">` tag
- Or links with `rosehomeslv.com/blog/` pattern

**IMPORTANT:** The correct URL pattern is `/blog/<slug>` (singular). The plural `/blogs/` pattern 404s on the live site. Always verify the URL format from the source file.

### Step 5: Read Each Blog File and Extract Key Data

For every blog repurpose post, read the ENTIRE source HTML file. Extract ALL data points:
- Prices, price ranges, medians
- Square footage, lot sizes
- HOA fees, SID/LID taxes
- School names and ratings
- Crime scores and safety rankings
- Distances and commute times
- Builder names, home counts
- Amenity details (parks, pools, rec centers, trails)
- Any other specific numbers or facts

You need these for writing AND for QA verification.

### Step 6: Write All 21 Posts

Write posts following the exact format and rules specified below.

### Step 7: Run QA Verification

For every blog repurpose post, cross-reference EVERY data point in your written post against the source blog data you extracted in Step 5. Check for:
- Incorrect numbers (prices, square footage, lot sizes, fees, distances, ratings)
- Misattributed facts (wrong school name, wrong builder, wrong management company)
- Inflated or unsupported statistics
- Missing names (incomplete school names, etc.)
- Logical errors (listing sold-out subdivisions as active, etc.)
- The homestead exemption described as creditor protection, NOT a tax reduction

Fix any errors found. Report all fixes to Ryan.

### Step 8: Add Source Citations

Add an italicized source line at the bottom of every post. Use external sources only, not rosehomeslv.com. Format:

```
*Source: greatschools.org, crimegrade.org, summerlin.com*
```

Common source mapping:

| Data Type | Source |
|-----------|--------|
| School ratings | greatschools.org |
| Crime/safety grades | crimegrade.org, neighborhoodscout.com |
| Property taxes | clarkcountynv.gov, leg.state.nv.us |
| Market data | lasvegasrealtor.com |
| Mortgage rates | freddiemac.com |
| Summerlin communities | summerlin.com |
| Henderson communities | cityofhenderson.com |
| Builder info | tollbrothers.com, pulte.com, lennar.com, etc. |
| HOA management | terrawest.com, associanevada.com |
| Utilities | nvenergy.com, cox.com, lumen.com |
| Golf | golfdigest.com, tpc.com |
| Federal lands | nps.gov, blm.gov |
| Census/income | census.gov |
| Solar | energysage.com, nvenergy.com |
| NAR data | nar.realtor |
| General real estate | redfin.com |

### Step 9: Run Em-Dash Check

Run a grep on the output file:

```bash
grep -c '—' /path/to/Week_file.md
```

- Em-dashes must appear ONLY in the 21 header lines (`### Post N of 21 — TIME — Type`)
- Em-dashes must appear NOWHERE in body content
- Total count should equal exactly **42** (2 per header x 21 posts)

### Step 10: Update the Tracker

Append entries to `/Reddit/repurposed-blogs.md` for all 14 blog repurpose posts:

```
| YYYY-MM-DD | DIRECTORY_NAME | filename.html | Reddit Post Title |
```

### Step 11: Update Memory Files (if they exist)

Update `/memory/blog-directory-rotation.md` with new completion status.
Update `/memory/reddit-weekly-posting-workflow.md` with the new week added.

If these files do not exist, skip this step. The tracker is the authoritative source.

---

## Post Format (PARSER-DEPENDENT, DO NOT CHANGE)

```markdown
### Post N of 21 — TIME — Type

**Subreddit:** r/VegasRealtor
**Flair:** <flair>
**Title:** <title>

**Body:**

<body text>

<for blog repurpose posts only:>
Full guide with more details: <canonical URL>

*Source: source1.com, source2.com*

---
```

**Critical format rules:**
- Header lines use em-dashes. This is REQUIRED.
- Body content must NEVER contain em-dashes. Use commas, periods, semicolons, or "and" instead.
- Each post ends with a `---` separator
- Blog repurpose posts include the "Full guide" link before the source line
- Content calendar posts have the source line directly after the closing question
- TIME values: `10:00 AM`, `1:00 PM`, or `4:00 PM`
- Type values for content calendar: `Content Calendar (Topic Name)`
- Type values for blog repurpose: `Blog Repurpose (DIRECTORY Post N)`

---

## Content Calendar Rotation

The 10:00 AM post each day follows this rotation:

| Day | Topic | Flair | Title Prefix |
|-----|-------|-------|-------------|
| Sunday | Weekly Stat Drop | Market Data | [Weekly Stat Drop] |
| Monday | Buyer Tips | Buyer Tips | [Buyer Tips] |
| Tuesday | Neighborhood Breakdown | Neighborhood Guide | [Neighborhood Breakdown] |
| Wednesday | Educational | Educational | [Educational] |
| Thursday | Seller Tips | Seller Tips | [Seller Tips] |
| Friday | Neighborhood Breakdown | Neighborhood Guide | [Neighborhood Breakdown] |
| Saturday | Cost of Living | Cost of Living | [Cost of Living] |

**Content calendar posts:** 300 to 600 words. Data-rich. Vegas-specific. End with a question. No links. No self-promotion.

**Topic ideas by category:**

- **Weekly Stat Drop:** Median price (~$470K), inventory (6,000+), days on market (60-79), mortgage rates (mid 6%), price per sq ft ($250-270), new construction incentives, seasonal trends
- **Buyer Tips:** Solar panels, HOA due diligence, inspection priorities in desert climate, SID/LID taxes, new construction vs resale, VA/FHA considerations
- **Seller Tips:** Professional photography, pricing strategy in high inventory, staging, competing with new construction, pre-listing inspections
- **Neighborhood Breakdown:** Compare two communities head-to-head
- **Educational:** Property tax cap (3% primary, 8% non-primary), NRS 116 HOA law, homestead declaration (creditor protection only, NOT tax reduction), title insurance, escrow
- **Cost of Living:** NV Energy summer bills ($200-400), internet/cable, groceries, HOA fee ranges, SID/LID

---

## Blog Repurpose Post Guidelines

- Read the ENTIRE source HTML blog file
- Rewrite the content for Reddit (not copy-paste)
- 250 to 500 words
- Pull the most interesting and data-rich points
- Use the "knowledgeable neighbor" voice
- Include specific numbers from the blog
- End with a question
- Include the canonical URL: `Full guide with more details: <URL>`
- Add italicized external source line
- Flair is usually "Neighborhood Guide" unless the directory topic is a buyer/seller tip

**Special flair directories:**
- Directory 20 (Answer The Public Questions): use "Buyer Tips" or "Seller Tips"
- Directory 33 (New Construction): use "Educational" or "Buyer Tips"
- Directory 40 (EXPIRED LISTINGS): use "Seller Tips"
- Directory 41 (WORKER ADVANTAGE PROGRAM): use "Buyer Tips"

---

## Writing Rules (NON-NEGOTIABLE)

Every single post must follow these rules:

1. **NO EM-DASHES EVER IN BODY CONTENT.** Not one. Use commas, periods, semicolons, or "and." Em-dashes are ONLY in the `### Post N of 21 — TIME — Type` header lines.
2. **6th grade reading level.** Simple words. Short sentences. No jargon unless explained.
3. **No links in body text.** The only link is the "Full guide with more details" line for blog repurpose posts.
4. **No self-promotion.** Never mention Rose Homes LV or any business in the body.
5. **Data-rich.** Include specific numbers: prices, percentages, dollar amounts, distances, ratings.
6. **Vegas-specific.** Use neighborhood names, local details, specific areas.
7. **"Knowledgeable neighbor" voice.** Casual, warm, helpful. Not salesy, not formal.
8. **End every post with a question.** Encourages comments and engagement.
9. **Bold section headers.** Use `**Header.**` format for organizing the post body.
10. **No fabricated data.** Every number must come from the source blog, the data points below, or verifiable public sources. If you cannot verify a number, do not include it.
11. **No em-dashes in any content Ryan will read.** This includes titles, body text, source lines, and closing questions.

---

## Key Data Points (for Content Calendar Posts)

These are baseline Las Vegas real estate data points:

- **Median home price (Vegas metro):** ~$470,000
- **Active listings:** 6,000+ across Clark County
- **Property tax rate:** ~0.53% (one of the lowest in the country)
- **Property tax cap:** 3% max increase/year for primary residence, 8% for non-primary
- **No state income tax** in Nevada
- **Homestead exemption:** Protects up to $605,000 equity from creditor judgments (NRS 115). Does NOT reduce assessed value or lower property taxes. This is purely creditor protection.
- **Summer electric bills:** $200-400/month for older homes
- **NV Energy budget billing** available to flatten monthly payments
- **HOA fees:** $100-200/month typical for houses, $350-500/month for condos
- **SID/LID taxes** in newer communities: $200-400/month additional
- **HVAC lifespan in Vegas:** 8-10 years (vs 15-20 in milder climates)
- **NRS 116:** Nevada HOA law governing reserve studies, resale packages
- **Rent ranges:** 1BR $1,200-1,800; 2BR $1,500-2,400
- **Mortgage rates:** Mid 6% range for conventional 30-year fixed
- **Days on market:** 60-79 days valley wide average
- **Price per square foot:** $250-270 valley wide, $500+ for Summerlin/Henderson luxury
- **Mortgage estimate:** ~$2,500-2,800/month for median priced home

---

## Blog Directory Rotation Order (1-41)

1. SUMMERLIN
2. Green Valley
3. MADEIRA CANYON
4. WHITNEY RANCH
5. INSPIRADA
6. CENTENNIAL HILLS
7. ALIANTE
8. RHODES RANCH
9. Seven Hills
10. THE PASEOS
11. EAGLE HILLS
12. ASCENSION
13. THE WILLOWS OF SUMMERLIN
14. CANYONS OF SUMMERLIN
15. THE PUEBLOS OF SUMMERLIN
16. TOURNAMENT HILLS
17. BLACK MOUNTAIN
18. HORIZONS EDGE
19. SPRING VALLEY
20. Answer The Public Questions
21. PALISADES SUMMERLIN
22. QUEENSRIDGE
23. RED ROCK COUNTRY CLUB
24. RIDGEBROOK
25. CROSSINGS IN SUMMERLIN
26. Canyon Fairways
27. ASTRA AT LA MADRE PEAKS
28. Reverence
29. MESQUITE NV
30. MOUNTAIN TRAILS
31. MacDonald Ranch
32. NAKED CITY
33. New Construction
34. SPANISH TRAILS
35. THE HILLS
36. THE RIDGES
37. THE VISTAS OF SUMMERLIN
38. The Arbors
39. The Cliffs
40. EXPIRED LISTINGS
41. WORKER ADVANTAGE PROGRAM

When all 41 directories are done in a round, loop back to #1 and use the next post from each directory.

---

## File Locations

| File | Path | Purpose |
|------|------|---------|
| Weekly posts output | `/Reddit/Week_MonDD-MonDD_Posts.md` | The 21-post batch file |
| Blog tracker | `/Reddit/repurposed-blogs.md` | Tracks every repurposed blog |
| Blog source files | `/Claude/Claude Blogs/<DIRECTORY>/` | HTML blog files to repurpose |
| Workflow memory | `/memory/reddit-weekly-posting-workflow.md` | Progress tracker (if exists) |
| Directory rotation memory | `/memory/blog-directory-rotation.md` | Completion status (if exists) |
| Strategy document | `/Reddit/CLAUDE.md` | Full Reddit strategy and rules |

All paths relative to the workspace root (the mounted folder).

---

## QA Checklist

Run this verification on every batch before delivering:

- [ ] Every blog repurpose post cross-referenced against its source HTML file
- [ ] All prices, square footage, lot sizes, and fees match the source
- [ ] All school names are complete and ratings correct
- [ ] All crime scores and safety rankings match the source
- [ ] All distances and commute times match the source
- [ ] All builder names and home counts match the source
- [ ] No inflated or unsupported statistics in content calendar posts
- [ ] Homestead exemption described as creditor protection, NOT tax reduction
- [ ] No em-dashes in body content (grep verified, count = 42)
- [ ] All 21 posts have italicized source lines with external sources
- [ ] All 14 blog repurpose posts have "Full guide with more details" links
- [ ] Tracker updated with all 14 new entries
- [ ] Memory files updated (if they exist)

---

## Output Summary

After completing all steps, provide Ryan with:

1. The posts file link
2. A count confirmation (7 content calendar + 14 blog repurpose = 21 total)
3. Which blog directories were used and which post round
4. Any QA fixes that were made
5. Confirmation that tracker and memory files were updated

---

## Common Mistakes to Avoid

1. **Using em-dashes in body content.** Always grep to verify.
2. **Citing the homestead exemption as a tax reduction.** It is creditor protection under NRS 115. Period.
3. **Misidentifying which blog files have been used.** Always check the tracker first.
4. **Fabricating comparison data.** If the source blog only covers one community, do not invent numbers for a comparison community unless verifiable.
5. **Using the wrong flair.** Neighborhood content = "Neighborhood Guide". Only content calendar posts get topic-specific flairs.
6. **Forgetting to extract the canonical URL.** Every blog repurpose post needs the blog link.
7. **Listing sold-out subdivisions as active.** Read the source blog carefully.
8. **Rounding source numbers.** If the blog says 23.4 acres, write 23.4 acres.
9. **Using `/blogs/` (plural) in URLs.** The correct pattern is `/blog/` (singular). Plural 404s.

---

## Already-Used Blog Files (Do Not Reuse)

The `/Reddit/repurposed-blogs.md` tracker is the authoritative source. This snapshot is current as of May 26, 2026. **Always check the live tracker before each batch.**

### Directories 1-16: Post 1, Post 2, AND Post 3 Complete

**1. SUMMERLIN**
- 06-moving-to-summerlin-relocation.html
- 07-relocating-summerlin-from-california.html
- 08-cost-of-living-summerlin.html

**2. Green Valley**
- blog-01-where-is-green-valley-located-henderson.html
- blog-02-green-valley-henderson-zip-code.html
- blog-03-is-green-valley-henderson-safe.html

**3. MADEIRA CANYON**
- post1-living-in-madeira-canyon-henderson.html
- post10-madeira-canyon-vs-anthem.html
- post3-madeira-canyon-hoa-fees.html

**4. WHITNEY RANCH**
- post1-living-in-whitney-ranch-henderson.html
- post10-whitney-ranch-first-time-buyer-guide.html
- post3-is-whitney-ranch-good-place-to-live.html

**5. INSPIRADA**
- 01-what-is-inspirada-henderson.html
- 02-inspirada-home-prices-2026.html
- 03-is-inspirada-good-place-to-live.html

**6. CENTENNIAL HILLS**
- 01-centennial-hills-las-vegas-guide.html
- 02-centennial-hills-home-prices-2026.html
- 03-is-centennial-hills-good-place-to-live.html

**7. ALIANTE**
- 01-aliante-north-las-vegas-community-guide.html
- 02-aliante-home-prices-2026.html
- 03-is-aliante-good-place-to-live.html

**8. RHODES RANCH**
- 01-rhodes-ranch-community-guide.html
- 02-rhodes-ranch-home-prices-2026.html
- 03-is-rhodes-ranch-good-place-to-live.html

**9. Seven Hills**
- allegro-park-seven-hills-henderson.html
- avalon-seven-hills-henderson.html
- butch-harmon-school-of-golf-seven-hills.html

**10. THE PASEOS**
- post1-paseos-summerlin-village-guide.html
- post10-summerlin-trails-near-paseos.html
- post2-paseos-home-prices-2026.html

**11. EAGLE HILLS**
- post1-eagle-hills-las-vegas-community-guide.html
- post10-eagle-hills-investment-potential-2026.html
- post2-eagle-hills-summerlin-home-prices-2026.html

**12. ASCENSION**
- post1-ascension-summerlin-community-guide.html
- post10-luxury-homes-ascension-summerlin.html
- post2-ascension-summerlin-home-prices-2026.html

**13. THE WILLOWS OF SUMMERLIN**
- 01-willows-summerlin-community-guide.html
- 02-willows-summerlin-home-prices-2026.html
- 03-is-willows-summerlin-good-place-to-live.html

**14. CANYONS OF SUMMERLIN**
- post1-canyons-summerlin-community-guide.html
- post10-investment-potential-canyons-summerlin.html
- post2-canyons-summerlin-home-prices-2026.html

**15. THE PUEBLOS OF SUMMERLIN**
- post-10-pueblo-summerlin-dog-parks-pet-friendly.html
- post2-pueblo-summerlin-home-prices-2026.html
- post3-is-pueblo-summerlin-good-place-to-live.html

**16. TOURNAMENT HILLS**
- post1-tournament-hills-las-vegas.html
- post10-living-guard-gated-summerlin.html
- post2-tournament-hills-home-prices-2026.html

### Directories 17-41: Post 1 and Post 2 Complete, Post 3 NOT Started

**17. BLACK MOUNTAIN**
- 01-black-mountain-henderson-community-guide.html
- 02-black-mountain-henderson-home-prices-2026.html

**18. HORIZONS EDGE**
- post1-what-is-horizons-edge-henderson.html
- post10-horizons-edge-south-floor-plans-prices.html

**19. SPRING VALLEY**
- 01-spring-valley-las-vegas-community-guide.html
- 02-spring-valley-las-vegas-home-prices-2026.html

**20. Answer The Public Questions**
- seller1-how-to-sell-house-las-vegas.html
- batch6-post2-buyer-contingencies-mountains-edge.html

**21. PALISADES SUMMERLIN**
- 01-palisades-summerlin-community-guide.html
- 02-palisades-summerlin-home-prices-2026.html

**22. QUEENSRIDGE**
- 01-what-is-queensridge-las-vegas.html
- 02-queensridge-home-prices-2026.html

**23. RED ROCK COUNTRY CLUB**
- 01-red-rock-country-club-community-guide.html
- 02-red-rock-country-club-home-prices-2026.html

**24. RIDGEBROOK**
- 01-ridgebrook-las-vegas-community-guide.html
- 02-ridgebrook-home-prices-2026.html

**25. CROSSINGS IN SUMMERLIN**
- post10-investment-properties-crossing-summerlin.html
- 02-crossing-summerlin-home-prices-2026.html

**26. Canyon Fairways**
- batch1-post1-what-is-canyon-fairways-summerlin.html
- batch1-post2-canyon-fairways-home-prices-2026.html

**27. ASTRA AT LA MADRE PEAKS**
- 01-astra-la-madre-peaks-community-guide.html
- 02-astra-la-madre-peaks-lot-prices-2026.html

**28. Reverence**
- batch1-post1-what-is-reverence-summerlin.html
- batch1-post2-reverence-summerlin-home-prices-2026.html

**29. MESQUITE NV**
- post1-mesquite-nv-living-guide.html
- post2-mesquite-nv-home-prices-2026.html

**30. MOUNTAIN TRAILS**
- 01-mountain-trails-summerlin-community-guide.html
- 02-mountain-trails-home-prices-2026.html

**31. MacDonald Ranch**
- post-01-macdonald-highlands-complete-guide.html
- post-02-history-macdonald-highlands.html

**32. NAKED CITY**
- post1-naked-city-las-vegas-guide.html
- post2-naked-city-home-prices.html

**33. New Construction**
- batch1-post1-new-construction-cost-las-vegas.html
- batch1-post2-new-construction-vs-resale.html

**34. SPANISH TRAILS**
- 01-spanish-trail-las-vegas-community-guide.html
- 02-spanish-trail-home-prices-2026.html

**35. THE HILLS**
- 01-the-hills-summerlin-community-guide.html
- 02-the-hills-summerlin-home-prices-2026.html

**36. THE RIDGES**
- 01-ridges-summerlin-community-guide.html
- 02-ridges-summerlin-home-prices-2026.html

**37. THE VISTAS OF SUMMERLIN**
- 01-what-is-vistas-summerlin.html
- 02-vistas-summerlin-home-prices-2026.html

**38. The Arbors**
- batch1-post1-what-is-the-arbors-summerlin.html
- batch1-post2-arbors-summerlin-home-prices-2026.html

**39. The Cliffs**
- 01-cliffs-summerlin-community-guide.html
- 02-cliffs-summerlin-home-prices-2026.html

**40. EXPIRED LISTINGS**
- post1-why-your-las-vegas-home-isnt-selling.html
- post2-home-didnt-sell-what-to-do-next.html

**41. WORKER ADVANTAGE PROGRAM**
- post1-nevada-worker-advantage-program-explained.html
- post2-apply-nevada-20000-down-payment-assistance.html

---

## Current Status (as of May 26, 2026)

- **Weeks completed:** Apr 6-12, Apr 15-21, Apr 22-28, Apr 29-May 5, May 6-12, May 13-19, May 20-26
- **Total posts written:** 147+ (21 per week x 7 weeks)
- **Post 1s:** ALL 41 directories exhausted
- **Post 2s:** ALL 41 directories exhausted
- **Post 3s:** Directories 1-16 complete (SUMMERLIN through TOURNAMENT HILLS)
- **Next batch:** Post 3s starting from directory 17 (BLACK MOUNTAIN) onward
- **Next week dates:** Starts the day after the last tracker entry
