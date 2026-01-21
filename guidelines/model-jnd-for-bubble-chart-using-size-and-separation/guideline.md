---
id: model-jnd-for-bubble-chart-using-size-and-separation
title: Model Bubble-Chart Just-Noticeable Differences Using Size and Separation
bibliography: references.bib
description: Treat both bubble size (intensity) and bubble-to-bubble distance (separation)
  as significant drivers of JND.
labels:
- chart:bubble
- task:sort
- visual:area
- visual:position
- impact:clarity
- data:quantitative
- audience:general
- perception:jnd
- complexity:advanced
---

## The Rule <!-- role: advice -->

Model bubble-chart JND using both object intensity (bubble size) and separation distance between the two compared bubbles.

## The Logic <!-- role: reason -->

In bubble charts, discriminability depends on both how large the bubbles are and how far apart they are: both variables show significant main effects on JND in the experiment.

- **The Principle:** JND in spatial displays can be jointly driven by intensity and spatial separation.
- **The Evidence:** Lu et al.’s bubble-chart experiment (as collated by Zeng & Battle) reports significant main effects of both intensity (radius) and distance on JND [@zengReviewCollationGraphical2023; @luModelingJustNoticeable2022].

## Where to Apply <!-- role: context -->

- **User Goal:** Sorting/ranking by comparing bubble sizes.
- **Data Type:** Quantitative values encoded as bubble size; items positioned in 2D space with categorical identity via color hue.
- **Audience:** General audiences.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Users are not comparing sizes (e.g., they only need to locate items).
- **Reason:** The collated task context is sorting/comparison, so the rule is scoped to comparison-driven reading [@zengReviewCollationGraphical2023; @luModelingJustNoticeable2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** More complex JND estimation (must account for both size and distance).
- **The Risk:** Applying this model outside the tested chart setup could misestimate JND.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Modeling JND from bubble size alone, ignoring spacing.
- **Why it fails:** The evidence indicates both distance and intensity matter for bubble-chart JND [@zengReviewCollationGraphical2023; @luModelingJustNoticeable2022].

## How to Check <!-- role: check -->

- **Visual Sign:** Two similarly sized bubbles are harder to compare when farther apart; and the smallest visible difference changes as bubbles get larger/smaller.
- **The Test:** Compare discriminability across (a) same size, different distances and (b) same distance, different sizes; if both change, you need a two-variable model [@zengReviewCollationGraphical2023; @luModelingJustNoticeable2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce distance for key comparisons and avoid relying on very small size differences for large bubbles.
- **Best Fix:** Implement a JND detector for bubble charts that uses both bubble size and separation distance, and only then decide whether to add targeted enhancements for below-JND pairs [@zengReviewCollationGraphical2023; @luModelingJustNoticeable2022].
