---
id: add-decile-ticks-to-improve-stacked-bar-part-to-whole-estimation
title: Add Decile Tick Marks to Improve Stacked Bar Part-to-Whole Estimation
bibliography: references.bib
description: Adding decile tick cues to a stacked bar reduced estimation error compared
  with both a plain bar and a bar with quartile ticks.
labels:
- chart:stacked-bar
- task:estimate
- visual:length
- visual:annotation
- impact:accuracy
- data:part-to-whole
- audience:general
- detail:internal-ticks
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

If you use a stacked bar for part-to-whole estimation, add internal decile tick marks (10% steps).

## The Logic <!-- role: reason -->

Denser internal reference cues (deciles) help users anchor their estimates, reducing mean absolute error versus a plain bar and versus sparser cues (quartiles).

- **The Principle:** Reference cues (ticks) as anchors improve proportional estimation on length encodings.
- **The Evidence:** In the collated results, bar with decile ticks (E-4) ranks above bar with quartile ticks (E-3) and above baseline bar (E-1), with significant pairwise differences for E-4 over E-3 and E-4 over E-1 [@redmondVisualCuesEstimation2019], as recorded in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Estimating the percent size of a highlighted segment in a two-segment stacked bar.
- **Data Type:** Part-to-whole proportions (percentages).
- **Audience:** General users.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You can add a quantitative scale instead of internal ticks.
- **Reason:** A bar with an explicit scale (E-6) is ranked above the decile-tick bar (E-4) with a significant difference in the study’s comparisons [@redmondVisualCuesEstimation2019], as collated in [@zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** Visual simplicity (more marks/ink inside the bar).
- **The Risk:** Tick density may add clutter in very small chart sizes.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding only quartile ticks (25% steps) and assuming it’s enough.
- **Why it fails:** The decile-tick variant performed significantly better than the quartile-tick variant in the reported rankings [@redmondVisualCuesEstimation2019], as captured by [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users’ estimates “snap” to coarse round values (e.g., 25/50/75) rather than matching varied true values.
- **The Test:** Compare error on a small set of test proportions with and without decile ticks; the study’s metric is mean absolute error [@redmondVisualCuesEstimation2019], and the collation expects decile ticks to reduce error vs. baseline/quartiles [@zengReviewCollationGraphical2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add faint internal tick marks at every 10% along the bar.
- **Best Fix:** If you can afford it, use an external quantitative scale for the bar (see separate guideline) [@redmondVisualCuesEstimation2019; @zengReviewCollationGraphical2023].
