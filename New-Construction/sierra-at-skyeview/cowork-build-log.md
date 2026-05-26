# Sierra at Skyeview — Lofty Smart Plan Build Log

**Built:** 2026-05-24  
**Builder:** Claude (Cowork automation)  
**Source blueprint:** `smart-plan.md`

---

## Plans Created

All three action plans were successfully built and saved in Lofty CRM under Smart Plans > My Plans.

| Plan Name | Duration | Touches | Trigger | Auto Pause |
|---|---|---|---|---|
| Sierra at Skyeview - Hot | 35 days | 17 | Tag Added: Sierra at Skyeview | On (lead responds) |
| Sierra at Skyeview - Warm | 35 days | 16 | Tag Added: Sierra at Skyeview | On (lead responds) |
| Sierra at Skyeview - Nurture | 35 days | 15 | Tag Added: Sierra at Skyeview | On (lead responds) |

---

## Touch Summary

### Touches in All Three Plans (shared)
- **Touch 1** — Day 0, Auto Text (SMS intro, Sierra at Skyeview)
- **Touch 2** — Day 0, Auto Email (subject: "The Sierra at Skyeview homes you were looking at", with DO/BBRA disclosure and buyer guide link)
- **Touch 3** — Day 0, Notification to ryan@rosehomeslv.com (new lead alert)
- **Touch 5** — Day 1, Auto Text (follow-up)
- **Touch 7** — Day 3, Auto Email
- **Touch 8** — Day 5, Auto Text
- **Touch 9** — Day 7, Auto Email
- **Touch 10** — Day 10, Auto Text
- **Touch 11** — Day 14, Auto Email
- **Touch 12** — Day 17, Auto Text
- **Touch 13** — Day 21, Auto Email
- **Touch 14** — Day 24, Auto Text
- **Touch 15** — Day 28, Auto Email
- **Touch 16** — Day 31, Auto Text
- **Touch 17** — Day 35, Auto Email + handoff trigger to "Long Term Nurture - Buyer"

### Hot Plan Only (17 touches)
- **Touch 4** — Day 0 +30min, Call Task

### Hot and Warm Plans (not Nurture)
- **Touch 6** — Day 1 12PM, Voicemail Drop (Call Task)

---

## Manual Steps Required

**Ryan must manually complete the following after this build:**

### PDF Attachments — Touch 2 Auto Email (ALL 3 plans)

The Touch 2 Auto Email in each plan requires two PDF attachments that cannot be added via automation due to browser security restrictions on file uploads. For each plan:

1. Open the plan in Lofty Smart Plans
2. Click the Touch 2 Auto Email step
3. Click "Zoom in to edit" to open the full-screen email editor
4. Click the paperclip icon (7th icon in the toolbar)
5. Attach both files:
   - `Duties Owed and BBRA.pdf` (located in `/Users/ryanrose/Downloads/Claude/New-Construction/DO.BBRA - Template/`)
   - `buyer-guide.pdf` (located in `/Users/ryanrose/Downloads/Claude/New-Construction/sierra-at-skyeview/`)
6. Save and close

Repeat for Sierra at Skyeview - Hot, Warm, and Nurture.

---

## Deviations from Blueprint

None. All touches, delays, copy, and settings match `smart-plan.md` exactly.

**Trigger fix applied:** The Nurture plan was initially saved without a trigger (subagent build step missed it). Trigger was added manually in the same session: Tag Changed, condition = Added, tag = "Sierra at Skyeview." Auto Pause Setting was also enabled in the same fix pass.

---

## Key Settings Verified

- Trigger type: Tag Changed, condition = Added, tag = "Sierra at Skyeview"
- Stop on Reply (Auto Pause): checked for all 3 plans
- Sender: Ryan Rose (Send From Agent)
- Target Lead Type: Buyer
- Duration: 35 days (Day 35 step triggers Long Term Nurture - Buyer handoff)
- Text messages: business hours 9AM-7PM PT
- All emails end with `#signature#` (Lofty auto-insert)
- Merge fields used: `#lead_first_name#`, `#lead_phone#`, `#signature#`
