---
id: increase-color-difference-for-small-marks
title: "Increase Color Differences for Smaller Marks"
tags:
  - impact:perceptual
  - impact:accessibility
  - chart:scatter
  - chart:line
  - chart:map.glyphs
  - task:compare
  - task:cluster
  - visual:color
  - access:color-vision-risk
  - medium:screen
evidence:
  strength: high
  summary: "Szafir (2018, n=461) experimentally quantified that perceived color difference varies inversely with mark size. For example, a 6-pixel scatterplot point requires a ~50% larger color difference (in CIELAB L*) to be as discriminable as a 50-pixel point. These findings provide visualization-specific models that build upon and confirm prior work in color science."
sources:
  - type: research
    ref: "Szafir, 2018"
    url: "https://doi.org/10.1109/TVCG.2017.2744359"
    note: "Crowdsourced experiments (n=461) across three chart types (points, bars, lines) provided probabilistic models for color difference as a function of mark size and shape. Found that a 2° point has a JND ~3x larger than predicted in controlled lab settings."
    role: primary
  - type: research
    ref: "Stone et al., 2014"
    url: "https://dl.acm.org/doi/10.2352/ISSN.2169-2629.2014.26.46"
    note: "Provided an initial engineering model for color difference as a function of size for isolated square marks, which Szafir (2018) extends to visualization contexts."
    role: supporting
tools:
  - type: validate
    name: Viz Palette
    url: https://projects.susielu.com/viz-palette
    description: "Simulates color palettes for different chart types and for users with color vision deficiency, helping you see how colors look on small marks."
  - type: implement
    name: d3-jnd
    url: https://github.com/connorgr/d3-jnd
    description: "A JavaScript library that implements the perceptual models from Szafir (2018) to create size-aware color scales."
---

## Guidance

Use perceptually larger color differences for smaller visual marks, such as points in a scatterplot or thin lines in a line chart.

## Why

The human visual system's ability to distinguish between two colors diminishes as the size of the colored objects decreases. Colors that appear distinct as large swatches may become indistinguishable when rendered as small marks in a chart, leading to misinterpretation.

### Core Principle

The perceived difference between two colors is not constant; it depends on the context in which they are viewed, especially the size of the marks.

## When it applies

-   When using color to encode categorical or quantitative data on small marks (e.g., less than 20 pixels wide).
-   In chart types that rely on small marks, such as scatterplots, line charts, or maps with small point glyphs.

## Exceptions

When marks are large and uniformly shaped (e.g., large regions in a choropleth map or large rectangles in a treemap), the effect of size is less pronounced. In these cases, standard color differences may suffice, although contrast with neighboring colors remains a concern.

## Trade-offs

Using larger color differences between steps reduces the total number of discernible steps available within a given color ramp. This may limit the granularity of the data you can represent (i.e., you can have fewer categories or bins).

## Signs of Trouble

-   **The Squint Test:** If you squint at your chart, marks from different categories blend into a single color.
-   **Indistinguishable Points:** In a scatterplot, points from different categories appear to have the same color, forcing users to constantly reference the legend.
-   **Legend Deception:** The color palette looks clear and distinct in the legend (with its large color swatches) but fails in the actual chart where marks are small.

## How to Improve

-   **Quick Fix: Reduce Categories or Bins.** If possible, simplify the color encoding by reducing the number of distinct colors needed. This allows you to use a smaller set of more distinct colors for the remaining groups.

-   **Moderate Approach: Manually Increase Color Distance.** When selecting your palette, intentionally pick colors that are farther apart in a perceptual color space (like CIELAB or LCH). As a heuristic, aim for a CIELAB ΔE2000 of at least 10 for small marks, rather than the classic "just noticeable" difference of 1.

-   **Comprehensive Approach: Use a Size-Aware Tool.** Use a tool or library that models size-dependent color perception. For example, `d3-jnd` implements the models from this research, allowing you to generate color palettes that are guaranteed to be discriminable at a specific mark size.
