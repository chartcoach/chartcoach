---
id: use-diverging-scales-for-bipolar-data
title: Use Diverging Scales for Bipolar Data
bibliography: references.bib
description: Use diverging color scales for data with a meaningful midpoint or opposing
  directions.
labels:
- visual:color
- data:diverging
- task:compare
- chart:heatmap
- chart:map
---

## The Rule <!-- role: advice -->
Use a diverging (bipolar) color scale for quantitative data that has a meaningful midpoint, negative/positive split, or opposing directions.

## The Logic <!-- role: reason -->
Diverging scales share the properties of sequential scales but proceed in two directions from a bright middle value (usually white or light grey) toward darker hues at both extremes. @muth_which_color_scale_2021 explains this is ideal for visualizing Likert scales (agree/disagree), election results (Democrat/Republican), or temperature anomalies, as it clearly signals deviation from a norm.

## Where to Apply <!-- role: context -->
*   **User Goal:** Showing deviation from a standard, median, or zero.
*   **Data Type:** Bipolar data (positive/negative values) or data with a neutral center (Likert scales).
*   **Audience:** Users needing to quickly identify extremes in two directions.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The midpoint is arbitrary.
*   **Reason:** If the "middle" (e.g., the national average) isn't meaningful to the specific story, a diverging scale might confuse the reader by implying a strict divide where none exists.

## The Price <!-- role: costs -->
*   **The Risk:** The critical middle range often has very low contrast (light colors), making values near the center harder to read accurately compared to the edges.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a sequential scale (low-to-high) for negative-to-positive data.
*   **Why it fails:** This implies that "negative" is simply a lower amount of "positive," rather than a distinct, opposing state.

## How to Check <!-- role: check -->
*   **Visual Sign:** Is the center of the scale the lightest point? Do the colors get darker as they move toward both extremes?
*   **The Test:** Check if the data crosses zero or a meaningful average. If yes, use diverging.

## How to Fix <!-- role: fix -->
*   **Best Fix:** Select a palette with two distinct hues (e.g., Orange and Blue) separated by a neutral color (white/grey) representing the midpoint.
