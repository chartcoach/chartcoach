---
id: prefer-bars-for-average-estimation
title: Use Bars Instead of Lines for Average Estimation
bibliography: references.bib
description: When users need to estimate the average value of a series, bars result
  in more precise judgments than lines.
labels:
- chart:bar
- chart:line
- task:estimate-average
- visual:position
- impact:precision
- audience:general
---

## The Rule <!-- role: advice -->
When the primary user task is estimating the average value of a data series, choose a bar chart over a line chart.

## The Logic <!-- role: reason -->
Research indicates that human position estimation for graphed data is systematically biased. However, the nature of the bias differs by chart type.
*   **The Principle:** Precision vs. Bias. While bar graphs lead to an *overestimation* of the average position (users perceive the average as higher than it is), these estimates are significantly more precise (lower variance) than estimates made on line graphs. Line graphs suffer from *underestimation* and lower precision.
*   **The Evidence:** Experiments showed that "judgments were more precise for bars compared to lines," leading researchers to suggest using bars in the absence of other constraints [@xiong_biased_2020].

## Where to Apply <!-- role: context -->
*   **User Goal:** The user needs to determine the approximate average magnitude of a dataset visually (e.g., "What was the average daily sales volume?").
*   **Data Type:** Discrete or continuous series where the aggregate summary (mean) is a key insight.
*   **Audience:** General audiences relying on visual intuition rather than calculated tooltips.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Trend Analysis.
*   **Reason:** If the goal is to see the shape of change over time rather than the magnitude of the average, lines are generally superior for continuity.
*   **Scenario:** High Data Density.
*   **Reason:** Bars require more pixels and horizontal space; lines are necessary for dense time series.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You risk the user perceiving the values as slightly higher than they truly are (systematic overestimation).
*   **The Risk:** The "ink-to-data" ratio increases, potentially cluttering the display if multiple series are needed.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a line chart to "reduce clutter" when the task is magnitude estimation.
*   **Why it fails:** Users will likely underestimate the average position of the line, perceiving the data as lower in value than reality [@xiong_biased_2020].

## How to Check <!-- role: check -->
*   **Visual Sign:** A line chart is used for a summary task.
*   **The Test:** Ask a user to point to where they think the average height of the line is. If they point too low (below the true mean), consider switching to bars to improve consistency.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a reference line indicating the true mathematical average.
*   **Best Fix:** Convert the visualization to a bar chart if the x-axis resolution allows it.
