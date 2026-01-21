---
id: use-bar-charts-for-finding-extrema-in-small-tabular-data
title: Use Bar Charts for Finding Extremes
bibliography: references.bib
description: For finding maximum/minimum values in small datasets, bar charts ranked
  highest in time and user preference in the experiment.
labels:
- chart:bar
- task:find-extremum
- visual:length
- impact:efficiency
- data:quantitative
- audience:general-public
- source:empirical
---

## The Rule <!-- role: advice -->

Use a bar chart when the task is to find an extreme (max/min) value.

## The Logic <!-- role: reason -->

- **The Principle:** Extremum finding is supported by rapid scanning for the longest/shortest mark.
- **The Evidence:** For **find-extremum**, bar-chart designs ranked best in **time** and ranked highest in **user preference** among the tested types [@saketTaskBasedEffectivenessBasic2019]. The collation includes this paper as evidence for task-driven recommendations [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Identify which item has the highest/lowest value.
- **Data Type:** Small tabular datasets summarized into 5–34 bars.
- **Audience:** General public / mixed-expertise users.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The extremum is defined over a 2D relationship (e.g., “highest y at a given x range”) rather than over a single value per item.
- **Reason:** The evidence here is for extremum tasks as implemented in the experiment; it does not cover all extremum definitions [@saketTaskBasedEffectivenessBasic2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may lose additional context (e.g., relationship patterns) compared with a scatter/line view.
- **The Risk:** If values are very close, users may need labels to distinguish the top items.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a pie chart to find the “largest slice” as the extremum display.
- **Why it fails:** In the experiment, pie designs were slowest for find-extremum compared with bars [@saketTaskBasedEffectivenessBasic2019], which is part of the collated evidence [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users hesitate between multiple candidates because the encoding makes “largest” ambiguous.
- **The Test:** Time a quick extremum question; if users take longer than expected while scanning labels, try a bar chart baseline scan (supported by best time ranking) [@saketTaskBasedEffectivenessBasic2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch to a bar chart sorted descending by value.
- **Best Fix:** Use a bar chart as the primary view for extremum tasks, consistent with the experiment’s top time and preference rankings [@saketTaskBasedEffectivenessBasic2019; @zengReviewCollationGraphical2023].
