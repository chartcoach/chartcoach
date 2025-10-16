---
id: cartogram-for-shape-recognition
title: "Use non-contiguous cartograms to preserve geographic shapes"
tags:
  - impact:perceptual
  - impact:cognitive
  - chart:map
  - chart:map.cartogram
  - chart:map.cartogram.non-contiguous
  - task:recognize-shape
  - data:spatial
  - visual:shape
  - medium:static

sources:
  - type: research
    ref: Nusrat, Alam, & Kobourov, 2018
    url: https://doi.org/10.1109/TVCG.2016.2642109
    note: "In a 'recognize' task, non-contiguous cartograms were significantly more accurate (nearly four times better) than contiguous cartograms. Rectangular and Dorling types were not tested as they replace shapes entirely."

---

## Guidance

When it is important for viewers to recognize the original shape of geographic regions, use non-contiguous cartograms.

## Why

Non-contiguous cartograms are the only major cartogram type that perfectly preserves the original shape of each region by scaling them individually in place. Other types fundamentally alter shapes:
- **Contiguous cartograms** must distort shapes to maintain adjacency.
- **Rectangular and Dorling cartograms** replace the original shapes entirely with rectangles and circles.

Studies show this leads to a dramatic, nearly four-fold increase in shape recognition accuracy for non-contiguous cartograms compared to contiguous ones.

## When it applies

- When viewer familiarity with geographic shapes (e.g., the shape of Italy or Texas) is an important part of interpreting the map.
- When you want to leverage shape as a perceptual cue for region identification.

## Exceptions

- If shape preservation is not a goal and other factors like topology (adjacency) or a schematic layout are more important, other cartogram types may be more suitable.

## Trade-offs

- To achieve perfect shape preservation, non-contiguous cartograms must sacrifice topology (adjacency information). They can also introduce large amounts of empty space, making the map feel "sparse" or disconnected.

## Signs of Trouble

- **Unrecognizable Blobs:** Regions in a contiguous cartogram are distorted beyond recognition.
- **"Is that Italy?":** Users express confusion or inability to identify well-known geographic shapes.
- **Loss of Geographic Grounding:** The viewer loses their sense of the underlying geography because the familiar shape cues are gone.

## How to Improve

- **Moderate Redesign: Switch to Non-Contiguous.** If you are using a contiguous, rectangular, or Dorling cartogram and shape recognition is a priority, switch to a non-contiguous cartogram.
- **Comprehensive Redesign: Use Glyphs on a Standard Map.** If both geographic accuracy and a data-driven size variable are important, consider an alternative. Use a standard geographic map and overlay each region with a sized glyph (e.g., a proportional symbol map) to represent its data value. This preserves the map's geography entirely.
