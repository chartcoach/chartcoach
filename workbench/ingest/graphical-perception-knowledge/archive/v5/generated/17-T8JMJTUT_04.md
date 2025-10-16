---
id: avoid-rectangular-cartograms-for-summarizing-patterns
title: "Avoid rectangular cartograms for summarizing spatial patterns"
tags:
  - impact:perceptual
  - impact:cognitive
  - chart:map
  - chart:map.cartogram
  - chart:map.cartogram.rectangular
  - task:distribution
  - task:summary-mean
  - data:spatial
  - data:quantitative
  - visual:area
  - visual:position
  - audience:general
  - medium:static
evidence:
  strength: medium
  summary: "A 2018 study on cartogram effectiveness found that rectangular cartograms had the highest error rate for 'summarize' tasks, a result that was statistically significant compared to non-contiguous and Dorling cartograms."
sources:
  - type: research
    ref: "Nusrat, Alam, and Kobourov, 2018"
    url: "https://doi.org/10.1109/TVCG.2016.2642109"
    note: "For the 'summarize' task, the error rate for rectangular cartograms was the highest, and significantly higher than for Dorling and non-contiguous types."
    role: primary
---
## Guidance

When the primary goal is for users to see the "big picture" and identify broad trends or patterns in the data, avoid using rectangular cartograms.

## Why

Rectangular cartograms severely distort both shape and relative geographic location, replacing them with a rigid, schematic grid. This abstraction can obscure the larger spatial patterns that are often the main takeaway of a thematic map. The study found that for `summarize` tasks (e.g., "Which part of the country contributes more to GDP?"), rectangular cartograms had the highest error rate. Dorling, non-contiguous, and contiguous cartograms, which all better preserve some aspect of the original geography (location or shape), performed significantly better.

## When it applies

-   When presenting a cartogram to show high-level trends, distributions, or patterns, such as an east/west divide, a coastal concentration, or a rural/urban split.
-   When the audience is a general one, not experts trained to read highly abstract schematics.

## Exceptions

-   If maintaining strict topology in a clean, grid-like schematic is the most critical requirement, and the audience is expert users familiar with this representation, a rectangular cartogram might be used.

## Trade-offs

-   Avoiding rectangular cartograms means you sacrifice their primary benefit: a clean, schematic layout that perfectly preserves adjacency without the visual complexity of distorted shapes.

## Signs of Trouble

-   **Pattern Obscurity:** Users are unable to describe the overall trend or pattern in your cartogram.
-   **Viewer Confusion:** Feedback indicates the visualization is confusing, abstract, or hard to connect back to the underlying geography.
-   **Wrong Tool for Summary:** You are using a rectangular cartogram to show a high-level summary to a general audience.

## How to Improve

-   **Moderate Redesign: Switch to a Dorling Cartogram.** Dorling cartograms performed well for summary tasks. The simple, uniform circles make it easy to spot clusters of large or small values, revealing patterns without the complexity of distorted shapes.
-   **Comprehensive Redesign: Switch to a Contiguous Cartogram.** Contiguous cartograms also performed well. By preserving a stronger sense of the underlying geography and topology, they help users interpret spatial patterns in a more familiar context.
