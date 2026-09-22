# Cowork Build Log: Southwind by Century Communities Smart Plans

**Built by:** Claude (Cowork mode)
**Completed:** May 2026
**Lofty account:** ryan@rosehomeslv.com
**Blueprint source:** `smart-plan.md` (same folder)

---

## What Was Built

Three Lofty Smart Plans for the Southwind by Century Communities lead funnel:

| Plan Name | Tracks | Touches | Duration |
|-----------|--------|---------|----------|
| Southwind by Century Communities - Hot | Hot | 17 (incl. builder notification + Day 0 call task) | 35 days |
| Southwind by Century Communities - Warm | Warm | 16 (incl. builder notification) | 35 days |
| Southwind by Century Communities - Nurture | Nurture | 15 (incl. builder notification) | 35 days |

---

## Trigger

- **Tag:** `Century-Southwind`
- **Auto-Pause:** Enabled on lead reply ("The lead responds / reaches out")
- **Business hours (texts):** 9 AM - 7 PM PT
- **Email sender:** Ryan Rose (ryan@rosehomeslv.com)

---

## Touch Summary (All Plans)

| Touch | Day | Channel | Hot | Warm | Nurture |
|-------|-----|---------|-----|------|---------|
| Builder Notification | 0 | Email to ryan@ | X | X | X |
| 1 | 0 | Text | X | X | X |
| 2 | 0 | Email (with PDF) | X | X | X |
| 3 | 0 +30 min | Call Task | X | | |
| 4 | 1 | Text | X | X | X |
| 5 | 1 | Voicemail Task | X | X | |
| 6 | 3 | Email | X | X | X |
| 7 | 5 | Text | X | X | X |
| 8 | 7 | Email | X | X | X |
| 9 | 7 | Call Task | X | X | X |
| 10 | 10 | Text | X | X | X |
| 11 | 14 | Email | X | X | X |
| 12 | 14 | Call Task | X | X | X |
| 13 | 21 | Email | X | X | X |
| 14 | 30 | Email | X | X | X |
| 15 | 30 | Text | X | X | X |
| 16 (handoff) | 35 | Start Smart Plan | X | X | X |

Day 35 handoff: "Start Another Action Plan" set to **Long Term Nurture - Buyer** in all 3 plans.

---

## Action Required: Attach PDF to Day 0 Email

The Duties Owed and BBRA PDF was not attached during the automated build and must be manually added to the Day 0 email node in each plan.

**How to attach:**
1. Open the plan in Lofty (Marketing > Smart Plans)
2. Click into the Day 0 Auto Email node (Touch 2, subject: "The Southwind homes you were looking at")
3. In the email editor toolbar, click the **three dots (...)** to expand additional options
4. Click the **paperclip icon** to attach a file
5. Upload the PDF from: `New-Construction/DO.BBRA - Template/Duties Owed and BBRA.pdf`

Do this for all 3 plans (Hot, Warm, Nurture).

---

## Action Required: Verify Nurture Plan Step Delays

The Nurture plan shows **0 day duration** in the Smart Plans list, while Hot and Warm show 36 days. This suggests the step delays (Day 1, Day 3, Day 5, etc.) may not have been saved on the Nurture plan nodes.

**How to verify:**
1. Open Southwind by Century Communities - Nurture in Lofty
2. Click each node and confirm its delay matches the blueprint in `smart-plan.md`
3. If delays are missing, re-enter them per the blueprint and save the plan

---

## Canvas Build Notes

- Canvas execution order in Lofty is **bottom to top** (nodes with the highest SVG y-value fire first)
- The trigger node (WHEN tag applied) sits at the top of the canvas; all action nodes hang below it in reverse execution order
- Each plan was built node by node from the first-firing action (builder notification) up to the last-firing action (Day 35 handoff)
- The "Add a Step" button (`div.plus` inside SVG foreignObject elements) was used to add each node above the previous one

---

## Files in This Folder

| File | Purpose |
|------|---------|
| `smart-plan.md` | Full blueprint: all copy, delays, subjects, and setup instructions |
| `cowork-build-log.md` | This file |
