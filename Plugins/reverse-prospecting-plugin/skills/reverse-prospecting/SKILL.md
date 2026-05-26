---
name: reverse-prospecting
description: Use when someone asks to create a reverse prospecting email, extract agent emails from MLS, set up a Kit broadcast for a listing, or run the full reverse prospecting campaign for a property.
---

## What This Skill Does

Runs the full reverse prospecting workflow for a listing: generates the HTML agent-to-agent email, extracts matching agents from MLS via browser, uploads images to Kit, creates the broadcast, and sends it. All steps use browser automation.

**Ryan Rose info:** Real Broker, LLC | 702-747-5921 | ryan@rosehomeslv.com | rosehomeslv.com | License #S.0185572
**Listing folder:** /Users/ryanrose/Downloads/Claude/Listings/
**Email template:** /Users/ryanrose/.claude/skills/reverse-prospecting/email-template.html

---

## Step 1: Locate the Listing and Gather Data

Search for a matching folder under `/Users/ryanrose/Downloads/Claude/Listings/` (folder name = street address, e.g., "29 Amber Rock St").

Read available files to gather property details:
- Marketing package (`.docx`) for features
- Existing reverse prospecting email (if already generated)
- Catalog photos in the `Listing Photos/` subfolder

**Required property details:**
- Full address (street, city, state, zip)
- List price
- MLS number
- Active date
- Beds / Baths / Square footage
- Garage type and count
- Story type (Single, Two-Story)
- Subdivision name
- Year built
- Lot size
- Solar (Owned/Leased/None)
- Occupancy (Vacant/Occupied)
- Showing method (ShowingTime, etc.)

**Photo selection:**
- Hero image: prefer filenames containing "twilight" first, then `dji_` prefix (drone), then ask
- Interior image: suggest kitchen as default

**Email copy:**
- Badge text: Coming Soon, Just Listed, Price Reduced, Back on Market, or Open House
- Subject line format: `Your buyer might be a match | Ref #{{ subscriber.ref_number }} | [Badge] in [City]`
- Agent note: two paragraphs, professional but warm, one colleague to another
  - Paragraph 1: reverse prospecting context + hook (what makes this listing worth a look)
  - Paragraph 2: subdivision, year built, notable features, availability/showing info

**Copy rules:** No em-dashes. No "stunning/gorgeous/dream home." Short sentences. Data-rich. Don't repeat info already visible in other email sections (price, beds/baths, address, MLS#).

---

## Step 2: Generate the Email HTML

1. Read the master template at `/Users/ryanrose/.claude/skills/reverse-prospecting/email-template.html`
2. Replace all `[BRACKET]` placeholders with actual property data
3. Save to: `/Users/ryanrose/Downloads/Claude/Listings/[Address Folder]/[Number]_[Street]_Agent_Reverse_Prospecting_Email.html`
   - Example: `29_Amber_Rock_Agent_Reverse_Prospecting_Email.html`

If an email already exists in the listing folder, use it instead of regenerating.

---

## Step 3: Extract Agent Emails from MLS (Browser)

1. Open Chrome and navigate to **https://las.mlsmatrix.com**
2. If a login screen appears, pause: "Please log into Matrix MLS. Let me know when you're ready."
3. Search for the listing by MLS number, or go to My Matrix > My Listings
4. Open the listing detail page
5. Click the **"Reverse Prospecting"** tab
6. Review the results. Look at the **"Count"** column for each agent:
   - **ONLY select agents with a count UNDER 50.** A count of 50+ means the buyer's search is too broad to be a meaningful match.
7. **Capture the "Ref #" column** for each agent. This is the client-specific reference number used for subject line personalization in Kit.
8. Check for agents who **SAVED or FAVORITED** the listing. Note their names and Ref #s separately for priority follow-up.
9. Select the filtered agents (count < 50 only) and click **"Export"** (CSV/Excel). If no export button, copy email addresses and Ref #s manually.
10. Save the export file.
11. Report totals: "Extracted [X] agents (count < 50). [Y] agents saved/favorited the listing."

---

## Step 4: Upload Images to Kit (Browser)

1. Navigate to **https://app.kit.com**
2. If a login screen appears, pause: "Please log into Kit. Let me know when you're ready."
3. Go to the **Image Library** (or Assets area)
4. Upload the **hero image** from the listing's Listing Photos folder
5. Upload the **interior image** from the listing's Listing Photos folder
6. Copy the **hosted URL** Kit provides for each uploaded image
7. Report: "Both images uploaded to Kit."

---

## Step 5: Create the Kit Broadcast (Browser)

1. Go to **Broadcasts > New Broadcast**
2. Add a **Custom HTML** content block (or use File > Import HTML)
3. Open the generated email file from Step 2. Copy everything inside the `<body>` tag.
4. Paste into the Custom HTML block in Kit
5. Replace the two image placeholder URLs:
   - Find `[KIT IMAGE URL: [hero filename]]` and replace with the Kit hosted URL from Step 4
   - Find `[KIT IMAGE URL: [interior filename]]` and replace with the Kit hosted URL from Step 4
6. **Create a tag:** `RP - [Street Address] - [Today's Date YYYY-MM-DD]`
7. **Import subscribers:** Go to Subscribers > Import, upload the MLS export from Step 3. Apply the tag. **CRITICAL: Map the "Ref #" column to a custom field called `ref_number`** so Kit can personalize the subject line per agent.
8. **Set broadcast recipients** to the new tag
9. **Set subject line** (from Step 1)
10. **Set sender** to: `Ryan Rose <ryan@rosehomeslv.com>`
11. **Preview** the email. Verify:
    - Both images display correctly
    - Layout works on desktop and mobile
    - Badge text is correct
    - `{{ subscriber.first_name }}` tag is intact
12. **Send a test** to ryan@rosehomeslv.com
13. Pause and ask: "Test email sent to ryan@rosehomeslv.com. Check your inbox and phone. Ready to send to all agents?"
14. Once confirmed, click **Send** (or Schedule)

After sending, remind:
- "Agents who saved/favorited the listing: [names]. Consider a direct call or text as priority follow-up."

---

## Important Rules

- **No em-dashes** in any copy. Use commas, periods, or "and."
- **Never make up property details.** Use [BRACKETS] for anything unknown.
- **Only export agents with count < 50** from MLS reverse prospecting. Broad searches are not meaningful matches.
- **Always map Ref # to `ref_number` custom field** during Kit subscriber import. This enables subject line personalization.
- The Kit personalization tag `{{ subscriber.first_name | default: "there" }}` is hardcoded in the template. Do not modify it.
- If the listing is not yet Active or Coming Soon in MLS, reverse prospecting results may not appear.
- Always pause before the final send to let Ryan verify the test email.
