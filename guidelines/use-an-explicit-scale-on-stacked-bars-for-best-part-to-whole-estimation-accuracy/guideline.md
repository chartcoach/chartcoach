---
id: use-an-explicit-scale-on-stacked-bars-for-best-part-to-whole-estimation-accuracy
title: Use an Explicit Scale on Stacked Bars for Best Part-to-Whole Estimation Accuracy
bibliography: references.bib
description: Adding an explicit quantitative scale to the stacked bar produced the
  lowest error among the tested bar variants.
labels:
- chart:stacked-bar
- task:estimate
- visual:length
- visual:scale
- impact:accuracy
- data:part-to-whole
- audience:general
- detail:axis
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

When using stacked bars for part-to-whole estimation, include an explicit quantitative scale.

## The Logic <!-- role: reason -->

An explicit scale provides precise reference points that reduce estimation error more than relying on the bar alone or on internal tick cues.

- **The Principle:** Explicit quantitative reference improves precision of length-based estimation.
- **The Evidence:** The collated ranking places bar with scale (E-6) above bar with decile ticks (E-4) and above baseline bar (E-1), with significant differences for E-6 over E-4 and E-6 over E-1 [@redmondVisualCuesEstimation2019], as collated in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Estimating a highlighted segment’s percentage in a two-segment bar.
- **Data Type:** Part-to-whole proportions (percentages).
- **Audience:** General users.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You cannot show an axis/scale due to space or design constraints, but must still use bars.
- **Reason:** In that case, the study indicates internal decile ticks are the next-best tested bar augmentation (ranked above baseline) [@redmondVisualCuesEstimation2019], as compiled in [@zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** More layout space and visual elements (scale/axis).
- **The Risk:** The scale can visually dominate very small multiples or compact dashboard tiles.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using the baseline stacked bar and expecting viewers to infer the percentage precisely from bar length alone.
- **Why it fails:** The bar-with-scale condition was significantly more accurate than the baseline bar in the reported results [@redmondVisualCuesEstimation2019], as captured by [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users disagree on estimates for the same segment size and cluster around rough guesses.
- **The Test:** Add the scale and compare mean absolute error on a small pilot; the study used mean absolute error and found the scaled bar best among tested bar variants [@redmondVisualCuesEstimation2019; @zengReviewCollationGraphical2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a clear 0–100 scale aligned to the bar.
- **Best Fix:** If bars are not required, consider switching to the tested alternative (pie vs. plain bar) when scale cannot be shown [@redmondVisualCuesEstimation2019; @zengReviewCollationGraphical2023].
