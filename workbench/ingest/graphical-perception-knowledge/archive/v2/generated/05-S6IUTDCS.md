```markdown
---
id: scatterplot-color-for-tasks
title: "In scatterplots, use color for identification, not for judging group aggregates"

impact:
  - perceptual
  - cognitive
  - logos

tags:
  - scatterplot
  - color
  - size
  - faceting
  - position
  - aggregation
  - comparison
  - lookup
  - cardinality

sources:
  - type: research
    ref: Kim & Heer, 2018
    url: https://doi.org/10.1111/cgf.13409
    note: "Found that colored scatterplots are effective for comparing individual values but perform poorly for summary tasks (like comparing group averages), especially as the number of categories (cardinality) increases."

tools:
  - type: implement
    name: Vega-Lite
    url: https://vega.github.io/vega-lite/
    description: A high-level grammar that allows for easily swapping encoding channels (e.g., from `color` to `row` for faceting) to test different designs.
  - type: learn
    name: "Multiple Views & Small Multiples"
    url: https://www.data-to-viz.com/graph/common-patterns.html
    description: A guide on how to use small multiples (faceting) as an alternative to encoding many categories in a single chart.

examples:
  - type: good
    description: "A scatterplot where two quantitative values are mapped to X/Y position and a categorical value is mapped to color. This is effective for a task like 'What is the value of point A?' or 'Find the item named X'."
  - type: bad
    description: "The same colored scatterplot, but with 20 different colors (high cardinality). This design is ineffective for a task like 'Which category has the highest average value?' because judging the average position of a dispersed, overlapping cloud of colored points is perceptually difficult and error-prone."
  - type: good
    description: "To fix the bad example, the data is faceted into small multiples, where each category gets its own small scatterplot. This makes comparing the overall position and spread of each group much easier."
---

## Guidance

When using a scatterplot to show data with two quantitative and one categorical field, be mindful of the user's primary task. While using **color** to encode the categories is effective for tasks involving individual points (e.g., finding or comparing specific items), it is often inaccurate and slow for summary tasks (e.g., comparing the average value of different groups).

## Why

Humans are good at spotting a specific colored dot in a field of others, making colored scatterplots excellent for lookup tasks. However, our brains are not well-equipped to accurately calculate the 'center of mass' or average position of a dispersed cloud of same-colored points. This difficulty gets much worse as the number of colors (categories) increases, leading to high error rates for aggregate judgments.

## When it applies

- You are designing a scatterplot with two quantitative variables (on X and Y axes) and one categorical variable.
- The user's primary goal is to perform a **summary task**, like comparing the averages, ranges, or distributions of the different categories.
- The categorical variable has many levels (high cardinality), which increases visual clutter and makes color-based grouping more difficult.

## Exceptions

- When the primary or only task is to **find, identify, or read the values of individual data points**. In this case, a colored scatterplot is a very effective design.
- When categories are very tightly clustered and spatially separated, making the groups distinct and easy to judge regardless of the encoding.

## Trade-offs

- Using alternatives like **small multiples (faceting)** is more perceptually accurate for summary tasks but requires significantly more screen space.
- Using **size** to encode a quantitative variable can be effective for judging aggregates but may interfere with the precise perception of point positions.

## Evaluate

- [ ] A scatterplot uses color to encode categories.
- [ ] A primary goal for the user is to compare aggregate properties (like averages or distributions) between the colored groups.
- [ ] The number of categories is high (e.g., more than 5-7), causing many overlapping or intermingled colors.

## Repair

1.  For summary tasks, the best alternative is to use **small multiples (faceting)**. Give each category its own chart, arranged in a grid. This makes group-level comparisons direct and clear.
2.  If faceting is not an option, consider encoding one of the quantitative variables with **size** for the summary task. While less precise for reading individual values, size can be effective for judging group properties.
3.  If you must use a single colored scatterplot for summary tasks, explicitly add summary marks like average lines, boxplots, or confidence ellipses for each color group to aid comparison.