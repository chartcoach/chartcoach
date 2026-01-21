---
id: use-small-multiple-proportional-symbol-maps-over-single-map-bar-glyphs-for-correlation-over-space-time
title: Prefer Small-Multiple Proportional Symbol Maps Over Single-Map Bar Glyphs
bibliography: references.bib
description: For correlation identification over space and time, small-multiple proportional-symbol
  maps are faster than bar-chart glyphs on a single map, and in this study also ranked
  higher for accuracy.
labels:
- chart:map
- chart:small-multiples
- chart:bar
- task:correlate
- visual:color-saturation
- visual:area
- visual:length
- visual:position
- data:spatiotemporal
- data:quantitative
- audience:expert
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

When you need users to identify correlation over space and time, use a proportional-symbol map in small multiples instead of bar-chart glyphs on a single map.

## The Logic <!-- role: reason -->

Small multiples juxtapose time into separate panels, reducing repeated within-glyph searching for the relevant time slice across many locations; in this experiment, that corresponded to significantly faster performance than a single-map bar-glyph design, and also a higher (non-significant) accuracy rank.

- **The Principle:** Reduce repeated search by externalizing time with small multiples.
- **The Evidence:** The collated ranking shows the proportional-symbol small-multiple design (E-2) ranked above the single-map bar-glyph design (E-3) for both accuracy and time, with a significant time advantage (E-2 > E-3) reported via bootstrapping at α=0.05 [@pena-arayaComparisonVisualizationsIdentifying2020]. This guideline is derived via the collation framework in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Decide whether two quantitative variables are correlated when viewed across geography and time.
- **Data Type:** Spatio-temporal, with multiple locations and time steps; quantitative variables encoded on a map.
- **Audience:** Analytical users (the study participants were visualization-literate).

## When to Break It <!-- role: exceptions -->

- **Scenario:** You must keep everything in one single map view (no faceting/small multiples available).
- **Reason:** This rule assumes you can allocate space for multiple panels; the compared alternative (single map with bar glyphs) is specifically the no-faceting option tested.

## The Price <!-- role: costs -->

- **The Sacrifice:** More screen space and visual complexity (multiple panels).
- **The Risk:** Small multiples may become hard to read if each panel is too small or if the number of time steps grows beyond what can be shown legibly.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Switching from bar-glyphs-on-one-map to circles-on-one-map without faceting time.
- **Why it fails:** The evidence here is specifically about using small multiples (row/column faceting) versus a single-map design; simply changing glyph shape does not recreate the juxtaposition benefit.

## How to Check <!-- role: check -->

- **Visual Sign:** Users have to repeatedly scan within each location’s glyph to find the same time slice before they can compare locations.
- **The Test:** Ask a user to answer a correlation question while thinking aloud; if they repeatedly say “now I need to find year X again in each state,” you likely violated the rule.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Facet the map by time (small multiples) while keeping the same proportional-symbol encoding.
- **Best Fix:** Rebuild as a proportional-symbol map in small multiples (encode one variable by symbol area and the other by color saturation, and lay out time using row/column facets), matching the higher-performing design pattern reported in [@pena-arayaComparisonVisualizationsIdentifying2020] and organized for reuse in [@zengReviewCollationGraphical2023].
