---
id: bar-chart-neighborhood-effects
title: "Recognize that neighborhood effects in bar charts are usually minor"
impact:
  - perceptual
  - cognitive
  - ethical
tags:
  - bar-chart
  - comparison
  - rank-estimation
  - perceptual-bias
  - context-effects
sources:
  - type: research
    ref: Zhao, Qu, & Sedlmair, 2019
    url: https://doi.org/10.1145/3290605.3300462
    note: "Primary study that quantified the small effect of neighboring bars on rank perception."
examples:
  - type: bad
    description: "A target bar's value can be slightly underestimated when surrounded by very tall bars. The tall context makes the target appear shorter by contrast."
  - type: good
    description: "Sorting bars by value makes rank comparison easy and renders the small neighborhood effect irrelevant. This is a more robust design choice."
---

## Guidance

Be aware that a bar's perceived height and rank can be slightly distorted by the height of its immediate neighbors. A bar surrounded by very tall neighbors may be perceived as shorter, while one surrounded by short neighbors may be perceived as taller.

## Why

This phenomenon, known as a "neighborhood effect," is a perceptual bias similar to the Parallel Line Illusion. Our brain judges visual elements in context; a bar placed next to very tall bars is perceived as shorter by contrast.

However, research shows this effect is small. Other factors, such as the bar's true rank or the overall data distribution (e.g., skewness), have a much larger impact on a viewer's judgment. While the effect exists, it is unlikely to cause significant misinterpretation on its own.

## When it applies

- When using bar charts for tasks that require viewers to estimate the rank or percentile of a specific bar within the entire dataset.
- When the bar order is not predetermined (e.g., alphabetical) and items of interest could end up next to extreme values.

## Exceptions

Because the effect is small, it is rarely a critical issue that demands a specific fix. If a bar's value or rank is crucial, using a direct label is a more effective solution than trying to rearrange its neighbors. Prioritizing other design principles, like sorting or logical grouping, will almost always have a greater positive impact on clarity.

## Trade-offs

Actively trying to mitigate this small effect—for example, by reordering bars to create a "neutral" neighborhood—could disrupt a more meaningful order (like alphabetical or chronological) and add unnecessary complexity for little perceptual gain.

## Evaluate

- [ ] Does the chart ask the viewer to estimate the rank of a specific bar?
- [ ] Is that bar positioned directly next to the tallest or shortest bars in the set?
- [ ] Is there a lack of direct labels or sorting that forces the viewer to rely solely on perceptual estimation?

## Repair

1.  **Acknowledge but Don't Overreact:** First, recognize that a minor perceptual bias may exist but is unlikely to mislead viewers significantly. Avoid over-engineering a solution.
2.  **Sort the Bars by Value:** If the category order is not inherently meaningful, sort the bars. This provides a clear visual hierarchy that makes rank estimation trivial and effectively nullifies the small neighborhood effect.
3.  **Add Direct Labels or Annotations:** If a specific bar's value or rank is critical, add a direct label or callout. This removes ambiguity and makes the visual estimation task unnecessary.