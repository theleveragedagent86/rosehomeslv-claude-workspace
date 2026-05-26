# Task: Complete Reverse Prospecting Email Setup for 29 Amber Rock St

You are completing the MLS reverse prospecting extraction and Kit broadcast setup for a listing. All content is already generated. You just need to execute the online steps.

---

## PROPERTY DETAILS (reference only)

- **Address:** 29 Amber Rock St, Henderson, NV 89012
- **MLS#:** 2759238
- **Price:** $485,000
- **Badge:** Coming Soon
- **Active Date:** March 11, 2026

---

## PART 1: MLS REVERSE PROSPECTING — EXTRACT AGENT EMAILS

1. Go to https://las.mlsmatrix.com and log in
2. Search for MLS# **2759238** (or go to My Matrix > My Listings and find 29 Amber Rock St)
3. Open the listing detail page
4. Click the **"Reverse Prospecting"** tab
5. Review the results. These are agents whose buyers have saved searches matching this listing.
6. **Filter by Count column:** ONLY select agents with a count **under 50**. A count of 50+ means the buyer's search is too broad to be a meaningful match.
7. **Check for agents who SAVED or FAVORITED the listing.** Write down their names separately. They get priority follow-up.
8. Select the filtered agents (count < 50 only)
9. **Export** the agent email list (CSV/Excel if available, or copy manually)
10. Save the exported file. You'll import it into Kit next.
11. Note the totals: how many agents exported, how many saved/favorited.

---

## PART 2: KIT BROADCAST SETUP

### A. Upload Images

1. Go to https://app.kit.com and log in
2. Go to the **Image Library**
3. Upload **PHOTO 1** (hero exterior):
   - File path: `/Users/ryanrose/Downloads/Claude/Listings/29 Amber Rock St/Listing Photos/29_amber_rock_st-8934_web_v24/dji_20260223130017_0005_d_twilight_2f4cf81d-fd19-448e-8bdf-7d1f6b1b85dc.jpg`
4. Upload **PHOTO 2** (interior/kitchen):
   - File path: `/Users/ryanrose/Downloads/Claude/Listings/29 Amber Rock St/Listing Photos/29_amber_rock_st-8934_web_v24/dsc05510.jpg`
5. **Copy the hosted URL** Kit gives you for each uploaded image. You'll need both URLs in the next section.

### B. Create the Broadcast

1. Navigate to **Broadcasts > New Broadcast**
2. Add a **"Custom HTML"** content block (or use File > Import HTML)
3. Open this file and copy everything inside the `<body>` tag:
   - File path: `/Users/ryanrose/Downloads/Claude/Listings/29 Amber Rock St/29_Amber_Rock_Agent_Reverse_Prospecting_Email.html`
4. Paste into the Custom HTML block in Kit
5. **Replace the hero image placeholder:**
   - Find: `[KIT IMAGE URL: dji_20260223130017_0005_d_twilight.jpg]`
   - Replace with: the hosted URL from the hero image upload
6. **Replace the interior image placeholder:**
   - Find: `[KIT IMAGE URL: dsc05510.jpg]`
   - Replace with: the hosted URL from the kitchen image upload

### C. Set Up Subscribers

1. **Create a new tag:** `RP - 29 Amber Rock St - 2026-02-27`
2. **Import** the agent emails from the MLS export (Subscribers > Import > paste CSV or upload file)
3. **Apply the tag** to the imported subscribers
4. In broadcast settings, **set recipients** to this tag

### D. Configure and Send

1. **Subject line** (paste exactly):
   ```
   Your buyer might be a match | Coming Soon in Henderson | MLS# 2759238
   ```
2. **Sender:** Ryan Rose <ryan@rosehomeslv.com>
3. **Preview the email** and verify:
   - Both images display correctly
   - Layout looks right on desktop and mobile
   - Gold badge shows "Coming Soon"
4. **Send a test email** to ryan@rosehomeslv.com
5. Check the test:
   - First name personalization works
   - ShowingTime button displays (placeholder is OK)
   - Reply and call/text links work
   - Check on phone for mobile layout
6. When everything looks good, **click Send** (or Schedule)

Kit will automatically append the unsubscribe link.

---

## IMPORTANT NOTES

- Agents who saved/favorited the listing should get a direct call or text in addition to this broadcast
- Only export agents with reverse prospecting count under 50
- Do NOT modify the `{{ subscriber.first_name | default: "there" }}` tag in the HTML — that's Kit's personalization
- If anything looks off in the preview, stop and flag it before sending
