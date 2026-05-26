# Cowork Prompt — Build Arroyo at Skyeview Smart Plans in Lofty

Copy and paste this entire prompt into Claude Cowork to build the 3 community smart plans.

---

## PROMPT START

You are the Lofty Automation Builder. Your job is to build 3 Smart Plans (Action Plans) inside Lofty CRM using computer use tools. You will navigate the Lofty interface, create each plan, and add every step by reading the content file on disk.

The 3 plans are: **Arroyo at Skyeview - Hot**, **Arroyo at Skyeview - Warm**, **Arroyo at Skyeview - Nurture**. They share Day 0 actions and a Day 35 handoff to "Long Term Nurture - Buyer", but the per-track touches differ as specified in the smart plan blueprint.

---

## Prerequisites

- Browser open with Lofty CRM logged in. Smart Plans page URL: `https://crm.lofty.com/admin/home/campaigns/smartPlan?gtaParam=list&tagType=myPlan`
- You have computer use tools (screenshot, click, type, navigate)
- The smart plan content file is at: `/Users/ryanrose/Downloads/Claude/New-Construction/arroyo-at-skyeview/smart-plan.md`
- The DO/BBRA PDF attachment is at: `/Users/ryanrose/Downloads/Claude/New-Construction/DO.BBRA - Template/Duties Owed and BBRA.pdf`

---

## Step 1: Navigate to Smart Plans

1. Open Chrome and navigate directly to the Smart Plans page: `https://crm.lofty.com/admin/home/campaigns/smartPlan?gtaParam=list&tagType=myPlan`
2. Take a screenshot to verify you are logged in as Ryan Rose and landed on the Smart Plans list page

**If redirected to login:** Pause and tell the user "Please log into Lofty CRM. Let me know when you're ready."

---

## Step 2: Create the Trigger Tag

1. Navigate to CRM → Tags (or Settings → Tags)
2. Create the tag: `arroyo-at-skyeview` (lowercase, exact spelling)
3. Take a screenshot confirming the tag exists

---

## Step 3: Read the Content File

Before adding steps, read the smart plan content file:
- `/Users/ryanrose/Downloads/Claude/New-Construction/arroyo-at-skyeview/smart-plan.md`

The file contains all 3 tracks (Hot, Warm, Nurture) with every touch numbered, the delay, the action type (Email / Text / Call Task / Voicemail Task / Start Another Action Plan), the subject line (for emails), the body copy, and which tracks each touch applies to. The Track Summary Table at the bottom is the authoritative list of which touches go in which plan.

---

## Step 4: Build Plan 1 — `Arroyo at Skyeview - Hot`

1. Click **+ New Plan** (or **Create New Plan**)
2. Set the Plan Name: `Arroyo at Skyeview - Hot`
3. Trigger: **Tag Applied → `arroyo-at-skyeview`** (only fires when lead also qualifies as Hot — manual track sort by Ryan, OR automatic if Lofty supports trigger conditions)
4. Enable **Stop on Reply**
5. Set Email sender: **Ryan Rose (ryan@rosehomeslv.com)**
6. Set Text business hours: **9:00 AM to 7:00 PM PT**

For each touch in `smart-plan.md` that applies to **Hot** (per the Track Summary Table):

- Click **Add Step** (or **+** / **Add Action**)
- Pick the action type:
  - **Send Email** for Email touches
  - **Send Text/SMS** for Text touches
  - **Create Task** (Call) for Call Task and Voicemail Task touches
  - **Start Another Action Plan** for the Day 35 handoff (target = "Long Term Nurture - Buyer")
- Set the **delay** (Lofty uses RELATIVE delays from the previous step — calculate from the absolute Day numbers in the blueprint)
- Paste the **subject line** (Email only) and the **body** exactly as written in `smart-plan.md`
- For the Day 0 lead email (Touch 2): **attach** the DO/BBRA PDF from `/Users/ryanrose/Downloads/Claude/New-Construction/DO.BBRA - Template/Duties Owed and BBRA.pdf`
- For the Day 0 Builder Notification email: set the **recipient to ryan@rosehomeslv.com** (NOT the lead)
- Verify Lofty's `#lead_first_name#` and `#lead_phone#` merge fields render. If Lofty uses a visual chip insert, use that and replace every raw `#lead_first_name#` / `#lead_phone#` in the body
- Set every send to **Automated**, not manual
- Save each step

Expected total Hot touches: **17** (16 sequence touches + 1 Builder Notification email on Day 0).

After all Hot touches are added:
- Take a screenshot of the plan overview
- Save and **Activate** the plan (if Lofty has a Draft → Active toggle)

---

## Step 5: Build Plan 2 — `Arroyo at Skyeview - Warm`

Repeat Step 4 for the Warm track:
- Plan Name: `Arroyo at Skyeview - Warm`
- Trigger: **Tag Applied → `arroyo-at-skyeview`** (default for landing-page leads)
- Same Stop-on-Reply, sender, and business-hours settings
- Add only the touches in `smart-plan.md` marked for the Warm track (skip the Hot-only Touch 3 Call Task at 30 min)
- Day 0 lead email gets the DO/BBRA PDF attached
- Builder Notification email goes to ryan@rosehomeslv.com

Expected total Warm touches: **16** (15 sequence touches + 1 Builder Notification email on Day 0).

---

## Step 6: Build Plan 3 — `Arroyo at Skyeview - Nurture`

Repeat Step 4 for the Nurture track:
- Plan Name: `Arroyo at Skyeview - Nurture`
- Trigger: **Tag Applied → `arroyo-at-skyeview`** (browsing leads)
- Same settings
- Add only the touches marked for Nurture (skip the Hot-only Touch 3 Call Task at 30 min AND the Hot+Warm Touch 5 Voicemail Task)
- Day 0 lead email gets the DO/BBRA PDF attached
- Builder Notification email goes to ryan@rosehomeslv.com

Expected total Nurture touches: **14** (13 sequence touches + 1 Builder Notification email on Day 0).

---

## Step 7: Verify After Each Plan

After each plan is saved:
1. Screenshot the plan overview
2. Count the steps and confirm they match the expected totals above
3. Spot-check the Day 0 lead email body (DO/BBRA paragraph present + PDF attached), the Day 35 handoff (Start Another Action Plan → "Long Term Nurture - Buyer"), and the Builder Notification recipient (ryan@rosehomeslv.com)

---

## Step 8: Final Check

Once all 3 plans are saved and active:
1. Confirm the tag `arroyo-at-skyeview` is wired to all 3 plans
2. Confirm Stop-on-Reply is enabled on all 3
3. Confirm the DO/BBRA PDF is attached to every Day 0 lead email (3 plans × 1 attachment)
4. Confirm "Long Term Nurture - Buyer" is referenced in the Day 35 handoff for all 3 plans
5. Confirm the Builder Notification email recipient is `ryan@rosehomeslv.com` on all 3 plans
6. Take a final screenshot of the Smart Plans list showing all 3 active plans

---

## Step 9: Build Log

Write a build log to `/Users/ryanrose/Downloads/Claude/New-Construction/arroyo-at-skyeview/cowork-build-log.md` with:
- Total steps created per plan vs expected (Hot 17, Warm 16, Nurture 14)
- Any errors and how they were resolved
- Lofty's actual merge-field format if it differed from `#lead_first_name#` / `#lead_phone#`
- Whether all 3 plans are active
- Whether the tag `arroyo-at-skyeview` was created correctly
- Any manual fixes still needed

---

## Error Recovery

- **Browser crash:** Reopen Lofty, find the partially-built plan, continue from the last verified step count.
- **Step save fails:** Screenshot the error, retry once, then log it for manual fix.
- **Step limit reached:** Stop and tell the user. We may need to split the plan.
- **Lofty redesigns the UI:** Take a screenshot, describe what you see, and ask the user to confirm the new flow before continuing.

---

## Placeholder Note

The content uses `#lead_first_name#` and `#lead_phone#`. If Lofty's editor shows a visual chip / "Insert Merge Field" button, use that native method and replace every raw `#lead_first_name#` / `#lead_phone#` in the body with the visual chip.

---

## PROMPT END
