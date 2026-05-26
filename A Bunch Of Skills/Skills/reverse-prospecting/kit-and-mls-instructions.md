# Reverse Prospecting — MLS + Kit Setup Instructions

These checklists are printed at the end of each reverse prospecting email generation, with all listing-specific details filled in. They guide Ryan through the manual steps of extracting agent emails from MLS and setting up the broadcast in Kit.

When printing these checklists, replace every `[PLACEHOLDER]` with the actual listing data collected during the workflow.

---

## MLS Reverse Prospecting — Agent Email Extraction

```
REVERSE PROSPECTING — AGENT EMAIL EXTRACTION
Property: [FULL_ADDRESS] | MLS# [MLS_NUMBER]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[ ] 1. Log into Matrix MLS at https://las.mlsmatrix.com

[ ] 2. Search for your listing: MLS# [MLS_NUMBER]
       (or navigate to My Matrix > My Listings)

[ ] 3. Open the listing detail page for [FULL_ADDRESS]

[ ] 4. Click the "Reverse Prospecting" tab on the listing

[ ] 5. Review the results — these are agents whose buyers
       have saved searches matching this listing

FILTER BY COUNT:

[ ] 6. Look at the "Count" column for each agent result.
       This shows how many total listings match that buyer's
       saved search criteria.

       ONLY select agents with a count UNDER 50.
       A count of 50+ means the buyer's search is too broad
       to be a meaningful match for this specific listing.

[ ] 7. Check for any prospects who SAVED or FAVORITED the
       listing. Note these agents separately — they get
       priority outreach and a personalized mention.
       Write down which agents saved/favorited it:
       _________________________________________________

[ ] 8. Select the filtered agents (count < 50 only)

[ ] 9. Export the agent list:
       - Click "Export" or "Email" button
       - Choose CSV/Excel if available
       - Or copy email addresses manually from the results

[ ] 10. Save the exported emails — you will import these
        into Kit in the next section

[ ] 11. Note the totals:
        _____ agents exported (count < 50)
        _____ agents who saved/favorited the listing

NOTE: If the listing is not yet Active or Coming Soon in MLS,
reverse prospecting results may not appear. Check your listing
status if no results are returned.
```

---

## Kit (ConvertKit) — Broadcast Setup

```
KIT BROADCAST SETUP — REVERSE PROSPECTING EMAIL
Property: [FULL_ADDRESS]
Subject:  [SUBJECT_LINE]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CREATE THE BROADCAST:

[ ] 1. Log into Kit at https://app.kit.com

[ ] 2. Navigate to: Broadcasts > New Broadcast

UPLOAD IMAGES:

[ ] 3. Go to your Kit Image Library

[ ] 4. Upload PHOTO 1 (hero exterior):
       File: [HERO_IMAGE_FILENAME]
       Path: Listings/[ADDRESS_FOLDER]/Listing Photos/.../[HERO_IMAGE_FILENAME]

[ ] 5. Upload PHOTO 2 (interior):
       File: [INTERIOR_IMAGE_FILENAME]
       Path: Listings/[ADDRESS_FOLDER]/Listing Photos/.../[INTERIOR_IMAGE_FILENAME]

[ ] 6. Copy the hosted URL Kit gives you for each image

PASTE THE HTML:

[ ] 7. In the broadcast editor, add a "Custom HTML" content block
       (or use File > Import HTML if your plan supports it)

[ ] 8. Open the generated email file:
       [OUTPUT_FILE_PATH]

[ ] 9. Copy everything inside the <body> tag

[ ] 10. Paste into the Custom HTML block in Kit

[ ] 11. Replace the hero image placeholder:
        Find:    [KIT IMAGE URL: [HERO_IMAGE_FILENAME]]
        Replace: (paste the hosted URL from Step 6)

[ ] 12. Replace the interior image placeholder:
        Find:    [KIT IMAGE URL: [INTERIOR_IMAGE_FILENAME]]
        Replace: (paste the hosted URL from Step 6)

SET UP SUBSCRIBERS:

[ ] 13. Create a new tag for this broadcast:
        Suggested: "RP - [STREET_ADDRESS] - [DATE]"

[ ] 14. Import the agent emails from the MLS export:
        Subscribers > Import > paste CSV or upload file

[ ] 15. Apply the tag from Step 13 to the imported subscribers

[ ] 16. In the broadcast settings, set recipients to this tag

FINAL CHECKS:

[ ] 17. Set the subject line:
        [SUBJECT_LINE]

[ ] 18. Set the sender: Ryan Rose <ryan@rosehomeslv.com>

[ ] 19. Preview the email and verify:
        - Both images display correctly
        - Layout looks right on desktop and mobile
        - Gold badge shows "[BADGE_TEXT]"

[ ] 20. Send a test email to ryan@rosehomeslv.com
        Check:
        - {{ subscriber.first_name }} displays your test name
        - ShowingTime button works (or shows placeholder)
        - Reply and call/text links work
        - Open on your phone to check mobile layout

[ ] 21. When everything looks good, click Send (or Schedule)

Kit will automatically append the unsubscribe link.
```

---

## Future Automation Note

When browser automation (Puppeteer, Playwright, or similar MCP tool) becomes available, both checklists above can be converted to automated steps. The MLS extraction (Steps 1-11) and Kit broadcast setup (Steps 1-21) are the primary candidates for automation. The HTML generation step is already automated by this skill.
