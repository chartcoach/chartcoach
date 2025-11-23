---
id: simplify-quantitative-labels
title: Simplify Crowded Quantitative Keys
bibliography: references.bib
description: Skip labels or use qualitative terms in color keys to avoid clutter when
  showing many classes.
labels:
- visual:text
- visual:scale
- data:quantitative
- impact:clarity
---

## The Rule <!-- role: advice -->
For quantitative color scales, skip intermediate labels (e.g., label every second class) or replace exact numbers with qualitative descriptors (e.g., "Less" to "More") if precision is not critical.

## The Logic <!-- role: reason -->
Labeling every single class in a detailed color scale can cause text to overlap or look overwhelmingly busy, discouraging the reader. Often, a general trend ("low" vs "high") is sufficient for the reader to understand the pattern, especially if exact values are available via tooltips. Showing only visibly distinct colors or the min/max/center values reduces cognitive load [@muth_color_keys_2023].

## Where to Apply <!-- role: context -->
*   **User Goal:** Understanding general distribution or geographic trends rather than reading exact values.
*   **Data Type:** Choropleth maps with many classes, high-resolution heatmaps.
*   **Audience:** General public or audiences consuming static images where interactivity isn't possible.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Technical or scientific analysis.
*   **Reason:** If the user needs to know exactly where a threshold lies (e.g., "Is this level safe or unsafe?"), exact labeling for every class is required.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Precision. Readers will not know the exact boundaries of a color bin immediately.
*   **The Risk:** Ambiguity. Terms like "High" are subjective without a numerical anchor.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Labeling colors that are visually indistinguishable (e.g., "Almost dark blue" vs. "Dark blue").
*   **Why it fails:** Readers cannot distinguish the colors on the map anyway, so the label is useless.

## How to Check <!-- role: check -->
*   **Visual Sign:** The numbers in your legend are touching each other or use a tiny font to fit.
*   **The Test:** Squint at the key. If the text creates a jagged, dense texture that is hard to scan, it needs simplification.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Remove every second label (e.g., 10, 30, 50 instead of 10, 20, 30, 40, 50).
*   **Best Fix:** Label only the extremes (Min/Max) and perhaps the center point, or replace numbers with "Lower" and "Higher" if the exact metric is complex.
