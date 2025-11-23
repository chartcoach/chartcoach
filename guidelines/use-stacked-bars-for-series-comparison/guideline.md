---
id: use-stacked-bars-for-series-comparison
title: Use Stacked Bars to Compare Multiple Totals
bibliography: references.bib
description: Avoid using multiple pie charts to compare different datasets (e.g.,
  two polls). Use stacked bars instead.
labels:
- chart:pie
- chart:stacked-bar
- task:compare
- data:multivariate
---

## The Rule <!-- role: advice -->
Do not use multiple pie charts to compare two different totals (e.g., two different polls). Use a stacked bar chart instead.

## The Logic <!-- role: reason -->
A single pie chart can only show one total and its shares. Comparing shares across multiple pie charts is cognitively difficult. Stacked bars align the shares linearly, making comparison easier [@muth_pie_charts_2018].

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing the composition of two different groups or time periods.
*   **Data Type:** Categorical data across multiple series (e.g., Poll A vs Poll B).
*   **Audience:** Analytical readers.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** You want to emphasize the distinctness of the two groups rather than compare them directly.
*   **Reason:** Separate pies create visual isolation.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the "part-to-whole" circle metaphor for each individual group.
*   **The Risk:** Stacked bars can sometimes be hard to compare if the middle segments shift baseline, but it is still generally better than comparing angles across two circles.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Placing two pie charts side-by-side.
*   **Why it fails:** The reader has to ping-pong their eyes back and forth to compare angles.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are there two or more circles next to each other?
*   **The Test:** Can you instantly tell if Category A is larger in Chart 1 or Chart 2?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** None.
*   **Best Fix:** Convert the data into a single stacked bar chart with two columns [@muth_pie_charts_2018].
