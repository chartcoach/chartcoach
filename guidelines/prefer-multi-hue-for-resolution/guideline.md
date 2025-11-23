---
id: prefer-multi-hue-for-resolution
title: Use Multi-Hue Scales for Fine-Grained Data Resolution
bibliography: references.bib
description: Select multi-hue scales over single-hue scales when visualizing small
  value differences to improve discriminability.
labels:
- chart:heatmap
- chart:scatterplot
- visual:color-saturation
- visual:color-hue
- task:compare
- impact:precision
- data:quantitative
---

## The Rule <!-- role: advice -->
When visualizing data where small value differences are critical, use a multi-hue scale (varying in both hue and luminance) rather than a single-hue scale.

## The Logic <!-- role: reason -->
While single-hue scales (e.g., Blues) are fast and intuitive for ordering, they suffer from lower resolution. Users struggle to discriminate between small value differences (low spans) in single-hue scales compared to multi-hue scales (e.g., Viridis), which utilize variation in hue to enhance the perceived distance between values.
*   **The Principle:** Color Discrimination Resolution
*   **The Evidence:** Research indicates that single-hue colormaps (E-2) exhibit higher error rates over small data value ranges compared to multi-hue maps (E-5) [@liu_somewhere_2018]. The review by Zeng and Battle highlights that while single-hue is generally good, multi-hue scales provide improved resolution for fine comparisons [@zeng_review_2023].

## Where to Apply <!-- role: context -->
*   **User Goal:** Precision tasks where distinguishing between slight variations in value (small spans) is necessary.
*   **Data Type:** Dense quantitative data where local variance is subtle but important.
*   **Audience:** Analysts or experts requiring detailed data inspection.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Simple Rank/Order Tasks
*   **Reason:** If the user only needs to determine global ordering (high vs. low) without fine precision, single-hue scales (like Blues) are processed slightly faster and are cognitively simpler [@liu_somewhere_2018].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Multi-hue scales introduce more visual complexity than simple single-hue gradients.
*   **The Risk:** If not perceptually uniform, a multi-hue scale can introduce "banding" or false artifacts; however, using verified scales like Viridis mitigates this.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Increasing the contrast of a single-hue scale excessively.
*   **Why it fails:** This often leads to clipping at the ends of the spectrum (too white or too black), making extreme values impossible to read.

## How to Check <!-- role: check -->
*   **Visual Sign:** Can you easily see the boundary between adjacent data points that have very similar values?
*   **The Test:** Zoom in on a region of low variance. If the area looks like a solid block of color despite underlying data differences, the scale lacks resolution.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Change the colormap from a single hue (e.g., "Greens") to a multi-hue ramp (e.g., "Viridis" or "Plasma").
*   **Best Fix:** Adopt a perceptually uniform multi-hue scale that traverses multiple color channels (hue and saturation) to maximize the "just noticeable difference" steps available.
