---
id: model-jnd-for-pie-chart-using-segment-angle-intensity
title: Model Pie-Chart Just-Noticeable Differences Using Segment Angle
bibliography: references.bib
description: Treat pie-slice angle (object intensity) as a primary driver of JND when
  users compare slice sizes.
labels:
- chart:pie
- task:sort
- visual:angle
- impact:clarity
- data:quantitative
- audience:general
- perception:jnd
- complexity:advanced
---

## The Rule <!-- role: advice -->

Model pie-chart JND primarily as a function of slice angle (the intensity of the compared segments).

## The Logic <!-- role: reason -->

In the studied pie-chart conditions, JND is strongly driven by the segment angle (intensity), indicating that discriminability changes as slices get larger/smaller.

- **The Principle:** Just Noticeable Difference scales with the intensity of the encoded visual attribute in this chart context.
- **The Evidence:** Lu et al.’s pie-chart experiment (as collated by Zeng & Battle) reports a significant main effect of intensity (slice angle) on JND in pie charts [@zengReviewCollationGraphical2023; @luModelingJustNoticeable2022].

## Where to Apply <!-- role: context -->

- **User Goal:** Sorting/ranking categories by comparing pie-slice sizes.
- **Data Type:** Quantitative values encoded as angles, categories encoded as color hues.
- **Audience:** General audiences doing quick visual comparisons.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are not comparing slice sizes (e.g., you only need to identify categories).
- **Reason:** The collated task context is sorting/comparison; without comparison, JND modeling is not the relevant design driver [@zengReviewCollationGraphical2023; @luModelingJustNoticeable2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** Requires computing or estimating pairwise discriminability thresholds rather than assuming uniform visibility.
- **The Risk:** Over-relying on this rule outside the tested chart/task context could mispredict perceptual difficulty.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Treating all slice differences as equally visible regardless of slice size.
- **Why it fails:** The evidence indicates JND changes with slice angle (intensity) in pie charts [@zengReviewCollationGraphical2023; @luModelingJustNoticeable2022].

## How to Check <!-- role: check -->

- **Visual Sign:** Tiny slices with small differences look indistinguishable, while similar absolute differences may be easier among larger slices.
- **The Test:** Compare pairs of slices at different base angles; if the smallest discernible difference changes with slice size, intensity-based JND modeling is warranted [@zengReviewCollationGraphical2023; @luModelingJustNoticeable2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** If critical comparisons involve small slices, avoid relying on subtle angle differences alone by changing the design intent (e.g., reduce the need for fine-grained ordering).
- **Best Fix:** Implement an angle-based JND model to detect below-JND slice pairs and then apply targeted enhancements only where needed [@zengReviewCollationGraphical2023; @luModelingJustNoticeable2022].
