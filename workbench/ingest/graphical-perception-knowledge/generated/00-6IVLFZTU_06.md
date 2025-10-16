---
id: use-filled-shapes-for-color-discrimination
title: "Use filled shapes instead of outlines to improve color discrimination"
tags:
  - impact:perceptual
  - chart:scatter
  - chart:map.proportional-symbol
  - visual:color
  - visual:shape
  - data:categorical
  - data:cardinality.high
audience:
  - audience:general
medium:
  - medium:screen
evidence:
  strength: medium
  summary: "An empirical study by Smart & Szafir (2019) on multiclass scatterplots found that colors are generally more discriminable when applied to filled shapes compared to unfilled outlines. As cited in Zeng & Battle's (2023) review, this suggests that using a larger colored area for marks improves perceptual performance."
sources:
  - type: research
    ref: Smart & Szafir, 2019
    note: "This study (ref [92] in Zeng & Battle) empirically measured the separability of visual channels and found that filled shapes aid in color discrimination in multiclass scatterplots."
    role: primary
  - type: research
    ref: Zeng & Battle, 2023
    url: https://arxiv.org/abs/2109.01271v3
    note: "This review paper synthesizes the finding from Smart & Szafir, highlighting it as an actionable guideline for improving visualization design (p. 8)."
    role: supporting
---
## Guidance
When using color to distinguish between categories in visualizations like scatterplots or bubble maps, use filled marks (e.g., ●, ■) instead of hollow outlines (e.g., ○, □).

## Why
The human visual system is better at discriminating between colors when they are applied to larger, solid areas. The thin lines decisões of an outlined shape provide a much weaker color signal, making it harder to tell similar colors apart, especially when marks are small or overlapping. Using filled shapes increases the colored area of each mark, enhancing perceptual distance between categories.

### Core Principle
Maximize the signal-to-noise ratio for your visual encodings. For color, the "signal" is the area of a given hue, so a larger colored area makes the signal stronger and easier to perceive.

## When it applies
- You are using color to encode categorical data.
- The visualization uses discrete marks, such as in a scatterplot, dot plot, or proportional symbol map.
- You have many categories, making color-based separation critical.
- Marks may be small or densely packed.

## Exceptions
- When you need to show overlapping marks. Hollow, semi-transparent marks can make it easier to see density and avoid occluding points underneath. In this case, you are prioritizing density representation over categorical distinction.
- For stylistic reasons where a lighter, less "heavy" aesthetic is desired, though this comes at a perceptual cost.

## Trade-offs
- **Occlusion:** Solid, filled marks are more likely to occlude other marks behind them in dense plots. This can be mitigated with transparency, but transparency also reduces color saturation and can weaken the signal.
- **Visual Weight:** A chart with many large, filled marks can feel visually heavy or cluttered compared to one with outlined marks.

## Signs of Trouble
- **Ambiguous Colors:** Viewers have trouble distinguishing between two different categories, asking "Is that the blue one or the purple one?"
- **Legend-Matching Difficulty:** It's hard to match the small, thin color of an outlined mark on the chart to the solid color swatch in the legend.
- **Small Mark Invisibility:** When marks are very small, the color of an outline can become almost invisible.

## How to Improve
- **Quick Fix: Fill the Shapes.** In your charting tool, change the mark style from "hollow" or "outline" to "solid" or "filled".
- **Moderate Redesign: Use a White Stroke.** If you are concerned about marks blending into each other or the background, use filled marks with a thin white or light-colored stroke around them. This preserves the strong internal color signal while creating a sharp boundary for each mark.
- **Comprehensive Redesign: Reduce Category Count.** If color discrimination is still a problem even with filled shapes, the issue may be that you have too many categories. Consider grouping less-important categories into a single "Other" category to reduce the number of colors needed.