---
id: use-perceptually-uniform-colormaps
title: "Use perceptually uniform colormaps for continuous data"
tags:
  - impact:perceptual
  - impact:ethical
  - impact:accessibility
  - data:quantitative
  - visual:color
  - access:color-vision-risk
  - chart:heatmap
  - chart:map.choropleth

evidence:
  strength: high
  summary: "Bujack et al. (2018) demonstrate that simple monotonicity in a single color channel (e.g., luminance) is insufficient for perceptual order, as uncontrolled variations in other channels can break the ordering. Perceptually uniform colormaps (like those designed in CIELAB or Oklab space) control for these interactions, ensuring that a given step in data corresponds to a perceptually equal step in color, which is critical for accurate data interpretation."

sources:
  - type: research
    ref: Bujack et al., 2018
    url: https://doi.org/10.1109/SciVis.2018.8823772
    note: "Provides counter-examples (Fig. 1) showing that colormaps monotonic in hue, saturation, or luminance alone can still fail to be perceptually ordered. This demonstrates the need for comprehensive control over perceptual dimensions."
    role: primary
  - type: standard
    ref: "d3-scale-chromatic"
    url: https://github.com/d3/d3-scale-chromatic
    note: "A widely-used visualization library that provides perceptually-uniform colormaps (like viridis, cividis) as a best-practice standard for data visualization on the web."
    role: related
  - type: practitioner
    ref: "A new colormap for Matplotlib"
    url: https://www.youtube.com/watch?v=xAoljeRJ3lU
    description: "Talk by the creators of the viridis colormap explaining the importance of perceptual uniformity and the process of designing such a map."
    role: learn

tools:
  - type: implement
    name: "Chroma.js"
    url: https://gka.github.io/chroma.js/
    description: "A JavaScript library for color conversions and scale generation that works in perceptually-uniform color spaces like L*a*b* and Lch."
  - type: validate
    name: "Vischeck"
    url: http://www.vischeck.com/
    description: "A tool that simulates color vision deficiency, allowing you to check if your colormap is readable by a wider audience."
---
## Guidance
For continuous data, prefer colormaps where steps in the data value correspond to perceptually uniform steps in color. These are often labeled as "perceptually uniform" and include palettes like `viridis`, `cividis`, or those designed in the CIELAB color space.

## Why
Many simple color gradients are not perceptually uniform. For example, a basic ramp from pure blue to pure yellow in RGB space has a large, sudden perceptual jump in the middle (where it becomes a muted gray/green) and smaller changes at the ends. This visual distortion misrepresents the data, making some data changes seem larger and others smaller than they actually are. Perceptually uniform colormaps prevent this by ensuring a 10% change in the data looks like a 10% change in color, everywhere along the scale.

### Core Principle
The perceived magnitude of change in a visualization should accurately reflect the true magnitude of change in the data.

## When it applies
- When mapping a continuous quantitative variable to a color gradient, such as in a heatmap, a choropleth map, or a 3D surface plot.
- When creating any sequential or diverging color scale for data analysis.

## Exceptions
- **Highlighting Thresholds:** A non-uniform colormap can be used intentionally as a special effect to highlight a specific, critical threshold in the data. This should be a deliberate, documented choice, not an accidental artifact of a poor palette.
- **Artistic Visualization:** In non-analytical, artistic contexts, aesthetic goals may override the need for perceptual accuracy.

## Trade-offs
- Creating a truly perceptually uniform colormap from scratch is technically difficult. It is almost always better to use well-vetted, pre-built options provided by visualization libraries and tools.
- Some perceptually uniform palettes may appear less saturated or vibrant than less accurate but more "colorful" alternatives.

## Signs of Trouble
- **Banding:** Your smooth color gradient appears to have discrete, sharp steps or bands.
- **Washed-out Zones:** A large range of your data is mapped to a small, hard-to-distinguish range of colors (often in the middle or at the ends of the scale).
- **Hotspots:** A small range of data values is mapped to a highly salient color range (like a bright yellow) that draws disproportionate attention.
- **Grayscale Information Loss:** When the color map is converted to grayscale, some details or ordering disappear, indicating it relied on hue in a non-uniform way.

## How to Improve
- **Quick Fix: Use a Better Pre-built Palette.** Instead of defining a gradient yourself (e.g., `"blue", "white", "red"`), use a pre-built, perceptually-uniform option from a library like D3 (`interpolateViridis`), Matplotlib (`viridis`), or a sequential scheme from ColorBrewer.
- **Moderate Approach: Analyze Your Palette.** Use a tool like Viz Palette to plot your current colormap's lightness, chroma, and hue profiles. If any of these lines are not smooth and monotonic (especially lightness), the map is not uniform. Use the tool to find a better alternative.
- **Comprehensive Approach: Build in a Perceptual Space.** If you need to create a custom or branded palette, construct your gradients using a color space designed for perceptual uniformity (like HCL, L\*a\*b\*, or Oklab) rather than legacy spaces like RGB or HSL. Tools like Chroma.js can facilitate this.