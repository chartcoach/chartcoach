---
id: prefer-mirrored-over-adjacent-for-correlation-in-bar-chart-small-multiples
title: Mirror Bar-Chart Small Multiples for Correlation Comparisons
bibliography: references.bib
description: For correlation judgments between two bar-chart series, mirrored small
  multiples outperform standard adjacent or stacked layouts.
labels:
- chart:bar
- task:correlate
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- comparison:between-series
- layout:mirrored
---

## The Rule <!-- role: advice -->

When asking viewers to judge which pair of bar charts is more correlated (more “similar”), use a **mirrored** small-multiples arrangement rather than standard **adjacent** or **stacked** bar-chart small multiples.

## The Logic <!-- role: reason -->

Mirroring places corresponding elements in a symmetry relationship, which can make differences and similarity structure easier to compare than translated (non-mirrored) layouts. This guideline is extracted via the collation in [@zengReviewCollationGraphical2023] from experimental results in [@ondovFaceFaceEvaluating2019] showing better performance for mirrored than adjacent layouts on the correlation task.

## Where to Apply <!-- role: context -->

- **User Goal:** Decide which of two series-pairs shows stronger correlation/similarity.
- **Data Type:** Two series of **quantitative** values with aligned categories; viewers compare similarity patterns across the two charts.
- **Audience:** General audiences performing quick similarity judgments.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You need a layout that scales naturally beyond comparing exactly two series at a time.
- **Reason:** Mirroring is inherently tied to a two-sided comparison metaphor and may be harder to extend cleanly to many series [@ondovFaceFaceEvaluating2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less conventional layout than standard adjacent small multiples.
- **The Risk:** Some viewers may find the mirrored axis direction less familiar, increasing interpretation friction in some contexts [@ondovFaceFaceEvaluating2019].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using stacked small multiples for correlation comparison because the baselines align.
- **Why it fails:** In the correlation experiment, stacked performed worse than other layouts, while mirrored was better than adjacent [@ondovFaceFaceEvaluating2019], as summarized in [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** People struggle to judge similarity and instead focus on individual bar heights.
- **The Test:** Ask users to pick the more correlated pair under a brief viewing time; if accuracy is low, try switching from adjacent/stacked to mirrored [@ondovFaceFaceEvaluating2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Convert adjacent small multiples into a mirrored arrangement (reverse one side so corresponding categories face each other).
- **Best Fix:** Use mirrored small multiples for correlation judgments and reserve other layouts for other tasks, reflecting the task-dependent outcomes emphasized in [@zengReviewCollationGraphical2023] and demonstrated in [@ondovFaceFaceEvaluating2019].
