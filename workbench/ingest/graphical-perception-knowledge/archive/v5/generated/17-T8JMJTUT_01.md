---
id: use-noncontiguous-cartograms-for-shape-recognition
title: "Use non-contiguous cartograms to preserve shape recognition"
tags:
  - impact:perceptual
  - impact:cognitive
  - chart:map
  - chart:map.cartogram
  - chart:map.cartogram.non-contiguous
  - chart:map.cartogram.contiguous
  - task:lookup
  - data:spatial
  - data:quantitative
  - visual:shape
  - visual:area
  - audience:general
  - medium:static
evidence:
  strength: medium
  summary: "In a 2018 experiment, non-contiguous cartograms, which perfectly preserve region shape, resulted in a four-fold reduction in error rates for shape recognition tasks compared to contiguous cartograms."
sources:
  - type: research
    ref: "Nusrat, Alam, and Kobourov, 2018"
    url: "https://doi.org/10.1109/TVCG.2016.2642109"
    note: "In a 'recognize' task, the error rate for non-contiguous cartograms was ~5%, while for contiguous cartograms it was ~20%, a statistically significant difference."
    role: primary
---
## Guidance

When it is critical for users to be able to recognize geographic regions by their original shape, use a non-contiguous cartogram.

## Why

Non-contiguous cartograms are constructed by scaling each region independently while keeping its original shape perfectly intact. In contrast, contiguous cartograms must distort shapes to maintain adjacency. The source study found a large and statistically significant difference in error rates (nearly a factor of four) for a shape recognition task, strongly favoring non-contiguous cartograms.

## When it applies

-   When the user's task is to identify a region based on its shape (e.g., "Which of these shapes is Colorado?").
-   When regions are not labeled and recognition relies on shape.
-   Note: Dorling and rectangular cartograms are unsuitable for this task by design, as they replace original shapes with circles and rectangles.

## Exceptions

-   If maintaining adjacency (topology) is more important than shape recognition, a contiguous cartogram would be a better choice.

## Trade-offs

-   The primary trade-off of using non-contiguous cartograms is the complete loss of adjacency information. The cartogram can look fragmented and makes it difficult to understand neighborhood relationships.

## Signs of Trouble

-   **Shape Blindness:** Users are unable to identify well-known geographic regions by their shape in your cartogram.
-   **Shape Distortion:** You are using a contiguous cartogram and expecting users to recognize shapes that have been significantly distorted by the algorithm.

## How to Improve

-   **Quick Fix:** If using a contiguous cartogram, add clear labels to compensate for the distorted shapes.
-   **Comprehensive Redesign:** If the task is primarily recognition, switch from a contiguous cartogram to a non-contiguous one. This is the most effective way to ensure shapes are recognizable.
