---
id: use-small-multiple-proportional-symbol-maps-for-geo-temporal-correlation
title: Use Small-Multiple Proportional Symbol Maps to Identify Geo-Temporal Correlation
  Faster Than Single-Map Bar-Chart Glyphs
bibliography: references.bib
description: For geo-temporal correlation judgments, small-multiple proportional symbol
  maps reduced completion time compared with a single map using bar-chart glyphs.
labels:
- chart:map
- chart:small-multiples
- chart:bar
- task:correlate
- visual:position
- visual:color
- visual:area
- impact:speed
- data:spatiotemporal
- audience:expert
- domain:geospatial
- complexity:advanced
---

## Prefer small-multiple proportional symbol maps over single-map bar-chart glyph maps for correlation speed <!-- role: advice -->

Use small-multiple proportional symbol maps (juxtaposing space) rather than a single map with bar-chart glyphs (juxtaposing time) when your primary goal is faster geo-temporal correlation judgments.

## Why small multiples speed up geo-temporal correlation judgments <!-- role: reason -->

Geo-temporal correlation tasks can become slower when viewers must repeatedly locate and compare the same temporal slices across many separate glyphs distributed over the map. Small multiples reduce this repeated search by presenting comparable views in a consistent, repeated layout, which can lower the time needed to extract the overall correlation judgment.

**Mechanism:** Small multiples reduce repeated within-glyph time-slice lookup across many locations, shifting work toward scanning a set of consistent panels.

**Evidence:** In a controlled experiment comparing three geo-temporal designs, the proportional symbol map as small multiples ranked faster than a single-map design using bar-chart glyphs for correlation tasks, with significant time advantages over the single-map bar-chart glyph design [@pena-arayaComparisonVisualizationsIdentifying2020]. This finding is preserved as structured, machine-actionable comparative knowledge for visualization recommendation scenarios [@zengReviewCollationGraphical2023].

**Notes:** This guideline is about completion time (speed), not about accuracy differences.

## When this applies to geo-temporal correlation work <!-- role: context -->

- **User Goal:** Decide whether two quantitative variables are correlated over space and time.
- **Task:** Correlate (overall correlation judgment across geo-temporal data).
- **Data:** Two quantitative variables over geographic locations and multiple time steps.
- **Chart Setting:** Static map-based views; no assumed interaction for filtering/highlighting.
- **Audience:** Analysts comfortable reading map-based multivariate displays.
- **Success Criterion:** Faster completion time for correlation judgments.

## When not to rely on this speed guideline <!-- role: exceptions -->

**Break it when:** Your primary success criterion is accuracy differences between these designs. **Why:** The extracted evidence does not show significant accuracy separation among the compared designs for the correlation task, so time-based preference may not improve correctness.

## Tradeoffs of small multiples for this task <!-- role: costs -->

**Sacrifice:** Screen space, because small multiples require multiple map panels.\
**Risk:** If display area is constrained, panels may shrink and reduce legibility, potentially eroding the speed advantage.\
**Mitigation:** Ensure each panel remains large enough to support the correlation judgment without zooming or scrolling.

## Common mistakes when applying this guideline <!-- role: mistakes -->

**Mistake:** Switching to small multiples and assuming it will also increase accuracy. **Why it fails:** The extracted results support a time advantage, not a clear accuracy advantage, for the correlation task.

## Quick checks before shipping the design <!-- role: check -->

**Failure Sign:** Viewers spend time hunting for the relevant time segment inside many bar-chart glyphs scattered across the map.\
**Quick Check:** Ask a colleague to answer one correlation question and note whether they repeatedly re-locate the same time step across many locations.\
**Stronger Test:** Run a small timed pilot comparing the two layouts on representative tasks and confirm the small-multiple design reduces median completion time.

## What to do instead if small multiples are not feasible <!-- role: fix -->

- Use a single-map bar-chart glyph design only if you can keep the time-slice lookup effort low for the intended questions (e.g., by reducing time steps shown per glyph).
- Reduce the number of time steps or locations shown at once to decrease the repeated scanning cost in a single-map glyph layout.
- Split the analysis into separate views so the correlation judgment does not require scanning many distributed glyphs on one map.
