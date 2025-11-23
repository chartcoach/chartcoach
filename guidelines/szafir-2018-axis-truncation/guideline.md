---
id: szafir-2018-axis-truncation
title: Start Bar Chart Axes at Zero
bibliography: references.bib
description: Prevent misleading comparisons by ensuring bar chart axes start at zero
  to preserve length-based encoding.
labels:
- chart:bar
- visual:position
- visual:length
- impact:accuracy
- task:compare
- bias:truncation
---

## The Rule <!-- role: advice -->
Start the y-axis at zero for bar charts and other length-based visualizations. Do not truncate the axis to the data range.

## The Logic <!-- role: reason -->
People interpret values in bar charts by measuring the distance between the x-axis and the top of the bar (length). When the axis does not start at zero, the ratio of the lengths no longer corresponds to the ratio of the values.
*   **The Principle:** Visual Length Perception.
*   **The Evidence:** [@szafir_good_2018] notes that a 5% difference in data can appear as a 100% difference (one bar twice as big as the other) if the axis is truncated, as shown in their Figure 1.

## Where to Apply <!-- role: context -->
This applies to any visualization where the user interprets value based on the magnitude (length or height) of a mark from a baseline.
*   **User Goal:** Accurate comparison of magnitudes between categories.
*   **Data Type:** Quantitative data displayed via bars or area.
*   **Audience:** General audiences who rely on "glanceability" rather than reading axis labels.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Analyzing variation rather than magnitude in line graphs.
*   **Reason:** For line graphs, analysts may care more about small-scale variations (trends) than the total distance from zero. Truncated axes maximize the space dedicated to these variations [@szafir_good_2018].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Small differences between categories may become difficult to distinguish visually if the total values are large (e.g., comparing 1000 to 1005 on a 0–1100 scale).
*   **The Risk:** Users might miss subtle variations or statistically significant but small effects.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Relying solely on axis labels to correct the visual distortion.
*   **Why it fails:** People seldom read axis labels carefully; the visual "gist" of the shape dominates the conclusion they draw [@szafir_good_2018].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the visual ratio between two bars match the mathematical ratio of their data? (e.g., if bar A is twice as tall as bar B, is the value of A double the value of B?)
*   **The Test:** Check the y-axis origin point. Is it 0?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Force the y-axis range to include 0.
*   **Best Fix:** If the difference is small and important, switch to a chart type that emphasizes change or difference directly (e.g., plotting the delta/growth rate) rather than the raw totals [@szafir_good_2018].
