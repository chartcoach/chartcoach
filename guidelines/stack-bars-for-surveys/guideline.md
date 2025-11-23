---
id: stack-bars-for-surveys
title: Use Stacked Bars for Survey Data
bibliography: references.bib
description: Stacked bar charts are space-efficient and standard for Likert scales
  and survey results.
labels:
- chart:stacked-bar
- data:survey
- data:categorical
- task:part-to-whole
- impact:space-efficiency
---

## The Rule <!-- role: advice -->
Use stacked bar charts to visualize survey results, specifically those with Likert scales (e.g., "very satisfied" to "not at all satisfied") or multiple response options.

## The Logic <!-- role: reason -->
Stacked bar charts allow for the comparison of totals and the composition of those totals simultaneously. According to [@muth_chart_types_guide_2025], they are the "best option" for survey results because they display multiple response options effectively and are "nicely space-efficient."

## Where to Apply <!-- role: context -->
*   **User Goal:** summarizing sentiment or survey distribution.
*   **Data Type:** Likert scales or multiple response categories.
*   **Audience:** General readers looking for opinion distributions.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** You want readers to compare the totals of the bars rather than the internal composition.
*   **Reason:** While stacked bars show composition well, grouped column charts (or standard bars) are better if the primary goal is comparing the absolute totals [@muth_chart_types_guide_2025].

## The Price <!-- role: costs -->
*   **The Sacrifice:** It is harder to compare the "middle" segments of the stack across different bars because they do not share a common baseline.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using multiple pie charts.
*   **Why it fails:** Multiple pies are difficult to compare side-by-side compared to the aligned axis of a stacked bar chart.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you using a separate chart for every survey question?
*   **The Test:** Can you stack them to save space and allow easier comparison?

## How to Fix <!-- role: fix -->
*   **Best Fix:** Align the data horizontally in a single stacked bar chart.
