---
id: match-scatterplot-design-to-task-data
title: "Match Scatterplot Design to Task and Data"

impact:
  - perceptual
  - cognitive
  - logos
  - ethical
  - performance
tags:
  - scatterplot
  - design-process
  - task-analysis
  - data-characteristics
  - overplotting
  - density
  - correlation
  - cluster-analysis

sources:
  - type: research
    ref: Sarikaya & Gleicher, 2017
    url: https://doi.org/10.1109/TVCG.2017.2744184
    note: "Provides the core framework for linking scatterplot tasks (e.g., finding clusters), data characteristics (e.g., number of points), and design choices (e.g., binning)."
  - type: research
    ref: Zeng & Battle, 2023
    url: https://doi.org/10.1145/3544548.3581349
    note: "Details the methodology for collating this knowledge from research papers into a structured format."

tools:
  - type: implement
    name: d3-twodim
    url: https://uwgraphics.github.io/d3-twodim/
    description: "A D3.js library for creating various scatterplot-like designs, mentioned in the source paper."

examples:
  - type: good
    description: "The source paper (Sarikaya & Gleicher, 2017, Fig. 1) shows how a traditional scatterplot is best for few points, a binned scatterplot is better for revealing density with many points, and a density-based design (Splatterplot) is effective for overlapping distributions."
  - type: bad
    description: "A scatterplot of 10,000 data points where all points are rendered as opaque circles, resulting in a 'hairball' where density and distribution are impossible to perceive."
---

## Guidance

Consciously choose your scatterplot design by considering the viewer's specific task and the characteristics of your data. A one-size-fits-all approach to scatterplots often fails with complex or large datasets.

## Why

A standard scatterplot, where every data point gets its own mark, can become ineffective with large datasets. This leads to "overplotting"—a dense mess of overlapping points that hides patterns, obscures density, and can mislead viewers.

Different designs, like binning or density plots, are optimized for specific tasks (e.g., assessing distribution) and data scales (e.g., thousands of points). Matching the design to the context improves analytical accuracy and makes the chart's message clearer.

## When it applies

- When creating any scatterplot, especially for exploratory analysis.
- When a standard scatterplot suffers from overplotting, creating a "hairball" effect.
- When the primary analytical task is not just identifying individual points but assessing **distribution**, **density**, or **clusters**.
- When visualizing datasets with more than a few hundred points.

## Exceptions

- For very small, simple datasets (e.g., under 100 points), a traditional scatterplot is usually sufficient, effective, and easy for any audience to understand.
- When there is a strict requirement to show every single data point without any aggregation, even if it results in overplotting.

## Trade-offs

- **Clarity vs. Fidelity:** Advanced designs like binning or contour plots improve the clarity of aggregate patterns (like density) but sacrifice the ability to see and interact with individual data points precisely.
- **Simplicity vs. Complexity:** A traditional scatterplot is simple to create and universally understood. Alternative designs can be more complex to implement and may require more explanation for an audience unfamiliar with them.

## Evaluate

- [ ] Does the chart have dense, opaque blobs of points where you can't distinguish individual marks or judge the data's density?
- [ ] Does the design make the primary analytical task difficult? (e.g., trying to see clusters in a chart that only shows individual points)
- [ ] Does an aggregation technique (like binning) hide important features, such as critical outliers?

## Repair

1.  **For minor overplotting:** Start by reducing point size or applying transparency (alpha blending) to reveal areas of higher density.
2.  **To emphasize density:** Switch from individual points to an aggregated representation. Use 2D binning (where color indicates the number of points in a grid cell) or contour lines.
3.  **To see clusters and outliers:** Use a density-based plot (like a Splatterplot) that groups dense regions together but still renders sparse, individual points as outliers. This gives a hybrid view of both the forest and the trees.