# beehiiv reference for The Rose Report

Publication: `pub_2d01a48c-d852-446f-a2ef-90428ddc6545` (rosehomeslv.beehiiv.com).
Subscribe link: https://rosehomeslv.beehiiv.com/subscribe
API key: macOS Keychain only, `security find-generic-password -a ryan -s beehiiv-api-key -w`.
Never print it, write it to a file, or put it in memory.

## Plan limits (checked 2026-09-24)

- Create Post and Update Post in the API are **Max and Enterprise only**. Ryan started a 14-day Max
  trial on 2026-09-23. After it ends he is on the free plan unless he upgrades.
- Listing and reading posts work on any plan.
- If `scripts/beehiiv.py create` or `update` returns 403 or 404, use the browser flow below.

## Posts, web versions, editing after send

- Posts default to `platform: "both"`, so each issue gets a web page at
  `https://rosehomeslv.beehiiv.com/p/<slug>`. That URL is what the catch-up line links to.
- After a post sends, its **web version can still be edited** (content, title, thumbnail).
  The email already delivered never changes. So never send a second "updated" email.

## What beehiiv does to our HTML (HTML snippet block)

- Strips `<style>` blocks (media queries, dark mode), Google Fonts `<link>`, HTML comments, and
  every `sms:` link. Keeps inline styles, `mailto:`, `https:` links.
- Adds its own 40px side padding and its own footer (unsubscribe + address). Remove our footer.
- A `<style>` block that slips through leaks into beehiiv's editor UI. Never include one.
- Snippet block cap: 50,000 characters.

So `beehiiv-snippet.html` must be:
1. Body only, starting at the outer container table. No `<html>`, `<head>`, `<style>`, `<link>`.
2. Container `align="center" width="100%" style="width:100%;max-width:680px;margin:0 auto;..."`
   (fluid, or phones side-scroll; centered + 680px or it sits left-aligned on the web post, Ryan 2026-10-01).
3. Horizontal padding on content cells 16px (not 40, beehiiv already adds 40).
4. Stat block sized to fit 375px phones: big number 60px, small stats 26px, black box padding
   `30px 12px 10px 12px`, stat-cell padding `14px 4px 4px 4px`.
5. `#lead_first_name#` (Lofty tag) replaced with "there". beehiiv's merge tag is NOT FOUND yet.
6. The Text-me button goes to `https://theleveragedagent86.github.io/rhlv-site-images/text-ryan/`
   (GitHub Pages page that opens Messages on phones), never an `sms:` link.
7. Keep the `<!-- Pxx Syy: ... -->` reel markers in the LOCAL file. beehiiv strips them, so the
   local snippet is the source of truth for reel swaps.

## Browser flow (free plan, or whenever the API refuses)

Use Claude in Chrome. beehiiv editor is ProseMirror.

**New draft:**
1. app.beehiiv.com > Start writing. Title field has real text "New post": click it, cmd+a, type title.
2. Focus the body with JS (collapse the selection into the empty `p` inside `.ProseMirror`).
3. Type `/html`, press Return, then immediately cmd+v. Fill the clipboard first with
   `pbcopy < beehiiv-snippet.html`.
4. Verify with JS: `.ProseMirror` children should be `node-htmlSnippet | DIV`.

**Replacing the snippet in an existing post (incl. a sent post's web version):**
Do NOT cmd+a / cmd+v into the existing snippet. It appends and hits the 50k cap, or replaces the
whole doc. Instead: delete the snippet block with the trash icon in the snippet toolbar, then do
steps 2 to 4 above. If something goes wrong, cmd+z right away.

**Check the mobile preview:** open Preview, switch to mobile, find the iframe whose body contains
"ROSE REPORT", and compare `scrollWidth` to `clientWidth` (must be equal). Return booleans or
numbers only from JS; results containing URLs get blocked.

## Things that need Ryan

- Sending a test email, scheduling, or sending the issue: ask first, every time.
- Deleting drafts or posts: never. Tell Ryan which one to delete (verify ids with `beehiiv.py list`).
- Plan upgrades or billing: Ryan only.
