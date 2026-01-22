---
id: do-not-assume-more-points-per-class-reduces-mean-comparison-accuracy-in-scatterplots
title: Do not assume that increasing points per class reduces mean-comparison accuracy
  in multiclass scatterplots
bibliography: references.bib
description: "Within tested ranges, increasing the number of points per class did\
  \ not reduce\u2014and may slightly improve\u2014accuracy for mean-comparison tasks\
  \ in multiclass scatterplots."
labels:
- chart:scatter
- task:aggregate
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- complexity:intermediate
---

## Do not reduce point counts just to “protect” mean-comparison accuracy <!-- role: advice -->

Do not assume that showing more points per class will make mean-comparison (aggregate) judgments less accurate in a multiclass scatterplot, at least within moderate point-count ranges.

## Why more points may not harm this aggregation task <!-- role: reason -->

If viewers rely on visual aggregation over sets, adding more samples can preserve the same aggregate signal and may even stabilize the perceived average rather than forcing point-by-point processing.

**Mechanism:** Set-based aggregation can operate over many items without requiring serial inspection of each point, so moderate increases in set size need not degrade mean estimation.

**Evidence:** In an accuracy-based aggregate task, a condition with more points per class (75) did not show worse performance than a condition with fewer points per class (50), and the ordering reported favors the higher-cardinality design in at least one comparison (E-3 over E-1), with no significant pairwise superiority reported for the reverse within those comparisons [@gleicherPerceptionAverageValue2013; @zengReviewCollationGraphical2023].

**Notes:** This guideline is constrained to the tested point-count levels and the specific mean-comparison task.

## When this applies to your scatterplot design <!-- role: context -->

- **User Goal:** Choose which class has the higher mean.
- **Task:** Aggregate (mean comparison).
- **Data:** Many points per class (e.g., tens of points), potentially considering showing more vs. fewer points.
- **Chart Setting:** Static multiclass scatterplot with class membership encoded visually.
- **Audience:** General audiences.
- **Success Criterion:** Preserve or improve accuracy while showing a representative sample.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Increasing point count causes overplotting that prevents seeing distinct marks. **Why:** The evidence assumes points remain visually separable enough to be perceived as a set.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Showing more points can increase visual density. **Risk:** Higher density can make class separation harder if marks overlap heavily. **Mitigation:** Monitor whether individual marks remain distinguishable at the intended display size.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Arbitrarily downsampling classes to very few points to make mean comparison “easier.” **Why it fails:** Lowering point count can remove evidence and may invite non-aggregate strategies that do not reflect the class mean.

## Quick checks before shipping <!-- role: check -->

**Failure Sign:** After adding more points, the plot becomes a solid mass where points are no longer distinguishable. **Quick Check:** Zoom out to the intended reading size; if points merge visually, density is too high. **Stronger Test:** Compare accuracy on a small mean-comparison question set with the lower vs. higher point counts at the final rendered size.

## What to do instead when this fails <!-- role: fix -->

- Increase the plotting area so points remain visually separable.
- Reduce mark size to keep overlaps low while maintaining class visibility.
- If density still overwhelms, show a representative subset but keep enough points to support an aggregate judgment.
