# Direction 1: Field Manual, rationale

**Thesis: a tool you carry into the model home, not a brochure you read on the couch.**

A buyer who has already driven past a model home is not undecided about new construction.
They are worried they are about to be handled. A brochure makes that worse, because a
brochure is the same object the builder just gave them. So this direction refuses the form.
The page is split 64/36, the narrow column is a live note rail with ruled lines, real
checkboxes and labeled blanks, and the whole thing is designed for a ballpoint. The rail sits
on the outer edge of every page, so a folded guide has writing space at both thumbs. The
argument runs down the wide column; the things you do sit in the rail beside it.

The single strongest object on the sample spread is the NOT FOUND callout, and this direction
makes it the widest thing on page 19: a full-measure plate with a black `NOT FOUND ·
REGISTER ITEM 14` header bar, the refusal set at 26px, and then, immediately to its right, a
bordered write-in block labeled `YOUR LOT, YOUR NUMBER` with ruled blanks for the annual
amount and the final payment year. The callout that will not print a number hands you the
line to write your own on. That converts a gap into a service in one object, which is the
whole editorial argument of the guide made physical.

## Who it persuades, who it loses

It persuades the skeptic, the engineer, the spreadsheet person, the out-of-state buyer who is
about to sign on a house they have stood in once, and anyone who has been sold to recently
and did not like it. The utilitarian voice reads as "I am not trying to charm you," which is
exactly the calibration of the headline about who the sales rep works for.

It loses the emotional buyer. There is no aspiration here, no lifestyle, no warmth from
imagery, and the cover looks like equipment rather than like a home. A first-time buyer who
wants to be excited will find it clinical. It is also the hardest of the six to extend into
lifestyle photography later without the photos looking pasted on. If Ryan wants the guide to
also sell the dream, this is the wrong direction.

## Ink coverage and toner

Interior pages run **about 8 to 10 percent coverage**: white stock, a 36 percent rail at a 6
percent tint, one black table header bar, one black callout bar, and text. The cover is the
outlier at **about 88 percent**, because it is a full bleed `#14181D` ground.

A 39 page duplex print is 20 sheets. Against a cartridge rated at 5 percent coverage, the 38
interior pages cost roughly 68 rated pages of toner and the cover alone costs roughly 18. At
$0.03 to $0.05 per rated page that is **about $2.60 to $4.30 per copy, call it $3**, and the
cover is a fifth of it for a fortieth of the pages. An ink-lite cover variant is specified in
`claude-design-prompt.md`: white stock, black masthead band, orange rule, black nameplate,
about 18 percent coverage, which drops the cover to roughly $0.14.

## Grayscale survival

Almost everything survives, because the system carries meaning in value and structure rather
than hue. Six ink tones sit at L\* 6, 20, 33, 42, 58 and 79, which a home laser separates
cleanly. Nothing anywhere is distinguished by color alone: the NOT FOUND table cells carry a
45 degree hatch plus the literal words, `Matured` and `Paid off` carry a 2px underline plus
the words, and the three path tabs get three values plus three fills.

**What breaks:** `--signal-tint` (L\* 93.2) and `--rail` (L\* 94.0) are the same gray. In
color the aside and the callout are visibly warm against a cool rail; in black and white they
are one tone. The mitigation is structural and must not be removed in a cleanup pass: every
tinted panel carries a 2px `--ink` border or a solid black header bar, so the boundary is a
line, not a tone change. Second, the `--zebra` table row is only 3.8 L\* off paper, which is
deliberate so it does not fight the source log, but on a low toner printer it may vanish
entirely. The table does not need it; the hairline row rules carry the structure.

## Mobile hero

At 1280px the hero is a 1.32/1 grid: argument left, and on the right a white card bordered in
3px black that is literally a page torn out of the manual, with the three value props set as
checklist entries. At 375px it stacks in priority order: eyebrow, headline, subhead, full
width button, microcopy, compliance plate, then the card. Headline clamps 70px to 34px, the
button goes full width with the arrow pushed right, and the phone number and email get
`white-space: nowrap` so they never break at the hyphen. Above the fold on a 667px phone you
get the headline, the subhead and the button. The value props are the scroll reward, which is
correct: the headline is the hook, not the feature list.

## Three-path wayfinding

The rail is the tab. Pages 6 to 17 get a bleed tab on the rail's outer edge at three stepped
vertical positions, so a closed stack shows three bands at three heights. Values and fills,
not hues: solid black, mid gray with a hatch, white with a heavy border and a dot grid. Every
path page also carries `PATH A · MOVING HERE` as real text at the head of the rail, visible on
screen and never print-only, and the folio in the source log band picks up the path letter.
Three redundant signals, so losing any one to a bad print does not strand a reader.

## What did not fit, named

The spread carries **1,629 set words** against `page-budget.md`'s 660 word allowance for pages
19 and 20 and against the stated hard ceiling of 360 words per page, which is 720 for a
spread. That is **2.26 times the ceiling**. Two things are consequently overset. Both are
measured, not estimated:

1. **The 19 entry source log.** At 7pt over 1.32 with full URLs in 8.3px mono, the log needs
   **4.79in of two column band across the spread**. After every other element sets complete,
   this grid can spare **2.12in**. Six of nineteen entries render. This is the finding that
   matters most beyond this spread: the strip appears on 34 of 39 pages, and at these URL
   lengths it wants roughly a quarter of every page it sits on. Either the log moves to a
   shared endnote section with per-page markers only, or the guide grows past 39 pages.
2. **SVG-04, the diagram placeholder.** It is not placed. Its labels need about 2.1in of width
   to render near 7pt, and after the callout, the table, the checklist and the log there is no
   4.4 square inch hole left on the spread. The full brief is carried verbatim in an
   HTML comment in `preview.html`, and the built schematic is viewable at
   `svg-04-unplaced.html`. It belongs on page 17
   or 21, where the monthly payment stack is already the subject.

Everything else sets complete at full size: all body prose, the deck, the aside, the beat
lines, the five item numbered list, the NOT FOUND callout, the 20 row table with all six
NOT FOUND cells and all three state cells, the four step checklist with its four write-in
blanks, the phone block, and the soft close. Column overrun on all four text columns is
measured at **0.00in**.
