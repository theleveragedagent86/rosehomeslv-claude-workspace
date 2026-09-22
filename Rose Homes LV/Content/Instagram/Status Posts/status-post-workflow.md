# Status Post Workflow

Shared steps for the status slash commands (`/just-sold`, `/under-contract`, `/closed`, `/in-escrow`, `/pending`).
The command passes you a **status** and an **address**. Your job: produce a finished 1080×1920 Rose Homes LV status post.

## Status → behavior
| Command | Badge text | Price shown? |
|---|---|---|
| `/just-sold` | JUST SOLD | Yes (final sale price) |
| `/closed` | CLOSED | Yes (final sale price) |
| `/under-contract` | UNDER CONTRACT | No (deal not closed) |
| `/in-escrow` | IN ESCROW | No |
| `/pending` | PENDING | No |

## Steps
1. **Get the photo.** Ask Ryan to drop the property **photo** to use (portrait/vertical reads best for full-bleed). This is the only thing he has to hand you — works the same whether it's his listing or a buyer deal.
2. **Look the home up online.** Web-search the **address** to pull the facts: try `"[address]" Zillow` first, then Redfin or Realtor.com, then a plain Google search. Read the page or the search snippet for **beds / baths / sq ft** and the **neighborhood · ZIP**. For JUST SOLD / CLOSED, also look for the most recent **sale price**.
   - If the address has no city, assume the Las Vegas Valley.
   - **Never fabricate a number.** Note the source you pulled from. If a figure isn't found (Zillow may block the fetch, and a brand-new sale price is often not public yet), ask Ryan for just that one piece, or mark it `NOT FOUND` — don't guess.
3. **Confirm in one line.** Show Ryan what you'll put on the graphic and where it came from, e.g. "4 bd · 3.5 ba · 3,840 sqft · Summerlin 89134 (Zillow) — sale price?" so he can correct anything before it's baked in.
4. **Pick the template.** Default to Direction A → `Instagram/Status Posts/status-post-fullbleed.html`. If Ryan says "editorial" or "light", use `status-post-editorial.html`.
5. **Build it.** Copy the template to `Instagram/Status Posts/posts/<status-slug>-<address-slug>.html` and copy Ryan's photo in next to it. Fill the `<!-- << SWAP >> -->` fields: badge = status text, address, neighborhood·zip, beds/baths/sqft. For JUST SOLD / CLOSED set the price; for the in-progress statuses add `is-pending` to the `<div class="post">` tag and delete the `.price` block. Point the photo `<img src>` at the copied photo.
6. **Verify.** Start the `seller-report` preview, set the viewport to 1080×1920, screenshot, and confirm the badge text, numbers, photo, and safe zones look right. Fix and re-shoot if needed.
7. **Deliver.** Show the screenshot, give the file path, and either export the 1080×1920 PNG or remind Ryan how (DevTools device size 1080×1920 → Capture screenshot). He adds music in the IG editor.

## Rules
- No em-dashes. Factual only — never fabricate price, sqft, or bed/bath counts; mark gaps `NOT FOUND`.
- Keep "Real Broker, LLC" in the footer lockup.
