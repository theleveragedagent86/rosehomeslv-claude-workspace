# Cowork Prompt — Build Rosa Point by Beazer Homes Smart Plans in Lofty

Copy and paste this entire prompt into Claude Cowork to build the 3 community smart plans.

---

## PROMPT START

You are the Lofty Automation Builder. Your job is to build 3 Smart Plans (Action Plans) inside Lofty CRM using computer use tools. You will navigate the Lofty interface, create each plan, and add every step by reading the content file on disk.

The 3 plans are: **Rosa Point by Beazer Homes - Hot**, **Rosa Point by Beazer Homes - Warm**, **Rosa Point by Beazer Homes - Nurture**. They share Day 0 actions and a Day 35 handoff to "Long Term Nurture - Buyer", but the per-track touches differ as specified in the smart plan blueprint.

---

## Prerequisites

- Browser open with Lofty CRM logged in. Smart Plans page URL: `https://crm.lofty.com/admin/home/campaigns/smartPlan?gtaParam=list&tagType=myPlan`
- You have computer use tools (screenshot, click, type, navigate)
- The smart plan content file is at: `/Users/ryanrose/Downloads/Claude/New-Construction/rosa-point-by-beazer-homes/smart-plan.md`
- The DO/BBRA PDF attachment is at: `/Users/ryanrose/Downloads/Claude/New-Construction/DO.BBRA - Template/Duties Owed and BBRA.pdf`

---

## Step 1: Navigate to Smart Plans

1. Open Chrome and navigate directly to the Smart Plans page: `https://crm.lofty.com/admin/home/campaigns/smartPlan?gtaParam=list&tagType=myPlan`
2. Take a screenshot to verify you are logged in as Ryan Rose and landed on the Smart Plans list page

**If redirected to login:** Pause and tell the user "Please log into Lofty CRM. Let me know when you're ready."

---

## Step 2: Create the Trigger Tag

1. Navigate to CRM → Tags (or Settings → Tags)
2. Create the tag: `rosa-point-by-beazer-homes` (lowercase, exact spelling)
3. Take a screenshot confirming the tag exists

---

## Step 3: Read the Content File

Before adding steps, read the smart plan content file:
- `/Users/ryanrose/Downloads/Claude/New-Construction/rosa-point-by-beazer-homes/smart-plan.md`

The file contains all 3 tracks (Hot, Warm, Nurture) with every touch numbered, the delay, the action type (Email / Text / Call Task / Trigger Plan), the subject line (for emails), the body copy, and which tracks each touch applies to.

---

## Step 4: Build Plan 1 — `Rosa Point by Beazer Homes - Hot`

1. Click **+ New Plan** (or **Create New Plan**)
2. Set the Plan Name: `Rosa Point by Beazer Homes - Hot`
3. Trigger: **Tag Applied → `rosa-point-by-beazer-homes`** (only fires when lead also qualifies as Hot — manual track sort by Ryan, OR automatic if Lofty supports trigger conditions)
4. Enable **Stop on Reply**
5. Set Email sender: **Ryan Rose (ryan@rosehomeslv.com)**
6. Set Text business hours: **9:00 AM – 7:00 PM PT**

For each touch in the smart-plan.md sequence that applies to **Hot**:

- Click **Add Step** (or **+** / **Add Action**)
- Pick the action type:
  - **Send Email** for Email touches
  - **Send Text/SMS** for Text touches
  - **Create Task** (Call) for Call Task touches
  - **Start Another Action Plan** for the Day 35 handoff
- Set the **delay** (Lofty uses RELATIVE delays from the previous step — calculate from the absolute Day numbers in the blueprint)
- Paste the **subject line** (Email only) and the **body** exactly as written in `smart-plan.md`
- For the Day 0 lead email (Touch 2): **attach** the DO/BBRA PDF from `/Users/ryanrose/Downloads/Claude/New-Construction/DO.BBRA - Template/Duties Owed and BBRA.pdf`
- For the Day 0 builder notification email (Touch 3): set the **recipient to ryan@rosehomeslv.com** (NOT the lead)
- Verify Lofty's `#lead_first_name#` merge field renders. If Lofty uses a visual chip insert, use that and replace every `#lead_first_name#` in the body
- Set every send to **Automated**, not manual
- Save each step

Expected total Hot touches: **17**.

After all Hot touches are added:
- Take a screenshot of the plan overview
- Save and **Activate** the plan (if Lofty has a Draft → Active toggle)

---

## Step 5: Build Plan 2 — `Rosa Point by Beazer Homes - Warm`

Repeat Step 4 for the Warm track:
- Plan Name: `Rosa Point by Beazer Homes - Warm`
- Trigger: **Tag Applied → `rosa-point-by-beazer-homes`** (default for landing-page leads)
- Same Stop-on-Reply, sender, and business-hours settings
- Add only the touches in `smart-plan.md` marked for the Warm track (skip Touch 4, the Hot-only call task)
- Day 0 lead email gets the DO/BBRA PDF attached
- Builder notification email goes to ryan@rosehomeslv.com

Expected total Warm touches: **16**.

---

## Step 6: Build Plan 3 — `Rosa Point by Beazer Homes - Nurture`

Repeat Step 4 for the Nurture track:
- Plan Name: `Rosa Point by Beazer Homes - Nurture`
- Trigger: **Tag Applied → `rosa-point-by-beazer-homes`** (browsing leads)
- Same settings
- Add only the touches marked for Nurture (skip Touch 4 the Hot-only call task, and skip Touch 6 the Hot+Warm voicemail task)
- Day 0 lead email gets the DO/BBRA PDF attached
- Builder notification email goes to ryan@rosehomeslv.com

Expected total Nurture touches: **15**.

---

## Step 7: Verify After Each Plan

After each plan is saved:
1. Screenshot the plan overview
2. Count the steps and confirm they match the expected totals above
3. Spot-check the Day 0 email body (DO/BBRA paragraph present), the Day 35 handoff (Start Another Action Plan → "Long Term Nurture - Buyer"), and the builder notification recipient

---

## Step 8: Final Check

Once all 3 plans are saved and active:
1. Confirm the tag `rosa-point-by-beazer-homes` is wired to all 3 plans
2. Confirm Stop-on-Reply is enabled on all 3
3. Confirm the DO/BBRA PDF is attached to every Day 0 lead email (3 plans × 1 attachment)
4. Confirm "Long Term Nurture - Buyer" is referenced in the Day 35 handoff for all 3 plans
5. Take a final screenshot of the Smart Plans list showing all 3 active plans

Total steps across all 3 plans: **48** (Hot 17 + Warm 16 + Nurture 15).

---

## Step 9: Build Log

Write a build log to `/Users/ryanrose/Downloads/Claude/New-Construction/rosa-point-by-beazer-homes/cowork-build-log.md` with:
- Total steps created per plan vs expected (Hot 17, Warm 16, Nurture 15)
- Any errors and how they were resolved
- Lofty's actual merge-field format if it differed from `#lead_first_name#`
- Whether all 3 plans are active
- Whether the tag was created correctly
- Any manual fixes still needed

---

## Error Recovery

- **Browser crash:** Reopen Lofty, find the partially-built plan, continue from the last verified step count.
- **Step save fails:** Screenshot the error, retry once, then log it for manual fix.
- **Step limit reached:** Stop and tell the user. We may need to split the plan.
- **Lofty redesigns the UI:** Take a screenshot, describe what you see, and ask the user to confirm the new flow before continuing.

---

## Placeholder Note

The content uses `#lead_first_name#` and `#lead_phone#`. If Lofty's editor shows a visual chip / "Insert Merge Field" button, use that native method and replace every raw `#lead_first_name#` and `#lead_phone#` in the body with the visual chip.

---

## PROMPT END
