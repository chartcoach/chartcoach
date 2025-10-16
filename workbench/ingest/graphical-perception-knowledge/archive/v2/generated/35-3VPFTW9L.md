---
id: optimize-scatterplot-colors
title: "Optimize Color Assignment for Class Separability in Multiclass Scatterplots"

impact:
  - perceptual
  - cognitive
  - logos
  - aesthetic
  - performance
tags:
  - scatterplot
  - color
  - class-separability
  - cluster-analysis
  - nominal-data
  - optimization

sources:
  - type: research
    ref: Wang et al., 2019
    url: https://doi.org/10.1109/TVCG.2018.2864912
    note: "Primary source for an optimization method to assign colors to classes in multiclass scatterplots to maximize perceptual separability, based on a genetic algorithm."

tools:
  - type: implement
    name: Colorgorical
    url: http://vrl.cs.brown.edu/color
    description: "Generates discriminable and aesthetically preferable categorical color palettes, a good first step before assigning colors."
  - type: implement
    name: ColorBrewer
    url: https://colorbrewer2.org/
    description: "Provides pre-defined, well-tested categorical color palettes suitable as input for a color assignment process."

examples:
  - type: bad
    description: "A multiclass scatterplot where adjacent or overlapping clusters are assigned similar colors (e.g., light blue and light green), making them difficult to distinguish."
  - type: good
    description: "The same scatterplot where the colors have been reassigned, ensuring that adjacent clusters have high-contrast colors (e.g., orange and dark blue), maximizing their visual separation."
---

## Guidance

When assigning colors to classes in a multiclass scatterplot, optimize the assignment to maximize the perceptual separability of spatially adjacent or overlapping clusters. Don't simply apply a palette in its default order; instead, match colors to classes based on their position in the plot.

## Why

A default color assignment can place visually similar colors on neighboring clusters, making it difficult for viewers to see the boundaries between groups. This can obscure the data's structure and lead to misinterpretation. An optimized assignment, by contrast, ensures high-contrast colors are used for adjacent groups, making class structures immediately clear and reducing the cognitive effort needed to analyze the plot.

## When it applies

- When creating multiclass scatterplots where classes have spatial overlap or are close to each other.
- When the primary task is to analyze class structure, count the number of clusters, or visually assess the quality of a classification.
- When visualizing high-dimensional labeled data that has been projected onto a 2D plane using techniques like PCA or t-SNE.

## Exceptions

- When colors have a strong, pre-defined semantic meaning that must be preserved (e.g., brand colors for competitors, party colors in a political map). In this case, semantic consistency is more important than perceptual optimization.
- When all classes are already perfectly separated in space with no overlap. The specific color assignment becomes less critical, though using a discriminable palette is still recommended.

## Trade-offs

- **Computational Cost:** Finding the optimal color assignment is a complex combinatorial problem. Unlike a simple default assignment, an optimized approach requires an algorithm (like the genetic algorithm from the source paper) that takes time to compute.
- **Predictability:** The optimal color for a given class (e.g., "Apples") will change depending on the spatial distribution of the data in each specific chart. This lack of consistency can be a drawback if you need the same class to always have the same color across multiple charts.
- **Aesthetics:** The algorithm prioritizes perceptual separability, which may not always align with traditional principles of color harmony. The resulting combination might be highly effective but less aesthetically pleasing than a manually curated theme.

## Evaluate

- [ ] Do spatially adjacent or overlapping clusters have colors that are hard to tell apart (e.g., light green next to light yellow, or two similar shades of blue)?
- [ ] Is it difficult to quickly and confidently count the number of distinct color groups in the plot?
- [ ] Is a low-contrast color (like yellow) assigned to a sparse or fragmented cluster, making it hard to see against a light background?

## Repair

1.  **Manual Swap:** Identify the two most confusing adjacent clusters and manually swap their assigned colors to a pair with higher contrast.
2.  **Iterative Refinement:** Systematically re-assign colors to maximize the perceptual distance between the most problematic pairs of clusters first. Ensure colors with high contrast to the background (e.g., dark, saturated colors) are used for the most intertwined or sparse classes.
3.  **Automate:** Use an optimization algorithm that takes a color palette and the data points as input to automatically find an assignment that maximizes a class separability metric.