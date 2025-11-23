---
id: avoid-short-separated-bars
title: Avoid Comparison of Short Separated Bars
bibliography: references.bib
description: Short bars are significantly harder to compare than tall bars when they
  are not adjacent.
labels:
- chart:bar
- task:compare
- visual:length
- impact:precision
- data:quantitative
---

## The Rule <!-- role: advice -->
Scale your axes so that bars are not visually short (e.g., very small pixel heights), especially if those bars are separated by space or other data points.

## The Logic <!-- role: reason -->
The difficulty of comparing bars is not uniform across all bar heights. There is a strong interaction between separation and bar height. While separation makes all comparisons harder, the effect is much larger for short bars (e.g., 125 pixels or less in the study context) than for medium or tall bars.
*   **The Principle:** Relative Size Perception
*   **The Evidence:** Talbot et al. found that for short reference bars, the "Separation Effect" causes a substantial increase in error (adding 0.74 to 0.88 percentage points of error), whereas the effect is much weaker for taller bars [@talbot_four_2014]. Reviews note that data characteristics like value magnitude significantly impact task performance [@zeng_review_2023].

## Where to Apply <!-- role: context -->
*   **User Goal:** Accurate estimation of ratios or differences.
*   **Data Type:** Datasets with small values or charts constrained to small vertical spaces (e.g., sparklines, small multiples).
*   **Audience:** Users viewing dashboards on small screens or dense displays.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Small Multiples (Trellis/Facet charts).
*   **Reason:** Space constraints often force bars to be short. In this case, ensure the comparison is general (trend detection) rather than precise value estimation.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You need more vertical screen real estate to ensure bars are tall enough for accurate reading.
*   **The Risk:** Truncating the Y-axis to make bars "taller" introduces a lie factor, exaggerating differences.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Shrinking the chart height to fit a dashboard layout without considering the data values.
*   **Why it fails:** This compresses the visual signal, making separated comparisons prone to significant error.

## How to Check <!-- role: check -->
*   **Visual Sign:** Do the bars look like small "stubs" or squares rather than elongated rectangles?
*   **The Test:** If the bars occupy less than 15-20% of the available vertical space or are physically small on the screen, they are at risk.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Increase the height of the chart component.
*   **Best Fix:** If values are naturally small, use a zoom-in (without truncating zero if comparing ratios) or switch to a dot plot, which may suffer less from the specific area-related biases of short thick bars.
