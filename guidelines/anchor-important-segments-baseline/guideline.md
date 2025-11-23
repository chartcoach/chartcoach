---
id: anchor-important-segments-baseline
title: Anchor the Most Important Segment to the Baseline
bibliography: references.bib
description: Place the primary category at the bottom of the stack to facilitate accurate
  comparison across columns.
labels:
- chart:stacked-column
- visual:position
- task:compare
- impact:readability
- data:categorical
---

## The Rule <!-- role: advice -->
Place the most important data category at the bottom of the stack and use a distinct color to make it stand out.

## The Logic <!-- role: reason -->
Stacked column charts are excellent for comparing totals, but they make it difficult to compare individual internal segments because they lack a consistent starting point. By placing the critical category at the bottom, you provide a shared baseline, making comparison as easy as reading a standard bar chart [@muth_stacked_columns_2018].

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing specific sub-categories across multiple totals.
*   **Chart Type:** Stacked column charts (vertical).
*   **Data Priority:** One specific category is more significant to the narrative than the others.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The data has a natural, strictly ordered hierarchy (e.g., Likert scales, income brackets) that must be preserved.
*   **Reason:** Reordering segments based on importance rather than their natural logic can confuse the reader regarding the data's structure.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Middle and top segments become harder to compare precisely as they "float" at different heights.
*   **The Risk:** Readers may ignore the segments not anchored to the baseline.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Arranging segments alphabetically or randomly.
*   **Why it fails:** It creates a "jagged" visual pattern for the most important data points, making accurate visual measurement impossible.

## How to Check <!-- role: check -->
*   **Visual Sign:** Is the segment you want the user to focus on "floating" in the middle of the stack?
*   **The Test:** Look at two non-adjacent columns. Can you instantly tell which version of the primary segment is larger without reading the label?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Sort the data series so the priority category is the first series (bottom).
*   **Best Fix:** If comparisons of *all* segments are equally important, switch to "Small Multiples" or "Split Bars" instead of a stacked chart.
