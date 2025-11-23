---
id: small-multiples-reduce-color
title: Use Small Multiples to Eliminate Spaghetti Charts
bibliography: references.bib
description: Split complex multi-line charts into individual panels to remove the
  need for color distinctions.
labels:
- chart:small-multiples
- chart:line
- visual:layout
- impact:comparability
- data:temporal
---

## The Rule <!-- role: advice -->
When a line chart becomes too crowded to distinguish categories by color, split the categories into separate small charts (small multiples/panel charts). Give each category its own space.

## The Logic <!-- role: reason -->
Small multiples trade screen space for cognitive clarity. By isolating each trend, you no longer need color to distinguish "Line A" from "Line B." You can make all lines the same color (or use color to show a metric like growth/decline) because the panel label identifies the category [@muth_fewer_colors_2022].

## Where to Apply <!-- role: context -->
*   **User Goal:** Analyzing trends or patterns within individual categories (e.g., "How did Iran's GDP evolve?").
*   **Data Type:** Time series data with many overlapping categories (spaghetti charts).
*   **Audience:** Analytical readers looking for patterns across many items.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The primary goal is precise comparison of values across categories at a specific point in time.
*   **Reason:** It is harder to compare the height of a line in Panel A vs Panel F than it is to compare two lines crossing in a single chart [@muth_fewer_colors_2022].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Immediate comparability of magnitude between categories is reduced.
*   **The Risk:** Requires significantly more layout space (vertical or grid).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Keeping all lines in one chart and making them all semi-transparent.
*   **Why it fails:** This usually results in a muddy, unreadable blob in the center of the chart.

## How to Check <!-- role: check -->
*   **Visual Sign:** Do you have 10+ intersecting lines in one frame?
*   **The Test:** Can you trace a single line from start to finish without losing it in the mess? If no, switch to small multiples.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Break the single chart into a grid of charts, one for each line.
*   **Best Fix:** Sort the small multiples by a meaningful metric (e.g., highest value to lowest value) to aid comparison, and consider adding a faint gray "context" line of the global average in the background of each panel.
