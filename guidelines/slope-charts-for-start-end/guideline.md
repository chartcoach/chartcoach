---
id: slope-charts-for-start-end
title: Use Slope Charts to Focus on Total Change
bibliography: references.bib
description: When the journey doesn't matter, use slope charts to highlight the difference
  between start and end points.
labels:
- chart:slope
- chart:line
- task:compare
- data:temporal
- impact:simplicity
---

## The Rule <!-- role: advice -->
Use a slope chart instead of a standard line chart when the fluctuations between the first and last date are irrelevant to your message.

## The Logic <!-- role: reason -->
A slope chart acts like a line chart where "everything between the first and last date has been erased." By removing the intermediate noise, you focus the reader's attention strictly on the evolution (increase or decrease) between two specific points in time. This is also an effective way to "tidy up an otherwise-messy line chart" [@muth_chart_types_guide_2025].

## Where to Apply <!-- role: context -->
*   **User Goal:** Showing how a value evolved from Point A to Point B.
*   **Data Type:** Time series where the "ups and downs" in the middle are "not that interesting."
*   **Audience:** Readers who need a clear "before and after" comparison.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The volatility or specific timing of changes is important.
*   **Reason:** Slope charts hide all variance between the two endpoints.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Total loss of context regarding *how* the change happened (e.g., was it gradual or a sudden spike?).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Keeping a full line chart but only labeling the ends.
*   **Why it fails:** The visual line still draws the eye to the intermediate noise, distracting from the start/end comparison.

## How to Check <!-- role: check -->
*   **Visual Sign:** Is the line between the start and end very jagged, but your commentary only discusses the final result?
*   **The Test:** Ask "Does the reader need to know what happened in the middle?" If no, use a slope chart.

## How to Fix <!-- role: fix -->
*   **Best Fix:** Remove intermediate data points and connect the start and end values directly (Slope Chart).
*   **Alternative:** If you have too many categories for a slope chart, use an arrow plot [@muth_chart_types_guide_2025].
