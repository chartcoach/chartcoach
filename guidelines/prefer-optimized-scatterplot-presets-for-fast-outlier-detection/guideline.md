---
id: prefer-optimized-scatterplot-presets-for-fast-outlier-detection
title: Use Optimized Scatterplot Presets to Speed Up Outlier Detection
bibliography: references.bib
description: For outlier-finding tasks in scatterplots, use a perceptually optimized
  design preset to reduce completion time versus common fixed defaults.
labels:
- chart:scatter
- task:find-anomalies
- visual:position
- impact:speed
- data:quantitative
- audience:novice
- source:literature-collation
- complexity:advanced
---

## The Rule <!-- role: advice -->

When users need to find outliers in a scatterplot, use a perceptually optimized scatterplot design preset (algorithm-generated) rather than relying on fixed defaults.

## The Logic <!-- role: reason -->

Optimizing scatterplot design parameters (within the same scatterplot chart type and position encodings) can reduce the time it takes users to spot outliers.

- **The Principle:** Task-tuned scatterplot design can improve operational efficiency (time) without changing the underlying encodings.
- **The Evidence:** In the collated evaluation, the algorithm-generated scatterplots (E-1) were fastest for the *find-anomalies* task, significantly faster than MATLAB (E-2), R (E-3), and a prior-study design (E-4) [@micallefPerceptualOptimizationVisual2017]. This finding is captured and organized for recommendation use in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly identifying outliers/anomalies in a bivariate scatterplot.
- **Data Type:** Two quantitative variables (positionX + positionY with linear scales).
- **Audience:** Especially useful when users depend on defaults/presets (e.g., novices or time-constrained analysts).

## When to Break It <!-- role: exceptions -->

- **Scenario:** Outlier detection accuracy is the top priority and you cannot tolerate a possible accuracy drop.
- **Reason:** For *find-anomalies* accuracy, MATLAB and R designs (E-2/E-3) ranked above the algorithm-generated design (E-1) [@micallefPerceptualOptimizationVisual2017], as collated in [@zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may trade off outlier-detection accuracy against speed.
- **The Risk:** Using an optimized preset tuned for speed may lead to more missed or incorrectly identified outliers than common fixed defaults in some settings [@micallefPerceptualOptimizationVisual2017].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming any scatterplot default is “good enough” for outlier detection.
- **Why it fails:** Fixed defaults (e.g., MATLAB/R/older-study settings) were slower than the optimized design for the outlier task in the reported comparison [@micallefPerceptualOptimizationVisual2017], as organized in [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users hesitate or take long to confirm which points are outliers.
- **The Test:** A/B test an optimized preset versus your current default with a timed outlier-finding task; if completion time is notably higher with the default, you are likely violating this rule (time differences were significant in the cited study) [@micallefPerceptualOptimizationVisual2017; @zengReviewCollationGraphical2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch your scatterplot “outlier” preset from a fixed default (e.g., MATLAB/R-like) to an optimized preset for that task.
- **Best Fix:** Implement task-aware scatterplot design selection (choose an optimized preset specifically for outlier finding) and expose it as the default for outlier workflows, as suggested by the collated recommendation framing in [@zengReviewCollationGraphical2023] based on [@micallefPerceptualOptimizationVisual2017].
