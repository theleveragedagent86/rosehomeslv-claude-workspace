# Direction 6: Sunrise to Sunset, rationale

## Thesis

The book moves through a day. It opens bright and open and closes deep and calm. The palette does not
switch, it drifts: front matter on first light paper, and by the time the reader reaches money and
contracts the pages have deepened into golden hour, ember and warm indigo. Every section header
carries a time of day marker, a dotted arc with a sun dot on it, so the progression is felt before it
is noticed. On this spread the sun sets in the gutter.

## Why this warms protective content

The rejected round made the sourcing apparatus into the design. This one makes time of day into the
design. Indigo at dusk reads as considered. Gray reads as institutional.

The NOT FOUND callout gets the warmest treatment on the page: the only full ember border, a three
colour sunset ribbon across its top, and a filled kicker reading **The most useful thing on this
page**. It does not look like a hole or an apology. The headline stays exactly as written, "I am not
going to hand you a number," at 17.5pt Fraunces with `SOFT` at 44, the roundest setting in the book.

The second move is inversion. Page 20 is a dusk page, but its two working objects, the twenty row
table and the five minute checklist, invert to lit ivory panels on the dark ground, like windows with
the lights on. The table never sits on a dark ground, and the checklist keeps white boxes with ember
outlines a person can tick with a pen in a sales office.

Headings were reframed as questions: "What is this bill that is not in my mortgage?" and "Why did
nobody ask me about this?" under a label reading **A fair question**. No fact, number, date, statute
or phone number was touched.

## Who it wins and who it loses

It wins the reader who has driven past a model home and is nervous but not yet cynical, and it wins on
a phone. It loses anyone who wants a document that looks like a document, and it carries the highest
craft risk of the six: a drift only works if it holds evenly across 44 pages.

## Print ink coverage, honestly

Page 20 is not fully flooded. On an 8.5 by 11 sheet the indigo ground covers about 48 percent, the
rose block 4, and the lit ivory panels take back roughly 47. Page 19 is under 20 percent, the cover
close to 70. Across a 44 page duplex book I estimate 28 to 35 percent average, against maybe 12 for a
plain text guide.

The real constraint is total area coverage. `#1E1442` builds near 250 to 280 percent TAC, which wants
a coated stock. On a digital press a click is a click and the flood costs nothing extra; on a home
inkjet it is punishing. Delivery is a PDF by email, so the fix is one stylesheet: an economy variant
that drops the page 20 flood to `--panel` and keeps a 0.5in indigo header band. Panels, chips and
table stay identical.

## Grayscale survival

Computed 8 bit gray values: paper 252, lit panel 248, wash noon 225, dawn blue 191, amber 178, ember
114, rose dusk 84, indigo dusk 52, indigo night 28. No two colours that share an edge land closer than
30 points. Ember and rose dusk are the closest pair overall, 114 and 84, and they never touch. Nothing
carries meaning in colour alone: the NOT FOUND chip says NOT FOUND, MATURED says MATURED, the diagram
labels every band in words. In grayscale the spread still reads light page, dark page, lit panels.

## Mobile hero

At 860px the hero collapses to one column and the photograph moves above the copy, so the first thing
a cold click sees is dusk over the valley. The button goes full width. The three value props stack in
day order, morning, golden hour, dusk, each keeping its arc marker, so the scroll performs the book's
idea before the reader downloads anything. No horizontal overflow at 375px, verified.

## Reader paths

Three dots sit in the running head of every section opener beside a written label naming which paths
apply. Here it reads "All three reader paths: browsing, touring, already in contract," because SID and
LID applies to everyone. Elsewhere the inactive dots drop to 30 percent opacity and the label names
only the live paths.

## What did not fit

Two honest overruns. The spread runs about 900 words against an 840 budget and I cut nothing. I paid
in type size: 8.7pt on page 19 and 8.5pt on page 20, where 9.5pt would be comfortable. Page 19 has
zero slack, page 20 about four pixels. And the diagram brief asked for roughly 45 percent of the page
19 column height; it is a full width band at about 18 percent. Both are gate items: this section
should get a third page, or the diagram its own half page.
