# 10 — Content Blueprint: `/new-construction` Master Hub (Rose Homes LV)

**Role of this file:** the information architecture, copy specification, SEO package, schema
plan, and internal link web for the flagship New Construction hub. A separate agent owns
visual design. This file owns **what goes where, in what order, in what words, sourced from
where.**

**Target:** 30 blueprint blocks, 22 of them anchored and in the table of contents,
**~10,400 editorial words** (excluding IDX card text and table cell text).

**Publishing target:** Lofty landing page, raw HTML embed, slug `/new-construction`.

---

## 0. Standing rules that govern every word on this page

These are not suggestions. Anything that violates one of them gets rejected at review.

| Rule | Detail |
|---|---|
| **No em-dashes. Anywhere.** | Use commas, periods, or "and". Also no en-dashes in prose. Hyphens are allowed only inside slugs and inside compound modifiers ("build-to-order"). Number ranges in tables use "to" ($400K to $600K), not a dash. |
| **Factual only** | Every price, count, incentive, fee, square footage, HOA amount, school rating, and date is either verified against a named primary source, or it is written into the HTML as the literal string `NOT FOUND` with an HTML comment naming the source to check. No exceptions, no placeholders that read like real numbers. |
| **Do not copy NRG's numbers** | Their incentive table, their community counts, and their price bands are their research, they go stale monthly, and a wrong incentive figure is a real liability for a licensed agent. We reference their page structure only. |
| **6th grade reading level** | Short sentences. One idea per sentence. No "premier", "exclusive opportunity", "nestled", "boasts", "unparalleled". Define any industry term on first use (SID, LID, buydown, lot premium, spec home). |
| **Soft CTAs** | "Have a question about a specific community? Send it over." not "Call now, inventory is moving fast." |
| **No inline `<form>`** | Lofty does not ingest leads from in-embed forms. Every CTA is `href="#contact"`. The Lofty form block is appended below the embed at publish time and the page JS scrolls `#contact` clicks to the bottom of the document. |
| **Flat slugs** | Lofty has no nested paths. `/new-construction`, `/henderson-new-construction`, `/dr-horton-las-vegas`. Blog posts are `/blog/<slug>`, singular. The plural `/blogs/` 404s. |
| **Citation format** | `<p style="font-size: 0.85em; font-style: italic;">Source: <a href="[url]">[Source Name]</a></p>` placed directly under the claim, table, or section it supports. |
| **Contact block** | Ryan Rose, Real Broker, LLC, 702-747-5921, ryan@rosehomeslv.com, rosehomeslv.com. |

### The `NOT FOUND` convention, exactly

In the HTML, an unverified value ships as:

```html
<td>NOT FOUND <!-- source to check: lennar.com/nv/las-vegas "Homes from" strip, re-verify monthly --></td>
```

It renders as the visible words `NOT FOUND` in the cell. That is deliberate. A visible gap is
honest and prompts Ryan to fill it. A fabricated number is a liability. If a whole table would
be more than half `NOT FOUND` at launch, ship the table with a dated note above it instead of
guessing (see Table 5).

---

## 1. Section-by-section blueprint, in page order

Column key: **WC** = target word count. **CTA** = the call to action that closes the block.
All CTAs are `href="#contact"` anchors unless noted.

### Block 0 — Breadcrumb strip

| Field | Value |
|---|---|
| Anchor id | none |
| H2 | none |
| TOC label | not in TOC |
| Type | nav strip |
| WC | 4 |
| Data needed | none |
| CTA | none |

Markup: `Home  ›  New Construction`. `Home` links to `https://www.rosehomeslv.com/`. Mirrored
1:1 in the BreadcrumbList schema block (see §8).

---

### Block 1 — Hero

Full spec in §2 below. Summary row:

| Field | Value |
|---|---|
| Anchor id | none |
| H1 | New Construction Homes in Las Vegas |
| TOC label | not in TOC |
| Type | image band, H1 + subhead + stat line + 3 CTA buttons |
| WC | 45 |
| Data needed | hero photo, builder count (self-verifiable), area count (self-verifiable), updated month |
| CTA | 3 buttons: `#listings`, `#builders`, `#contact` |

---

### Block 2 — Direct answer and key takeaways

| Field | Value |
|---|---|
| Anchor id | `answer` (not in TOC, but needed as the `speakable` schema target) |
| H2 | none. `aria-label="Direct answer summary"` on the wrapper. |
| TOC label | not in TOC |
| Type | `blockquote.direct-answer` + `ul.key-takeaways` (6 bullets) |
| WC | 290 |
| Data needed | see below, all six bullets are structural or statutory, no dollar figures |
| CTA | none. This block is for answer engines, not for conversion. |

This is the single most important block on the page for AI search and featured snippets. It is
the `cssSelector` target in the Article schema's `speakable` property. It must answer the head
query in the first sentence.

**Proposed copy, verbatim:**

> Las Vegas is one of the busiest new home markets in the country. This guide covers 20 builders
> working across Clark County, the seven parts of the valley where most new homes are going up,
> and the full buying process from your first model home visit to the day you get the keys. In
> Nevada, the builder pays the buyer agent commission out of the same marketing budget either
> way, so bringing your own agent does not raise your price. What does change your price is the
> lot premium, the design center, and whether the community carries a SID or LID assessment on
> top of property taxes. Those three line items are where new construction buyers get surprised,
> and they are covered in detail below.

**Key takeaways, verbatim, 6 bullets:**

1. Register with your own agent on your very first visit. If you walk into a model home alone,
   the person at the desk works for the builder, not for you.
2. The base price on the sign is not the finished price. Lot premium, design center upgrades,
   and landscaping are usually billed on top of it.
3. Every new home in Nevada carries a 1-2-10 warranty. One year on workmanship, two years on
   systems, ten years on structure.
   *(Cite: Nevada Revised Statutes 624.602 and NRS Chapter 40. VERIFY-CITE before publish.)*
4. Many newer master plans carry a SID or LID assessment. That is a separate bill from your
   property tax, and it can run for 10 to 20 years. Ask for the exact amount in writing before
   you sign.
   *(Cite: Clark County Assessor and City of Henderson. Dollar amount stays NOT FOUND on the hub,
   it is community specific.)*
5. Nevada has no state income tax, and yearly property tax increases on a primary residence are
   capped at 3 percent.
   *(Cite: Nevada Department of Taxation. VERIFY-CITE before publish.)*
6. You cannot put grass in the front yard of a new Southern Nevada home. Plan your landscape
   budget around desert planting.
   *(Cite: Southern Nevada Water Authority. VERIFY-CITE before publish.)*

**Sourcing note:** bullets 3, 5, and 6 are statutory or regulatory, so they are stable, but they
still need a live link before publish. Bullets 1, 2, and 4 are process facts with no numbers, so
they carry no data risk.

---

### Block 3 — Byline and meta strip

| Field | Value |
|---|---|
| Anchor id | none |
| H2 | none |
| TOC label | not in TOC |
| Type | one line of meta text |
| WC | 22 |
| Data needed | Ryan's Nevada license number (**NOT FOUND**, source: Ryan, or nvrealtors / Nevada Real Estate Division licensee lookup at red.nv.gov), publish date, updated date, read time |
| CTA | none |

**Proposed copy:**

> By Ryan Rose, Real Broker, LLC, Nevada license NOT FOUND · Published [DATE] · Updated [DATE] ·
> About a 30 minute read

The `Updated` date must be a real `<time datetime="">` and must match `dateModified` in the
Article schema. Set a calendar reminder to bump it whenever the incentives section or any table
is refreshed. A stale `Updated` date on a page that claims current pricing is worse than no date.

---

### Block 4 — Table of contents ("On This Page")

| Field | Value |
|---|---|
| Anchor id | none (the `nav.toc` element itself) |
| H2 | On This Page |
| TOC label | n/a |
| Type | ordered list, 22 jump links |
| WC | 70 |
| Data needed | none |
| CTA | none |

TOC labels are the **short keyword form**, not the H2 text. That is the pattern worth copying:
the H2 is the natural language question that wins the snippet, the TOC label is the two or three
word scannable label.

| # | Anchor | TOC label |
|---|---|---|
| 1 | `#listings` | New homes for sale now |
| 2 | `#builders` | Las Vegas builders |
| 3 | `#why-new` | Why buy new in Las Vegas |
| 4 | `#summerlin` | Summerlin |
| 5 | `#henderson` | Henderson |
| 6 | `#north-las-vegas` | North Las Vegas |
| 7 | `#southwest` | Southwest Las Vegas |
| 8 | `#skye-canyon` | Skye Canyon |
| 9 | `#centennial-hills` | Centennial Hills |
| 10 | `#lake-las-vegas` | Lake Las Vegas |
| 11 | `#launches` | New communities |
| 12 | `#builder-comparison` | Builder comparison |
| 13 | `#price-by-area` | Prices by area |
| 14 | `#new-vs-resale` | New vs resale |
| 15 | `#step-by-step` | The buying steps |
| 16 | `#incentives` | Builder incentives |
| 17 | `#sid-lid` | SID and LID taxes |
| 18 | `#warranties` | Warranties |
| 19 | `#lot-premiums` | Lot premiums and upgrades |
| 20 | `#why-ryan` | Working with Ryan |
| 21 | `#faq` | Questions and answers |
| 22 | `#sources` | Sources |

**Two deliberate improvements over NRG:**
1. NRG's "Why use us" H2 has no `id` and no TOC entry. Ours (`#why-ryan`) is anchored and
   listed. It is the conversion section, it should be reachable.
2. NRG has no `#sources` block at all. Ours does, and it is in the TOC. That is an E-E-A-T
   signal and it makes the "factual only" rule visible to the reader.

---

### Block 5 — "New Construction by Area" pill row

| Field | Value |
|---|---|
| Anchor id | none |
| H2 | New Construction by Area |
| TOC label | not in TOC |
| Type | row of 7 pill links |
| WC | 45 |
| Data needed | none, all 7 destinations are our own spoke pages |
| CTA | the pills themselves |

One line of intro, then 7 pills. **Proposed intro copy:**

> Each area below has its own page with the builders, the communities, and the homes that are
> actually for sale there right now.

Pills, in this order, linking to the 7 geo spokes (see §7 for slugs): Summerlin · Henderson ·
North Las Vegas · Southwest Las Vegas · Skye Canyon · Centennial Hills · Lake Las Vegas.

---

### Block 6 — Live listings slot

Full spec in §3 below. Summary row:

| Field | Value |
|---|---|
| Anchor id | `listings` |
| H2 | **New Construction Homes For Sale in Las Vegas Right Now** |
| TOC label | New homes for sale now |
| Type | Lofty IDX embed, or the static fallback |
| WC | 230 (header, lede, method note, and attribution, all static) |
| Data needed | **the Lofty IDX embed snippet. BLOCKED on Ryan.** See §10. |
| CTA | "See all new construction listings" button to a pre-filtered Lofty search URL (**NOT FOUND**, source: Ryan) |

---

### Block 7 — Builder grid

Full spec in §4 below. Summary row:

| Field | Value |
|---|---|
| Anchor id | `builders` |
| H2 | **Who is building new homes in Las Vegas?** |
| TOC label | Las Vegas builders |
| Type | 20 builder cards + 5 filter chips |
| WC | 1,050 (150 intro + 20 cards at ~45 words each) |
| Data needed | per-card fields, see §4. Community counts from Ryan's own research files, price bands **NOT FOUND** |
| CTA | none inside the grid. Each card links to its builder page. |

**Proposed section intro, verbatim:**

> Twenty builders are actively selling new homes in Clark County. A few of them are national
> companies that build thousands of homes a year at a set price with a set list of finishes.
> Others are local companies that build a few dozen homes a year and let you change almost
> anything. Neither one is better. They are built for different buyers. Use the filter buttons
> to narrow the list by price level, then open a builder page to see where they are building and
> what their homes actually include.

---

### Block 8 — Why buy new construction in Las Vegas

| Field | Value |
|---|---|
| Anchor id | `why-new` |
| H2 | **Why do so many Las Vegas buyers choose new construction?** |
| TOC label | Why buy new in Las Vegas |
| Type | prose, 4 paragraphs, 5 to 8 outbound authority citations |
| WC | 560 |
| Data needed | see below |
| CTA | soft, closing line to `#contact` |

**The four paragraphs, by argument:**

1. **Supply.** Clark County is still permitting a large number of single family homes each year,
   which is why there is real choice here and not in most metros.
   Data needed: annual single family permit count for Clark County.
   **NOT FOUND.** Source to pull: [Clark County Building and Fire Prevention permit reports](https://www.clarkcountynv.gov/)
   and the [US Census Building Permits Survey](https://www.census.gov/construction/bps/).
2. **Rates and incentives.** Builders can move the payment in ways a private seller cannot,
   because a builder has a mortgage arm and a marketing budget. No dollar figures in this
   paragraph, they live in `#incentives`.
   Data needed: current 30 year fixed average, for context only.
   **NOT FOUND.** Source to pull: [Freddie Mac Primary Mortgage Market Survey](https://www.freddiemac.com/pmms).
3. **The relocation story.** A large share of Las Vegas buyers are moving in from another state,
   and a brand new home in a brand new neighborhood is an easier landing than a 1970s resale in a
   neighborhood they have never seen. This paragraph carries blog topic 19 (California to Las
   Vegas) as an inline link.
   Data needed: net domestic migration into Clark County.
   **NOT FOUND.** Source to pull: [US Census ACS migration tables](https://www.census.gov/).
4. **Efficiency and code.** Homes built to the current Clark County code are meaningfully cheaper
   to cool than a pre-2010 house, which matters in a place where the air conditioning runs most of
   the year.
   Data needed: which code cycle Clark County is currently on, and its effective date.
   Ryan's reference file says the 2024 IBC/IRC/IECC cycle took effect January 11, 2026.
   **VERIFY-CITE** against [Clark County Building and Fire Prevention](https://www.clarkcountynv.gov/)
   before publish. Do not publish the date unverified.

**Closing line, verbatim:**

> None of that means new is automatically the right call. The honest comparison is further down
> the page, in the new versus resale section.

---

### Blocks 9 to 15 — The seven area sections

All seven follow an identical four part structure so the page reads as a system. This is the
pattern NRG uses and it is genuinely good: it makes each block scannable and it keeps the H2
outline clean, because the sub-headings are bolded lead-ins inside paragraphs, not real headings.

**The four sub-blocks, in order, every time:**

1. **What is being built here.** Two to three sentences of plain narrative.
2. **`Named communities.`** The specific master plans and villages, each linked to its own page
   where one exists.
3. **`What it costs.`** Price positioning. **Every dollar figure here is NOT FOUND until Ryan or
   a research pass supplies it.** Write the sentence structure now, fill the numbers later.
4. **`Who this area fits.`** Buyer profile. No data needed, pure editorial judgment, so this
   sub-block can be written today in full.

Each section ends with one inline link to its geo spoke page, anchor text in the form
"[Area] new construction page".

| # | Anchor | H2 (verbatim) | TOC label | WC | Key data needed | Spoke link |
|---|---|---|---|---|---|---|
| 9 | `summerlin` | **What new construction is available in Summerlin?** | Summerlin | 500 | Active villages (Stonebridge, Redpoint, Kestrel, Cloudbreak Ridge, Ascension). Village names **VERIFY** against [summerlin.com](https://www.summerlin.com/). Price bands **NOT FOUND**, source: builder "homes from" pages. | `/summerlin-new-construction` |
| 10 | `henderson` | **What new construction is available in Henderson?** | Henderson | 520 | Cadence, Inspirada, Union Village, Anthem area, Aries. Build-out status **NOT FOUND**, source: [cadencenv.com](https://www.cadencenv.com/) and [inspirada.com](https://www.inspirada.com/). Carries blog topic 14. | `/henderson-new-construction` |
| 11 | `north-las-vegas` | **What new construction is available in North Las Vegas?** | North Las Vegas | 450 | Villages at Tule Springs, Valley Vista, Vista Cielo, Sedona Ranch. Entry price point **NOT FOUND**, source: builder sites. This is the affordability section, carries blog topic 12. | `/north-las-vegas-new-construction` |
| 12 | `southwest` | **What new construction is available in Southwest Las Vegas?** | Southwest Las Vegas | 430 | Mountain's Edge build-out status, Southern Highlands, Rhodes Ranch area, the Enterprise township. Status **NOT FOUND**. | `/southwest-las-vegas-new-construction` |
| 13 | `skye-canyon` | **What new construction is available in Skye Canyon?** | Skye Canyon | 400 | Active builders and remaining phases. **NOT FOUND**, source: [skyecanyon.com](https://www.skyecanyon.com/). Skye Summit is listed in Ryan's reference file as a separate future master plan, keep the two clearly distinct. Carries blog topic 11. | `/skye-canyon-new-construction` |
| 14 | `centennial-hills` | **What new construction is available in Centennial Hills?** | Centennial Hills | 380 | Providence, Lone Mountain, Kyle Canyon area. Kyle Canyon status **NOT FOUND**, source: Clark County planning agendas. | `/centennial-hills-new-construction` |
| 15 | `lake-las-vegas` | **What new construction is available at Lake Las Vegas?** | Lake Las Vegas | 380 | Active villages, waterfront versus non-waterfront pricing. **NOT FOUND**, source: [lakelasvegas.com](https://www.lakelasvegas.com/). Note in copy that Lake Las Vegas sits inside Henderson, so buyers searching Henderson should read both sections. | `/lake-las-vegas-new-construction` |

**Sample of the finished pattern (Summerlin, sub-block 4, written in full to set the voice):**

> **Who this area fits.** Summerlin works best for buyers who want the finished version of Las
> Vegas. The parks are built, the trails connect, Downtown Summerlin is right there, and the
> schools have a track record. You pay for that. If your budget is tight and you are willing to
> wait a few years for a neighborhood to fill in, North Las Vegas and Southwest Las Vegas give
> you more house for the money today.

---

### Block 16 — Communities opening and actively selling

| Field | Value |
|---|---|
| Anchor id | `launches` |
| H2 | **Which new communities are opening in Las Vegas?** |
| TOC label | New communities |
| Type | 200 words of prose + **Table 1** |
| WC | 200 |
| Data needed | **Table 1, see §5. Almost entirely NOT FOUND at launch.** |
| CTA | "Want a heads up when a new phase releases? Send me the area you are watching." → `#contact` |

**Required lead sentence, verbatim (this is the honesty guard on a table that goes stale):**

> This table was last checked on [DATE]. New home communities open, sell out, and release new
> phases on their own schedule, so treat this as a starting point and confirm anything you are
> serious about.

---

### Block 17 — Builder comparison

| Field | Value |
|---|---|
| Anchor id | `builder-comparison` |
| H2 | **How do national and local Las Vegas builders compare?** |
| TOC label | Builder comparison |
| Type | 260 words of prose + **Table 2** |
| WC | 260 |
| Data needed | **Table 2, see §5.** |
| CTA | none, the table's builder names are the links |

Carries blog topic 15 as an inline link.

---

### Block 18 — Prices by area

| Field | Value |
|---|---|
| Anchor id | `price-by-area` |
| H2 | **How much does a new home cost in each part of Las Vegas?** |
| TOC label | Prices by area |
| Type | 260 words of prose + **Table 3** |
| WC | 260 |
| Data needed | **Table 3, see §5. Every cell NOT FOUND at launch.** |
| CTA | none |

**Required framing sentence, verbatim:**

> These are base prices, which is the number the builder puts on the sign. The price you actually
> sign for is usually higher once the lot premium and the design center are added. Read the lot
> premium section before you use these numbers to set your budget.

---

### Block 19 — New construction versus resale

| Field | Value |
|---|---|
| Anchor id | `new-vs-resale` |
| H2 | **Should you buy new construction or a resale home in Las Vegas?** |
| TOC label | New vs resale |
| Type | 250 words of prose + **Table 4** |
| WC | 250 |
| Data needed | **Table 4, see §5. This is the one table that is almost fully verifiable today.** |
| CTA | soft: "Not sure which side you land on? Send me your must-haves and I will tell you straight." → `#contact` |

Carries blog topic 3 as an inline link.

---

### Block 20 — The buying steps

| Field | Value |
|---|---|
| Anchor id | `step-by-step` |
| H2 | **How do you buy a new construction home in Las Vegas, step by step?** |
| TOC label | The buying steps |
| Type | 9 numbered steps, bolded lead-ins, real `<ol>` |
| WC | 720 |
| Data needed | none. **This block is 100 percent writable today.** |
| CTA | after step 9: "That is the whole process. If you want someone in your corner for it, start here." → `#contact` |

Use a real `<ol>` (NRG uses fake bolded lead-ins with no list markup, which is worse for
accessibility and for the HowTo schema). Each step maps 1:1 to a `HowToStep` in the schema (§8).

**The nine steps, with their headline sentences written:**

1. **Get pre-approved first.** Walk in with a lender letter. It changes what the sales office
   shows you and it protects your position if a home you want gets a second offer.
2. **Bring your agent to the very first visit.** Most builders will only recognize your agent if
   they are with you or registered on your first sign in. If you miss that, you may be on your
   own for the whole build.
3. **Tour the models, then ask for the price sheet.** The model home is fully upgraded. Ask which
   items in it are standard and which are extra, and get that in writing.
4. **Pick the lot before you pick the plan.** You can change almost everything inside the house
   later. You cannot change what is behind it.
5. **Read the purchase agreement before you sign it.** Builder contracts are written by the
   builder. Look at the delay clause, the arbitration clause, and what happens to your deposit.
   (Links to blog topic 16.)
6. **Compare the builder's lender against your own.** The builder's incentive usually requires
   their lender. Run both numbers side by side, all in, not just the rate.
7. **Go to the design center with a number in your head.** This is where budgets break. Decide
   your ceiling before you walk in. (Links to blog topic 8.)
8. **Get a pre-drywall inspection and a final inspection.** A brand new home is not a
   defect free home. Two independent inspections during the build are normal and worth it.
   (Links to blog topic 10.)
9. **Do a real walkthrough and start your warranty list.** Everything you find at walkthrough
   goes on a punch list. Year one workmanship coverage starts at closing, so document early.

---

### Block 21 — Builder incentives

| Field | Value |
|---|---|
| Anchor id | `incentives` |
| H2 | **What builder incentives can you get in Las Vegas?** |
| TOC label | Builder incentives |
| Type | 400 words of prose + **Table 5** (types, not dollar figures) |
| WC | 400 |
| Data needed | **Table 5, see §5. All dollar cells are NOT FOUND by design.** |
| CTA | "Incentives change every month. Tell me which builders you are looking at and I will check what is on the table this week." → `#contact` |

**This is the highest liability block on the page.** The prose explains the four mechanisms
(closing cost credit, rate buydown, design center credit, price reduction on standing inventory)
and how each one actually affects a payment. **It names no dollar amounts at all.** The current
numbers live in the monthly refreshed blog post (topic 1), which this section links to twice.

**Required lead paragraph, verbatim:**

> Builder incentives in Las Vegas change month to month, and they change by community inside the
> same builder. Any specific dollar figure you read on a website is out of date the week after it
> is written, including on this page. So here is what the four kinds of incentives are and how
> each one actually changes your payment. For current numbers, ask the builder directly or ask me,
> and get it in writing before you sign anything.

Carries blog topics 1, 4, and 5 as inline links.

---

### Block 22 — SID and LID assessments

| Field | Value |
|---|---|
| Anchor id | `sid-lid` |
| H2 | **What are SID and LID assessments on a Las Vegas new build?** |
| TOC label | SID and LID taxes |
| Type | prose, 4 paragraphs |
| WC | 450 |
| Data needed | definitions (writable today), typical dollar range (**NOT FOUND**), which communities carry one (**NOT FOUND**) |
| CTA | "Before you fall in love with a community, ask me to pull its assessment. It takes five minutes." → `#contact` |

**This is our biggest editorial differentiator.** NRG mentions SID and LID once, in a bullet.
It is the single most common surprise for a Las Vegas new construction buyer, and it deserves a
full anchored section. Carries blog topic 6.

**Required opening, verbatim:**

> A SID is a Special Improvement District. A LID is a Local Improvement District. They are the
> same idea with different names. When a developer builds the roads, sewers, streetlights, and
> flood control for a brand new area, somebody has to pay for that infrastructure. Often the cost
> is spread across every lot in the district and billed to the homeowner every year until it is
> paid off. It is a separate bill from your property tax and it is not part of your HOA dues.

Data to source, per cell: typical annual range and typical term.
**NOT FOUND.** Source to pull: [Clark County Assessor](https://www.clarkcountynv.gov/assessor)
special assessment lookup, and the City of Henderson LID pages. Ryan's reference file suggests a
range and a term, but that file is a compiled agent note, not a primary source, so it does not
clear the bar. Pull the real numbers from the Assessor before publishing any range.

---

### Block 23 — Warranties

| Field | Value |
|---|---|
| Anchor id | `warranties` |
| H2 | **What warranty comes with a new home in Nevada?** |
| TOC label | Warranties |
| Type | prose, 3 paragraphs |
| WC | 400 |
| Data needed | statutory structure only. **Writable today, pending citation verification.** |
| CTA | soft close to `#contact` |

Explains 1-2-10 in plain words, what "workmanship" versus "systems" versus "structural" actually
means, that the warranty is the builder's obligation and not an insurance policy, and that
extended coverage varies by builder.

**Citations required (VERIFY-CITE, do not publish unverified):**
- [Nevada Revised Statutes 624.602](https://www.leg.state.nv.us/nrs/) for the minimum one year
  builder warranty.
- [Nevada Revised Statutes Chapter 40](https://www.leg.state.nv.us/nrs/) for constructional
  defect claims and the statute of repose.
- [Nevada State Contractors Board](https://www.nvcontractorsboard.com/) for builder license
  lookup and complaint history.

Carries blog topic 18. Add one soft, high-value line: "Look your builder up on the Nevada State
Contractors Board before you sign. It is free and it takes a minute."

---

### Block 24 — Lot premiums and design center upgrades

| Field | Value |
|---|---|
| Anchor id | `lot-premiums` |
| H2 | **What is a lot premium, and is it worth paying?** |
| TOC label | Lot premiums and upgrades |
| Type | prose, 4 paragraphs |
| WC | 400 |
| Data needed | typical premium range (**NOT FOUND**), typical design center spend (**NOT FOUND**) |
| CTA | "Send me the lot map and the price sheet for the community you are looking at. I will tell you which premiums hold value and which do not." → `#contact` |

Covers: what a lot premium buys (view, size, corner, cul de sac, no rear neighbor), which
premiums tend to hold value at resale and which do not, and the separate question of design
center spend. Carries blog topics 8 and 9.

**Required honesty line, verbatim:**

> Lot premiums are set by the builder and they are rarely negotiable on a hot phase. On a slow
> phase they sometimes are. Nobody can tell you in advance which one you are in, which is exactly
> why it helps to have someone who is watching that community every week.

---

### Block 25 — Working with Ryan

| Field | Value |
|---|---|
| Anchor id | `why-ryan` |
| H2 | **Why bring your own agent to a new construction purchase?** |
| TOC label | Working with Ryan |
| Type | prose, 2 paragraphs + contact block |
| WC | 230 |
| Data needed | Ryan's license number (**NOT FOUND**), years in the Las Vegas market (**NOT FOUND**, source: Ryan). **Do not invent a transaction count or a production figure.** |
| CTA | "Send me a note. No script, no follow up campaign, just an answer." → `#contact` |

**Proposed copy, verbatim (first paragraph):**

> The person at the desk in the model home is good at their job. Their job is to sell that
> builder's homes at that builder's terms. That is not a criticism, it is just what the role is.
> A buyer's agent works for you instead, and in Nevada the builder pays that agent out of a
> budget they have already set aside. Your price does not go up because you brought someone.
> That is the part most people do not know, and it is the reason the first visit matters so much.

Second paragraph: what Ryan actually does on a new build (reads the contract, tracks the phase
releases, sits in on the design center appointment, orders the pre-drywall inspection, manages
the walkthrough punch list). All process, no claims, no numbers. Zero data risk, writable today.

Contact block: Ryan Rose · Real Broker, LLC · 702-747-5921 · ryan@rosehomeslv.com ·
rosehomeslv.com

---

### Block 26 — FAQ

| Field | Value |
|---|---|
| Anchor id | `faq` |
| H2 | **Questions Las Vegas new construction buyers ask** |
| TOC label | Questions and answers |
| Type | 15 × (`h3` question + `p` answer). **Always open. Not an accordion. No `<details>`.** |
| WC | 1,100 (15 answers at 65 to 80 words) |
| Data needed | see §6. Most answers are process based and writable today. |
| CTA | after the last answer: "Did not see your question? Send it over and I will answer it." → `#contact` |

Full question list and blog mapping in §6. Every answer is mirrored **verbatim** in the FAQPage
JSON-LD. If the visible text and the schema text ever drift apart, that is a spam signal, so they
get edited together or not at all.

---

### Block 27 — Sources and how this page is maintained

| Field | Value |
|---|---|
| Anchor id | `sources` |
| H2 | **Where the information on this page comes from** |
| TOC label | Sources |
| Type | short prose + bulleted source list |
| WC | 260 |
| Data needed | the actual list of sources used, assembled at write time |
| CTA | none |

A plain bulleted list of every organization cited on the page, each with a one line note on what
it supplies. Then a maintenance statement.

**Required maintenance statement, verbatim:**

> Anything on this page marked NOT FOUND is a number we have not verified from a primary source
> yet. We would rather show you a gap than a guess. Prices, incentives, and community status are
> checked on the date shown at the top of this page and they change often. Confirm anything you
> are relying on with the builder or with me before you make a decision.

That paragraph is doing real work. It converts our biggest weakness at launch (missing data) into
a trust signal, and it is literally true.

---

### Block 28 — Contact

| Field | Value |
|---|---|
| Anchor id | `contact` |
| H2 | **Have a question about a specific builder or community?** |
| TOC label | not in TOC (it is the target of every CTA) |
| Type | dark CTA band, 2 buttons, then the Lofty form appended below the embed |
| WC | 70 |
| Data needed | none |
| CTA | this **is** the CTA. `tel:7027475921` and `mailto:ryan@rosehomeslv.com`. |

**Proposed copy, verbatim:**

> Tell me the area, the builder, or the community you are looking at and I will send you what I
> know about it. If I do not know, I will find out and tell you where the answer came from.
>
> Ryan Rose · Real Broker, LLC · 702-747-5921 · ryan@rosehomeslv.com

**Critical build note:** `#contact` must be the id on this band, and the page JS rewrites all
`href="#contact"` clicks to scroll to the **bottom of the document**, which is where Lofty
appends its own form block. Do not put a `<form>` element in the embed. Lofty will not ingest it.

---

### Block 29 — Fair housing and disclosure

| Field | Value |
|---|---|
| Anchor id | none |
| H2 | none |
| TOC label | not in TOC |
| Type | small print aside |
| WC | 100 |
| Data needed | Ryan's license number (**NOT FOUND**) |
| CTA | none |

Equal Housing Opportunity statement, brokerage identification (Real Broker, LLC), a line that
listing information is deemed reliable but not guaranteed, and a line that builder pricing,
incentives, availability, and plans change without notice.

---

### Block 30 — Read next

| Field | Value |
|---|---|
| Anchor id | `read-next` |
| H2 | **More on buying new in Las Vegas** |
| TOC label | not in TOC |
| Type | 3 blog cards, hand picked, not automated |
| WC | 130 |
| Data needed | the 3 posts must exist. **At launch, likely 0 of 3 exist. See §10.** |
| CTA | the cards |

Hand pick 3. Do not automate this. NRG ships the identical "related reading" block on all 173
posts, which is a wasted signal. Recommended first three once written: blog topic 1 (incentives
roundup), topic 2 (do you need a realtor), topic 6 (SID and LID).

---

### Word count roll-up

| Block group | Words |
|---|---|
| Hero, direct answer, meta, TOC, pill row (blocks 1 to 5) | 472 |
| Listings slot (block 6) | 230 |
| Builder grid (block 7) | 1,050 |
| Why new (block 8) | 560 |
| Seven area sections (blocks 9 to 15) | 3,060 |
| Four table sections (blocks 16 to 19) | 970 |
| Buying steps (block 20) | 720 |
| Incentives (block 21) | 400 |
| SID and LID, warranties, lot premiums (blocks 22 to 24) | 1,250 |
| Working with Ryan (block 25) | 230 |
| FAQ (block 26) | 1,100 |
| Sources, contact, disclosure, read next (blocks 27 to 30) | 560 |
| **Total editorial** | **~10,600** |

Table cell text and IDX card text sit on top of that and are not counted.

---

## 2. Hero spec

### H1

> **New Construction Homes in Las Vegas**

Exactly one H1 on the page. Do not add a year to the H1. Years go in the meta title and in the
`Updated` date, where they can be changed without touching the on-page heading that is earning
the ranking.

### Subhead

> Everything you need to know about buying a brand new home in the Las Vegas valley. Who is
> building where, what it really costs once you add it all up, and the steps in order.

### Stat bar

NRG's stat line is one `<p>` of middot separated tokens, not a grid. Copy that, it is cheap and
it reads well. **But every token has to be defensible.**

**Ship this version at launch. All four tokens are self-verifiable, so nothing on the page's most
prominent line can be wrong:**

> 20 builders covered · 7 valley areas · Updated [Month Year] · About a 30 minute read

| Token | Value | Source | Status |
|---|---|---|---|
| Builder count | 20 | Count of builder cards in block 7 and builder pages we publish. Self-verifiable. | **VERIFIED by construction** |
| Area count | 7 | Count of geo sections and geo spoke pages. Self-verifiable. | **VERIFIED by construction** |
| Updated | [Month Year] | Must match `dateModified` in Article schema and the byline strip. | **Set at publish** |
| Read time | About 30 minutes | Word count divided by 225 wpm, computed at publish. | **Compute at publish** |

**Do not ship this version until the data exists.** It is the more persuasive line, and it is
what NRG runs, but three of its four tokens are unverified:

> [X]+ active communities · 20 builders · $[LOW] to $[HIGH] · Updated [Month Year]

| Token | Status | Source to pull |
|---|---|---|
| Active community count | **NOT FOUND** | Count across the 20 builder research files in `Rose Homes LV/Content/New-Construction/New Construction Full Communities/`. Those files were compiled May 1 2026 and are stale. Re-pull from each builder's own Las Vegas page, or from newhomesource.com Las Vegas area, before using a number. |
| Low price | **NOT FOUND** | Lowest "homes from" figure across the 20 builders' own Las Vegas pages. |
| High price | **NOT FOUND** | Highest published figure among the luxury and custom builders. Custom builders often publish no ceiling, in which case use the highest published number and write "and up", never an invented ceiling. |

**Do not copy NRG's community count or price band.** They are NRG's research, they are unsourced
from our side, and using them would be presenting someone else's unverified numbers as our own.

### CTA buttons

Three, in this order:

| Label | Target | Style intent |
|---|---|---|
| See Homes For Sale | `#listings` | primary |
| Browse the Builders | `#builders` | secondary |
| Ask Ryan a Question | `#contact` | secondary |

No phone number in the hero. NRG runs "Call (702) 637-1759" as a hero button. That is a harder
push than Ryan's voice. The phone number appears in the contact band, in the disclosure, and in
the mobile sticky bar, which is plenty.

### Mobile sticky bar (below 1024px)

Three buttons, mirroring the desktop trade: on desktop you get the fixed TOC rail, on mobile you
get this bar.

| Label | Target |
|---|---|
| Call | `tel:7027475921` |
| Text | `sms:7027475921` |
| Ask a Question | `#contact` |

---

## 3. The listings slot

### Placement

**Immediately after the "New Construction by Area" pill row and before the builder grid.**
That is block 6, anchor `#listings`.

Reasoning: the head query "new construction homes las vegas" has mixed intent. Roughly half of
those searchers want to browse homes and half want to understand the process. Putting live
listings above the 10,000 words of editorial serves the browsers immediately, and the TOC gives
the researchers a one click path past it. This mirrors NRG's placement, which is the one thing
about their hub that is unambiguously correct.

### Static wrapper copy (ships either way, IDX or fallback)

**Eyebrow:** `Las Vegas MLS · New construction only`

**H2:** New Construction Homes For Sale in Las Vegas Right Now

**Lede, verbatim:**

> These are new construction homes currently for sale in the Las Vegas valley. The feed is
> filtered to Clark County only, and to homes built recently or still being built. If you have
> seen other Las Vegas new construction pages showing 1970s houses and homes in Pahrump, that is
> a filter problem, not a market. This one is scoped on purpose.

That paragraph is the competitive pitch, delivered without naming anyone. It is verifiably true
about our own feed as long as we actually set the filter correctly, and the QA file documents
that the competitor's flagship feed is 58 percent Pahrump listings with homes back to 1960. **Do
not name NRG on the page. Do not cite the QA finding on the page.** It is internal.

**Method note, verbatim (fill the bracket at build time):**

> Filtered to Clark County, single family and townhome, [FILTER DESCRIPTION FROM THE LOFTY SEARCH
> WE ACTUALLY BUILD]. Updated [FREQUENCY, NOT FOUND, depends on Lofty]. Homes sell and come back
> on the market daily, so if something is gone, ask and I will tell you what replaced it.

**Attribution line, verbatim:**

> Listing information comes from the Las Vegas MLS through Lofty. Whether a specific home is a
> spec, a model, or a quick move in varies, and current incentives vary by community. Confirm
> with the builder's sales office or with me before you tour. Information is deemed reliable but
> is not guaranteed.

### Path A — Lofty IDX renders inline

Drop the Lofty embed into a `<ul class="listing-grid">` shaped slot between the header block and
the attribution line. Keep the eyebrow, H2, lede, method note, and attribution as static HTML
around it, because those are the credibility elements and they are ours regardless of what the
embed does.

Grid target: 1 column below 500px, 2 columns at 500px, 3 at 800px, 4 at 1700px. Cards 4:3 image.
Whatever the Lofty embed renders is what we get, so this is guidance for the design agent on slot
sizing only.

**Requires from Ryan: the IDX embed snippet. Currently BLOCKED.**

### Path B — Fallback, IDX cannot render inline

If Lofty IDX will not render inside an HTML embed, the section becomes a static featured
communities grid plus one prominent button into a pre-filtered Lofty search. Visually equivalent,
zero live data, zero MLS cost.

**Six to nine cards, one per featured community.** Card fields:

| Field | Source | Status |
|---|---|---|
| Community name | our own geo research | writable |
| Builder or builders | `New Construction Full Communities/*.md` | **VERIFY**, files are dated May 1 2026 |
| Area | our own | writable |
| "Homes from" | builder's own site | **NOT FOUND** |
| One line description | editorial | writable |
| Photo | Ryan's photography, or the builder's press kit with permission | **NOT FOUND**, see §10 |
| Link | the community's own page on rosehomeslv.com, or the geo spoke if no community page exists | writable |

**Fallback header copy replaces only the lede. Verbatim:**

> Here are new construction communities selling in the Las Vegas valley right now. Each one links
> to a page with the builders, the floor plans, and what is actually available. To see every new
> construction listing on the Las Vegas MLS, use the search below.

**Fallback CTA button, verbatim label:** `See every new construction listing`
**Target:** pre-filtered Lofty search URL. **NOT FOUND.** Source: Ryan builds the saved search in
Lofty and sends the URL.

**Fallback note under the button, verbatim:**

> That search is filtered to Clark County new construction. It updates from the Las Vegas MLS.

---

## 4. Builder grid

### The 20 builders

Sourced from Ryan's own research files in
`/Users/ryanrose/Downloads/Claude/Rose Homes LV/Content/New-Construction/New Construction Full Communities/`,
cross checked against the competitor's 20 builder pages. Every builder below has a research file
in that folder **except Shea Homes**, which is flagged.

Tier assignment drives the filter chips. **Tier is provisional on every row** and must be
confirmed from each builder's own Las Vegas "homes from" page before launch, because tier is
derived from price and price is `NOT FOUND`.

| # | Builder | Provisional tier | Builder page slug | Ryan research file | Communities in that file (May 1 2026, STALE, re-verify) |
|---|---|---|---|---|---|
| 1 | Lennar | Mid | `/lennar-las-vegas` | yes | 42 |
| 2 | D.R. Horton | Entry | `/dr-horton-las-vegas` | yes | 13 |
| 3 | KB Home | Mid | `/kb-home-las-vegas` | yes | 27 |
| 4 | Pulte and Del Webb | Mid | `/pulte-del-webb-las-vegas` | yes | 17 |
| 5 | Toll Brothers | Luxury | `/toll-brothers-las-vegas` | yes | 14 |
| 6 | Taylor Morrison | Mid | `/taylor-morrison-las-vegas` | yes | 11 |
| 7 | Richmond American | Mid | `/richmond-american-las-vegas` | yes | 27 |
| 8 | Tri Pointe Homes | Mid | `/tri-pointe-las-vegas` | yes | 9 |
| 9 | Century Communities | Entry | `/century-communities-las-vegas` | yes | 16 |
| 10 | Beazer Homes | Mid | `/beazer-homes-las-vegas` | yes | 17 to 19, file itself is ambiguous |
| 11 | Woodside Homes | Mid | `/woodside-homes-las-vegas` | yes | 6 |
| 12 | Meritage Homes | Mid | `/meritage-homes-las-vegas` | yes | 1 |
| 13 | LGI Homes | Entry | `/lgi-homes-las-vegas` | yes | 5 |
| 14 | Shea Homes | Mid | `/shea-homes-las-vegas` | **NO FILE. Needs a full research pass.** | **NOT FOUND** |
| 15 | Harmony Homes | Entry | `/harmony-homes-las-vegas` | yes | 2 |
| 16 | Touchstone Living | Entry | `/touchstone-living-las-vegas` | yes | 3 |
| 17 | StoryBook Homes | Entry | `/storybook-homes-las-vegas` | yes | 5 |
| 18 | Signature Homes | Mid | `/signature-homes-las-vegas` | yes | 6 |
| 19 | Blue Heron | Custom | `/blue-heron-las-vegas` | yes | 12 |
| 20 | Christopher Homes | Custom | `/christopher-homes-las-vegas` | yes | 3 |

**Community counts above are row counts from files compiled May 1 2026, which is roughly three
months stale as of this writing.** Do not publish any of them without a re-pull. They are listed
here only so the research pass knows where to start and what to diff against.

**Under the grid, one line of text (writable today, no data risk):**

> Several smaller local builders also build in Clark County, including Brooks Home, Edward Homes,
> Landon Miller Homes, Pinnacle Homes, and Trust Home Builders. If you are looking at one of
> them, send me the community and I will pull what I have.

Research files exist for all five of those in the same folder, so that sentence is supportable.

### What each builder card shows

| Field | Content | Source | Verification status |
|---|---|---|---|
| Logo | builder logo SVG or PNG | **NOT FOUND.** Builder press kits or media pages. Check each builder's brand usage terms. `builder-brand-colors.md` in the new-construction skill has palettes but not logo files. | **BLOCKED, see §10** |
| Builder name | e.g. "Lennar" | ours | verified |
| Parent or public company line | e.g. "Lennar Corporation (NYSE: LEN)" | builder investor relations page | **VERIFY per builder** |
| Stat pill 1: price from | e.g. "Homes from $X" | builder's own Las Vegas page | **NOT FOUND on all 20** |
| Stat pill 2: community count | e.g. "N communities in Clark County" | re-pull, see table above | **NOT FOUND on all 20** |
| Stat pill 3: years in Las Vegas | e.g. "20+ years in Las Vegas" | builder's own about page or Nevada State Contractors Board license date | **NOT FOUND on all 20** |
| One line on what they are known for | ~25 words, editorial, no numbers | ours | **writable today for all 20** |
| Area tags | e.g. "Henderson", "North Las Vegas" | derived from the community research files | **VERIFY with the count re-pull** |
| Link | "See [Builder] communities" → builder page slug | ours | writable, but the destination page must exist |

**Card copy sample, written in full to set the voice (D.R. Horton):**

> America's largest homebuilder by volume. Their Express Homes line is where a lot of Las Vegas
> first time buyers start, and they build heavily in North Las Vegas and around Cadence.

No numbers, no superlatives beyond a verifiable one ("largest by volume", which is a published
industry fact and gets a citation to Builder Magazine's Builder 100 or to D.R. Horton's own
investor page).

### Filter chips

Five pill buttons above the grid. Counts in the labels are **counts of our own cards**, so they
are self-verifying and safe.

| Chip | Label | Cards |
|---|---|---|
| all | All (20) | 20 |
| entry | Entry (6) | D.R. Horton, Century Communities, LGI, Harmony, Touchstone, StoryBook |
| mid | Mid (10) | Lennar, KB Home, Pulte and Del Webb, Taylor Morrison, Richmond American, Tri Pointe, Beazer, Woodside, Meritage, Shea, Signature |
| luxury | Luxury (1) | Toll Brothers |
| custom | Custom (2) | Blue Heron, Christopher Homes |

**Flag:** the mid list above has 11 names, not 10. That is deliberate and it is the exact problem
to resolve at build time. Tier assignment is downstream of price, and price is `NOT FOUND` on all
20 builders. **Do not publish the chips with counts until the price pull is done and every
builder is assigned a tier from a real "homes from" figure.** Until then, either ship the grid
with no chips, or ship chips with no counts in the labels.

**Tier definitions to publish next to the chips (so the classification is transparent):**
- Entry: most floor plans start under $450,000
- Mid: most floor plans start between $450,000 and $800,000
- Luxury: most floor plans start above $800,000
- Custom: you bring or choose the lot and the plan is designed for you

Those thresholds are our editorial definition, stated as such. That is honest. What is not honest
is calling a builder "entry level" with no published price behind it.

### Fields that need verification, consolidated

Every one of these is a per builder research task, 20 rows deep:

1. Price from figure (20 cells, all `NOT FOUND`)
2. Clark County community count (20 cells, all stale or `NOT FOUND`)
3. Years active in Las Vegas (20 cells, all `NOT FOUND`)
4. Parent company and ticker (20 cells, `VERIFY`)
5. Logo file and usage rights (20 files, all `NOT FOUND`)
6. Tier assignment (20 cells, all provisional)
7. Areas built (20 cells, derived, `VERIFY`)
8. Shea Homes has no research file at all

**That is 140 cells plus 20 logo files.** It is the largest single data task in the build.

---

## 5. The five data tables

Every table gets a real `<caption>`. Captions are an accessibility win and they are the highest
density quotable surface for AI search. Every table gets a `Source:` line underneath in the
standard citation format, and a "Checked [DATE]" note.

### Table 1 — Communities opening and actively selling (`#launches`)

**Caption:** New construction communities in the Las Vegas valley, checked [DATE]. Builder,
area, and status.

**Columns:** `Community | Builder | Area | Homes from | Status`

Row set: 12 communities, chosen to cover all 7 geo areas and all 4 price tiers, so the table
doubles as an area sampler.

| # | Community | Builder | Area | Homes from | Status | Source to check |
|---|---|---|---|---|---|---|
| 1 | Cadence | multiple | Henderson | NOT FOUND | NOT FOUND | cadencenv.com |
| 2 | Inspirada | multiple | Henderson | NOT FOUND | NOT FOUND | inspirada.com |
| 3 | Union Village area | NOT FOUND | Henderson | NOT FOUND | NOT FOUND | Ryan has a Union Village folder in `Content/New-Construction/the-townes-at-union-village` |
| 4 | Stonebridge | multiple | Summerlin | NOT FOUND | NOT FOUND | summerlin.com |
| 5 | Redpoint | multiple | Summerlin | NOT FOUND | NOT FOUND | summerlin.com |
| 6 | Kestrel | multiple | Summerlin | NOT FOUND | NOT FOUND | summerlin.com |
| 7 | Villages at Tule Springs | multiple | North Las Vegas | NOT FOUND | NOT FOUND | builder sites, D.R. Horton file lists Heartland series here |
| 8 | Valley Vista | multiple | North Las Vegas | NOT FOUND | NOT FOUND | builder sites |
| 9 | Vista Cielo | Harmony Homes | North Las Vegas | NOT FOUND | NOT FOUND | harmonyhomes.com |
| 10 | Skye Canyon | multiple | Skye Canyon | NOT FOUND | NOT FOUND | skyecanyon.com |
| 11 | Providence | multiple | Centennial Hills | NOT FOUND | NOT FOUND | builder sites |
| 12 | Lake Las Vegas villages | multiple | Lake Las Vegas | NOT FOUND | NOT FOUND | lakelasvegas.com |

**Verified cells: 24 of 60** (Community, Builder where named, and Area columns are editorial
identification, not market data). **NOT FOUND cells: 36 of 60.**

**Do not publish this table until at least the Status column is filled.** A launches table with
an empty Status column has no reason to exist. If Status cannot be sourced in time, cut Table 1
from v1 and ship the section as prose pointing at the 7 geo spokes.

---

### Table 2 — Builder comparison (`#builder-comparison`)

**Caption:** How Las Vegas home builders compare, checked [DATE]. Company type, price level,
what you can change, and design center approach.

**Columns:** `Builder | Type | Price level | How much you can change | Design approach`

Row set: 8 builders, chosen to span the full spectrum rather than to be exhaustive. The full 20
live in the grid above, this table exists to explain the **categories**.

| Builder | Type | Price level | How much you can change | Design approach | Status |
|---|---|---|---|---|---|
| Lennar | National, high volume | NOT FOUND | Limited, options come as a package | "Everything's Included" model, VERIFY on lennar.com | 2 of 4 data cells NOT FOUND |
| D.R. Horton | National, entry focused | NOT FOUND | Limited, mostly standard selections | VERIFY on drhorton.com | 2 of 4 NOT FOUND |
| KB Home | National, build to order | NOT FOUND | High for a national builder | Design studio, VERIFY on kbhome.com | 2 of 4 NOT FOUND |
| Pulte and Del Webb | National, plus 55+ brand | NOT FOUND | Moderate, structural options offered | VERIFY on pulte.com | 2 of 4 NOT FOUND |
| Toll Brothers | National luxury | NOT FOUND | High | Full design studio, VERIFY on tollbrothers.com | 2 of 4 NOT FOUND |
| Richmond American | National, design forward | NOT FOUND | Moderate to high | Home gallery, VERIFY on richmondamerican.com | 2 of 4 NOT FOUND |
| Touchstone Living | Local, entry focused | NOT FOUND | Limited | VERIFY on touchstoneliving.com | 2 of 4 NOT FOUND |
| Blue Heron | Local, custom and luxury | NOT FOUND | Full custom | VERIFY on blueheron.com | 2 of 4 NOT FOUND |

**Verified cells: 16 of 40** (Builder and Type columns are editorial classification, defensible).
**NOT FOUND or VERIFY cells: 24 of 40.**

**Column choice note:** NRG's version of this table has a "Communities" column and a "Warranty"
column. We drop both on purpose. Community counts go stale monthly and the warranty column would
read "1/2/10" on every row, because that is the statutory Nevada minimum, which makes it a
useless column that implies a difference that does not exist. "How much you can change" is a
better column, it is the thing buyers actually differ on, and it is verifiable from each
builder's own site.

---

### Table 3 — Prices by area (`#price-by-area`)

**Caption:** Las Vegas new construction base prices by area, checked [DATE]. Entry, mid, and
upper price levels.

**Columns:** `Area | Entry | Mid | Upper | Most active builders`

| Area | Entry | Mid | Upper | Most active builders | Source to check |
|---|---|---|---|---|---|
| Summerlin | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | summerlin.com builder list + each builder's Summerlin page |
| Henderson | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | cadencenv.com, inspirada.com, builder sites |
| North Las Vegas | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | builder sites |
| Southwest Las Vegas | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | builder sites |
| Skye Canyon | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | skyecanyon.com |
| Centennial Hills | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | builder sites |
| Lake Las Vegas | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | lakelasvegas.com |

**Verified cells: 7 of 35** (the Area column only). **NOT FOUND cells: 28 of 35.**

This is the emptiest table in the set and it is also the one buyers most want. It is a **hard
blocker for v1**. Two options:

- **Option A, preferred:** do the price pull. It is 20 builder sites, roughly 2 hours, and it
  fills Table 2, Table 3, the builder grid price pills, and the aggressive hero stat bar all at
  once. Highest leverage data task in the build.
- **Option B:** ship the section as prose that ranks the seven areas from least to most expensive
  **without dollar figures**, which is defensible from general knowledge and is genuinely useful,
  and add the table in v2. Relative ranking is a claim we can stand behind. Absolute numbers are
  not.

---

### Table 4 — New construction versus resale (`#new-vs-resale`)

**Caption:** New construction compared with a resale home in Las Vegas, across the eight things
buyers ask about most.

**Columns:** `What you are comparing | New construction | Resale`

**This is the only table that is essentially fully writable today**, because every cell is a
structural statement about how the two purchase types work, not a market figure.

| What you are comparing | New construction | Resale | Status |
|---|---|---|---|
| Price per square foot | Usually higher than a comparable resale | Usually lower | **VERIFY the direction with a GLVAR figure before publishing any percentage. State the direction only, no percentage, if unverified.** |
| Choosing your finishes | You pick at the design center before it is built | You renovate after you close | verified structural |
| Warranty | Nevada 1-2-10 applies | None, unless a warranty transfers | **VERIFY-CITE:** NRS 624.602 |
| Energy efficiency | Built to the current Clark County code | Depends entirely on the age of the house | verified structural |
| Landscaping and trees | New, and it takes years to fill in | Established | verified structural |
| HOA | Brand new, so there is no financial history to review | Years of budgets and reserves you can read | verified structural |
| Property tax in year one | Often based on land only at first, then it resets | Already reflects the improved value | **VERIFY-CITE:** Clark County Assessor |
| SID or LID assessment | Common in newer master plans | Less common in older neighborhoods | **VERIFY-CITE:** Clark County Assessor |
| How long until you move in | Months, if it is being built for you | Weeks | verified structural |
| Negotiating | Builders protect base price, they give on incentives instead | Price itself is negotiable | verified structural |

Ten rows, not eight. **Verified cells: 16 of 20 content cells.** **VERIFY-CITE cells: 4 of 20.**
**NOT FOUND: 0**, as long as we do not put a percentage in row 1.

**Build this table first.** It is the proof that the page can be substantive without any of the
blocked data, and it is the one most likely to win a featured snippet.

---

### Table 5 — Builder incentive types (`#incentives`)

**This table is deliberately restructured away from NRG's version.** Theirs is a per-builder grid
of dollar ranges ("$10K to $25K closing cost credit") for twelve builders. That data goes stale
within weeks, we cannot source it, and publishing a wrong incentive figure under a licensed
agent's name is a real liability. **We do not build that table.**

Instead:

**Caption:** The four kinds of builder incentive in Las Vegas, what each one does to your
payment, and what to ask for.

**Columns:** `Incentive type | What it actually does | What to ask the builder | Usual catch`

| Incentive type | What it actually does | What to ask the builder | Usual catch | Status |
|---|---|---|---|---|
| Closing cost credit | Lowers the cash you bring to closing. Does not lower your loan or your payment. | "What is the credit, in dollars, and can it be applied to prepaids?" | Usually requires their lender to get the full amount | **all 4 cells writable today** |
| Rate buydown | Lowers your interest rate, either for the first year or two, or for the life of the loan. | "Is this temporary or permanent, and what is the rate in year three?" | A temporary buydown ends. Budget for the rate it resets to. | **all 4 cells writable today** |
| Design center credit | Money you can spend on upgrades. It is not cash and it does not reduce the price. | "What is the credit and does it cover structural options or only finishes?" | Often finish only, and often it expires at a set date | **all 4 cells writable today** |
| Price reduction on standing inventory | An actual cut to the price of a finished or nearly finished home. | "Is this price cut on the base or on the as built price?" | Only available on homes already built, so you take the finishes as they are | **all 4 cells writable today** |

**Verified cells: 16 of 16. NOT FOUND: 0.** Every cell is a structural explanation of a mechanism,
not a market figure.

**Directly under the table, verbatim:**

> This page does not publish current incentive dollar amounts, because they change every month
> and by community. For this month's numbers, read the incentives roundup on the blog, or send me
> the builders you are looking at and I will check.

Then two links: to blog topic 1 (`/blog/las-vegas-new-construction-incentives`, monthly refresh,
same slug forever, bump `dateModified`) and to `#contact`.

**This is the single most important structural decision in the blueprint.** It converts the
page's biggest liability into its most durable section. The mechanism table never goes stale.

### Table verification roll-up

| Table | Content cells | Verified or writable | VERIFY-CITE | NOT FOUND |
|---|---|---|---|---|
| 1 — Communities | 60 | 24 | 0 | **36** |
| 2 — Builder comparison | 40 | 16 | 0 | **24** |
| 3 — Prices by area | 35 | 7 | 0 | **28** |
| 4 — New vs resale | 20 | 16 | 4 | **0** |
| 5 — Incentive types | 16 | 16 | 0 | **0** |
| **Total** | **171** | **79** | **4** | **88** |

**88 of 171 table cells come back NOT FOUND.** Add the builder grid (140 cells, 20 logo files),
the hero's optional stat tokens (3), and the assorted in-prose figures, and the total unverified
data surface for the page is roughly **235 items**.

---

## 6. FAQ block

**Format:** always open. `<h3>` question, `<p>` answer. **No accordion, no `<details>`, no
toggle JS.** Reasons: the text is in the DOM and visible to every crawler without interaction, it
matches the FAQPage schema exactly, and it is one less thing to break inside a Lofty embed.

**Length:** 15 questions, answers 65 to 80 words each. Each answer opens with a direct answer in
the first sentence, then supports it. Each answer ends either with a concrete next step or a soft
invitation, never with a hard push.

### The 15 questions, verbatim

1. **Do I need my own agent to buy a new construction home in Las Vegas?**
2. **Is new construction or a resale home the better buy in Las Vegas right now?**
3. **What builder incentives can I get in Las Vegas?**
4. **How does a builder rate buydown actually work?**
5. **What are SID and LID assessments on a Las Vegas new build?**
6. **Why does my property tax bill go up in the second year on a new home?**
7. **How much should I budget for design center upgrades?**
8. **What is a lot premium, and can I negotiate it?**
9. **Do I still need a home inspection on a brand new house?**
10. **Where can I find the most affordable new homes in the Las Vegas valley?**
11. **Which Las Vegas home builder should I choose?**
12. **What should I try to negotiate in a builder's contract?**
13. **How long does it take to build a home in Las Vegas?**
14. **What does the Nevada 1-2-10 home warranty actually cover?**
15. **Can I put grass in the yard of a new Las Vegas home?**

### Sample answers, written in full to set length and voice

**Q1 answer, verbatim:**

> Yes, and it costs you nothing. In Nevada the builder sets aside a co-op commission whether you
> bring an agent or not, so your price is the same either way. The catch is timing. Most builders
> only recognize your agent if they come with you or are registered on your very first visit. If
> you tour alone first, you may not be able to add representation later. So bring your agent to
> visit number one, even if you are only looking.

**Q5 answer, verbatim:**

> A SID is a Special Improvement District and a LID is a Local Improvement District. They are the
> same idea. When a developer builds the roads, sewers, and drainage for a brand new area, that
> cost gets spread across the lots and billed to each homeowner every year until it is paid off.
> It arrives as a separate bill from your property taxes and it can run for many years. Ask for
> the exact yearly amount and the payoff date in writing before you sign anything.

**Q9 answer, verbatim:**

> Yes. A brand new house is not a defect free house, and the county inspector is checking code
> compliance, not your interests. Two independent inspections are normal on a new build. A
> pre-drywall inspection while the framing, wiring, and plumbing are still visible, and a full
> inspection before your final walkthrough. Anything found goes on the builder's punch list while
> your year one workmanship coverage is still fresh.

### The FAQ to blog topic mapping

This is the editorial calendar. **Every FAQ answer is the 70 word version. Every blog post is the
1,500 to 2,500 word version, and it links back to `/new-construction#faq`.** That is the entire
spider web mechanic, and it is the highest leverage finding in the whole research set.

| FAQ # | Blog topic # | Blog post title | Proposed slug (`/blog/…`) | Exists? |
|---|---|---|---|---|
| 1 | 2 | Do You Need a Realtor for New Construction in Las Vegas? | `do-you-need-realtor-new-construction-las-vegas` | **Ryan's reference file lists this slug as already published. VERIFY, then update rather than duplicate.** |
| 2 | 3 | New Construction vs Resale in Las Vegas: The Real Comparison | `new-construction-vs-resale-homes-las-vegas` | **Listed as published. VERIFY and update.** |
| 3 | 1 | Las Vegas New Construction Incentives: [Month] Roundup | `builder-incentives-las-vegas-2026` | **Listed as published. Convert to the monthly refresh post, keep the slug forever.** |
| 4 | 5 | How a 2-1 Buydown Works on a Las Vegas New Build | `2-1-buydown-las-vegas-new-construction` | no |
| 5 | 6 | SID and LID Assessments on Las Vegas New Builds | `sid-lid-taxes-explained-las-vegas-new-construction` | **Listed as published. VERIFY and update.** |
| 6 | 7 | Property Taxes on a Las Vegas New Build: Year One vs Year Two | `new-construction-property-tax-year-two-las-vegas` | no |
| 7 | 8 | Design Center Budgeting for Las Vegas New Build Buyers | `most-valuable-upgrades-las-vegas-new-construction` | **Listed as published. VERIFY, may need a new post for budgeting specifically.** |
| 8 | 9 | Lot Premiums in Las Vegas New Construction: What to Pay For | `lot-premiums-las-vegas-new-construction` | no |
| 9 | 10 | Pre-Drywall Inspection on a Las Vegas New Build | `home-inspection-new-home-las-vegas` | **Listed as published. VERIFY and update.** |
| 10 | 12 | New Homes Under $450K in North Las Vegas | `north-las-vegas-new-construction-under-450k` | no |
| 11 | 15 | Las Vegas Home Builders Compared | `top-home-builders-las-vegas-2026` | **Listed as published. VERIFY and update.** |
| 12 | 16 | Builder Contract Clauses Las Vegas Buyers Should Negotiate | `builder-contract-clauses-las-vegas` | no |
| 13 | 17 | How Long Does It Take to Build a Home in Las Vegas? | `new-construction-timeline-las-vegas` | no |
| 14 | 18 | Nevada New Home Warranty: What 1-2-10 Covers | `nevada-new-home-warranty-1-2-10` | no |
| 15 | 20 | HOA Landscape Rules on Las Vegas New Builds | `hoa-landscape-rules-las-vegas-new-construction` | no |

**The 5 remaining blog topics map to page sections, not to FAQs:**

| Blog topic # | Title | Maps to |
|---|---|---|
| 4 | Builder Closing Cost Credits: What They Actually Save You | section `#incentives`, Table 5 row 1 |
| 11 | Skye Canyon New Homes: Builders, Prices, and What Is Left | section `#skye-canyon` + spoke `/skye-canyon-new-construction` |
| 13 | Summerlin West New Villages Compared | section `#summerlin` + spoke `/summerlin-new-construction` |
| 14 | Cadence Henderson: Build-Out Status and What Is Still Selling | section `#henderson` + spoke `/henderson-new-construction` |
| 19 | Moving From California to a Las Vegas New Build | section `#why-new`, paragraph 3 |

**Duplicate content warning:** Ryan's `new-construction-reference.md` lists 13 slugs as already
published on rosehomeslv.com, and 6 of them overlap with this calendar. **Check each one before
writing.** Update and expand the existing post, keep the existing slug, and bump `dateModified`.
Do not publish a second post on the same topic. NRG has three near duplicate new versus resale
posts competing with each other, and that is a mistake worth not repeating.

---

## 7. Internal link web

Every outbound link from this hub, with its anchor text and destination slug. Anchor text is
descriptive and varied, never "click here", and never the bare slug.

### 7a. Geo spokes (7 destinations, 21 links)

Each spoke gets **three** links from the hub: the pill row, the end of its own area section, and
the Prices by Area table row. Three contextual links from a 10,000 word hub is a strong signal
without looking manufactured.

| Destination slug | Anchor text (pill) | Anchor text (section close) | Anchor text (table) | Exists? |
|---|---|---|---|---|
| `/summerlin-new-construction` | Summerlin | Summerlin new construction page | Summerlin | **no** |
| `/henderson-new-construction` | Henderson | Henderson new construction page | Henderson | **no** |
| `/north-las-vegas-new-construction` | North Las Vegas | North Las Vegas new construction page | North Las Vegas | **no** |
| `/southwest-las-vegas-new-construction` | Southwest Las Vegas | Southwest Las Vegas new construction page | Southwest Las Vegas | **no** |
| `/skye-canyon-new-construction` | Skye Canyon | Skye Canyon new construction page | Skye Canyon | **no** |
| `/centennial-hills-new-construction` | Centennial Hills | Centennial Hills new construction page | Centennial Hills | **no** |
| `/lake-las-vegas-new-construction` | Lake Las Vegas | Lake Las Vegas new construction page | Lake Las Vegas | **no** |

**All 7 geo spokes are net new.** Until they exist, those links 404. **Do not ship the hub with
21 broken links.** Two acceptable interim states: build the 7 spokes first (they are template
work once the hub sets the pattern), or ship v1 with the pill row and section closes pointing at
`#` anchors on the hub itself, then swap in the real slugs when the spokes go live.

### 7b. Builder pages (20 destinations, 22 links)

Each builder gets one link from its card. Two builders get a second link from Table 2.

| Destination slug | Anchor text | Exists? |
|---|---|---|
| `/lennar-las-vegas` | See Lennar communities | **no** |
| `/dr-horton-las-vegas` | See D.R. Horton communities | **no** |
| `/kb-home-las-vegas` | See KB Home communities | **no** |
| `/pulte-del-webb-las-vegas` | See Pulte and Del Webb communities | **no** |
| `/toll-brothers-las-vegas` | See Toll Brothers communities | **no** |
| `/taylor-morrison-las-vegas` | See Taylor Morrison communities | **no** |
| `/richmond-american-las-vegas` | See Richmond American communities | **no** |
| `/tri-pointe-las-vegas` | See Tri Pointe communities | **no** |
| `/century-communities-las-vegas` | See Century Communities communities | **no** |
| `/beazer-homes-las-vegas` | See Beazer communities | **no** |
| `/woodside-homes-las-vegas` | See Woodside communities | **no** |
| `/meritage-homes-las-vegas` | See Meritage communities | **no** |
| `/lgi-homes-las-vegas` | See LGI communities | **no** |
| `/shea-homes-las-vegas` | See Shea Homes communities | **no** |
| `/harmony-homes-las-vegas` | See Harmony Homes communities | **no** |
| `/touchstone-living-las-vegas` | See Touchstone Living communities | **no** |
| `/storybook-homes-las-vegas` | See StoryBook communities | **no** |
| `/signature-homes-las-vegas` | See Signature Homes communities | **no** |
| `/blue-heron-las-vegas` | See Blue Heron homes | **no** |
| `/christopher-homes-las-vegas` | See Christopher Homes homes | **no** |

**All 20 builder pages are net new.** Good news from the QA file: builder pages carry **no MLS
grid at all**, so they are not blocked on the Lofty IDX question and can be built in parallel
with everything else.

### 7c. Blog posts (15 destinations, 24 links)

Placed contextually inside the section that covers the same topic, at roughly one blog link per
450 words of body copy. Anchor text is the natural phrase, never the post title verbatim.

| Destination | Anchor text | Placed in | Exists? |
|---|---|---|---|
| `/blog/builder-incentives-las-vegas-2026` | this month's incentive roundup | `#incentives` (×2), FAQ 3 | **verify, listed as published** |
| `/blog/do-you-need-realtor-new-construction-las-vegas` | why the first visit matters | `#step-by-step` step 2, `#why-ryan`, FAQ 1 | **verify, listed as published** |
| `/blog/new-construction-vs-resale-homes-las-vegas` | the full comparison | `#new-vs-resale`, FAQ 2 | **verify, listed as published** |
| `/blog/sid-lid-taxes-explained-las-vegas-new-construction` | how SID and LID assessments work | `#sid-lid`, FAQ 5 | **verify, listed as published** |
| `/blog/home-inspection-new-home-las-vegas` | what a pre-drywall inspection catches | `#step-by-step` step 8, FAQ 9 | **verify, listed as published** |
| `/blog/most-valuable-upgrades-las-vegas-new-construction` | which upgrades hold their value | `#lot-premiums`, FAQ 7 | **verify, listed as published** |
| `/blog/top-home-builders-las-vegas-2026` | the builders compared side by side | `#builder-comparison`, FAQ 11 | **verify, listed as published** |
| `/blog/new-construction-homes-cost-las-vegas-2026` | what a new home really costs here | `#price-by-area` | **verify, listed as published** |
| `/blog/hidden-costs-new-construction-las-vegas` | the costs that are not on the price sheet | `#lot-premiums` | **verify, listed as published** |
| `/blog/moving-california-las-vegas-new-construction` | moving here from California | `#why-new` paragraph 3 | **verify, listed as published** |
| `/blog/2-1-buydown-las-vegas-new-construction` | how a buydown works | FAQ 4 | **no** |
| `/blog/lot-premiums-las-vegas-new-construction` | how lot premiums are priced | `#lot-premiums`, FAQ 8 | **no** |
| `/blog/nevada-new-home-warranty-1-2-10` | what the warranty covers | `#warranties`, FAQ 14 | **no** |
| `/blog/builder-contract-clauses-las-vegas` | the clauses worth pushing on | `#step-by-step` step 5, FAQ 12 | **no** |
| `/blog/new-construction-timeline-las-vegas` | how long a build actually takes | FAQ 13 | **no** |

**10 of 15 are listed as already published in `new-construction-reference.md` but none have been
verified live.** First job: load rosehomeslv.com and confirm each slug returns 200. Any that 404
gets removed from the link plan until the post exists.

### 7d. Conversion destinations

| Destination | Anchor text | Placed in | Notes |
|---|---|---|---|
| `#contact` | varies by section, see the per-block CTA column | 14 sections | The single conversion target. Scrolls to the Lofty form below the embed. |
| `tel:7027475921` | 702-747-5921 | `#contact` band, disclosure, mobile bar | |
| `mailto:ryan@rosehomeslv.com` | ryan@rosehomeslv.com | `#contact` band, disclosure | |
| Lofty pre-filtered new construction search | See every new construction listing | `#listings` | **URL NOT FOUND, blocked on Ryan** |
| `https://www.rosehomeslv.com/` | Home | breadcrumb | exists |

**CTA rhythm:** one `#contact` CTA roughly every two sections, which reproduces NRG's conversion
cadence without an inline form. 14 CTAs across 30 blocks.

### 7e. Outbound authority links (target: 12 or more)

Every one opens in a new tab with `rel="noopener noreferrer"`, and the anchor text is the
organization's name, not the URL.

Clark County Assessor · Clark County Building and Fire Prevention · Nevada Department of Taxation
· Nevada State Contractors Board · Nevada Revised Statutes (NRS 624 and NRS Chapter 40) · Nevada
Real Estate Division · Southern Nevada Water Authority · Las Vegas REALTORS (GLVAR) · US Census
Bureau · Freddie Mac PMMS · Clark County School District · plus each builder's own Las Vegas page
from inside the builder cards.

### 7f. Link summary

| Group | Destinations | Links from hub | Exist today |
|---|---|---|---|
| Geo spokes | 7 | 21 | **0 of 7** |
| Builder pages | 20 | 22 | **0 of 20** |
| Blog posts | 15 | 24 | **10 claimed, 0 verified** |
| Conversion | 5 | 18 | 3 of 5 |
| Outbound authority | 12+ | 12+ | n/a |
| **Total internal** | **47** | **85** | **at most 10, unverified** |

---

## 8. Schema and JSON-LD plan

Six blocks, emitted together near the bottom of the embed, each in its own
`<script type="application/ld+json">`. Keep them separate rather than using `@graph`, because a
single malformed block then only breaks itself.

### Block 1 — BreadcrumbList
Two `ListItem`s. Position 1: "Home", `https://www.rosehomeslv.com/`. Position 2: "New
Construction", the canonical hub URL. Must match the visible breadcrumb exactly.

### Block 2 — Article
The editorial half of the page.

| Property | Value |
|---|---|
| `headline` | New Construction Homes in Las Vegas: 20 Builders and 7 Areas |
| `description` | matches the meta description |
| `datePublished` / `dateModified` | real ISO dates, `dateModified` must match the visible Updated date |
| `author` | `Person`, name "Ryan Rose", `url` rosehomeslv.com about page, `hasCredential` → Nevada license, **number NOT FOUND** |
| `author.knowsAbout` | ["Las Vegas new construction", "Clark County home builders", "New home buyer representation", "Master-planned communities in Southern Nevada"] |
| `publisher` | `Organization`, name "Rose Homes LV", logo `ImageObject` |
| `image` | the hero image, 1200×630 |
| `mainEntityOfPage` | `WebPage`, the canonical URL |
| `speakable` | `SpeakableSpecification`, `cssSelector: [".direct-answer", ".key-takeaways", ".faq-answer"]` |

The `speakable` property is the single highest value line in the whole schema plan. It is an
explicit answer engine play and it costs nothing.

### Block 3 — FAQPage
`mainEntity`: 15 × `Question` with `acceptedAnswer` `Answer`. **The `text` of each answer must be
byte identical to the visible `<p>`.** Any divergence is a spam signal.

### Block 4 — ItemList (builders)
`numberOfItems: 20`. Each `ListItem` has `position` and an `item` of type `Organization` with
`name`, `url` (our builder page slug), `sameAs` (the builder's own website), and `areaServed` as
`City` values. **Omit `image` until we actually have licensed logo files.** Do not point `image`
at a hotlinked logo.

### Block 5 — HowTo
| Property | Value |
|---|---|
| `name` | How to buy a new construction home in Las Vegas |
| `totalTime` | **NOT FOUND.** NRG publishes `P90D`. Do not copy it. Either omit the property or set it after the build timeline research (blog topic 17) gives a defensible figure. |
| `supply` | `HowToSupply` × 2: a mortgage pre-approval, and buyer agent representation registered on the first visit |
| `step` | **9 × `HowToStep`**, each with `name`, `text`, and `url` = `<canonical>#step-by-step`. Mirrors block 20 exactly, 1:1. |

### Block 6 — RealEstateAgent
| Property | Value |
|---|---|
| `@id` | `<canonical>#realestateagent` |
| `name` | Ryan Rose |
| `url` | https://www.rosehomeslv.com/ |
| `telephone` | +17027475921 |
| `email` | ryan@rosehomeslv.com |
| `address` | `PostalAddress`. **NOT FOUND.** Real Broker LLC Nevada branch address, source: Ryan. |
| `areaServed` | `City` × 5: Las Vegas, Henderson, North Las Vegas, Summerlin, Boulder City |
| `hasCredential` | Nevada real estate license. **Number NOT FOUND**, source: Ryan or red.nv.gov |
| `parentOrganization` | `Organization`, Real Broker, LLC |
| `aggregateRating` | **OMIT.** NRG publishes a 4.9 from 9,061 reviews. We have no verified review corpus, and a fabricated `aggregateRating` is a Google manual action risk. Add it only if Ryan has a real, countable review source. |
| `priceRange` | **OMIT.** Meaningless for an agent and often flagged. |

### What we deliberately do not emit

- **`CollectionPage`.** NRG doubles `CollectionPage` and `Article` on one URL. Skip it unless the
  Lofty IDX actually renders inline. If it does, add `CollectionPage` in v2.
- **`ItemList` of `RealEstateListing`.** Only meaningful if we control the listing markup. Inside
  a Lofty IDX embed we do not.
- **`aggregateRating` anywhere on the page.**

---

## 9. SEO package

| Element | Value | Length |
|---|---|---|
| **Slug** | `/new-construction` | |
| **Canonical** | `https://www.rosehomeslv.com/new-construction` (match Lofty's actual trailing slash behavior, **VERIFY**) | |
| **Meta title** | `New Construction Homes Las Vegas \| 20 Builders 2026` | 51 |
| **Meta description** | `New construction in Summerlin, Henderson, North Las Vegas and more. 20 builders, 7 areas, real prices, and the buying steps in order. Ask Ryan Rose anything.` | 156 |
| **H1** | `New Construction Homes in Las Vegas` | |
| **OG title** | `New Construction Homes in Las Vegas` | |
| **OG description** | `Who is building where, what it really costs once you add lot premiums and SID assessments, and the steps in order. A plain English guide from Ryan Rose.` | 153 |
| **OG image** | 1200×630, the hero photo. **NOT FOUND**, see §10. | |
| **Twitter card** | `summary_large_image`, same image | |
| **robots** | `index, follow, max-image-preview:large, max-snippet:-1` | |

**Meta description is 156 characters, which is 6 over the usual 150 truncation point.** Trim to
`New construction in Summerlin, Henderson, North Las Vegas and more. 20 builders, 7 areas, and
the buying steps in order. Ask Ryan Rose anything.` (147) if a shorter version is wanted. Both
are supplied so Ryan can pick.

### Keywords

**Primary:** `new construction homes las vegas`

**Secondary, in priority order:**
1. `las vegas new construction`
2. `new homes las vegas`
3. `las vegas home builders`
4. `new build homes las vegas`
5. `new construction homes henderson nv`
6. `new construction summerlin`
7. `north las vegas new construction`
8. `las vegas new home builders list`

**Question keywords the H2s are built to capture** (each is a real H2 on the page, phrased as the
query):
- who is building new homes in las vegas
- why do so many las vegas buyers choose new construction
- what new construction is available in summerlin / henderson / north las vegas / southwest las
  vegas / skye canyon / centennial hills / lake las vegas
- how do national and local las vegas builders compare
- how much does a new home cost in each part of las vegas
- should you buy new construction or a resale home in las vegas
- how do you buy a new construction home in las vegas step by step
- what builder incentives can you get in las vegas
- what are sid and lid assessments on a las vegas new build
- what warranty comes with a new home in nevada
- what is a lot premium and is it worth paying
- why bring your own agent to a new construction purchase

**Do not create a separate `/las-vegas-new-construction` page.** NRG deliberately has no
`/las-vegas/new-construction/` (it 404s) because the city term belongs to the root hub. That is a
correct decision and we copy it. One page owns the head term.

---

## 10. Build order, and what is blocked

### Writable today, with zero input from Ryan

Roughly **5,600 of the 10,600 words**, and 2 of the 5 tables.

| Block | Words |
|---|---|
| Hero, with the self-verifiable stat bar | 45 |
| Direct answer and key takeaways | 290 |
| TOC and pill row | 115 |
| Listings slot, all static wrapper copy, both paths | 230 |
| Builder grid intro and all 20 card descriptions (words only, no data pills) | 650 |
| All 7 area sections, sub-blocks 1 and 4 (narrative and buyer fit) | 1,400 |
| New vs resale, prose and **Table 4 complete** | 250 |
| The 9 buying steps, complete | 720 |
| Incentives prose and **Table 5 complete** | 400 |
| SID and LID, definitions and process | 450 |
| Warranties, structure and process | 400 |
| Lot premiums and upgrades, prose | 400 |
| Working with Ryan | 230 |
| All 15 FAQ answers | 1,100 |
| Sources statement, contact band, disclosure | 430 |
| **Total** | **~7,100** |

**Recommendation: write all of it now.** The page is substantive and publishable at 7,100 words
with visible `NOT FOUND` cells and an honest sources statement. That is a better v1 than waiting
three weeks for a complete data set, and the `NOT FOUND` cells create their own pressure to
finish.

### Blocked on data research (no Ryan input needed, just hours)

| Task | Effort | Unblocks |
|---|---|---|
| **Builder price pull.** Visit all 20 builders' Las Vegas pages, record "homes from", community count, areas, years active, parent company. | ~3 hours | Builder grid (140 cells), Table 2, Table 3, filter chip tiers, the aggressive hero stat bar. **Highest leverage task in the build.** |
| **Master plan status pull.** cadencenv.com, inspirada.com, summerlin.com, skyecanyon.com, lakelasvegas.com. | ~2 hours | Table 1, and sub-block 2 and 3 of all 7 area sections |
| **Statutory citation pass.** Pull live URLs for NRS 624.602, NRS Chapter 40, Clark County Assessor, Nevada Dept of Taxation, SNWA turf rules, Clark County code cycle. | ~1 hour | 4 VERIFY-CITE cells in Table 4, the warranty section, key takeaways 3, 5, and 6, the SID and LID section |
| **Blog slug audit.** Load all 13 slugs from `new-construction-reference.md` and record which return 200. | ~30 min | 24 of the 85 internal links |
| **Shea Homes research file.** The only builder in the 20 with no file. | ~30 min | 1 builder card, 1 builder page |

### Blocked on Ryan, hard

These cannot be resolved by research. **They are the ask.**

1. **The Lofty IDX embed snippet, or a decision to use the fallback.** Either the embed code, or
   the URL of an existing Lofty page of his that renders IDX inside an HTML embed, or a
   confirmation that it is not possible. If it is not possible, we also need the **pre-filtered
   Lofty search URL** for the fallback button. This is the single biggest unknown in the entire
   build and it has been open since file 08.
2. **The Lofty CSS test.** Publish a throwaway Lofty page with a 20 line embed containing a
   `position: fixed` box and a `:has()` rule, and look at it. Ten minutes. If Lofty wraps embeds
   in a container with `transform`, `filter`, or `contain`, `position: fixed` silently anchors to
   the wrapper instead of the viewport and the entire TOC rail design has to change to
   `position: sticky` inside a two column grid, which changes the page skeleton. **Do this before
   the design agent writes any CSS.**
3. **Ryan's Nevada real estate license number**, and Real Broker LLC's Nevada branch address.
   Needed in five places: the byline, the fair housing disclosure, the Article schema
   `hasCredential`, the RealEstateAgent schema `address`, and the warranty section's "look your
   builder up" credibility parallel.
4. **Photography.** One hero image at 1200×630 or larger, plus 6 to 9 community photos if we go
   the fallback route on listings, plus 20 builder logo files with usage rights confirmed. **Do
   not hotlink builder logos and do not use a stock photo of a house that is not in Las Vegas.**
5. **Slug confirmation.** Confirm Lofty accepts `/new-construction` and the flat spoke pattern,
   and confirm whether it forces a trailing slash. Slugs are painful to change after indexing.

### Recommended build sequence

| Phase | Work | Why |
|---|---|---|
| **0** | The 10 minute Lofty CSS test | It can invalidate the page skeleton. Do it first. |
| **1** | Write the 7,100 writable words. Ship Table 4 and Table 5 complete. Builder grid with no data pills and no chip counts. Listings slot with the fallback copy in place. | Gets a real, honest, publishable page standing. |
| **2** | Builder price pull (3 hrs) + statutory citation pass (1 hr) | Fills the grid, Table 2, Table 3, the tiers, and every VERIFY-CITE. Page goes from 7,100 to ~9,500 words of substantiated content. |
| **3** | Master plan status pull (2 hrs) | Fills Table 1 and area sub-blocks 2 and 3. Page reaches ~10,600. |
| **4** | Swap in the Lofty IDX embed or lock the fallback | Whenever Ryan unblocks it. Nothing else waits on this. |
| **5** | Build the 20 builder pages | **Not blocked on IDX.** They carry no MLS grid at all. Template work once the hub sets the pattern. |
| **6** | Build the 7 geo spokes | Turns 21 broken links into 21 real ones. |
| **7** | Write the 5 net new blog posts, update the 10 existing ones | Completes the FAQ to blog mapping and closes the spider web. |

### The one thing nobody has checked

There is **no traffic or ranking data anywhere in this research set.** We are reverse engineering
a 2,129 page competitor on the assumption that their hub actually ranks. Before committing to the
20 builder pages and 7 geo spokes in phases 5 and 6, one Ahrefs or Semrush pull on
`nevadarealestategroup.com/new-construction/` either validates the whole program or reveals we
are copying an expensive page that ranks for nothing. **It does not block the hub.** It does block
the decision to build 27 more pages behind it.

---

*Written 2026-07-25. Sources: `01-hub-page-teardown.md` (structure), `00-master-sitemap-architecture.md`
(link architecture), `05-blog-cluster.md` §5 (the 20 blog topics), `07-qa-verification.md`
(authoritative corrections, trusted over conflicting files), `08-lofty-porting-constraints.md`
(Lofty constraints), workspace `CLAUDE.md` and `blog-writer/content-rules.md` (content rules),
and Ryan's own `Content/New-Construction/New Construction Full Communities/` research files
(builder inventory, compiled May 1 2026 and now stale).*
