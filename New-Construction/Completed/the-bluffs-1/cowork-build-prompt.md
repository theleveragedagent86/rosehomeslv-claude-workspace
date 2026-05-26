# Cowork Prompt — Build The Bluffs I Smart Plans in Lofty

Copy and paste this entire prompt into Claude Cowork to build the 3 community smart plans.

---

## PROMPT START

You are the Lofty Automation Builder. Your job is to build 3 Smart Plans (Action Plans) inside Lofty CRM using computer use tools. You will navigate the Lofty interface, create each plan, and add every step by reading the content file on disk.

The 3 plans are: **The Bluffs I - Hot**, **The Bluffs I - Warm**, **The Bluffs I - Nurture**. They share Day 0 actions and a Day 35 handoff to "Long Term Nurture - Buyer", but the per-track touches differ as specified in the smart plan blueprint.

## Prerequisites
- Browser open with Lofty CRM logged in. Smart Plans page URL: `https://crm.lofty.com/admin/home/campaigns/smartPlan?gtaParam=list&tagType=myPlan`
- You have computer use tools (screenshot, click, type, navigate)
- The smart plan content file is at: `/Users/ryanrose/Downloads/Claude/New-Construction/the-bluffs-1/smart-plan.md`
- The DO/BBRA PDF is at: `/Users/ryanrose/Downloads/Claude/New-Construction/DO.BBRA - Template/Duties Owed and BBRA.pdf`

## Step 1: Navigate to Smart Plans
1. Open Chrome and navigate directly to the Smart Plans page: `https://crm.lofty.com/admin/home/campaigns/smartPlan?gtaParam=list&tagType=myPlan`
2. Screenshot to verify Ryan Rose is logged in and on the Smart Plans list page

If redirected to login: pause and tell user "Please log into Lofty CRM. Let me know when you're ready."

## Step 2: Create the Trigger Tag
1. Navigate to CRM → Tags (or Settings → Tags)
2. Create the tag: `the-bluffs-1` (lowercase, exact spelling, no prefix, no spaces)
3. Screenshot confirming the tag exists in the tag list
4. If the tag already exists, skip creation and continue

## Step 3: Read the Content File
Read `/Users/ryanrose/Downloads/Claude/New-Construction/the-bluffs-1/smart-plan.md`. This file contains all 3 tracks (Hot, Warm, Nurture) with every touch, full copy, subject lines, task scripts, and the Track Summary table that maps which touches go into which plan.

Also note these expected counts so you can verify nothing was dropped:
- The Bluffs I - Hot: 16 touches
- The Bluffs I - Warm: 15 touches
- The Bluffs I - Nurture: 14 touches
- **Total steps across all 3 plans: 45**

## Step 4: Build Plan 1 — `The Bluffs I - Hot`

### 4a. Create the plan
1. Click "Create New Smart Plan" (or "New Action Plan")
2. Plan name: `The Bluffs I - Hot`
3. Description: `Hot track for The Bluffs I by Century Communities. ASAP or 1-3 month buyers who are already pre-approved.`
4. Settings:
   - Stop on reply: **ON**
   - Business hours for texts: **9:00 AM - 7:00 PM PT**
   - Email sender: **Ryan Rose (ryan@rosehomeslv.com)**
5. Save the plan shell. Screenshot.

### 4b. Add steps in order (16 touches)
For each touch, click "Add Step" → pick the right type → fill in the content from `smart-plan.md`. Use exact subject lines and exact body copy. Keep `#lead_first_name#` and `#lead_phone#` and `#signature#` as literal strings (do NOT replace them).

Step-by-step:

1. **Day 0, Immediate** — Text. Use Touch 1 body verbatim.
2. **Day 0, Immediate** — Email. Subject: `The Bluffs I homes you were looking at`. Body: Touch 2 body verbatim. **Attach** the DO/BBRA PDF from `/Users/ryanrose/Downloads/Claude/New-Construction/DO.BBRA - Template/Duties Owed and BBRA.pdf`.
3. **Day 0, Immediate** — Internal Email to ryan@rosehomeslv.com. Subject: `New Lead for The Bluffs I by Century Communities - #lead_first_name#`. Body: the full Builder Rep Notification block from `smart-plan.md`.
4. **Day 0, +30 min** — Call Task. Title and notes from Touch 3.
5. **Day 1, 10:00 AM** — Text. Touch 4 body verbatim.
6. **Day 1, 12:00 PM** — Voicemail Task. Title and script from Touch 5.
7. **Day 3** — Email. Subject: `The Bluffs I builder incentives you should know about`. Body: Touch 6 verbatim.
8. **Day 5, 10:00 AM** — Text. Touch 7 verbatim.
9. **Day 7** — Email. Subject: `How The Bluffs I compares to other Lake Las Vegas new builds`. Body: Touch 8 verbatim.
10. **Day 7, 2:00 PM** — Call Task. Title and script from Touch 9.
11. **Day 10, 9:30 AM** — Text. Touch 10 verbatim.
12. **Day 14** — Email. Subject: `Honest question, #lead_first_name#`. Body: Touch 11 verbatim.
13. **Day 14, 3:00 PM** — Call Task. Title and script from Touch 12.
14. **Day 21** — Email. Subject: `Lake Las Vegas market update for you`. Body: Touch 13 verbatim.
15. **Day 30** — Email. Subject: `Monthly The Bluffs I update`. Body: Touch 14 verbatim.
16. **Day 30, 2:00 PM** — Text. Touch 15 verbatim.
17. **Day 35** — Smart Plan Trigger / Start Another Action Plan: `Long Term Nurture - Buyer`.

(Note: the internal builder-rep notification on Day 0 is counted as part of Touch 2 in the blueprint table, so the user-facing touch count is 16. Lofty itself will store 17 step rows because the internal notification is its own action.)

### 4c. Save the plan
1. Click "Save" or "Activate"
2. Screenshot the final step list
3. Verify the step count matches expected (16 user-facing touches plus the internal notification action)

Expected total Hot touches: **16**.

## Step 5: Build Plan 2 — `The Bluffs I - Warm`

Repeat Step 4 with these adjustments:
- Plan name: `The Bluffs I - Warm`
- Description: `Warm track for The Bluffs I. 1-3 or 3-6 month timeline, any pre-approval. Default plan for landing page leads.`
- **Skip Touch 3** (the HOT-only call task at Day 0 +30 min)
- All other touches match the Hot plan exactly

Expected total Warm touches: **15**.

## Step 6: Build Plan 3 — `The Bluffs I - Nurture`

Repeat Step 4 with these adjustments:
- Plan name: `The Bluffs I - Nurture`
- Description: `Nurture track for The Bluffs I. Just browsing leads, any pre-approval. Slower cadence, no voicemail.`
- **Skip Touch 3** (HOT-only call task)
- **Skip Touch 5** (voicemail, HOT + WARM only)
- All other touches match

Expected total Nurture touches: **14**.

## Step 7: Verify Each Plan

For each of the 3 plans:
1. Open the plan
2. Screenshot the full step list
3. Count steps and confirm they match the expected count
4. Spot-check:
   - Day 0 lead email has DO/BBRA PDF attached
   - Day 0 has the internal builder rep notification to ryan@rosehomeslv.com
   - Day 35 is a "Start Another Action Plan" pointing at `Long Term Nurture - Buyer`
   - Stop on reply is ON
   - Business hours = 9 AM - 7 PM PT
   - Email sender = Ryan Rose
5. Confirm `#lead_first_name#`, `#lead_phone#`, and `#signature#` are present as literal strings (not pre-filled)

## Step 8: Final Check

- All 3 plans are saved and set to Active
- The `the-bluffs-1` tag exists and is wired to auto-start the appropriate plan (default = Warm for landing page leads)
- Stop on reply is ON for all 3
- DO/BBRA PDF is attached on Day 0 Touch 2 in all 3 plans
- Day 35 handoff to `Long Term Nurture - Buyer` is wired in all 3 plans
- Total step rows across all 3 plans should land at approximately **45** (16 + 15 + 14, with internal notification rows added per plan)

## Step 9: Build Log

Write a build log to `/Users/ryanrose/Downloads/Claude/New-Construction/the-bluffs-1/cowork-build-log.md` with:

- Timestamp build started and finished
- Plans created (with the exact name as saved in Lofty)
- Step counts per plan (actual versus expected)
- Tag created or already existing
- DO/BBRA attachment status per plan (attached / not attached)
- Day 35 handoff target verified per plan
- Any errors hit during build, what you tried, and how you resolved them
- Any manual items left for Ryan to finish (for example, double-checking that the landing page form and Meta lead form ad both apply the `the-bluffs-1` tag, or wiring the qualifying-answer routing to assign Hot vs Warm vs Nurture)

## Error Recovery

- **Browser crash mid-build:** Reopen Lofty, find the partially built plan, pick up at the next missing step. Do not start over from scratch.
- **Step save fails:** Screenshot the error, retry the save once, then if it still fails, log the failure in the build log and skip to the next step. Flag it for Ryan to add manually.
- **Lofty hits a step limit on a single plan:** Log it, save what you have, and tell Ryan how many steps fit so he can either upgrade the plan tier or split the plan in two.
- **Lofty UI redesign breaks selectors:** If buttons or fields have moved, screenshot the current UI and describe what you see, then proceed using your best inference of which control matches the action. Log every UI guess in the build log so Ryan can audit.
- **Tag already exists or already wired to a different plan:** Do not create a duplicate. Confirm the existing tag, log it, and proceed.
- **Lead variable not available in Lofty's variable picker:** Type the literal string `#lead_first_name#` or `#lead_phone#` directly into the field. Do not substitute.

## PROMPT END
