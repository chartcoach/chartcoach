---
id: avoid-rainbow-colormaps
title: "Avoid rainbow colormaps for quantitative data"

tags:
  - impact:perceptual
  - impact:accessibility
  - chart:map
  - chart:heatmap
  - data:quantitative
  - visual:color
  - access:color-vision-risk

evidence:
  strength: high
  summary: "Liu & Heer (2018) found the 'jet' rainbow colormap performed worst among 9 tested schemes for both speed and accuracy in a relative distance judgment task. This confirms longstanding critiques that it lacks perceptual ordering, creates false boundaries, and is not friendly to common forms of color vision deficiency."

sources:
  - type: research
    ref: Liu & Heer, 2018
    url: https://doi.org/10.1145/3173574.3174172
    note: "Empirical study (n=56 per group) showed the 'jet' rainbow colormap was the slowest and most error-prone for quantitative comparison tasks, concluding it 'should be jettisoned'."
    role: primary
  - type: research
    ref: Borland & Taylor, 2007
    url: https://doi.org/10.1109/MCG.2007.323435
    note: "A widely cited paper arguing that rainbow colormaps are 'considered harmful' because they lack perceptual ordering and can obscure or create misleading data features."
    role: supporting
  - type: research
    ref: Zeng & Battle, 2023
    url: https://doi.org/10.1145/3544548.3581349
    note: "Review paper that notes the ineffectiveness of rainbow colormaps, citing Liu & Heer [58] who found it 'performs the worst for ordering colors and should be jettisoned'."
    role: related

tools:
  - type: implement
    name: viridis
    url: https://bids.github.io/colormap/
    description: "A family of perceptually uniform colormaps designed to be readable by people with common forms of color blindness, now the default in many scientific tools."
  - type: validate
    name: Viz Palette
    url: https://projects.susielu.com/viz-palette
    description: "Tool to test color palettes for colorblind safety and perceptual distance."
  - type: learn
    name: "A Better Default Colormap for Matplotlib"
    url: https://www.youtube.com/watch?v=xAoljeRJ3lU
    description: "A talk by the creators of viridis explaining the problems with rainbow colormaps and the design of perceptually uniform alternatives."
---

## Guidance

For encoding continuous quantitative data, avoid using the "rainbow" (or "jet") colormap that cycles through all hues of the spectrum (blue-cyan-green-yellow-red).

## Why

The rainbow colormap is not perceptually ordered. The order of hues in the spectrum does not correspond to a naturally perceived order of magnitude, leading to inaccurate interpretations of data. It can create misleading visual artifacts, such as sharp boundaries where none exist in the data, and it can mask subtle variations. Furthermore, it is not accessible to users with common forms of color vision deficiency.

### Core Principle

Visual encodings should match the structure of the data and the task. Ordered data, like quantitative values, requires a visual encoding that is clearly perceived as ordered.

## When it applies

- When visualizing continuous quantitative data, such as in heatmaps, choropleth maps, or scientific visualizations (e.g., temperature, pressure, elevation).
- When the goal is for viewers to accurately judge the magnitude of values or compare differences between regions.

## Exceptions

None known. While the rainbow colormap is still prevalent in some scientific domains due to historical convention, its perceptual flaws make it a poor choice for effective and accurate data communication. One study (Liu & Heer, 2018) found a single edge case where color name boundaries in a rainbow map aided a specific judgment, but this was an anomaly and does not outweigh the significant overall drawbacks.

## Trade-offs

- **Familiarity vs. Clarity:** In some expert communities, the rainbow colormap is conventional. Switching to a better alternative may require a brief adjustment period for the audience but will ultimately lead to more accurate interpretation.
- **Aesthetics vs. Accuracy:** Some may find the vibrant colors of a rainbow map more visually engaging, but this comes at the high cost of perceptual accuracy and accessibility.

## Signs of Trouble

- **False Boundaries:** The chart appears to have sharp bands of color (e.g., a distinct yellow band between green and red) that don't correspond to a sudden change in the underlying data.
- **Colorblind Invisibility:** When viewed with a color vision deficiency simulator (e.g., deuteranopia), large portions of the color scale become indistinguishable, appearing as a uniform block of brownish-yellow.
- **Ambiguous Order:** It's unclear whether yellow represents a higher or lower value than green without constantly referencing the legend.
- **Hidden Features:** Subtle but important variations in the data are not visible because they fall within a single broad color band (like the wide green area in a typical rainbow map).

## How to Improve

- **Quick Fix: Switch to Grayscale.** A simple grayscale (black-to-white) ramp is perceptually ordered and accessible. This is a safe and immediate improvement.

- **Moderate Approach: Use a Single-Hue Sequential Colormap.** Use a palette that progresses from a light shade of one color to a dark shade of the same color (e.g., light blue to dark blue). This provides a clear, intuitive sense of order.

- **Comprehensive Approach: Use a Perceptually Uniform Multi-Hue Colormap.** Use a modern palette like Viridis, Plasma, Magma, or Cividis. These are specifically designed to have a linear relationship between data value and perceived brightness, are accessible to colorblind viewers, and provide good resolution across the entire data range.