---
id: color-scale-natural-breaks
title: Use Natural Breaks to Respect Data Clustering
bibliography: references.bib
description: Use Natural Breaks (Jenks) to group similar values together and separate
  distant ones.
labels:
- chart:map
- chart:choropleth
- visual:color
- impact:clarity
- data:clusters
---

## The Rule <!-- role: advice -->
Select "Natural Breaks" (Jenks) interpolation when you want to balance showing data distribution with maintaining meaningful differentiation between groups.

## The Logic <!-- role: reason -->
Natural Breaks is an algorithm that minimizes the variance within classes and maximizes the variance between classes. As [@muth_interpolation_2022] describes, if many values are close together (e.g., 4.6, 4.7, 4.8), Natural Breaks groups them into a single color. If values are far apart (outliers), it keeps them separate. This creates a compromise where the map reflects the actual "clusters" in the data rather than forcing a strict linear math or a strict equal count.

## Where to Apply <!-- role: context -->
*   **User Goal:** To show "natural" groups in the data where items in the same color group are statistically similar.
*   **Data Type:** Uneven distributions that have clumps of data points and some outliers.
*   **Audience:** General audiences who need an intuitive understanding of "low," "medium," and "high" groups without misleading boundaries.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When you need precise, readable legend labels.
*   **Reason:** Natural Breaks algorithms calculate precise mathematical cuts (e.g., 4.1, 5.7, 12.3), which result in messy, hard-to-read legends compared to rounded numbers [@muth_interpolation_2022].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Legibility of the key (often produces awkward decimals).
*   **The Risk:** The groups are data-dependent, meaning if the data updates slightly, the boundaries might shift unpredictably, making year-over-year comparison difficult.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Leaving the raw Jenks values in the legend (e.g., "4.134 to 5.789").
*   **Why it fails:** It increases cognitive load for the reader trying to parse specific decimal ranges.

## How to Check <!-- role: check -->
*   **Visual Sign:** Look at the histogram or "rug plot." Are the cut lines falling in the middle of a dense cluster of data points?
*   **The Test:** If a cut line splits a dense bar in the histogram, Natural Breaks might not be working correctly (or the data has no natural breaks).

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Use the calculated Natural Breaks as a starting point, then manually round them (Custom Interpolation).
*   **Best Fix:** Convert the scale to "Custom" and adjust the break points slightly to the nearest round number (e.g., change 4.1 to 4) to make the legend readable while preserving the clustering logic.
