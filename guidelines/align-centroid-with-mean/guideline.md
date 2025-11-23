---
id: align-centroid-with-mean
title: Align Visual Centroid with Arithmetic Mean
bibliography: references.bib
description: Ensure the visual center of mass in a bar chart aligns with the actual
  mean to prevent deceptive perception.
labels:
- chart:bar
- task:estimate-mean
- visual:position
- visual:shape
- impact:accuracy
- data:quantitative
- audience:general
---

## The Rule <!-- role: advice -->
When visualizing distributions (like bar charts) where users must estimate the average, ensure the visual "center of mass" (centroid) of the shape reflects the true arithmetic mean. Do not rely on the data values alone to convey the average if the distribution is heavily skewed.

## The Logic <!-- role: reason -->
The human visual system does not compute the arithmetic mean of bar lengths mathematically. Instead, it extracts "perceptual proxies"—heuristic shortcuts based on visual features. Research identifies the **centroid** (the center of the area occupied by the bars) as the most influential proxy for estimating the mean in bar charts [@ondov_revealing_2021]. If the visual centroid diverges from the mathematical mean (e.g., due to skew or outlier placement), users are statistically likely to misjudge which chart has the higher average, even if the data is accurate.

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing the average value (mean) of two or more data series.
*   **Data Type:** Discrete quantitative data displayed as bar charts or similar aggregate shapes.
*   **Audience:** Users relying on rapid visual estimation rather than reading exact labels.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Precise Reporting.
*   **Reason:** If the goal is to show exact individual values rather than an aggregate summary, and the specific outliers are more important than the average, preserving the raw distribution order is prioritized. However, the perception of the mean will still be biased.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You may need to reorder bars or annotate the chart, which disrupts the natural ordering of data (e.g., alphabetical or time-based sorting).
*   **The Risk:** Users may misinterpret the distribution shape if bars are artificially reordered solely to manipulate the centroid.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** relying solely on the "Amount of Ink" (sum of bar areas).
*   **Why it fails:** While related, the centroid (distribution of that mass) is a stronger predictor of perceived mean than total area alone [@ondov_revealing_2021].
*   **The Wrong Fix:** Assuming "Longest Bar" determines the mean.
*   **Why it fails:** The "max bar" proxy is less influential than the centroid; users can be deceived into thinking a chart with a shorter max bar has a higher mean if the centroid is shifted correctly [@ondov_revealing_2021].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does one chart look "heavier" on the right side, even though its calculated average is lower?
*   **The Test:** Calculate the geometric centroid of the polygon formed by your bars. Compare its horizontal position to the arithmetic mean of the data values. Large discrepancies indicate high potential for deception.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a clear, visible reference line indicating the actual arithmetic mean to override the perceptual proxy.
*   **Best Fix:** Reorder bars to shift the visual bulk (centroid) closer to the true mean, or switch to a summary visualization (like a dot plot with error bars) if individual bar values are secondary to the average.
