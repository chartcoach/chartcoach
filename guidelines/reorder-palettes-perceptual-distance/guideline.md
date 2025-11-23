---
id: reorder-palettes-perceptual-distance
title: Reorder Palettes to Maximize Perceptual Distance
bibliography: references.bib
description: Improve categorical discrimination by re-ordering palette items so that
  sequentially assigned values are perceptually distinct.
labels:
- chart:qualitative
- visual:color
- visual:shape
- task:distinguish
- impact:clarity
- data:categorical
---

## The Rule <!-- role: advice -->
Do not assign visual variables (shapes or colors) from a palette in their default or random order. Re-order the palette sequence so that each new item added to the set maximizes the perceptual distance from all previously selected items.

## The Logic <!-- role: reason -->
Default palettes often contain clusters of items that look similar (e.g., multiple triangular shapes or similar hues). If data categories are assigned sequentially to these similar items, users struggle to distinguish them. By re-ordering based on perceptual kernels, you ensure that the most distinct items are used first.
*   **The Principle:** Perceptual Discriminability
*   **The Evidence:** [@demiralp_learning_2014] demonstrate that standard palettes (like Tableau's defaults) contain perceptual clusters. Re-ordering them using a "max-min" distance approach (Hausdorff distance) significantly increases the distinctness of the first $n$ items used in a visualization.

## Where to Apply <!-- role: context -->
*   **User Goal:** Distinguishing between different categories in a scatterplot or map.
*   **Data Type:** Nominal (categorical) data.
*   **Audience:** Users who need to rapidly identify distinct groups without confusion.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Semantic Resemblance
*   **Reason:** If specific colors or shapes have strong semantic meaning (e.g., Blue for Water, Green for Land), these associations override abstract perceptual optimization [@demiralp_learning_2014].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the "aesthetic" cohesion that sometimes comes with analogous color schemes or grouped shapes.
*   **The Risk:** The resulting palette may look eclectic or less "designed" because it jumps between highly disparate visual elements (e.g., pairing a filled circle with a cross immediately).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Relying solely on mathematical color spaces (like CIELAB) without checking shape.
*   **Why it fails:** [@demiralp_learning_2014] show that while CIELAB correlates with perception, crowd-sourced "perceptual kernels" (actual human judgment) provide more accurate distance measures, particularly for shapes where no simple mathematical formula exists.

## How to Check <!-- role: check -->
*   **Visual Sign:** Do two different categories look confusingly similar (e.g., a square and a diamond) while a distinct option (e.g., an X) remains unused in the legend?
*   **The Test:** Check if the subset of items used in your chart includes the most visually disparate options available in your full palette.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Manually pick items from your palette that look the most different for your top categories, rather than taking the first 5.
*   **Best Fix:** Algorithmically re-order the palette using a perceptual kernel (distance matrix) to greedily select the next item that has the maximum distance to the existing set [@demiralp_learning_2014].
