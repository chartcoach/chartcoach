---
id: prefer-position-length-over-slope-for-deltas
title: Use Position or Length to Visualize Differences, Not Slope
bibliography: references.bib
description: When visualizing deltas, position (dot plots) and length (bars) outperform
  slope (line segments) for accuracy and speed.
labels:
- chart:dot-plot
- chart:bar-chart
- chart:slope-graph
- visual:position
- visual:length
- visual:slope
- task:aggregate
- task:sort
- impact:accuracy
---

## The Rule <!-- role: advice -->
When visualizing the difference between two data points, use Position encodings (like dot plots) or Length encodings (like bar charts). Avoid using Slope encodings (angled lines/slope graphs) to represent the magnitude of difference.

## The Logic <!-- role: reason -->
Even when differences are explicitly encoded, the type of visual channel matters. Humans perceive position and length more accurately than slope.
*   **The Principle:** Visual Encoding Ranking.
*   **The Evidence:** In the collation by [@zeng_review_2023] of work by [@nothelfer_measures_2020], "Delta Slopes" (E-6) consistently underperformed "Delta Position" (E-2) and "Delta Length" (E-4) in sorting accuracy and filtering time.
*   **Nuance:** For tasks requiring **aggregation** (e.g., finding the average difference), Length encodings (bars) outperformed Position encodings.

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing the magnitude of changes across multiple items or finding the average change.
*   **Data Type:** Quantitative differences (deltas).
*   **Audience:** Users performing quantitative analysis on relationships.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Visualizing time-series trends where "rate of change" is the primary metaphor.
*   **Reason:** Users are culturally conditioned to read "upward slope" as "increase over time," which may aid intuition despite lower perceptual precision for the exact magnitude.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Slope graphs can compactly show the "before" and "after" states connected by a line. Switching to Position/Length delta charts often requires either dropping the absolute values or using a composite chart.
*   **The Risk:** Using bars (Length) for differences can be visually heavy (high ink-to-data ratio) compared to dots (Position).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a slope graph to strictly compare *magnitudes* of change.
*   **Why it fails:** While slope graphs show direction (increase/decrease) well, judging which of two steep slopes is *steeper* is perceptually difficult compared to judging which of two bars is taller.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the chart rely on the angle of lines to convey which change is biggest?
*   **The Test:** Look at the chart. Can you instantly tell if an 80-degree angle is larger than a 75-degree angle? Now compare two bar lengths. The latter should be easier.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add numeric labels to the slopes.
*   **Best Fix:** Convert the slopes into a dot plot (encoding the delta by position on a common scale) or a bar chart (encoding delta by length).
