# Newsreader and Figtree

> The warmest of the five. Magazine feature rather than manual.

## Why this pairing

Newsreader has more stroke contrast and open counters than Spectral, which reads friendlier at headline size and a little softer at body size. Figtree is a rounded humanist sans, so the caps labels lose some of their institutional edge.

## What changed from round 3

Nothing except the two typefaces and the tracking and weight adjustments they need.
Same copy, same page architecture, same page budget, same contrast pairs. If one of
these reads better than another, the difference is typography and nothing else.

## Tracking

The base file tracks display type tight, between -.018em and -.034em, which suits the
heavy grotesque it was drawn for. A serif at 54pt does not want that. Every display
selector here is `calc(base + .014em)`, so the relative hierarchy the base
established survives while the absolute tracking loosens to what this face wants.
