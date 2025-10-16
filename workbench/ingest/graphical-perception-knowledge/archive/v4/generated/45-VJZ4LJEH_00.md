---
id: avoid-rainbow-colormap
title: "Avoid rainbow colormaps for ordered data"
tags:
  - impact:perceptual
  - impact:accessibility
  - impact:cognitive
  - impact:ethical
  - chart:heatmap
  - chart:map.choropleth
  - task:compare
  - task:rank
  - task:lookup
  - data:quantitative
  - data:ordinal
  - visual:color
  - access:color-vision-risk
  - access:cognitive-load-risk
sources:
  - type: research
    ref: Liu & Heer, 2018
    url: https://doi.org/10.1145/3173574.3174172
    note: "The study found that the 'jet' (rainbow) colormap performed the worst overall in both time and error for relative distance judgments and 'should be jettisoned'."
tools:
  - type: implement
    name: viridis
    url: https://bids.github.io/colormap/
    description: A set of perceptually-uniform colormaps (Viridis, Magma, Plasma, Inferno) designed to be a better default than rainbow schemes.
  - type: validate
    name: Viz Palette
    url: https://projects.susielu.com/viz-palette
    description: A tool to check how colormaps appear to people with different types of color vision deficiency.
  - type: learn
    name: "The End of the Rainbow"
    url: https://www.youtube.com/watch?v=xAoljeRJ3lU
    description: A talk by Stéfan van der Walt & Nathaniel Smith on the problems with rainbow colormaps and the creation of viridis.
---

## Guidance

Do not use a rainbow (or "jet") colormap to represent ordered quantitative or sequential data.

## Why

Rainbow colormaps lack perceptual ordering, meaning the order of colors (e.g., green, yellow, orange) does not intuitively map to the order of the data. This creates uneven perceived gradients, introduces false boundaries where none exist in the data, and makes it difficult for viewers to accurately judge values or compare differences. Research consistently shows that they lead to higher error rates and slower interpretation times compared to perceptually-uniform alternatives. They are also not accessible to users with common forms of color vision deficiency.

## When it applies

- When encoding sequential, diverging, or other ordered quantitative data using a continuous color scale.
- This is especially critical in charts like heatmaps and choropleth maps where color is the primary channel for representing magnitude.

## Exceptions

None known for effective data visualization. While rainbow colormaps are sometimes used in scientific imaging for historical or convention-based reasons, they are not recommended for communicating data accurately and ethically.

## Trade-offs

- **Clarity over convention:** Moving away from a rainbow colormap might be a change for audiences accustomed to it in certain scientific fields, but the significant gains in perceptual accuracy and accessibility justify the change.

## Signs of Trouble

- **The Squint Test:** If you squint at the visualization, you see distinct, harsh bands of color instead of a smooth gradient.
- **Order Ambiguity:** It's not immediately obvious whether yellow represents a higher or lower value than green without constantly referring to the legend.
- **False Boundaries:** The sharp transition between two hues (e.g., green to yellow) suggests a significant shift in the data that may not actually exist.
- **The `jet` colormap:** The presence of the specific `jet` colormap is a clear sign of trouble.

## How to Improve

- **Quick Fix: Switch to a Single-Hue Scheme.** Replace the rainbow colormap with a simple, sequential single-hue colormap (e.g., "Blues," "Greys"). This immediately establishes a clear perceptual order based on luminance (lightness/darkness).

- **Comprehensive Redesign: Use a Perceptually-Uniform Colormap.** Switch to a perceptually-uniform multi-hue colormap like Viridis, Magma, or Plasma. These are specifically designed to have a consistent and linear change in perceived brightness, making them highly interpretable, robust, and accessible to viewers with color vision deficiencies.
