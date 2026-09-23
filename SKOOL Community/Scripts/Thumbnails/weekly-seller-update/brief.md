# Thumbnail brief: Weekly Seller Update (Level 5)

**Brand:** The Leveraged Agent. Locked Brandkit layout (white field, lowercase 900 headline left, Ryan right). Only the headline and the photo crop were touched.

## The five questions

1. **Real argument:** Agents lose listings to silence, not price. One Plan Mode prompt builds a system that sends every seller a real, data-backed update every week, and it was built from a real listing (29 Amber Rock St).
2. **First-half-second feeling:** A = warned. B = greedy (I want that).
3. **Visual evidence:** Ryan's face and the claim. No stat on the thumbnail. The proof numbers (21 showings, 5,500+ views) belong in the video.
4. **Works with no text?** Not by itself. This is a person-plus-claim thumbnail, same as the approved set.
5. **Expression:** Stock smiling headshot. Right for B. For A, a flat, closed-mouth expression would fit better, but that needs a generated likeness and Ryan's approval, so the approved headshot was used.

## Competitive check (YouTube search "weekly seller update real estate agent", 2026-09-17)

- **Nobody owns it.** The top results are low view counts (63 to 1.3K), framed as a manual "sheet" or "routine". Zero are about AI or automating it.
- **The fear is proven on the seller side:** "Fire Your Real Estate Agent If They Do This" pulled 7.5K views in 16 hours. Concept A borrows that fear and flips it to the agent.
- **Layout:** the category is busy, colorful and text-heavy. A white field with two lines of black type stands out.

## Concepts

| | File | Headline | Argument |
|---|---|---|---|
| A | `thumb-a.png` | sellers fire silent agents | the fear: silence costs you the listing |
| B | `thumb-b.png` | ai writes my seller updates | the payoff: the update writes itself |

**Recommendation: ship A, test B.** A matches the fear that is already getting views in this niche and gives the title room to carry the AI promise. B is clearer about the video but reads like every other "AI does X" thumbnail.

## Paired titles

**For A (sellers fire silent agents):**
1. The Weekly Seller Update That Runs Itself (Claude Code for Realtors)
2. I Automated My Weekly Seller Updates With One Prompt
3. Stop Losing Listings: Build an AI Seller Update in Claude Code

**For B (ai writes my seller updates):**
1. Why Sellers Fire Their Agent (And the 5 Minute Weekly Fix)
2. The Seller Report My Clients Get Every Friday, Built With Claude Code
3. Never Miss a Seller Update Again: My Full Claude Code System

"5 Minute" in B.1 is an estimate. Confirm the real weekly runtime before using it.

## Files

- `thumb-a.html` / `thumb-b.html`: sources. Canonical template text spec (44px / 190px / 94px / 900). Photo crop changed to match `Brandkit/YouTube-Thumbnails/example.png`: frame 780px wide, image height 2000px, top -110px, plus a white fade on the frame's left edge that hides the gray backdrop seam. The template's documented crop (580 / 1168 / -13) renders Ryan far smaller than the approved example.
- `shoot.mjs`: `node shoot.mjs thumb-a thumb-b` renders 1280x720 PNGs over file://, no server needed.
- `*-squint.png`: 120px proofs. Both headlines are readable.
