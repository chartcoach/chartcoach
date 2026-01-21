---
id: model-jnd-for-bar-chart-separation-distance
title: Model Bar-Chart Just-Noticeable Differences Using Separation Distance
bibliography: references.bib
description: Treat bar-to-bar separation distance as a primary driver of just-noticeable
  differences (JND) when users compare bar heights.
labels:
- chart:bar
- task:sort
- visual:length
- visual:position
- impact:clarity
- data:quantitative
- audience:general
- perception:jnd
- complexity:advanced
---

## The Rule <!-- role: advice -->

Model the just-noticeable difference (JND) for bar comparisons as a function of the separation distance between the two bars.

## The Logic <!-- role: reason -->

When comparing bars, the minimum discriminable difference depends strongly on how far apart the bars are: as separation increases, the JND increases.

- **The Principle:** Just Noticeable Difference depends on chart context (distance between compared elements).
- **The Evidence:** The collation by Zeng & Battle records Lu et al.’s empirical finding that separation distance has a significant main effect on JND in bar charts [@zengReviewCollationGraphical2023; @luModelingJustNoticeable2022].

## Where to Apply <!-- role: context -->

- **User Goal:** Sorting/ranking categories by value using bars.
- **Data Type:** Quantitative values by nominal categories.
- **Audience:** General audiences making visual comparisons.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are not doing a comparison/sorting task.
- **Reason:** The reported task context in the collated knowledge is sorting; this guideline is scoped to that context [@zengReviewCollationGraphical2023; @luModelingJustNoticeable2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** Requires tracking/estimating pairwise distances (extra logic/compute for a recommender or QA check).
- **The Risk:** If you apply a distance-based JND rule to a different task, you may mis-prioritize which differences matter.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming a single fixed JND threshold for all bar comparisons.
- **Why it fails:** The evidence indicates JND varies with separation distance in bar charts [@zengReviewCollationGraphical2023; @luModelingJustNoticeable2022].

## How to Check <!-- role: check -->

- **Visual Sign:** Bars that look “almost the same” become harder to tell apart when they are far apart in the chart.
- **The Test:** Compare the same two values when bars are adjacent vs. widely separated; if discriminability changes, a distance-dependent JND model is needed [@zengReviewCollationGraphical2023; @luModelingJustNoticeable2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reorder bars so key comparisons are closer together (reducing separation distance).
- **Best Fix:** Use an explicit distance-based JND model to detect below-JND bar pairs and trigger an enhancement workflow (e.g., selective cues) [@zengReviewCollationGraphical2023; @luModelingJustNoticeable2022].
