---
id: account-for-neighborhood-contrast-in-bars
title: Account for Contrast Effects in Bar Chart Ordering
bibliography: references.bib
description: Bars are perceived as shorter when next to tall neighbors and taller
  when next to short neighbors.
labels:
- chart:bar
- task:sort
- task:rank
- visual:length
- impact:accuracy
- impact:bias
- data:quantitative
---

## The Rule <!-- role: advice -->
When presenting bar charts for rank estimation, arrange bars to avoid extreme height differences between neighbors, or account for the fact that a bar will appear shorter next to tall bars and taller next to short bars.

## The Logic <!-- role: reason -->
Human perception of a bar's height is not independent; it is influenced by the "neighborhood" of adjacent bars.
*   **The Principle:** The Neighborhood Effect (Contrast Effect). Experimental results show a systematic bias where target bars surrounded by high neighbors are underestimated, while the same bars surrounded by low neighbors are overestimated [@zhao_neighborhood_2019].
*   **The Evidence:** The collation of graphical perception knowledge identifies this as a significant bias in sort and rank tasks, noting significant performance differences between targets with "highest" versus "lowest" neighbors [@zeng_review_2023].

## Where to Apply <!-- role: context -->
This advice applies to standard visualizations of quantitative data where accurate judgment of value or rank is necessary.
*   **User Goal:** Estimating the specific rank or value of a data point relative to the whole.
*   **Data Type:** Quantitative data mapped to length (Bar Charts).
*   **Audience:** Users performing detailed analysis or comparison of individual entities.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When the data has a strict, meaningful intrinsic order that cannot be changed (e.g., time series or ordinal stages).
*   **Reason:** Preserving the semantic structure of the data (e.g., "January, February, March") usually outweighs the need to eliminate minor perceptual biases in height estimation.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You may lose the ability to order data alphabetically or by a secondary variable if you sort by value to smooth out neighborhood effects.
*   **The Risk:** If you leave the chart unsorted (e.g., random or alphabetical), users may misjudge the rank of bars located next to outliers.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Relying solely on gridlines to correct perception.
*   **Why it fails:** While gridlines help, the optical illusion caused by the immediate neighbors (the contrast effect) persists in rapid visual processing.

## How to Check <!-- role: check -->
*   **Visual Sign:** Look for "ragged" profiles where a medium-height bar is sandwiched between two very tall bars or two very short bars.
*   **The Test:** Check if the sandwiched bar looks significantly different if you cover the neighbors with your hand.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Sort the bar chart by value (ascending or descending). This minimizes the height difference between neighbors, removing the extreme contrast.
*   **Best Fix:** If sorting is not possible, add value labels directly to the bars to override the perceptual bias with explicit data.
