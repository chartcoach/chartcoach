---
id: use-small-multiples-for-spaghetti-data
title: Use Small Multiples to Untangle Overlapping Lines
bibliography: references.bib
description: Replace cluttered single line charts with small multiples when lines
  overlap significantly to improve readability.
labels:
- chart:line
- chart:small-multiples
- visual:layout
- impact:clarity
- data:temporal
---

## The Rule <!-- role: advice -->
When a single line chart contains many lines that overlap significantly ("spaghetti charts"), separate each line into its own individual panel within a small multiple (trellis/facet) chart.

## The Logic <!-- role: reason -->
*   **The Principle:** Separation and Focus.
*   **The Evidence:** Overlapping lines make it difficult for readers to parse individual trends. According to [@muth_small_multiple_line_charts_2024], giving each line "space to breathe" in its own panel reduces reader overwhelm and makes it easier to trace the shape and development of each specific category.

## Where to Apply <!-- role: context -->
*   **User Goal:** The reader needs to see the specific trend shape (ups and downs) of individual categories.
*   **Data Type:** Multiple time-series datasets (usually more than 3-4) that share a similar value range and intersect frequently.
*   **Audience:** Readers trying to analyze individual category performance rather than just aggregate noise.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The lines do not overlap (e.g., stacked layers or distinctly separated values).
*   **Reason:** If the lines are distinct, a single chart allows for easier direct comparison of magnitude without the cognitive load of scanning multiple panels.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the ability to make immediate, precise comparisons of value at specific points in time (e.g., "Was line A higher than line B in 2022?").
*   **The Risk:** It takes up more layout space than a single chart.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a single chart with a legend and 10+ colors.
*   **Why it fails:** It creates visual clutter and forces the eye to jump back and forth between the legend and the lines.

## How to Check <!-- role: check -->
*   **Visual Sign:** Can you follow a single line from start to finish without losing it in a knot of other lines?
*   **The Test:** If your single chart looks like a plate of spaghetti, split it.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Create a panel for each category.
*   **Best Fix:** Create panels for each category and sort them meaningfully (e.g., by value).
