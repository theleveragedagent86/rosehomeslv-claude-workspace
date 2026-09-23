# Weekly Seller Update System: Plan-Mode Build Prompt

> **The Leveraged Agent, Claude Code Course for Realtors, Level 5 attachment.**
>
> **How to use this file:**
> 1. Open Claude Code **inside your Business Brain folder** (the one you built in Level 1).
> 2. Switch to **Plan Mode** (press Shift+Tab until the bottom of the screen says "plan mode").
> 3. Paste this entire file and hit Enter.
> 4. Answer Claude's questions. Have your listing address, seller email, and portal logins handy.
> 5. Read the plan it gives you. Approve it. Claude builds the whole system.
>
> After that, every week is one command: `/weekly-update [address]`.
>
> This was reverse-engineered from a real listing, Ryan's 29 Amber Rock St in Henderson, NV: 5 weekly reports and 5 seller emails over 30 days on market. Where you see `e.g.`, that is what Ryan's answer was, so you can see what a good answer looks like. Your answers will be different. Seller names and contact details from that listing were left out on purpose.

---

## INSTRUCTIONS TO CLAUDE (read all of this before doing anything)

You are in plan mode, working inside the user's Business Brain folder. Your job is to build a **done-for-you weekly seller update system** for a real estate listing, stored inside that folder so it gets smarter every week. The finished system, run once a week, produces:

1. A branded, self-contained **HTML seller report** (executive summary, online views by platform, showings summary, listing activities).
2. A **paste-ready copy** of that report for the agent's CRM landing page (raw HTML, images embedded as base64).
3. A **seller email draft** (a Gmail draft if the Gmail connector is live, otherwise paste-ready text) to the seller with a short summary, the report link, and nearby competing listings.
4. Updated **tracking files** (platform links, view history, showing log, feedback log) so next week is faster.

**Rules for this session:**

- **Do not write or edit any file until the user approves your plan.** Plan mode is read-only. Reading, searching, and asking questions are fine.
- **Interview first. Never guess.** Every value below marked `ASK` must come from the user or from a file the user points you to. If the user does not know, record it as `NOT FOUND` and plan a way to find it. Never invent prices, view counts, showing counts, offer amounts, or feedback.
- **Ask in rounds**, using the AskUserQuestion tool for multiple-choice items (max 4 questions per call, 2 to 4 options each) and plain chat for free-text items (addresses, emails, URLs, file paths). Group related questions. Do not dump 60 questions at once.
- **Before asking, look.** Run Phase 0 discovery first. If a value already exists in a file, show it and ask the user to confirm instead of asking from scratch.
- After each round, echo back a short table of what you captured so the user can correct it.
- **No em dashes (—) anywhere** in anything you generate: report, email, summaries, file names. Use commas, periods, or colons.
- **Fair housing.** Write about the property and the activity, never about who lives there, who should buy it, or why the seller is selling. If buyer feedback contains a comment about the occupants or a protected class, leave it out of the report and flag it to the user.
- **Respect the Business Brain.** Follow the user's `CLAUDE.md` (BROKER), especially the KEEP OUT and ESCALATION blocks. Reuse what earlier levels already built instead of re-asking.
- The final plan must list every file you will create, every tool/connector you will use, and every step of the weekly run, with nothing left as "TBD." Anything unresolved becomes an explicit open item with an owner.

---

## PHASE 0: Discovery (do this silently before the first question)

Search the working directory and report what you found in one short list:

- The Business Brain `CLAUDE.md` (BROKER). Pull the agent name, brokerage, market, and any KEEP OUT rules from it.
- Your voice profile and writing rules (Level 4), client roster (Level 4), brand file or design tokens such as `brand.md` (Level 8), and the landing page setup (Level 2), if they exist yet.
- A `listings/` folder and a folder for this property inside it (look for the street number + street name in folder names).
- Listing photos, especially a hero/exterior shot.
- Any existing `platform-links.json`, `Showings.md`, `feedback.md`, mailing list spreadsheet (`.xlsx`/`.csv`), Meta ad creatives, reverse prospecting CSVs, past `Weekly Reports/`.
- An existing report template (`report-template.html`, `seller-report-template.html`) or a `weekly-update` skill in `~/.claude/skills/`.
- An agent headshot image.
- Which connectors/tools are live in this session: Gmail, Claude in Chrome, iMessage, calendar, scheduled tasks. List what is missing.

Then start Round 1.

---

## PHASE 1: The Interview

Ask every item below. Items marked **(first run only)** are saved to a config file and never asked again. Items marked **(every week)** become the short weekly questionnaire the finished system asks.

### Round 1: The agent and brand (first run only)

| # | Ask | Why it matters | e.g. |
|---|-----|----------------|------|
| 1.1 | Your name exactly as it should appear on the report | Header, sticky bar, sign-off | Ryan Rose |
| 1.2 | Brokerage name | Footer / compliance | Real Broker, LLC |
| 1.3 | Phone, email, website | Optional contact block | (your own) |
| 1.4 | Path to your headshot (transparent or square works best) | Embedded as base64 in the header circle | `brand/headshot.png` |
| 1.5 | Logo file, if you want it on the report (yes/no + path) | Optional header element | none used |
| 1.6 | Brand colors: use your brand file from Level 8 if it exists, the default "Beacon" palette, or your own hex codes? | Report theme | Navy `#10133B`, accent blue `#3B82F6`, highlight `#DBEAFE`, off-white `#FAF9F5` |
| 1.7 | Fonts: default (DM Sans headings, Inter body) or your own? | Report typography | default |
| 1.8 | Does your brokerage or state require a disclaimer or license # on client-facing material? Paste it. (Level 9 covers this in depth.) | Compliance | NOT FOUND, ask your broker |
| 1.9 | Email sign-off style: "Best," / "Sincerely," / "Talk soon," / custom. Name only, or name + title + phone? | Email close | "Best," then "Ryan Rose", nothing else |
| 1.10 | Writing rules: reading level, words to never use, banned punctuation. (Pull from your Level 4 voice profile if it exists.) | Voice | 6th-grade level, no em dashes, no "premier" |
| 1.11 | Do you use an email tracker (Mailsuite, Streak, etc.)? | Plan notes whether the tracker footer is added automatically | Mailsuite |

### Round 2: The listing (first run only, update if anything changes)

| # | Ask | Why | e.g. |
|---|-----|-----|------|
| 2.1 | Full property address | Everything | 29 Amber Rock St, Henderson, NV 89012 |
| 2.2 | How to split it for the hero headline (line 1 / line 2) | Hero H1 | "29 Amber Rock St," / "Henderson, NV 89012" |
| 2.3 | MLS number | Portal searches, showing service lookup | 2759238 |
| 2.4 | Current list price, original list price, and every price change with date | DOM and positioning language. Never shown as "reduce" advice | $485,000 |
| 2.5 | Date the listing went live on MLS (and Coming Soon date if different) | Days on market math | Mar 11, 2026 is first showing |
| 2.6 | Beds / baths / sqft / lot / year built / garage | Context for summary | NOT FOUND in files, ask |
| 2.7 | Top 3 selling points you want reinforced every week | Positives in showings summary | layout, lot size, 3-car garage |
| 2.8 | Known objections or quirks (solar lease, HOA, condition, estate sale, tenant) and the exact facts you tell buyers | Keeps summary accurate | Solar PPA, year 7 of 20, transferable, under $100/mo summer bills |
| 2.9 | Path to the listing folder (or should I create one in `listings/`?) | Where everything saves | `listings/29 Amber Rock St/` |
| 2.10 | Which photo is the hero image? (show the user 3 candidates if photos exist) | Report hero | `Listing Photos/hero_email.jpg` |
| 2.11 | Current status: Active / Coming Soon / Active Under Contract / Pending | Decides which report version to run | Active |

### Round 3: The seller (first run only)

| # | Ask | Why | e.g. |
|---|-----|-----|------|
| 3.1 | Seller legal name(s) as on the listing agreement | Records | (on file) |
| 3.2 | **What name do they actually go by?** (can differ from legal name) | Greeting. The 29 Amber Rock seller's legal name and greeting name were different | "Hi [nickname]," |
| 3.3 | Seller email(s). One seller or two? Both on To, or one To + one CC? | Email routing | single recipient |
| 3.4 | Anyone else to CC (co-listing agent, assistant, attorney, family member)? | Email routing | none |
| 3.5 | Day and time the update should go out | Schedule | Fridays, evening |
| 3.6 | Seller's goal and timeline (move date, must-net number if they shared one) | Tone decisions | ASK |
| 3.7 | Sensitive topics to never put in writing (divorce, death in family, financial stress, other offers) | Keeps report safe to forward | ASK |
| 3.8 | Is the seller okay with offer amounts appearing in the report? Default: **no**, keep offer details verbal | The report is a public-ish URL | Default no |

### Round 4: Online performance sources (first run only, links saved)

For each platform, ask: **Is the listing live there? What is the URL? Where do you see views: public page or agent dashboard?**

| # | Platform | Where views live | e.g. URL |
|---|----------|------------------|----------|
| 4.1 | Zillow | Public listing page ("X views, Y saves") | zillow.com/homedetails/29-Amber-Rock-St-Henderson-NV-89012/7194804_zpid/ |
| 4.2 | Redfin | Public page (sometimes shown) | redfin.com/NV/Henderson/29-Amber-Rock-St-89012/home/29672171 |
| 4.3 | Homes.com | **Agent dashboard**, not the public page | homes.com/customer/dashboard/listings/?t=3&s=14 |
| 4.4 | Realtor.com | Public page ("XX views, X saves") | realtor.com/realestateandhomes-detail/29-Amber-Rock-St_Henderson_NV_89012_M18383-49659 |
| 4.5 | Your own property landing page (Lofty, kvCORE, BoldTrail, Squarespace, etc.) | CRM analytics, which view metric (page views vs visitors) and which window (e.g. last 30 days) | rosehomeslv.com/weekly-update-29-amber-rock, Lofty CMS > Content > Landing Pages > "Overview (last 30 days)" > Page Views |
| 4.6 | Any others (YouTube tour, IG reel, Facebook post)? Include or skip? | Optional extra tiles | skipped |
| 4.7 | Are you logged in to each of these in Chrome right now? | Browser automation needs live sessions. Claude never types passwords | ASK |
| 4.8 | **Rule for when a number goes DOWN week over week** (rolling 30-day windows do this) | Total views dropped from ~5,800 (Apr 3) to 5,566 (Apr 10) on 29 Amber Rock because a rolling window shrank. Seller noticed-risk | Options: keep highest-ever value / always report live number / report live + note "30-day window" |
| 4.9 | Last known view counts (baseline), if any | Week-over-week deltas | Zillow 2,592, Redfin 728, Homes.com 1,874, Realtor 318, landing page 54 |

### Round 5: Showings and feedback (first run, plus every week)

| # | Ask | Why | e.g. |
|---|-----|-----|------|
| 5.1 | Which showing service? (ShowingTime via your MLS/board portal, BrokerBay, Aligned, manual) and how to reach it | Showing count + ShowingTime feedback | ShowingTime through the local board portal (GLVAR in Las Vegas) |
| 5.2 | Do you export the showing list, or should Claude read it in the browser? | Data path | Browser, then logged to `Showings.md` |
| 5.3 | Where do buyer-agent follow-ups live? (ShowingTime, texts, email, phone calls) | Feedback sources | ShowingTime + iMessage + verbal |
| 5.4 | May Claude search your iMessages / Gmail for feedback from showing agents by name/phone? (yes / no / ask each time) | Privacy permission | ASK |
| 5.5 | **One source of truth for feedback.** 29 Amber Rock ended up with feedback split across `Showings.md` and `Feedback/feedback.md`. Pick one file (recommended: a single `Showings.md` with a showing log table + feedback section) | Prevents missed feedback | Consolidate |
| 5.6 | **(every week)** Paste any feedback you got by text, call, or in person that is not written down yet | Raw input | "Buyer loved layout, felt ~$50K of updates needed" |
| 5.7 | Count method: total showings to date, showings this week, or both? | Summary accuracy | Total to date + "this week" |
| 5.8 | Should repeat showings by the same agent count as separate showings? | Counting rule | 29 Amber Rock: one agent showed 3 times, counted 3 |

### Round 6: Listing activities (first run, plus every week)

The report has 3 activity cards. Ask for each: **where the number comes from, cumulative or this-week, and the one-line caption under the number.**

| # | Card | Source | Cumulative or 7-day? | e.g. |
|---|------|--------|----------------------|------|
| 6.1 | Neighborhood mailers sent | Mailing list file row count x rounds sent | ASK | 476, caption "Two rounds sent to nearby homeowners" |
| 6.2 | How many mail rounds have gone out so far, and dates? | Multiplier for 6.1 | **(every week)** | 2 rounds |
| 6.3 | Facebook/Instagram ad impressions | Meta Ads Manager, campaigns filtered by street name | Cumulative | 8,713 "Across 3 campaigns" |
| 6.4 | Meta ad account + campaign naming convention | Filter | ASK | campaign names contain "Amber Rock" |
| 6.5 | Show ad spend to the seller? (default no) | Report content | Default no | no |
| 6.6 | Reverse prospecting (agent email blasts) platform | Kit/ConvertKit, Mailchimp, MLS email, other | ASK: the old skill said "last 7 days" but the real report showed a cumulative total. Pick one | 531 "Agents emailed via Kit broadcasts" |
| 6.7 | Broadcast naming convention | Filter | contains the street address |
| 6.8 | Swap or add a card? (open houses held, database email blast opens, social post reach, video views) | Custom cards | none |

### Round 7: Competition and market (first run, refresh every week)

| # | Ask | Why | e.g. |
|---|-----|-----|------|
| 7.1 | 3 to 5 nearby competing listings or recent solds (Zillow URLs or addresses) | Email section "Nearby Listings/Solds to Keep an Eye On" | 1109 Thunder Canyon Ave, 1100 Blitzen Dr, 59 Sterling Meadow St, 15 Hatten Bay St, 1078 Las Palmas Entrada Ave |
| 7.2 | Selection rule if Claude refreshes them (radius, sqft range, beds, status, days back) | Keeps comps honest | same subdivision, +/- 200 sqft, last 60 days |
| 7.3 | Competition in the email only, or also in the report? | 29 Amber Rock: email only | email only |
| 7.4 | Pull comps from MLS each week (saved search name?) or only when you ask? | Scope | only when asked |
| 7.5 | **(every week)** Any competitor status changes you know about (went pending, price drop, sold price)? | Summary talking points | "Blitzen went under contract at $455K, renovated" |

### Round 8: This week's message (every week)

| # | Ask | Options |
|---|-----|---------|
| 8.1 | Report date (defaults to today) | date |
| 8.2 | Tone | **Momentum** (strong activity, affirm price) / **Subtle repositioning** (slow activity, comps moving, hint at adjustment without ever saying "reduce") / **Hold steady** (slow but patient) / **Custom** |
| 8.3 | The one thing you want the seller to take away this week | free text |
| 8.4 | Offers or serious interest to mention? (default: mention "productive conversations," never amounts, unless 3.8 = yes) | free text |
| 8.5 | Anything coming up next week (open house, price change effective date, new photos, new ad round, mailer drop)? | free text, becomes the forward-looking last sentence |
| 8.6 | Anything to leave out this week? | free text |

**Golden rule for every tone:** never tell the seller in writing to reduce the price. Use phrases like "capture a wider buyer pool" or "strengthen our competitive position." Buyer feedback about price is reported neutrally, as what buyers said.

### Round 9: Publishing and delivery (first run only)

| # | Ask | Why | e.g. |
|---|-----|-----|------|
| 9.1 | Where does the seller view the report? (CRM landing page / hosted HTML / PDF attachment) | Delivery method | Lofty landing page |
| 9.2 | Same URL every week (overwrite) or a new page each week? | 29 Amber Rock reused one URL all 5 weeks | same URL, overwrite |
| 9.3 | Page URL / slug | Email link | `/weekly-update-29-amber-rock` |
| 9.4 | Does Claude paste into the CRM for you via browser, or do you paste it? | Automation scope | ASK |
| 9.5 | CRM paste format quirks | The paste file must be raw HTML starting with `<!DOCTYPE html>`, **no code fences**, all CSS inline, all images base64 | confirmed |
| 9.6 | Email subject format | Consistency | `Weekly Update - 29 Amber Rock St` |
| 9.7 | Draft only, or send after your "yes"? (default: draft only) | Safety | draft only |
| 9.8 | Save location + file naming | Archive | `Weekly Reports/29 Amber Rock St - April 10, 2026.html` and `.md` |
| 9.9 | Also text the seller a heads-up? (yes/no, template) | Optional | no |

### Round 10: Automation and lifecycle (first run only)

| # | Ask | Options |
|---|-----|---------|
| 10.1 | Package this as a reusable `/weekly-update` skill? | Yes (recommended) / No, one-off |
| 10.2 | Scheduled reminder or scheduled run? | Manual command each week (recommended for now) / Remind me every [day/time] / Fully scheduled run that stops at the draft (set up later with the Cowork Automations bonus, B1) |
| 10.3 | Which steps must stay manual? | Logins, CRM paste, sending email, reading texts |
| 10.4 | What happens when the listing goes under contract? | Stop updates / Switch to an escrow update / Final "we're pending" report |
| 10.5 | Multiple listings at once? | One config per listing folder, skill takes the address as input |

---

## PHASE 2: What your plan must contain

After the interview, present a plan with these sections, in this order:

1. **Captured inputs table:** every answer from Rounds 1 to 10, with `NOT FOUND` items flagged.
2. **Files to create** (full paths), at minimum:
   - `[Listing Folder]/listing-config.json`: agent, brand, listing, seller, platforms, activity sources, competition, delivery settings, lifecycle rules. (Replaces and extends `platform-links.json`. Include `seller.legalName` and `seller.greetingName` as separate fields.)
   - `[Listing Folder]/view-history.csv`: one row per week per platform, so drops and deltas are visible.
   - `[Listing Folder]/Showings.md`: single showing log + feedback file (format below).
   - `[Listing Folder]/Weekly Reports/`: output folder.
   - Report template HTML (reuse an existing one if Phase 0 found it; otherwise build it from the section spec below).
   - The skill folder `.claude/skills/weekly-update/` inside the Business Brain (the same place your Level 3 skills live) with `SKILL.md`, `tone-guide.md`, `report-template.html`, and one playbook per data source, if 10.1 = yes.
3. **Data collection steps**, one per source, with the exact URL, what to click, what number to read, and the fallback if login is needed or the number is hidden (use `-` in the tile and exclude from total).
4. **Report build steps**, including base64 embedding of headshot + hero, the placeholder map below, and the views-total rule from 4.8.
5. **Showings summary method** (prompt below).
6. **Email draft spec** (structure below).
7. **Weekly run checklist**: the short list of every-week questions (5.6, 6.2, 7.5, Round 8) and the run order.
8. **QA checklist** (below) run before the user sees anything.
9. **Open items**: anything unresolved, who owns it, and what happens if it stays unresolved.
10. **Permissions needed**: connectors, Chrome logins, iMessage access, scheduled task.

---

## Reference specs (use these when building)

### Report sections and placeholders

| Section | Placeholder(s) | Content rule |
|---------|----------------|--------------|
| Agent header | `{{AGENT_PHOTO}}`, agent name | base64 headshot in a 72px circle |
| Sticky bar | `{{ADDRESS_FULL}}` | "Seller Report For" / address / agent name, accent bar on top |
| Hero | `{{HERO_IMAGE}}`, `{{ADDRESS_LINE1}}`, `{{ADDRESS_LINE2}}` | base64 hero photo, 4:3 |
| Executive Summary | `{{EXECUTIVE_SUMMARY}}` | 2 to 4 sentences, headline story only, key numbers wrapped in `<span class="highlight">`, ends forward-looking |
| Online Performance (dark band) | `{{TOTAL_VIEWS}}`, `{{ZILLOW_VIEWS}}`, `{{REDFIN_VIEWS}}`, `{{HOMES_VIEWS}}`, `{{REALTOR_VIEWS}}`, `{{LANDING_PAGE_VIEWS}}` | numbers with commas, total = sum of available platforms |
| Showings | `{{SHOWINGS_SUMMARY}}` | 3 to 4 short conversational paragraphs |
| Listing Activities | `{{MAILER_COUNT}}`, `{{FB_IMPRESSIONS}}`, `{{FB_CAMPAIGN_COUNT}}`, `{{REVERSE_PROSPECTING_COUNT}}`, `{{REVERSE_PROSPECTING_DETAIL}}` | number + label + one-line caption |
| Footer | `{{REPORT_DATE}}` | "Last Updated: April 10, 2026" |

### Showing log format (`Showings.md`)

```markdown
# Showings - [Address]

**List Price:** $[price] | **MLS ID:** [#]

| # | Date | Time | Showing Agent | Company | Phone | Email | Feedback |
|---|------|------|---------------|---------|-------|-------|----------|
| 1 | Wed 3/11/26 | 9:30 AM | [Name] | [Brokerage] | [phone] | [email] | See below / blank |

## Feedback

### Showing #[n] - [Agent] ([Brokerage]) - [Date]
- **Source:** ShowingTime / iMessage / Email / Verbal
- **Interest level:**
- **Liked:**
- **Concerns:**
- **Opinion of price:**
- **Follow-up notes:**
```

Preserve the agent's actual words. Never merge two agents into one entry. Date unknown is written as "Date unknown," not guessed.

### Showings summary prompt

> You are an experienced listing agent giving showing feedback to your seller, like a talk at the kitchen table. Read the feedback section of `Showings.md`. Lead with the theme buyers mention most. Report what buyers said neutrally, no spin and no added opinion. Acknowledge real positives. Be warm where feedback is hard to hear. Close with what the feedback suggests we consider next, without ever telling the seller to reduce the price. Keep it brief. Phrases like "Here's what I'm hearing..." are good. If there is no feedback yet, state the showing count and that feedback is pending. Do not invent themes. Do not include offer amounts unless the config allows it.

### Seller email structure

```
To: [seller email(s)]   CC: [per config]
Subject: Weekly Update - [Street Address]

Hi [greeting name],

[Executive summary, same 2 to 4 sentences as the report, plain text, no highlight spans]

Here's your full report with all the details:
[report URL]

Nearby Listings/Solds to Keep an Eye On:
[Street address 1, hyperlinked to its Zillow page]
[Street address 2, hyperlinked]
...

Best,
[Agent name]
```

Create as a Gmail **draft** in HTML if the Gmail connector is live. If not, print the email ready to copy and paste. Never send without an explicit "send it" from the user in chat. The system drafts, the agent sends.

### Tone quick reference

- **Momentum:** lead with big numbers, affirm pricing, buyer interest as validation.
- **Subtle repositioning:** acknowledge the data calmly, frame comp moves as "market movement," suggest "capturing a wider buyer pool." Never "overpriced," "reduce," or "price is too high" in our own voice.
- **Hold steady:** quality over quantity, seasonal context, marketing still running.
- **Custom:** user's direction, golden rule still applies.
- Style: "we/our" for strategy, "your" for the home. Every claim backed by a number.

### QA checklist (run before showing the user)

- [ ] Zero em dashes in report, paste file, and email (search for the `—` character).
- [ ] Nothing in the report describes the occupants, the seller's reasons, or who the home is "perfect for."
- [ ] Every number traces to a source captured this run or to `NOT FOUND`.
- [ ] Total views = sum of the tiles shown. Week-over-week drops handled per rule 4.8.
- [ ] Showing count matches the log table row count (per rule 5.8).
- [ ] Greeting uses the greeting name, not the legal name.
- [ ] No offer amounts, sensitive topics, or ad spend unless the config allows it.
- [ ] Executive summary is 2 to 4 sentences and matches between report and email.
- [ ] Paste `.md` is byte-identical to the `.html`, starts with `<!DOCTYPE html>`, no code fences.
- [ ] Headshot and hero render (base64, no broken local paths).
- [ ] Competition links open to the right properties and are labeled by street address.
- [ ] Preview served on localhost and screenshotted for the user before saving as final.
- [ ] Email is a draft, not sent.

### Weekly run order (what the finished skill does each time)

1. Load `listing-config.json`. Warn if any saved link is older than 7 days and re-verify it still points to this listing.
2. Ask the every-week questions (5.6, 6.2, 7.5, Round 8) in one or two rounds.
3. Pull views: Zillow, Redfin, Homes.com dashboard, Realtor.com, CRM landing page. Append to `view-history.csv`.
4. Pull showings from the showing service. Append new rows to `Showings.md`. Search allowed channels for new feedback by agent name/phone and log it.
5. Pull Meta impressions + campaign count, reverse prospecting recipients, mailer count.
6. Write the executive summary and showings summary in the chosen tone.
7. Fill the template, embed images, preview on localhost, screenshot, get approval.
8. Save `[Address] - [Month Day, Year].html` and `.md` to `Weekly Reports/`.
9. Publish to the landing page (or hand the user the paste file and URL).
10. Create the email draft. Show it. Wait. The agent reads it, changes what only they would know to change, and sends it.
11. Update `listing-config.json` (`lastUpdated`, last views) and print a 5-line recap: numbers, deltas, open items, what to watch next week.

---

## Lessons from Ryan's 29 Amber Rock run (build these in)

- Seller's legal name and the name they go by were different. Store both.
- Feedback lived in two files and one was never read by the report step. One file only.
- Views total went down between weeks because the landing page uses a rolling 30-day window. Decide the rule up front.
- The skill said reverse prospecting = last 7 days, but the report showed a cumulative total. Decide up front and label the caption to match.
- The mailer caption was hand-edited to "Two rounds sent to nearby homeowners." Make rounds an every-week input.
- One URL, overwritten weekly, worked well: the seller always has the same link.
- The CRM paste breaks if the HTML is wrapped in code fences.
- One agent's text feedback speculated about the previous occupants. That kind of comment never goes in the report.
- Offer amounts came up in buyer-agent texts. Keep them out of the written report by default.
- Portal logins (Homes.com dashboard, Lofty, Meta, ShowingTime) are the usual blocker. Confirm the user is logged in to each before the run starts, and pause for manual login instead of failing.
