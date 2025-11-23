---
id: use-shades-not-hues
title: Use Single-Hue Shades for Stacked Categories
bibliography: references.bib
description: Replace multi-colored palettes with shades of a single hue to reduce
  clutter and emphasize totals.
labels:
- chart:stacked-bar
- visual:color
- impact:clarity
- data:part-to-whole
---

## The Rule <!-- role: advice -->
Instead of assigning a different hue (e.g., red, blue, green) to every segment of a stacked bar chart, use darker and lighter variations of the same hue (e.g., light blue to dark blue).

## The Logic <!-- role: reason -->
Using varying hues can make a chart difficult to decipher and visually chaotic. Using shades of a single color creates a cohesive visual unit. However, this shift changes the reader's perception: using shades emphasizes the *total* bar length rather than the individual segments, as the segments blend together more easily [@muth_fewer_colors_2022].

## Where to Apply <!-- role: context -->
*   **User Goal:** The user needs to see the aggregate total primarily, with the breakdown being secondary.
*   **Data Type:** Stacked bar charts or area charts with multiple categories.
*   **Audience:** Readers who might be overwhelmed by high-contrast, multi-color palettes.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The individual parts are as important (or more important) than the total.
*   **Reason:** Shaded categories are harder to distinguish from one another than distinct hues. If precise comparison of the segments is required, distinct hues are necessary [@muth_fewer_colors_2022].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Contrast between adjacent segments is reduced.
*   **The Risk:** Readers may struggle to tell where one segment ends and another begins if the lightness steps are not distinct enough.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a gradient that is too subtle, making the segments indistinguishable.
*   **Why it fails:** The chart becomes a single block rather than a stacked bar.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the chart look cohesive, or does it look like a "confetti party"?
*   **The Test:** Can you easily see the boundary between the lightest and the second-lightest shade?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Convert your categorical color palette to a sequential monochromatic palette.
*   **Best Fix:** Ensure there is sufficient luminance contrast between the shades, or add a thin white stroke between segments to aid differentiation.
