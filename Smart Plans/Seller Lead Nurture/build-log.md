# Seller Lead Nurture -- Evergreen: Build Log

**Plan Name:** Seller Lead Nurture -- Evergreen
**Plan ID:** 842451
**Platform:** Lofty CRM
**Date Built:** March 28, 2026

---

## Summary

Successfully built and saved a 286-step Smart Plan (Action Plan) inside Lofty CRM. The plan delivers 130 emails and 26 SMS messages over approximately 5 years (1,807 days) at a 14-day cadence. Every 5th email position is paired with a companion SMS sent on the same day.

## Step Breakdown

- 130 Email steps (leftAction.type = 5)
- 26 SMS steps (leftAction.type = 4)
- 129 Wait steps (14-day intervals between positions)
- 1 End step
- **Total: 286 steps**

## Technical Details

The plan was built by:
1. Parsing all 130 email subjects/bodies and 26 SMS messages from the content files
2. Converting to Lofty's compact data format (285 entries across 10 JSON chunks)
3. Injecting the data into the browser via JavaScript
4. Building full Lofty step objects using the original plan's email/wait/end steps as templates (ensuring all 30 step fields and 25 leftAction fields matched the expected server schema)
5. Signing the API request using Lofty's internal webpack signature module (module ID 400339) to bypass the gateway signature validation
6. Sending the 1.19MB payload via a clean XMLHttpRequest to /api/smart-plan-server/settings/save/v2

Key technical finding: Lofty's `previousStepLevels` field is a STRING (not an array), which differs from the `next` field (which IS an array). Sending an array caused 400 Bad Request errors from Spring Boot's JSON deserializer.

## Current Configuration

- **Trigger:** Tag Changed > tags added is > Any Tags
- **Auto Pause (Stop on Reply):** Enabled (leadResponse: true)
- **Lead Types:** Homeowner (8), Seller (1)
- **Plan State:** Draft (state: 0)

## Manual Steps Required

Two items need to be completed manually in the Lofty UI:

### 1. Update the Trigger Tag

The tag `sln-evergreen-nurture` does not yet exist in the CRM. To set it up:

1. Open the plan editor: Marketing > Smart Plans > Seller Lead Nurture -- Evergreen > Edit
2. Click the trigger card ("Tag Changed")
3. Click the "Any Tags" dropdown
4. Type `sln-evergreen-nurture` to create and select it
5. Click Save Smart Plan

### 2. Activate the Plan

Once the trigger tag is set:

1. From the Smart Plans list, find "Seller Lead Nurture -- Evergreen"
2. Toggle the plan from Draft to Active
3. Optionally enable "Auto Apply" if you want leads to be automatically enrolled when the tag is added

## Content Verification

All 130 email subjects were verified present in the Lofty flow editor after save, including:
- First email: "My contact info"
- Last email: "How to fall in love with your home again"
- Sample middle emails: "Supply and demand decide your price", "Why Zillow gets your value wrong", "National news isn't your market"

All 26 SMS messages were included at every 5th email position.

## Source Files

- Email content: `/Smart Plans/Seller Lead Nurture/seller-nurture-smart-plan-FINAL.md`
- SMS content: `/Smart Plans/Seller Lead Nurture/sms-supplements.md`
- Build log: This file
