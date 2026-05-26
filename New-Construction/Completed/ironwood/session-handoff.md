# Lofty Smart Plan Build — Ironwood by Century Communities
## Session Handoff

### What We're Doing
Building 3 Smart Plans (Action Plans) in Lofty CRM via browser automation (Claude in Chrome, tab ID 470154884). The plans automate lead follow-up for the Ironwood by Century Communities new construction community in Southwest Las Vegas. All content is defined in `/Users/ryanrose/Downloads/Claude/New-Construction/ironwood/smart-plan.md`.

**Plans to build:**
- `Ironwood - Hot` — 17 steps
- `Ironwood - Warm` — 16 steps (skip Touch 4)
- `Ironwood - Nurture` — 15 steps (skip Touch 4 and Touch 6)

**Total: 48 steps across all 3 plans**

After all 3 plans are built, write a build log to `/Users/ryanrose/Downloads/Claude/New-Construction/ironwood/cowork-build-log.md`.

---

### What's Already Done
- **Tag:** `Century-Ironwood` confirmed to exist in Lofty (user chose this over creating a new `ironwood` tag)
- **Plan 1 (`Ironwood - Hot`) — IN PROGRESS:**
  - **Step 1 ✅** — Auto Text (Touch 1, Day 0 opening text to lead) — saved
  - **Step 2 ✅** — Auto Email (Touch 2, Day 0 lead email "The Ironwood homes you were looking at") — saved, with `Duties Owed and BBRA.pdf` attached from `/Users/ryanrose/Downloads/Claude/New-Construction/DO.BBRA - Template/Duties Owed and BBRA.pdf`
  - **Step 3 🔴 NOT YET SAVED** — Notification (Touch 3, builder rep notification to ryan@rosehomeslv.com) — currently mid-fill in Lofty

---

### Where To Resume: Step 3 (Touch 3 — Notification)

The Notification form is open in Lofty at `https://crm.lofty.com/admin/home/campaigns/smartPlan`. It's positioned between step 2 and End.

**Known UI quirk:** The Send To field has a persistent "Agent Role" dropdown (Agent / Assistant checkboxes) that opens whenever you click anywhere near it and covers the Email Subject field. Workaround: use the `find` tool to locate the subject input by ref and type into it directly, or use `javascript_exec` to set the value:

```js
const subjectInput = document.querySelector('input[placeholder="Please enter the subject"]');
subjectInput.focus();
subjectInput.value = 'New Lead for Ironwood by Century Communities - #lead_first_name#';
subjectInput.dispatchEvent(new Event('input', { bubbles: true }));
subjectInput.dispatchEvent(new Event('change', { bubbles: true }));
```

**Also known:** Clicking outside the Notification panel closes it without saving. Stay inside the panel at all times.

**Touch 3 form values to fill:**
- Send From: Agent (already set by default — leave it)
- Send To: `ryan@rosehomeslv.com` ONLY — no Agent, no Assistant chips
- Email Subject: `New Lead for Ironwood by Century Communities - #lead_first_name#`
- Email Body (use "Zoom in to edit"):

```
Below is the curated email for new lead buyer at Ironwood by Century Communities for lead #lead_first_name#.

Copy and paste the email below and send it to the Century Communities sales rep at 702-605-1504.

---

Subject: New Buyer Interest - Ironwood

Hi there,

Ryan Rose with Real Broker here. I just wanted to let you know I have a client that is interested in Ironwood by you guys and they are talking about stopping by within the next few days. I wanted to make sure I pre-register them in the event that I for some reason cannot attend. Can we go ahead and do that real quick?

The client's name is #lead_first_name# and the best number to reach them is #lead_phone#.

Thank you,
Ryan Rose
Real Broker, LLC
702-747-5921
ryan@rosehomeslv.com
```

Click Save after filling the body.

---

### Remaining Steps for Plan 1 (Ironwood - Hot) — Steps 4–17

After saving Touch 3, continue adding steps in sequence. Each step = click the green "Add an Action" dashed box or the + connector, choose Action, pick the type, fill content, save.

| Step | Touch | Day | Delay | Action Type | Notes |
|------|-------|-----|-------|-------------|-------|
| 4 | T4 | 0+30min | 30 min | **Task (Call)** | HOT ONLY. Expand "Manage Tasks and Plans" section in action list |
| 5 | T5 | 1 | 10:00 AM | Auto Text | Day 1 text to lead |
| 6 | T6 | 1 | 12:00 PM | **Task (Voicemail)** | Voicemail script |
| 7 | T7 | 3 | — | Auto Email | Subject: "Ironwood builder incentives you should know about" |
| 8 | T8 | 5 | 10:00 AM | Auto Text | Day 5 text |
| 9 | T9 | 7 | — | Auto Email | Subject: "How Ironwood compares to other new builds in Southwest Las Vegas" |
| 10 | T10 | 7 | 2:00 PM | **Task (Call)** | Week 1 check-in |
| 11 | T11 | 10 | 9:30 AM | Auto Text | Quick move-in text |
| 12 | T12 | 14 | — | Auto Email | Subject: "Honest question, #lead_first_name#" |
| 13 | T13 | 14 | 3:00 PM | **Task (Call)** | Check-in call |
| 14 | T14 | 21 | — | Auto Email | Subject: "Southwest Las Vegas market update for you" |
| 15 | T15 | 30 | — | Auto Email | Subject: "Monthly Ironwood update" |
| 16 | T16 | 30 | 2:00 PM | Auto Text | Month check-in |
| 17 | T17 | 35 | — | **Start Smart Plan** | → "Long Term Nurture - Buyer" |

For all exact body copy, read from `/Users/ryanrose/Downloads/Claude/New-Construction/ironwood/smart-plan.md`.

**Unknown action types still to explore:** Call Task, Voicemail Task, and Start Smart Plan are all under the "Manage Tasks and Plans" collapsible section in the action picker. This section was visible at the bottom of the action list but not yet expanded.

---

### Then Build Plan 2 (Ironwood - Warm, 16 steps)
Same as Hot but skip Touch 4 (the HOT-only call task at Day 0+30min).

### Then Build Plan 3 (Ironwood - Nurture, 15 steps)
Same as Hot but skip Touch 4 AND Touch 6 (the voicemail task at Day 1).

---

### Key Settings for All 3 Plans
- **Trigger:** Auto Apply Setting → Tag Changed → `Century-Ironwood`
- **Stop on Reply:** Auto Pause Setting → check "The lead responds / reaches out" — ALREADY CONFIGURED on Plan 1
- **Target Lead Type:** Buyer
- **Email sender:** Ryan Rose (ryan@rosehomeslv.com)
- **Text business hours:** 9:00 AM to 7:00 PM PT

---

### Key Files
- **Content:** `/Users/ryanrose/Downloads/Claude/New-Construction/ironwood/smart-plan.md`
- **PDF attachment (Touch 2 only):** `/Users/ryanrose/Downloads/Claude/New-Construction/DO.BBRA - Template/Duties Owed and BBRA.pdf`
- **Build log (write when done):** `/Users/ryanrose/Downloads/Claude/New-Construction/ironwood/cowork-build-log.md`
- **Implementation plan:** `/Users/ryanrose/.claude/plans/you-are-the-lofty-mossy-stream.md`
- **This handoff file:** `/Users/ryanrose/Downloads/Claude/New-Construction/ironwood/session-handoff.md`

---

### Lofty UI Notes (Discovered During Build)
- Lofty merge field format matches the content file exactly: `#lead_first_name#`, `#lead_phone#`, `#signature#` — no special chip insertion needed, just type them
- The Notification form's Send To defaults to including "Agent" and "Assistant" roles — always remove those, keep only the typed email address
- Clicking outside any action form panel closes it without saving — stay inside the panel
- The "Add a Condition" panel sometimes opens alongside the action panel and cannot be closed — it is harmless, just work in the middle column
- PDF attachment uses a paperclip icon in the email body toolbar → "CHOOSE FILES" dialog
- "Long Term Nurture - Buyer" plan already exists in Lofty (confirmed)
- The Notification action type is found under Communication → Notification in the action picker
- Call Task, Voicemail Task, and Start Smart Plan are under the "Manage Tasks and Plans" section (collapsible, at the bottom of the action picker) — not yet explored
- The trigger save required deleting an empty "Criteria" row — click the trash icon to remove it before saving the trigger
- Use `javascript_exec` or the `find` tool with refs when UI dropdowns block input fields
