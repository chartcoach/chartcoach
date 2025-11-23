---
id: use-bars-for-precise-comparison
title: Use Bar Charts for Precise Percentage Comparisons
bibliography: references.bib
description: Pie charts mask small differences; use bar or column charts when comparing
  similar percentage values.
labels:
- chart:bar
- chart:pie
- task:compare
- visual:length
- impact:accuracy
- data:part-to-whole
---

## The Rule <!-- role: advice -->
Use bar or column charts instead of pie or donut charts when you need the reader to compare values accurately, even if the data represents shares or percentages.

## The Logic <!-- role: reason -->
Circle sections (angles and areas) are difficult for the human eye to compare. [@muth_chart_types_guide_2025] notes that a 3% difference between two categories is easy to spot in a bar chart but "practically invisible" in a pie or donut chart. While pies clearly signal "part-to-whole," bars dominate for comparison.

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing the magnitude of shares (e.g., election results, market share).
*   **Data Type:** Percentages or shares where differences might be subtle.
*   **Audience:** Readers who need to know which category is larger, even by a small margin.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** You only need to communicate the concept of "shares" broadly, not precise differences.
*   **Reason:** Pie, donut, and parliament charts are "very obvious" in stating that the data represents percentages/parts of a whole [@muth_chart_types_guide_2025].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the immediate visual metaphor of a "whole" circle that implies the values add up to 100%.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Adding data labels to a pie chart to explain the invisible differences.
*   **Why it fails:** The visual (the slice) still fails to show the difference; the user is forced to read text rather than seeing the data.

## How to Check <!-- role: check -->
*   **Visual Sign:** Do two slices look roughly the same size even though the data says they are different?
*   **The Test:** Remove the number labels. Can you still tell which category is bigger? If not, use a bar chart.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Switch the chart type to a column chart or bar chart.
*   **Alternative:** If you want something eye-catching, use a waffle chart or pictogram (though these also sacrifice some readability for fun) [@muth_chart_types_guide_2025].
