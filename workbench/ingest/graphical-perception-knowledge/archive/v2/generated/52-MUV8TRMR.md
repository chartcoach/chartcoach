---
id: use-sufficiently-large-marks
title: "Use sufficiently large marks for target search tasks"
impact:
  - perceptual
  - performance
  - cognitive
tags:
  - size
  - mark-size
  - scatterplot
  - target-search
  - find-anomalies
  - legibility
  - performance

sources:
  - type: research
    ref: "Gramazio, Schloss, & Laidlaw, 2014"
    url: https://doi.org/10.1109/TVCG.2014.2346983
    note: "Found that search time to find a target significantly slows when mark size is below ~0.5° of visual angle. Performance improves as size increases, eventually plateauing for larger marks."

examples:
  - type: bad
    description: "A dense scatterplot where each point is rendered as a single pixel. It is nearly impossible to find a specific point or distinguish between overlapping marks without zooming."
  - type: good
    description: "A scatterplot where points have a sufficient radius (e.g., 3-5 pixels) so that their color and shape are clearly visible, making it easy to scan for specific targets."
---

## Guidance

Ensure visual marks (like points in a scatterplot or cells in a grid) are large enough to be easily and quickly identified. For tasks that require finding a specific item, avoid using very small marks.

## Why

Human visual search performance is significantly slower for smaller marks. Tiny marks are harder to process, increasing the time and cognitive effort required to locate a target. Research shows a steep performance penalty for the smallest marks, with search times decreasing as mark size increases, until performance plateaus at a sufficient size. Using marks that are large enough improves search speed and reduces user frustration.

## When it applies

- When a primary user task is to **find a specific item** (target search) or **identify an anomaly** in a chart.
- When designing visualizations that use discrete marks, such as **scatterplots**, **dot plots**, **bubble charts**, or **grid-based heatmaps**.
- When the visualization will be viewed on displays where marks might otherwise render as just a few pixels.

## Exceptions

If the primary goal is to show the **overall distribution, density, or global pattern** of the data, using smaller marks can be more effective. Smaller marks reduce overplotting in dense datasets and allow the high-level structure to emerge more clearly. In this case, the task is not to find an individual point, but to see the "shape" of the data as a whole.

## Trade-offs

- **Legibility vs. Data Density:** Larger marks are more legible but take up more space. This can lead to increased occlusion (overlap) in dense visualizations, which can obscure other data points.
- **Clarity vs. Precision:** In some cases, very large marks might obscure the precise location of the data point, trading some positional accuracy for faster identification.

## Evaluate

- [ ] Are marks so small that they are difficult to see or distinguish from one another?
- [ ] Does it take a noticeable amount of time and effort to locate a specific point you are looking for?
- [ ] On a scatterplot, do the points look like indistinct, single-pixel dots?

## Repair

1.  **Increase mark size.** This is the most direct fix. In most tools, this means increasing the point radius, symbol size, or cell size.
2.  **Use opacity to manage overlap.** If increasing mark size causes too much occlusion in dense areas, apply partial transparency (e.g., alpha = 0.5) to reveal underlying points.
3.  **Provide a filtering or faceting mechanism.** If the dataset is too dense, allow users to filter the data or split it into small multiples to reduce the number of marks displayed at one time, making each one easier to see.