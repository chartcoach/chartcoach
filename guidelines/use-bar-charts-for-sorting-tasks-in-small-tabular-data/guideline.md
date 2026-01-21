---
id: use-bar-charts-for-sorting-tasks-in-small-tabular-data
title: Use Bar Charts for Sorting Tasks
bibliography: references.bib
description: For ordering/sorting items by value in small datasets, bar charts ranked
  best in accuracy, time, and preference in the experiment.
labels:
- chart:bar
- task:sort
- visual:length
- impact:efficiency
- data:categorical
- audience:general-public
- source:empirical
---

## The Rule <!-- role: advice -->

Use a bar chart when the task is to sort or rank items by a quantitative value.

## The Logic <!-- role: reason -->

- **The Principle:** Ranking is supported by quick comparisons of lengths aligned to a common baseline.
- **The Evidence:** For the **sort** task, bar-chart designs ranked highest in **accuracy**, ranked fastest in **time**, and ranked highest in **user preference** relative to the other tested visualization types [@saketTaskBasedEffectivenessBasic2019]. This evidence is included in the collation used to derive recommendation guidance [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Put categories/items in order from largest to smallest (or similar).
- **Data Type:** Small tabular datasets summarized as one value per category (5–34 marks).
- **Audience:** General public / mixed-expertise users.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The ranking is across two quantitative variables simultaneously (multi-criteria ranking).
- **Reason:** The evidence here is for the experiment’s sort task and does not cover multi-criteria ranking behavior [@saketTaskBasedEffectivenessBasic2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** Bar charts prioritize one quantitative measure at a time.
- **The Risk:** If there are many categories, sorting may require additional interaction (not covered by the study’s static setting).

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a pie chart to rank slices by size.
- **Why it fails:** Pie designs were consistently lower-ranked than bars for sorting in the experiment, including time and preference [@saketTaskBasedEffectivenessBasic2019; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users must read labels/values to compare items rather than visually scanning bar lengths.
- **The Test:** If users can’t confidently name the top-3 ordering without reading many numbers, switch to bars (aligned with the study’s top ranking for sort) [@saketTaskBasedEffectivenessBasic2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Convert the view to a bar chart and order bars by value.
- **Best Fix:** Use a bar chart as the primary view for sorting tasks, matching the experiment’s best-performing visualization type for sort by accuracy, time, and preference [@saketTaskBasedEffectivenessBasic2019; @zengReviewCollationGraphical2023].
