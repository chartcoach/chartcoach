---
id: avoid-small-multiples-for-point-comparison
title: Avoid Small Multiples for Point Comparisons
bibliography: references.bib
description: Use normal line charts instead of small multiples when comparing values
  at specific time points.
labels:
- chart:line
- chart:small-multiples
- task:compare
- impact:readability
---

## The Rule <!-- role: advice -->
Use a standard (single) line chart, not small multiples, if the primary goal is to compare lines with each other at specific points in time.

## The Logic <!-- role: reason -->
*   **The Principle:** Proximity for Comparison.
*   **The Evidence:** It is visually difficult to compare the height of a line in one panel to the height of a line in a different panel. [@muth_small_multiple_line_charts_2024] illustrates that questions like "Which was higher in 2022?" are easy to answer when lines share a single axis, but nearly impossible in separated panels.

## Where to Apply <!-- role: context -->
*   **User Goal:** Precise comparison of values between categories (e.g., "Did Company A overtake Company B in Q3?").
*   **Data Type:** A manageable number of lines (usually fewer than 5-6) that do not overlap excessively.
*   **Audience:** Analysts or readers needing precise ranking data.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The lines are an unreadable "spaghetti" mess.
*   **Reason:** If you can't read the single chart, the comparison advantage is lost anyway. In that case, switch to small multiples with "shadow lines" (background context).

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the clean separation of trends that small multiples provide.
*   **The Risk:** Line overlap may obscure data points.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using small multiples for a "Horse Race" narrative.
*   **Why it fails:** The reader cannot easily see the crossover points or the lead changes.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you trying to look back and forth between two panels to see which line is physically higher?
*   **The Test:** Ask, "Which line is highest at the peak?" If you have to check axis numbers to answer, you need a single chart.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Merge the panels back into one chart.
*   **Best Fix:** Merge into one chart and use direct labeling or highlighting to manage clutter.
