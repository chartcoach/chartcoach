---
id: avoid-pie-charts-for-comparison
title: Avoid Pies for Precise Comparisons
bibliography: references.bib
description: Pie charts are poor tools for comparing the size of shares, especially
  when differences are small.
labels:
- chart:pie
- chart:bar
- task:compare
- visual:perception
- impact:accuracy
---

## The Rule <!-- role: advice -->
Do not use pie charts if you want readers to compare the sizes of different shares, particularly if the differences are small.

## The Logic <!-- role: reason -->
It is difficult for readers to visually compare angles and areas to determine size differences. It is much easier to compare lengths in bar or column charts [@muth_pie_charts_2018].

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing values to rank them or see minor differences.
*   **Data Type:** Values that are numerically close to one another.
*   **Audience:** Readers who need analytical precision.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The differences are massive and obvious (e.g., 90% vs 10%).
*   **Reason:** Visual comparison is not required; the dominance is instant.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the "whole circle" metaphor of 100%.
*   **The Risk:** Readers might not immediately grasp that the values represent parts of a whole without explicit context.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Adding value labels to every slice to force comparison.
*   **Why it fails:** This forces the user to read numbers rather than relying on the visual representation.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are there multiple slices of roughly similar width?
*   **The Test:** Remove the numbers. Can you tell which slice is bigger just by looking?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add explicit data labels (numbers).
*   **Best Fix:** Switch to a bar or column chart [@muth_pie_charts_2018].
