---
id: evaluate-colors-on-actual-marks
title: "Evaluate Color Palettes on Actual Mark Sizes, Not Legend Swatches"
tags:
  - impact:perceptual
  - impact:ethical
  - chart:scatter
  - chart:line
  - chart:map.glyphs
  - visual:color
  - task:compare
  - task:cluster
  - medium:screen
evidence:
  strength: high
  summary: "Szafir (2018) demonstrated this by applying her size-dependent models to the widely-used ColorBrewer palettes. She found that for small marks (e.g., 10-pixel scatterplot points), 13 of the 18 standard 9-step sequential ramps failed to maintain a 1-JND (Just Noticeable Difference) between consecutive colors, even though they appear distinct as large swatches."
sources:
  - type: research
    ref: "Szafir, 2018"
    url: "https://doi.org/10.1109/TVCG.2017.2744359"
    note: "Section 8, 'Discussion,' highlights that when evaluated for 10px scatterplot points, many widely-used ColorBrewer ramps lose discriminability, demonstrating the danger of relying on large-swatch evaluation."
    role: primary
tools:
  - type: validate
    name: Viz Palette
    url: https://projects.susielu.com/viz-palette
    description: "Lets you test color palettes on realistic chart mockups (including small marks) and simulate color vision deficiencies."
  - type: validate
    name: Coblis
    url: https://www.color-blindness.com/coblis-color-blindness-simulator/
    description: "Upload an image of your chart to see how it appears to users with different types of color vision deficiency."
---

## Guidance

Always test and evaluate your chosen color palette in the context of the final visualization, using the smallest marks that will appear in the chart. Do not rely solely on how colors look in a legend or color picker.

## Why

Perceived color difference is highly dependent on mark size. Large, uniform swatches in a legend or tool make colors appear far more distinct than they will as small points, thin lines, or small glyphs in the actual visualization. A palette that looks great in the legend can fail completely in the chart, leading to an unreadable and potentially misleading visualization.

## When it applies

-   For any visualization that uses color on marks that are smaller than a typical legend swatch.
-   This is especially critical for scatterplots, line charts, and maps with small glyphs.

## Exceptions

When marks are very large (e.g., large regions in a choropleth map or sizable rectangles in a treemap), the legend is a more reliable proxy for the final appearance. However, even then, testing is recommended to account for contrast effects with neighboring colors.

## Trade-offs

Evaluating in context takes slightly more time than just picking from a list of palettes. It may require creating a mockup or using a specialized tool. However, this small upfront effort prevents significant downstream problems with readability and interpretation.

## Signs of Trouble

-   **Legend Deception:** The color palette looks vibrant and clear in the legend, but the actual chart looks muddy and its colors are hard to tell apart.
-   **"Is this blue or purple?":** Viewers express confusion about which category a mark belongs to because two colors in the palette look too similar at a small size.
-   **False Groupings:** Users mistakenly perceive marks from two different categories as belonging to a single group because their colors have become indistinguishable.

## How to Improve

-   **Quick Fix: Create a "Micro-Chart" Swatch.** Instead of a standard legend with large squares, create a small, representative sample of your chart using the smallest expected mark sizes (e.g., a mini scatterplot with 5-10 dots) to see how the colors actually hold up.

-   **Moderate Approach: Test a Chart Mockup.** Create a static image of your final chart design and run it through a validation tool like Viz Palette. This allows you to check for both color discriminability and accessibility issues *at the final rendered size*.

-   **Comprehensive Approach: Integrate a Perceptual Model.** For design systems or reusable components, use or build tools that automatically adjust color ramps based on mark size parameters. The system can dynamically increase the perceptual distance between colors as the specified mark size for a chart decreases.
