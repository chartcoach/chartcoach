---
id: prefer-sequential-colormap-for-patterns
title: "Prefer sequential colormaps over rainbow schemes for identifying overall patterns"

tags:
  # Impact dimensions (select all that apply)
  - impact:perceptual
  - impact:cognitive

  # Chart types (use hierarchy with dots for specificity)
  - chart:map
  - chart:map.choropleth
  - chart:map.isarithmic
  - chart:heatmap

  # Tasks (what the user is trying to accomplish)
  - task:trend
  - task:distribution
  - task:rank
  - task:cluster

  # Data characteristics
  - data:quantitative
  - data:spatial

  # Visual channels
  - visual:color
  - visual:color.lightness

  # Audience characteristics
  - audience:general
  - audience:expert

  # Medium/format
  - medium:static
  - medium:screen

evidence:
  strength: medium # Options: high | medium | low
  summary: "Gołębiowska & Çöltekin (2020, n=534) found sequential colormaps were superior to rainbow for pattern interpretation tasks. On a choropleth map, accuracy in a pattern association task was significantly higher with the sequential scheme. On a region ranking task, the rainbow scheme led to significantly slower performance."

sources:
  - type: research
    ref: Gołębiowska & Çöltekin, 2020
    url: https://doi.org/10.1109/TVCG.2020.3035823
    note: "Study (n=534) comparing rainbow vs. sequential schemes on map tasks. For pattern association on choropleth maps (T7), sequential was more accurate (p=0.000). For ranking regions (T8), rainbow was slower on choropleth maps (p<0.001)."
    role: primary # Options: primary | supporting | related

tools:
  - type: implement
    name: ColorBrewer
    url: https://colorbrewer2.org/
    description: "Provides pre-built, perceptually-tested sequential color schemes ideal for pattern recognition."
  - type: learn
    name: "A Better Default Colormap for Matplotlib"
    url: https://bids.github.io/colormap/
    description: "An article explaining the design of perceptually uniform colormaps like Viridis, which are excellent for pattern recognition."
---

## Guidance

When the primary goal is for a user to identify general patterns, trends, or the overall "shape" of the data, use a sequential colormap with a smooth, monotonic lightness gradient. Avoid using rainbow colormaps for this purpose.

## Why

The human visual system is excellent at perceiving structure and patterns from smooth gradients of lightness (shading). A sequential colormap leverages this by mapping data values to a perceptually continuous scale from light to dark. This allows viewers to effortlessly see clusters, gradients, and outliers. Rainbow colormaps disrupt this process by creating harsh, artificial boundaries and non-uniform perceptual steps, which can obscure the true underlying pattern of the data.

### Core Principle

Make the most important patterns the easiest to see. Smooth, monotonic lightness changes support the pre-attentive perception of form and structure, while unordered hue changes interfere with it.

## When it applies

- The user needs to understand the overall distribution of values across a map or heatmap.
- The task is to identify clusters, hot spots, or areas of high/low concentration.
- The user is trying to determine the direction of a trend or gradient in the data.
- Tasks like "find the area with the highest concentration" or "describe the overall pattern."

## Exceptions

- If the primary task is to look up a specific value by matching a color to a legend, and pattern recognition is not important. In this limited case, the distinct hues of a rainbow map can be faster (though this is a significant trade-off).

## Trade-offs

- **Detail vs. Gestalt:** A sequential scheme excels at showing the overall pattern (gestalt), but its subtle variations may make it slightly slower to identify a specific value compared to a high-contrast rainbow scheme. However, this can be easily mitigated with interactive tooltips.

## Signs of Trouble

- **Can't See the Forest for the Trees:** Viewers can name the color of any given point but struggle to describe the overall trend or shape of the data.
- **Artificial "Contour Lines":** The chart looks more like a contour map with sharp, colorful edges, even if the underlying data is smooth.
- **Misinterpreted Gradients:** Viewers incorrectly describe the direction or steepness of a change in the data because of the non-uniform steps in the rainbow palette.

## How to Improve

- **Quick Fix: Switch to a Single-Hue Sequential Scheme.** In your visualization tool, change the colormap from "Rainbow" or "Jet" to a sequential one like "Blues," "Greens," or "Reds." This immediately provides a monotonic lightness ramp that will reveal patterns more clearly.

- **Comprehensive Approach: Use a Perceptually Uniform Multi-Hue Scheme.** Adopt a colormap like Viridis, Plasma, or Cividis. These schemes are designed to be perceptually uniform, meaning a certain step in the data corresponds to a same-sized perceptual step in the color. They vary in lightness monotonically (making them great for patterns) but also shift in hue, making them more visually rich and robust for people with color vision deficiencies.
