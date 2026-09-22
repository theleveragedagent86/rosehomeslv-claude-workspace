# Safety and Caps

These numbers exist to keep `@rosehomeslv` alive. They are hard limits, not targets to push past. When "more reach" and a limit here conflict, the limit wins.

## Daily DM Cap (followers + likers combined)

Ryan set the cap to the **50 to 75 per day** range and accepts the elevated block risk. It is a single combined ceiling, randomized daily:

- At run start, if `daily-budget.json` `date` is not today (or `daily_cap` is missing), choose a fresh `daily_cap` = a random whole number from **50 to 75**, reset `follower_dms_sent_today` and `liker_dms_sent_today` to 0, and set `date` to today. Randomizing the ceiling avoids sending the exact same count every day, which is itself a fingerprint. (Get a random number however is handy, e.g. `echo $((RANDOM % 26 + 50))`.)
- The cap is **shared** across both triggers. DM followers first (oldest-first), then likers, until `follower_dms_sent_today + liker_dms_sent_today` reaches `daily_cap`.
- **No warm-up ramp** (removed at Ryan's request). Be aware: starting at 50+ proactive DMs on a freshly automated account is the highest block risk there is. If Instagram throws any block, stop immediately per the block protocol and do not resume for 24h+.

Liker DMs draw from this same budget. Likers are harvested from recent reels (see the scout), not just flagged ones.

## DM Eligibility Filter (REQUIRED before every DM)

Do not DM a handle unless ALL of these are true:
- Has a profile picture (not the default silhouette).
- Has at least one post.
- Handle is not an obvious bot pattern (long random digits, gibberish, spam-word salad).
- Is not a zero-info private account (no pic, no name, no posts).
- **Is not a real estate agent or broker.** Ryan never DMs competitors. Skip anyone whose profile presents as a Realtor, real estate agent, broker, brokerage, or real estate team. Signals: bio or name containing "Realtor", "REALTOR", "Real Estate Agent", "Broker", "Realty", "Homes by", "Your [city] Realtor", a real estate license number (Nevada agent licenses look like `S.0123456`), or a brokerage affiliation.

**Allowed (these PASS):** regular consumers, AND other businesses or service providers that could be **referral sources**, for example divorce attorneys, landscapers, contractors, photographers, and loan officers / lenders. They are potential partners, not competitors, so DM them. Ryan confirmed `@vegasdivorcepros` and `@signature_classicyards` are fine. Skip the competitors, for example `@jlevylasvegas` and `@frankonrealestate` (both realtors).

Bot/spam accounts are the most likely to **report** Ryan (reports drive bans), so the quality checks are the primary report protection. The filter is never disabled to hit a cap. Falling short because eligible targets ran out is fine.

## Message Variation (REQUIRED)

- Rotate the variants in `dm-templates.md`. Never the same variant twice in a row.
- Always personalize with the first name, or use a no-name variant. Never send a literal "[Name]".
- Identical mass-sends are the top spam fingerprint. This rule matters more than the volume cap.

## Pacing

- **45 to 90 seconds between DMs**, randomized. Do not send on a fixed cadence.
- Longer gap (a couple minutes) when switching from followers to likers.
- The whole DM run should look like a person checking messages, not a script firing.

## Dedupe and Crash-Safety

- **Never DM a handle twice**, across followers and likers, ever. Before DMing anyone, check `state/dmed-users.json`; if their handle is there, skip them. Match handles canonically (lowercase, ignore a leading `@`) so format differences never cause a duplicate. This ledger is what keeps the routine from messaging the same people over and over: once someone gets a follow or like DM, they are off the list for good.
- **Write state incrementally.** The instant a DM is verified sent: append a timestamped object to `dmed-users.json` (`handle`, `trigger`, `dmed_at`, `variant`, `mode`, `display_name`), append a row to `output/dm-history.md` (the readable cumulative log), and increment the counter in `daily-budget.json`. Never wait until the end of the run. A crash mid-run must never re-send to people already messaged.
- **Timestamps:** get them from the system clock with `date "+%Y-%m-%dT%H:%M:%S%z"` (macOS-safe). Every DM record carries when it was sent.
- **Abort on uncertainty.** If you cannot confirm you are in the correct person's thread, or cannot confirm the message sent, skip and log. Never guess your way through a DM.

## Combined Account Load

`@rosehomeslv` also runs the `ig-engage` outbound skill (~17 to 18 comments/day) and this plugin's comment-replies. Instagram counts all automated actions together. Keep the inbound run on a different time of day than `ig-engage`, and treat the rough daily ceiling for the whole account as: outbound comments + inbound replies + DMs all staying within human range. If a day feels heavy, cut the DM cap, not the safety.

## Block Protocol (STOP triggers)

Stop the run immediately, save state, report to Ryan, and wait at least 24 hours if you see any of:
- "Action Blocked" or "Try Again Later"
- A DM fails to send twice
- A "confirm your identity" / challenge / captcha redirect
- An unexpected logout or repeated page reloads

A block is the warning shot before a ban. Respect it. Do not try a "few more" after a block.

## Sanity Defaults

- First several runs: **preview mode** until Ryan approves.
- Liker-DM stays idle until Ryan flags reels.
- When unsure whether something is safe: do less, log it, and tell Ryan.
