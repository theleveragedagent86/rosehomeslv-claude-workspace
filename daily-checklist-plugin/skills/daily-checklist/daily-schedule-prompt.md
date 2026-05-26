# Daily Checklist — Cowork Scheduler Prompt

Use this as the prompt when setting up a scheduled task in Cowork.

---

## Schedule Settings

- **Description:** Daily Morning Checklist
- **Frequency:** Daily (weekdays only recommended, skip Sat/Sun)
- **Time:** 7:00 AM (or whenever you want your morning briefing)

---

## Prompt to Paste

```
Good morning. Run my daily checklist.

STEP 1 — READ DATA FILES
Read these files:
- /Users/ryanrose/Downloads/Claude/daily-checklist-plugin/skills/daily-checklist/calendar.json
- /Users/ryanrose/Downloads/Claude/daily-checklist-plugin/skills/daily-checklist/recurring-tasks.json
- /Users/ryanrose/Downloads/Claude/daily-checklist-plugin/skills/daily-checklist/expired-cannonball-tracker.json
- /Users/ryanrose/Downloads/Claude/daily-checklist-plugin/skills/daily-checklist/cannonball-cadence.json
- /Users/ryanrose/Downloads/Claude/daily-checklist-plugin/skills/daily-checklist/completion-log.json

STEP 2 — GET TODAY'S INFO
Determine today's date and day of the week.

STEP 2B — CHECK YESTERDAY'S COMPLETION STATUS
Read completion-log.json. Find yesterday's entry (or last weekday if today is Monday).
If there are items in the "incomplete" array, show them at the TOP of the checklist:

## Carried Over from [DATE]
- [ ] [TASK TITLE] (carried over)
- [ ] [TASK TITLE] (carried over)
Were these completed? Tell me which ones to check off.

If yesterday had no incomplete items or no entry exists, skip this section.

STEP 3 — RUN EXPIRED WORKFLOW (weekdays only)
If today is Monday–Friday:
1. Read the download log at /Users/ryanrose/Downloads/Claude/Expireds/Elise_Attachments/download_log.json to see what was last downloaded.
2. Use the Gmail MCP tool (gmail_search_messages) to search for: from:Elise Demarinis has:attachment after:2026/01/01
3. Compare results against the download_log.json downloaded_files list to identify NEW emails not yet downloaded.
4. If there are new emails:
   a. Use browser automation (tabs_context_mcp, navigate, computer) to open Gmail in Chrome
   b. For each new email, scroll to attachments, hover over the "Expired" .xlsx file, and click the download icon. Wait 2 seconds between each.
   c. After all downloads, copy each new Expired file from ~/Downloads/ to /Users/ryanrose/Downloads/Claude/Expireds/Elise_Attachments/
   d. Update download_log.json: add each new file to downloaded_files array, set last_run to today's date
   e. Report: "Downloaded X new Expired files from Elise (dates: ...)"
5. If no new emails: report "No new Elise emails since last run."
Note: Only download files with "Expired" in the filename. Skip FSBO and Withdrawn files.

STEP 3B — PROCESS EXPIRED DATA & UPDATE CANNONBALL TRACKER
After downloading (or if files were already current), process the data:
1. Read the master hotsheet CSV from /Users/ryanrose/Downloads/Claude/Expireds/Elise_Attachments/ (glob for "Expired 1-1-2026 to *.csv")
2. Find the latest *Expired.xlsx workbook in the same folder.
3. Read the main data sheet (not the Mailing List sheet) from that workbook.
4. Filter for new cannonball candidates matching the buy box in expired-cannonball-tracker.json:
   - List Price between $600,000 and $2,000,000
   - Property Zip in target_zips list
   - NOT already in active_campaigns or completed_campaigns (match by normalized address)
   - NOT a Residential Rental or Condo/Hotel
5. For each new qualifying listing, auto-populate these fields and add to active_campaigns:
   - first_name: from the "First Name" column in the workbook
   - owner_name: from the "Name" column
   - address: from "Property Address"
   - price: from "List Price"
   - zip: from "Property Zip"
   - area: map zip to area using zip_to_area in the tracker (89135/89134/89144/89145/89138 = Summerlin, 89178/89179/89141/89183/89139 = Henderson, 89113/89147/89148/89117/89118 = Spring Valley, anything else = Las Vegas)
   - price_range: round list price to nearest $100k bracket (e.g., $792k = "$700,000-$800,000", $650k = "$600,000-$700,000")
   - sold_count: count homes from the master hotsheet CSV where Stat = "S" (sold only, do NOT include COS), Current Price falls in the same $100k range, Zip Code maps to the same area, and the data is from the current month + last month
   - mailing_street: from "Mailing Street" column
   - mailing_city: from "Mailing City" column
   - mailing_state: from "Mailing State" column
   - mailing_zip: from "Mailing Zip" column
   - start_date: today
   - status: "active"
   - completed_steps: []
   - next_step: "day1-cannonball"
   - next_step_date: today
6. Also check all existing active_campaigns against the hotsheet — if any address now has status A-ER, A-EA, UCNS, UCS, S, or COS, move it to completed_campaigns.
7. Save the updated tracker JSON.
8. Report: "Added X new listings to cannonball tracker" or "No new cannonball candidates today."

STEP 3C — GENERATE READY-TO-PASTE PROMPT FILES
For every cannonball step due today that involves a letter/mail piece, generate a ready-to-paste prompt file so Ryan doesn't have to fill in any values manually. Save to: /Users/ryanrose/Downloads/Claude/Expireds/Cannonball_Letters/

For Day 1 Sales Letters:
1. Read the template prompt from /Users/ryanrose/Downloads/Claude/Listing Leads Content/Expired Editor Designs/Cannonball_Sales_Letter_claude_prompt.txt
2. In the HTML template section of the prompt, replace ALL placeholders with the campaign's stored values:
   - [First Name] → campaign first_name (both in salutation and opening hook)
   - [#] homes → campaign sold_count
   - [$XXX,XXX–$XXX,XXX] → campaign price_range
   - [Area] → campaign area
   - [Your Phone Number] → 702-747-5921
   - "Agent Full Name" → Ryan Rose
   - "Email" in signature → ryan@rosehomeslv.com
   - "Phone" in signature → 702-747-5921
   - "Your Logo Here" div → <img src="[Company Logo URL from the prompt]" style="max-height:70px;">
   - "Headshot" div → <img src="[Headshot URL from the prompt]" style="width:80px;height:80px;object-fit:cover;border-radius:4px;">
3. Save as: [DATE]_[FirstName]_[LastName]_[AddressSlug]_Sales_Letter_Prompt.txt

For Day 1 Cover Letters:
1. Read the template prompt from /Users/ryanrose/Downloads/Claude/Listing Leads Content/Expired Editor Designs/Cannonball_The_Personalized_Cover_Letter_claude_prompt.txt
2. Replace the address placeholder with the campaign's property address
3. Replace footer: Agent Name → Ryan Rose, DRE# → S.0185572, phone → (702) 747-5921, email → ryan@rosehomeslv.com
4. Save as: [DATE]_[FirstName]_[LastName]_[AddressSlug]_Cover_Letter_Prompt.txt

For follow-up letters #1-#3 (Days 7, 14, 21):
1. Read the corresponding Sales Letter prompt from Expired Editor Designs
2. Replace [Your Phone Number] → 702-747-5921
3. Replace agent name/email/phone in signature, logo and headshot placeholders
4. Save as: [DATE]_[FirstName]_[LastName]_[AddressSlug]_Letter_[N]_Prompt.txt

Each file must contain the COMPLETE prompt (system instructions + fully filled template) — ready to copy-paste into Claude.ai in one shot with zero manual editing.

STEP 4 — DISPLAY CALENDAR EVENTS
From calendar.json, find any events where "date" matches today. Display them with time, title, location, and notes. Sort by time. If none, say "No calendar events today."

STEP 5 — DISPLAY RECURRING TASKS
From recurring-tasks.json, get the tasks for today's day of the week. For each task:
- Show the title and time suggestion
- Show the "ready_to_use" content INLINE so I can copy-paste immediately:
  - For emails: show Subject, Preview Text, and Body directly
  - For social: show the Canva template link as a clickable URL
  - For texts: show the exact text message script
  - For video: show the Showflow PDF link, Canva thumbnail link, video title, description, and hashtags
- Show audience and channel

If it's a weekend with no tasks, say "No recurring tasks. Enjoy your weekend!"

STEP 5B — DISPLAY EXPIRED CANNONBALL ACTIONS
Read the tracker at /Users/ryanrose/Downloads/Claude/daily-checklist-plugin/skills/daily-checklist/expired-cannonball-tracker.json and the cadence file. For each active campaign:
1. Calculate days elapsed: today - start_date
2. Find which cadence steps are due today (step day == days_elapsed + 1)
3. Also find any overdue steps (step day < days_elapsed + 1 AND step id NOT in completed_steps)
4. For NEW cannonball packages (Day 1) or any mail/letter steps, show the generated prompt file path:
   - "Sales Letter — READY TO PASTE"
   - File: /Users/ryanrose/Downloads/Claude/Expireds/Cannonball_Letters/[FILENAME].txt
   - "Open this file, copy entire contents, paste into Claude.ai. All values pre-filled. Generate and print."
   - Also show the pre-filled values for reference (first_name, sold_count, price_range, area, phone)
5. For EVERY mail step, also show the full mailing address:
   Mail to: [first_name] [last_name]
            [mailing_street]
            [mailing_city], [mailing_state] [mailing_zip]
6. For call steps, read and display the call script inline from /Users/ryanrose/Downloads/Claude/Listing Leads Content/Blueprints/2026_Expired_Marketing_Blueprint/Linked_Pages/

If no active campaigns or nothing due today, say "No expired cannonball actions today."

STEP 5C — LOG TODAY'S TASKS TO COMPLETION TRACKER
Write all of today's task IDs (recurring tasks, cannonball steps, calendar events) to the completion-log.json as the "incomplete" array for today's date. As I mark things done throughout the day, they'll move to "completed". Remove entries older than 7 days.

STEP 6 — SHOW UPCOMING (NEXT 3 DAYS)
Show a brief preview of calendar events and recurring task titles for the next 3 days.

STEP 7 — ALSO READ CONTENT LIBRARY (if available)
Check for more detailed content at /Users/ryanrose/Downloads/Claude/Listing Leads Content/
Look for the most recent week folder in each category subfolder. If today's task has a matching How_to_Execute or resources file, read it and include the Canva links, full email copy, or text scripts inline.

Format everything cleanly with checkboxes (- [ ]) so items feel actionable. Keep it scannable.
```
