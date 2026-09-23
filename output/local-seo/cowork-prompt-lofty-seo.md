# Cowork Prompt — Lofty Site Editor SEO Pass

Paste everything below the line into Cowork with the Lofty site editor open and logged in.

---

You are working in my **Lofty (Chime) website back office** for rosehomeslv.com in the browser. I am logged in already. Your job is a mechanical SEO pass: update page SEO titles and meta descriptions, and install two JSON-LD schema blocks. You are NOT writing new pages.

**Ground rules**
- Do NOT click Publish / Save-and-publish on anything until you show me what changed and I say go. Draft/save-as-draft is fine if Lofty offers it.
- If a field, menu, or setting is not where you expect, take a screenshot, tell me what you see, and ask. Do not guess your way through a menu.
- Never invent data. If a value is missing, leave it and flag it.
- No em dashes anywhere in anything you type. Use commas or periods.
- Work one page at a time. After each page, screenshot the saved field so I can verify.
- Do not touch listings, leads, CRM, smart plans, or billing. Website settings only.

**Reference file (read it first):** `/Users/ryanrose/Downloads/Claude/output/local-seo/rosehomeslv.com-fast-wins.md`

---

## TASK 1 — SEO titles (highest priority)

Every page title is currently 70 characters and truncating in Google. Find the site editor's per-page SEO settings (usually Website → Pages → the page → SEO / Page Settings, with Meta Title and Meta Description fields). Replace the Meta Title on each page below with the exact string in the right column. Do not add or remove anything.

| Page | New Meta Title |
|---|---|
| Home | Las Vegas Homes for Sale \| Ryan Rose, Realtor |
| All Listings | Las Vegas Homes & Condos for Sale \| Ryan Rose |
| Featured Listings | Featured Las Vegas Listings \| Ryan Rose |
| Sold Listings | Recently Sold Las Vegas Homes \| Ryan Rose |
| Sell / Sell My Home | Sell Your Las Vegas Home \| Ryan Rose, Realtor |
| Home Valuation | What's My Las Vegas Home Worth? \| Ryan Rose |
| About Me | About Ryan Rose \| Las Vegas Realtor |
| Contact | Contact Ryan Rose \| Las Vegas Realtor |
| Affordability Calculator | Home Affordability Calculator \| Ryan Rose LV |
| Mortgage Calculator | Las Vegas Mortgage Calculator \| Ryan Rose |
| Blog index | Las Vegas Real Estate Blog \| Ryan Rose |
| Southern Highlands | Southern Highlands Homes for Sale \| Ryan Rose |
| Macdonald Highlands | MacDonald Highlands Homes for Sale \| Ryan Rose |
| Summerlin | Summerlin Homes for Sale \| Ryan Rose, Realtor |
| Henderson | Henderson NV Homes for Sale \| Ryan Rose |

If a page in this list does not exist under that exact name, tell me the closest match before editing it. If the site has pages NOT in this list, list them for me at the end with a suggested title under 60 characters, but do not edit them yet.

---

## TASK 2 — Homepage meta description

Replace the homepage Meta Description with exactly this (it removes an em dash that violates my brand rules):

> Explore Las Vegas homes for sale, including luxury and new listings. Buy or sell with Ryan Rose at Rose Homes LV, your trusted local real estate expert.

---

## TASK 3 — Remove the duplicate Organization schema

The homepage source currently outputs the `Organization` JSON-LD block twice. Check whether one of them is coming from a custom code / header injection field I control (Site Settings → Advanced → Custom Code, or similar). If yes, delete my duplicate and keep Lofty's. If both are Lofty-generated and I cannot edit them, say so and move on. Do not fight the platform.

---

## TASK 4 — Install RealEstateAgent schema

Find the site-wide custom code / header injection field. Paste the `RealEstateAgent` JSON-LD block from the reference file. The address (9580 W Sahara Ave Ste 200, Las Vegas, NV 89117) and rating (5.0 from 5 reviews) are already filled in and verified against my Google Business Profile. Do not change those values.

One edit needed first: replace `{{HEADSHOT_OR_LOGO.jpg}}` with the real URL of my headshot or logo image on the site. Find it in the page source or the media library. Do not guess a filename.

Show me the final block before you paste it.

---

## TASK 5 — Homepage FAQ section + FAQPage schema

Two parts, in this order. Google requires the FAQ text to be visible on the page, not schema-only.

**5a.** Add a new content/text section near the bottom of the homepage (above the footer) titled **Frequently Asked Questions**, containing the five Q&As from the "Visible FAQ copy" section of the reference file. Use the homepage editor's standard text or accordion module. Match existing homepage fonts and spacing. If the editor has no section that can hold this cleanly, stop and show me the available module types instead of forcing it.

**5b.** Once the visible FAQ is live, paste the `FAQPage` JSON-LD block into the homepage's page-level custom code if Lofty has a per-page field. If it only has a site-wide field, put it there and tell me, since it only stays valid while the FAQ is on the homepage.

---

## TASK 6 — Report back

When done, give me:
1. A table of every field you changed: page, field, old value, new value.
2. Anything you could not do and why.
3. The exact location (menu path) of the custom code field, so I have it for next time.
4. Whether Lofty exposes a per-page custom code field or only site-wide.

Then run each schema block through Google's Rich Results Test (https://search.google.com/test/rich-results) using the live URL after I publish, and report pass/fail.

---

## What is explicitly OUT of scope for you

Do not attempt these. They are on my list, not yours.
- Creating the New Construction, Luxury, or Relocation pages
- The Ryan Rose bio page
- New area/community pages
- The triple-H1 theme bug (needs Lofty support or a theme edit)
