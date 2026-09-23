# Claude Design prompt — New Construction hub page

Copy everything below the line into Claude Design. It is self-contained. The copy is final, so Claude Design only handles layout and visual design.

---

Design a landing page for a Las Vegas real estate agent. I am giving you the finished copy. **Do not rewrite it, do not add sections, and do not add any facts, numbers, prices, timelines, or claims that are not in this brief.** Your job is layout, hierarchy, and visual craft only.

## Where this page lives (this constrains the build)

It gets pasted as a raw HTML block into a **Lofty (Chime) hosted real estate CRM website**. That means:

- **One self-contained HTML file.** All CSS in a single inline `<style>` block. No Tailwind CDN, no external stylesheets, no external fonts, no JS libraries, no build step.
- **Every selector must be scoped** under a single wrapper class `.rhlv-nc` so nothing leaks into or fights the host theme. No bare `body`, `h1`, `p`, or `*` selectors outside that scope.
- The host page already has a header, nav, and footer. **Do not build a nav bar or a site footer.** Start at the hero, end at the closing CTA.
- Interactive bits must work with **zero JavaScript**. Use `<details>/<summary>` for the FAQ accordion.
- Images: use `https://placehold.co/WIDTHxHEIGHT` placeholders with descriptive `alt` text. I will swap in real photos. Do not pull in stock photos of homes, since they would misrepresent actual listings.

## Brand tokens (pulled from the live site, use these exactly)

```
Deep teal (primary, headings)   #0c4a57
Teal body text                  #1e616f
Muted teal-gray (secondary)     #688389
Warm tan (CTA / accent)         #d99e6a
Button text                     #ffffff
Page background                 #ffffff
```

Buttons on the live site are **fully pill-shaped, 25px border radius**, white text on the tan. Keep that. The live font stack is `"font-normal", "Arimo", system-ui` for body and `"font-title", "font-bold", "Arimo", system-ui` for headings. Those first names are the host's own font aliases, so reference them exactly and let them fall through to Arimo and system fonts.

Do not introduce a new brand color. You can derive tints and shades from the four above.

## What I want visually

The current version is technically correct and completely flat. It reads like a document, not a page. Make it feel like a premium but warm real estate brand: editorial, confident, lots of breathing room, real visual rhythm between sections instead of one continuous column of text.

Specifically:
- Give the hero real presence. Right now it is a headline and a paragraph on a pale gradient.
- Break the wall-of-text sections up. Vary the layout section to section, do not stack six identical centered text blocks.
- The "new build vs resale" comparison should read as a genuine side-by-side, not two bulleted lists in boxes.
- The community grid should feel browsable and inviting.
- Layered, color-tinted shadows at low opacity. Never a flat gray `box-shadow`.
- A clear surface layering system: page base, elevated card, floating element. Not everything on the same plane.
- Tight letter-spacing (about `-0.03em`) on large headings, generous line-height (about `1.7`) on body copy.
- Every clickable element needs hover, `focus-visible`, and active states. Animate only `transform` and `opacity`. Never `transition-all`.
- Mobile-first and fully responsive. Wide content must never cause horizontal page scroll.
- Respect `prefers-reduced-motion`.

## Hard rules

- **Exactly one `<h1>` on the page.** Everything else is `h2`/`h3`.
- **No em dashes or en dashes anywhere.** Use commas, periods, or "and". This is a firm brand rule.
- The FAQ question and answer text must be **present as real visible HTML text**, not hidden, not injected by script. Collapsed in an accordion is fine.
- Reading level around 6th grade. Do not "elevate" the copy. No words like "premier", "exclusive", "unparalleled", "curated".
- Do not add testimonials, statistics, awards, badges, logos, counters, or team members. I only have the one review below.

---

# THE COPY (use verbatim)

**Page title:** New Construction Homes Las Vegas | Ryan Rose
**Meta description:** Buying a new build in Las Vegas? Ryan Rose represents you, not the builder. Communities, incentives, and what to know before you visit a model home.

## Hero

Eyebrow: NEW CONSTRUCTION

H1: New Construction Homes in Las Vegas

Subhead: The agent in the model home works for the builder. I work for you. If you are thinking about a new build anywhere in the Las Vegas valley, let's talk before you tour your first community, because that first visit decides whether you get to have representation at all.

Primary button: Call or Text 702-747-5921 → `tel:+17027475921`
Secondary button: See Where They're Building → anchor to the communities section

Trust line: ★★★★★ · 5.0 from 5 Google reviews · Ryan Rose, Realtor with Real Broker, LLC

## Section: Why you want your own agent on a new build

Intro: This is the part most buyers get wrong. The friendly person at the sales desk is paid by the builder and represents the builder in your contract. That is not a criticism of them, it is their job. It just means nobody in that room is looking out for you unless you bring them.

Four numbered points:

1. **The contract is the builder's** — Builder purchase agreements are written by the builder's attorneys and are very different from a standard resale contract. I read them with you and flag what actually matters.
2. **Upgrades are where budgets die** — The design center is designed to be exciting. Some upgrades hold value at resale and some do not. I will tell you which is which before you sign, not after.
3. **Incentives move, base prices don't** — Builders protect the base price because it sets the comps for the whole community. The real negotiation happens in incentives, and knowing that changes how you ask.
4. **Someone has to watch the build** — Walkthroughs, punch lists, delays, and the final inspection all need a second set of eyes. I stay on it so you are not chasing the superintendent yourself.

(Note: the "—" characters above are separators for your reading only. Do not put them in the HTML.)

## Section: Read this before you visit a model home

This is the most important section on the page. Give it visual weight.

Paragraph 1: Most Las Vegas builders require your agent to register you or walk in with you on your **first** visit to that community. If you tour alone and sign the visitor sheet, many builders will not let you add an agent to that community afterward. It is the single most common and most avoidable mistake in new construction.

Paragraph 2: Two minutes of planning protects you. Send me the communities you want to see and I will register you correctly, confirm each builder's rules, and either meet you there or make sure you are covered before you walk in. Already toured somewhere? Tell me which ones and I will check where you still stand.

Button: Get Registered Before You Tour → `tel:+17027475921`

## Section: New build or resale?

Intro: There is no universally right answer. It comes down to your timeline, your budget, and how much you want the home to be exactly yours. Here is the honest trade-off.

**New construction**
- Nobody has lived in it, and everything is under builder warranty
- You choose the floor plan, lot, finishes, and layout
- Built to current energy and building standards
- Builder incentives can offset rate and closing costs
- You may wait months, and quick move-in homes are limited
- Landscaping, window coverings, and upgrades are usually extra
- The neighborhood is still filling in around you

**Resale**
- Move in on a normal escrow timeline instead of a build schedule
- Yard, window coverings, and upgrades are often already done
- You can see the actual neighborhood, traffic, and neighbors
- More room to negotiate on price and on repairs
- Older systems and roof, with no builder warranty
- You inherit someone else's finish choices
- You compete with other buyers on the good ones

Closing line: Plenty of my buyers start out certain about one and end up choosing the other once they see both in person. I am happy to show you a couple of each so you are deciding from real information instead of a guess.

## Section: Where they're building in the valley

Give this section the id `rhlv-nc-communities` so the hero button can anchor to it.

Intro: New home construction is spread across the valley, and each area has a different feel, commute, and price range. These are the areas with active new home building right now.

| Community | Description | Link |
|---|---|---|
| Summerlin | Master planned, west valley, Red Rock views | `/summerlin` |
| Henderson | Cadence, Inspirada, and the southeast valley | `/henderson` |
| Skye Canyon | Northwest, newer, trail and park focused | **no link yet** |
| Centennial Hills | Northwest, established with new pockets | **no link yet** |
| Mountain's Edge | Southwest, mountain views, family heavy | **no link yet** |
| North Las Vegas | Some of the most attainable new pricing | **no link yet** |

**Important:** only the first two are links. The other four pages do not exist yet, so render them as non-clickable cards, and make it visually obvious which ones are clickable and which are not. Leave an HTML comment explaining how I convert each one to a link later.

Closing line: Not sure which area fits your commute and budget? Tell me where you work and what you want to spend, and I will narrow it to two or three communities worth your Saturday.

## Section: About builder incentives

Paragraph 1: Incentives are how builders compete without cutting the base price. In Las Vegas they usually show up as an interest rate buydown through the builder's own lender, a closing cost credit, or design center dollars toward upgrades.

Paragraph 2: The important thing to understand is that they change constantly. What a community offers this month may be gone next month, and a builder carrying finished inventory will be far more generous than one selling from a waitlist. Anything you read online about current incentives is probably already out of date.

Paragraph 3: I track what is actually being offered right now, community by community. Ask me before you assume a deal is or is not available.

Button: Ask About Current Incentives → `tel:+17027475921`

## Section: Review

Quote: "Ryan was critical in negotiating on our behalf and keeping us up to date, and I was confident that I didn't need to check in constantly to make sure things were getting done when they needed to be."

Attribution: Kevin Rich, Google review

## Section: New construction questions, answered

FAQ accordion, nine items. First one open by default.

**Do I need my own agent to buy new construction in Las Vegas?**
You are not required to have one, but the agent sitting in the model home works for the builder. They are paid by the builder and represent the builder's interests in the contract. A buyer's agent represents you. Most new home communities in Las Vegas have budgeted for a buyer's agent, and I will confirm the exact terms with you in writing before you register.

**When do I need to bring my agent to a new home community?**
On your very first visit. Most Las Vegas builders require your agent to accompany you or register you at the time of your first tour. If you walk in alone and sign in, many builders will not allow you to add representation later on that community. If you have already visited a community, tell me which ones so I can check the registration rules before you go further.

**Is it better to buy new construction or a resale home in Las Vegas?**
It depends on your timeline, your budget, and how much you want to customize. New construction gives you a home nobody has lived in, a builder warranty, and current building standards, but you may wait months and pay for upgrades and landscaping. Resale gets you in faster, often with mature landscaping and window coverings already done, in an established neighborhood. I can walk you through the trade-offs for your specific situation.

**Which Las Vegas areas have the most new construction?**
Skye Canyon and Centennial Hills in the northwest, Summerlin in the west, Mountain's Edge and Southern Highlands in the southwest, Cadence and Inspirada in Henderson, and several communities across North Las Vegas all have active new home construction.

**What are builder incentives?**
Incentives are promotions builders use to move inventory. Common ones in Las Vegas include interest rate buydowns through the builder's own lender, closing cost credits, and design center allowances. They change often, sometimes month to month, and they vary by community and by how much standing inventory a builder is carrying. I track current incentives and can tell you what is being offered right now.

**Are new construction prices negotiable?**
Builders rarely cut the base price, because a recorded lower sale price affects the appraisals and values of every other home in the community. They are usually more flexible on incentives instead, such as upgrades, closing costs, or a rate buydown. Knowing where a builder will and will not move is a large part of what a buyer's agent does on a new build.

**Do I still need a home inspection on a brand new home?**
Yes. New homes are built by people, and inspectors regularly find items worth correcting while the builder warranty is fresh and the fixes are still the builder's responsibility. I recommend an independent inspection before your final walkthrough, separate from any municipal inspection.

**Do I have to use the builder's lender?**
In most cases you can use any lender you choose. Builders often attach their best incentives to their in house or preferred lender, so the real question is whether the incentive is worth more than what an outside lender can offer on rate and fees. I can help you compare both side by side before you commit.

**How long does it take to build a new home in Las Vegas?**
It depends entirely on the builder, the community, and whether you are buying a home to be built or a quick move-in home that is already under way. Quick move-in homes can close in weeks. A home started from dirt takes considerably longer. I will get the current build timeline from the specific community you are considering rather than give you a general estimate.

## Closing CTA

Heading: Thinking about a new build?

Body: Send me the communities on your list. I will check each builder's registration rules, tell you what they are offering right now, and make sure you are represented before you ever sit down at a sales desk. No pressure, and no cost to talk it through.

Primary button: Call or Text 702-747-5921 → `tel:+17027475921`
Secondary button: Email Ryan → `mailto:ryan@rosehomeslv.com`

Contact block:
Ryan Rose, Realtor | Real Broker, LLC
9580 W Sahara Ave Ste 200, Las Vegas, NV 89117
702-747-5921 | ryan@rosehomeslv.com

---

## Deliver

One HTML file. Wrap the pasteable region in `<!-- BEGIN PASTE -->` and `<!-- END PASTE -->` comment markers so I know exactly what to copy into the CRM. Everything inside those markers must be self-contained and safe to drop into an existing page.
