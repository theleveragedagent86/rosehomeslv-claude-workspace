# Weekly Seller Email Template

Use this exact structure every week for all listings. Do not change the layout, section order, dividers, or sign-off.

---

## Format (HTML, text/html)

```html
<div style="font-family: Arial, sans-serif; font-size: 14px; color: #333; line-height: 1.6;">

<p>Hi [SELLER_FIRST_NAME],</p>

<p>[EXECUTIVE_SUMMARY — 2 to 4 sentences. High-level story only. No platform breakdowns or granular stats.]</p>

<p>Here's your full report with all the details:<br>
<a href="[REPORT_URL]">View Your Weekly Report</a></p>

<hr style="border: none; border-top: 1px solid #ccc; margin: 16px 0;">

<p><strong>Nearby Listings/Solds to Keep an Eye On:</strong></p>

<ul>
  <li>🏠 <a href="[ZILLOW_URL]">[STREET_ADDRESS]</a></li>
  <li>🏠 <a href="[ZILLOW_URL]">[STREET_ADDRESS]</a></li>
  <li>🏠 <a href="[ZILLOW_URL]">[STREET_ADDRESS]</a></li>
  <li>🏠 <a href="[ZILLOW_URL]">[STREET_ADDRESS]</a></li>
  <li>🏠 <a href="[ZILLOW_URL]">[STREET_ADDRESS]</a></li>
</ul>

<hr style="border: none; border-top: 1px solid #ccc; margin: 16px 0;">

<p>Let me know if you have any questions. I'll keep you posted as things progress.</p>

<p>Best,<br>
Ryan Rose</p>

</div>
```

---

## Rules

1. Greeting: "Hi [First Name]," — first name from platform-links.json → seller.firstName
2. Executive summary: 2-4 sentences, same story as the report. No platform-by-platform breakdown.
3. Report link: "Here's your full report with all the details:" on one line, "View Your Weekly Report" as hyperlink on the next line.
4. HR divider (1px solid #ccc) before and after the competition section.
5. Competition header: exact wording "Nearby Listings/Solds to Keep an Eye On:" in bold.
6. Each competition link: 🏠 emoji + hyperlinked street address (no city/state, just the street).
7. Closing line: exact wording "Let me know if you have any questions. I'll keep you posted as things progress."
8. Sign-off: "Best," then "Ryan Rose" — no title, no phone number, no extra branding.
9. No em dashes anywhere.
