---
id: balance-color-discriminability-preference
title: "Balance color discriminability with aesthetic preference for categorical palettes"
tags:
  - impact:perceptual
  - impact:aesthetic
  - impact:cognitive
  - visual:color
  - data:categorical
  - task:compare
  - audience:general

evidence:
  strength: medium
  summary: "Gramazio et al. (2016) experimentally demonstrated a core trade-off where palettes optimized for discriminability (ease of telling colors apart) were often rated as less aesthetically pleasing, and vice versa. Their Colorgorical tool is explicitly designed to help users navigate this balance."
sources:
  - type: research
    ref: Gramazio et al., 2016
    url: https://doi.org/10.1109/TVCG.2016.2598918
    note: "Primary study establishing the inverse relationship between preference and discriminability (perceptual/name distance) and creating a tool to manage it."
    role: primary
  - type: research
    ref: Schloss & Palmer, 2011
    url: https://doi.org/10.3758/s13414-010-0087-y
    note: "Establishes that preference is related to hue similarity, which is often at odds with discriminability."
    role: supporting
tools:
  - type: implement
    name: Colorgorical
    url: http://vrl.cs.brown.edu/color
    description: Generates categorical palettes by allowing users to explicitly weigh discriminability and preference factors.
  - type: implement
    name: ColorBrewer
    url: https://colorbrewer2.org/
    description: Provides distinct pre-made palettes. Qualitative palettes prioritize discriminability, while sequential/diverging palettes can be more harmonious.

examples:
  - type: good
    description: A palette for an analytical dashboard might prioritize discriminability, using highly distinct colors to ensure clarity, even if they aren't the most 'beautiful' combination.
  - type: bad
    description: Using a highly harmonious, analogous palette (e.g., several similar shades of blue and green) for a 10-category line chart, making it nearly impossible for viewers to distinguish the lines.
---
## Guidance

When choosing a color palette for categorical data, explicitly consider the trade-off between how easy the colors are to tell apart (discriminability) and how visually pleasing they are (aesthetic preference).

## Why

These two goals are often in conflict. Highly discriminable palettes, which use very different colors, can be less aesthetically pleasing. Conversely, harmonious palettes, which use similar colors, are often harder to distinguish. The optimal choice depends on the purpose of your visualization.

### Core Principle

A color palette's effectiveness is a balance between perceptual clarity and aesthetic appeal. Optimizing for one often comes at the cost of the other.

## When it applies

- When using color to distinguish between categories in any chart type (e.g., bar charts, line charts, scatter plots).
- When deciding between a pre-made palette and generating a custom one.
- When the visualization has a dual purpose of both analysis and presentation.

## Exceptions

- For purely functional, analytical tools used by experts, discriminability should almost always take priority over aesthetics.
- For purely artistic or decorative data art, aesthetic preference may be the primary or only consideration.

## Trade-offs

- **Prioritizing discriminability** may result in a palette that feels less cohesive, jarring, or fails to meet brand guidelines.
- **Prioritizing aesthetics** can make the chart harder to read accurately, increase cognitive load, and exclude users with color vision deficiencies.

## Signs of Trouble

- **The Squint Test:** If you squint at the chart, do different categories blur into one another? This signals low discriminability.
- **Audience Feedback:** Do viewers comment that the colors are "ugly" or "clash"? This signals low aesthetic preference.
- **Legend Deception:** The colors look distinct in the large swatches of the legend but are hard to tell apart as small points or thin lines in the chart itself.

## How to Improve

- **Quick approach:** For analytical charts, choose a pre-made "Qualitative" palette from a tool like ColorBrewer, which is designed for high discriminability. For presentation-focused charts, a palette with more similar hues might be acceptable.
- **Moderate approach:** Start with an aesthetically pleasing palette, and then use a tool like Viz Palette to check it for color-vision-deficiency issues. Manually adjust the lightness or saturation of any conflicting colors to increase their discriminability.
- **Comprehensive approach:** Use a tool like Colorgorical to generate a custom palette. Start with the weights for discriminability and preference balanced, then adjust them based on your primary goal (analysis vs. presentation) to find a suitable middle ground.