---
id: prefer-proportional-symbol-map-small-multiples-over-cartogram-small-multiples-for-geo-temporal-correlation-accuracy
title: Prefer Proportional-Symbol-Map Small Multiples Over Cartogram Small Multiples
  for More Accurate Geo-Temporal Correlation Judgments
bibliography: references.bib
description: When using small multiples for geo-temporal correlation judgments, proportional
  symbol maps ranked higher in accuracy than Dorling cartogram small multiples.
labels:
- chart:map
- chart:small-multiples
- task:correlate
- visual:position
- visual:color
- visual:area
- impact:accuracy
- data:spatiotemporal
- audience:expert
- domain:geospatial
- complexity:advanced
---

## Choose proportional symbol map small multiples over cartogram small multiples for correlation accuracy <!-- role: advice -->

When you use small multiples to judge geo-temporal correlation, choose proportional symbol maps rather than Dorling cartogram small multiples to improve accuracy.

## Why proportional symbol map small multiples can be more accurate than cartogram small multiples <!-- role: reason -->

Cartogram-based small multiples can introduce additional perceptual work because the geographic shapes and their relative positions can shift across panels, making it harder to consistently match locations when forming a correlation judgment. Proportional symbol maps keep a stable base geography, which can reduce location re-identification errors.

**Mechanism:** A stable spatial frame reduces location-matching overhead across panels, supporting more consistent comparisons.

**Evidence:** In an experiment comparing Dorling cartogram small multiples versus proportional symbol map small multiples for geo-temporal correlation judgments, the proportional symbol map small multiples ranked higher in accuracy than the Dorling cartogram small multiples [@pena-arayaComparisonVisualizationsIdentifying2020]. This comparative result is included as collated structured knowledge for visualization recommendation and rule extraction [@zengReviewCollationGraphical2023].

**Notes:** The extracted structured record does not include significant-pair evidence for accuracy differences, so treat this as a directional preference rather than a guaranteed improvement.

## When this applies in practice <!-- role: context -->

- **User Goal:** Correctly judge whether two quantitative variables are correlated over space and time.
- **Task:** Correlate.
- **Data:** Two quantitative variables across locations and time steps.
- **Chart Setting:** Small multiples on a standard display; static views.
- **Audience:** Analysts using map-based multivariate views.
- **Success Criterion:** Higher accuracy (fewer incorrect correlation judgments).

## When not to follow this preference <!-- role: exceptions -->

**Break it when:** You need cartogram-specific benefits (e.g., emphasizing region size encoding) as a primary requirement of the visualization. **Why:** This guideline only addresses correlation-task performance, not other communication goals that cartograms may serve.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Some thematic emphasis that cartogram deformation can provide.\
**Risk:** If symbol overlap or clutter becomes severe in proportional symbol maps, accuracy gains may not materialize.\
**Mitigation:** Keep symbol sizes and densities within a legible range for the available display size.

## Common mistakes <!-- role: mistakes -->

**Mistake:** Using cartogram small multiples without considering cross-panel location matching. **Why it fails:** Shifting positions across panels can add matching burden that undermines correlation judgments.

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers hesitate because they cannot quickly find the same location across multiple small-multiple panels.\
**Quick Check:** Ask someone to point to the same location in several panels; if they repeatedly search, location matching is a bottleneck.\
**Stronger Test:** Collect error rates on a small set of representative correlation questions for both designs and compare.

## What to do instead if you must use cartograms <!-- role: fix -->

- Use proportional symbol map small multiples for the correlation judgment view, and reserve cartograms for separate communication goals.
- Reduce the number of small-multiple panels shown at once so location re-identification is less frequent.
- Provide a stable reference (e.g., consistent ordering and labeling of locations) to reduce cross-panel matching effort.
