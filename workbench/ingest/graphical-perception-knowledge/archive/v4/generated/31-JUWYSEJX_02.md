---
id: test-colors-on-actual-marks
title: "Test Color Palettes on Target Mark Types and Sizes, Not Large Swatches"

tags:
  - impact:perceptual
  - impact:ethical
  - impact:aesthetic
  - chart:scatter
  - chart:line
  - chart:bar
  - visual:color
  - visual:size
  - visual:shape
  - medium:screen
  - medium:print
  - access:color-vision-risk

sources:
  - type: research
    ref: "Szafir, 2018"
    url: "https://doi.org/10.1109/TVCG.2017.2744359"
    note: "The paper's core finding is that color perception is context-dependent on mark size and shape. This makes testing with large swatches an unreliable proxy for performance in a real chart."

tools:
  - type: validate
    name: Viz Palette
    url: https://projects.susielu.com/viz-palette
    description: "Lets you apply a color palette to simulated chart types to see how it performs in context and for colorblind users."
  - type: validate
    name: Color Blindness Simulator (Coblis)
    url: https://www.color-blindness.com/coblis-color-blindness-simulator/
    description: "Upload an image of your chart to see how it would appear to people with different types of color vision deficiency."

examples:
  - type: bad
    description: "A designer chooses a categorical palette based on large color squares in a style guide. When applied to a dense scatterplot, the colors become indistinguishable."
    url: "https://raw.githubusercontent.com/d3/d3-scale-chromatic/main/img/schemeCategory10.png"
  - type: good
    description: "Before finalizing the palette, the designer creates a small mockup of the scatterplot with the proposed colors to confirm they are still distinct at the target mark size. They also run a screenshot through a color blindness simulator."
---

## Guidance

Always evaluate the distinguishability of your color palette using the actual mark types (points, bars, lines) and sizes that will appear in the final visualization. Do not rely on the large color swatches typically shown in palette pickers or style guides.

## Why

Perceived color difference is highly dependent on context, especially the size and shape of the colored mark. A palette that looks vibrant and clear with large, uniform color blocks can fail completely when applied to small points or thin lines. Relying on large swatches leads to an overestimation of color differences, resulting in charts where viewers cannot reliably distinguish between categories, potentially leading to data misinterpretation.

## When it applies

- This is a universal best practice when designing or choosing a color palette for any data visualization.
- It is especially critical when visualizations contain small marks (e.g., < 10 pixels wide) or when designing for accessibility.

## Exceptions

- There are no known exceptions. Testing visual elements in their final context is a fundamental design principle.

## Trade-offs

- **Increased Effort:** This requires more effort than simply picking a pre-made palette from a dropdown menu. It may involve creating mockups, using specialized testing tools, or prototyping. However, this upfront effort prevents much larger problems with chart legibility later on.

## Signs of Trouble

- **"It looked fine in Figma!":** The most common sign is when a palette chosen in a design tool (where colors are often represented as large shapes) results in an illegible chart.
- **Legend-Chart Mismatch:** The colors in the legend appear clearly different, but those same colors are ambiguous when used on small marks within the chart.
- **Relying on Hue Alone:** The palette relies mostly on changes in hue (e.g., red, green, blue) without sufficient variation in lightness or saturation, which is a common cause of failure at small sizes.

## How to Improve

- **Quick Fix: Create a "Stress Test" Legend.** In your design file or on the chart itself, create a small test area. Instead of showing legend colors as large squares, show them as small circles (e.g., 4-pixel diameter) or thin lines (e.g., 2-pixels thick) placed close together. This gives a much better approximation of in-chart performance.

- **Moderate Approach: Use a Validation Tool.** Use a tool like Viz Palette. Paste in your list of hex codes to instantly see how your palette performs on different simulated chart types (bars, lines, areas) and how it appears to users with various forms of color vision deficiency.

- **Comprehensive Approach: Integrate Testing into Your Design System.** If you work with a design system, specify that color palettes must be tested and approved not just as abstract swatches, but also on mockups of key chart types with minimum mark sizes. Provide guidance on minimum perceptual distances for different contexts.
