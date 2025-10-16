---
id: increase-color-difference-for-small-marks
title: "Increase Color Difference for Smaller Marks"

tags:
  - impact:perceptual
  - impact:accessibility
  - chart:scatter
  - chart:line
  - chart:bar
  - task:cluster
  - task:compare
  - task:lookup
  - visual:color
  - visual:size
  - medium:screen
  - access:color-vision-risk

sources:
  - type: research
    ref: "Szafir, 2018"
    url: "https://doi.org/10.1109/TVCG.2017.2744359"
    note: "Found that perceived color difference varies inversely with mark size. Smaller marks require a larger color distance (e.g., in CIELAB) to be reliably distinguished."

tools:
  - type: validate
    name: Viz Palette
    url: https://projects.susielu.com/viz-palette
    description: "Check how your color palette looks on different chart types and simulate color vision deficiencies."
  - type: implement
    name: d3-jnd
    url: https://github.com/connorgr/d3-jnd
    description: "A tool based on this research to calculate Just Noticeable Differences for colors, accounting for mark size."

examples:
  - type: bad
    description: "In a dense scatterplot with small points, similar colors like a light blue and a light green can become nearly indistinguishable, causing viewers to merge distinct categories."
  - type: good
    description: "The same scatterplot is adjusted by either increasing the size of the points or by choosing a palette with much greater perceptual distance between the blue and green, making them clearly distinct even at small sizes."
---

## Guidance

To ensure viewers can distinguish between categories, the perceptual difference between colors must increase as the size of the marks (points, lines, bars) decreases.

## Why

Human ability to discern color differences diminishes for smaller visual targets. What looks like a clear difference between two large color swatches may become imperceptible when applied to small points in a scatterplot or thin lines in a line chart. This can lead viewers to mistakenly group distinct categories, undermining the chart's purpose. Research shows that the "Just Noticeable Difference" (JND) for color is significantly larger for smaller marks.

## When it applies

- When using color to encode categorical or quantitative data.
- When creating visualizations that use small marks, such as scatterplots, thin line charts, or detailed maps with small glyphs.
- When the visualization is likely to be viewed on screens of varying sizes, where marks may appear smaller than intended.

## Exceptions

- If marks are very large (e.g., large regions in a choropleth map or thick bars in a simple bar chart), standard color difference metrics are more reliable.
- When color is a redundant encoding and another channel, like position or shape, is the primary means of distinguishing categories.

## Trade-offs

- **Limited Palette Size:** Increasing the perceptual distance required between colors reduces the total number of distinct colors you can use in a single palette. This may limit the number of categories you can display.
- **Aesthetic Constraints:** Requiring larger color differences may conflict with brand guidelines or aesthetic preferences that favor more subtle or harmonious palettes.

## Signs of Trouble

- **The Squint Test:** When you squint at the chart, do different colored categories blend into a single color?
- **Indistinguishable Neighbors:** Does your palette contain two similar colors (e.g., light green and teal) that are difficult to tell apart when used for small marks?
- **Legend Deception:** The colors look distinct in the large swatches of the legend but are hard to differentiate in the chart itself.
- **User Confusion:** Viewers ask "Which category is this point?" or express difficulty telling lines apart.

## How to Improve

- **Quick Fix: Increase Mark Size.** The simplest fix is to make the marks larger. Increasing the diameter of points or the thickness of lines will make any color palette more effective.

- **Moderate Approach: Adjust Your Palette.** Manually increase the perceptual distance between problematic colors in your palette. Focus on increasing differences in both lightness and chroma/saturation, not just hue. Use a tool like Viz Palette to test your changes.

- **Comprehensive Approach: Use a Size-Aware Model.** Use a tool or model (like the one proposed in the source paper) that recommends a minimum color difference based on your smallest anticipated mark size. This allows you to quantitatively ensure your palette will be robust for your specific design.
