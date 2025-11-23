---
id: limit-cardinality-for-color-shape
title: Restrict Color and Shape for High Cardinality Data
bibliography: references.bib
description: Avoid mapping high-cardinality variables to color or shape to prevent
  discrimination issues and clutter.
labels:
- visual:color
- visual:shape
- data:categorical
- impact:clarity
- complexity:intermediate
---

## The Rule <!-- role: advice -->
Do not map variables with high cardinality (a large number of unique values) to color hue or shape channels.

## The Logic <!-- role: reason -->
Human perception has limited capacity to discriminate between many distinct colors or shapes simultaneously.
*   **The Principle:** Discriminability and Visual Clutter.
*   **The Evidence:** The Compass recommendation engine penalizes encoding effectiveness based on cardinality. High cardinality on these channels leads to "poor color or shape discrimination." Furthermore, if used in small multiples (facets), high cardinality creates "massive, sparse trellis plots" that are difficult to scan [@wongsuphasawat_voyager_2016].

## Where to Apply <!-- role: context -->
*   **User Goal:** distinguishing between groups or tracking items across a plot.
*   **Data Type:** Nominal or Ordinal data with many unique levels (e.g., > 7-10 categories).
*   **Visual Channels:** Retinal variables (Color Hue, Shape) and Faceting (Row, Column).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Interactive highlighting/brushing.
*   **Reason:** If the user needs to find one specific item among thousands (e.g., "Highlight Product X"), using color for *selection* is valid, even if the background cardinality is high.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You cannot display every single category identity simultaneously in a single view using these channels.
*   **The Risk:** You may need to aggregate data (e.g., "Top 5 + Others") which hides the long tail of the distribution.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Generating a legend with 20+ distinct colors.
*   **Why it fails:** Users cannot effectively map the colors back to the data points, and colors inevitably become too similar to distinguish.

## How to Check <!-- role: check -->
*   **Visual Sign:** A "fruit salad" effect where the chart is a noisy mix of indistinguishable colors, or a legend that requires a scrollbar.
*   **The Test:** Check the distinct count of the variable mapped to color. If it exceeds ~10 (or 7 per Voyager's defaults), the design violates this rule.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Filter the data to the top N items before visualizing.
*   **Best Fix:** Switch visual encodings. Move the high-cardinality variable to a positional axis (e.g., a long bar chart) rather than a retinal channel (color/shape).
