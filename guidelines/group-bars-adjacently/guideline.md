---
id: group-bars-adjacently
title: Place Compared Bars Adjacently
bibliography: references.bib
description: Minimize the spatial distance between bars that require direct comparison
  to improve accuracy.
labels:
- chart:bar
- task:compare
- visual:position
- impact:accuracy
- audience:general
---

## The Rule <!-- role: advice -->
Place bars that need to be compared immediately next to each other. Do not separate them with unrelated bars or significant white space.

## The Logic <!-- role: reason -->
Separating bars creates a "Separation Effect" that measurably increases the difficulty of estimating height ratios. When bars are separated, the viewer cannot easily make a direct position comparison and must rely on more difficult mental projections.
*   **The Principle:** Spatial Adjacency / Separation Effect
*   **The Evidence:** Experiments by Talbot et al. confirm that separation increases error by roughly 0.6–1 percentage points compared to adjacent bars [@talbot_four_2014]. This finding is collated in recent reviews of graphical perception which highlight that position encodings (like adjacent bars) are top choices for quantitative data [@zeng_review_2023].

## Where to Apply <!-- role: context -->
This advice applies to standard bar charts where specific pairwise comparisons are the user's primary goal.
*   **User Goal:** Comparing the precise difference or ratio between two specific values (e.g., "This Year vs. Last Year").
*   **Data Type:** Quantitative values represented by bar length.
*   **Audience:** Any user performing analytical tasks.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The dataset has a natural ordering (e.g., time series) that dictates position.
*   **Reason:** Breaking the temporal or logical sequence to force adjacency would confuse the overall trend, which is often more important than individual pairwise precision.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You may lose the ability to sort by magnitude or maintain a consistent category order across multiple charts.
*   **The Risk:** If the grouping logic is unclear, users may struggle to find specific categories within the chart.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using gridlines to connect distant bars.
*   **Why it fails:** While gridlines help, Talbot et al. found that visual separation itself is a primary source of error, regardless of intervening distractors or aids [@talbot_four_2014].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are the two most important bars for the user separated by more than the width of a single bar?
*   **The Test:** Ask a user to estimate the ratio between two bars. If they have to trace a line across the screen with their finger or eye, the bars are too far apart.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Reorder (sort) the bars so that relevant comparison targets are neighbors.
*   **Best Fix:** If comparing multiple distinct pairs (e.g., Actual vs. Budget for 5 departments), use a grouped bar chart where the pairs are adjacent, rather than two separate charts or a single interleaved list.
