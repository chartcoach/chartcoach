---
id: bar-chart-mean-underestimation
title: "Recognize that viewers underestimate the average value in bar charts"

impact:
  - perceptual
  - cognitive
  - logos
  - ethical
tags:
  - bar-chart
  - dot-plot
  - aggregate
  - average
  - central-tendency
  - bias
  - underestimation

sources:
  - type: research
    ref: Godau, Vogelgesang, & Gaschler, 2016
    url: https://doi.org/10.1016/j.chb.2016.01.036
    note: "Primary study demonstrating that people systematically underestimate the mean of values in bar charts but not in point graphs."
  - type: research
    ref: Zeng & Battle, 2023
    url: https://arxiv.org/abs/2109.01271
    note: "Review paper that collates this finding as part of a larger knowledge base on graphical perception."

examples:
  - type: bad
    description: "A bar chart shows monthly website traffic. A horizontal line indicates the annual average. Viewers are likely to visually underestimate the average of the bars, potentially concluding traffic is performing worse than it actually is relative to the line."
  - type: good
    description: "The same monthly website traffic is shown using a dot plot. Each month's traffic is a single dot. This format allows viewers to more accurately judge the average traffic level without the underestimation bias caused by bars."
---

## Guidance

Use bar charts with caution when the primary task is for viewers to judge the overall average of the data. Viewers tend to systematically perceive the average value to be lower than it actually is.

## Why

This perceptual bias is caused by how our visual system processes the filled areas of the bars. We don't just see the top edge of each bar; the entire "weight" of the bars pulls our perception of the average down. Studies have confirmed this underestimation effect is consistent, even when comparing bar charts to other chart types like dot plots, which do not produce the same bias.

## When it applies

- When using a bar chart where a key message relies on understanding the **average value across all categories** (the "grand average").
- When a bar chart includes a **benchmark or target line**, and the viewer is meant to judge whether the group's average performance is above or below that line.

## Exceptions

The underestimation of the *average* is less critical if the primary task is different. Using a bar chart is generally fine when the goal is to:
- **Compare individual bars** to each other (e.g., "Which category is highest?").
- **Look up the value** of a specific category.

## Trade-offs

- **Familiarity vs. Accuracy**: Bar charts are one of the most familiar chart types. Switching to a more perceptually accurate alternative like a dot plot might be slightly less intuitive for some audiences, even though it avoids the estimation bias.
- **Clutter**: For very dense datasets, a bar chart can become more cluttered than a simple dot plot.

## Evaluate

- [ ] A bar chart is used to display values across multiple categories.
- [ ] A key takeaway from the chart requires the viewer to estimate the average value of all the bars combined.
- [ ] The chart's title, caption, or annotations prompt the viewer to think about the "average performance," "overall level," or "central tendency."

## Repair

1.  **Change the chart type.** The most effective fix is to use a chart that doesn't rely on filled areas. A **dot plot** or a **strip plot** are excellent alternatives that allow for more accurate perceptual averaging.
2.  **State the average explicitly.** If you must use a bar chart, remove the ambiguity by directly annotating the chart with the correct average value (e.g., "Average: $5,430").
3.  **Add a clear average line.** Draw a distinct, labeled reference line on the chart to represent the true average. This gives viewers a concrete anchor, though be aware that the visual impression of the bars may still conflict with the line's position.