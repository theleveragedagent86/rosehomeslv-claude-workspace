# Claude Design prompt, Carousel 03, 12 Things To Automate Before Your Next Listing

Build a 7-slide Instagram carousel for **The Leveraged Agent**. Attach the Brandkit logo
files to this chat, you cannot read local paths.

## Brand block, applies to every slide

- Canvas 1080 x 1350, 4:5, all seven slides, no mixed ratios.
- Palette: the thirteen Vector tokens in Part 1 below. One accent, `#1768E5`. No second
  blue, no gradient, no warm color anywhere.
- Type: Barlow 800 headlines at -0.028em. Raleway 600 eyebrow and micro-label only.
  Inter 400/500 body at 1.6 line-height.
- Grid: 64px margins, slide number top-left, monogram bottom-right, both 40px from edge.
- This is a **list carousel**. The numbered items are the product. Set them as a real
  numbered list with generous leading, never as a paragraph, never as icon cards.
- Numerals 1 through 12 are set in `structure` `#0B3FA8`, Barlow 800, visually larger than
  the item text. They are the spine of the whole set and must read at thumbnail size.
- Slide 1 and slide 7 are full-bleed black. Slides 2 through 6 are white. That alternation
  is the only structural device in the set, do not add more.

## Slide by slide

**Slide 1.** Text: eyebrow "THE LEVERAGED AGENT". Headline "12 THINGS TO AUTOMATE BEFORE YOUR NEXT LISTING". Subline "Photos land Tuesday. Everything else is already written." Visual: full-bleed black `#000000`. "12" is oversized in `accent-inv` `#5B9BFF` and may bleed off the left margin as a structural element. Headline in `ink-inv` white, subline in `ink-2-inv`. Full horizontal wordmark bottom-left, minimum 240px wide.

**Slide 2.** Text: micro-label "BEFORE YOU EVER SEE THE HOUSE". Items: "1 The seller CMA and listing presentation" / "2 The pre-listing prep checklist and data sheet". Footer line "Both are built before the appointment, not after." Visual: white. Two items only, so let them breathe at large type. Footer line in `ink-2` above a `line` hairline.

**Slide 3.** Text: micro-label "THE DAY PHOTOS LAND". Items: "3 MLS remarks, written in your voice" / "4 The vertical photo tour video" / "5 The listing landing page". Footer line "Photos in at noon. All three live by one." Visual: white, same list spec, three items.

**Slide 4.** Text: micro-label "LAUNCH DAY". Items: "6 Coming-soon and just-listed sphere emails" / "7 Neighbor letters for the surrounding blocks" / "8 The Meta listing ad and lead form". Footer line "Housing ads run Special Ad Category. No age, gender, or ZIP targeting." Visual: white. This footer is a compliance line, set it in a `bg-2` `#F7F8FA` sunken panel at 20px radius so it reads as a rule, not as commentary.

**Slide 5.** Text: micro-label "THE FIRST WEEK". Items: "9 The agent-to-agent reverse prospecting broadcast" / "10 The carousel and the Shorts cutdowns". Footer line "One shoot. Eight assets. Nothing filmed twice." Visual: white, two items, matches slide 2's spacing exactly.

**Slide 6.** Text: micro-label "AFTER IT GOES PENDING". Items: "11 The Friday seller report" / "12 Every escrow email for the next thirty days". Footer line "My sellers stopped calling for updates. The update just shows up." Visual: white. "12" gets the same treatment as 1 through 11, do not make the last one a special case.

**Slide 7.** Text: "That is 3 to 4 hours of desk work per listing." then "Mine takes about twenty minutes now." then the action line "SAVE THIS BEFORE YOUR NEXT ONE." Visual: full-bleed black, closing the loop with slide 1. The two stat lines in `ink-inv`, with "3 to 4 hours" and "twenty minutes" in `accent-inv` `#5B9BFF`. The save line sits in an `accent` `#1768E5` filled block at 20px radius, text `accent-on` white. One action only, no second ask. Full wordmark bottom-left.

---

# Vector Carousel Design Loop, paste-ready for Claude Design

This is the second half of a skool-carousel deliverable. The DESIGN BRIEF section of
SKILL.md writes the slide-by-slide content brief. This file is the brand-DNA and
critic-loop layer that goes on top of it, pasted into the *same* Claude Design message,
brief first, this file second. Together they are what gets pasted, not this file alone.

Why this exists: pasting a design brief and asking for "a nice carousel" produces a
different, average result every time. This file gives Claude Design hard numbers instead
of adjectives, then makes it grade its own output against a reference before showing it,
the same two-step other design work in this workspace already gets (loop, then codify).
See the two Jack Roberts videos this was built from for the source technique, "design
loop" and "measure, don't describe."

---

## PART 1, Vector brand DNA, measured, not described

Source of truth: `SKOOL Community/Brandkit/Brand-Guide/tokens.json`, adopted 2026-08-19.
If tokens.json has since changed, tokens.json wins, not this file. Update this file to
match if they ever drift.

**Canvas:** 1080 x 1350px (4:5), the IG carousel ratio. Every slide is this size, no
exceptions, no mixed aspect ratios in one set.

**Color, exactly these thirteen values, no invented shades:**

| Token | Hex | Use on a carousel slide |
|---|---|---|
| `bg` | `#FFFFFF` | Default slide surface |
| `bg-2` | `#F7F8FA` | Sunken panel behind a stat or quote block |
| `bg-inv` | `#000000` | Full-bleed black slide (cover, CTA, or a "stop scrolling" beat) |
| `line` | `#E4E7EF` | Hairline dividers only, never text |
| `structure` | `#0B3FA8` | Large numerals, chart bars, structural blocks of color |
| `ink` | `#050E3D` | Headline and body text on white |
| `ink-2` | `#55627F` | Secondary text, captions, slide numbers on white |
| `ink-inv` | `#FFFFFF` | Headline and body text on black |
| `ink-2-inv` | `#9AA3BC` | Secondary text on black |
| `accent` | `#1768E5` | The one accent. Buttons, underline, icon fill, CTA slide background block |
| `accent-on` | `#FFFFFF` | Text sitting on an accent-filled shape |
| `accent-txt` | `#1768E5` | Accent used as colored text on white |
| `accent-inv` | `#5B9BFF` | Accent used as colored text on black |

**The one color rule:** one accent, `#1768E5`, nothing else supplies color. No second
blue, no gradient, no warm color anywhere (no cream, gold, sage, orange). Most of the
visual pop is structural, a full-bleed black slide or block against white, not chromatic.
Black is a surface, never a text color choice on its own slide, it always pairs with
`ink-inv`.

**Type, three faces, three jobs, never swapped:**

| Role | Family | Weight | Tracking | Where |
|---|---|---|---|---|
| Headline | Barlow | 800 | -0.028em | The one big line per slide |
| Subtext/eyebrow | Raleway | 600 | 0.01em | Slide label, kicker, one short line only, never a paragraph |
| Micro-label | Raleway | 600 | 0.15em, uppercase | Slide number, pillar tag |
| Body | Inter | 400/500 | normal | Supporting copy, 1.6 line-height |

Google Fonts link to embed: `https://fonts.googleapis.com/css2?family=Barlow:wght@800&family=Inter:wght@400;500&family=Raleway:wght@600&display=swap`

**Grid, measured, base unit 8px:**

- Canvas margin: 64px on all four sides. Nothing but the logo lockup crosses it.
- Content-safe zone: 952 x 1222px inside the margin.
- Vertical rhythm: headline block, then a 24px gap, then body block, then a 32px gap
  before any supporting element (stat, icon row, quote).
- Slide number / pillar micro-label sits top-left inside the margin, 40px from the top
  edge. Logo monogram sits bottom-right inside the margin, 40px from the bottom edge,
  48px minimum size per the Brandkit min-size rule.
- Headline max width: 80% of the content-safe zone. Never edge-to-edge, it reads as
  cramped.

**Shape and depth:**

- Corner radius: 20px on any card, panel, or button. 12px on a small chip or tag. Never
  a sharp 0px rectangle for a filled shape, never a full pill unless it is a tag.
  Structural full-bleed color blocks (the black or accent bands) stay square, radius
  applies to floating elements only.
- Shadow, only on elevated cards (a stat callout, a quote block), never on the base
  slide: `0 12px 32px rgba(11, 63, 168, 0.14)`, blue-tinted off the `structure` token,
  never a flat gray shadow.
- Depth has two layers max on a carousel slide: base surface, then one elevated card.
  Never a third floating layer, it clutters a 4:5 crop.

**Logo:** monogram only on slides 2 through 9 (bottom-right, per grid above). Full
horizontal wordmark allowed only on the cover slide and the final CTA slide, minimum
240px wide per the Brandkit rule. **Every current logo file is off-palette v1 teal/gold
per tokens.json's own status note.** Until the Vector-palette logo regeneration happens,
render the wordmark as live text, "The Leveraged Agent" in Barlow 800, `ink` or
`ink-inv`, not the PNG. Flag this to Ryan in one line if the brief did not already.

---

## PART 2, The design loop, run this before showing Ryan anything

Do not one-shot the carousel and stop. Build it, then grade it, then fix it, then grade
again. Two full passes minimum, three if the first grade fails on more than one axis.

**Step 1, build.** Generate all requested slides from the DESIGN BRIEF pasted above this
file, using the measured values in Part 1. No adjectives-only decisions, if a value is
not in Part 1, pick the nearest token and say which one you used.

**Step 2, grade against three lenses, one pass each, write the verdict before revising:**

1. **Brief-fit critic.** Does every slide say what the brief's Text: line says, nothing
   added, nothing dropped? Is the CTA slide's one action the same one the brief named?
   Flag any slide that drifted from its brief line.
2. **Vector-brand critic.** Check against Part 1 like a checklist: only the thirteen
   listed hex values present, no stray gray or off-brand color, headline is Barlow 800,
   body never in Barlow, margins at 64px not eyeballed, radius at 20px on cards, shadow
   is the blue-tinted spec not a flat gray, logo treatment matches the rule above. Flag
   every miss by slide number.
3. **Visual-craft critic.** Independent of the brand checklist: does the hierarchy read
   in under 2 seconds, is there one clear focal point per slide, is spacing even and
   intentional rather than centered-by-default, does the accent color appear with
   purpose rather than decoration. Flag anything that looks like a generic template.

**Step 3, revise.** Fix every flagged item. Do not re-run the whole set from scratch,
patch the specific slides that failed.

**Step 4, re-grade.** Run all three critics again on the revised set. If clean, stop and
deliver. If something is still flagged, do one more revise-and-grade pass, then deliver
regardless and name the remaining flag so Ryan can decide if it matters.

**What NOT to do:** don't ask Ryan to pick between design variations, the brief already
made the content decisions, this loop is about execution quality, not new options. Don't
silently lower a value in Part 1 to make something "look better", if a value genuinely
doesn't work for a slide, say so and name the value, don't quietly drift off-spec.

---

## Reuse

This file is Vector-brand-general, not tied to one topic. Paste it after any
skool-carousel DESIGN BRIEF without edits, unless Part 1 has gone stale against
`tokens.json`, check the adoption date at the top of that file against 2026-08-19 first.
