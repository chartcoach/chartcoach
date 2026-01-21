---
id: avoid-size-encoding-when-users-need-accurate-means-in-scatterplots
title: Avoid Size Encoding When Users Must Estimate Mean Position
bibliography: references.bib
description: Size-varying scatterplots (bubble charts) increase mean-position error
  and bias, especially when size correlates with position.
labels:
- chart:scatter
- task:aggregate
- visual:position
- visual:area
- impact:accuracy
- impact:bias
- data:quantitative
- audience:general
- risk:weighted-average-illusion
---

## The Rule <!-- role: advice -->

Do not encode a third quantitative variable with mark size/area in scatterplots when users need to estimate the mean (average) position of the points.

## The Logic <!-- role: reason -->

- **The Principle:** Salient marks (larger) receive disproportionate perceptual weight in ensemble averaging, pulling the perceived mean toward them.
- **The Evidence:** In the collated experiment results, size/area-encoded designs (E-10–E-18) generally rank worse for aggregate-task accuracy and show higher bias than comparable lightness-encoded designs (E-1–E-9), with many significant pairwise differences; this pattern is summarized for visualization recommendation use in [@zengReviewCollationGraphical2023] based on [@hongWeightedAverageIllusion2022].

## Where to Apply <!-- role: context -->

- **User Goal:** Estimating or comparing the average (mean) x/y position of a point cloud.
- **Data Type:** Quantitative x and y positions with an additional quantitative variable that could be mapped to size.
- **Audience:** General audiences (or any audience) performing aggregate judgments.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The user is not doing mean-position estimation (i.e., aggregate task is not required).
- **Reason:** The evidence provided here is specific to aggregate (mean-position) performance; it does not establish harm for other tasks [@hongWeightedAverageIllusion2022; @zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** You lose a common way to show a third quantitative dimension (bubble size) in the same scatterplot.
- **The Risk:** You may need additional views or encodings, increasing complexity or space.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** “Use bubble charts but just make the range tasteful.”
- **Why it fails:** Even with narrower size ranges, size-encoded designs still appear among worse bias rankings compared to several lightness designs, and size conditions were significantly worse than baseline in error (as summarized in the extracted results) [@hongWeightedAverageIllusion2022; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** The visually “heavier” region (larger points) seems to define where “average” lies.
- **The Test:** Temporarily remove size encoding (make all points equal size) and see whether the perceived “center of mass” shifts.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Keep the scatterplot but make all marks a constant size (drop the area encoding).
- **Best Fix:** Use a size-invariant scatterplot and show the third quantitative variable through a different representation (e.g., separate view), if mean judgments are central [@hongWeightedAverageIllusion2022; @zengReviewCollationGraphical2023].
