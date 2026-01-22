---
id: use-split-space-row-separated-multi-series-for-faster-aggregate-over-time
title: Use split-space row-separated designs for faster aggregate judgments across
  multiple time series
bibliography: references.bib
description: For aggregate judgments over multiple series, split-space row-separated
  designs were fastest in completion time.
labels:
- chart:line
- task:aggregate
- visual:facet
- impact:speed
- data:temporal
- audience:expert
- complexity:intermediate
---

## Split-space row separation for aggregate tasks <!-- role: advice -->

Use a split-space layout that separates series into rows when people must make an aggregate judgment over the series. Prefer row-separated split-space designs over shared-space overlays when speed matters.

## Why row-separated split-space helps for aggregation <!-- role: reason -->

Aggregate judgments over time require scanning and integrating values across the full series, and separating series into distinct bands can reduce interference between series during this scan.

**Mechanism:** Spatial separation reduces visual interference between series, making it easier to track each series’ magnitude pattern when mentally combining information.

**Evidence:** For the aggregate task, row-separated designs (E-3 and E-4) were the fastest group and were significantly faster than the non-row designs (E-1 and E-2). [@javedGraphicalPerceptionMultiple2010] This conclusion is surfaced through a structured collation of graphical perception results for recommendation use. [@zengReviewCollationGraphical2023]

**Notes:** This guideline is about completion time; the accuracy ordering for aggregate differed (row-separated were also top-ranked in accuracy, but the time result is the strongest due to significant pairwise differences).

## When this applies in multi–time series views <!-- role: context -->

- **User Goal:** Decide which series is larger in aggregate (or which aggregate is largest) across the time span shown.
- **Task:** aggregate.
- **Data:** Multiple time series with quantitative values across ordered time; categorical identity per series.
- **Chart Setting:** Static view; viewers must read across the time span rather than a single time point.
- **Audience:** Analysts comparing multiple concurrent series.
- **Success Criterion:** Faster completion time on aggregate judgments.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The viewer must directly compare series values at the same time point repeatedly (local point-by-point comparison). **Why:** The time advantage here was shown for aggregate judgments, not for pointwise comparisons.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Row-separated layouts use more vertical space per series (or reduce per-series height when space is fixed). **Risk:** Very small per-row height can reduce legibility and hurt correctness. **Mitigation:** Keep per-series vertical resolution sufficient for the intended reading precision.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using a shared-space overlay for aggregate tasks because it “shows everything together.” **Why it fails:** In the tested aggregate task, the shared-space design (E-1) was in the slower group compared to row-separated designs.

## Quick tests <!-- role: check -->

**Failure Sign:** Users lose their place while following a single series through time because other series overlap it. **Quick Check:** Ask a viewer to make an aggregate judgment and watch whether they repeatedly re-locate the target series. **Stronger Test:** Measure median completion time for aggregate prompts on both layouts using the same data and number of series.

## What to do instead <!-- role: fix -->

- Separate each series into its own row when the task requires aggregating across time.
- Reduce series overlap by isolating series (e.g., show fewer series at once) if you must stay in shared space.
- Add visual emphasis to help tracking across time (e.g., consistent labeling and clear series identification).
- If space is too constrained, limit the task scope (aggregate fewer series per view) rather than compressing all series into tiny rows.
