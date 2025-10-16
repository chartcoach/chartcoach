---
id: avoid-treemaps-for-simple-composition
title: "Prefer stacked bars or pie charts over treemaps for simple part-to-whole comparisons"

impact:
  - perceptual
  - cognitive
  - logos
tags:
  - treemap
  - pie-chart
  - stacked-bar-chart
  - composition
  - comparison
  - part-to-whole

sources:
  - type: research
    ref: Kosara, 2019
    url: https://doi.org/10.2312/EVS.20191162
    note: "Found treemaps were less accurate and slower than pie charts and stacked bar charts for comparing parts of a whole with a small number of categories."

examples:
  - type: bad
    description: "A treemap used to show the breakdown of a budget across five departments. Viewers are likely to be slower and less accurate at judging the size of each department's share compared to if a pie chart or stacked bar chart were used."
  - type: good
    description: "A stacked bar chart showing market share for five companies. This allows for reasonably accurate part-to-whole comparison, outperforming a treemap for the same task."

---

## Guidance

For simple part-to-whole comparisons with a small number of categories, prefer using a stacked bar chart or a pie chart over a treemap.

## Why

When people are asked to judge the size of different parts of a whole (e.g., "what percentage is this slice?"), they are less accurate and take longer when reading a treemap compared to a pie chart or a stacked bar chart. Treemaps encode values as rectangular areas, which are harder for our eyes to compare precisely than the length in a bar chart or the angle/area in a pie chart.

## When it applies

- When showing part-to-whole relationships (composition).
- When the number of categories is small (e.g., 2-7 categories).
- When a primary task for the user is to compare the size or percentage of individual parts.

## Exceptions

- **When visualizing hierarchical data.** Treemaps excel at showing a nested structure (e.g., continent > country) within a fixed space, which is their original and most powerful use case.
- **When there is a very large number of categories.** For hundreds or thousands of parts, a treemap can provide a compact overview of the distribution, even if precise comparisons are difficult. In this scenario, it functions more like a heatmap of values.

## Trade-offs

- **Space Efficiency:** Treemaps are often more space-efficient, as they fill a rectangular area completely. Bar charts and pie charts can leave more white space or have awkward aspect ratios.
- **Pie Chart Baggage:** While pie charts performed better than treemaps in this context, they are often criticized for other perceptual issues, especially when slices are similarly sized or when making part-to-part comparisons. Use them with care.

## Evaluate

- [ ] A treemap is used to show composition for a small number of non-hierarchical categories (e.g., fewer than 10).
- [ ] A key task for the viewer is to accurately judge or compare the percentage of individual segments.

## Repair

1. **Switch to a stacked bar chart.** This is often the most robust alternative, as it allows for easy comparison of the parts.
2. **Consider a pie chart (with caution).** If the data has very few categories (2-4) and the goal is strictly part-to-whole judgment, a pie chart can be effective and familiar. Ensure it is well-labeled with percentages.
3. **If a treemap must be used,** add direct labels (category name and value/percentage) to each rectangle to compensate for the difficulty of perceptual estimation.