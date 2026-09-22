# Google Form to Lofty CRM Setup Guide

## SkyeView Terra Lead Capture Form

This guide walks you through three things:

1. Creating the Google Form for the SkyeView Terra landing page
2. Embedding it in your landing page HTML
3. Connecting it to Lofty CRM so leads trigger the smart plan automatically

**Total setup time:** 30 to 45 minutes
**Lead delivery speed to Lofty:** 1 to 3 seconds after submission

---

## Part 1: Create the Google Form

### Step 1: New Form

1. Go to https://forms.google.com
2. Click the blank form (plus icon) at the top left
3. Sign in with `ryan@rosehomeslv.com`

### Step 2: Form Title and Description

- **Form title:** `SkyeView Terra Buyer Guide Request`
- **Description:**
  ```
  Get the complete SkyeView Terra buyer guide, including floor plans, pricing, builder incentives, HOA details, and current quick move-in homes. We will send it to your inbox within minutes. No spam.
  ```

### Step 3: Form Settings

Click the **Settings** tab at the top.

**Responses section:**
- Collect email addresses: **Off** (we ask for it as a question instead, so we can validate it)
- Allow response editing: **Off**
- Limit to 1 response: **Off**

**Presentation section:**
- Show progress bar: **Off**
- Shuffle question order: **Off**
- Show link to submit another response: **Off**
- Confirmation message:
  ```
  Thanks! Ryan will send your SkyeView Terra buyer guide to your inbox within a few minutes. If you need anything sooner, text 702-747-5921.
  ```

**Defaults section:**
- Make questions required by default: **On**

### Step 4: Add the Questions

Switch back to the **Questions** tab.

#### Question 1: Full Name
- **Type:** Short answer
- **Question:** `Full Name`
- **Required:** Yes
- **Response validation:** None

#### Question 2: Email
- **Type:** Short answer
- **Question:** `Email`
- **Required:** Yes
- **Response validation:**
  - Click the three dots, choose "Response validation"
  - Select **Text** then **Email**
  - Custom error: `Please enter a valid email address.`

#### Question 3: Phone
- **Type:** Short answer
- **Question:** `Phone`
- **Description:** `Best number to reach you. We will only text or call about SkyeView Terra.`
- **Required:** Yes

#### Question 4: Timeline
- **Type:** Multiple choice
- **Question:** `When are you looking to buy?`
- **Required:** Yes
- **Options:**
  - `ASAP`
  - `1 to 3 months`
  - `3 to 6 months`
  - `Just browsing`

#### Question 5: Pre-Approval
- **Type:** Multiple choice
- **Question:** `Are you pre-approved for a mortgage?`
- **Required:** Yes
- **Options:**
  - `Yes`
  - `No`
  - `Not yet, but I want help with that`

### Step 5: Style the Form

Click the **Customize theme** icon (paint palette, top right).

- **Header:** Upload a SkyeView Terra hero image (use any of the model photos in `research-report.md`)
- **Theme color:** `#1a3a5c` (Century Communities navy, custom hex)
- **Background color:** Light gray
- **Font style:** Default

This makes the embedded form match the landing page brand.

### Step 6: Publish

Click the **Send** button (top right) and choose your audience: **Anyone with the link**.

---

## Part 2: Embed the Form in the Landing Page

### Step 1: Get the Embed Code

1. With the form open, click **Send** (top right)
2. Click the **embed icon** `< >`
3. Note the iframe `src` URL. It looks like:
   ```
   https://docs.google.com/forms/d/e/1FAIpQLSdXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX/viewform?embedded=true
   ```
4. Copy that full URL

### Step 2: Paste It Into the Landing Page

1. Open `landing-page.html` in your editor
2. Search for `REPLACE_WITH_YOUR_FORM_ID`
3. Replace the entire `src` value with the URL from Step 1
4. Save the file

The form area on the landing page is now live. The form posts directly to your Google Sheet of responses.

---

## Part 3: Connect Google Form to Lofty CRM

You have **three options**, ranked from fastest to slowest:

| Option | Speed | Cost | Skill Needed |
|--------|-------|------|--------------|
| A. Apps Script + Lofty Webhook | 1 to 3 sec | Free | Easy (paste code) |
| B. Zapier | 1 to 3 min | Free tier or $20/mo | None (visual) |
| C. Email Parser | 1 to 5 min | Free | None |

**Recommended: Option A.** It is fast, free, and uses no external services.

---

### Option A: Apps Script + Lofty Webhook (Recommended)

This runs a small script every time someone submits the form. The script POSTs the lead data to Lofty's webhook URL, which auto-creates the contact and applies the `skyeview-terra` tag.

#### Step 1: Get Your Lofty Webhook URL

1. Log into Lofty CRM
2. Go to **Settings** > **Integrations** (or **Lead Sources**, depending on your version)
3. Look for **Webhook URL**, **Inbound Lead URL**, or **API Endpoint**
4. Copy that URL. It will look something like:
   ```
   https://api.lofty.com/v1/leads/inbound?key=YOUR_API_KEY
   ```
   The exact format depends on your Lofty plan. If you do not see a webhook option, contact Lofty support and ask: "What is my inbound lead webhook URL for custom integrations?"

#### Step 2: Open the Apps Script Editor

1. Open your Google Form
2. Click the three dots in the top right
3. Click **Script editor**
4. A new tab opens with `Code.gs`

#### Step 3: Paste the Integration Code

1. Delete everything in `Code.gs`
2. Open the file `google-form-apps-script.js` in this folder
3. Copy all of its contents
4. Paste into `Code.gs`
5. Replace `YOUR_LOFTY_WEBHOOK_URL_HERE` with the URL from Step 1

#### Step 4: Set the Trigger

1. In the Apps Script editor, click the **clock icon** (Triggers) on the left sidebar
2. Click **Add Trigger** (bottom right)
3. Set:
   - Choose function: `onFormSubmit`
   - Choose deployment: `Head`
   - Event source: `From form`
   - Event type: `On form submit`
   - Failure notifications: `Notify me immediately`
4. Click **Save**
5. Google will ask for permissions. Approve them.

#### Step 5: Test the Integration

1. Open your form preview (click the eye icon in the form editor)
2. Submit a test entry with your own info
3. Check Lofty CRM. Within 1 to 3 seconds, you should see a new contact with:
   - First name, last name, email, phone filled in
   - Tag: `skyeview-terra`
   - Source: `SkyeView Terra Landing Page`
   - Notes field with timeline and pre-approval answers
4. Verify the smart plan auto-started

If the contact does not appear:

- Open Apps Script, click **Executions** in the left sidebar
- Look for the most recent run. If it failed, the error message will tell you what is wrong.
- Common issues:
  - Lofty webhook URL is wrong (re-check Step 1)
  - Lofty expects a different field format. Adjust the `payload` object in the Apps Script.

---

### Option B: Zapier (No Code)

Use this if Apps Script feels like too much. It works but adds 1 to 3 minutes of delay.

1. Sign up at https://zapier.com (free tier handles up to 100 leads per month)
2. Click **Create Zap**
3. Trigger: **Google Forms** > **New Form Response**
   - Connect your Google account
   - Choose `SkyeView Terra Buyer Guide Request` as the form
4. Action: **Webhooks by Zapier** > **POST**
   - URL: Your Lofty webhook URL
   - Payload type: JSON
   - Data:
     - `firstName`: Map to first word of Full Name field
     - `lastName`: Map to remaining words of Full Name field
     - `email`: Map to Email field
     - `phone`: Map to Phone field
     - `tags`: `skyeview-terra`
     - `source`: `SkyeView Terra Landing Page`
     - `notes`: Combine timeline and pre-approval answers
5. Test the Zap with a sample form response
6. Turn the Zap on

---

### Option C: Email Parser (Universal Fallback)

Use this only if Options A and B do not work. Lofty parses emails sent to your dedicated inbound address.

1. In Lofty, find your **inbound email address** (Settings > Integrations > Email Lead Parser). It looks like `leads-rosehomeslv@inbound.lofty.com`.
2. In your Google Form settings, turn on **Email notifications for this form** (Responses tab > three dots > Get email notifications)
3. Set up a Gmail filter that forwards form notification emails to the Lofty inbound address.
4. Important caveat: this method usually does NOT support custom tags. You may need to manually tag leads in Lofty after they arrive, which means the smart plan will not auto-start. Only use this if you cannot use Option A or B.

---

## Part 4: Track Assignment Logic

The smart plan blueprint defines three tracks based on the qualifying answers:

| Timeline | Pre-Approved | Track |
|----------|--------------|-------|
| ASAP or 1 to 3 months | Yes | **Hot** |
| 1 to 3 or 3 to 6 months | Any | **Warm** |
| Just browsing | Any | **Nurture** |

The Apps Script automatically calculates this and sends the right track name to Lofty in the `notes` and `customField` payload.

In Lofty, you have two options for triggering the right track:

**Option 1: Use the qualifying answers to assign track**
- In Lofty Settings > Smart Plans, set up rules:
  - If tag is `skyeview-terra` AND custom field `track` is `hot`, start Hot plan
  - If tag is `skyeview-terra` AND custom field `track` is `warm`, start Warm plan
  - If tag is `skyeview-terra` AND custom field `track` is `nurture`, start Nurture plan

**Option 2: Default everyone to Warm and manually move Hot leads**
- Tag `skyeview-terra` triggers the Warm smart plan
- You manually move leads to Hot or Nurture as you review them in Lofty

Most agents start with Option 2 because it is simpler. As you grow, switch to Option 1.

---

## Part 5: Testing Checklist

Before pointing real ad traffic at the landing page, run through this:

- [ ] Submit the Google Form with a test lead (use your own info)
- [ ] Verify the form thank-you message appears
- [ ] Check Apps Script Executions log for any errors
- [ ] Open Lofty within 30 seconds. Confirm the new lead appears.
- [ ] Verify these fields populated correctly:
  - First name
  - Last name
  - Email
  - Phone (10 digits, no dashes is fine)
  - Tag: `skyeview-terra`
  - Source: `SkyeView Terra Landing Page`
  - Notes: includes timeline and pre-approval answers
- [ ] Confirm the SkyeView Terra Warm smart plan started automatically
- [ ] Verify the first text and email in the smart plan fired (or scheduled to fire)
- [ ] Verify the DO/BBRA PDF attached to the Day 0 email
- [ ] Delete the test contact in Lofty when done

If everything passes, you are live.

---

## Part 6: Maintenance Notes

- **If you change the Google Form questions**, update the field names in the Apps Script `payload` object
- **If you add new communities**, create a separate Google Form per community and copy the Apps Script with the new tag
- **Apps Script free quota:** 1,500 form submissions per day. You will not hit this with normal lead volume.
- **Google Forms free quota:** Unlimited
- **Lofty webhook quota:** Check your Lofty plan. Most plans allow at least 500 inbound leads per month.

---

## Part 7: What Goes Where

```
Lead submits form
    |
    V
Google Forms (saves response in Sheet)
    |
    V
Apps Script trigger fires (within 1 sec)
    |
    V
POST to Lofty webhook (200 ms)
    |
    V
Lofty creates contact + applies tag
    |
    V
Smart plan auto-starts
    |
    V
Day 0 text + email fire
    |
    V
DO/BBRA PDF attached to email
    |
    V
Builder rep notification email sent to ryan@rosehomeslv.com
```

End to end: under 5 seconds from form submit to first text hitting the lead's phone.

---

## Need Help?

If something is not working, check in this order:

1. **Apps Script Executions log** - shows the exact error
2. **Lofty integrations log** - shows if Lofty received the POST
3. **Google Forms response sheet** - confirms the form is collecting data

If still stuck, the issue is almost always the Lofty webhook URL format. Contact Lofty support with the error message from the Apps Script log.
