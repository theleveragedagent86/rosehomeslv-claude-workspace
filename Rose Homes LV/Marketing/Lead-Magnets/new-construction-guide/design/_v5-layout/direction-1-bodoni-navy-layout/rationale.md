# Bodoni Moda and Archivo

> Bodoni and Archivo in the navy layout. Identical to round 4 direction 2, rebuilt so the two layouts sit next to each other.

## Why this pairing

The panel layout: a photographic cover with a lit navy panel under it, the section opening as a full bleed band dissolving into the paper, and a two column text page. Bodoni's high contrast reads as formal against the navy, and the thin strokes hold up because the display sizes here are large.

## What changed from round 3

Nothing except the two typefaces and the tracking and weight adjustments they need.
Same copy, same page architecture, same page budget, same contrast pairs. If one of
these reads better than another, the difference is typography and nothing else.

## Tracking

The base file tracks display type tight, between -.018em and -.034em, which suits the
heavy grotesque it was drawn for. A serif at 54pt does not want that. Every display
selector here is `calc(base + .022em)`, so the relative hierarchy the base
established survives while the absolute tracking loosens to what this face wants.
