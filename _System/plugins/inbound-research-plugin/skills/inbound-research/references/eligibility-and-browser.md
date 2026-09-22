# Eligibility Filter and Harvest Mechanics

## Browser (Cowork / Claude in Chrome)

Drive Ryan's real Chrome, logged in as `@rosehomeslv`. Read pages with the browser's read/snapshot tool, click and scroll as needed. This uses the same real session a human would, which is the point.

- Profiles: `https://www.instagram.com/<handle>/`
- Reels grid: `https://www.instagram.com/rosehomeslv/reels/`
- Followers dialog: open `https://www.instagram.com/rosehomeslv/` and click the "followers" count.
- Likers: open a reel, click its likes count to open the "liked by" dialog.

Instagram's likes and followers dialogs render a limited number of rows until you scroll inside them. Scroll the dialog to load more when you need a fuller list, but stay reasonable (top ~75 followers, ~60 likers across reels per run).

## Eligibility Filter (for followers and likers only; comments are screened separately)

A handle is **eligible** (gets added so it can be DMed) only if ALL are true:
- A profile picture is optional. A missing photo or default silhouette is fine, do not skip for that.
- Has at least one post.
- Handle is not an obvious bot pattern (long random digit strings, gibberish, spam-word salad).
- Is not a zero-info private account (no pic, no name, no posts).
- **Is not a real estate agent or broker.** Ryan never DMs competitors. Skip anyone whose name or bio presents as a Realtor, real estate agent, broker, brokerage, or real estate team. Signals: "Realtor", "REALTOR", "Real Estate", "Broker", "Realty", "Homes by", a license like `S.0123456`, a brokerage name.

**Allowed on purpose:** regular people, AND non-competing businesses or service providers that can be referral sources (divorce attorneys, landscapers, contractors, photographers, loan officers / lenders). They are partners, not competitors. Example keeps: `@vegasdivorcepros`, `@signature_classicyards`. Example skips: `@jlevylasvegas`, `@frankonrealestate` (realtors).

Capture each person's **display name** so the DM plugins can pull a first name; if there is no usable personal first name, the DM plugin uses a no-name variant.

## Comment Screening (for the Comments harvest)

Apply Ryan's `ig-engage` guardrails. Read them at `/Users/ryanrose/.claude/skills/ig-engage/comment-guidelines.md`. Skip entirely any comment that is political, LGBTQ+, religious, hostile, or otherwise charged. Skip Ryan's own comments and pure-spam. Only add genuine, safe comments worth a reply.
