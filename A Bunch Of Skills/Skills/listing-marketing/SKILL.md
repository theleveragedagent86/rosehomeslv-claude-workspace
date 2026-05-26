---
name: listing-marketing
description: Use when someone asks to create listing marketing content, generate a marketing plan for a listing, write listing emails, create neighbor letters, write social posts for a listing, generate voicemail scripts, or produce any content for a listing launch phase (coming soon, just listed, pending, just sold).
argument-hint: "property address or phase name"
---

## What This Skill Does

Generates all ready-to-use listing marketing content for Ryan Rose based on the Ultimate Listing Launch Marketing Playbook. For a given property, produces phase-specific deliverables: email blasts, neighbor letters, social media captions, voicemail scripts, and agent-to-agent outreach.

**Listing folder:** /Users/ryanrose/Downloads/Claude/Listings/
**Playbook:** /Users/ryanrose/Downloads/Claude/Listings/29 Amber Rock St/Ultimate_Listing_Launch_Marketing_Playbook.docx
**All letter and email templates:** See [templates.md](templates.md)

---

## Step 1: Collect Property Info

If property details are not already known from the conversation or from files in the Listings folder, ask for them. Required fields:

- **Address** (full street address + city/state/zip)
- **Neighborhood** (subdivision or community name, e.g., "Champion Village")
- **Beds / Baths** (e.g., "3 bed / 2 bath")
- **Square footage** (e.g., "1,796 sq ft")
- **Lot size** (e.g., "6,534 sq ft")
- **List price** (e.g., "$485,000")
- **Expected price range** (for Coming Soon use, e.g., "$470,000–$490,000")
- **Launch date** (Day 15 / official MLS Active date, e.g., "March 11, 2026")
- **Open house date and time** (e.g., "Saturday March 15, 12–3 PM")
- **3–5 key features** (e.g., "3-car garage, chef's kitchen with island, single-story, tile roof, 6,534 sq ft lot")

If $ARGUMENTS contains an address, check /Users/ryanrose/Downloads/Claude/Listings/ for existing files (data sheets, marketing packages) to pull details automatically.

Optional fields needed only in later phases:
- # of showings received
- # of offers received
- Final sold price / % over asking
- Days on market

---

## Step 2: Determine Phase

Ask which phase to generate content for, or infer from $ARGUMENTS or context:

| Phase | Trigger |
|-------|---------|
| **Phase 1** — Pre-Listing | Listing appointment booked; before Coming Soon |
| **Phase 2** — Coming Soon | Days 1–14, before official MLS launch |
| **Phase 3** — Just Listed | Day 15, official launch day |
| **Phase 5A** — Pending | Home goes under contract |
| **Phase 5B** — Just Sold | Closing day |

If $ARGUMENTS includes a phase name (e.g., "coming soon", "just listed", "pending", "sold"), skip this step.

---

## Step 3: Generate Content by Phase

---

### PHASE 1 — Pre-Listing

Generate both items:

**1. Database Activation Email**
- Subject: Something like "Quick question before my appointment tomorrow"
- Body: Announce you're meeting with a seller in [NEIGHBORHOOD] tomorrow. Ask if anyone they know has been looking in that area. Invite replies for early details. Under 100 words. Personal and excited, not corporate.

**2. Seller Discovery Form Email**
- Send to potential seller 24–48 hours before listing appointment
- Short intro explaining you send this to every seller beforehand
- Frames it as preparation, not homework
- Professional, builds credibility and separates Ryan from other agents
- See [templates.md → Phase 1](templates.md)

---

### PHASE 2 — Coming Soon

Generate all 7 items:

**1. "Exclusivity Ends" Email Blast** (Day 1)
- Subject: "Exclusive: New Listing in [NEIGHBORHOOD] — Details Before Anyone Else"
- Offer early access before it hits public sites. Reference the address. Invite replies. Under 150 words.
- See [templates.md → Phase 2](templates.md)

**2. Coming Soon Neighbor Letter** (Days 6–7, mail 300 neighbors)
- Use Letter 2 template from [templates.md → Phase 2](templates.md)
- Fill in all property details

**3. VIP Teaser Instagram Story Caption** (Day 1)
- 2–3 sentences. Tease without revealing address. Invite DMs for early access. Create FOMO.

**4. Coming Soon Announcement Reel Caption** (Day 1)
- 4–6 lines. Hook + tease 2 features + neighborhood mention + CTA to DM. No address. Emoji optional.

**5. Feature Highlight Reel Caption** (Day 4)
- Spotlight the single best feature of the home. 4–6 lines. Conversational, specific.

**6. "Deal of the Week" Email** (Day 5)
- NO address, NO photos — curiosity only
- Short intro, bullet the home highlights, end with "Reply for full details"
- See [templates.md → Phase 2](templates.md)

**7. Video CMA Email Hook** (Days 4–5, send to 25–50 nearby database contacts)
- Subject line + opening paragraph (Ryan records the actual video; this is just the written hook)
- Reference [NEIGHBORHOOD] activity and home values

---

### PHASE 3 — Just Listed

Generate all 4 items:

**1. "Just Listed" Email Blast** (launch day, 7:30 AM)
- Subject: "Just Listed: [ADDRESS] | [NEIGHBORHOOD]"
- Price, top 3–5 features, open house date/time, virtual tour CTA
- See [templates.md → Phase 3](templates.md)

**2. Just Listed Neighbor Letter** (mail 300 same day)
- Use Letter 3 template from [templates.md → Phase 3](templates.md)
- Include open house invite. Leave [X inquiries] and [X showing requests] as brackets if unknown.

**3. Launch Day Social Blitz** (8:00 AM, post simultaneously on all platforms)
Generate separate captions for:
- Instagram Reel caption
- Instagram Carousel caption (include 5 slide text suggestions in brackets)
- Facebook post
- TikTok caption
- LinkedIn update

**4. Agent-to-Agent Text** (9:00 AM, send to 30–50 agents)
- 2–3 sentences. Address, one key feature, price, virtual tour link placeholder. Professional but brief.

---

### PHASE 5A — Pending

Generate all 4 items:

**1. Slybroadcast Voicemail Script — Pending Announcement**
- 30–45 seconds when read aloud. Natural speech, no jargon.
- Include: address, neighborhood, # showings, # offers (use brackets if unknown), invite callbacks
- See [templates.md → Phase 5A](templates.md)

**2. "Pending / Buyers Still Looking" Social Post #1**
- Celebrate going under contract. Note your buyers are still searching the area. Invite inquiries.

**3. "Pending / Buyers Still Looking" Social Post #2**
- Different angle: show the result (speed of sale, # offers) as proof of your marketing system.

**4. Magic Buyer Letter** (mail 300 neighbors)
- Use Letter 4 template from [templates.md → Phase 5A](templates.md)
- Customize buyer's specifics: beds/baths, budget, timeline, what they love about the neighborhood

---

### PHASE 5B — Just Sold

Generate all 4 items:

**1. Slybroadcast Voicemail Script — Just Sold**
- 30–45 seconds when read aloud. Include: sold price or % over asking, # of offers, invite valuation calls
- See [templates.md → Phase 5B](templates.md)

**2. Just Sold Neighbor Letter** (mail 300)
- Use Letter 5 template from [templates.md → Phase 5B](templates.md)
- Fill in all sold results. Leave brackets for any unknown numbers.

**3. "Story of Sold" Social Post Series** (3 posts)
- Post 1: Throwback to the launch — what the journey looked like
- Post 2: The result — sold price, speed, # of offers
- Post 3: What it means for neighbors — their home value context

**4. Referral Request Script** (verbal, at closing)
- 3–4 sentences spoken aloud. Based on Tom Ferry's referral script.
- See [templates.md → Phase 5B](templates.md)

---

## Output Format

Present each deliverable in this format:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[CONTENT TYPE] — [Phase]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[READY-TO-USE CONTENT — all known property details filled in]

Notes: [Any platform instructions or [BRACKETS] still needing real numbers]
```

After delivering all content for a phase, ask: "Ready for the next phase?"

---

## Notes

- **Ryan Rose info:** Real Broker, LLC | 702-747-5921 | ryan@rosehomeslv.com | rosehomeslv.com
- Leave unknown stats as `[X showings]`, `[X offers]`, `[$XXX,XXX sold price]` — never make up numbers.
- Social posts: warm, local, knowledgeable. Never corporate or salesy. No em-dashes. Short sentences.
- Slybroadcast scripts: read them aloud mentally before finalizing. They must sound natural, not robotic.
- "Deal of the Week" email **never** includes the address or photos — this is intentional to drive reply volume.
- If $ARGUMENTS contains an address, that is the property. If it contains a phase name, start at that phase.
- The 300-postcard count is per Meredith Fogle's expanded system. Letters 2–5 are the neighborhood outreach for each phase.
