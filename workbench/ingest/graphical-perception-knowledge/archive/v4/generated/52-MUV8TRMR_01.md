---
id: use-sufficient-mark-size
title: "Use sufficiently large marks for target identification tasks"

tags:
  - impact:perceptual
  - impact:cognitive
  - chart:scatter
  - chart:heatmap
  - chart:line
  - task:lookup
  - task:find-anomalies
  - visual:size
  - medium:screen
  - access:cognitive-load-risk

sources:
  - type: research
    ref: Gramazio, Schloss, & Laidlaw, 2014
    url: https://doi.org/10.1109/TVCG.2014.2346983
    note: "Experiments found that search performance was slowest for the smallest mark sizes (less than ~0.5° visual angle) and improved until plateauing at larger sizes. This holds true for both grid and scatterplot layouts."

examples:
  - type: bad
    description: A scatterplot with thousands of tiny, single-pixel dots. It is extremely difficult to locate a specific dot, and its color may be hard to discern.
  - type: good
    description: A scatterplot where marks are large enough to be clearly visible and their shape and color are unambiguous, making it easy to find a specific target.
---

## Guidance

For tasks that require finding a specific target, ensure visual marks are large enough to be easily and quickly perceived. Avoid using very small marks (e.g., those subtending less than 0.5° of visual angle).

## Why

The human visual system requires a minimum size to accurately and quickly perceive an object's features, such as its color and shape. Very small marks are difficult to differentiate from their neighbors and require more cognitive effort to process, which significantly slows down visual search tasks. Performance improves as mark size increases, up to a point where further size increases offer no additional benefit and may even be detrimental.

## When it applies

- **Task is Target Identification:** This is crucial when the viewer needs to locate a specific data point, such as finding a particular outlier in a scatterplot or a specific mutation in a genomic heatmap.
- **High-Density Plots:** In charts with many marks, small marks are especially problematic as they can easily get lost in the clutter.
- **Color or Shape Encoding:** When color or shape is a key encoding channel, marks must be large enough for the color/shape to be unambiguously perceived. Research by Stone (2012) shows perceived color can change with size.

## Exceptions

- **Task is Global Pattern Recognition:** If the primary goal is to see the overall shape of the data, trends, or density patterns (e.g., in a density plot or a scatterplot showing overall correlation), using smaller, semi-transparent marks can be more effective. Larger marks can obscure these global patterns through overplotting. The Gramazio paper's case study confirmed this: researchers preferred smaller marks for seeing global trends.
- **Extremely Large Datasets:** For datasets with millions of points, using larger marks may be impossible due to overplotting. In such cases, aggregation or sampling techniques are often a better solution than simply plotting all points.

## Trade-offs

- **Data Density vs. Legibility:** Using larger marks makes individual points more legible but reduces the number of points you can display without significant overlap (overplotting). You trade the ability to see every point for the ability to clearly see individual points.
- **Global vs. Local Views:** Larger marks prioritize local detail (finding one point) at the expense of the global view (seeing the overall trend). Smaller marks do the opposite.

## Signs of Trouble

- **Slow Search:** Users take a long time to find a specific point, even when they know what they are looking for.
- **Misidentification:** Users misinterpret the color or shape of small marks.
- **"It all blends together":** Users complain that the visualization is a "smudge" or that they can't distinguish individual points.
- **Overplotting:** Larger marks create a solid mass of color where the density and distribution of points are completely obscured.

## How to Improve

- **Quick Fix: Increase Mark Size.** Simply increase the size (e.g., pixel radius) of the marks. Test a few sizes to find the point where they are clearly legible but overplotting is still manageable.

- **Moderate Approach: Use Outlines.** Add a contrasting outline (e.g., a white or black stroke) around marks. This can improve their individual legibility even at slightly smaller sizes by separating them from the background and each other.

- **Comprehensive Approach: Dynamic Sizing or Aggregation.** For interactive visualizations, link mark size to the zoom level. At a zoomed-out level, use smaller marks, transparency, or data aggregation (e.g., hexbinning) to show global patterns. As the user zooms in, increase the mark size to reveal local detail. This resolves the trade-off between global and local views.
