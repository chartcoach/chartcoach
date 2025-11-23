---
id: optimize-color-mapping-spatial-proximity
title: Map Distinct Colors to Spatially Adjacent Classes
bibliography: references.bib
description: Assign specific hues based on spatial data distribution to improve class
  separability in scatterplots.
labels:
- chart:scatter
- task:cluster
- visual:color
- impact:clarity
- data:categorical
- data:spatial
- complexity:intermediate
---

## The Rule <!-- role: advice -->
Do not assign colors from a palette to data classes randomly or alphabetically. Explicitly assign the most perceptually distinct colors in your palette to the data classes that are spatially closest to each other or overlapping.

## The Logic <!-- role: reason -->
A high-quality color palette is insufficient if the assignment of those colors fails to account for spatial data distribution. If two distinct data clusters overlap or sit near each other, assigning them similar colors (e.g., Blue and Cyan) makes them visually indistinguishable.
*   **The Principle:** Perceptual Class Separability. By minimizing the visual similarity between spatially neighboring points, you maximize the user's ability to perceive distinct groups.
*   **The Evidence:** In a review of graphical perception knowledge, Zeng and Battle [@zeng_review_2023] highlight the work of Wang et al. [@wang_optimizing_2019], who demonstrated that optimizing color assignment based on spatial neighbors significantly reduces errors in counting classes and improves the speed of cluster identification compared to default assignments.

## Where to Apply <!-- role: context -->
*   **User Goal:** Differentiating between multiple categories (Class Separability) or identifying clusters.
*   **Data Type:** Multiclass scatterplots (specifically 2D quantitative data with nominal labels), particularly those with 6 to 10 classes.
*   **Audience:** Users performing analytical tasks where distinguishing class boundaries is critical.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The data classes are already spatially distinct (separated by large whitespace gaps).
*   **Reason:** As noted by Wang et al. [@wang_optimizing_2019], when spatial separation is high, color distinctness becomes less critical for separability because position encoding already separates the groups.
*   **Scenario:** The colors carry inherent semantic meaning (e.g., Red for Republicans, Blue for Democrats).
*   **Reason:** Semantic consistency usually overrides optimization for separability.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Implementation complexity. You cannot simply map a scale to a legend; you must calculate the spatial nearest neighbors (KNN) of the data points first.
*   **The Risk:** If the data updates or filters change, the optimal assignment might change, leading to inconsistent coloring across different views of the same data.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Switching to a "better" palette (e.g., Tableau 10 instead of Excel default) without changing the mapping order.
*   **Why it fails:** Even a robust palette will fail if its two most similar colors happen to map to two overlapping data clusters. The *assignment* matters as much as the *palette* [@wang_optimizing_2019].

## How to Check <!-- role: check -->
*   **Visual Sign:** Look for areas where two different clusters merge into an amorphous blob because their colors lack contrast.
*   **The Test:** Check the "border" regions between clusters. Can you clearly see which point belongs to which class?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Manually swap the colors of two classes if they overlap and look similar.
*   **Best Fix:** Use an optimization algorithm (like the genetic algorithm proposed by Wang et al. [@wang_optimizing_2019]) to minimize color similarity between k-nearest neighbors of different classes.
