---
id: adapt-scatterplot-for-data-density
title: "Adapt scatterplot marker size and opacity to handle varying data density"

tags:
  - impact:perceptual
  - impact:performance
  - chart:scatter
  - task:correlation
  - task:distribution
  - data:quantitative
  - data:cardinality.high
  - visual:size
  - visual:opacity
  - audience:general
  - medium:screen

evidence:
  strength: medium
  summary: "Micallef et al. (2017) demonstrated that a perceptually-driven optimization algorithm could automatically adapt a scatterplot's visual design to changing data resolutions. By adjusting marker size and opacity, the algorithm maintained the visibility of structural patterns as data points increased from ~15k to 250k, unlike a fixed-design approach which became an unreadable blob."

sources:
  - type: research
    ref: Micallef et al., 2017
    url: https://doi.org/10.1109/TVCG.2017.2674978
    note: "Case study in Figure 1 shows how the algorithm adjusts marker size and opacity to reveal patterns in the Hurricane Isabel dataset at two different resolutions, while the standard fixed design fails at the higher resolution due to overplotting."
    role: primary

examples:
  - type: good
    description: "Figure 1b in the source paper shows a scatterplot of a high-density dataset where marker opacity and size have been automatically reduced. This reveals the fine-grained structure within the data cloud."
  - type: bad
    description: "Figure 1a in the source paper shows the same high-density dataset plotted with fixed, default parameters (larger, opaque markers). The result is a solid black 'ink blob' where all internal detail is lost to overplotting."
---

## Guidance

For scatterplots with high or variable data density, dynamically adjust marker size and opacity to prevent overplotting and reveal underlying patterns. As data density increases, decrease marker size and/or opacity.

## Why

When many data points are plotted in a small area, default markers (which are often moderately sized and fully opaque) will overlap and merge into an unreadable "ink blob." This phenomenon, called overplotting, obscures the distribution, density, and structure within the data. By making markers smaller and semi-transparent, you allow the density to be represented by the accumulation of color, revealing the shape of the distribution while still suggesting the location of individual points.

### Core Principle

Effective visualization designs must adapt to the characteristics of the data. A design that works for a sparse dataset will often fail for a dense one.

## When it applies

- When creating scatterplots with a large number of data points (e.g., thousands or more).
- When the data is not uniformly distributed and has dense clusters or areas of high overlap.
- When the task is to understand the distribution, density, or fine-grained structure of the data, rather than just identifying a few individual points.

## Exceptions

- For very sparse datasets where no points overlap, adjusting for density is unnecessary.
- If the primary task is to locate a few specific, known points, and their exact location is more important than the overall distribution, using solid, distinct markers might be preferable.

## Trade-offs

- Using semi-transparent markers can make it harder to spot individual, isolated points, which can be a drawback for outlier detection tasks.
- Very small markers can be difficult to see, especially on high-resolution displays or for users with visual impairments.
- Calculating the optimal parameters can be computationally intensive and may require specialized tools or algorithms.

## Signs of Trouble

- **The "Ink Blob":** Large areas of the scatterplot are a solid color with no visible texture or detail, indicating severe overplotting.
- **Hidden Structures:** You suspect there are patterns or clusters within a dense region, but the plot is just a solid mass.
- **Inconsistent Appearance:** The same dataset plotted at different resolutions or sizes results in dramatically different and uninformative visual representations.

## How to Improve

- **Quick approach:** Manually add transparency (alpha blending) to your markers. Start with a high transparency (low opacity) and gradually increase opacity until the structure becomes clear. Also, try reducing the marker size.
- **Moderate approach:** Use visualization techniques designed for density, such as 2D histograms (heatmap) or contour plots, which explicitly encode the number of points in a given area.
- **Comprehensive approach:** Use a model-based optimization approach, as described in the source paper. These algorithms programmatically adjust visual parameters based on perceptual models to find a design that best reveals the data's structure for a given task and density.
