---
id: use-filled-shapes-for-color-discrimination
title: "Use filled shapes over unfilled shapes to improve color discrimination"
tags:
  - impact:perceptual
  - impact:accessibility
  - chart:scatter
  - task:compare
  - task:lookup
  - task:cluster
  - data:categorical
  - visual:color
  - visual:shape
  - medium:screen
  - access:color-vision-risk
sources:
  - type: research
    ref: Smart & Szafir, 2019
    url: https://doi.org/10.1145/3290605.3300899
    note: "Experiment 1 found that colors are significantly more discriminable for filled shapes (e.g., a solid square ■) than for their unfilled counterparts (e.g., a hollow square □) across all tested color axes in CIELAB space. For example, a filled square had significantly better color discrimination than a hollow square or hollow triangle."
examples:
  - type: bad
    description: "In this scatterplot, the hollow square and triangle shapes make it difficult to distinguish the green and blue hues, as there are very few colored pixels for each mark."
  - type: good
    description: "By switching to filled shapes (solid square and triangle), the same green and blue hues are much easier to tell apart because the larger colored area provides a stronger perceptual signal."
---
## Guidance

When using color to encode data in a scatterplot with multiple shape encodings, prefer using filled shapes (e.g., ●, ■, ◆) over unfilled, hollow shapes (e.g., ○, □, ◇).

## Why

Filled shapes provide a larger, more solid area of color, making it easier for the human visual system to perceive and compare differences in hue, saturation, or lightness. Unfilled shapes, which are essentially just outlines, contain far fewer colored pixels. This provides a weaker color signal, which significantly reduces a viewer's ability to accurately discriminate between colors, especially when marks are small or colors are subtle.

## When it applies

- When using both `shape` and `color` to encode different attributes in a multiclass scatterplot.
- When it is critical for viewers to accurately and quickly distinguish between categories represented by color.
- When mark sizes may be small, as the effect is more pronounced with fewer pixels.

## Exceptions

- **When managing overplotting:** In densely packed scatterplots, unfilled (hollow) shapes can be preferable because they reduce occlusion and allow underlying data points to be seen. This is a common strategy in tools like Tableau to mitigate overdraw. However, this comes at the cost of reduced color discriminability.

## Trade-offs

- **Clarity vs. Occlusion:** Filled shapes improve color perception but can obscure overlapping data points in dense plots. Unfilled shapes reduce occlusion but make color discrimination harder. You are trading color clarity for density representation.
- **Aesthetics:** A dense field of large, filled shapes might appear visually heavy or cluttered compared to the lighter appearance of unfilled shapes.

## Signs of Trouble

- **Color Confusion:** Viewers report difficulty telling categories apart, frequently mixing up points with similar colors (e.g., a blue square and a purple triangle).
- **The Squint Test:** If you squint at the chart, the colors on the unfilled shapes become muddy, indistinct, or disappear entirely into the background.
- **Legend-to-Plot Mismatch:** Colors that are easily distinguishable in a large legend swatch are hard to tell apart when rendered as small, thin outlines in the plot.
- **Increased Task Time:** Viewers take longer to complete tasks that involve finding or comparing color-coded categories.

## How to Improve

- **Quick Fix: Increase Stroke Width.** If you must use unfilled shapes (e.g., to manage overplotting), increase the stroke width of the shape outlines. This adds more colored pixels and can partially mitigate the loss of color discriminability.

- **Moderate Redesign: Switch to Filled Shapes.** Change the shape encoding from unfilled to their filled counterparts (e.g., change `hollow circle` to `solid circle`). This is the most direct way to apply the guideline and will immediately improve color perception.

- **Comprehensive Redesign: Rethink Encodings.** If color is the primary or most important categorical encoding, consider using a single, filled shape (e.g., circles) for all points to maximize color perceptibility and eliminate interference from shape. The secondary categorical variable could be encoded differently, perhaps in a separate chart (small multiples) if it is also important.