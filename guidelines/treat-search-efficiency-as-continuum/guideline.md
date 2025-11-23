---
id: treat-search-efficiency-as-continuum
title: Treat Search Difficulty as a Continuum
bibliography: references.bib
description: Do not categorize visualizations as simply 'parallel' or 'serial'; search
  difficulty increases incrementally with complexity.
labels:
- theory:perception
- task:search
- visual:complexity
- impact:usability
---

## The Rule <!-- role: advice -->
Do not rely on a binary distinction between "instant pop-out" and "slow serial search." Assume that every distractor you add to a visualization imposes a processing cost, which scales along a continuous curve based on the similarity between the target and distractors.

## The Logic <!-- role: reason -->
Historical models divided search into "parallel" (slope ~0ms) and "serial" (steep slopes). However, extensive data proves this dichotomy is false.
*   **The Principle:** Unimodal Distribution of Search Slopes.
*   **The Evidence:** The distribution of search slopes across 2,500 sessions is unimodal. There is no "mythical threshold of 10ms/item" that divides search types. Instead, efficiency varies smoothly from easy feature searches to difficult spatial searches [@wolfe_what_1998].

## Where to Apply <!-- role: context -->
*   **User Goal:** Designing complex dashboards with mixed data types.
*   **Data Type:** High-density displays with varying symbol types.
*   **Audience:** Designers creating heuristics for "good" vs "bad" charts.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Teaching basic concepts to novices.
*   **Reason:** It is sometimes useful to simplify the concept into "pop-out" vs. "serial" for educational purposes, even if the underlying psychophysics is a continuum.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You cannot guarantee a "zero cost" search. Even efficient feature searches have a non-zero slope (cost per item).
*   **The Risk:** Believing a design is "parallel" might lead to overloading the display, assuming the user can handle infinite density as long as the colors are distinct.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Adding more data points to a scatterplot because the target color is "pop-out," assuming the number of distractors doesn't matter.
*   **Why it fails:** Even in efficient searches, slopes are rarely exactly zero. With enough distractors, the cumulative time will eventually impact performance [@wolfe_what_1998].

## How to Check <!-- role: check -->
*   **Visual Sign:** A display that is technically "feature search" based but feels cluttered and slow to read.
*   **The Test:** Measure reaction time as you double the number of items (Set Size). If the reaction time increases linearly, you are paying a cost per item, even if it is small.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Reduce the number of distractor items (Set Size).
*   **Best Fix:** Filter the view. Since all search places a load on the user proportional to the set size, the most effective way to speed up search is to reduce the N (number of items) displayed.
