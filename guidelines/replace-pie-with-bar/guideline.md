---
id: replace-pie-with-bar
title: Replace Pie Charts with Bar Charts
bibliography: references.bib
description: Bar charts provide significantly higher accuracy than pie charts for
  data comparison.
labels:
- chart:pie
- chart:bar
- task:compare
- visual:angle
- impact:accuracy
- data:quantitative
---

## The Rule <!-- role: advice -->
Do not use pie charts for comparing values. Use bar charts or dot charts instead.

## The Logic <!-- role: reason -->
Pie charts require the viewer to make judgments based on *angle* (and potentially area), whereas bar charts rely on *position along a common scale*.
*   **The Principle:** Position superiority. Position judgments are more accurate than angle judgments.
*   **The Evidence:** In controlled experiments reported by [@cleveland_graphical_1984] and synthesized by [@zeng_review_2023], bar charts (Design E-1) performed significantly better than pie charts (Design E-6). The bootstrap analysis showed a significant performance difference (at 95% threshold) favoring the bar chart over the pie chart for sorting and comparison tasks.

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing the relative size of parts to the whole or parts to each other.
*   **Data Type:** Categorical data with a quantitative value (proportions or absolute numbers).
*   **Audience:** General audiences who need to accurately rank or compare the segments.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The specific intent is to show a very rough part-to-whole relationship where precision is irrelevant (e.g., "Does this occupy more than 50%?").
*   **Reason:** While less accurate, the metaphor of the "whole" is immediate in a pie chart, though still perceptually inferior for comparison.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the immediate visual metaphor of "a complete circle" representing 100%.
*   **The Risk:** Using a pie chart increases the "log absolute error" in user judgment, leading to incorrect conclusions about which values are larger or by how much [@cleveland_graphical_1984].

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a donut chart to make it look modern.
*   **Why it fails:** Donut charts remove the center angle, often forcing users to judge arc length or area, which are also lower in the perceptual hierarchy than position.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you using a circular chart divided into slices?
*   **The Test:** Can you easily and instantly tell the difference between a slice that is 23% and a slice that is 26%? In a pie chart, this is difficult; in a bar chart, the height difference is obvious.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** List the percentage values directly on the pie slices.
*   **Best Fix:** Convert the data into a bar chart (sorted by value) or a dot plot.
