---
id: color-scale-linear-interpolation
title: Use Linear Interpolation for Even Distributions
bibliography: references.bib
description: Use linear color mapping for evenly distributed data to maintain truthful
  representation of magnitude.
labels:
- chart:map
- chart:choropleth
- visual:color
- impact:truthfulness
- data:distribution
- audience:general
---

## The Rule <!-- role: advice -->
Choose linear (equi-distant) interpolation when your data values are distributed fairly evenly, or when you specifically intend to highlight extreme outliers against a uniform background.

## The Logic <!-- role: reason -->
Linear interpolation divides the distance between the lowest and highest values into equal steps (for classed scales) or creates a direct linear gradient (for unclassed scales). According to [@muth_interpolation_2022], this is the "most honest" method because it represents the actual numerical distance between values. It ensures that colors are assigned based on absolute magnitude, making it intuitive for readers to understand that the brightest color is the minimum and the darkest is the maximum with a consistent rate of change between them.

## Where to Apply <!-- role: context -->
*   **User Goal:** To show the data "truthfully" or to highlight how distinct outliers are from the norm.
*   **Data Type:** Data with a fairly even distribution (no massive gaps or skew) OR data where outliers are the main story.
*   **Audience:** Readers who need to see raw magnitude differences rather than rank or order.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Data with strong outliers where you want to see variation in the non-outlier values.
*   **Reason:** If one value is extremely high (e.g., 23.5%) and most are low (e.g., 4%), a linear scale will color the vast majority of regions the same light color, hiding all local geographic patterns [@muth_interpolation_2022].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose visibility of regional differences among the majority of the data points.
*   **The Risk:** The map may look "washed out" or empty if a single outlier stretches the scale too far, making most regions indistinguishable from one another.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Keeping linear interpolation on highly skewed data to "be accurate."
*   **Why it fails:** While mathematically accurate, it fails to communicate the distribution or patterns within the main body of the data, rendering the map less useful for understanding regional nuances.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the map look mostly one color (e.g., 90% light yellow) with only one or two dark spots?
*   **The Test:** Check a histogram of the data. If there is a massive gap between the majority of data and the maximum value, linear interpolation is likely hiding information.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Switch to a "Quantile" or "Natural Breaks" interpolation to utilize the full color spectrum.
*   **Best Fix:** Assess if the outliers are the story. If not, use a non-linear interpolation (like Quantiles) to reveal patterns in the bulk of the data.
