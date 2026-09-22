# Rose Homes LV — Property Status Post (Instagram)

A reusable system for "Just Sold / Closed / Under Contract / In Escrow / Pending" posts.
Vertical **1080 × 1920** (9:16, reel size) so it sits on your main grid and plays like a reel once you add music.

There are **two ways** to use this:

1. **Fastest — use the ready-made templates** already in this folder:
   - [status-post-fullbleed.html](status-post-fullbleed.html) — Direction A (photo fills the frame, navy + gold)
   - [status-post-editorial.html](status-post-editorial.html) — Direction B (warm off-white, photo on top)
   Open one in your browser, swap the photo + words + numbers, and export a PNG (see **How to export** at the bottom). Same layout every time.

2. **To spin up fresh options — paste the prompt below into Claude Design.** It is self-contained; you don't need to paste the brand guide too.

---

## THE PROMPT (paste into Claude Design)

> Build me a reusable **Instagram property-status post** as a single self-contained HTML file (inline CSS, no build step), sized **exactly 1080 × 1920 px** (9:16 vertical, Instagram reel size). Generate **two distinct on-brand directions** so I can compare:
> - **Direction A — Full-bleed:** the property photo fills the whole frame, with a deep-navy gradient fading up from the bottom; the copy sits over the dark base.
> - **Direction B — Light editorial:** the property photo fills the top ~58%, with the details on a warm off-white panel below.
>
> **Brand — Rose Homes LV** (Las Vegas real estate; agent Ryan Rose, brokered by Real Broker, LLC). Sophisticated, modern, editorial. Luxury but understated — let type and photography carry it.
>
> **Colors (use these exact hex):** deep navy `#1C2333`, champagne gold `#C9A86E` (accent only — thin rules, corner brackets, the badge, the price; never a large fill), white `#FFFFFF`, warm off-white `#F7F5F0`, slate `#8A8FA8` (muted labels).
>
> **Fonts (Google Fonts):** **Playfair Display** Bold for the address, the price, and the stat numbers; **Montserrat** SemiBold, UPPERCASE, wide letter-spacing (~0.2em) for the status badge, the eyebrow, and labels; **Inter** for any body text.
>
> **Signature details:** thin (1–1.5px) gold **L-shaped corner brackets** framing the canvas; a short 1px gold rule under the address; corner radius 0–8px max; generous whitespace.
>
> **Content + reading order:**
> - **Status badge** (swappable text): `JUST SOLD` / `CLOSED` / `UNDER CONTRACT` / `IN ESCROW` / `PENDING`. Make it **large and pronounced** (~55–60px, bold, uppercase) — it's a hero element, second only to the address. It must stay legible over **any** photo — for Direction A use a solid navy chip with a gold border and gold text; for Direction B use a solid gold chip with navy text.
> - **Address** in large Playfair (example: 2412 Quail Ridge Court), ~80–86px, confident.
> - **Eyebrow:** NEIGHBORHOOD · ZIP (example: SUMMERLIN · 89134).
> - **Stats row:** Beds / Baths / Sq Ft (Playfair numbers + small Montserrat labels).
> - **Final sale price** in gold (example: $1,495,000) — shown on SOLD / CLOSED only.
> - **Footer brand lockup:** a small Rose Homes LV mark on the left, and "RYAN ROSE · REAL BROKER, LLC" on the right.
>
> **Two content states (make it easy to toggle):**
> - **SOLD / CLOSED:** show the final sale price.
> - **UNDER CONTRACT / IN ESCROW / PENDING:** hide the price (the deal hasn't closed) — just badge + address + eyebrow + stats.
>
> **Instagram safe zones (important):**
> - Keep all key content (badge, address, price, footer) inside the **centered 1080 × 1350 (4:5)** area — Instagram crops the grid thumbnail to that, so anything in the far top or far bottom gets cut on the grid.
> - Keep critical content out of the **bottom ~420px** and **right ~140px** — that's where Instagram's reel caption, handle, and action buttons sit. Put the footer lockup around 80% of the height, just above the caption zone.
>
> Use placeholder content I can swap: a `https://placehold.co/1080x1920` photo and the sample address / stats / price above. **Mark every swappable field with an HTML comment.** Output the full HTML, then render both directions so I can see them.

---

## PER-POST FILL-IN (swap these each time)

Whether you edit the HTML or use Claude Design, these are the only things that change:

- **Status badge:** `________` (JUST SOLD / CLOSED / UNDER CONTRACT / IN ESCROW / PENDING)
- **Property photo:** `________` (a strong vertical/portrait listing photo works best for full-bleed)
- **Address:** `________`
- **Neighborhood · ZIP:** `________`
- **Beds / Baths / Sq Ft:** `__ / __ / ______`
- **Final sale price:** `$________` (SOLD / CLOSED only — leave out for in-progress)
- **Optional line:** "Represented the Buyer" or "Represented the Seller"

**To regenerate in Claude Design:** paste *"Using my locked template, regenerate with this data: [paste the fields above]. Keep the layout identical, only swap the photo and text."*

**To edit the HTML directly:** open the file, find each `<!-- << SWAP >> -->` comment, change the text. For an in-progress post, add the word `is-pending` to the `<div class="post">` tag (this hides the price) and change the badge text.

---

## BRAND ASSETS + RULES

**Logo files on disk** (upload to Claude Design if it accepts image references, or keep the built-in text lockup):
- `SKOOL Community/hyperframes-student-kit/Rose Homes Brandkit/Rose Homes LV Design System (Template)/assets/` → `logo-horizontal.svg`, `logo-stacked.svg`, `monogram.svg`, `rose-mark.svg`
- Real Broker marks: same path, `assets/brokerage/` → `real-broker-knockout.png` (for dark), `real-broker-outline.png` (for light)

**Always:**
- **No em-dashes.** Commas, periods, or "and".
- **Factual only.** Never invent a price, square footage, bed/bath count, or sale figure. If you don't have a number, mark it `NOT FOUND` so it's obvious to fill in — don't guess.
- Keep **"Real Broker, LLC"** in the lockup (brokerage compliance).
- Don't put the street address on a paid **ad** — fine for an organic grid post about a closed/pending deal.

---

## CAPTION TEMPLATE (for the Instagram post itself)

**Sold / Closed:**
> Just sold in [Neighborhood]. 🔑
> [Address] — [beds] bed, [baths] bath, [sqft] sq ft.
> [One warm line, e.g. "Another Summerlin family off to their next chapter."]
> If you're even thinking about selling in [area], I'm happy to walk you through what your home could do right now. No pressure.
>
> Ryan Rose | Rose Homes LV | Real Broker, LLC | 702-747-5921 | rosehomeslv.com

**Under Contract / In Escrow / Pending:**
> Under contract in [Neighborhood]. 🤝
> [A short line on speed or interest, e.g. "Strong activity on this one."]
> Buyers are still looking in [area]. If you've thought about listing, let's talk.
>
> Ryan Rose | Rose Homes LV | Real Broker, LLC | 702-747-5921 | rosehomeslv.com

*(Keep it warm, short sentences, no em-dashes, soft CTA.)*

---

## HOW TO EXPORT A PNG FROM THE HTML

1. Open the `.html` file in Chrome.
2. Open DevTools (Cmd+Option+I) → click the device-toolbar icon (Cmd+Shift+M) → set a custom size of **1080 × 1920**.
3. In the DevTools "..." menu choose **Capture screenshot** (or **Capture full size screenshot**). You get a clean 1080×1920 PNG.
4. Post it to Instagram and add your music in the IG editor so it plays like a reel.

*(Or just paste the prompt above into Claude Design and download the image it renders.)*
