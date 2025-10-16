---
id: highlight-small-differences
title: "Highlight small differences between similar values"

impact:
  - perceptual
  - cognitive
  - accessibility
  - logos
  - ethical
  - performance
tags:
  - comparison
  - bar-chart
  - pie-chart
  - bubble-chart
  - jnd
  - just-noticeable-difference
  - perception
  - annotation

sources:
  - type: research
    ref: Lu et al., 2022
    url: https://doi.org/10.1109/TVCG.2021.3114874
    note: "Models the Just Noticeable Difference (JND) in bar, pie, and bubble charts, showing how distance and the marks' own size (intensity) affect our ability to perceive small differences."

examples:
  - type: bad
    description: "A bar chart where two bars representing similar values (e.g., 170 and 172.5) are placed far apart. At a glance, it's impossible to tell which is taller or if they are the same height."
  - type: good
    description: "The same chart, but with text labels (annotations) added to the two similar bars. The labels make the small difference explicit and prevent misinterpretation."
---

## Guidance

When marks in a chart represent very similar values, their difference may be imperceptible. Explicitly highlight these small differences using annotations or secondary visual cues.

## Why

Human perception has limits. We can't reliably distinguish between two visual marks (like bars or bubbles) if their difference in size, length, or angle is below a certain threshold—the "Just Noticeable Difference" (JND). This problem gets worse when the marks are far apart from each other. Failing to account for this can lead viewers to incorrectly assume the values are identical, missing a potentially important detail in the data.

## When it applies

- When comparing precise values in bar charts, bubble charts, or pie charts.
- When the dataset contains values that are very close to each other.
- In bar charts and bubble charts, this is especially critical when similar-valued items are positioned far from each other.

## Exceptions

- If only the general trend or approximate values are important, and the precise difference between two specific items is irrelevant to the chart's message.
- When the goal is to show that several items are effectively the same, and highlighting minor, statistically insignificant differences would be distracting.

## Trade-offs

- Adding annotations can increase visual clutter, especially if many items need highlighting.
- Over-emphasizing very small differences with dramatic styling might make them seem more significant than they actually are.

## Evaluate

- [ ] The chart contains two or more marks that are very similar in size, length, or angle.
- [ ] A quick glance makes it difficult to tell which of the similar marks is larger, or if they are the same.
- [ ] In a bar or bubble chart, the similar marks are not adjacent to each other.

## Repair

1.  **Reorder the chart.** If possible, sort the chart to place the items being compared next to each other. This is most effective for bar charts, as it makes direct position comparison easier.
2.  **Add direct labels.** Annotate the specific marks that are hard to distinguish with their exact values. This is the clearest way to resolve the ambiguity.
3.  **Use a secondary cue.** If annotating is too cluttered, consider adding a subtle secondary visual cue (like small dots or a faint texture) to create a visual ranking for the group of similar items.