# Thumbnail design rules

The bar is not "nice". The bar is **legible and arguable at 120 pixels wide**, which is
the size YouTube actually renders a thumbnail in a feed on a phone.

## The squint standard

Every render produces `<out>-squint.png` at 120px. Open it and read it.

- The headline must be **readable**. Not "guessable from memory of what you typed".
- The face must read as **a person with an expression**, not a beige smudge.
- The kicker, badge and disclaimer will be illegible at 120px. That is fine and expected.
  They are for the people who already clicked in far enough to see them.

If the headline fails the squint test, the fix is always **fewer words**, never a bigger
font. The renderer already shrinks type to fit; if it warns that it hit the floor, the
copy is too long for a thumbnail.

## Word count

| Words in headline | Verdict |
|---|---|
| 2–4 | Target. |
| 5–6 | Only if the words are short and the layout is `face-right`. |
| 7+ | Cut it. The title carries the detail, not the thumbnail. |

The thumbnail and the title are **one packaging unit** and should not repeat each other.
If the title says "The New Construction Trap Nobody Warns You About in Las Vegas", the
thumbnail says "THE NEW BUILD TRAP", not the whole title again.

## Colour

- Palette comes from the brand token file. Do not invent colours per thumbnail.
- **One** accent word per headline, marked `[[like this]]`. Two accents means no accent.
- Run the competitive check (see `strategy-brief.md`). If the thumbnails already ranking
  for this query are all warm/orange, lean on the navy field and let gold be the only
  warm note. Standing out beats matching the category.
- Red (`alert`) is reserved for negation: a strike-through, or a downward delta. It is
  not a general accent.

## Composition

- Subject on the right, copy on the left. YouTube overlays the duration badge in the
  bottom-right corner, so keep nothing load-bearing in the last ~120x40px.
- The scrim exists so the headline survives any plate. Do not remove it and do not
  brighten it to "show more of the photo", the photo is context, the words are the click.
- One idea per thumbnail. A stat *and* a comparison *and* a warning is three thumbnails.

## Banned

Carried over from the brand's anti-generic rules and the reasons AI thumbnails look fake:

- Emojis as design elements
- Cheesy stock photography, clip art, generic skylines that are not Las Vegas
- Gradient soup, drop shadows on text used as decoration rather than separation
- Text touching the frame edge
- More than two fonts
- Fake or misleading numbers. Every stat on a thumbnail must be one you can defend in the
  video, sourced from MLS or a named report. This is advertising and the same
  brokerage, MLS and fair-housing rules apply.

## Season and geography

Las Vegas has no snow, no autumn colour, and no lawns. Plates must show palms, gravel
xeriscape, stucco-and-tile, desert mountains. A plate that a local would clock as "not
here" costs more trust than a plain background would have.

Match the plate to the publish date: bleached vertical light in summer, low gold light in
winter.
