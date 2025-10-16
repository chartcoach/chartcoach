---
id: prioritize-position-for-comparisons
title: "Prioritize position over angle or length for quantitative comparisons"

impact:
  - perceptual
  - logos
  - ethical
  - performance
tags:
  - comparison
  - quantitative
  - position
  - angle
  - length
  - area
  - bar-chart
  - pie-chart
  - dot-chart
  - cleveland-mcgill

sources:
  - type: research
    ref: Cleveland & McGill, 1984
    url: https://doi.org/10.1080/01621459.1984.10478080
    note: "The foundational experimental paper establishing the perceptual hierarchy of visual encodings, showing position is judged more accurately than length and angle."
  - type: research
    ref: Zeng & Battle, 2023
    url: https://arxiv.org/abs/2109.01271v3
    note: "This review paper collates and structures the findings from 59 graphical perception papers, including Cleveland & McGill, to create a knowledge base for visualization recommendation systems."

examples:
  - type: bad
    description: "A pie chart forces readers to compare angles, which is a difficult and inaccurate perceptual task. It's hard to tell the precise difference between slices, especially those with similar values."
  - type: good
    description: "A bar chart or dot chart encodes the same data using position along a common baseline. This allows for fast, easy, and accurate comparisons between the categories."
---

## Guidance

Use position along a common scale to represent quantitative values that need to be compared. Avoid using angle, length (without a common baseline), or area, as these are harder for people to judge accurately.

## Why

Landmark experiments by William Cleveland and Robert McGill established a clear hierarchy of how accurately people perceive different visual encodings. They found that we make the most accurate and least biased judgments when decoding data from **position along a common scale** (the basis of bar and dot charts).

Other encodings are progressively less accurate:
1.  **Position** (Most Accurate)
2.  Length
3.  Angle
4.  Area (Least Accurate)

Using a more perceptually accurate encoding channel like position makes your chart easier to read correctly and less likely to mislead your audience. For example, replacing a pie chart (angle) with a bar chart (position) can increase the accuracy of readers' judgments by nearly a factor of two.

## When it applies

- When the primary goal is for the audience to make precise comparisons between quantitative values.
- When choosing between chart types to show parts of a whole, such as deciding between a bar chart and a pie chart.
- When designing charts with multiple series, like stacked bar charts, where only the bottom-most series is aligned to a common baseline.

## Exceptions

- **General part-to-whole, not precise comparison:** If the goal is simply to show that you are representing proportions of a total (e.g., "Category A is about half the total"), a pie chart can be an acceptable and familiar choice.
- **Very few slices:** For a pie chart with only two or three slices representing very different values (e.g., 25% vs 75%), the imprecision of angle judgments is less of a problem.
- **Encoding additional variables:** When encoding a third quantitative variable on a scatterplot, using size (area) is a common convention. While less precise, it is often the only practical option.

## Trade-offs

- A bar or dot chart may take up more linear space (horizontally or vertically) than a single, compact pie chart representing the same data.
- Pie charts are highly familiar to general audiences. Replacing one with a dot chart, while perceptually superior, might require a moment for an unfamiliar reader to orient themselves.

## Evaluate

- [ ] The chart uses angles (e.g., pie chart, donut chart) for comparing multiple quantitative values.
- [ ] The chart requires comparing the lengths of unaligned segments (e.g., the inner segments of a stacked bar chart).
- [ ] The chart uses 2D area (e.g., bubble chart) or 3D volume as the primary means for readers to make precise comparisons.

## Repair

1.  **Replace pie/donut charts with bar or dot charts.** This is the most direct fix. It shifts the perceptual task from judging angles to judging position, which is significantly more accurate and less error-prone.
2.  **Unstack stacked bars.** If you need to compare all segments in a stacked bar chart, consider a grouped bar chart instead. This places all bars on the same baseline, enabling accurate comparisons across all categories.
3.  **Add direct labels.** If you must use a less accurate encoding like area (in a bubble chart), add direct data labels to each element. This provides the precise value and compensates for the inherent difficulty of comparing sizes.