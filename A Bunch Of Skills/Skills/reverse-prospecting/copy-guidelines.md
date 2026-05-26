# Reverse Prospecting Email — Copy Guidelines

These rules govern how to write the two-paragraph agent note section in every reverse prospecting email. This is the only section that changes meaningfully between listings. Everything else is template-driven.

---

## Voice and Tone

- Write as Ryan, one agent emailing another agent. First person.
- Warm and direct. Not formal, not corporate, not salesy.
- Conversational but professional. Think "helpful colleague," not "marketing blast."
- Confident, not excited. No exclamation points.
- Data-rich. Specific room dimensions, feature names, lot sizes, year built. Never vague.

## Formatting Rules

- **No em-dashes.** Use commas, periods, or "and" instead. This is the number one rule.
- No semicolons.
- Short sentences. If a sentence has more than one comma, consider splitting it.
- No bullet points in the agent note. Flowing prose only.
- Two paragraphs maximum. The email is designed to be scannable.

## Words and Phrases to Avoid

- "Stunning," "gorgeous," "beautiful," "dream home," "must-see," "won't last"
- "We are pleased to present," "It is our pleasure," or any third-person corporate language
- "Amazing opportunity," "rare find" (unless you explain exactly why it's rare with data)
- Any phrase that sounds like it belongs on a flyer

## Paragraph 1 — Reverse Prospecting Context

**Purpose:** Explain why the recipient is getting this email and give them a reason to keep reading.

**Structure:**
1. First sentence: Why this email exists. Reference reverse prospecting directly. Example: "this one showed up on reverse prospecting and I wanted to get it in front of you directly before it goes active."
2. Second sentence: The hook. What combination of features makes this listing worth a look for their buyer? Focus on what is hard to find at this price point or in this area. Example: "If you have a buyer looking for a single-story in Henderson with a 3-car garage, this is worth a look."

**Saved/Favorited variant:** If the user reports that a prospect saved or favorited the listing in MLS, adjust the opening to acknowledge this directly. Example: "I noticed your buyer saved this listing in MLS, so I wanted to reach out directly." This is stronger than the generic reverse prospecting opener because the buyer already showed active interest. The rest of the paragraph stays the same (the hook).

**Length:** 2-3 sentences. Keep it tight.

**Note:** The paragraph starts after the Kit greeting tag `Hey {{ subscriber.first_name | default: "there" }},` which is already in the HTML template. Your copy begins with a lowercase letter (e.g., "this one showed up...") since it follows the comma after the name.

## Paragraph 2 — Property Details

**Purpose:** Give the agent enough specifics to know whether this home fits their buyer, without needing to open the MLS sheet.

**Structure:**
1. Open with subdivision name and year built for geographic/age context.
2. Walk through the most notable interior features using specific details. "Kitchen has a center island with bar stools, gas range, and a walk-in pantry" not "Updated kitchen."
3. Mention the primary suite if notable (dimensions, closet type, bath features).
4. Include differentiating features: solar (owned vs. leased), pool, RV parking, etc.
5. End with availability and showing info. "It's vacant right now and available for showings through ShowingTime anytime." or "Occupied, 24-hour notice required through ShowingTime."

**Length:** 3-5 sentences.

## What NOT to Include in the Agent Note

- **Price** — already displayed in the price line above the note
- **Bed/bath/sqft stats** — already in the stat bar
- **MLS number** — already in the price line
- **Full address** — already in the address heading
- **Ryan's contact info** — already in the footer and secondary CTA

These are all visible in other sections of the email. Repeating them wastes space and makes the note feel templated rather than personal.

---

## Reference Example

From the 29 Amber Rock St email:

> this one showed up on reverse prospecting and I wanted to get it in front of you directly before it goes active. If you have a buyer looking for a single-story in Henderson with a 3-car garage, this is worth a look.

> The home is in Champion Village, built in 2000. Kitchen has a center island with bar stools, gas range, and a walk-in pantry. Open to the family room with a fireplace. Primary suite is 16x14 with a walk-in closet. Solar is owned. It's vacant right now and available for showings through ShowingTime anytime.
