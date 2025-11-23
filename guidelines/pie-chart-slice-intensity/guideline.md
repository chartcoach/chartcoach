---
id: pie-chart-slice-intensity
title: Avoid Comparing Similar Large Slices in Pie Charts
bibliography: references.bib
description: Just Noticeable Difference in pie charts follows Weber's Law; larger
  slices require larger differences to be distinguishable.
labels:
- chart:pie
- task:compare
- visual:angle
- visual:area
- impact:readability
- data:part-to-whole
---

## The Rule <!-- role: advice -->
Do not use pie charts if the user needs to distinguish small differences between large segments.

## The Logic <!-- role: reason -->
In pie charts, the JND is governed by the intensity of the stimulus (the angle of the fan), following Weber's Law. This means it is significantly harder to distinguish a difference between two large slices (e.g., 30% vs 32%) than it is to distinguish the difference between two small slices (e.g., 2% vs 4%). Unlike bar charts, the distance between the slices does not significantly affect readability; the size of the slice itself is the limiting factor.

*   **The Principle:** Weber's Law (Object Intensity)
*   **The Evidence:** [@lu_modeling_2022], reviewed in [@zeng_review_2023].

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing proportions or part-to-whole relationships.
*   **Data Type:** Quantitative data summing to a whole.
*   **Audience:** Audiences requiring quick estimation of proportions.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The user only needs to identify the largest category or get a rough overview.
*   **Reason:** If precision isn't the goal, the "whole" context of the pie chart may be more valuable than precise discrimination.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the part-to-whole metaphor provided by the circle.
*   **The Risk:** Users may misinterpret which segment is larger if the values are close and the segments are large.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Moving the slices closer together.
*   **Why it fails:** Research shows angular distance does not improve JND in pie charts. The error comes from the size of the angle itself.

## How to Check <!-- role: check -->
*   **Visual Sign:** Do you have multiple slices that look roughly equal in size (especially if they take up a large portion of the chart)?
*   **The Test:** Remove the data labels. Can you confidently rank the slices from largest to smallest?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add explicit data labels (percentage or value) to resolving ambiguity.
*   **Best Fix:** Switch to a bar chart or dot plot, where comparisons are made on a common linear scale and are not subject to the same intensity-based JND limitations.
