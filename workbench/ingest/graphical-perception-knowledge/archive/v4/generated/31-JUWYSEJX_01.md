---
id: use-elongated-marks-for-color
title: "Use Elongated Marks for Better Color Discrimination"

tags:
  - impact:perceptual
  - chart:bar
  - chart:line
  - chart:scatter
  - task:cluster
  - task:compare
  - visual:color
  - visual:shape
  - medium:screen

sources:
  - type: research
    ref: "Szafir, 2018"
    url: "https://doi.org/10.1109/TVCG.2017.2744359"
    note: "Experimentally found that colors are significantly more discriminable on elongated marks (bars, lines) than on diagonally symmetric marks (points) of the same thickness."

examples:
  - type: bad
    description: "A scatterplot uses color to distinguish between three categories of points. With a 2-pixel diameter, the colors are difficult to tell apart."
  - type: good
    description: "A line chart using the same color palette and a 2-pixel line thickness makes the categories much easier to distinguish because the elongated shape of the lines enhances color perception."
---

## Guidance

When using color to distinguish categories, prefer using elongated marks (like bars and lines) over symmetric marks (like points) of the same thickness.

## Why

Elongated marks provide more surface area and more defined edges, which enhances the human visual system's ability to perceive differences in color. Research by Szafir (2018) demonstrated that for the same color difference and mark thickness, viewers were significantly more accurate at distinguishing colors on bars and lines than on points. The benefit of elongation is asymptotic, leveling off once the mark's length is about twice its width.

## When it applies

- When choosing a chart type and color is a primary channel for encoding categorical data.
- When comparing the potential effectiveness of a colored scatterplot versus a colored line chart or bar chart for the same data.
- When you are constrained to a palette with subtle color differences and need to maximize their distinguishability.

## Exceptions

- **Inappropriate Chart Type:** The data may not be suitable for a line or bar chart (e.g., data with no temporal or ordinal relationship). A scatterplot may be the only correct representation for showing correlation between two quantitative variables.
- **High Mark Density:** Points are more effective than bars or lines in very dense visualizations, as they occupy less space and create less overlap.
- **Primary Task is Not Category Distinction:** If the main goal is to see overall trends, density, or correlation, the choice of mark shape may be less critical than other design factors.

## Trade-offs

- **Encoding Implications:** Line and bar charts imply continuity, connection, or magnitude comparison from a common baseline, which might not be appropriate for all datasets. Scatterplots are more neutral in this regard.
- **Visual Clutter:** A bar chart can be more visually cluttered than a scatterplot representing the same number of data points.

## Signs of Trouble

- **Struggling with a Scatterplot:** You find that users consistently struggle to distinguish colored categories in a scatterplot.
- **Palette Failure:** A color palette that works well in a bar chart or line chart fails completely when applied to a scatterplot with small points.

## How to Improve

- **Quick Fix: Increase Point Size.** If you must use a scatterplot, significantly increase the size of the points. This won't provide the same benefit as elongation but will still improve color discriminability.

- **Moderate Approach: Switch Chart Type.** If the data and task allow, represent your data with a chart type that uses elongated marks. For example, a time-series could be shown as a line chart instead of a scatterplot, which will make colored series easier to track.

- **Comprehensive Approach: Use a Redundant Encoding.** If you are stuck with points, add a redundant visual channel to help distinguish categories. For example, use both color and shape (e.g., circles, squares, triangles). Be aware that this can also add visual complexity.
