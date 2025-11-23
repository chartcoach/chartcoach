---
id: segmentation-color-over-shape
title: Prioritize Color Over Shape for Grouping
bibliography: references.bib
description: Use color rather than shape when data points need to be visually segmented
  into distinct clusters.
labels:
- chart:scatterplot
- task:cluster
- task:segmentation
- visual:color
- visual:shape
- impact:clarity
---

## The Rule <!-- role: advice -->
Use color hue, rather than shape, to encode categories that viewers need to visually segment or cluster within a visualization.

## The Logic <!-- role: reason -->
Color is a dominant grouping cue in human vision. Viewers can easily segment points of different colors regardless of their shape. However, segmenting points based on shape is significantly more challenging, especially if the shapes have different colors. Shape perception is often interfered with by other features, making it a weak channel for segmentation tasks.
*   **The Principle:** Feature Dominance in Segmentation
*   **The Evidence:** [@szafir_four_2016] as collated in [@zeng_review_2023]

## Where to Apply <!-- role: context -->
*   **User Goal:** Identifying distinct clusters or separating data into logical groups (e.g., "Where are the high-income countries located?").
*   **Data Type:** Nominal data overlaid on quantitative axes (e.g., a categorical scatterplot).
*   **Audience:** General audiences or analysts looking for distributional patterns across categories.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The visualization must be accessible to color-blind users and redundant encoding is necessary.
*   **Reason:** While color is stronger for segmentation, accessibility requires a secondary channel (like shape) to ensure all users can distinguish the data.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You consume the color channel, which is often the most salient channel, preventing its use for quantitative encoding (e.g., a heatmap).
*   **The Risk:** Over-reliance on color without luminance contrast can cause issues for color-vision deficient users.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using shape alone to differentiate dense clusters.
*   **Why it fails:** In a dense scatterplot, distinguishing a cluster of squares from a cluster of triangles requires serial inspection, whereas colors separate pre-attentively [@szafir_four_2016].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you using symbols (squares, crosses, circles) to define your primary groups?
*   **The Test:** Can you squint your eyes and still see the groups as distinct "blobs"? If not, the segmentation is weak.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Assign distinct colors to the categories currently defined by shape.
*   **Best Fix:** Use color as the primary separator and use shape only as a redundant encoding to support accessibility.
