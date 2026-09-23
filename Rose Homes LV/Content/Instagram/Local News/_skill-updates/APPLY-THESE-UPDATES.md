# Local News Skill Updates - Combined Apply

**Covers two rounds of changes at once:**

- **August 24, 2026** - a new Local News and Events category, and a source line on every Instagram caption. Never applied.
- **September 1, 2026** - the new BONUS BLOGS pipeline stage.

Neither round is live yet. One copy applies both.

I could not write to the installed plugin directly (skill files are read-only from inside a session), so every changed file is in this folder as a complete drop-in replacement.

---

## How to apply

Copy all 17 `.md` files from this folder into your plugin's skill directory, overwriting what is there. Based on the publish script path, that should be:

```
/Users/ryanrose/Downloads/Claude/_System/plugins/local-news-plugin/skills/local-news/
```

One-liner:

```
cp "/Users/ryanrose/Downloads/Claude/Rose Homes LV/Content/Instagram/Local News/_skill-updates/"*.md \
   "/Users/ryanrose/Downloads/Claude/_System/plugins/local-news-plugin/skills/local-news/"
```

That single copy applies everything, both rounds. Nothing gets deleted. Files that are not in this folder (`blog-strategist.md`, `blog-creator.md`) are unchanged and stay as they are.

If your plugin source lives somewhere else, drop them there instead. Reinstall or reload the plugin afterward so the changes take effect.

---

## Round 1, August 24: New category, Local News and Events

A sixth research agent now runs alongside the existing five, feeding a fifth output category. It is the quick-hit beat modeled on @realvegaslocals: events and things to do, restaurant and business openings and closings, traffic and road closures, weather and utilities, public safety of broad interest, community and human interest, viral local moments, and neighborhood-level happenings. Residents first, tourists never.

**The weekly set goes from 21 stories to 27.** New balance:

| Category | Stories | Floor |
|---|---|---|
| Government and Development | 5 | 4 |
| School Board and Education | 4 | 3 |
| Hockey | 5 | 3 |
| Real Estate Market | 7 | 5 |
| Local News and Events | 6 | 4 |
| **Total** | **27** | |

Local News and Events stories get the full package: video transcript, blog, Instagram caption, YouTube description. They do NOT get Reddit posts. Reddit stays real estate only, now about 7 posts a week.

Blog creation runs in five waves of 6/6/6/6/3 instead of four.

There is a variety rule on the new category so it cannot come back as six restaurant openings. The selection has to span at least four different beat types.

### Where the sources came from

I researched @realvegaslocals to find their actual sourcing. They publish a FAQ that lays it out: city and county press releases, public meetings, government records, public safety agencies, court filings, development applications, and resident tips, verified against official records. They monitor neighborhood groups and social media for leads, then confirm before posting. Very little original reporting.

The four anchors that will fill most of a week, now baked into the source registry:

1. **LVMPD press releases** for public safety. Highest-cadence source in the valley, multiple same-day posts.
2. **Seeing Orange NV** for traffic. Refreshes every Thursday and already aggregates city, county and NDOT closures.
3. **Las Vegas Weekly "What to do this week"** for events. Published Wednesdays, pre-curated.
4. **RJ Neon Dining Out** for openings and closings. Highest-engagement quick-hit format after public safety.

Plus a full set of neighborhood calendars on a rotation so Summerlin, Henderson, North Las Vegas, Boulder City, Skye Canyon, Centennial Hills and Green Valley each get covered roughly monthly. The Craig Ranch AMP page and the Skye Canyon calendar were the two highest-yield finds.

### Broken URLs I fixed while I was in there

Several sources in the old registry are dead or redirected. These are now corrected and flagged:

- `lasvegaslocally.com` is a dead placeholder now, follow the Instagram instead
- `vitalvegas.com` moved to casino.org/vitalvegas
- `reviewjournal.com/entertainment/food` redirects to neon.reviewjournal.com/dining-out
- `ndot.nv.gov` is wrong, the domain is `dot.nv.gov`
- `thespringspreserve.org` is dead, it is `springspreserve.org` with no "the"
- `downtownsummerlin.com` folds into `summerlin.com`
- `lasvegasmotorspeedway.com` redirects to `lvms.com`
- `lasvegasraiders.com` is wrong, it is `raiders.com`

There is also a new list of sources that silently block automated fetching, so a research agent knows to route around them instead of dropping a real story.

---

## Round 1, August 24: Source line on every Instagram caption

Every caption now ends with:

```
Source: Redfin - "How to Buy a House"
```

Publication name, space hyphen space, then the exact article title in straight double quotes. It is the very last line, below the contact block. The same line was added to YouTube descriptions, sitting between the contact block and the tags.

To make this work, the article title has to survive the whole pipeline, so all six research agents now capture an `Article Title` field alongside the source and URL, transcribed word for word from the source headline. The viral strategist passes it through. The social writer builds the line from it. It is also a column in the story spreadsheet now.

Rules baked in:

- Transcribe the headline exactly. No paraphrasing, no shortening, no re-capitalizing, no fixing punctuation. Followers use it to go find the article.
- Regular hyphen, not an en-dash or em-dash.
- One source per caption. If a story came from several, credit the strongest.
- Never credit an Instagram or TikTok account. Those are leads only, so the story gets traced back to the primary source and that gets credited.
- A story with no article title cannot be published and gets dropped in favor of the next-best story in its category.

---

## Round 2, September 1: Bonus blogs

Every researched story that does NOT make the weekly selected set now gets a blog post anyway. Blogs only. No video transcript, no Instagram caption, no YouTube description, no Reddit post. This is straight SEO volume, so nothing that was researched and verified goes to waste.

It runs as a new pipeline stage, **Step 5B**, which sits after the main blog creation step and before the Reddit step.

### How it works

1. **The viral strategist now writes two files.** `top-stories.md` is unchanged. `bonus-stories.md` is new, and it holds every unselected story from all six research agents, with the full summary, source, article title, URL, date, why it matters, and figures. Each carries a `Cut Reason`.

2. **Cut Reason is one of three values:**
   - `Duplicate` - a prior week already covered this event. These also carry a `Prior Coverage` field naming the earlier headline.
   - `Score` - verified and fresh, just ranked below the cut.
   - `Overlap` - functionally the same content as a selected story.

3. **Two kinds of story are excluded from bonus entirely.** Anything with no verified source URL, and anything that overlaps a selected story. Overlap happens most often when the local Real Estate agent and the National-to-Local agent both surface the same Case-Shiller or Freddie Mac number from different angles. A bonus blog there would be word-for-word competition with a selected blog, so it gets logged as `Overlap` in the notes and skipped.

4. **The bonus set never shrinks the selected set.** Selection and ranking happen exactly as before. The bonus file is a sweep of what is left over.

5. **A new Bonus Blog Strategist** builds `bonus-blog-seo-package.md`: slug, SEO title under 60 characters, meta description under 150, keyword string near 500, and 3 related internal links per story. Same as the regular blog strategist, plus two things that are unique to it.

6. **A new Bonus Blog Creator** writes the articles to `blogs/bonus/bonus-[NN]-[slug].html`. Format is identical to the regular blog creator: 2400 words, 4 to 5 real image URLs, NewsArticle schema, source attribution, contact CTA, 3 related links, no metadata blocks, no em-dashes.

### The two things unique to the bonus strategist

**Slug collision check.** Months of weekly runs means a lot of slugs are already taken, and a repeat means a broken URL or an overwritten post. Before assigning anything, the agent has to enumerate every slug already in use across every dated run folder, main and bonus both:

```
ls "/Users/ryanrose/Downloads/Claude/Rose Homes LV/Content/Instagram/Local News/"2026-*/blogs/*.html "/Users/ryanrose/Downloads/Claude/Rose Homes LV/Content/Instagram/Local News/"2026-*/blogs/bonus/*.html 2>/dev/null | sed 's|.*/story-[0-9]*-||; s|.*/bonus-[0-9]*-||; s|\.html$||' | sort -u
```

No new slug may collide. And when one would, the fix is a genuinely different slug built on a different keyword or place name, never the old slug with a `-2` on the end.

**Angle field.** Every `Duplicate` cut gets a mandatory `Angle`, because a prior post already covers that event and a rehash would just compete with it. The Angle names the distinct treatment: a newer development, a deeper explainer, a "what this means for buyers, sellers, or parents" piece, or a background and timeline piece. It also names the prior post's slug, so the new article links back to it as earlier coverage. A duplicate with no findable angle gets dropped rather than shipped.

### Everything else that changed

- **Step 0** now creates `blogs/bonus/` alongside `blogs/`.
- **Step 5B** runs the bonus strategist, then the bonus creators in waves of 6, same as the main blog waves. Validation gate is one HTML file per bonus story, each with `<article>`, an ld+json schema block, and `<img>` tags, plus the same `grep -rl 'src="#"'` placeholder check run against the bonus folder.
- **The whole bonus stage is non-blocking.** A failing wave gets one retry, then it flags and moves on. Bonus failures never stop Step 6 or Step 7, and never delay the main set.
- **Reddit excludes bonus stories entirely**, including bonus real estate stories.
- **The spreadsheet excludes bonus stories from the main table and from the weekly summary**, and instead carries a short appendix at the bottom with four columns: bonus headline, category, cut reason, slug.
- **The final report** gained a Bonus Blogs section with counts by cut reason, exclusion counts, slug rewrites, and any misses.

---

## Files in this folder

**New**

- `research-local-events.md` - the Local News and Events research agent (August 24)
- `bonus-blog-strategist.md` - the bonus SEO and slug agent, with the collision check and the Angle rule (September 1)
- `bonus-blog-creator.md` - the bonus article agent, points at blog-creator.md for format (September 1)

**Changed**

- `SKILL.md` - six research agents, 27-story minimum, new balance, five blog waves, source line, plus the whole Step 5B bonus stage, `blogs/bonus/` in Step 0, bonus exclusions on Reddit and the spreadsheet, bonus error handling, bonus core principles, updated report
- `viral-strategist.md` - fifth category, new balance and floors, variety rule, two new tiebreakers for free and time-sensitive events, article title passthrough, plus the required `bonus-stories.md` output with cut reasons and exclusions
- `spreadsheet-assembler.md` - Article Title column, fifth category, 27-story count, plus the bonus appendix table
- `source-registry.md` - full Local News and Events source section, expanded Instagram lead accounts, broken-URL corrections
- `content-rules.md` - new Source Attribution section, new Local News and Events rules
- `social-media-writer.md` - source line spec for Instagram and YouTube, local events voice guidance, self-check
- `transcript-templates.md` - source line in both templates, new local events video template, new hooks and comment questions
- `content-producer.md` - fifth category, local events voice and length guidance
- `reddit-post-writer.md` - excludes Local News and Events, count updated to ~7
- `research-gov-dev.md`, `research-school-board.md`, `research-hockey.md`, `research-real-estate.md`, `research-national-real-estate.md` - Article Title field added to each output format

**Not in this folder, unchanged**

- `blog-strategist.md` and `blog-creator.md` are untouched. `bonus-blog-creator.md` references `blog-creator.md` for the article format, so leave it where it is.

---

## Things to watch on the first run

**Run length.** 27 stories with full blogs was already a meaningfully longer run than 23 was, and the bonus set adds more blogs on top. Last week's run hit a session limit during the final blog wave. If it happens again, the blogs that were mid-write still land on disk, they just come out short, so the fix is to expand those specific files rather than rerun the pipeline. The bonus stage is deliberately non-blocking for exactly this reason: if it does not finish, the week still ships.

**Bonus volume.** The first run will show how big the bonus set actually is. Six research agents pulling 8 to 15 stories each is 50 to 80 stories in, minus 27 selected, minus overlaps and unverified ones. If that leaves more bonus blogs than is comfortable in one session, the easy lever is to cap the bonus set at the top N by score in `viral-strategist.md`.

**Slug collisions.** The collision command is the guardrail here. Spot-check the bonus SEO package the first time and confirm the agent actually ran it rather than assuming.
