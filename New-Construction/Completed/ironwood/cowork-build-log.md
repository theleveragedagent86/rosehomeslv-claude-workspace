# Lofty Smart Plan Build Log — Ironwood by Century Communities
## Sessions: 2026-05-16 (steps built) + 2026-05-17 (delays configured)
## Status: COMPLETE

---

## What Was Built

All 3 Smart Plans for Ironwood by Century Communities were created in Lofty CRM:

| Plan Name | Steps | Wait Conditions | Duration | Status |
|-----------|-------|----------------|----------|--------|
| Ironwood - Hot | 17 | 10 | 35 days | ✅ Complete |
| Ironwood - Warm | 16 | 10 | 35 days | ✅ Complete |
| Ironwood - Nurture | 15 | 9 | 35 days | ✅ Complete |

---

## Plan Details

### Ironwood - Hot (17 steps)
Built from scratch in the Lofty Smart Plan builder (accessed via gear → Edit on the plan list page).

Steps built:
1. Auto Text (Touch 1, Day 0) — Opening text to lead
2. Auto Email (Touch 2, Day 0) — "The Ironwood homes you were looking at" + Duties Owed and BBRA.pdf attached
3. Notification (Touch 3, Day 0) — Builder rep notification to ryan@rosehomeslv.com
4. Call Task (Touch 4, HOT ONLY, 30-min delay) — "HOT LEAD. #lead_first_name# is ready to buy..."
5. Auto Text (Touch 5, Day 1, 10:00 AM) — "Ironwood Day 1 Text"
6. Custom Task / Voicemail (Touch 6, Day 1, 12:00 PM) — Voicemail script to #lead_first_name#
7. Auto Email (Touch 7, Day 3) — "Ironwood builder incentives you should know about"
8. Auto Text (Touch 8, Day 5, 10:00 AM) — "Ironwood Day 5 Text"
9. Auto Email (Touch 9, Day 7) — "How Ironwood compares to other new builds in Southwest Las Vegas"
10. Call Task (Touch 10, Day 7, 2:00 PM) — Week 1 check-in call
11. Auto Text (Touch 11, Day 10, 9:30 AM) — "Ironwood Day 10 Text" — quick move-in heads up
12. Auto Email (Touch 12, Day 14) — "Honest question, #lead_first_name#"
13. Call Task (Touch 13, Day 14, 3:00 PM) — Check-in call
14. Auto Email (Touch 14, Day 21) — "Southwest Las Vegas market update for you"
15. Auto Email (Touch 15, Day 30) — "Monthly Ironwood update"
16. Auto Text (Touch 16, Day 30, 2:00 PM) — "Ironwood Day 30 Text"
17. Start Smart Plan (Touch 17, Day 35) → "Long Term Nurture - Buyer"

### Ironwood - Warm (16 steps)
Created by copying Ironwood - Hot and deleting Step 4 (HOT-only Call Task at 30 minutes).
- Skips Touch 4 (the immediate 30-min call task)
- All other 16 steps are identical to Hot

### Ironwood - Nurture (15 steps)
Created by copying Ironwood - Warm and deleting the Voicemail Task (Custom Task, Touch 6 / Day 1, 12:00 PM).
- Skips Touch 4 (no call task)
- Skips Touch 6 (no voicemail task)
- All other 15 steps are identical to Hot/Warm

---

## Trigger Settings
All 3 plans are configured with:
- **Trigger:** Tag Changed → `Century-Ironwood`
- **Target Lead Type:** Equals To: Buyer
- **Auto Pause Setting:** Stop on reply (configured from previous session)

---

## Key UI Discoveries This Session

1. **Edit mode vs View mode:** Clicking a plan name opens VIEW mode (read-only). The gear icon → Edit opens the actual EDIT mode with the flow builder and "+" buttons on connectors.

2. **Adding steps:** In edit mode, click the "+" circle on a connector between steps → "Add a Step" popup → choose "Action" or "Condition".

3. **Delay configuration:** The delay mechanism is via "Condition" → "Wait a Period of Time" step inserted between actions. This panel appears automatically after saving each action. For task actions (Call, Custom Task), delays can also be set within the task form via the "Due Date" section.

4. **Action types:**
   - Communication: Auto Email, Auto Text, Notification, Slybroadcast, etc.
   - Manage Tasks and Plans: Email, Text, Call, Custom Task (Other), Checklist
   - Automate and Integrate: **Start Smart Plan** ← used for Touch 17 handoff to Long Term Nurture

5. **Start Smart Plan:** Found under Automate and Integrate section in the action picker. Lets you select any existing plan to trigger next.

6. **Deleting steps:** Hover over a step node in edit mode → "×" button appears in top-right corner → click → confirm dialog.

7. **Copying plans:** From the plan list, gear → Copy opens the plan in copy mode. Rename via the pencil icon next to the plan name in Settings.

8. **"Add a Condition" panel:** After saving an action, Lofty automatically opens an "Add a Condition" panel offering: Wait a Period of Time, Wait Until a Specific Date, Wait Until an Event, Branch. This is how timing delays are configured between steps.

---

## Delay Conditions Configured (Session 2 — 2026-05-17)

All "Wait a Period of Time" conditions inserted between steps in all 3 plans.

### Ironwood - Hot delays (10 total)
| Touches | Wait |
|---------|------|
| T4 → T5 (Day 0+30min → Day 1 Text) | 1 Day |
| T5 → T6 (Day 1 Text → Day 1 Voicemail) | 2 Hours |
| T6 → T7 (Day 1 Voicemail → Day 3 Email) | 2 Days |
| T7 → T8 (Day 3 Email → Day 5 Text) | 2 Days |
| T8 → T9 (Day 5 Text → Day 7 Email) | 2 Days |
| T10 → T11 (Day 7 Call → Day 10 Text) | 3 Days |
| T11 → T12 (Day 10 Text → Day 14 Email) | 4 Days |
| T13 → T14 (Day 14 Call → Day 21 Email) | 7 Days |
| T14 → T15 (Day 21 Email → Day 30 Email) | 9 Days |
| T16 → T17 (Day 30 Text → Day 35 Start Plan) | 5 Days |

### Ironwood - Warm delays (10 total — same as Hot, T3→T5 replaces T4→T5)
Same 10 delays, with Wait 1 Day placed between T3 (Day 0 Notification) and T5 (Day 1 Text) since T4 is absent.

### Ironwood - Nurture delays (9 total — same as Warm minus 2-Hour wait)
Same as Warm but no 2-Hour wait since T6 (Voicemail) is absent. Wait 2 Days goes directly from T5 (Day 1 Text) to T7 (Day 3 Email).

### No delay between same-day pairs (correct per smart-plan.md)
- T9 (Day 7 Email) → T10 (Day 7 Call): same day, no wait
- T12 (Day 14 Email) → T13 (Day 14 Call): same day, no wait
- T15 (Day 30 Email) → T16 (Day 30 Text): same day, no wait

---

## Remaining Items

### Activation
All 3 plans are currently inactive (Auto Apply toggle is OFF). Activate when ready by toggling Auto Apply ON for each plan.

### Build error caught and fixed
During Ironwood - Warm configuration, a Wait 7 Days node was initially placed at T14→T15 instead of T13→T14. Caught and corrected: the misplaced node was edited to 9 Days, and a fresh Wait 7 Days was inserted between T13 and T14.

---

## Plans in Lofty
- **Ironwood - Hot**: 17 steps, My Plan, Buyer
- **Ironwood - Warm**: 16 steps, My Plan, Buyer
- **Ironwood - Nurture**: 15 steps, My Plan, Buyer

Content source: `/Users/ryanrose/Downloads/Claude/New-Construction/ironwood/smart-plan.md`
PDF attachment (Touch 2): `/Users/ryanrose/Downloads/Claude/New-Construction/DO.BBRA - Template/Duties Owed and BBRA.pdf`
