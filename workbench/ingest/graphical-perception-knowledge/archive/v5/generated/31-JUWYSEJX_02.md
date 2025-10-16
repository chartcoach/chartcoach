---
id: verify-palette-for-mark-geometry
title: "Verify Color Palette Robustness for Specific Mark Geometry"

tags:
  - impact:perceptual
  - impact:ethical
  - chart:any
  - visual:color
  - visual:shape
  - visual:size
  - task:distribution
  - task:compare
  - data:cardinality.high
  - medium:screen

evidence:
  strength: medium
  summary: "A 2018 study demonstrated that popular, pre-designed color palettes like ColorBrewer can fail when applied to small or thin marks (e.g., points, lines). Many of the palette's 'perceptually distinct' steps can become indistinguishable, showing the need to validate palettes in the context of their final use."

sources:
  - type: research
    ref: "Szafir, 2018. Modeling Color Difference for Visualization Design"
    url: "https://doi.org/10.1109/TVCG.2017.2744359"
    note: "The Discussion section (Sec. 8) gives a concrete example: when evaluating ColorBrewer's 9-step sequential palettes for use on 10px scatterplot points, 13 out of 18 palettes were 'not robust,' meaning at least one color step was smaller than a Just-Noticeable Difference (JND)."
    role: primary

tools:
  - type: implement
    name: "d3-jnd"
    url: "https://github.com/connorgr/d3-jnd"
    description: "A D3 plugin (inspired by the source paper) that helps compute Just Noticeable Differences for color, accounting for mark size."
  - type: learn
    name: "ColorBrewer"
    url: "https://colorbrewer2.org/"
    description: "A widely used tool for generating map color schemes. This guideline cautions that its palettes must be validated for other chart types with different mark geometries."

examples:
  - type: bad
    description: "A line chart with 4px-thick lines using the 9-step 'YlGnBu' ColorBrewer palette. The study's analysis suggests that several steps in this palette would become perceptually indistinguishable at this thickness, flattening the appearance of the data."
  - type: good
    description: "The same line chart, but the 9-step palette has been replaced with a 5-step version. The larger perceptual distance between each of the 5 colors ensures that each step remains distinct, even on the thin lines."
---

## Guidance

Do not assume a pre-designed color palette (e.g., from ColorBrewer) is perceptually uniform for your specific chart. Always verify that its color steps remain distinguishable when applied to your chart's actual mark type (point, bar, line) and smallest expected size.

## Why

Color palettes are often designed and evaluated using large, uniform color swatches, like those you see in a legend or a tool's UI. However, the perceptual distance between colors shrinks dramatically when they are applied to small points or thin lines. A palette that appears to have many smooth, distinct steps in the legend can collapse into a few coarse, indistinguishable bands of color on the actual chart. This can obscure important patterns and mislead the viewer into thinking there is less variation in the data than actually exists.

### Core Principle

What you see in the legend is not what you get on the chart. The perception of color is heavily modulated by the geometry (shape and size) of the mark it is applied to.

## When it applies

- Whenever you use a pre-made sequential or diverging color ramp, especially one with many steps (e.g., more than 5).
- For any chart that uses small or thin marks, such as scatterplots, line charts, or small multiples.
- When creating data-driven tools or templates that will apply a standard color palette to data with unknown characteristics.

## Exceptions

- When using color for large, area-based charts like choropleth maps or treemaps, for which many standard palettes (like ColorBrewer) were originally designed. Even then, very small regions on the map can still pose a problem.
- When using a categorical palette with a small number of very distinct colors (e.g., 3-4 colors from opposite sides of the color wheel), as the perceptual distance is already very large.

## Trade-offs

- **Convenience vs. Accuracy:** Verifying and adjusting palettes takes extra effort compared to simply picking a default. This is a trade-off between the convenience of using off-the-shelf solutions and the perceptual accuracy of the final visualization.
- **Customization Effort:** Creating a truly robust palette for a specific mark geometry may require using specialized tools or writing code, which may not be feasible for all projects.

## Signs of Trouble

- **Banding:** A supposedly smooth, continuous color ramp appears as a few distinct, chunky bands of color on the chart.
- **Lost Detail:** You are encoding a continuous variable with color, but the marks on the chart make it look like the data is binned into a few categories.
- **Legend-Chart Mismatch:** The colors in the legend look like a rainbow of distinct steps, but the colors on the chart marks look like "mostly blue" or "mostly green," with little visible variation.
- **Expert Curation Isn't Enough:** You have chosen a palette curated by experts, but it still fails the "Squint Test" on your chart because it wasn't designed for your specific mark geometry.

## How to Improve

- **Quick Fix: Reduce the Number of Steps.** The easiest way to make a palette more robust is to use fewer colors. If your 9-step palette is failing, switch to the 5-step or even 3-step version. This increases the perceptual gap between each color, making them more likely to survive on small marks.

- **Moderate Approach: Test with a Simulator.** Use a color tool that can simulate how palettes appear on different mark shapes and sizes. This allows you to evaluate your chosen palette in a context closer to its final use and identify which steps are likely to fail.

- **Comprehensive Approach: Generate a Custom, Model-Based Palette.** Use a programmatic approach to generate a color ramp based on a perceptual model that accounts for mark size and shape. You can define a target "Just Noticeable Difference" (JND) and generate colors that maintain this perceptual distance for your specific mark geometry, ensuring the ramp is truly uniform in practice, not just in the legend.
