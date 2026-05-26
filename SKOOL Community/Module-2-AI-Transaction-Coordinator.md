# Module 2: The AI Transaction Coordinator — The Leveraged Agent

## Module Overview

The intensive one. Everything that happens from "offer accepted" to "closed and funded," handled by AI. Members walk in drowning in transaction admin — timelines, inspection responses, escrow emails, lender coordination, document review, client updates — and walk out running their transactions in **15 minutes a day** instead of burning 2-4 hours per file.

**The core promise:** "My transactions don't run my life anymore. I open Cowork in the morning, it tells me what needs attention today, I handle it in 15 minutes, and my clients think I'm the most organized agent they've ever worked with."

**Who this is for:**
- Solo agents who coordinate their own transactions (no TC)
- Agents who have a TC but want to augment them, not replace them
- Transaction coordinators themselves who want to handle 3x more files
- Team leads overseeing multiple deals at once

**Why it's intensive:** Transaction coordination has more moving parts than any other real estate workflow. Inspections, appraisals, loan conditions, HOA docs, title work, escrow deadlines, disclosures, addendums, repair negotiations, final walkthroughs, closing coordination. Module 2 systemizes all of it.

**Note on contract filling:** This module intentionally does NOT cover filling out Authentisign/GLVAR forms programmatically. That's a separate workflow with legal/access constraints (see Module 2.5 down the road). Everything else in the transaction lifecycle IS covered.

**Prerequisite:** **Module 0 must be completed first.** Voice Profile + email templates + basic Claude workflow are required foundations. Module 1 is NOT required — buyer agents who rarely launch listings can jump straight here.

**Design philosophy (same as Modules 0 and 1):**
- Every lesson produces a real, deployable asset
- Screen-share walkthroughs using Ryan's actual active transactions
- Every lesson ends with "Post your result in Wins & Results"
- In Cowork: each workflow is a reusable skill. In browser: copy-paste templates provided
- **Module 2 unlocks when Module 0 is marked complete.** All 10 lessons available at once — no internal gates.

---

## Skool Classroom Placement

```
Classroom
├── [Tile] Module 0: Start Here (complete)
├── [Tile] Module 1: Listing Launch Package
├── [Tile] Module 2: The AI Transaction Coordinator    ← THIS FILE
├── [Tile] Module 3: Social Media & Content
└── [Tile] Call Replays
```

**Course Name:** The AI Transaction Coordinator
**Course Description (shows under tile):**
> The intensive one. Manage your entire transaction pipeline — timelines, inspections, document review, client updates, escrow and lender coordination, post-close follow-up — in 15 minutes a day. No more dropped balls. No more 10pm email panic.

---

## Cover Image Prompt (Gemini Nano Banana)

> Wide landscape course cover image, 16:9 aspect ratio. Clean modern design for a course module titled "The AI Transaction Coordinator." Dark teal background (#0F4C5C) with subtle gradient. In the center-left, large bold white sans-serif text "AI TRANSACTION COORDINATOR" with a thin warm amber (#E8A33D) underline accent beneath. Smaller white text below reads "Your whole pipeline. Handled in 15 min/day." On the right side, a minimal geometric illustration: three to four interconnected chain links or a clean horizontal timeline with nodes, rendered in amber and white — suggesting connected milestones, process flow, and coordination. No people, no photos, no clip art, no busy patterns. Ultra clean, professional, modern SaaS aesthetic. High contrast, legible at thumbnail size. Matches a deep teal and amber brand palette and feels visually distinct from other modules via the chain/timeline motif.

---

## Module 2 Lessons (10 Total — All Unlocked Once Module 0 Is Complete)

### Lesson 1: The AI TC System Overview (15 Minutes a Day)
**Format:** Talking head + simple diagram | 10-12 min
**Outcome:** Member understands the full TC workflow and the "daily 15" routine

**Covers:**
- What a transaction coordinator actually does (the unsexy list: timelines, documents, communication, deadlines, compliance)
- The math: most agents spend 2-4 hours per transaction in admin. With 5-10 files open at once, that's 20-40 hours/week on TC work alone.
- The "Daily 15" concept: open Cowork each morning, get a briefing on all active files, spend 15 minutes actioning what needs attention
- How Module 2 workflows stack: intake → timeline → inspections → documents → weekly updates → escrow/lender coordination → close
- Preview of the 10 lessons
- Why this module doesn't cover contract filling (and what to do in the meantime — fill forms in Authentisign like normal, just use everything else from this module)

---

### Lesson 2: Transaction Intake — Setting Up a New Deal
**Format:** Screen recording | 10-12 min
**Downloadable:** Transaction Intake Template + Deal File Structure
**Outcome:** Repeatable intake ritual that takes 5 minutes per new transaction

**Covers:**
- The moment an offer gets accepted — what do you do in the next 30 minutes?
- The transaction folder structure (in Cowork project or Google Drive):
  - Contract + addendums
  - Inspection reports (as they come in)
  - Disclosures (seller, HOA, title, lead paint, etc.)
  - Lender docs
  - Escrow docs
  - Communication log
  - Key dates sheet
- The Key Dates Sheet — the single most important document: EMD due, inspection period, loan contingency, appraisal, final walk, close date, possession
- Claude reads the contract and auto-extracts the key dates into the sheet
- Demo: Ryan runs intake on a real active transaction in under 5 minutes

---

### Lesson 3: The Timeline Tracker — Never Miss a Deadline Again
**Format:** Screen recording | 10-12 min
**Downloadable:** Timeline Tracker Prompt + Daily Briefing Prompt
**Outcome:** Morning briefing that surfaces every upcoming deadline across every file

**Covers:**
- The #1 thing that kills agents in transactions: missed deadlines. EMD not delivered, inspection objections missed, loan contingency not released, final walkthrough forgotten.
- The Daily Briefing prompt: "Give me a briefing on all my active transactions — any deadlines today, this week, or overdue"
- How Claude reads your Key Dates Sheets across all deals and flags what needs attention
- Color-coded urgency: red (today), yellow (this week), green (future)
- Integration with Google Calendar (Cowork can create calendar blocks for every deadline)
- Demo: live briefing run across Ryan's actual active files

---

### Lesson 4: The Inspection Response System
**Format:** Screen recording | 12-15 min
**Downloadable:** Inspection Summary Prompt + Repair Request Template
**Outcome:** Inspection report summary + client-ready explanation + drafted repair request in under 10 minutes

**Covers:**
- Inspection reports are 40-80 pages. Most agents skim and miss things.
- The Inspection Summary prompt: Claude reads the full PDF and outputs:
  - Executive summary (3-5 sentences)
  - Safety issues (must-fix)
  - Major defects (significant cost or risk)
  - Minor/cosmetic items (negotiable)
  - Items you can safely ignore
  - Client-ready explanation in plain English (no inspector jargon)
- The Repair Request Draft: based on the inspection, Claude drafts the actual repair request letter to the listing agent, with defensible negotiation framing
- Demo on a real inspection report (redacted for privacy)
- The Buyer Agent version vs. Seller Agent version of this workflow

---

### Lesson 5: Disclosure & Document Review (HOA, Title, Seller)
**Format:** Screen recording | 12-15 min
**Downloadable:** Document Review Prompt Library
**Outcome:** 200-page HOA packet read + summarized + red-flagged in under 5 minutes

**Covers:**
- The documents that matter and nobody reads carefully:
  - Seller Property Disclosure (SPDS in NV)
  - HOA CC&Rs, Rules, Financials, Minutes (the infamous HOA packet)
  - Title Commitment + Title Exceptions
  - Lead Paint Disclosure (if pre-1978)
  - Mello-Roos / Special Assessment disclosures
- The Red Flag Prompt: Claude reads the doc and outputs a list of "things your client needs to know" in plain English
- Specific things to flag: pending litigation, special assessments coming, easement issues, HOA reserve problems, title exceptions, deed restrictions
- How to present the findings to your client (clear, professional, CYA)
- Demo: Ryan runs an HOA packet through Claude and reads the red-flag list on screen

---

### Lesson 6: The Weekly Status Update System
**Format:** Screen recording | 10-12 min
**Downloadable:** Weekly Update Prompt (Buyer + Seller versions)
**Outcome:** Client status update sent every Friday, 30 seconds per file

**Covers:**
- Why most transactions feel chaotic to clients: agents communicate reactively. The fix: proactive weekly updates.
- The Friday Status Update: one email per active client, every Friday, summarizing:
  - Where we are in the timeline
  - What happened this week
  - What's coming up next week
  - What the client needs to do (if anything)
- Claude generates the update from your transaction folder in seconds
- Buyer version vs. Seller version (different info matters to each)
- The "no surprises" rule: clients who get Friday updates don't call you stressed on Tuesday
- Demo: Ryan runs the Friday Update across 3 real files

---

### Lesson 7: Escrow & Title Coordination
**Format:** Screen recording | 10-12 min
**Downloadable:** Escrow Email Templates (6 common situations)
**Outcome:** Every escrow/title communication handled in 30 seconds

**Covers:**
- The 6 emails you send escrow over and over:
  1. Initial intro + file info
  2. EMD delivery confirmation
  3. Document requests (CPL, preliminary title, wire instructions)
  4. Status check / timeline confirmation
  5. Problem escalation (title exceptions, delayed docs)
  6. Closing coordination (signing location, funding timeline)
- Same approach for title company communication
- How to escalate a stalled file without being rude
- Demo: live pulling an escrow update from Ryan's current file

---

### Lesson 8: Lender Coordination (Buyer Side)
**Format:** Screen recording | 10-12 min
**Downloadable:** Lender Coordination Email Templates + Appraisal Response Scripts
**Outcome:** Buyer-lender relationship managed proactively across every file

**Covers:**
- The buyer-lender handoff: the warm intro email that sets up the whole relationship
- Weekly loan status check-ins with the lender
- Appraisal coordination: scheduling, CMA packet to send to the appraiser, response to a low appraisal
- Loan contingency release: the email you send the day of
- Final underwriting conditions: tracking what the lender still needs from the buyer and nudging without being annoying
- What to do when the loan is behind schedule (escalation path)
- Demo: live lender status email generated from a real file

---

### Lesson 9: Post-Close Follow-Up (The 90-Day Sequence)
**Format:** Screen recording | 8-10 min
**Downloadable:** 90-Day Post-Close Sequence (8 touchpoints)
**Outcome:** Every closed client gets 8 automated touchpoints over 90 days

**Covers:**
- The #1 source of referrals: clients who just closed. Most agents drop the ball the day after closing.
- The 90-Day Sequence:
  - Day 1: Closing day congratulations + photo request
  - Day 3: "Everything okay?" check-in
  - Day 7: Service provider recommendations (handyman, cleaner, HVAC)
  - Day 14: Review request (Google, Zillow, realtor.com)
  - Day 30: "Moved in yet?" / housewarming note
  - Day 45: Referral ask — framed right, not pushy
  - Day 60: Anniversary reminder setup for future touchpoints
  - Day 90: Full move-in check, ask for feedback
- Claude personalizes every email based on the deal and the client
- Connecting this back to your CRM / database
- Demo: generating the full sequence for a real just-closed client

---

### Lesson 10: The One-Command Transaction (Cowork Integration)
**Format:** Screen recording | 12-15 min
**Downloadable:** Cowork TC Skill (installable)
**Outcome:** Single command runs the full daily TC routine

**Covers:**
- The payoff — everything connected in Cowork as a single skill
- Member types: "tc brief" — Cowork outputs:
  - Active transactions summary
  - Today's deadlines (red)
  - This week's deadlines (yellow)
  - Status emails due (Fridays)
  - Post-close touchpoints coming up
  - Any flagged issues (overdue items, missing docs)
- Then member types specific commands for each file: "draft the inspection response for 580 Celebratory" or "send the Friday update for all three sellers"
- Walkthrough of installing the skill
- Customizing it to your market, your templates, your process
- Demo: Ryan runs a full Daily 15 on camera — morning briefing, 3-4 actions, done in 15 minutes
- Browser users: provided as a set of prompt templates that replicate the workflow manually

---

## Module 2 Assets Checklist

| Asset | Type | Length | Status |
|-------|------|--------|--------|
| Lesson 1: AI TC Overview | Talking head + diagram | 10-12 min | [ ] |
| Lesson 2: Transaction Intake | Screen recording | 10-12 min | [ ] |
| Lesson 3: Timeline Tracker | Screen recording | 10-12 min | [ ] |
| Lesson 4: Inspection Response | Screen recording | 12-15 min | [ ] |
| Lesson 5: Disclosure Review | Screen recording | 12-15 min | [ ] |
| Lesson 6: Weekly Status Updates | Screen recording | 10-12 min | [ ] |
| Lesson 7: Escrow & Title | Screen recording | 10-12 min | [ ] |
| Lesson 8: Lender Coordination | Screen recording | 10-12 min | [ ] |
| Lesson 9: Post-Close Follow-Up | Screen recording | 8-10 min | [ ] |
| Lesson 10: One-Command TC | Screen recording | 12-15 min | [ ] |
| Transaction Intake Template | Download | — | [ ] |
| Deal File Structure Guide | Download | — | [ ] |
| Timeline Tracker Prompt | Template | — | [ ] |
| Daily Briefing Prompt | Template | — | [ ] |
| Inspection Summary Prompt | Template | — | [ ] |
| Repair Request Template | Template | — | [ ] |
| Document Review Prompt Library | Templates (5+) | — | [ ] |
| Weekly Update Prompts | Templates (buyer + seller) | — | [ ] |
| Escrow Email Templates (6) | Templates | — | [ ] |
| Lender Coordination Templates | Templates | — | [ ] |
| Appraisal Response Scripts | Templates | — | [ ] |
| 90-Day Post-Close Sequence | Template set (8 emails) | — | [ ] |
| Cowork TC Skill | Installable skill | — | [ ] |
| TC Master Prompt (browser fallback) | Template | — | [ ] |

**Total recording time:** ~110-130 minutes of content (10 videos)
**Total member time commitment:** Completable in a weekend. Produces immediate ROI on next active transaction.

---

## Skool Settings Summary

| Setting | Value |
|---------|-------|
| Module 2 tile visibility | Visible to all members (title + description shown) |
| Prerequisite | **Module 0 complete** (Module 1 NOT required) |
| Module 2 lessons | Locked until Module 0 is complete |
| Once unlocked | All 10 Module 2 lessons unlock at once — no internal gates |
| All lesson titles visible before unlock? | Yes — motivates Module 0 completion |

---

## YouTube Strategy

Same pattern as Modules 0 and 1:
- Each lesson gets a standalone YouTube video (public, free)
- Each lesson gets a YouTube description with timestamps, prompt template, links
- Each lesson gets 5 Instagram Shorts (Teaser, Quick Win, Before/After, Hot Take, Math)
- Lesson 10 (One-Command TC) is the flagship video for this module — the "Daily 15" concept is sticky and memorable, pitch the community off this

---

## Module 2.5: Contract Automation (Future / Placeholder)

When Authentisign/Lone Wolf API access is figured out, build this as a separate advanced module:
- Programmatic form filling using the Transact API (Forms Editor + Authentisign endpoints)
- Cowork skill that drafts field values, writes them to the official forms, generates the PDF, and creates the signing envelope
- Target: full contract lifecycle from verbal acceptance to envelope sent for signature, fully automated
- Gated behind Module 2 completion
- Likely requires Lone Wolf partnership agreement + API licensing

For now, document this as "coming when the partnership pieces are in place." Don't promise a timeline.

---

## Design Notes

- **Module 2 justifies the membership for buyer agents** — Module 1 was all about listings. Module 2 is for agents whose pain is the transaction side. This expands the community's audience.
- **The "Daily 15" is the sticky concept** — members need a simple daily ritual to anchor the whole module. "Open Cowork in the morning, do the Daily 15, your transactions are handled." Lead with that in marketing.
- **Inspection response is the "holy shit" moment** — a 60-page inspection turned into a summary + drafted response in 10 minutes. That's the lesson that sells the module.
- **Post-close follow-up is the stealth win** — it doesn't sound sexy, but agents who follow up consistently get 2-3x more referrals. This lesson alone can pay for the community.
- **Don't promise contract filling** — until the Lone Wolf path is real, leave it out of the marketing. Over-promise is a killer.
