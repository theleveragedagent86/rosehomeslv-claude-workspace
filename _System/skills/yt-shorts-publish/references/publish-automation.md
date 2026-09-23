# YouTube Studio automation (Shorts, Rose Homes LV channel)

Runs after Ryan has uploaded the Shorts MP4s as **drafts**. The skill never uploads video: `file_upload` has a 10 MB cap and only works from session-shared folders. Filename = join key.

## Tooling

Use **claude-in-chrome** for every click and keystroke. computer-use grants browsers only read tier. Load the core tools in ONE ToolSearch call:

`select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__read_page,mcp__claude-in-chrome__find,mcp__claude-in-chrome__form_input`

If Chrome is not connected, stop, tell Ryan to open Chrome with the Claude extension, and leave `schedule.md` with every row `pending` so a rerun resumes.

## Finding the drafts

1. Navigate to `https://studio.youtube.com` > Content > **Shorts** tab. Confirm the channel is **Rose Homes LV / Ryan Rose**, not Codename History. If the wrong channel is active, stop and ask Ryan to switch.
2. Filter or search by the filename. Drafts show the uploaded filename as the working title.
3. Match against `schedule.md` rows. Row not found = status `no-draft`, keep going.

## Inventory first

Read the whole Shorts list (get_page_text) before assigning any slot. Note which batch titles are already Public, already Scheduled (open Details > Visibility to read the exact time), Draft, or missing. Only Draft rows get new slots.

Drafts uploaded through Ryan's upload template carry a placeholder description ("First Paragraph Here ... Description Here") and a generic 460-char tag set. Replace the description only. Leave the tags exactly as uploaded.

## Per-draft steps (in this order)

1. **Open Details** (pencil icon on the row).
2. **Title.** Click the title field. Before `cmd+a`, confirm the char counter (e.g. `14/100`) is visible under the field. Then `cmd+a`, type the title. `find` the field and read the value back.
3. **Description.** Same focus check, then paste the full description. Read it back; confirm the hashtags line is present.
4. **Tags.** Leave alone. The upload template already filled them and Ryan wants them unchanged.
5. **Audience.** Click **"No, it's not made for kids."**
6. **AI / altered content.** Click **No** unless `schedule.md` says `AI disclosure: Yes`. Required, never skip.
6b. **Related video.** In the right-hand panel, click Related video > search the long-form title from `schedule.md` ("Las Vegas News <date> | ...") > select it. Confirm the title shows in the panel.
7. **Visibility.** Click **Next** through Video elements / Checks (or the Visibility tab). Choose **Schedule**. Set the date and time from the row. Do NOT open or change the Time zone control. Leave it alone (Ryan, 2026-09-01). Click **Schedule**.
8. **Verify.** The Content list should show the row as **Scheduled** with the date. Take a screenshot or `read_page` and copy the video link (share icon or the row's link).
9. **Write back** to `schedule.md`: status `scheduled`, link. Save the file now, not at the end.

## Careful-interaction checklist

- Never type until a field-scoped focus is confirmed. A page-wide `cmd+a` closed the dialog and wiped edits once.
- If a dialog closes unexpectedly, reopen Details and re-check every field before continuing.
- Do all metadata first, visibility last.
- One Short at a time. Do not open several Details dialogs.
- Never click Public. Scheduled only, unless Ryan typed the word Public for that Short.
- If a step fails twice, mark the row `failed` with a one-line reason and move to the next.

## Draft-dialog specifics (learned 2026-09-01)

- Drafts open in the 4-step upload dialog (Details > Video elements > Initial check > Visibility), not the Details page. Use `find` for the title/description textboxes and the two "No" radios, then `Next` (bottom right) to reach Video elements > Related video > Add > pick the long-form tile.
- Visibility step defaults to **Public** with a **Publish** button. Never click it. Click the Schedule section's "Click to expand" button; the bottom button then reads **Schedule**.
- Date defaults to tomorrow. Set the time by clicking the time textbox, `cmd+a`, type e.g. `6:00 PM`, press Return, then go **straight to the Schedule button**. Clicking anywhere else in the panel collapses Schedule and flips the dialog back to Publish mode.
- The scheduled video's id is the `udvid=` value in the dialog URL, so the link is `https://youtube.com/shorts/<udvid>`.
