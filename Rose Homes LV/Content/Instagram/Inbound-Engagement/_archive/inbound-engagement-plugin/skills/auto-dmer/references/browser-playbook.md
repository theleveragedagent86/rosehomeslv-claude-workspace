# Auto-DMer — Browser Playbook

**Read fully before sending. The DM compose flow is where a wrong move sends the wrong person a message. Fail safe.**

You are logged in as `@rosehomeslv`. Use `browser_snapshot` (accessibility tree) as the primary tool. Use `browser_screenshot` only when the snapshot is ambiguous.

## Two Ways To Open A DM Thread (prefer the profile route)

### Route A: From the person's profile (preferred, least error-prone)
1. Navigate to `https://www.instagram.com/<handle>/`.
2. Snapshot. **Confirm the handle on the page matches the target handle exactly.** This is your correctness check, you are provably on the right person.
3. Click the "Message" button on their profile.
4. This opens the DM thread with that exact person.

### Route B: From the DM inbox (use only if Route A fails)
1. Navigate to `https://www.instagram.com/direct/inbox/`.
2. Click the new-message / pencil icon.
3. Type the exact handle in the search box.
4. **Verify the selected result's handle matches exactly** before choosing it. Handles can be similar, do not pick a lookalike.
5. Select the person and open the chat.

## Send The Message

1. Confirm the open thread header shows the **correct handle**. If it does not, or you are unsure, **abort this target**, log it, move on. Never send into an unverified thread.
2. Click the message input ("Message..." placeholder).
3. Type the personalized, variant-selected message.
4. Send (click the send control, or Enter where that submits).
5. Wait 2 to 3 seconds, snapshot, and **verify your message bubble appears in the thread** with the text you sent.
6. Only after that verification: write the handle to `dmed-users.json` and increment `daily-budget.json`. Incremental, every time.

## Abort-On-Uncertainty (the most important rule here)

Skip the target and log it (do NOT retry blindly) if any of these are true:
- The profile handle or thread header does not exactly match the intended target.
- You cannot find a clear Message button or message input.
- After sending you cannot confirm the message bubble appeared.
- Anything about the page looks off (challenge, redirect, logged out).

A missed DM costs nothing. A DM to the wrong person, or a double-send, damages trust and can draw a report. When in doubt, skip.

## Things That Make You Stop The Whole Run

Per `safety-and-caps.md` and `CLAUDE.md`: "Action Blocked", "Try Again Later", a send failing twice, a verify/challenge redirect, or an unexpected logout. Stop, save state, report, wait 24h+.

## Notes On Instagram's DM UI

- **Message requests:** a DM to someone who follows Ryan usually lands in their primary inbox. Some still route to "requests" and may go unseen. That is expected, not an error.
- **Already-existing thread:** if a thread with this person already exists, the handle should already be in `dmed-users.json` and you should have skipped them. If you somehow open an existing thread with prior messages from Ryan, **do not send again**, log it as already-contacted and move on.
- **Reply detected:** if the open thread shows the person already replied to a past message, flag it in the daily log as a live lead for Ryan and do not auto-reply.
- **Pacing:** 45 to 90 seconds between sends. The DM inbox is watched closely by Instagram's anti-spam, slow is safe.
