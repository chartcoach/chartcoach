---
id: visualize-scale-irregularities
title: Visually Represent Uneven Scales
bibliography: references.bib
description: Adjust the width or design of key segments to reflect non-linear interpolations
  or uneven data ranges.
labels:
- visual:accuracy
- visual:scale
- data:quantitative
- impact:truthfulness
---

## The Rule <!-- role: advice -->
If your color scale uses non-linear interpolation or unequal class sizes, reflect this in the design of the key (e.g., different segment widths) or explicitly label the min/max of the distorted ranges.

## The Logic <!-- role: reason -->
If one color class covers a range of 0–50 and the next covers 50–1000, visually representing them as equal-sized blocks is misleading. Readers assume equal visual weight implies equal data range. By giving classes different widths in the key corresponding to their range, or by labeling the extremes of irregular classes, you communicate the interpolation truthfully [@muth_color_keys_2023].

## Where to Apply <!-- role: context -->
*   **User Goal:** Correctly interpreting the magnitude of data differences.
*   **Data Type:** Logarithmic scales, quantile scales, or diverging scales where the "center" is not mathematically central (e.g., a scale from -5 to +100).
*   **Audience:** Analytical readers who need to understand the distribution logic.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Strict space constraints.
*   **Reason:** Variable-width keys can become very wide; if space is tight, explicit text labeling is a safer fallback than visual sizing.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Aesthetics. Variable-width keys look jagged and less "clean" than uniform blocks.
*   **The Risk:** Complexity. Readers unfamiliar with the data might be confused by the varying sizes if not explained.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using equal-sized blocks for a scale that doubles at every step (log scale) without labeling the "0" or the upper bounds.
*   **Why it fails:** Readers assume a linear progression and misinterpret the data values.

## How to Check <!-- role: check -->
*   **Visual Sign:** A symmetric diverging key (e.g., Blue to Red) where Blue represents -5 and Red represents +40.
*   **The Test:** Check the mathematical range of your first class versus your last class. Are they vastly different? If yes, does the key look uniform? That's a mismatch.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Explicitly label the start and end values of every class, especially the irregular ones.
*   **Best Fix:** Design the key segments to have different widths proportional to the range they cover, or make the key asymmetrical around the zero point.
