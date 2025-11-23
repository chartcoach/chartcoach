---
id: switch-to-bars-for-labels-and-count
title: Switch to Stacked Bars for Many Categories or Long Labels
bibliography: references.bib
description: Use horizontal stacked bars instead of vertical columns when dealing
  with many totals or lengthy text labels.
labels:
- chart:stacked-bar
- visual:orientation
- impact:readability
- data:categorical
---

## The Rule <!-- role: advice -->
If you have more than approximately 10 totals (columns), or if your x-axis labels are long, switch from a stacked *column* chart to a stacked *bar* chart (horizontal).

## The Logic <!-- role: reason -->
On a screen, the width of a chart is strictly limited by the device, but the height is generally flexible (users can scroll). Long labels do not fit well below vertical columns. Horizontal bars accommodate long labels naturally and allow for an unlimited number of categories by extending vertically [@muth_stacked_columns_2018].

## Where to Apply <!-- role: context -->
*   **Data Type:** Categorical data with >10 items or verbose category names.
*   **Medium:** Digital screens (mobile or desktop).
*   **Constraint:** Limited horizontal pixel width.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Time series data.
*   **Reason:** Time is conventionally plotted on the horizontal x-axis (left to right). Vertical time axes (top to bottom) are counter-intuitive for most readers.

## The Price <!-- role: costs -->
*   **The Sacrifice:** It may be harder to perceive the "shape" of the distribution (like a bell curve) which is often easier to read on a vertical histogram-style layout.
*   **The Risk:** The chart takes up more vertical screen real estate.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Rotating text labels 45 or 90 degrees to fit them under columns.
*   **Why it fails:** Rotated text is significantly harder to read and breaks the reading flow.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are your x-axis labels truncated (using "...") or rotated? Are the columns extremely thin to fit the screen?
*   **The Test:** If you cannot read the labels without tilting your head, or if the chart looks crowded on a mobile width, switch orientation.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Transpose the chart axes (swap X and Y).
*   **Best Fix:** Ensure the stacking order is consistent (most important value aligned to the left baseline for horizontal bars).
