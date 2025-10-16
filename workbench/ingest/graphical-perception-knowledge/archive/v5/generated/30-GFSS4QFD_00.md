---
id: use-filled-shapes-for-color
title: "Use filled shapes over unfilled shapes to improve color discrimination"

tags:
  - impact:perceptual
  - impact:accessibility
  - chart:scatter
  - chart:map.glyphs
  - task:compare
  - task:lookup
  - data:categorical
  - visual:color
  - visual:shape
  - medium:screen
  - access:color-vision-risk

evidence:
  strength: medium
  summary: "A 2019 crowdsourced study on scatterplots found that viewers can distinguish color differences more accurately and with less variance on filled shapes (e.g., ●) than on equivalent unfilled shapes (e.g., ○)."

sources:
  - type: research
    ref: Smart & Szafir, 2019
    url: https://doi.org/10.1145/3290605.3300899
    note: "Primary study that measured just-noticeable differences (JNDs) for color on 16 different mark shapes, finding filled shapes consistently outperformed unfilled shapes."
    role: primary

tools:
  - type: learn
    name: The D3 extension from the paper
    url: https://bit.ly/2prjuRu
    description: Implements models from the study to normalize color encoding scales based on shape and size.

examples:
  - type: bad
    description: "This scatterplot uses unfilled shapes. The colors are only on the thin outlines, making it difficult to distinguish the light green 'Adelie' from the light purple 'Gentoo' penguins."
  - type: good
    description: "This version uses filled shapes. The larger color area makes each category's color much more distinct and easier to identify, improving readability."
---

## Guidance

When using color to encode categorical data in scatterplots or glyph maps, prefer using filled shapes (like circles `●`, squares `■`, or triangles `▲`) instead of unfilled, outlined shapes (like `○`, `□`, or `△`).

## Why

The human visual system's ability to discriminate between colors is strongly influenced by the size and solidity of the colored area. Filled shapes present a larger, more coherent patch of color, which provides a stronger visual signal and makes it easier to perceive and compare hues. Unfilled shapes relegate the color to a thin outline, significantly reducing this signal and making accurate color comparison more difficult, especially for small marks.

### Core Principle

Perceptual accuracy depends on the strength of the visual signal. For color, a larger and more solid colored area provides a stronger, more discriminable signal. The shape of a mark is not independent of the color it displays; they are perceptually entangled.

## When it applies

-   In any visualization using mark color to distinguish between categories, such as multiclass scatterplots or maps with symbol markers.
-   When you have a moderate to high number of categories (5+) or when some colors in your palette are perceptually close (e.g., light green and light blue).
-   When marks may be rendered at a small size.

## Exceptions

-   When severe overplotting (data occlusion) is the primary concern. Unfilled shapes can help reveal the density of underlying points in a way that opaque filled shapes cannot. Even in this case, a better alternative often exists.

## Trade-offs

-   **Occlusion:** Filled shapes can obscure each other more easily in dense plots. This can be a significant problem, hiding underlying data patterns.
-   **Clutter:** A dense plot with large filled shapes may appear more cluttered than one with unfilled shapes.

## Signs of Trouble

-   **Color Confusion:** It's difficult to tell which category a point belongs to without using a tooltip or zooming in.
-   **Legend Reliance:** Viewers have to constantly look back and forth between the chart and the legend because the colors on the small, outlined marks are not distinct enough.
-   **The Squint Test:** If you squint at your chart, do points from different color categories blend together or become indistinguishable?
-   **Similar Color Failure:** Two colors that look distinct in the legend (e.g., a large square) are hard to tell apart as small marks on the chart.

## How to Improve

-   **Quick Fix: Switch to Filled Shapes.** Change the mark property in your visualization tool from an unfilled or "open" shape to its filled equivalent.
    - *Example:* In Vega-Lite, change `"shape": "circle-open"` to `"shape": "circle"`.

-   **Moderate Approach: Use Transparent Fills.** If overplotting is a concern, use filled shapes with partial transparency (e.g., an `alpha` or `opacity` value of 0.6-0.8). This often preserves the color signal better than an unfilled shape while still allowing you to see data density. Adding a thin, dark stroke can also help define the shape boundaries.

-   **Comprehensive Approach: Facet by Category.** If distinguishing categories is critical and the plot is dense, the best solution is often to use small multiples (also known as faceting or trellising). Create a separate plot for each category, which completely removes the burden of discriminating colors or shapes and allows for much clearer comparisons of distributions within each category.
