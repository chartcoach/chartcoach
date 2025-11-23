---
id: adjust-panel-size-to-data-density
title: Resize Panels Based on Data Density
bibliography: references.bib
description: Shrink panel sizes for datasets with fewer data points to maximize space
  efficiency.
labels:
- chart:small-multiples
- visual:layout
- visual:size
- impact:efficiency
---

## The Rule <!-- role: advice -->
Do not be afraid to shrink your charts. Scale the size of your panels relative to the data density: the fewer data points you have, the smaller your panels can be.

## The Logic <!-- role: reason -->
*   **The Principle:** Visual Acuity.
*   **The Evidence:** The human eye is efficient at detecting variation in size, position, and shape even at small resolutions. [@muth_small_multiple_line_charts_2024] (citing Andy Kirk) notes that small multiples allow you to play with size. Panels don't need to be large to show a simple trend.

## Where to Apply <!-- role: context -->
*   **User Goal:** Showing many categories (high density) in a limited space (e.g., dashboard or mobile screen).
*   **Data Type:** Simple trend lines or low-frequency data.
*   **Audience:** Readers scanning for general patterns rather than specific values.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** High-frequency, noisy data where fine detail matters.
*   **Reason:** If the chart is too small, significant fluctuations might look like smooth lines or visual noise.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Axis labels may become unreadable or need to be removed (sparklines).
*   **The Risk:** Making them too small can frustrate users on mobile devices trying to tap or examine details.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Making every panel "presentation size" (large).
*   **Why it fails:** It pushes relevant data "below the fold," forcing scrolling and breaking the ability to see the whole picture at once.

## How to Check <!-- role: check -->
*   **Visual Sign:** Is there more white space than data line?
*   **The Test:** Can you reduce the chart size by 50% and still see the trend? If yes, shrink it.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Reduce the height of the rows.
*   **Best Fix:** Use sparklines in a table if the panels need to be extremely small.
