---
id: use-line-or-scatter-for-correlation
title: "Use line or scatter charts to show correlation"

impact:
  - perceptual
  - cognitive
  - logos
  - ethos
  - performance
tags:
  - correlation
  - relationship
  - line-chart
  - scatterplot
  - bar-chart
  - pie-chart
  - comparison
  - quantitative

sources:
  - type: research
    ref: Saket et al., 2019
    url: https://doi.org/10.1109/TVCG.2018.2829750
    note: "Found line charts and scatterplots were significantly more accurate and faster for correlation tasks compared to bar charts, pie charts, and tables."
  - type: research
    ref: Zeng & Battle, 2023
    url: https://doi.org/10.1145/3544548.3581349
    note: "Summarizes and collates the findings from Saket et al. (2019), recommending specific chart types for the 'Correlate' task based on empirical evidence."
  - type: research
    ref: Harrison et al., 2014
    url: https://doi.org/10.1109/TVCG.2014.2346979
    note: "An earlier study ranking nine visualization types for correlation, finding that scatterplots and parallel coordinates perform best."

examples:
  - type: good
    description: "A scatterplot clearly shows the relationship between two quantitative variables, such as a car's weight and its fuel efficiency. Each variable is mapped to an axis, and the pattern of the points reveals the correlation."
  - type: bad
    description: "A pie chart is used to show the relationship between movie budget and rating. Pie charts encode part-to-whole relationships using angles and area, which are ineffective for showing how two separate variables relate to each other."
---

## Guidance

To help users identify the relationship or correlation between two quantitative variables, use a scatterplot or a line chart. Avoid using pie charts, bar charts, or tables for this task.

## Why

The human visual system is highly effective at detecting linear patterns and orientation. Scatterplots leverage this by mapping each variable to a position on an axis, allowing us to perceive correlation from the alignment and slope of the points. Similarly, line charts use slope to represent trends and relationships, making them effective for correlation tasks, especially when one variable is ordered (like time).

Empirical studies show that users are significantly faster and more accurate at judging correlation with scatterplots and line charts than with other chart types like pie or bar charts, which encode data using angles or lengths that do not intuitively map to statistical relationships.

## When it applies

- When the primary goal is for the user to assess the relationship between two continuous (quantitative) variables.
- When answering questions like: "Does an increase in Variable A correspond to an increase, decrease, or no change in Variable B?"

## Exceptions

- **If one variable is categorical**, a scatterplot is not appropriate. A box plot, violin plot, or grouped bar chart would be better for comparing distributions across categories.
- **If the x-axis is not ordered**, a line chart can be misleading, as the connecting lines imply a sequence that doesn't exist. In this case, a scatterplot is the better choice.

## Trade-offs

- **Overplotting**: Scatterplots can become dense and unreadable when there are many data points, obscuring the true strength of the correlation. This can be mitigated with transparency, smaller points, or aggregation techniques (e.g., a heatmap).
- **Implied Causation**: While these charts show correlation, they do not inherently prove causation. Viewers may incorrectly infer a causal link where none exists.

## Evaluate

- [ ] Is a pie chart, bar chart, or table being used to show the relationship between two quantitative variables?
- [ ] Does the task involve judging a trend or correlation, but the chosen chart only effectively shows individual magnitudes or proportions?

## Repair

1.  If using a bar, pie, or other inappropriate chart, **replace it with a scatterplot**. Assign one variable to the x-axis and the other to the y-axis.
2.  If the variable on the x-axis is ordered (e.g., time), **consider using a line chart** to make the sequential relationship more explicit.
3.  If the resulting scatterplot is overplotted, **reduce point opacity** or use an aggregation technique like 2D binning (a heatmap) to show density.