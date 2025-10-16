---
id: avoid-rainbow-colormaps-for-ordered-data
title: "Avoid rainbow colormaps for ordered data"
tags:
  - impact:perceptual
  - impact:cognitive
  - impact:accessibility
  - chart:heatmap
  - chart:map.choropleth
  - task:rank
  - task:trend
  - task:lookup
  - data:quantitative
  - data:ordinal
  - visual:color
  - visual:color.hue
  - access:color-vision-risk
evidence:
  strength: high
  summary: "Theoretical proofs and extensive empirical research show that the perceptual ordering of hues in a rainbow is ambiguous and its luminance is non-monotonic, leading to misinterpretation of data."
sources:
  - type: research
    ref: "Bujack et al., 2018"
    url: "https://doi.org/10.1109/SciVis.2018.8823772"
    note: "Provides theoretical proof that a full hue circle lacks global intrinsic order because it is periodic, mathematically validating why rainbow schemes fail for ordered data."
    role: primary
  - type: research
    ref: "Borland & Taylor, 2007"
    url: "https://doi.org/10.1109/MCG.2007.323435"
    note: "Classic paper summarizing the perceptual problems of rainbow colormaps, such as non-monotonic luminance and ambiguous ordering."
    role: supporting
  - type: research
    ref: "Ware, 1988"
    url: "https://doi.org/10.1109/38.7760"
    note: "Points out that a monotonic change in luminance is critical for seeing the overall form of data, a property that rainbow colormaps violate."
    role: related
tools:
  - type: implement
    name: ColorBrewer
    url: https://colorbrewer2.org
    description: "Provides pre-built, perceptually-sound sequential and diverging color schemes as alternatives to rainbow palettes."
  - type: validate
    name: Viz Palette
    url: https://projects.susielu.com/viz-palette
    description: "Helps you analyze a colormap's luminance profile and simulate for color vision deficiencies."
  - type: learn
    name: "Cynthia Brewer's Color Use Guidelines"
    url: https://web.archive.org/web/20220120192534/https://www.personal.psu.edu/cab38/ColorSch/Schemes.html
    description: "Explains the principles behind designing effective color schemes for maps and visualizations."
examples:
  - type: bad
    description: "A typical weather map using a rainbow colormap to show temperature. The bright yellow band creates a false impression of an extreme region, while the ordering of other colors is difficult to discern without constantly checking the legend."
  - type: good
    description: "A choropleth map using the 'Viridis' colormap or a ColorBrewer sequential scheme (e.g., 'YlGnBu'). The color smoothly transitions from a light color to a dark color, making it easy to perceive which areas have lower or higher values."
---
## Guidance
Do not use a full-spectrum rainbow (or similar multi-hue schemes with non-monotonic luminance) to represent continuous quantitative or ordinal data.

## Why
The order of hues in a rainbow is not perceptually intuitive. Furthermore, the luminance (lightness) of hues in a standard rainbow colormap is not monotonic—yellow is much lighter than adjacent green and red, and blue is very dark. This creates misleading "stripes" in the data and makes it impossible to correctly judge the magnitude and order of values without constantly referring to a legend.

### Core Principle
The visual ordering of an encoding should match the data's inherent order. A visually unordered color scheme fundamentally misrepresents ordered data, hindering accurate perception.

## When it applies
- When encoding continuous or ordered discrete data (e.g., temperature, elevation, density, pressure).
- In any chart type that uses a continuous color scale, such as heatmaps, choropleth maps, or surface plots.

## Exceptions
- **Cyclical data:** A carefully designed circular colormap may be appropriate for cyclical data (e.g., time of day, wind direction, phase), where the start and end values are conceptually adjacent.
- **Purely categorical data:** If the goal is purely segmentation into distinct, unordered categories (e.g., a political map of countries), a multi-hue palette is appropriate. However, this is a categorical task, not a quantitative one.

## Trade-offs
- **Aesthetics vs. Clarity:** Rainbow colormaps are often perceived as more colorful or engaging. Replacing them with a perceptually ordered scheme might be seen as less visually vibrant, but it dramatically improves data fidelity and interpretability.

## Signs of Trouble
- **False Boundaries:** You see sharp "stripes" or bands of color (especially yellow or cyan) that don't correspond to significant features in the data.
- **Ambiguous Order:** It's unclear whether yellow represents a higher or lower value than a neighboring green without checking the legend.
- **Inconsistent Lightness:** Colors that are far apart in the data values (e.g., blue and red) may appear more similar in lightness than colors that are close (e.g., yellow and green).

## How to Improve
- **Quick Fix: Switch to Grayscale.** A simple black-to-white gradient guarantees perfect perceptual order and is a safe, immediate improvement. The trade-off is a loss of color's discriminative power.
- **Moderate Approach: Use a Single-Hue Sequential Scheme.** Select a scheme from a tool like ColorBrewer that progresses from a light shade of a single color to a dark one (e.g., light blue to dark blue). This provides a clear "low-to-high" progression.
- **Comprehensive Approach: Use a Perceptually-Uniform Multi-Hue Scheme.** Adopt a colormap like Viridis, Magma, Plasma, or Cividis. These are specifically designed to have monotonically increasing luminance while traveling through multiple hues, offering high discriminative power, guaranteed perceptual order, and improved robustness for viewers with color vision deficiencies.