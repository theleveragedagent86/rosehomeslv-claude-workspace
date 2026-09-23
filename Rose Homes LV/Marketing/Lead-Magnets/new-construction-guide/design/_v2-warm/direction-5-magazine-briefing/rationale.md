# Direction 5 · Magazine to Briefing · Rationale

**Thesis.** A lifestyle magazine that quietly turns into the clearest briefing document you have ever
been handed. Part one is saturated desert colour, full-bleed photography and a hand-drawn valley map.
Part two drops to two hues pulled out of part one, clay and dusk plum, tightens the grid, shrinks the
photography to a band and doubles the density. Round corners, Petrona and the colour survive. Same
person, different furniture.

**Why this warms protective content.** The last round asked typography to carry warmth alone and it
could not. Warming everything evenly instead either dilutes the hard pages or looks decorative on top of
them. This direction refuses that trade: it gives part one all the warmth it can hold, then spends the
credit on page 19. A reader arrives at the SID and LID spread having been treated well for eighteen
pages, so density reads as intimacy, not austerity. A structural answer, not a typographic one.

Page 18 is a designed transition, included as a bonus panel. A dusk valley photograph dissolves into
paper, a 36pt line says *"That was the tour. Now let's sit down at the table,"* and three cards state
the contract: the colour calms down, the photos get small, the warmth stays.

**The move that makes the hard page work.** The "I am not going to hand you a number" panel is the
largest object on page 19. Its eyebrow is an ochre pill reading *the part where I hand you a tool
instead*, and it ends with an arrow pointing across the gutter at the checklist, which answers with
*here it is, the tool from the facing page*. A gap that hands you something is generosity. A gap that
just sits there is an apology.

**Who it wins.** The reader still in browsing mode. Part one sells them on reading at all, which is the
real conversion problem for a 39 page PDF from a cold ad. It also wins whoever prints one page: page 20
is a worksheet on its own, with the table, the lookup and two phone numbers.

**Who it loses.** Anyone who wants a uniform document. This deliberately looks like two books, and a
skimmer who opens at page 20 never sees the magazine. It is the most expensive of the six to art direct
and the hardest to extend.

**Ink coverage, honestly.** Part one is expensive: roughly 180 to 220 percent coverage on a duplex
sheet, and the cover is worse. Part two is the relief, and that is the argument rather than the excuse.
The spread as built runs about 30 to 40 percent: a thin photo band, one clay panel, one tinted
checklist, zebra rows, otherwise paper. Split near the middle of 44 pages the book averages roughly 100
to 130 percent, comparable to a photography-led brochure. Treat it as PDF-first, and if it ever runs
physically, coat the front half and do not add colour to the back half to match it.

**Grayscale.** Verified by rendering the print PDF to gray. Clay flattens to `#5B5B5B` and plum to
`#373737`, so the table header still reads as a header and the callout still dominates. Nothing depends
on separating those grays, by rule, and the two tints are grayscale identical so they never share a
component. `NOT FOUND` carries four redundant signals: the words, italic, a dotted underline and a
hollow-circle glyph.

**Mobile hero.** Two columns at 1280px. Under 900px the photograph moves above the copy with
`order: -1`, so a phone visitor meets a warm Las Vegas image before any text. Under 560px the H1 drops
to 30px, the quote card goes full width and the button goes full bleed with microcopy beneath. Every
grid track is `minmax(0, ...)`, because plain `1fr` clipped every line at 375px.

**Reader paths.** Three signposts, none dependent on colour. The cover's bottom strip splits into
"Part one · The valley" and "Part two · The briefing". The transition page carries three lettered chips:
Path A, not toured yet; Path B, picking a lot; Path C, already signed. Every briefing spread runs
"Part two · The briefing" as a running head.

**What did not fit.** The copy runs about 900 words against an 840 budget and will not fit at a
readable size unaltered. Three deviations, flagged not hidden. **One,** the 20 row table is set as two
10-row tables side by side, still four columns, each with `<caption>`, `<th scope>` and a header group.
That bought two inches. **Two,** the diagram is landscape at about 30 percent of the page 19 column
height rather than 45, sharing the bottom band with the callout, every specified element present.
**Three,** the dotted escrow box holds only principal and interest, property tax and insurance;
enclosing the association layers would assert they are normally escrowed, which no ledger fact supports,
so they sit outside it, labelled.

Also: the copy says 39 pages and the target is 44, so that number changes in three places if it lands
at 44. License `S.0185572` and `Real Broker, LLC` are a designed lockup on both the cover and the
landing trust line, not swept into a corner.
