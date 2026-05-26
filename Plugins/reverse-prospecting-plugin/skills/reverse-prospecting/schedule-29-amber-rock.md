# Reverse Prospecting Schedule — 29 Amber Rock St

Paste this prompt into Cowork's scheduler. Set it to run **once** (on-demand), or schedule it for the date you want the email blast to go out.

---

## Schedule Settings

- **Frequency:** On-demand (run once when ready)
- **Trigger:** When the listing goes Coming Soon or Active in MLS

---

## Prompt to Paste

```
Run the full reverse prospecting campaign for 29 Amber Rock St. The email is already generated. Your job is to extract agents from MLS, set up Kit, and send the broadcast. Here are all the details:

PROPERTY DETAILS:
- Address: 29 Amber Rock St, Henderson, NV 89012
- Price: $485,000
- MLS#: 2759238
- Active Date: March 11, 2026
- Badge: Coming Soon
- Subdivision: Champion Village
- Subject Line: Your buyer might be a match | Ref #{{ subscriber.ref_number }} | Coming Soon in Henderson
- Sender: Ryan Rose <ryan@rosehomeslv.com>

EXISTING EMAIL FILE:
/Users/ryanrose/Downloads/Claude/Listings/29 Amber Rock St/29_Amber_Rock_Agent_Reverse_Prospecting_Email.html

PHOTOS TO UPLOAD TO KIT:
- Hero: /Users/ryanrose/Downloads/Claude/Listings/29 Amber Rock St/Listing Photos/29_amber_rock_st-8934_web_v24/dji_20260223130017_0005_d_twilight_2f4cf81d-fd19-448e-8bdf-7d1f6b1b85dc.jpg
- Interior: /Users/ryanrose/Downloads/Claude/Listings/29 Amber Rock St/Listing Photos/29_amber_rock_st-8934_web_v24/dsc05510.jpg

STEP 1 — EXTRACT AGENTS FROM MLS
Open Chrome and navigate to https://las.mlsmatrix.com. If you need to log in, pause and let me handle it. Search for MLS# 2759238 (or go to My Matrix > My Listings). Open the listing detail page and click the "Reverse Prospecting" tab. Review results:
- ONLY select agents where the "Count" column is UNDER 50. Counts of 50+ mean the buyer's search is too broad.
- Capture the "Ref #" column for each agent (this gets imported into Kit for subject line personalization).
- Note any agents who SAVED or FAVORITED the listing separately for priority follow-up.
- Export the filtered agent list (email + Ref # columns) as CSV/Excel. If no export button, copy manually.
- Report: how many agents exported, how many saved/favorited.

STEP 2 — UPLOAD IMAGES TO KIT
Navigate to https://app.kit.com. If you need to log in, pause and let me handle it. Go to the Image Library. Upload both photos listed above. Copy the hosted URL that Kit gives you for each image.

STEP 3 — CREATE THE KIT BROADCAST
1. Go to Broadcasts > New Broadcast
2. Add a Custom HTML content block
3. Open the email file at the path above. Copy everything inside the <body> tag and paste it into the Custom HTML block.
4. Replace image placeholders:
   - Find "[KIT IMAGE URL: dji_20260223130017_0005_d_twilight.jpg]" and replace with the Kit hosted URL for the hero image
   - Find "[KIT IMAGE URL: dsc05510.jpg]" and replace with the Kit hosted URL for the interior image
5. Create a tag: "RP - 29 Amber Rock St - [today's date YYYY-MM-DD]"
6. Import the MLS export as subscribers. Apply the tag. CRITICAL: Map the "Ref #" column to a custom field called "ref_number" during import.
7. Set recipients to the new tag
8. Set subject line: Your buyer might be a match | Ref #{{ subscriber.ref_number }} | Coming Soon in Henderson
9. Set sender: Ryan Rose <ryan@rosehomeslv.com>
10. Preview the email. Verify: both images display, layout works on desktop/mobile, gold badge says "Coming Soon", {{ subscriber.first_name }} tag is intact
11. Send a test to ryan@rosehomeslv.com

STEP 4 — PAUSE BEFORE SENDING
After sending the test, tell me: "Test email sent. Check your inbox and phone. Ready to send to all agents?" Do NOT send to all agents until I confirm.

After I confirm and the broadcast sends, remind me which agents saved/favorited the listing so I can call or text them directly as priority follow-up.
```
