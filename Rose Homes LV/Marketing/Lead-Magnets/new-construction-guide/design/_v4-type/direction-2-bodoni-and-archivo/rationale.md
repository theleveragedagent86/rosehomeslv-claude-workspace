# Bodoni Moda and Archivo

> Direction 2's typography, which you called nice, with direction 6's color and layout instead of the orange.

## Why this pairing

Bodoni Moda is high contrast, so it is the most formal option here and the most fragile at small sizes. Weight is held at 700 rather than 800 because Bodoni's thick strokes get heavy fast. Archivo is a workhorse grotesque with a wide range.

## What changed from round 3

Nothing except the two typefaces and the tracking and weight adjustments they need.
Same copy, same page architecture, same page budget, same contrast pairs. If one of
these reads better than another, the difference is typography and nothing else.

## Tracking

The base file tracks display type tight, between -.018em and -.034em, which suits the
heavy grotesque it was drawn for. A serif at 54pt does not want that. Every display
selector here is `calc(base + .022em)`, so the relative hierarchy the base
established survives while the absolute tracking loosens to what this face wants.
