---
id: avoid-scrolled-bars-when-speed-matters-for-ranked-list-tasks
title: Avoid Scrolled Barcharts When Speed Matters for Ranked-List Tasks
bibliography: references.bib
description: Scrolled barcharts are consistently slower than non-scrolling ranked-list
  visualizations for ranking, comparison, and average-estimation tasks.
labels:
- chart:bar
- task:rank
- task:compare
- task:aggregate
- impact:speed
- data:quantitative
- audience:general
- domain:ranked-list
---

## The Rule <!-- role: advice -->

Avoid scrolled barcharts when task completion time is a priority; prefer non-scrolling ranked-list visualizations.

## The Logic <!-- role: reason -->

Across the extracted time rankings, scrolled barchart (E-1) is consistently in the slowest group for both “sort” conditions and is slowest for the aggregate (mean) task.

- **The Principle:** Interaction and navigation overhead increases task time.
- **The Evidence:** For time: sort-1 groups E-1 among the slower designs; for sort-2 and aggregate, E-1 is ranked slowest [@mylavarapuRankedListVisualizationGraphical2019]. This empirical pattern is captured for recommender use in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Fast rank lookup, fast two-item comparison, or fast mean/average estimation in long ranked lists.
- **Data Type:** Ranked lists with many items (the study varied list size; designs represent a single quantitative value per item).
- **Audience:** General audiences.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Accuracy is more important than time for the specific task.
- **Reason:** In the extracted accuracy rankings, scrolled barchart is in the top tier for two-item comparison (sort-2) and in the top tier for aggregate accuracy (aggregate), tied with Zvinca [@mylavarapuRankedListVisualizationGraphical2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may lose accuracy advantages for certain tasks (notably two-item comparison and mean estimation).
- **The Risk:** Switching to faster designs (e.g., Zvinca for comparison) can reduce accuracy, depending on task.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping a scrolled barchart and adding more scrolling affordances (e.g., faster scroll) instead of changing the representation.
- **Why it fails:** The study’s timing disadvantages for scrolled barcharts appear in the extracted time rankings for multiple tasks [@mylavarapuRankedListVisualizationGraphical2019].

## How to Check <!-- role: check -->

- **Visual Sign:** Users spend noticeable time navigating (scrolling) before answering.
- **The Test:** Instrument time-on-task; if scrolled barchart time is consistently higher than alternatives for the same prompts, the rule is being violated.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace scrolled barcharts with a non-scrolling alternative (e.g., wrapped bars) in time-critical views.
- **Best Fix:** Offer two modes: a fast non-scrolling view by default, and a scrolled barchart “precision” view when users need the accuracy tradeoff [@mylavarapuRankedListVisualizationGraphical2019; @zengReviewCollationGraphical2023].
