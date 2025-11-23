---
id: use-parallel-coordinates-for-change-detection
title: Use Parallel Coordinates to Detect Changes Across Attributes
bibliography: references.bib
description: Parallel coordinates outperform scatterplots and tables for identifying
  changes across ordered attributes.
labels:
- chart:parallel-coordinates
- chart:scatterplot
- task:change-detection
- task:correlate
- visual:position
- data:multivariate
---

## The Rule <!-- role: advice -->
When users need to identify changes across ordered attributes (such as temporal sequences or progressive categories), use Parallel Coordinates Plots (PCP) rather than Scatterplots (SP) or Data Tables.

## The Logic <!-- role: reason -->
Parallel Coordinates Plots are significantly more effective for change detection because they physically connect data points across axes with lines. This allows the user to visually track the "flow" or delta of a single entity across multiple dimensions instantly. Experimental results collated by [@zeng_review_2023] from the study by [@kanjanabose_multi-task_2015] show that Parallel Coordinates ranked highest for change detection tasks, outperforming both Scatterplots and Data Tables in terms of accuracy and response time.

*   **The Principle:** Visual Continuity and Slope Perception.
*   **The Evidence:** [@kanjanabose_multi-task_2015]; [@zeng_review_2023]

## Where to Apply <!-- role: context -->
*   **User Goal:** Identifying which items changed the most or followed a specific trend across multiple steps.
*   **Data Type:** Multivariate data where the axes have a meaningful order (e.g., time steps `t1, t2, t3` or logical progression `input -> process -> output`).
*   **Audience:** Analysts looking for trends or deviations in flow.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The attributes have no logical order and the relationships are purely pairwise correlations.
*   **Reason:** Without ordered axes, the "change" (slope) between axes is semantically meaningless, and Scatterplots may be more intuitive for simple pairwise correlation [@kanjanabose_multi-task_2015].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Ease of learning. Parallel Coordinates are often perceived as less intuitive to novice users compared to standard Scatterplots.
*   **The Risk:** Visual Clutter. If the dataset is extremely large, the lines in a PCP can overlap (overplotting), making individual trend lines hard to trace without interaction (brushing/filtering).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a series of small multiple Scatterplots (Scatterplot Matrix) to track changes.
*   **Why it fails:** The user must mentally link a point in one plot to the corresponding point in the next plot, increasing cognitive load compared to following a single connected line in a PCP.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you asking the user to compare values between Axis A and Axis B to see how much they differ?
*   **The Test:** Ask, "Can I immediately see which item increased the most from step 1 to step 2 without reading the numbers?" If not, consider Parallel Coordinates.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Connect the dots in your scatterplot if the x-axis represents the ordered attribute (converting it to a line chart).
*   **Best Fix:** Switch to a Parallel Coordinates Plot where each vertical axis represents a step in the sequence.
