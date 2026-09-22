# Inbound Scout — Browser Playbook

**Read this entire file before harvesting. These are the UI flows and the filter logic.**

All harvesting is on `@rosehomeslv`'s own surfaces. You are logged in as Ryan. Prefer `browser_snapshot` (accessibility tree) over screenshots, it is faster and gives you handles and text directly. Use `browser_screenshot` only as a fallback when the snapshot is ambiguous.

## Key Playwright MCP Tools

- `browser_navigate` — go to a URL
- `browser_snapshot` — read the page via accessibility tree (primary tool)
- `browser_click` — click an element
- `browser_screenshot` — visual fallback only
- `browser_tab_*` — manage tabs if needed

## Reading Comments on Ryan's Reels

1. Navigate to `https://www.instagram.com/rosehomeslv/reels/`.
2. The reels appear as a grid, newest first. Click the first reel to open it.
3. Snapshot the open reel. The caption and the comment list are in the side panel (desktop) or below (mobile layout). Capture: the reel URL (from the address bar), a short caption snippet, and each comment as `commenter_handle + comment_text`.
4. Some reels have a "View all N comments" or "Load more comments" control. Click it once or twice to load the visible set. Do NOT exhaustively load hundreds of comments, the most recent and the top ones are what matter.
5. Close the reel (or navigate back to the reels URL) and open the next one.
6. Stop after ~8 reels, or once you reach reels with no new (unfingerprinted) comments.

**Fingerprinting:** for each comment, build `reel_url + "|" + handle + "|" + a stable hash of the comment text` (normalize whitespace and lowercase before hashing). This is how you and the reply skill avoid double-replies. If the fingerprint is already in `replied-comments.json`, skip it silently.

**Comment screening:** apply the `ig-engage` guardrails. Mark as unsafe (do not reply later) any comment that is political, LGBTQ+, religious, hostile, or otherwise charged. Also skip comments Ryan himself posted (his own handle), pure emoji reactions with nothing to respond to, and obvious spam.

## Reading the Followers List (newest first)

1. Navigate to `https://www.instagram.com/rosehomeslv/`.
2. Click the "followers" count to open the followers dialog.
3. Instagram orders this list **most-recent-first** at the top. The topmost handle is the newest follower.
4. Snapshot the dialog. Collect handles top-down. Scroll the dialog to load more only as needed.
5. **Stop walking** as soon as you hit: the `last_follower_watermark` from `last-run.json`, OR a handle already in `dmed-users.json`, OR ~50 collected. Everything above the stop point is new since last run.
6. Record the **topmost** handle as `topmost_follower_seen` for the new watermark.

## Reading Reel Likers (recent reels by default)

1. Decide the reels: the URLs in `target-reels.md` if any are listed, otherwise his ~6 most recent reels.
2. For each reel, navigate to it and click the likes count / "liked by" to open the likers dialog.
3. Snapshot and collect handles. Drop any already in `dmed-users.json`, and apply the eligibility filter (skip realtors/brokers; other businesses are fine).
4. Optionally also open the web notifications panel (heart / activity icon, or `/notifications/`) and add any "liked your reel" entries it shows. Web coverage is thin, so treat this as a bonus on top of the per-reel lists.
5. Cap at ~60 liker candidates total for the work-list. The DMer applies the real daily cap.

## The Real-Follower Filter (REQUIRED before any handle becomes a DM target)

A handle **passes** only if ALL of these are true. If any fails, set `passes_filter: false` with a short `filter_reason` and do not DM them.

- **Has a profile picture** (not the default grey silhouette).
- **Has at least one post** (profile is not completely empty).
- **Handle is not an obvious bot pattern:** reject long random digit strings (e.g. `user82910473`), keyboard gibberish, or names that are clearly spam (sequences of unrelated words plus numbers, adult-spam handles).
- **Not a zero-info private account:** a private account with no pic, no name, and no posts is a skip. A private account that otherwise looks real (pic + name) is fine.
- **Not a real estate agent or broker:** Ryan does not DM competitors. Set `passes_filter: false` (reason: "realtor/competitor") for anyone whose name or bio presents as a Realtor, real estate agent, broker, brokerage, or real estate team. Signals: "Realtor", "REALTOR", "Real Estate", "Broker", "Realty", "Homes by", a license like `S.0123456`, or a brokerage name.

**Allowed on purpose:** regular people AND non-competing businesses or service providers that could be referral sources (divorce attorneys, landscapers, contractors, photographers, loan officers / lenders) all PASS, they are partners, not competitors. So `@vegasdivorcepros` and `@signature_classicyards` pass; `@jlevylasvegas` and `@frankonrealestate` (realtors) do not.

To check cheaply: the followers/likers dialog usually shows the avatar and display name inline, that alone filters most bots (no avatar = skip). When a handle is borderline, open the profile, snapshot it, and judge by pic + post count + bio. Spend this effort only on borderline cases, not every handle.

**Why this matters:** fake/spam accounts that follow every realtor are the ones most likely to report Ryan. Reports drive bans. Filtering them out protects the account, this is the point of the filter, not just audience quality.

## First-Name Extraction (for `[Name]` in DMs)

Capture each target's **display name** (the real-name line, not the @handle). The DMer will take the first token as the first name. If the display name is missing, is a business name, is all emoji, or is clearly not a personal first name, the DMer uses a no-name variant. Capture what you see and let the DMer decide.

## Pacing and Block Protocol

- 3 to 8 seconds between reels and between list scrolls.
- This is read-only, but Instagram still rate-limits aggressive scrolling. If you see "Try Again Later", a challenge page, or an unexpected logout, STOP, save what you have, and report. Do not continue.
