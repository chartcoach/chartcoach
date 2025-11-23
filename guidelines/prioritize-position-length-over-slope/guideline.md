---
id: prioritize-position-length-over-slope
title: Prioritize Position and Length Over Slope for Relations
bibliography: references.bib
description: When visualizing differences, position (dot plots) and length (bar charts)
  enable faster and more accurate processing than slope (line charts).
labels:
- chart:slope-graph
- chart:bar
- chart:dot-plot
- visual:slope
- visual:position
- visual:length
- impact:accuracy
---

## The Rule <!-- role: advice -->
Use position (e.g., dot plots) or length (e.g., bar charts) encodings to represent relations and differences. Avoid using slope (e.g., line segments) when efficiency and accuracy are paramount.

## The Logic <!-- role: reason -->
While slope is a common way to show change, it is visually less efficient to parse than position or length.
*   **The Principle:** Visual Feature Efficiency. Processing slopes (orientation) is generally slower and more error-prone for magnitude estimation than processing linear displacement or size.
*   **The Evidence:** Search rates were significantly slower for slope encodings than for length or position. Accuracy in proportion tasks was also significantly lower for slopes. Even when directly encoding deltas, position and length yielded 20-50% better performance than slope [@nothelfer_measures_2020].

## Where to Apply <!-- role: context -->
*   **User Goal:** Rapidly scanning a dataset to identify specific changes or estimating the average change across many items.
*   **Data Type:** Multiple data pairs requiring comparison (e.g., 10+ categories with before/after states).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When the dataset is a time series with high continuity constraints.
*   **Reason:** Slope is the standard convention for continuous time-series data (line charts), and breaking this convention might confuse users despite the perceptual inefficiency for discrete comparisons.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Position and length encodings (like floating bars or dot plots) generally take up more horizontal width per item than a thin line segment used in a slope graph.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a "Slope Graph" (two parallel axes connected by lines) when the goal is strictly to compare the *magnitude* of changes across many items.
*   **Why it fails:** Randomly arranged slopes tend to form a texture that is hard to segment, making it difficult to isolate and judge individual changes compared to aligned bars or dots [@nothelfer_measures_2020].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you using angled lines to represent value changes across categorical data?
*   **The Test:** If the user needs to tell if "Category A changed more than Category B," are they comparing the steepness of two angles (hard) or the height of two bars (easy)?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add data labels to the slopes to aid magnitude judgment.
*   **Best Fix:** Convert the slope graph into a dot plot (showing the delta as distance from a baseline) or a bar chart (showing delta as height).
