# Meta Listing Lead Form Campaign: 29 Amber Rock St

**Property:** 29 Amber Rock St, Champion Village, Henderson NV 89012
**MLS:** 2759238
**Price:** $485,000
**Specs:** 3 bed / 2 bath, single-story, 3-car garage
**Campaign Type:** Listing Lead Form (Leads Objective with Instant Form)
**Created:** March 21, 2026

---

## Campaign Configuration (Meta Business Suite)

### Goal
- **Objective:** Get more leads
- **Performance goal:** Maximize leads likely to become customers

### Ad Creative

**Ad Text (Variation 1 - Similar Homes Hook):**
Love this Champion Village home? There are more like it. 3 beds, single-story with a 3-car garage, starting in the $480s. I'll send you matches as they come up.

**Headline:** Henderson Home Alerts (21/25 chars)
**Button Label (CTA):** Sign up
**Media:** Single hero listing photo (uploaded manually via Browse media)

### Additional Ad Copy Variations (for duplication in Ads Manager)

**Variation 2 (Alerts Hook):**
This 3-bed in Champion Village is getting a lot of attention. Want to be first to know when similar homes hit the market? I'll set you up with instant alerts.
- Headline: Get Home Alerts
- Description: New listings, sent first

**Variation 3 (Neighborhood Lifestyle Hook):**
Champion Village keeps drawing buyers for a reason. Move-in ready homes, established neighborhoods, and great schools. Curious what's available? I'll send you options.
- Headline: Homes in Champion Village
- Description: See what's available now

**Variation 4 (Price Point Hook):**
Homes in Champion Village range from the $400s to $550s. This 3-bed at $485K is one of several on the market right now. Want the full list? I'll send it over.
- Headline: Champion Village Prices
- Description: Get the full list free

### Targeting
- **Special Ad Category:** Housing (required for real estate)
- **Location:** Las Vegas, Nevada, United States (+20 mile radius)
- **Age:** 18 - 65+
- **Gender:** All (restricted by Housing category)
- **Placements:** Advantage+ (auto across Facebook, Instagram, Messenger, Meta Audience Network)

### Budget and Schedule
- **Daily Budget:** $10.00/day
- **Duration:** 30 days
- **End Date:** April 20, 2026
- **Total Budget:** $300.00

### Instant Form Configuration
- **Form Name:** 29 Amber Rock, Champion Village Home Interest
- **Contact Fields:**
  - Full name (checked)
  - Phone number (checked)
  - Email (checked)
- **Qualifying Question 1:** When are you looking to buy? (ASAP / 1-3 months / 3-6 months / Just browsing)
- **Qualifying Question 2:** Are you pre-approved for a mortgage? (Yes / No / Not yet)
- **Privacy Policy Link Text:** Privacy Policy
- **Privacy Policy URL:** https://www.rosehomeslv.com/site/privacy-terms
- **Form Language:** English (US)

---

## Important Notes

1. **Only 1 ad variation** was entered in the simplified Meta Business Suite flow. Variations 2-4 can be duplicated via Ads Manager after publishing.

2. **Headline was broadened** from "Get Champion Village Listings" to "Henderson Home Alerts" because Champion Village alone is too small a sample size to attract volume.

3. **Thank you screen** is not configurable in the simplified builder. Can be customized in Ads Manager after creation.

4. **Account spending limit warning** appeared during setup. May need to increase or reset the spending limit before the campaign can run its full course.

5. **Funds available at time of setup:** $8.59. Funds need to be added to cover the $300 total budget.

6. **Property address is never included in ad copy** per best practices. Only neighborhood, features, and price are referenced.

7. **No em-dashes** used in any ad copy per content guidelines.

---

## Lead Follow-Up Plan

Leads from this form should be routed into Lofty CRM and assigned to Action Plans based on qualifying answers:

| Timeline Answer | Pre-Approved? | Lead Tier | Action Plan |
|---|---|---|---|
| ASAP | Yes | HOT | Hot Lead - Immediate Outreach |
| ASAP | No / Not yet | WARM | Warm Lead - Nurture + Lender Intro |
| 1-3 months | Yes | WARM | Warm Lead - Drip Sequence |
| 1-3 months | No / Not yet | WARM | Warm Lead - Nurture + Lender Intro |
| 3-6 months | Any | NURTURE | Nurture - Long-term Drip |
| Just browsing | Any | NURTURE | Nurture - Long-term Drip |

**Lofty Action Plans still need to be created** (Hot, Warm, Nurture tracks with 30-day follow-up sequences).

---

## Campaign Document
The full campaign doc with all 4 variations, targeting specs, and visual plan is saved at:
`Listings/29 Amber Rock St/Phase 3/Meta Ad Campaign - Lead Form.docx`

---

## Browser Automation Notes

### Issues Encountered During Setup
- **Navigation timeouts:** Initial attempts to navigate to Meta Business Suite timed out. Resolved by using an already-open Meta tab.
- **Image upload:** Browser automation couldn't trigger Meta's React file upload component. Ryan manually uploaded the hero photo.
- **Wrong Las Vegas:** Initially selected Las Vegas, NM instead of Las Vegas, NV. Corrected by removing and re-adding the correct location.
- **Budget input:** The budget field didn't respond to keyboard select-all. Used `form_input` tool to set the value directly.
- **Button label dropdown:** Required using the `find` tool to locate the exact option element ref, as coordinate-based clicks on the dropdown options weren't registering.

### Meta Business Suite URL
`https://business.facebook.com/latest/consolidatedad/` (via the simplified ad creation flow, not full Ads Manager)

### Ad Account
- **Ad Account ID:** 739987375117947
- **Page:** Ryan Rose - Real Broker LLC
