---
id: prefer-color-over-size-secondary
title: Prefer Color Over Size for Secondary Metrics
bibliography: references.bib
description: When adding a third variable to a scatterplot, use color saturation instead
  of size to minimize interference.
labels:
- chart:scatterplot
- visual:color-saturation
- visual:size
- task:retrieve-value
- impact:clarity
- data:quantitative
---

## The Rule <!-- role: advice -->

When encoding a secondary quantitative variable on a scatterplot (a third dimension), use color saturation rather than mark size.

## The Logic <!-- role: reason -->

Encoding a secondary variable using size interferes with the user's ability to read the primary variables encoded by position. Color saturation creates less visual interference with spatial decoding.
*   **The Principle:** Channel Interference.
*   **The Evidence:** Kim and Heer [@kim_assessing_2018], as reviewed by Zeng and Battle [@zeng_review_2023], found that encodings using size for secondary data (e.g., Designs E-3, E-4) degraded performance in `retrieve-value` tasks compared to encodings using color (e.g., Designs E-1, E-2). The size of the mark obscures the precise center point needed for positional reading.

## Where to Apply <!-- role: context -->

*   **User Goal:** Visualizing multivariate data (3+ variables) where the user still needs to read the X/Y axis values accurately.
*   **Data Type:** Trivariate data (2 primary quantitative, 1 secondary quantitative).
*   **Audience:** Users performing detailed analysis of specific data points.

## When to Break It <!-- role: exceptions -->

*   **Scenario:** When the user has color vision deficiencies and the palette is not accessible, or when the data points are extremely dense (causing occlusion).
*   **Reason:** While color is better for interference, high occlusion in dense plots can make color difficult to perceive for individual points.

## The Price <!-- role: costs -->

*   **The Sacrifice:** Color saturation has lower perceptual resolution than size; users cannot read the precise value of the third variable as easily as they might compare large size differences.
*   **The Risk:** Users may only be able to perceive broad categories (e.g., "low" vs "high") for the colored variable rather than specific values.

## Common Mistakes <!-- role: mistakes -->

*   **The Wrong Fix:** Using "bubble size" to represent a secondary metric because it feels more "quantitative."
*   **Why it fails:** The varying sizes make it harder to align the center of the dot with the axis grid lines, reducing the accuracy of the primary X/Y reading.

## How to Check <!-- role: check -->

*   **Visual Sign:** Do the dots vary in size based on data?
*   **The Test:** Try to determine the exact X-axis value of a very large dot. Is it harder than determining the value of a small dot?

## How to Fix <!-- role: fix -->

*   **Quick Fix:** Change the variable mapping from `size` to `color` (saturation or luminance).
*   **Best Fix:** Ensure the marks are a consistent, uniform size and use a sequential color scale for the secondary metric.
