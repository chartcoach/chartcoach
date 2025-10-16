---
id: cartogram-for-summary-patterns
title: "Use Dorling or non-contiguous cartograms for summarizing broad patterns"
tags:
  - impact:perceptual
  - impact:cognitive
  - chart:map
  - chart:map.cartogram
  - chart:map.cartogram.dorling
  - chart:map.cartogram.non-contiguous
  - task:summary
  - task:distribution
  - task:pattern-detection
  - data:spatial
  - data:quantitative
  - visual:area
  - medium:static

sources:
  - type: research
    ref: Nusrat, Alam, & Kobourov, 2018
    url: https://doi.org/10.1109/TVCG.2016.2642109
    note: "For a 'summarize' task, Dorling and non-contiguous cartograms were significantly more accurate than rectangular cartograms. They allow users to see the 'big picture' more effectively."

---

## Guidance

For "big picture" tasks like summarizing the overall distribution of data or identifying broad trends and patterns, prefer Dorling or non-contiguous cartograms.

## Why

Dorling cartograms (with simple circles) and non-contiguous cartograms (with preserved, familiar shapes) reduce visual complexity. This makes it easier for viewers to get a quick impression of the overall data landscape (e.g., "the population is concentrated in the east"). The complex and distorted shapes in contiguous, and especially rectangular, cartograms can obscure these high-level patterns and increase cognitive load, leading to lower accuracy on summarization tasks.

## When it applies

- When the primary goal is for the viewer to quickly understand the general distribution, find clusters, or see high-level trends.
- When the focus is on the overall pattern rather than the precise values or properties of individual regions.

## Exceptions

- If the "big picture" explicitly involves relationships between adjacent regions (e.g., a trend flowing across borders), a **contiguous cartogram** may be more appropriate as it preserves topology, even if it's slightly less accurate for pure summarization.

## Trade-offs

- Dorling and non-contiguous cartograms are better for summarization but do not show adjacency. They present a more abstract, less geographically "stitched-together" view of the data.

## Signs of Trouble

- **"Can't see the forest for the trees":** Users get bogged down in the complex, distorted shapes of a contiguous or rectangular cartogram and fail to spot the larger pattern.
- **Incorrect Summaries:** Users make incorrect high-level statements about the data distribution because the visualization's distortions misled them.
- **High Cognitive Load:** The visualization looks like a complex, jumbled puzzle, requiring significant mental effort to interpret.

## How to Improve

- **Moderate Redesign: Switch Cartogram Type.** If using a rectangular or contiguous cartogram for a summarization task, switch to a **Dorling** or **non-contiguous** type to improve accuracy and reduce cognitive load.
- **Comprehensive Redesign: Simplify the Data.** If the goal is purely a summary, consider whether a cartogram is needed at all. Aggregating the data into larger regions (e.g., Northeast, South, West) and using a simpler chart, like a bar chart, might communicate the key takeaway more clearly.
