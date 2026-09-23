> A screen-printed desert poster that happens to be a disclosure document: direction 5's sunset palette and dissolving photo header, direction 1's page architecture, and not one serif in the whole book.

## What I was asked to keep, and what I did with it

Ryan gave three pieces of direction and they are all load-bearing. He liked **the layout of
direction 1**, **the colour scheme of direction 5**, and specifically **the header on direction 5's
Strip pages**. This variant is the second of two that take that instruction literally and differ only
in typography. Variant 2 is the other one. Mine is the geometric poster.

**The layout I inherited from direction 1.** The rounded full-bleed photo headline block at the top
of the section. Friendly question subheads in coloured small caps, each answered by a short
declarative line set larger underneath. Tinted rounded callout cards two abreast, each opening with a
small coloured square glyph. A numbered list with the numerals in filled circles. Short inline
attribution set small and quiet under the paragraph it supports, never a source strip. The refusal
callout as the single loudest object on the spread, a solid saturated panel with a ribbon label. The
stacked payment diagram with one item visibly outside the escrow bracket. The dense district table.
Folios reading across the gutter.

**The header device I inherited from direction 5.** Full-bleed photograph, the dusk valley shot with
the city lights, its bottom edge dissolving into the page paper on a gradient, a small colour eyebrow
in caps above and the big headline sitting inside the faded zone. In direction 5 that device carried
an italic second line in the accent colour. Syne ships no italic, so I set the second line as a
separate display line in `--sunset` instead. It does the same job louder.

## Why geometric, and how it stays warm

The brief for this variant was explicit: no display serif, build the whole hierarchy from one strong
geometric family used heavy and large with tight optical tracking. **Syne** is that family. It has
real weight range, its bones are strange enough to have a personality, and it is not a face anyone in
Las Vegas real estate is using. **Karla** reads underneath it, a grotesque with a tall x-height that
holds at 5.9pt in a table token and still looks human at 9.5pt in body prose.

The obvious failure mode here is drifting into the analytical, tech-startup look. Four things stop it:

1. **Colour volume, not colour accents.** The refusal panel is a solid sunset field roughly a fifth of
   page 20. The credibility band on the cover is a slab of ochre that bleeds off the left edge. The
   cover seam is four saturated bands. This is a poster palette used at poster scale, not a UI theme
   with an accent colour.
2. **Round geometry everywhere.** Radii of 10, 16 and 26pt, pill chips, pill numeral circles. The only
   square corners in the direction are the seam ribbon, the folio tiles and the glyph squares.
3. **Photography at full bleed.** The opener photo is a third of page 19. The cover photo is half the
   cover. There are two more photo bands. Photography is what makes this feel like a guide rather than
   a disclosure.
4. **Not one neutral gray.** Every rule, every muted value and every tint is warm. `#977C61` instead of
   `#999999` is a small thing that changes the whole temperature of the page.

## The refusal callout

Thirty-four of thirty-nine pages carry a `NOT FOUND`, so if a refusal reads as a hole the direction has
failed. Here it is the biggest, loudest, most saturated object anywhere in the book: a full-width
sunset panel with a cream ribbon tag reading **Here is where I stop** and a 21pt Syne headline that
says **I am not going to hand you a number.** The body then splits into two columns so the panel is
wide and confident rather than tall and apologetic. Nothing else on the spread competes with it. It
reads like a maker's mark, which is exactly the register Ryan's voice wants: I checked, it does not
exist, here is the lookup instead.

## Three pages, not two

Every director in rounds two and three overran a two-page budget once photography came in. This
variant is built on the three-page allocation and it uses all of it:

- **Page 19, what it is.** The photo header device, the deck, the origin of the money, and the five
  things to know before you sign.
- **Page 20, what it costs and what I will not tell you.** Why nobody asked you, whether you can pay it
  off, the payment diagram, the refusal, and then the five minute lookup the refusal promises.
- **Page 21, the tools.** The twenty-district table split into two ten-row halves, the thirty-years-apart
  comparison, the two phone numbers, and the soft close.

Body prose sits at **9.5pt over 1.50** throughout. Nothing in prose is crushed to make a grid work.

## What I rewrote and what I did not

I rewrote every heading, subhead, callout label and ribbon into a more declarative register, because
Ryan asked for different content between variants: **The bill that never shows up in your mortgage**,
**Into the ground, before your house was there**, **Outside the escrow bracket, on a bill of its own**,
**Every district ends. Which one your lot sits in is the whole game.**

I changed **no fact, no number, no date, no statute reference, no phone number and no source.** The
cover title, the landing headline and every value prop stayed exactly as written, because those are
the calibration sentences for the whole guide's voice and changing them would stop being a design
comparison.

## The bug this direction shipped with, and what it cost

The first build of this file looked finished and was not. The base prose rule is `.gp p`, which is
specificity (0,1,1) and uses the `font` shorthand, so it beat every paragraph component selected by a
single class and reset it to 9.5pt Karla 400. Seven components were flattened: the question subheads,
the lead hit line, the inline attributions, the pull line, and all three parts of the section opener.
The pull line was authored at 23pt Syne 800 and was rendering at 9.5pt Karla 400. The opener's sunset
accent line, which is the whole substitute for direction 5's italic, was rendering as body text.

The page still looked plausible, which is the point. It read as a slightly bland version of itself,
and no amount of squinting at a screenshot would have found it. Reading `getComputedStyle` for every
component against the type scale did. Every paragraph component is now scoped `.gp .name` at (0,2,0),
and section 5 of `tokens.md` carries the rule so the next person does not repeat it.

## Where it is weakest

**Page 21 is the tight page, at 37px of slack in the print box.** Adding a district row or a sentence
to that page means taking something off it. Pages 19 and 20 have about 54 and 51.

**The pull line only works at full measure.** At 23pt Syne with -0.034em it needs the whole 710px text
width to break into two clean lines. Set inside a column it broke three ways with a one-word last
line, which is why it now sits full width above the two-column row. Anyone reusing `.pull` in a
column will get that widow back.

**Sunset is a large-display colour only.** It computes 4.35 on paper, so it cannot carry a caption, a
label or a body line. Every small coloured word in the book is `--clay`, and the two reading almost
identically at a glance is a discipline the next person has to keep.

**The grayscale set is tight in the middle.** Clay, muted and agave land at 91, 92 and 95. They are not
separable on a monochrome laser, which is why nothing encodes meaning through them and why the NOT
FOUND and Matured tokens are told apart by a hollow versus a filled square.

**Syne has no italic.** If a later section genuinely needs a quiet aside voice rather than a loud one,
this system has weight, caps and colour and nothing else. That is a real constraint, not a preference.

**The valley map is decorative.** It is schematic, labelled as not to scale, and it should stay a
generic orientation drawing. It must never imply a specific named community.
