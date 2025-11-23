---
id: optimize-adjacency-for-range
title: Juxtapose Minimum and Maximum Bars for Range Tasks
bibliography: references.bib
description: Place minimum and maximum bars near each other to improve range estimation
  accuracy.
labels:
- chart:bar
- task:estimate-range
- task:compare
- visual:position
- impact:clarity
- data:quantitative
---

## The Rule <!-- role: advice -->
When the user's task is to determine the range (the difference between the minimum and maximum values), place the shortest and tallest bars adjacent or close to one another. Avoid separating the extremes with many intermediate bars.

## The Logic <!-- role: reason -->
Perceiving range is driven by "slope" proxies—heuristics derived from the line connecting bar tips. Research suggests that "notch" patterns, where the shortest bar is flanked by bars near the maximum (or vice versa), significantly simplify the extraction of range information [@ondov_revealing_2021]. This juxtaposition simplifies the visual scan and emphasizes the difference (slope) between the extremes, making the range easier to estimate compared to random arrangements.

## Where to Apply <!-- role: context -->
*   **User Goal:** Judging which data series has a larger spread or range (variability).
*   **Data Type:** Series of values presented in bar charts.
*   **Audience:** General audiences performing "MaxRange" tasks (identifying the largest spread).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Time-Series or Ordinal Data.
*   **Reason:** If the X-axis represents a fixed sequence (e.g., months, ordered categories), you cannot rearrange bars to create adjacency between min and max values without destroying the data's semantic meaning.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the ability to sort by value (ascending/descending) or by label (alphabetical).
*   **The Risk:** The resulting "notch" pattern might look cluttered or disorderly compared to a sorted list.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Sorting bars by height (ascending/descending).
*   **Why it fails:** While this makes finding min/max easy, it separates them by the maximum visual distance, requiring the eye to saccade across the entire chart width to compare the extremes, rather than seeing the slope directly.
*   **The Wrong Fix:** Relying on the "Slope Neighbor" proxy (steepest drop between any two bars).
*   **Why it fails:** Users often select *against* steep local slopes when judging global range, or individual differences vary wildly on how this proxy is interpreted [@ondov_revealing_2021].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are the shortest and tallest bars located at opposite ends of the chart?
*   **The Test:** Trace the line between the tip of the shortest bar and the tallest bar. If this line traverses the entire width of the chart, the range is harder to process perceptually.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Highlight the min and max bars with a distinct color to visually link them.
*   **Best Fix:** If data ordering is flexible, re-sort the series to place the minimum and maximum values as immediate neighbors (creating a visual "notch").
