---
id: color-scale-continuous-median
title: Anchor Continuous Scales to the Median
bibliography: references.bib
description: For unclassed scales, set the center color to the median to diversify
  colors in skewed data.
labels:
- chart:map
- visual:color
- visual:scale
- data:skewed
- complexity:intermediate
---

## The Rule <!-- role: advice -->
When using an unclassed (continuous) color scale on skewed data, set the center point of your color gradient to the median value of your dataset.

## The Logic <!-- role: reason -->
In a standard linear continuous scale, outliers stretch the gradient so that most values fall into the lightest color range. By defining the median (the 50th percentile) as the center color, you force the gradient to stretch independently for the lower half and the upper half of the data. [@muth_interpolation_2022] calls this a "magic trick" to get more regions to appear darker/colored: you stretch the lower values to cover 50% of the gradient and the higher values to cover the other 50%, ensuring a more diverse use of the available colors.

## Where to Apply <!-- role: context -->
*   **User Goal:** To keep a continuous gradient (no distinct "steps") but avoid the "washed out" look of linear mapping.
*   **Data Type:** Continuous data with a skewed distribution or high outliers.
*   **Audience:** Readers who prefer smooth transitions over distinct buckets.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When you want to show even more granularity than a simple high/low split.
*   **Reason:** Just splitting at the median might still result in large groups of similar colors if the data is clustered in quartiles. In those cases, using quartile or decile interpolation (dividing the gradient into 4 or 10 stretched sections) is more effective [@muth_interpolation_2022].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Linearity. The rate of color change is no longer consistent across the whole scale (it changes speed at the median).
*   **The Risk:** A color change in the lower half of the data might represent a smaller numerical change than a similar color change in the upper half (or vice versa).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a linear continuous scale and just darkening the base color.
*   **Why it fails:** This creates a muddy map where everything looks slightly dark, rather than a map with meaningful contrast.

## How to Check <!-- role: check -->
*   **Visual Sign:** Is the map mostly white/light with only 3% of regions showing color?
*   **The Test:** Check the scale settings. Is the center color handle aligned with the peak of the data histogram? It should be near the dense part of the data (the median), not the mathematical center of the range.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** In your tool's settings, select "Median" or manually set the center value handle to the median value.
*   **Best Fix:** If the median split isn't enough, switch to Quartile interpolation to introduce anchor points at the 25th and 75th percentiles as well.
