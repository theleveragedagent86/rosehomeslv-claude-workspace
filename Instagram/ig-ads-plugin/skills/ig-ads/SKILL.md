---
name: ig-ads
description: Use when someone asks to create Instagram ads, set up Meta ads, build a Facebook or Instagram ad campaign, run paid social ads for a listing, create Meta Business Suite campaigns, run a just listed ad, run a just sold ad, create listing ads on Meta, run listing lead form ads, create lead form campaigns, capture buyer leads from a listing, or sync Meta leads to Lofty CRM.
disable-model-invocation: true
argument-hint: "listing address or campaign topic"
---

## What This Skill Does

Creates Instagram/Meta ad campaigns and inputs them into Meta Business Suite via Cowork browser automation. Uses a multi-agent team (Campaign Manager, Ads Strategist, Content Creator, Creative Director) to develop professional ad campaigns for Ryan Rose. Also supports Listing Lead Form campaigns (buyer lead capture via Instant Form) and automated lead sync from Meta to Lofty CRM.

**Meta Business Suite:** https://business.facebook.com
**Account:** Rose Homes LV
**Default Objective:** Traffic / Leads
**Default Placement:** Advantage+ (let Meta auto-optimize)

**Supporting files in this skill directory:**
- [meta-business-suite-automation.md](meta-business-suite-automation.md) — Browser automation playbook for Meta Business Suite
- [ad-copy-templates.md](ad-copy-templates.md) — Ad copy templates by campaign type
- [campaign-structures.md](campaign-structures.md) — Campaign structure and audience targeting reference
- [follow-up-sequence.md](follow-up-sequence.md) — 30-day lead follow-up sequence (texts, emails, call tasks) for Lofty Action Plans

---

## Architecture

You are the **Campaign Manager**. You orchestrate three sub-agents:

1. **Ads Strategist** (1 instance) — Recommends campaign structure, number of variations, audience targeting, budget allocation, and objective setup
2. **Content Creator** (1 instance) — Writes all ad copy variations: headlines, primary text, descriptions, CTAs
3. **Creative Director** (1 instance) — Handles visuals: generates AI images when needed, specs out requirements when user provides their own, ensures Meta ad specs compliance

**You coordinate all agents, assemble the final campaign, and handle the Cowork browser automation to input everything into Meta Business Suite.**

---

## Workflow

### Step 1: Gather Campaign Info

If `$ARGUMENTS` is provided, use it as the subject matter. If no arguments, ask:

> "What's the subject for this ad campaign? This can be a listing (e.g., 1234 Desert Rose Dr) or a campaign topic (e.g., spring market update, brand awareness, open house promo)."

Then ask the user for the following (one prompt, all questions together):

- **Landing page URL:** Where should the ad drive traffic? (Required for listing ads — this is where people go instead of Zillow)
- **Budget:** Daily or lifetime budget amount (recommend based on listing price if unsure — see campaign-structures.md)
- **Duration:** How long the campaign should run
- **How many photos:** How many listing photos should be included in the ad? (1 = single image ad, 2+ = carousel)
- **Campaign type:** Just Listed, Just Sold, or Listing Lead Form (if this is a listing ad). Listing Lead Form = Week 2+ of a listing launch, uses the listing as a hook but captures buyer leads via Meta Instant Form.
- **Visuals:** Are you providing images/video, or should we generate them with AI?

**IMPORTANT — No address in listing ads:** The ad copy must NEVER include the property address. The entire point is to drive people to Ryan's landing page, not to give them enough info to find it on Zillow. Use neighborhood name, features, and price instead.

If invoked from listing-marketing Phase 3 or Phase 5B, property details and listing photos will already be in context. Skip questions that are already answered. Still ask for **landing page URL**, **budget**, **duration**, and **how many photos** — these are always required.

---

### Step 2: Spawn Ads Strategist

Read [campaign-structures.md](campaign-structures.md) from this skill directory.

Use the **Agent tool** to spawn a `general-purpose` sub-agent:

```
You are an Ads Strategist for the ig-ads system.

You are building a Meta/Instagram ad campaign for Ryan Rose, a Las Vegas real estate agent at Real Broker, LLC.

CAMPAIGN STRUCTURES REFERENCE:
[FULL CONTENTS OF campaign-structures.md]

CAMPAIGN BRIEF:
- Subject: [SUBJECT MATTER]
- Campaign type: [JUST LISTED / JUST SOLD / LISTING LEAD FORM / OTHER]
- Landing page URL: [URL]
- Budget: [BUDGET]
- Duration: [DURATION]
- Target audience: 20-mile radius centered on downtown Las Vegas, 89101 (Housing Special Ad Category — no age, gender, or zip targeting allowed). ALWAYS center on 89101, NOT the listing address.
- Objective: Traffic (for Just Listed/Just Sold) or Leads with Instant Form (for Listing Lead Form)
- Placement: Advantage+ (auto)
- Number of photos: [X]
- Visuals available: [YES/NO + description]

IMPORTANT: This is a Housing Special Ad Category campaign. Targeting is restricted to location radius only (minimum 15 miles). No age, gender, zip code, or detailed interest targeting is permitted. The ad copy must NOT include the property address — use neighborhood, features, and price only. All traffic goes to the landing page URL. The radius must be centered on downtown Las Vegas (89101), NOT the listing address.

IF LISTING LEAD FORM: The objective is Leads (not Traffic). The campaign uses Meta Instant Forms to capture buyer contact info. The listing is the HOOK but the CTA is about finding similar homes or getting alerts. CTA button = "Sign Up". Include Instant Form configuration in your recommendations (see campaign-structures.md for form field defaults).

Based on this brief, recommend:
1. Campaign name (clear, descriptive)
2. Number of ad sets (usually 1-2 unless split testing audiences)
3. Number of ad variations per ad set (recommend based on campaign type)
4. Audience targeting details (location, age range, interests, behaviors)
5. Budget allocation across ad sets
6. Recommended ad formats (single image, carousel, video)
7. Call-to-action button type (Learn More, Send Message, Sign Up, etc.)

Return your recommendations in a structured format.
```

Store the output as `STRATEGY`.

---

### Step 3: Spawn Content Creator

Read [ad-copy-templates.md](ad-copy-templates.md) from this skill directory.

Use the **Agent tool** to spawn a `general-purpose` sub-agent:

```
You are a Content Creator for the ig-ads system.

You are writing ad copy for Ryan Rose, a Las Vegas real estate agent at Real Broker, LLC.

AD COPY TEMPLATES:
[FULL CONTENTS OF ad-copy-templates.md]

CAMPAIGN STRATEGY:
[STRATEGY output from Step 2]

SUBJECT MATTER: [SUBJECT]
CAMPAIGN TYPE: [JUST LISTED / JUST SOLD / LISTING LEAD FORM / OTHER]
PROPERTY DETAILS (if listing): [NEIGHBORHOOD, BEDS, BATHS, SQFT, PRICE, KEY FEATURES]
LANDING PAGE URL: [URL]

WRITING RULES:
- Warm, local, knowledgeable. Never corporate or salesy.
- NO em-dashes. Use commas, periods, or "and" instead.
- Short sentences. Conversational tone.
- Each variation must feel distinct, not just word-swapped.
- Headlines: max 40 characters. Punchy and specific.
- Primary text: 125 characters visible before "See More", so front-load the hook.
- Description: max 30 characters. Supporting context.
- CTA must match the button type from the strategy.
- **CRITICAL: NEVER include the property address in any ad copy.** Use neighborhood name, features, price, and lifestyle language instead. The goal is to drive clicks to the landing page, not give enough info to find the home on Zillow.
- **IF LISTING LEAD FORM:** The CTA is "Sign Up" (not "Learn More"). Primary text uses the listing as a hook but pivots to broader buyer interest (similar homes, alerts, neighborhood options). The ad drives to an Instant Form, NOT a website URL. Use the "Listing Ad — Listing Lead Form" templates from the templates reference.

For each ad variation recommended by the strategist, write:
1. Primary text (the main ad copy body)
2. Headline
3. Description
4. CTA text (matching the button type)

Return all variations in a numbered, structured format.
```

Store the output as `AD_COPY`.

---

### Step 4: Spawn Creative Director

Use the **Agent tool** to spawn a `general-purpose` sub-agent:

```
You are a Creative Director for the ig-ads system.

You are handling visuals for a Meta/Instagram ad campaign for Ryan Rose, Las Vegas real estate agent.

CAMPAIGN STRATEGY:
[STRATEGY output]

AD COPY:
[AD_COPY output]

VISUAL SITUATION: [USER PROVIDED / AI GENERATE / MIX]
NUMBER OF PHOTOS REQUESTED: [X] (1 = single image ad, 2+ = carousel)
USER-PROVIDED ASSETS: [file paths or URLs if provided]
LISTING PHOTOS FOLDER: [path if applicable]

Your job:

IF user provided images/video:
- Confirm the assets meet Meta ad specs:
  - Feed: 1080x1080 (1:1) or 1080x1350 (4:5)
  - Stories/Reels: 1080x1920 (9:16)
  - Text overlay: keep under 20% of image area
  - File size: under 30MB for images, under 4GB for video
  - Video length: 15 seconds or less recommended for Stories, up to 60 seconds for Feed
- Map which asset goes with which ad variation
- Flag any issues (wrong dimensions, too much text overlay, etc.)

IF AI-generating images:
- Write detailed image generation prompts for each ad variation
- Style: professional real estate photography aesthetic, warm lighting, Las Vegas setting
- Include specific composition notes (wide angle for exteriors, lifestyle shots for brand awareness)
- Specify dimensions needed for each placement
- DO NOT actually generate the images. Return the prompts for the Campaign Manager to execute.

Return your visual plan in a structured format: which visual pairs with which ad variation, and any specs or prompts needed.
```

Store the output as `CREATIVE_PLAN`.

**Note:** Spawn the Content Creator and Creative Director in parallel if the user is providing their own visuals (no dependency). If AI-generating visuals, the Creative Director needs the ad copy first, so run sequentially.

---

### Step 5: Assemble Campaign Document

Combine all agent outputs into a single campaign document. Save it to:

```
/Users/ryanrose/Downloads/Claude/Listings/[ADDRESS]/Phase 3/Meta Ad Campaign.docx
```

If this is NOT a listing campaign (brand awareness, general topic), save to:

```
/Users/ryanrose/Downloads/Claude/Instagram/Ad Campaigns/[CAMPAIGN NAME].docx
```

Create the directory if it does not exist.

**Campaign document format:**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
META AD CAMPAIGN: [CAMPAIGN NAME]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Subject: [subject matter]
Campaign Type: [Just Listed / Just Sold / Listing Lead Form / Other]
Landing Page URL: [URL]
Objective: [Traffic / Leads (Instant Form)]
Placement: Advantage+ (auto)
Budget: [amount] ([daily/lifetime])
Duration: [start] - [end]
CTA Button: [button type]
Photos Included: [X]

━━━ AUDIENCE TARGETING ━━━
Special Ad Category: Housing (REQUIRED)
Location: 20-mile radius centered on downtown Las Vegas (89101)
(No age, gender, zip, or detailed interest targeting — Housing category restriction)

━━━ INSTANT FORM (Listing Lead Form campaigns only) ━━━
Form Name: [name]
Form Type: More Volume
Fields: Full Name, Email, Phone
Question 1: When are you looking to buy? (ASAP / 1-3 months / 3-6 months / Just browsing)
Question 2: Are you pre-approved? (Yes / No / Not yet)
Privacy Policy: https://www.rosehomeslv.com/site/privacy-terms
Thank You: "You're All Set!" → View Website

━━━ AD VARIATION 1 ━━━

Primary Text:
[ad copy]

Headline: [headline]
Description: [description]
Visual: [image description or file reference]

━━━ AD VARIATION 2 ━━━
[repeat for each variation]

━━━ VISUAL SPECS ━━━
[Creative Director's notes on dimensions, specs, AI prompts if applicable]

━━━ CAMPAIGN NOTES ━━━
[Any strategist recommendations, A/B testing notes, optimization tips]
```

**Save workflow:**
1. Write content to a temporary `.txt` file at the target path
2. Run: `textutil -convert docx "[FILE].txt"`
3. Delete the `.txt` file: `rm "[FILE].txt"`

Present the full campaign document to the user for review before proceeding to browser automation.

Ask: **"Campaign is assembled. Ready to input into Meta Business Suite, or want to make changes first?"**

---

### Step 6: Input into Meta Business Suite — Choose Mode

Check if browser/computer use tools are available (navigate, click, type, screenshot, browser_navigate, browser_click, browser_type, browser_snapshot, javascript_tool, or computer use tools).

- If browser tools found: **Mode A (Cowork Automation)**
- If no browser tools found: **Mode B (Manual Checklist)**

---

### Mode A: Cowork Automation

Read [meta-business-suite-automation.md](meta-business-suite-automation.md) from this skill directory for the full browser automation playbook.

**High-level steps (detailed navigation in the automation playbook):**

1. Navigate to `https://business.facebook.com/latest/ads/create`
2. Verify logged in and on the Rose Homes LV account
3. If not logged in, pause and ask user to log in
4. Select campaign objective (Traffic for Just Listed/Just Sold, Leads for Listing Lead Form)
5. Name the campaign
6. Configure ad set: audience targeting (20-mile radius centered on 89101), budget, schedule, placements (Advantage+)
7. Create each ad variation: upload/select visuals, enter primary text, headline, description, CTA
8. **If Leads objective (Listing Lead Form):** Create the Instant Form using the steps in meta-business-suite-automation.md → "Instant Form Creation" section. Create the form once, then attach it to all ad variations.
9. **STOP before clicking Publish.** Tell the user: "Campaign is fully set up and ready for review in Meta Business Suite. Please review and publish when ready."
10. **If Listing Lead Form campaign:** Create Lofty Action Plans. Read [follow-up-sequence.md](follow-up-sequence.md) for the sequence content. Replace template variables with actual listing data ({AREA}, {NEIGHBORHOOD}, {LISTING_FEATURE}, {PRICE}, {BEDS}, {BATHS}). Leave `#lead_first_name#` as the Lofty merge field. Follow the "Lofty Action Plan Creation" steps in [meta-business-suite-automation.md](meta-business-suite-automation.md) to create all 3 plans (Hot, Warm, Nurture) in Lofty. Activate all plans immediately.

**Report after each major step:**
```
Step [X] complete: [description]
```

---

### Mode B: Manual Checklist

Output a step-by-step checklist the user can follow in Meta Business Suite:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
META BUSINESS SUITE CAMPAIGN SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[ ] 1. Go to https://business.facebook.com/latest/ads/create
[ ] 2. Select campaign objective: [Traffic / Leads]

[ ] 3. CAMPAIGN LEVEL
    • Campaign name: [name]
    • Budget optimization: ON
    • Budget: [amount] [daily/lifetime]

[ ] 4. AD SET LEVEL
    • Special Ad Category: Housing (REQUIRED — select this first)
    • Ad set name: [name]
    • Audience location: 20-mile radius centered on downtown Las Vegas (89101)
    • (No age, gender, or interest targeting — Housing category restriction)
    • Placements: Advantage+ (automatic)
    • Schedule: [start date] to [end date]

[ ] 5. AD LEVEL — Variation 1
    • Ad name: [name]
    • Upload image/video: [file or description]
    • Primary text — paste:
      [full primary text]
    • Headline — paste:
      [headline]
    • Description — paste:
      [description]
    • CTA button: [button type]
    • Website URL: [LANDING PAGE URL — never Zillow/MLS]

[ ] 6. AD LEVEL — Variation 2
    [repeat for each variation]

[ ] 7. INSTANT FORM (Listing Lead Form campaigns only)
    • Lead method: Instant forms
    • Form type: More volume
    • Intro headline: "Find Similar Homes in [NEIGHBORHOOD]"
    • Fields: Full Name, Email, Phone
    • Question 1: "When are you looking to buy?" → ASAP / 1-3 months / 3-6 months / Just browsing
    • Question 2: "Are you pre-approved for a mortgage?" → Yes / No / Not yet
    • Privacy policy URL: https://www.rosehomeslv.com/site/privacy-terms
    • Thank you headline: "You're All Set!"
    • Thank you CTA: View Website → [landing page URL]

[ ] 8. REVIEW all settings, then click PUBLISH when ready

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

If AI images need to be generated, output the prompts and tell the user to generate and download them before starting the checklist.

---

## Integration with Listing Marketing

When invoked from listing-marketing Phase 3 (Just Listed) or Phase 5B (Just Sold):

- Property details are already in context — do not re-ask
- Subject matter = the listing (but NEVER put the address in the ad copy)
- Default audience: 20-mile radius centered on downtown Las Vegas (89101) — Housing Special Ad Category (no age/gender/interest targeting)
- Default CTA: "Learn More" linking to the landing page URL (Traffic campaigns) or "Sign Up" (Listing Lead Form campaigns)
- Default visuals: listing photos from `[LISTING FOLDER]/Listing Photos/`
- **Still ask for:** landing page URL, budget, duration, and how many photos
- Save campaign doc to `[LISTING FOLDER]/Phase 3/Meta Ad Campaign.docx` (Just Listed) or `[LISTING FOLDER]/Phase 5B/Meta Ad Campaign.docx` (Just Sold) or `[LISTING FOLDER]/Phase 3/Meta Ad Campaign - Lead Form.docx` (Listing Lead Form)
- After completion, return control to listing-marketing to continue phase deliverables

When invoked from listing-marketing Phase 3 with campaign type "Listing Lead Form" (Week 2+ of listing launch):
- This creates a Leads objective campaign using the listing as the hook
- The Instant Form captures buyer leads interested in similar homes
- This runs alongside or replaces the initial Traffic campaign after Week 1
- Leads are automatically synced to Lofty CRM via the Lead Sync workflow

---

## Lead Sync: Meta → Lofty CRM

This skill also handles syncing leads from Meta Instant Forms into Lofty CRM. This can be triggered by:
- Saying "sync leads", "sync Meta leads to Lofty", or "pull my leads"
- Automated scheduled runs (via `/loop` skill)

### How It Works

1. **Check for browser tools** — same as campaign creation, requires browser automation (Cowork)
2. **Read the automation playbook** — follow the "Lead Sync: Meta → Lofty CRM" section in [meta-business-suite-automation.md](meta-business-suite-automation.md)
3. **Download leads from Meta** — navigate to Leads Center, extract new form submissions
4. **Enter leads into Lofty** — for each new lead, create a contact in Lofty CRM with name, email, phone, source, and qualifying question answers in notes
5. **Tag the lead** — based on qualifying answers, apply the listing + track tag (e.g., "29 Amber Rock - Hot"). See meta-business-suite-automation.md for the track determination logic.
6. **Assign Action Plan** — assign the matching listing-specific Action Plan to the lead. The first automated text fires immediately.
7. **Log synced leads** — update the tracking log at `/Users/ryanrose/Downloads/Claude/Instagram/Ad Campaigns/lead-sync-log.json` to prevent duplicates
8. **Report results** — tell the user how many leads were synced, which track each was assigned, and confirm Action Plans are running

### Lead Sync Without Browser Tools (Mode B)

If no browser tools are available, output a manual sync checklist:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
META LEAD SYNC — MANUAL CHECKLIST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[ ] 1. Go to https://business.facebook.com/latest/leads_center
[ ] 2. Filter by form name and date range (since last sync)
[ ] 3. Download leads as CSV
[ ] 4. Open Lofty CRM → Add each lead:
    • Name, Email, Phone
    • Source: "Meta Lead Form Ad"
    • Notes: qualifying question answers
[ ] 5. Done — follow up within 24 hours!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Notes

- **Ryan Rose info:** Real Broker, LLC | 702-747-5921 | ryan@rosehomeslv.com | rosehomeslv.com
- **NEVER publish/launch ads.** Always stop before the final publish button. Set up for review only.
- **NEVER include the property address in ad copy.** Use neighborhood, features, and price. Drive all traffic to the landing page URL.
- **NO em-dashes** in any ad copy. Use commas, periods, or "and" instead.
- **Housing Special Ad Category is REQUIRED** for all real estate ads. Targeting is limited to location radius (15-mile minimum, we use 20 miles centered on 89101). No age, gender, zip code, or detailed interest targeting.
- Ad copy should be warm, local, knowledgeable. Never corporate or salesy.
- Front-load the hook in primary text — only 125 characters show before "See More."
- Meta rejects ads with more than 20% text overlay on images. Flag this to the user.
- If browser automation encounters an error or unexpected UI, pause and describe what you see. Do not guess at button locations.
- Landing page URL, budget, duration, and photo count are asked fresh each campaign.
- Campaign summary doc always saves to the listing folder when this is a listing campaign.
