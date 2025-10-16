---
id: use-filled-shapes-in-scatterplots
title: "Use filled shapes for better color discrimination in scatterplots"

impact:
  - perceptual
  - logos
  - accessibility
  - aesthetic
tags:
  - scatterplot
  - shape
  - color
  - size
  - categorical-data
  - perceptual-bias
  - comparison

sources:
  - type: research
    ref: Smart & Szafir, 2019
    url: https://doi.org/10.1145/3290605.3300899
    note: "Primary study demonstrating that filled shapes improve color discriminability and are perceived as larger than unfilled shapes in scatterplots."
  - type: research
    ref: Zeng & Battle, 2023
    url: https://arxiv.org/abs/2109.01271v3
    note: "Review paper that collates and summarizes graphical perception knowledge, including the findings from Smart & Szafir (2019)."

tools:
  - type: implement
    name: Perceptual Color Normalization
    url: https://osf.io/vba7h/
    description: A D3.js extension from the original researchers to normalize color encoding scales based on the size and shape parameters of a visualization.

examples:
  - type: bad
    description: A scatterplot uses unfilled shapes like hollow circles (○) and hollow squares (□) to encode different categories. The thin lines of color make it harder for viewers to accurately distinguish between two similar shades (e.g., a light blue vs. a slightly lighter blue).
  - type: good
    description: The same scatterplot uses filled shapes like solid circles (●) and solid squares (■). The larger area of solid color makes it significantly easier for viewers to perceive differences between colors, leading to a more accurate interpretation of the data.
---

## Guidance

In scatterplots that use shape to encode categories, prefer using filled shapes (e.g., ●, ■) over unfilled or hollow shapes (e.g., ○, □), especially when color is also used as a channel.

## Why

The shape of a mark is not a neutral container; it biases our perception of other visual channels like color and size. Research shows that colors are significantly easier to tell apart when applied to filled shapes compared to hollow shapes of the same dimensions. This is because the larger colored area provides a stronger signal to our visual system.

Additionally, filled shapes are often perceived as larger or more visually prominent than their unfilled counterparts, which can create an unintended and potentially misleading visual hierarchy. Using filled shapes for all categories leads to a more accurate and less biased interpretation of the data.

## When it applies

- In multiclass scatterplots where you are using **shape** to distinguish between categories.
- When **color** or **size** are also used to encode other data variables.
- When ensuring accurate **color discrimination** is a primary design goal.

## Exceptions

When dealing with very **dense scatterplots** where many points overlap. In this context, using unfilled or semi-transparent shapes can help mitigate overplotting, making it possible to see the underlying distribution and individual points that would otherwise be hidden. Here, the need to maintain global legibility may outweigh the benefit of improved color discrimination for individual marks.

## Trade-offs

Using filled shapes in a dense plot can lead to significant **overplotting**, where marks obscure each other and make the overall data distribution difficult to see. This creates a direct trade-off between the perceptual accuracy of individual marks and the legibility of the plot's global structure.

## Evaluate

- [ ] The chart is a scatterplot that uses different shapes to encode categories.
- [ ] Some or all of the shapes used are unfilled or hollow (e.g., ○, □, △).
- [ ] The plot is not overly dense, meaning filled shapes could have been used without causing major overplotting issues.

## Repair

1.  **Switch to filled shapes.** Change all unfilled marks to their filled counterparts (e.g., `○` → `●`, `□` → `■`). This is the most direct way to improve color and size perception.
2.  **If overplotting is a concern, reduce opacity.** Use filled shapes but make them semi-transparent (e.g., 50% opacity). This maintains a larger colored area for better perception while allowing overlapping points to be seen.
3.  **Consider an alternative encoding.** If shape is not a critical channel, encode the category using only color on a single, consistent filled shape (e.g., all solid circles). This eliminates the perceptual interference from shape entirely.