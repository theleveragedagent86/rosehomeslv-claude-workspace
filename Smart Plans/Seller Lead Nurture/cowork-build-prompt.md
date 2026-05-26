# Cowork Prompt — Build Seller Lead Nurture Smart Plan in Lofty

Copy and paste this entire prompt into Claude Cowork to build the Smart Plan.

---

## PROMPT START

You are the Lofty Automation Builder. Your job is to build a complete Smart Plan (Action Plan) inside Lofty CRM using computer use tools. You will navigate the Lofty interface, create the plan, and add every step by reading from the content files on disk.

---

## Prerequisites

- Browser must be open with Lofty CRM logged in at `https://account.lofty.com` or `https://app.lofty.com`
- You must have access to computer use tools (screenshot, click, type, navigate)
- The content files are at: `/Users/ryanrose/Downloads/Claude/Smart Plans/Seller Lead Nurture/`

---

## Step 1: Navigate to Smart Plans

1. Open Chrome and navigate to Lofty CRM
2. Take a screenshot to verify you're logged in as Ryan Rose
3. Navigate to **CRM** (left sidebar) → **Smart Plans** or **Action Plans**
4. If you see "Smart Plans" in the sidebar, click it. If not, look for "Automation" or "Action Plans"
5. Take a screenshot to confirm you're on the Smart Plans list page

**If redirected to login:** Pause and tell the user "Please log into Lofty CRM. Let me know when you're ready."

---

## Step 2: Create New Smart Plan

1. Click **"Create New Plan"** or **"+ New Plan"** button
2. Set the Plan Name: **Seller Lead Nurture — Evergreen**
3. Look for a trigger/enrollment setting. Set it to: **Tag Applied → sln-evergreen-nurture**
   - If you need to create the tag first, do so. The tag name is exactly: `sln-evergreen-nurture`
4. Look for "Stop on Reply" or "Pause when lead responds" setting. **Enable it.**
5. Look for any "Evergreen" or "No fixed start date" option. Enable it if available.
6. Take a screenshot to verify settings before saving

---

## Step 3: Read the Content Files

Before adding steps, read both content files:
- `/Users/ryanrose/Downloads/Claude/Smart Plans/Seller Lead Nurture/seller-nurture-smart-plan-FINAL.md` — Contains 130 emails
- `/Users/ryanrose/Downloads/Claude/Smart Plans/Seller Lead Nurture/sms-supplements.md` — Contains 26 SMS messages

The FINAL file has emails in this format:
```
### EMAIL [N] — Day [D] | Category: [Category Name]
**Delay:** [D] days
**Subject:** [Subject line]

[Email body]

Ryan Rose
Rose Homes LV
ryan@rosehomeslv.com
702-747-5921
```

SMS messages are at positions 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130.

---

## Step 4: Add Steps in Batches

Add steps one at a time in the Lofty Smart Plan editor. Work in batches of ~20 steps, verifying after each batch.

### For each EMAIL step:

1. Click **"Add Step"** or **"Add Action"** or the **"+"** button
2. Select action type: **Send Email**
3. Set the **delay:**
   - Email 1: 1 day (or "Day 1" / "Immediately" depending on Lofty's UI)
   - Email 2: The delay FROM THE PREVIOUS STEP. Since Email 1 is Day 1 and Email 2 is Day 15, the delay from step 1 to step 2 is **14 days**
   - **IMPORTANT:** Lofty Smart Plans use RELATIVE delays (days from previous step), not absolute days. Every email after Email 1 has a 14-day delay from the previous step. EXCEPT when an SMS falls between two emails, then calculate accordingly.
4. Enter the **Subject Line** exactly as written in the file
5. Enter the **Email Body** exactly as written in the file, including the signature block
6. Look for the **placeholder/merge field** button in the email editor. Verify that `#lead_first_name#` renders correctly in Lofty's editor. If Lofty uses a different format (like `{First Name}` or a dropdown insert), use Lofty's native format and replace all instances.
7. Set to **Automated Send** (not manual task/reminder)
8. Save the step

### For each SMS step:

1. Click **"Add Step"** or **"Add Action"**
2. Select action type: **Send Text/SMS**
3. Set the delay: SMS fires on the **same day** as its companion email. If the companion email was the previous step, set SMS delay to **0 days** (same day). If there were other steps in between, calculate accordingly.
4. Enter the **SMS body** exactly as written in the sms-supplements.md file
5. Verify `#lead_first_name#` renders correctly
6. Set to **Automated Send**
7. Save the step

### Step Order (interleaved emails + SMS):

The full sequence with SMS interleaved is:

| Step | Type | Position | Day | Delay from Previous |
|------|------|----------|-----|---------------------|
| 1 | Email | 1 | 1 | 1 day |
| 2 | Email | 2 | 15 | 14 days |
| 3 | Email | 3 | 29 | 14 days |
| 4 | Email | 4 | 43 | 14 days |
| 5 | Email | 5 | 57 | 14 days |
| 6 | SMS | 5 | 57 | 0 days |
| 7 | Email | 6 | 71 | 14 days |
| 8 | Email | 7 | 85 | 14 days |
| 9 | Email | 8 | 99 | 14 days |
| 10 | Email | 9 | 113 | 14 days |
| 11 | Email | 10 | 127 | 14 days |
| 12 | SMS | 10 | 127 | 0 days |
| 13 | Email | 11 | 141 | 14 days |
| 14 | Email | 12 | 155 | 14 days |
| 15 | Email | 13 | 169 | 14 days |
| 16 | Email | 14 | 183 | 14 days |
| 17 | Email | 15 | 197 | 14 days |
| 18 | SMS | 15 | 197 | 0 days |

**Pattern:** Every 5th email is followed by its SMS on the same day (0-day delay). All other emails have a 14-day delay from the previous step. BUT when an SMS was the previous step (0-day delay), the NEXT email must be 14 days from the EMAIL before the SMS, which means 14 days from the SMS step too since SMS has 0-day delay.

**Simplified rule:**
- After an Email step → next Email = 14 days
- After an Email step at position 5/10/15/etc → next SMS = 0 days
- After an SMS step → next Email = 14 days

---

## Step 5: Verify After Each Batch

After every ~20 steps:
1. Take a screenshot of the plan overview
2. Count the total number of steps
3. Verify the step count matches expected
4. Scroll through the steps to spot-check delays and content

### Batch Schedule:

| Batch | Steps to Add | Email Positions | SMS Positions | Expected Total After |
|-------|-------------|-----------------|---------------|---------------------|
| 1 | 1-24 | 1-20 | 5, 10, 15, 20 | 24 |
| 2 | 25-48 | 21-40 | 25, 30, 35, 40 | 48 |
| 3 | 49-72 | 41-60 | 45, 50, 55, 60 | 72 |
| 4 | 73-96 | 61-80 | 65, 70, 75, 80 | 96 |
| 5 | 97-120 | 81-100 | 85, 90, 95, 100 | 120 |
| 6 | 121-144 | 101-120 | 105, 110, 115, 120 | 144 |
| 7 | 145-156 | 121-130 | 125, 130 | 156 |

---

## Step 6: Final Settings

After all 156 steps are added:

1. Scroll to the top of the plan
2. Verify the plan name: **Seller Lead Nurture — Evergreen**
3. Verify the trigger tag: **sln-evergreen-nurture**
4. Verify **Stop on Reply** is enabled
5. Verify all steps are set to **Automated Send**
6. **Save the plan**
7. **Activate the plan** (switch from Draft to Active if applicable)
8. Take a final screenshot

---

## Step 7: Create the Trigger Tag

If not already done during plan creation:

1. Navigate to CRM → Tags or Settings → Tags
2. Create tag: `sln-evergreen-nurture`
3. Verify the tag is linked to this Smart Plan as an enrollment trigger
4. Take a screenshot confirming the tag exists and is linked

---

## Step 8: Build Log

After completing the build, write a build log to:
`/Users/ryanrose/Downloads/Claude/Smart Plans/Seller Lead Nurture/build-log.md`

Include:
- Total steps created
- Any errors encountered and how they were resolved
- Screenshots taken at each verification point
- Whether the plan is saved and active
- The exact tag name created
- Any differences between Lofty's placeholder format and what was in the content files

---

## Placeholder Note

The content files use `#lead_first_name#` which is the standard Lofty merge field format. However, Lofty's visual editor may show this as a blue chip/tag that says "First Name" rather than the raw code. When entering content:

1. First check what merge fields Lofty has available (look for an "Insert Merge Field" or "Personalize" button in the email editor)
2. If Lofty shows `#lead_first_name#` as raw text, that's correct
3. If Lofty uses a visual insert method, use that instead and replace every instance of `#lead_first_name#` in the email body with Lofty's native merge field

Also check for these additional merge fields that may be available:
- `#agent_full_name#`
- `#agent_phone#`
- `#agent_email#`

The emails currently hardcode Ryan's name and contact info in the signature. This is fine, but if you want to use agent merge fields in the signature instead, you can.

---

## Error Recovery

- **If the browser crashes:** Reopen Lofty, navigate to Smart Plans, find "Seller Lead Nurture — Evergreen", and continue from the last verified step count.
- **If a step fails to save:** Screenshot the error, retry once. If it fails again, skip it and log it in the build log for manual fix later.
- **If Lofty has a step limit:** If you hit a maximum step limit (e.g., 100 steps), stop and tell the user. We'll need to split into two linked plans: "Seller Lead Nurture — Evergreen (Year 1-3)" and "Seller Lead Nurture — Evergreen (Year 3-5)" with a handoff tag.
- **If Lofty's delay options don't support days beyond a certain number:** Report the limitation. We may need to restructure delays.

---

## PROMPT END
