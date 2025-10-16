---
id: ensure-monotonic-colormap-for-legend-tasks
title: "Ensure colormaps are monotonic for tasks requiring a legend"
tags:
  - impact:perceptual
  - impact:cognitive
  - task:lookup
  - task:rank
  - data:quantitative
  - data:ordinal
  - visual:color
evidence:
  strength: high
  summary: "Theoretical proof shows that a colormap that is strictly monotonic in at least one visual attribute is guaranteed to be invertible. This means no two data values map to the same color, a necessary condition for unambiguous value lookup using a legend."
sources:
  - type: research
    ref: "Bujack et al., 2018"
    url: "https://doi.org/10.1109/SciVis.2018.8823772"
    note: "Theorem 1 proves that a strictly monotonic colormap suffices for local and global legend-based order, as monotonicity guarantees invertibility (a one-to-one mapping)."
    role: primary
examples:
  - type: bad
    description: "A colormap that fades from black to red, then back to black. A value of 0.1 and 0.9 might both be mapped to the same dark red, making it impossible to know the value from the color alone."
  - type: good
    description: "A simple grayscale colormap. Every value is mapped to a unique shade of gray, so every color on the chart corresponds to exactly one value in the legend."
---
## Guidance
For tasks that require users to look up specific values by matching a color on the chart to a color in the legend, the colormap must be monotonic in at least one of its perceptual attributes (luminance, saturation, or hue).

## Why
If a colormap is not monotonic, it can "fold back" on itself, meaning two or more different data values could be assigned the exact same color. This makes it impossible to uniquely determine the data value from its color, rendering the legend ambiguous and the lookup task impossible to complete accurately. A monotonic colormap guarantees a one-to-one mapping between data values and colors, ensuring the encoding is invertible.

### Core Principle
For a visual encoding to be unambiguously decodable with a legend, it must be invertible. Monotonicity is a sufficient condition for invertibility.

## When it applies
- Any time a chart with a continuous colormap is accompanied by a color legend or scale bar.
- When the primary task is to look up a specific value or range (e.g., "What is the temperature in this specific region?").

## Exceptions
- **Cyclical data:** A cyclical colormap will intentionally map the start and end values to the same or similar colors. This is an acceptable, deliberate design choice that reflects the cyclical nature of the underlying data (e.g., 0° and 360°).

## Trade-offs
- **Emphasis vs. Lookup:** Some non-monotonic colormaps are used to highlight specific data ranges (e.g., a "dip" to a neutral color for values around zero in a diverging scheme). This sacrifices unambiguous lookup across the entire range for the ability to emphasize a specific part of it. This should be a conscious choice based on the task priority.

## Signs of Trouble
- **Duplicate Colors:** You can find two different positions on the color legend that show the exact same color swatch.
- **"Banding" Colormaps:** Colormaps that use repeating color segments (e.g., a repeating red-green-blue pattern) are non-monotonic and make value lookup impossible.
- **User Confusion:** Viewers express confusion about what a particular color means, or misinterpret values because they cannot reliably map them back to the legend.

## How to Improve
- **Quick Fix: Check the Legend.** Visually scan the color legend for any duplicate colors or color sequences that reverse direction. If found, the colormap is not monotonic and should be replaced.
- **Moderate Approach: Choose a Standard Sequential Scheme.** Select any sequential or diverging scheme from a trusted source like ColorBrewer. These are all designed to be monotonic and therefore suitable for legend-based lookup.
- **Comprehensive Approach: Analyze the Colormap Channels.** When designing a new colormap, plot the values for each of its perceptual channels (e.g., Luminance, Chroma, Hue). Ensure that at least one of these channels is strictly increasing or decreasing across the entire range to guarantee invertibility.