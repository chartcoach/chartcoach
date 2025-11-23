---
id: prioritize-standard-defaults-outlier-accuracy
title: Use Standard Scatterplot Defaults for Accurate Outlier Detection
bibliography: references.bib
description: Standard plotting presets often outperform perceptually optimized designs
  when the goal is the accurate identification of outliers.
labels:
- chart:scatterplot
- task:find-anomalies
- visual:point
- impact:accuracy
- audience:analyst
---

## The Rule <!-- role: advice -->
When the primary goal is the highly accurate detection of outliers in a scatterplot, utilize standard plotting defaults (similar to R or MATLAB presets) rather than aggressively optimizing for perceptual density or speed.

## The Logic <!-- role: reason -->
While perceptual optimization can improve the speed of reading a chart, it may obscure the fine details required to identify anomalies correctly. Experimental results collated by @zeng_review_2023 show that standard defaults (referenced as designs E-2 and E-3, corresponding to MATLAB and R presets) achieved a higher success rate (accuracy) in outlier detection tasks compared to a perceptually optimized algorithm (E-1) @micallef_towards_2017. The standard designs likely preserve singular points better than algorithms that might optimize for aggregate density or structural similarity.

## Where to Apply <!-- role: context -->
*   **User Goal:** identifying specific data points that deviate from the norm (outlier detection).
*   **Data Type:** Quantitative 2D data (Scatterplots).
*   **Audience:** Data analysts or users performing quality control where precision is more valuable than speed.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Time-critical monitoring.
*   **Reason:** If the user needs to spot *potential* issues as fast as possible and can tolerate some false negatives, the perceptually optimized design was found to be significantly faster (see associated speed guideline) @micallef_towards_2017.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Speed.
*   **The Risk:** Users will take significantly longer to complete the task compared to using perceptually optimized designs (E-1 ranked higher for time) @micallef_towards_2017.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Increasing opacity or marker size to make the "main" data look better.
*   **Why it fails:** This often merges outliers into the background noise or clusters, making distinct anomalies harder to separate from the group.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are single points visible distinct from the main cluster, or do they look like rendering artifacts?
*   **The Test:** Verify if a single isolated point (outlier) is clearly distinguishable from a small cluster of 2-3 points.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Revert to the software's default marker size and opacity settings.
*   **Best Fix:** Ensure marker size is small enough and opacity is high enough that individual points do not blend entirely into the background or neighboring clusters.
