---
id: ordered-data-saturation-luminance
title: Use Saturation or Luminance for Ordered Data
bibliography: references.bib
description: Use saturation or luminance ramps for quantitative and ordinal data to
  communicate magnitude.
labels:
- chart:heatmap
- chart:choropleth
- visual:color-saturation
- visual:luminance
- data:quantitative
- data:ordinal
- task:compare
- impact:accuracy
---

## The Rule <!-- role: advice -->
Map quantitative or ordinal data to color saturation or luminance (lightness). Avoid using a multi-hue spectrum (like the rainbow colormap) for ordered data unless it is perceptually uniform.

## The Logic <!-- role: reason -->
Quantitative and ordinal data possess an inherent order and magnitude.
*   **The Principle:** **Monotonicity and Natural Order.** Humans naturally perceive changes in brightness (luminance) and intensity (saturation) as ordered magnitude (darker/more saturated = "more") [@bujack_good_2018].
*   **The Evidence:** Theoretical frameworks confirm that Saturation (CS) and Luminance are expressive for Quantitative (T-4) and Ordinal (T-6) data [@zeng_review_2023]. Pure Hue (CH) often lacks an intuitive order (e.g., is red "more" than green?), and traditional multi-hue maps like the rainbow scale lack perceptual uniformity, leading to false artifacts and interpretation errors [@bujack_good_2018].

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing the magnitude of values (e.g., temperature, population density, Likert scales).
*   **Data Type:** Quantitative (continuous) or Ordinal (ranked) data.
*   **Audience:** Analysts looking for trends, clusters, or outliers in dense data.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Cyclic Data (e.g., angle, time of day, phase).
*   **Reason:** Hue is naturally cyclic (red transitions back to red on a color wheel), making it appropriate for data that wraps around.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Reduced number of distinguishable bins compared to a multi-hue scale. The human eye can distinguish fewer steps of saturation than differences in hue.
*   **The Risk:** Losing visibility of data structure if the contrast range is too narrow or if the display has poor gamma calibration.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a standard "Rainbow" colormap (Jet) to show magnitude.
*   **Why it fails:** It introduces "Mach bands" (perceptual artifacts), lacks natural order (yellow often appears brightest, confusing the high/low end), and is not safe for color-blind users [@bujack_good_2018].

## How to Check <!-- role: check -->
*   **Visual Sign:** Convert the visualization to grayscale.
*   **The Test:** If the visualization becomes unreadable or the gradient is not monotonic (e.g., it gets light, then dark, then light again), the encoding is flawed.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Switch to a single-hue sequential palette (e.g., light blue to dark blue).
*   **Best Fix:** Use a perceptually uniform multi-hue sequential palette (like Viridis or Magma) which varies both hue and luminance simultaneously but monotonically [@bujack_good_2018].
