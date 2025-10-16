---
id: increase-color-difference-for-small-marks
title: "Increase Perceptual Color Differences for Smaller Marks"

tags:
  - impact:perceptual
  - impact:accessibility
  - chart:scatter
  - chart:bubble
  - chart:map.glyphs
  - task:compare
  - task:distribution
  - visual:color
  - visual:size
  - medium:screen
  - medium:print
  - access:color-vision-risk

evidence:
  strength: medium
  summary: "A 2018 study found that the human ability to perceive color differences is inversely proportional to mark size. This requires significantly larger color steps (Just-Noticeable Differences or JNDs) for small marks, like points in scatterplots, than what is predicted by standard color science models."

sources:
  - type: research
    ref: "Szafir, 2018. Modeling Color Difference for Visualization Design"
    url: "https://doi.org/10.1109/TVCG.2017.2744359"
    note: "Primary study demonstrating that JNDs for color vary inversely with mark size (e.g., Table 1 shows JNDs for 6px points are ~2-3x larger than for 50px points)."
    role: primary
  - type: research
    ref: "Stone, Szafir, & Setlur, 2014. An engineering model for color difference as a function of size"
    url: "https://doi.org/10.2352/J.ImagingSci.Technol.2014.58.6.060403"
    note: "Precursor study establishing the core model for color difference as a function of size for uniform square marks."
    role: supporting

tools:
  - type: learn
    name: "VisColors Repository"
    url: "http://cmci.colorado.edu/visualab/VisColors/"
    description: "The data and infrastructure from the source paper, which can be used to model color differences."

examples:
  - type: bad
    description: "A scatterplot using a 9-step ColorBrewer palette for 10-pixel points. The study found that many of the steps in such palettes become indistinguishable at this size, causing viewers to miss details in the data."
  - type: good
    description: "A scatterplot where the color palette has been adjusted or simplified to 5 steps for small marks, ensuring each color is clearly distinct from its neighbors. Alternatively, a model like the one in the paper is used to 'boost' the differences between colors for small marks to preserve relative differences (as shown in Figure 6 of the paper)."
---

## Guidance

When using color to encode data, ensure there is a larger perceptual difference (e.g., a greater CIELAB ΔE value) between colors applied to smaller marks.

## Why

Our ability to distinguish between two colors diminishes as the size of the colored marks gets smaller. Standard color difference metrics are typically based on large, uniform patches of color and systematically underestimate the difference needed for the small marks common in visualizations like scatterplots. This can cause data values that are meant to be distinct to appear identical, leading to misinterpretation.

### Core Principle

Perceptual sensitivity is context-dependent. The effectiveness of a visual encoding, like color, changes based on other visual properties of the mark, such as its size.

## When it applies

- When using color to encode data on charts with small marks, such as scatterplots, bubble charts, or glyphs on a map.
- When designing responsive visualizations where marks may render at very small sizes on certain devices.
- When selecting a color palette with many steps (e.g., >5) for a continuous or high-cardinality categorical variable.

## Exceptions

None known. The principle that smaller marks are harder to distinguish by color is a fundamental aspect of perception. While you may choose to use larger marks to mitigate this, the principle itself still holds.

## Trade-offs

- **Fewer Distinguishable Colors:** To make colors distinguishable on small marks, you must increase the perceptual "distance" between them. This reduces the total number of distinct colors you can fit into a given palette, limiting the cardinality or granularity of the data you can display with color.
- **Aesthetic vs. Clarity:** A palette with large, perceptually-safe steps may sometimes appear less smooth or aesthetically pleasing than a finely-grained one, creating a tension between visual appeal and perceptual accuracy.

## Signs of Trouble

- **The Squint Test:** If you squint your eyes while looking at the chart, do different colored marks blend together into a single color?
- **Legend Deception:** The color ramp in your legend (which uses large swatches) looks smooth and has many clear steps, but on the chart itself (with small marks), it looks like there are only a few coarse bands of color.
- **Subtle Neighbors:** The palette contains adjacent colors (e.g., a light green and a slightly lighter green) that are impossible to tell apart on the actual chart marks.

## How to Improve

- **Quick Fix: Reduce Palette Steps.** If you are using a 9-step color ramp, try switching to a 5-step or 3-step version. This increases the perceptual distance between each remaining color, making them more distinguishable even on small marks.

- **Moderate Approach: Manually Increase Mark Size.** If possible, increase the minimum size of your marks (e.g., the radius of points in a scatterplot). This directly counteracts the problem by making all marks easier to see and their colors easier to distinguish.

- **Comprehensive Approach: Use a Size-Aware Color Model.** Use a tool or model (like the one proposed in the source paper) to programmatically generate or adjust your color palette. These models can calculate the necessary CIELAB ΔE to achieve a "just noticeable difference" (JND) for a given mark size, ensuring your palette is robust for your specific design.