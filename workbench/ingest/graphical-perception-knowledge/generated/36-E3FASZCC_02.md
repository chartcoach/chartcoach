---
id: avoid-cyclical-colormaps-for-linear-data
title: "Avoid cyclical colormaps for linear data"
tags:
  - impact:perceptual
  - impact:ethical
  - data:quantitative
  - data:ordinal
  - visual:color
  - access:color-vision-risk
  - chart:heatmap
  - chart:map.choropleth

evidence:
  strength: high
  summary: "Bujack et al. (2018) prove mathematically that cyclical hue maps (like a rainbow) cannot satisfy global perceptual order because their start and end points are the same. Decades of research, summarized by sources like Borland & Taylor (2007), show they create false boundaries and obscure true data patterns, leading to a high risk of misinterpretation."

sources:
  - type: research
    ref: Bujack et al., 2018
    url: https://doi.org/10.1109/SciVis.2018.8823772
    note: "Theoretically proves that a full hue map is periodic and therefore cannot satisfy global intrinsic order (Theorem 4), meaning it is not perceptually ordered from end to end."
    role: primary
  - type: research
    ref: Borland & Taylor, 2007
    url: https://doi.org/10.1109/MCG.2007.323435
    note: "Classic paper titled 'Rainbow Color Map (Still) Considered Harmful,' which demonstrates how rainbow colormaps create misleading visual artifacts and obscure data features compared to perceptually ordered schemes."
    role: supporting
  - type: practitioner
    ref: "IBM Design Language: Data-visualization color palettes"
    url: https://www.ibm.com/design/language/data-visualization/color-palettes/
    note: "Professional style guide explicitly warns against using rainbow palettes for continuous data due to lack of perceptual order and accessibility issues."
    role: related

tools:
  - type: implement
    name: viridis colormaps
    url: https://bids.github.io/colormap/
    description: "A set of perceptually-uniform, colorblind-friendly colormaps (viridis, plasma, magma, inferno, cividis) designed to replace the rainbow default."
  - type: learn
    name: "The End of the Rainbow"
    url: https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2004EO400002
    description: "A concise, accessible article explaining the perceptual problems with rainbow colormaps."
---
## Guidance
Do not use a rainbow or other cyclical colormap to represent continuous or ordered data that is linear (i.e., goes from a low value to a high value).

## Why
Cyclical colormaps, like the rainbow, are not perceptually ordered. They have two major flaws:
1.  **False Boundaries:** Abrupt changes in hue and luminance (e.g., the sharp transition from yellow to green) create artificial "bands" in the visualization, suggesting significant shifts in the data where none exist.
2.  **Obscured Extremes:** They bring dissimilar values visually close together. In a rainbow, the low-value reds and high-value violets can appear similar, making it hard to interpret the data's true range.

Using a rainbow colormap is a common way to inadvertently mislead your audience.

### Core Principle
The perceptual distance between colors should correspond to the data distance between the values they represent. Cyclical colormaps violate this principle by creating non-uniform perceptual steps.

## When it applies
- When mapping a continuous quantitative variable (e.g., temperature, elevation, sales) to a color gradient.
- When creating heatmaps, choropleth maps, or other visualizations that use a color ramp for linear data.

## Exceptions
- **Periodic Data:** The only correct use for a cyclical colormap is for data that is itself cyclical or periodic. For example, direction (0-360 degrees), angle, or time of day. In these cases, the cyclical encoding correctly matches the structure of the data where the start and end points are adjacent.

## Trade-offs
- Rainbow colormaps are often the default in older scientific software and may be familiar to certain expert audiences. Replacing a rainbow with a more perceptually appropriate scheme (like `viridis`) might meet initial resistance but will ultimately lead to more accurate interpretations.

## Signs of Trouble
- **Banding:** The visualization shows distinct stripes of color (e.g., a bright yellow band) that don't correspond to any specific feature in the data.
- **Similar Extremes:** The colors representing the lowest and highest values in your data range look visually similar.
- **Grayscale Chaos:** When you convert the visualization to grayscale, it becomes an unordered mess of light and dark patches, indicating the order was dependent on hue alone.

## How to Improve
- **Quick Fix: Use a Better Default.** Instead of `jet` or `rainbow`, switch to a modern, perceptually-uniform default like `viridis`, `plasma`, or `cividis`, which are available in most modern plotting libraries (e.g., Matplotlib, D3).
- **Moderate Redesign: Choose the Right Palette Type.** Explicitly choose a "sequential" color palette (for 0 to max data) or a "diverging" palette (for -max to +max data) from a trusted source like ColorBrewer.
- **Comprehensive Approach: Educate Your Team.** If rainbow palettes are common in your organization, share articles or examples demonstrating their perceptual flaws. Work to change the default settings in your team's tools to promote the use of perceptually-uniform palettes.