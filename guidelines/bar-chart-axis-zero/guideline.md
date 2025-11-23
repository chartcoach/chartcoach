---
id: bar-chart-axis-zero
title: Start Bar Chart Axes at Zero
bibliography: references.bib
description: Prevents visual exaggeration of differences between data categories in
  bar charts.
labels:
- chart:bar
- visual:scale
- visual:length
- task:compare
- impact:integrity
- impact:accuracy
---

## The Rule <!-- role: advice -->
Always include zero on the quantitative axis of a bar chart. Do not truncate the y-axis to zoom in on the differences between the bars.

## The Logic <!-- role: reason -->
Truncating the axis alters the visual ratio between the bars, leading to **Message Exaggeration**. When the baseline is removed, users perceive the difference between quantities as significantly larger than the data supports.
*   **The Principle:** Visual Length Encoding
*   **The Evidence:** In a crowdsourced study, @pandey_how_2015 found that truncated axis bar charts led to significantly higher estimates of difference (exaggeration) compared to control charts with zero-baselines, regardless of the user's education level.

## Where to Apply <!-- role: context -->
This applies to any visualization using length to encode quantity, specifically standard bar charts where users compare the magnitude of distinct categories.
*   **User Goal:** Comparing the magnitude of two or more distinct values.
*   **Data Type:** Categorical data with quantitative values.
*   **Audience:** General audiences (even those with high chart familiarity are susceptible).

## When to Break It <!-- role: exceptions -->
The paper focuses on the deceptive nature of this technique; however, outside this specific study context, experts sometimes truncate axes when:
*   **Scenario:** The chart is explicitly measuring deviation from a baseline (not total magnitude).
*   **Reason:** The visual encoding changes from "length" to "position" relative to a reference point.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Small variations between large numbers (e.g., 10,000 vs 10,005) may become visually indistinguishable.
*   **The Risk:** The chart may look "flat" or uninteresting if the differences are minor relative to the total values.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Adding a "break" symbol (zigzag) to the axis while still using bars.
*   **Why it fails:** While technically honest, the visual mass of the bar still triggers the length-comparison cognitive shortcut, leading to the same exaggerated perception.

## How to Check <!-- role: check -->
*   **Visual Sign:** Look at the bottom (or left) of the bars. Does the axis start at a value other than 0?
*   **The Test:** Calculate the ratio of the physical bar lengths. Does it match the ratio of the data values?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Reset the axis minimum to 0.
*   **Best Fix:** If differences are too small to see with a zero baseline, switch chart types. Use a dot plot or a deviation chart that encodes position rather than length.
