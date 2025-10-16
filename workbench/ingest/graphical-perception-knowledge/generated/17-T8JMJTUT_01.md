---
id: use-non-contiguous-cartograms-for-shape-recognition
title: "Use non-contiguous cartograms to preserve geographic shape recognition"

tags:
  - impact:perceptual
  - chart:map
  - chart:map.cartogram
  - chart:map.cartogram.non-contiguous
  - task:lookup
  - data:spatial
  - visual:shape
  - audience:general

evidence:
  strength: medium
  summary: "A 2018 study (n=33) found that non-contiguous cartograms, which preserve shape, resulted in a nearly 4x lower error rate for shape recognition tasks compared to contiguous cartograms, which distort shapes (ANOVA F=13.53, p<0.001)."

sources:
  - type: research
    ref: "Nusrat, Alam, & Kobourov, 2018"
    url: https://doi.org/10.1109/TVCG.2016.2642109
    note: "Experiment H2 tested shape recognition. Non-contiguous cartograms were significantly more accurate than contiguous cartograms, as they do not distort the original geographic shapes."
    role: primary

---

## Guidance

To ensure viewers can recognize geographic regions (like countries or states) by their familiar shapes, use a **non-contiguous cartogram**. Avoid cartogram types that distort shape, such as contiguous cartograms, for this specific task.

## Why

Non-contiguous cartograms work by scaling each region in place without altering its boundaries. This perfectly preserves the original, recognizable shape of each geographic area. Other types, like contiguous cartograms, must warp and distort shapes in order to maintain adjacencies, which can make even familiar regions difficult to identify.

### Core Principle

When recognition of a familiar shape is a key part of decoding a chart, that shape should be preserved with high fidelity.

## When it applies

- When the audience's ability to identify specific geographic regions by their shape is important for interpreting the map.
- When creating visualizations for a general audience who may rely on familiar shapes for orientation.

## Exceptions

- When preserving topology (adjacency) or showing a connected whole is more important than individual shape recognition. In such cases, a contiguous cartogram is more appropriate, despite the loss of shape fidelity.

## Trade-offs

- **Loss of Adjacency:** Non-contiguous cartograms completely sacrifice topological information. It is impossible to tell which regions are neighbors.
- **"Empty" Space:** This cartogram style can result in significant white space between regions, which can make the map feel sparse or disconnected.

## Signs of Trouble

- **Recognition Failure:** Viewers cannot identify well-known states, provinces, or countries from their shape alone.
- **Over-reliance on Labels:** The visualization is incomprehensible without text labels on every single region.

## How to Improve

- **Quick Fix: Link to a Reference Map.** If using a shape-distorting cartogram, provide a linked, undistorted reference map. Clicking or hovering on a region in the cartogram highlights the corresponding region on the standard map.

- **Moderate Redesign: Switch to Non-Contiguous.** If shape recognition is a primary goal, change the chart type from a contiguous or rectangular cartogram to a non-contiguous one.

- **Comprehensive Redesign: Use Glyphs on a Standard Map.** Instead of distorting the map area, represent the data variable using scaled symbols (glyphs) placed on a standard, undistorted map. This preserves both shape and location perfectly but sacrifices using area as a visual channel.
