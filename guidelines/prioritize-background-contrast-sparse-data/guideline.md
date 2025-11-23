---
id: prioritize-background-contrast-sparse-data
title: Prioritize Background Contrast for Sparse Clusters
bibliography: references.bib
description: Ensure low-density data points have high luminance contrast against the
  chart background.
labels:
- chart:scatter
- visual:color
- visual:luminance
- data:density
- impact:visibility
- task:identify
---

## The Rule <!-- role: advice -->
Assign colors with the highest luminance contrast against the background to data classes that are sparse, widely dispersed, or possess low density.

## The Logic <!-- role: reason -->
Human perception of class separation relies on distinctness and visibility. While dense clusters create their own visual "mass," isolated or sparse points rely entirely on their contrast with the background to be detected.
*   **The Principle:** Point Contrast. High luminance difference between the mark and the background ensures visibility for small visual angles (individual points).
*   **The Evidence:** Wang et al. [@wang_optimizing_2019], as collated by Zeng and Battle [@zeng_review_2023], incorporate "contrast with background" as a weighted factor in their optimization objective, specifically to prevent sparse classes from disappearing.

## Where to Apply <!-- role: context -->
*   **User Goal:** Identifying all classes present in a dataset, including outliers or small groups.
*   **Data Type:** Multiclass scatterplots containing classes with varying densities (e.g., one dense cluster and one sparse trail of points).
*   **Audience:** Analysts who need to ensure no data is overlooked due to poor visibility.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The background is mid-grey.
*   **Reason:** Achieving high luminance contrast for *all* colors is difficult on mid-tone backgrounds; you may need to rely on hue or saturation instead.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You may have to use darker colors (on white backgrounds) for sparse data, which might reduce the number of distinct hues available for the rest of the dense clusters.
*   **The Risk:** Over-emphasizing sparse data (outliers) might draw attention away from the primary dense clusters (the main trends).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using high-saturation, light colors (like Yellow or Cyan) for sparse outliers on a white background.
*   **Why it fails:** These colors have low luminance contrast with white, making individual points nearly invisible [@wang_optimizing_2019].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are there "ghost" points that are hard to see without squinting?
*   **The Test:** Move a single point of that color to an empty white space. Is it immediately obvious, or does it blend in?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Darken the color (lower value/lightness) of the sparse class.
*   **Best Fix:** Calculate the density of each class. Map the lowest density classes to the colors with the highest distance from the background color (e.g., dark purple on white), and reserve lighter colors for high-density clusters.
