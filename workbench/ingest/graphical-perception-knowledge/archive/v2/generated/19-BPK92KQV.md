---
id: place-charts-back-to-back-for-comparison
title: "Place charts back-to-back for easier comparison"

impact:
  - perceptual
  - cognitive
  - performance
tags:
  - comparison
  - correlation
  - bar-chart
  - small-multiples
  - layout
  - task

sources:
  - type: research
    ref: Ondov et al., 2019
    url: https://doi.org/10.1109/TVCG.2018.2864884
    note: "Experiments showed that mirrored small multiples improved performance for both finding the 'biggest change' and judging overall correlation between two bar charts, compared to standard stacked or adjacent layouts."
  - type: research
    ref: Wagemans, 1997
    url: https://doi.org/10.1016/S1364-6613(97)01105-4
    note: "Reviews the perceptual science behind the human visual system's powerful ability to detect symmetry, which this guideline leverages."

examples:
  - type: good
    description: "Two bar charts are placed back-to-back, sharing a central vertical axis for categories. Bars for the first dataset extend to the left, and bars for the second dataset extend to the right. This mirrored layout makes it easy to compare corresponding bars and see the overall pattern of similarity."
  - type: bad
    description: "Two bar charts intended for comparison are stacked vertically. To compare the lengths of corresponding bars, the viewer must scan up and down between the two charts, remember the length of the top bar, and then compare it to the bottom bar. This process is slower and more prone to error."
---

## Guidance

When comparing values between two charts (like two bar charts), place them back-to-back so they form a mirror image. This is often more effective than placing them side-by-side or one above the other.

## Why

Our visual system is exceptionally good at processing symmetry. By arranging charts in a mirrored layout (e.g., with bars extending left from a central axis for one chart and right for the other), you tap into this powerful, pre-attentive ability.

This makes it faster and more accurate for a viewer to judge the overall similarity (correlation) between the two datasets and to spot the largest differences. It reduces the cognitive load of scanning back and forth and trying to remember values from one chart to compare with the other.

## When it applies

- The primary goal is to **compare** two datasets, series, or conditions.
- This works especially well for chart types with a strong directional component, like **bar charts**.
- It is effective for tasks like finding the "biggest mover" (maximum change) or assessing overall similarity.

## Exceptions

- **Comparing more than two datasets:** This technique is optimized for pairwise comparison. It is difficult to scale to three or more charts in a way that maintains the direct mirrored effect.
- **Audience familiarity:** Because it's less common than a standard side-by-side layout, a mirrored arrangement might momentarily confuse an audience unfamiliar with it. For public-facing, static graphics where you can't provide guidance, a more conventional layout may be a safer choice.

## Trade-offs

- You trade the **conventionality** of a standard small-multiple layout for a perceptually more **powerful** one. The small learning curve for the viewer is often worth the significant improvement in their ability to make accurate comparisons.

## Evaluate

- [ ] Are two charts meant for direct comparison placed far apart, such as one above the other?
- [ ] Do the charts use an identical side-by-side layout that forces the viewer's eyes to travel back and forth to compare corresponding items?

## Repair

1.  **Create a mirrored layout.** If you have two horizontal bar charts, for example, align them on their shared category axis. Have the bars for the first chart extend to the left and the bars for the second chart extend to the right.
2.  **Reduce distance.** If a mirrored layout isn't possible, place the charts immediately adjacent to each other rather than stacking them. Proximity helps, even without symmetry.
3.  **Use an overlaid chart.** As an alternative, layering the two series in a single chart (e.g., two sets of bars on the same axis) is also highly effective for comparison, but be mindful of potential occlusion if bars overlap.