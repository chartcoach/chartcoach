---
id: use-index-charts-to-compare-relative-change-across-time-series-when-baselines-differ
title: Use index charts to compare relative change across time series when baselines
  differ
bibliography: references.bib
description: Normalize multiple time series to a chosen reference point to compare
  percentage change rather than raw levels.
labels:
- chart:line
- task:compare
- visual:position
- impact:clarity
- data:temporal
- audience:general
- complexity:intermediate
---

## Normalize time series to a reference point for growth comparisons <!-- role: advice -->

Use an index chart that normalizes each series to a selected index point when relative change is more meaningful than raw values.

## Normalization makes disparate baselines comparable <!-- role: reason -->

When series have different starting levels, raw-value plots can hide whether a series grew faster or slower; indexing shifts attention to proportional change.

**Mechanism:** Converting values to percent change from a common reference reduces baseline effects and supports direct comparison of growth trajectories.

**Evidence:** Index charts are presented as interactive line charts that show percentage changes for multiple time series based on a selected index point, enabling meaningful comparison when raw values differ [@heerTourVisualizationZoo2010].

**Notes:** The reference point can be user-selected to support exploratory comparison across periods.

## Context: Relative performance over time <!-- role: context -->

- **User Goal:** Compare growth/decline rates across multiple series.
- **Task:** Judge which series changed more since a chosen time.
- **Data:** Multiple quantitative time series with different baseline magnitudes.
- **Chart Setting:** Interactive or annotated time-series display where a reference date can be set or clearly stated.
- **Audience:** Mixed audiences, including non-experts comparing performance.
- **Success Criterion:** Viewers can correctly identify relative change leaders/laggards.

## Exceptions: When raw values are the point <!-- role: exceptions -->

**Break it when:** Absolute levels (not relative change) drive decisions. **Why:** Indexing can obscure the true scale and magnitude of differences in raw values [@heerTourVisualizationZoo2010].

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Absolute magnitude context is reduced when everything is normalized. **Risk:** Viewers may misinterpret indexed values as actual levels. **Mitigation:** Clearly label the index point and units as percent change.

## Mistakes: Common failure modes <!-- role: mistakes -->

**Mistake:** Using an index chart without clearly indicating the index point and what “0%” means. **Why it fails:** Viewers can confuse normalized change with raw value levels [@heerTourVisualizationZoo2010].

## Check: Quick tests <!-- role: check -->

**Failure Sign:** Viewers ask “what was the actual value?” or interpret indexed peaks as the highest absolute value. **Quick Check:** Ask a viewer to explain what the baseline represents; confusion indicates inadequate framing. **Stronger Test:** Have viewers answer both “largest percent increase” and “largest absolute value” to ensure the chart supports only the intended question.

## Fix: What to do instead <!-- role: fix -->

- Pair the index chart with a separate view (or annotation) showing starting levels at the index date.
- Provide a toggle between indexed and raw-value views.
- Use small multiples of raw series when absolute levels must remain visible.
- Add clear labeling that values are percentage change from the chosen reference point.
