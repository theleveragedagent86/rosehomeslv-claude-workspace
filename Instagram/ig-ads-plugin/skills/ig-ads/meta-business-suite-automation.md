# Meta Business Suite — Browser Automation Playbook

Detailed browser automation steps for inputting ad campaigns into Meta Business Suite via Cowork. This file is read by the Campaign Manager during Mode A execution.

---

## Prerequisites

- Browser tools must be available (browser_navigate, browser_click, browser_type, browser_snapshot, or computer use tools)
- User must be logged into Meta Business Suite with access to the Rose Homes LV ad account
- Campaign document must be assembled and approved by the user before starting

---

## Navigation

### Getting to Ads Manager
1. Navigate to `https://business.facebook.com/latest/ads/create`
2. Take a snapshot/screenshot to verify the page loaded
3. Look for the campaign creation flow (objective selection screen)
4. If redirected to login: pause and tell the user "Please log into Meta Business Suite. Let me know when you're ready."
5. If on the wrong account: look for the account switcher (top-left dropdown) and switch to "Rose Homes LV"

### Account Verification
- The account name "Rose Homes LV" should appear in the top navigation
- If you see a different account name, pause and ask the user to switch accounts

---

## Campaign Creation Flow

Meta's Ads Manager follows a 3-level hierarchy: **Campaign > Ad Set > Ad**

### Level 1: Campaign

1. **Select Objective**
   - Look for objective cards (Awareness, Traffic, Engagement, Leads, App Promotion, Sales)
   - Click **Traffic** or **Leads** based on the campaign strategy
   - Click **Continue** to proceed

2. **Campaign Name**
   - Find the campaign name field (usually at the top of the campaign settings)
   - Click the field, clear any default text (Ctrl+A), type the campaign name
   - Enable **Campaign Budget Optimization** if available (toggle switch)
   - Set the budget amount in the budget field

3. Click **Next** to move to Ad Set level

### Level 2: Ad Set

1. **Ad Set Name**
   - Click the ad set name field, Ctrl+A to clear, type the ad set name

2. **Audience Targeting**
   - **Location:** Look for the "Locations" section. Click the search field and type the target location (e.g., "Las Vegas, Nevada"). Set the radius using the dropdown (e.g., "15 miles")
   - **Age:** Find the age range sliders or dropdowns. Set min and max age
   - **Interests:** Look for "Detailed Targeting" or "Interests" section. Click "Browse" or the search field. Type each interest one at a time, clicking to add each one
   - **Behaviors:** Same section as interests — search and add each behavior

3. **Placements**
   - Look for the Placements section
   - Select **Advantage+ placements** (automatic) — this is usually the default
   - If manual placements are selected, switch to Advantage+

4. **Budget & Schedule**
   - If budget wasn't set at campaign level, set it here
   - **Start date:** Click the start date field and set it
   - **End date:** Click the end date field and set it (or select "Run continuously" if no end date)

5. Click **Next** to move to Ad level

### Level 3: Ad (Repeat for Each Variation)

1. **Ad Name**
   - Click the ad name field, Ctrl+A to clear, type the ad variation name (e.g., "Variation 1 - Feature Hook")

2. **Identity**
   - Verify the Facebook Page is set to "Rose Homes LV"
   - Verify the Instagram Account is connected (should be automatic)

3. **Ad Creative — Media**
   - Look for the "Media" or "Add Media" section
   - Click **Add Media** > **Add Image** (or Add Video)
   - If uploading: click **Upload**, navigate to the file, select it, wait for upload to complete
   - If selecting from library: browse existing media and select
   - Wait for the media preview to appear before proceeding

4. **Ad Creative — Text**
   - **Primary Text:** Find the "Primary text" field. Click it, Ctrl+A to clear any default, paste the primary text
   - **Headline:** Find the "Headline" field. Click it, Ctrl+A, paste the headline
   - **Description:** Find the "Description" field. Click it, Ctrl+A, paste the description

5. **Call to Action**
   - Find the CTA dropdown (usually labeled "Call to action")
   - Click it and select the appropriate option (Learn More, Send Message, Sign Up, etc.)

6. **Destination**
   - Find the "Website URL" field
   - Click it, Ctrl+A, paste the **landing page URL** (NEVER a Zillow, Realtor.com, or MLS page)

7. **Adding More Variations**
   - To add another ad variation within the same ad set, look for a **"+ Create"** or **"Duplicate"** button in the ad panel
   - Click it to create a new ad
   - Repeat steps 1-6 for each variation

---

## Instant Form Creation (Leads Objective Only)

When using the Leads objective for Listing Lead Form campaigns, the ad level includes a lead form builder. After entering the ad creative (media, text, CTA), you must create the Instant Form.

### Step-by-Step: Creating the Instant Form

1. **Select Lead Method**
   - At the Ad level, look for "Lead method" or "Instant form" section
   - Select **Instant forms** (not Messenger, not Calls)
   - Click **Create form** (or **+ New form** if forms already exist)

2. **Form Name**
   - A modal/panel will open for the form builder
   - Find the form name field at the top
   - Type the form name: "[CAMPAIGN NAME] - Lead Form"

3. **Form Type**
   - Look for "Form type" options: "More volume" vs "Higher intent"
   - Select **More volume** (recommended — auto-fills from Facebook, higher completion rate)
   - Click Next/Continue

4. **Intro (Recommended)**
   - Toggle ON the intro section if available
   - **Headline:** Type the form headline (e.g., "Find Similar Homes in [NEIGHBORHOOD]")
   - **Image:** Select the same listing photo used in the ad, or the campaign hero image
   - **Description:** Type 1-2 sentences (e.g., "Get new listings in [NEIGHBORHOOD] and surrounding areas sent directly to you. No spam, no pressure.")
   - **Layout:** Select "Paragraph" layout (not list)

5. **Questions**
   - Look for the "Questions" section
   - **Pre-filled fields:** Ensure these are enabled:
     - Full name (click "+ Add" or check the box)
     - Email (click "+ Add" or check the box)
     - Phone number (click "+ Add" or check the box)
   - **Custom Question 1:**
     - Click **"+ Add question"** or **"+ Custom question"**
     - Select question type: **Multiple choice**
     - Type: "When are you looking to buy?"
     - Add options: "ASAP", "1-3 months", "3-6 months", "Just browsing"
     - Click Done/Save
   - **Custom Question 2:**
     - Click **"+ Add question"** again
     - Select question type: **Multiple choice**
     - Type: "Are you pre-approved for a mortgage?"
     - Add options: "Yes", "No", "Not yet"
     - Click Done/Save

6. **Privacy Policy**
   - Find the "Privacy policy" section (REQUIRED — form cannot be saved without this)
   - **Link text:** "Privacy Policy"
   - **URL:** Type `https://www.rosehomeslv.com/site/privacy-terms`

7. **Thank You Screen**
   - Find the "Thank you screen" or "Completion" section
   - **Headline:** Type "You're All Set!"
   - **Description:** Type "Ryan will send you matching listings within 24 hours. In the meantime, check out what's available now."
   - **Button type:** Select "View website"
   - **Button URL:** Type the landing page URL or `https://www.rosehomeslv.com`

8. **Save the Form**
   - Click **"Save"** or **"Publish"** within the form builder modal
   - Wait for the modal to close and verify the form name appears in the ad setup
   - The form is now attached to the ad — it does NOT go live until the campaign itself is published

### Adding the Form to Additional Ad Variations
- When duplicating ad variations, the form may need to be re-attached
- In each new ad variation, look for the "Instant form" dropdown and select the form you just created
- All variations can share the same form

### Common Form Builder Issues
- **"Privacy policy required" error:** The URL field must be filled before the form can be saved
- **Custom question not saving:** Make sure all answer options are filled in before clicking Save
- **Form builder not opening:** Ensure the campaign objective is set to "Leads" at the campaign level. Traffic campaigns do not have form builders.
- **Pre-filled fields greyed out:** These auto-fill from the user's Facebook profile on delivery. This is normal.

---

## Lead Sync: Meta → Lofty CRM (Browser Automation)

Automated workflow to download new leads from Meta Business Suite and enter them into Lofty CRM. Uses the same browser automation patterns as the publish-blogs skill (tab management, field entry, verification).

### Prerequisites
- Browser tools must be available
- User must be logged into both Meta Business Suite AND Lofty CRM (`https://cms.lofty.com`)
- A lead tracking log file must exist (or will be created) to avoid duplicate entries

### Lead Tracking Log
- Location: `/Users/ryanrose/Downloads/Claude/Instagram/Ad Campaigns/lead-sync-log.json`
- Format: Array of objects with `name`, `email`, `phone`, `synced_date`, `form_name`, `campaign_name`
- Before entering any lead into Lofty, check the log to confirm the lead hasn't already been synced (match by email)

### Step 1: Download Leads from Meta

1. Navigate to `https://business.facebook.com/latest/leads_center`
2. Take a snapshot to verify the Leads Center loaded
3. If redirected to login, pause and ask user to log in
4. Look for the leads table/list — it should show form submissions
5. Filter by form name if multiple forms exist (click the form filter dropdown)
6. Filter by date range to get only new submissions (since last sync)
7. For each lead visible in the table, extract:
   - **Name** (full name column)
   - **Email** (email column)
   - **Phone** (phone column)
   - **Custom answers** (qualifying question responses — "When looking to buy?" and "Are you pre-approved?")
   - **Form name** (which form/campaign it came from)
   - **Date** (submission date)
8. Store all extracted leads in memory before proceeding to Lofty

**Alternative download method:** If Leads Center is not available or leads are not visible:
1. Navigate to `https://business.facebook.com/latest/ads/manage`
2. Find the campaign, click into the ad level
3. Look for "Results" or "Leads" column
4. Click the lead count to view/download leads
5. If a CSV download option is available, use it

### Step 2: Enter Leads into Lofty CRM

For each lead extracted from Meta:

1. **Check duplicate:** Compare email against `lead-sync-log.json`. If already synced, skip.
2. Navigate to Lofty CRM (open new tab or navigate to `https://cms.lofty.com`)
3. Look for **"+ Add"** or **"Add Contact"** or **"Add Lead"** button
4. Click to open the new lead form
5. Enter fields:
   - **First Name / Last Name:** Split the full name and enter into appropriate fields
   - **Email:** Enter the email address
   - **Phone:** Enter the phone number
   - **Source:** Set to "Facebook" or "Meta Lead Form Ad" (look for a source/lead source dropdown)
   - **Notes:** Add qualifying question answers:
     ```
     Meta Lead Form Ad - [FORM NAME]
     Looking to buy: [ANSWER]
     Pre-approved: [ANSWER]
     Submitted: [DATE]
     ```
6. Click **Save** or **Submit** to create the lead
7. Verify the lead was saved (look for success message or redirect to lead profile)
8. **Tag the lead:**
   - Look for a "Tags" section on the lead profile (or an "Add Tag" button)
   - Determine the track from qualifying answers:
     - **Hot:** "ASAP" or "1-3 months" AND "Yes" pre-approved → tag: `[Address Short] - Hot`
     - **Warm:** "1-3 months" or "3-6 months", any pre-approval → tag: `[Address Short] - Warm`
     - **Nurture:** "Just browsing" → tag: `[Address Short] - Nurture`
   - Type the tag name and add it (e.g., "29 Amber Rock - Hot")
9. **Assign the Action Plan:**
   - On the lead's profile, look for "Action Plans", "Plans", or "Smart Plans" section
   - Click "Add Action Plan" or "Assign Plan"
   - Search for the matching plan: `[Address Short] Follow-Up - [Hot/Warm/Nurture]`
   - Select it and confirm assignment
   - Verify the plan appears as active on the lead's profile
   - The first automated text will fire immediately once the plan is assigned
10. Add the lead to `lead-sync-log.json`

### Step 3: Report Results

After all leads are processed, report to the user:

```
Lead Sync Complete:
- New leads found: [X]
- Leads synced to Lofty: [Y]
- Duplicates skipped: [Z]
- Leads synced: [list names with track assignments]
  - [Name] → [Address Short] - Hot (Action Plan assigned)
  - [Name] → [Address Short] - Warm (Action Plan assigned)
  - etc.

First automated text fires immediately for each synced lead.
Next sync: Run "sync leads" again or set up a scheduled sync.
```

### Error Handling
- If Lofty CRM is not accessible, save the extracted leads to a CSV file at `/Users/ryanrose/Downloads/Claude/Instagram/Ad Campaigns/pending-leads.csv` and tell the user
- If a lead fails to save in Lofty, log the error and continue with the next lead. Report failures at the end.
- If Meta Leads Center shows no new leads, report "No new leads to sync" and exit

---

## Lofty Action Plan Creation (Browser Automation)

Creates listing-specific follow-up Action Plans in Lofty CRM. Three plans are created per listing (Hot, Warm, Nurture). This runs once when the Listing Lead Form campaign is set up, not during each lead sync.

### Prerequisites
- Browser tools must be available
- User must be logged into Lofty CRM (`https://cms.lofty.com`)
- The follow-up sequence content must be ready (read from `follow-up-sequence.md`)
- Listing details must be available to replace template variables

### Template Variable Replacement

Before creating each plan, replace these variables in all message copy:
- `{AREA}` → the broader city/area (e.g., "Henderson")
- `{NEIGHBORHOOD}` → the specific community (e.g., "Champion Village")
- `{LISTING_FEATURE}` → standout feature (e.g., "that 3-car garage")
- `{PRICE}` → listing price or range (e.g., "$425,000" or "the $400s")
- `{BEDS}` → bed count (e.g., "3")
- `{BATHS}` → bath count (e.g., "2")

Leave `#lead_first_name#` as-is — Lofty replaces it automatically per lead.

### Step-by-Step: Creating an Action Plan

Repeat this process 3 times (once for Hot, once for Warm, once for Nurture). Use the track summary table in `follow-up-sequence.md` to know which touches apply to each track.

1. **Navigate to Action Plans**
   - Go to `https://cms.lofty.com` (or navigate from the Lofty dashboard)
   - Look for **"Automations"**, **"Action Plans"**, or **"Smart Plans"** in the left sidebar or top navigation
   - Click to open the Action Plans list
   - Take a snapshot to verify you're on the right page

2. **Create New Plan**
   - Click **"Create Action Plan"**, **"+ New"**, or **"+ Add Plan"**
   - A new plan editor should open

3. **Name the Plan**
   - Find the plan name field at the top
   - Type: `[Address Short] Follow-Up - [Hot/Warm/Nurture]`
   - Example: "29 Amber Rock Follow-Up - Hot"

4. **Configure Plan Settings**
   - Look for a **"Stop on reply"** or **"Pause when contact responds"** setting
   - Enable it — this is CRITICAL so automated messages stop when a lead replies
   - Set the plan to **active** (not draft)

5. **Add Steps (for each touch in the sequence)**

   For each touch that applies to this track (see follow-up-sequence.md track summary table):

   **Adding a Text step:**
   - Click **"Add Step"** or **"+"**
   - Select step type: **"Text"** or **"Send Text"**
   - Set the delay: "Immediately" for Day 0, or the appropriate day/time delay
   - Paste the text message content (with template variables already replaced, `#lead_first_name#` left as Lofty merge field)
   - Save the step

   **Adding an Email step:**
   - Click **"Add Step"** or **"+"**
   - Select step type: **"Email"** or **"Send Email"**
   - Set the delay
   - Enter the subject line
   - Enter the email body (paste the full email content)
   - Save the step

   **Adding a Task step (for calls and voicemail reminders):**
   - Click **"Add Step"** or **"+"**
   - Select step type: **"Task"** or **"Create Task"** or **"Reminder"**
   - Set the delay
   - Enter the task description (the note to Ryan with call script)
   - Save the step

   **Adding a Wait/Delay between steps:**
   - If Lofty requires explicit wait steps between actions, add them
   - Set the delay period (e.g., "Wait 1 day", "Wait until 10:00 AM")
   - Some Lofty plans allow delay configuration directly on each step — use whichever method the UI provides

6. **Verify All Steps**
   - After adding all steps, take a snapshot/screenshot
   - Count the steps and verify against the expected count:
     - **Hot:** 22 touches
     - **Warm:** 19 touches
     - **Nurture:** 15 touches
   - Verify the first step is "Send Text — Immediately"

7. **Activate the Plan**
   - Ensure the plan status is set to **Active** (not Draft or Paused)
   - Click **Save** or **Publish** to finalize
   - The plan is now live and will trigger automatically when assigned to a lead

8. **Repeat for Next Track**
   - Go back to the Action Plans list
   - Create the next variant (Warm or Nurture)
   - Use the same listing data but only include the touches that apply to that track

### After All 3 Plans Are Created

Report to the user:
```
Lofty Action Plans Created:
- [Address Short] Follow-Up - Hot (22 touches, 30 days) ✓ Active
- [Address Short] Follow-Up - Warm (19 touches, 30 days) ✓ Active
- [Address Short] Follow-Up - Nurture (15 touches, 30 days) ✓ Active

Stop-on-reply: Enabled for all plans.
These will be assigned to leads automatically during lead sync based on qualifying answers.
First text fires immediately when a plan is assigned to a lead.
```

### Common Lofty Action Plan Issues
- **Can't find Action Plans:** Try Automations > Action Plans, or Smart Plans in the sidebar. The location varies by Lofty account tier.
- **No "stop on reply" option:** Check plan settings or advanced options. If not available, add a manual note in the task descriptions reminding Ryan to check for responses.
- **Step delay not saving:** Some Lofty plans require you to set the delay before entering the message content. Try setting the delay first, then the content.
- **Text character limit:** Lofty may truncate texts over 300 characters. All texts in the sequence are designed to stay under this limit.
- **Merge field not recognized:** Ensure you're using `#lead_first_name#` with hash delimiters, not curly braces.

---

## Final Review — DO NOT PUBLISH

After all ad variations are entered:

1. Look for a **"Review"** or **"Publish"** button (usually bottom-right)
2. If there's a "Review" step, click it to see the full campaign summary
3. **DO NOT click Publish.** Stop here.
4. Tell the user:

> "Campaign is fully set up in Meta Business Suite and ready for your review. Here's what was entered:
> - Campaign: [name]
> - Ad Set: [targeting summary]
> - Ad Variations: [count]
> - Budget: [amount]
>
> Please review everything in Ads Manager and click Publish when you're satisfied."

---

## Common UI Patterns

### Field Clearing
- Always use **Ctrl+A** before typing into any field that might have default content
- Meta pre-fills some fields with placeholder text or previous values

### Dropdowns
- Click the dropdown to open it
- Wait for options to load (can take 1-2 seconds)
- Click the desired option
- Verify the dropdown closed and shows the selected value

### Toggles
- Click the toggle switch to enable/disable
- Verify the toggle changed state (check for color change or position shift)

### Modals
- Some actions open modal dialogs (e.g., media upload, audience creation)
- Complete all actions inside the modal before trying to interact with the page behind it
- Look for "Save" or "Done" button inside the modal to close it

### Loading States
- Meta's UI has loading spinners and skeleton screens
- Wait for content to fully load before clicking
- If a button click has no effect, wait 2-3 seconds and try again
- Take a snapshot/screenshot to verify the current state if unsure

---

## Error Handling

### "Something went wrong"
- Take a screenshot, describe the error to the user
- Try refreshing the page and navigating back to the campaign
- If the campaign was partially saved, it may appear in Drafts

### Validation Errors
- Meta highlights invalid fields in red with error messages
- Read the error message and report it to the user
- Common issues: missing destination URL, budget too low, audience too narrow

### Session Timeout
- If redirected to login page mid-flow, pause and ask the user to log in
- After login, navigate back to `https://business.facebook.com/latest/ads/drafts` to find the in-progress campaign

### Rate Limiting / Slow UI
- If the UI becomes unresponsive, wait 5-10 seconds before retrying
- Do not rapid-click buttons — one click, wait, verify
