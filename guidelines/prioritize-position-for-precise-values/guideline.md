---
id: prioritize-position-for-precise-values
title: Prioritize Position Over Size for Precise Value Retrieval
bibliography: references.bib
description: Use positional encodings (scatterplots) rather than size or color when
  users must identify specific values or extremums.
labels:
- chart:scatterplot
- task:retrieve-value
- task:find-extremum
- visual:position
- visual:size
- impact:accuracy
- data:quantitative
---

## The Rule <!-- role: advice -->

Map your primary quantitative variables to spatial position (x/y axes), rather than size or color, when the user needs to read specific values or identify maximums.

## The Logic <!-- role: reason -->

Human perceptual processing decodes spatial position significantly more accurately than area (size) or color saturation when extracting specific numerical values.
*   **The Principle:** Channel Effectiveness and Interference.
*   **The Evidence:** In experiments collated by Zeng and Battle [@zeng_review_2023], Kim and Heer [@kim_assessing_2018] demonstrated that standard scatterplots (using position) consistently outranked sized charts (like bubble charts) for `retrieve-value` and `find-extremum` tasks in terms of accuracy.

## Where to Apply <!-- role: context -->

*   **User Goal:** Reading exact data points (e.g., "What is the sales value for Store A?") or finding the highest/lowest value (e.g., "Which store sold the most?").
*   **Data Type:** Quantitative data variables (ratio or interval).
*   **Audience:** Analysts or general users performing lookup tasks.

## When to Break It <!-- role: exceptions -->

*   **Scenario:** When the primary goal is to show aggregate patterns or summaries rather than individual values.
*   **Reason:** Kim and Heer [@kim_assessing_2018] found that for `aggregate` tasks (like comparing averages), the performance gap narrows, and complex positional plots can sometimes be outperformed or matched by other encodings depending on data distribution.

## The Price <!-- role: costs -->

*   **The Sacrifice:** You are limited to two primary quantitative dimensions (X and Y) for the highest precision.
*   **The Risk:** Adding a third dimension via size or color will result in lower precision for that third variable compared to the spatial ones.

## Common Mistakes <!-- role: mistakes -->

*   **The Wrong Fix:** Using a bubble chart (size encoding) for the most critical variable to make the chart look "engaging."
*   **Why it fails:** Users struggle to accurately compare the areas of circles, leading to errors in identifying which value is actually the maximum or reading the specific value.

## How to Check <!-- role: check -->

*   **Visual Sign:** Is the most important number represented by the size of a bubble?
*   **The Test:** Ask a user to read the exact value of a data point without hovering. If they can't do it easily using the axes, the rule is broken.

## How to Fix <!-- role: fix -->

*   **Quick Fix:** Swap the encoding channels so the most important variable is on the Y-axis or X-axis.
*   **Best Fix:** Switch from a bubble chart to a standard scatterplot or dot plot.
