---
id: model-jnd-as-distance-sensitive-for-bar-chart-ranking
title: Treat bar-chart discriminability as distance-sensitive when ranking bars
bibliography: references.bib
description: Account for increasing just noticeable difference (JND) with greater
  separation between bars when users must visually rank values.
labels:
- chart:bar
- task:sort
- visual:length
- visual:position
- impact:accuracy
- data:quantitative
- complexity:advanced
---

## Bar-chart ranking: account for separation-driven JND <!-- role: advice -->

When a bar chart is used for sorting, assume that bars become harder to tell apart as the horizontal separation between the compared bars increases. Prefer bar arrangements (or judgments) where close values are compared at short separations.

## Why separation drives bar-chart JND in sorting <!-- role: reason -->

In bar charts, the minimum visually detectable difference between two bar-encoded values can grow with the spatial separation between the bars, meaning “small differences” become less perceptible when items are farther apart. This affects sorting because ranking depends on reliably detecting pairwise differences.

**Mechanism:** Increasing separation distance increases the perceptual threshold needed to notice a difference, so more pairs fall below the Just Noticeable Difference (JND) and become effectively indistinguishable for ranking.

**Evidence:** In bar charts, separation distance showed a statistically significant main effect on JND while bar height (intensity) did not, indicating discriminability depends strongly on distance for this comparison task [@luModelingJustNoticeable2022]. This result is captured as structured graphical-perception knowledge for recommendation-oriented guidelines and constraints [@zengReviewCollationGraphical2023].

**Notes:** This guidance is specifically about perceptual discriminability for pairwise comparisons that underpin sorting, not about any aesthetic preference.

## When this bar-distance JND guideline applies <!-- role: context -->

- **User Goal:** Rank categories by their quantitative values using a bar chart.
- **Task:** Sort.
- **Data:** Quantitative measure by category (nominal grouping).
- **Chart Setting:** Static bar chart with bars positioned along an x-axis by category.
- **Audience:** General audiences, including viewers without specialized visualization training.
- **Success Criterion:** Accurate ordering of categories with similar values.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The sorting decision never requires comparing non-adjacent bars (only local, adjacent comparisons matter). **Why:** Separation-driven JND primarily affects comparisons across larger gaps, so the effect may not influence the intended judgment.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may reduce flexibility in ordering categories if you try to keep potentially comparable values close. **Risk:** Over-emphasizing separation effects can cause over-engineering in situations where differences are large and already well above JND. **Mitigation:** Treat it as a concern mainly when values are close and ranking errors would be costly.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Assuming bar-height differences are equally easy to detect regardless of where the bars sit in the chart. **Why it fails:** The perceptual threshold for noticing differences can increase with separation, making distant, similar bars harder to discriminate during sorting [@luModelingJustNoticeable2022; @zengReviewCollationGraphical2023].

## Quick tests <!-- role: check -->

**Failure Sign:** Users disagree on the ordering of categories with similar bar heights, especially when the bars are far apart.\
**Quick Check:** Pick a few pairs of similar-height bars that are far separated and see if you can confidently judge which is taller at a glance.\
**Stronger Test:** Run a small internal check where readers do a rapid “which is higher?” judgment on separated vs. nearby bar pairs and compare error rates.

## What to do instead <!-- role: fix -->

- Reorder categories so values likely to be compared are placed nearer to each other.
- Add a secondary cue for close values that are hard to discriminate (for example, showing the numeric value for the compared items).
- Switch to a view that supports more reliable ranking when many values are close (for example, a tabular listing of values for precise sorting).
