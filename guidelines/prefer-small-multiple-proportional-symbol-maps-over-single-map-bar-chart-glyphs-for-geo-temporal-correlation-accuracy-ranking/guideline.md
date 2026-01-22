---
id: prefer-small-multiple-proportional-symbol-maps-over-single-map-bar-chart-glyphs-for-geo-temporal-correlation-accuracy-ranking
title: Prefer Small-Multiple Proportional Symbol Maps Over Single-Map Bar-Chart Glyphs
  for Higher Accuracy in Geo-Temporal Correlation Judgments
bibliography: references.bib
description: For geo-temporal correlation judgments, proportional symbol map small
  multiples ranked above a single map using bar-chart glyphs on accuracy.
labels:
- chart:map
- chart:small-multiples
- chart:bar
- task:correlate
- visual:position
- visual:color
- visual:length
- impact:accuracy
- data:spatiotemporal
- audience:expert
- domain:geospatial
- complexity:advanced
---

## Prefer proportional symbol map small multiples over single-map bar-chart glyph maps for correlation accuracy <!-- role: advice -->

For geo-temporal correlation judgments, use proportional symbol maps in small multiples rather than a single map with bar-chart glyphs to prioritize accuracy.

## Why this accuracy preference can hold for correlation judgments <!-- role: reason -->

A single-map glyph approach distributes time-series structure across many separate glyphs, which can increase the chances of missing or misintegrating evidence across locations when forming a single correlation judgment. Small multiples can reduce this integration burden by organizing comparable views into a repeated layout.

**Mechanism:** Lower integration overhead across many dispersed glyphs supports more reliable synthesis of correlation evidence.

**Evidence:** In a comparative experiment of three geo-temporal designs, proportional symbol map small multiples ranked higher than a single-map bar-chart glyph design on accuracy for correlation judgments (with no significant-pair differences recorded for accuracy in the extracted summary) [@pena-arayaComparisonVisualizationsIdentifying2020]. This ranking is represented as structured knowledge intended for translation into visualization recommendation constraints and heuristics [@zengReviewCollationGraphical2023].

**Notes:** Treat this as a ranking-based guideline rather than a statistically confirmed accuracy gap.

## When this applies <!-- role: context -->

- **User Goal:** Make the correct correlation judgment (positive/negative/none) over space and time.
- **Task:** Correlate.
- **Data:** Geo-temporal dataset with at least two quantitative variables.
- **Chart Setting:** Static map-based visualization; standard display.
- **Audience:** Analysts performing correlation assessment.
- **Success Criterion:** Fewer incorrect correlation judgments.

## When not to follow it <!-- role: exceptions -->

**Break it when:** You must maximize within-location temporal readability for each location above all else. **Why:** The guideline targets overall correlation-judgment accuracy, not the ease of reading each location’s full time series in isolation.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Space efficiency, because small multiples require multiple panels.\
**Risk:** If panels become too small, legibility may drop and negate accuracy benefits.\
**Mitigation:** Limit the number of panels shown simultaneously or increase display space.

## Common mistakes <!-- role: mistakes -->

**Mistake:** Keeping the single-map bar-chart glyph design while asking users to make a single global correlation judgment. **Why it fails:** The design can force repeated, distributed reading and integration that increases opportunities for error.

## Quick tests <!-- role: check -->

**Failure Sign:** Users answer quickly but disagree widely on the correlation judgment for the same view.\
**Quick Check:** Ask two reviewers to independently judge the correlation; if disagreement is high with the single-map glyph layout, accuracy is at risk.\
**Stronger Test:** Run a brief accuracy test set (a handful of questions) on both designs and compare error rates.

## What to do instead <!-- role: fix -->

- Use proportional symbol map small multiples for the correlation-judgment task and keep the single-map bar-chart glyph design only for tasks centered on individual locations.
- Reduce the number of locations shown at once in the single-map glyph design to lower integration burden.
- Separate the workflow into two stages: an overview for correlation judgment (small multiples) and a detailed per-location view (single map with glyphs).
