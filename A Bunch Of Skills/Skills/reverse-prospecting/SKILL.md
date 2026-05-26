---
name: reverse-prospecting
description: Use when someone asks to create a reverse prospecting email, generate an agent-to-agent email for a listing, build a Kit/ConvertKit broadcast for buyer agents, or set up a reverse prospecting campaign.
argument-hint: "property address"
---

## What This Skill Does

Generates a polished HTML reverse prospecting email for a listing, then walks through the MLS email extraction and Kit broadcast setup. The email targets agents whose buyers have saved searches matching the property.

This skill produces the fully-designed HTML agent-to-agent email + Kit/MLS workflow. For plain-text email blasts, social posts, neighbor letters, and other listing marketing content, use the listing-marketing skill.

**Listing folder:** /Users/ryanrose/Downloads/Claude/Listings/
**Master template:** [email-template.html](email-template.html)
**Copy rules:** [copy-guidelines.md](copy-guidelines.md)
**MLS + Kit checklists:** [kit-and-mls-instructions.md](kit-and-mls-instructions.md)

---

## Step 1: Locate the Listing Folder

If `$ARGUMENTS` is provided, search for a matching folder under `/Users/ryanrose/Downloads/Claude/Listings/`. The folder name is the street address (e.g., "29 Amber Rock St").

Once found, read available files to auto-gather property details:
- Marketing package (`.docx`) for property highlights and features
- Any existing email files for reference (avoid duplicating what already exists)
- Glob the `Listing Photos/` subfolder to catalog available images

If no listing folder exists, ask the user for the property address and whether to create the folder.

If no `$ARGUMENTS` is provided, ask: "Which listing are we building the reverse prospecting email for?"

---

## Step 2: Collect Property Details

Gather all required data. If the listing folder provided enough info, confirm with the user. Otherwise, ask for missing fields.

**Core property details (required):**
- Full address (street, city, state, zip)
- List price
- MLS number
- Active date (or launch date)
- Beds / Baths
- Square footage
- Garage (type and count, e.g., "3-Car")
- Story type (Single, Two-Story)

**Email-specific details:**
- Badge text: Coming Soon, Just Listed, Price Reduced, Back on Market, Open House (default: "Coming Soon")
- Subject line (suggest one using: `Your buyer might be a match | [Badge Text] in [City] | MLS# [MLS_NUMBER]` -- user can override)
- ShowingTime link (or leave as placeholder)

**Photo selection:**
- Hero image: List available photos from the Listing Photos folder. Prefer filenames containing "twilight" first, then `dji_` prefix (drone shots), then ask the user.
- Interior image: Suggest the kitchen as default. List filenames and ask the user to pick one, or accept their suggestion.

**Quick Details (6 rows, defaults shown):**

| Row | Default Label | Example Value |
|-----|--------------|---------------|
| 1 | Subdivision | Champion Village |
| 2 | Lot Size | 6,534 SF (0.15 ac) |
| 3 | Year Built | 2000 |
| 4 | Solar | Owned |
| 5 | Occupancy | Vacant |
| 6 | Showing Method | ShowingTime |

Ask if these labels work or if any should be swapped (e.g., "HOA Fee" for condos, "Builder" for new builds).

**Reverse prospecting details:**
- Ask: "Did any agents save or favorite this listing in MLS?" If yes, note which agents. This affects the email copy (see copy-guidelines.md for the saved/favorited variant).

**Standout features for the agent note (2-3 items):**
- What makes this home stand out?
- What combination of features is hard to find in this area or at this price?

---

## Step 3: Check for Template

Check if `/Users/ryanrose/Downloads/Claude/A Bunch Of Skills/Skills/reverse-prospecting/email-template.html` exists.

- **If it exists:** Read it and proceed to Step 4. Print: "Loaded master template."
- **If it does not exist:** This should not happen since the template ships with the skill. If somehow missing, recreate it by writing the full HTML template from memory (the structure matches the 29 Amber Rock reverse prospecting email with all property values replaced by `[BRACKET]` placeholders). Print: "Recreated master template."

---

## Step 4: Write the Agent Note Copy

Read [copy-guidelines.md](copy-guidelines.md) for the full writing rules. Write two paragraphs:

**Paragraph 1 (reverse prospecting context):**
- If agents saved/favorited the listing: Use the saved/favorited variant opener ("I noticed your buyer saved this listing in MLS, so I wanted to reach out directly.")
- Otherwise: Use the standard reverse prospecting opener ("this one showed up on reverse prospecting and I wanted to get it in front of you directly before it goes active.")
- Follow with the hook: what makes this listing worth a look for their buyer.

**Paragraph 2 (property details):**
- Subdivision + year built, notable features, differentiators, availability/showing info.

Present the draft to the user: "Here's the agent note copy. Want to adjust anything before I generate the email?"

Wait for approval or revisions before proceeding.

---

## Step 5: Generate the Final HTML Email

1. Read the master template from `email-template.html`.
2. Replace all `[BRACKET]` placeholders with the actual property data.
3. Write the completed HTML file to the listing folder.

**Output filename convention:**
- Take the street number and street name (drop the suffix like St, Ave, Dr, Ct, Ln)
- Replace spaces with underscores
- Append `_Agent_Reverse_Prospecting_Email.html`

Example: "29 Amber Rock St" becomes `29_Amber_Rock_Agent_Reverse_Prospecting_Email.html`

**Output path:** `/Users/ryanrose/Downloads/Claude/Listings/[Address Folder]/[Filename]`

After writing the file, print:
```
Email generated and saved to:
[full output path]

Open the file in a browser to preview the layout before uploading to Kit.
```

---

## Step 6: Output MLS + Kit Checklists

Read [kit-and-mls-instructions.md](kit-and-mls-instructions.md) and print both checklists with all listing-specific details filled in:

- `[FULL_ADDRESS]` replaced with the actual address
- `[MLS_NUMBER]` replaced with the MLS number
- `[SUBJECT_LINE]` replaced with the final subject line
- `[HERO_IMAGE_FILENAME]` and `[INTERIOR_IMAGE_FILENAME]` replaced with the chosen filenames
- `[ADDRESS_FOLDER]` replaced with the listing folder name
- `[OUTPUT_FILE_PATH]` replaced with the full path to the generated email
- `[BADGE_TEXT]` replaced with the badge text
- `[STREET_ADDRESS]` replaced with just the street address
- `[DATE]` replaced with today's date

Important reminders to include:
- Only export agents with a reverse prospecting count under 50 (broad searches are not meaningful matches)
- Note any agents who saved or favorited the listing for priority follow-up

---

## Notes

- **Ryan Rose info:** Real Broker, LLC | 702-747-5921 | ryan@rosehomeslv.com | rosehomeslv.com | License #S.0185572
- **No em-dashes.** Across all copy. Use commas, periods, or "and" instead.
- Never make up property details. Use [BRACKETS] for anything unknown.
- The email is agent-to-agent. Tone is professional but warm, one colleague to another.
- The Kit personalization tag `{{ subscriber.first_name | default: "there" }}` is hardcoded in the template. Do not modify it.
- If the listing already has a reverse prospecting email in its folder, confirm with the user before overwriting.
