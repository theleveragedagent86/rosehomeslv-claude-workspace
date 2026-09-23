# Direction 3, Wayfinding, rationale

**Thesis:** find your line and ride it to the end. The three reader paths are literal transit routes, and every page says which line you are on with a letter, a shape, a rail pattern and a colour, in that order.

**Why it serves a scared buyer.** Someone who drove past a model home and told nobody is not confused about real estate, they are afraid of missing something. An airport does not calm you by explaining itself, it calms you by never letting you wonder where you are. Every page answers three questions before a word is read: what line am I on, how far in am I, where does this end. The cover is the route map, so a reader sees the shape of the commitment before boarding.

It also fits the content's hardest move. The guide refuses to print numbers it cannot verify, on 34 of 39 pages. In signage a missing figure is not an apology, it is a service advisory: hatched plate, heavy rule, stated reason. The NOT FOUND callout is the second largest object on page 19 and reads as competence. In the table it shrinks to a hatched swatch plus the words, so five NOT FOUND cells look deliberate, not broken.

**Who it wins and loses.** It wins the literal and the organised: engineers, nurses, transferees, anyone who reads a lease before signing. It loses the reader who wants warmth. No photography, no lifestyle, no softness. It is the least luxurious direction Ryan will see.

**Ink coverage.** An interior page runs about **11 percent**: rail 2.5 square inches, body text 3.7, source strip 2.1, rules and tints 1.0, against 93.5. The cover is about 8 percent. ISO toner ratings assume 5 percent, so a 39-page duplex print is about 86 standard pages, which on a 1,500 page cartridge at around $70 is **$3.50 to $4.50 of toner per copy**. Duplex halves paper, not toner. The rail alone is 2.4 of those 11 points, so `tokens.md` ships a `--rail-outline` variant that prints the band as a 1.2pt outline, dropping a copy to about $3.00 and costing the closed-stack thumb read.

**Grayscale survival.** What survives: every marker carries a letter, a shape and an ink outline, so black and white loses nothing. As grey patches Line A is 2.56 against Line B and Line B is 2.45 against Line C, visibly different tones rather than three identical greys. Rail patterns are solid, dashed and dotted, a fourth channel. NOT FOUND is ink and hatch, never colour. What breaks: the trunk band and the Line A band compute to **1.48 against each other in grayscale**, nearly the same black. That is fixed by pattern, not tone. The trunk band carries a continuous paper-white centreline and Line A never does. Delete that centreline and grayscale wayfinding on trunk pages is gone.

**Mobile hero.** Container queries, not viewport queries, so it reflows wherever Lofty embeds it. Below 860px the ink station panel drops under the copy, the H1 goes from 60px to 40px, and an action bar pins to the bottom with the button and microcopy. In production that bar is `position: fixed`; in the preview it is `position: sticky` so it stays in frame. The button appears twice on a phone, a deliberate conversion choice. No form in the embed: the button anchors to `#contact`.

**Three-path wayfinding.** Four redundant channels ranked letter, shape, pattern, colour. On pages 6 to 17 exactly one tab plate prints, stepped to one of three heights, so a closed stack shows three bands at three heights. On shared pages all three plates print at those heights against the ink trunk band, which is what pages 19 and 20 show: your own letter on a page that belongs to everybody.

**What did not fit, named.** The spread is over budget and no type size fixes it.

1. The 19-entry source strip needs **2.64 inches** at the foot of page 19 and **2.52 inches** on page 20 at the specified 7pt, three columns, every entry set. That is 27 percent of each page before any body copy.
2. Body prose is **9pt over 1.32, not the 10.5pt the budget requires**. Even at 7.4pt, page 20 still overran. Type size is not what makes this spread fit.
3. **SVG-04 was specified at 45 percent of the page 19 column, 2.64 inches. It got 1.08 inches, 18 percent.** The placeholder plate says so on the page.
4. **The phone block did not fit on page 20.** An overset plate names it and points to page 21, and both numbers still appear in sources 18 and 19 on the same spread.
5. Page 19 carries 509 words against a 320 budget, page 20 carries 388 against 340, plus a 384 word strip. **This spread needs a third page, or the per-page strips need to become one sources section.**

Every other word is set verbatim, with zero overflow on all three page boxes.
