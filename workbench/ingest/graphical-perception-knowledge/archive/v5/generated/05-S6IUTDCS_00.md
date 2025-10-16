---
id: avoid-colored-scatter-for-high-cardinality-summary
title: "Avoid colored scatterplots for summary tasks with high category counts"
tags:
  - impact:perceptual
  - impact:performance
  - chart:scatter
  - task:summary-mean
  - task:aggregate
  - data:categorical
  - data:cardinality.high
  - visual:color
  - visual:position
  - access:cognitive-load-risk
evidence:
  strength: medium
  summary: "A 2018 experiment by Kim & Heer found that for summary tasks, the error rate of colored scatterplots increases significantly as the number of categories (cardinality) or points per category increases, due to visual congestion and occlusion."
sources:
  - type: research
    ref: Kim & Heer, 2018
    url: https://doi.org/10.1111/cgf.13409
    note: "Primary experiment showing performance degradation for summary tasks on colored scatterplots with high cardinality (see Figure 7)."
    role: primary
tools: []
examples: []
---

## Guidance

When users need to perform summary tasks (e.g., comparing averages between groups) on a dataset with many categories, avoid using a single colored scatterplot where each category is represented by a different color.

## Why

As the number of categories or data points increases, a single scatterplot becomes visually congested. Overlapping points of different colors make it difficult for the human visual system to accurately perceive the aggregate properties (like the average or spread) of any single group. This leads to higher error rates and slower performance.

### Core Principle

Visual congestion and overplotting inhibit the perception of group-level summary statistics. Separating groups into distinct visual spaces (faceting) or abstracting them (calculating averages) can restore perceptual accuracy.

## When it applies

- When performing summary or aggregation tasks (e.g., "Which category has the highest average?").
- When the categorical variable encoded by color has high cardinality (e.g., more than 5-7 categories).
- When there are many data points per category, leading to heavy overplotting and occlusion.

## Exceptions

- For value-based tasks (e.g., "What is the value of this specific point?"), colored scatterplots perform well, even with many points, as the user is focused on a single mark.
- If the categories are spatially well-separated in the plot (forming distinct visual clusters), the negative effect of color is reduced.

## Trade-offs

- Avoiding a scatterplot means you lose the ability to see the relationship between the two quantitative variables and the raw data distribution simultaneously. Alternative chart types that show only the summary (like a bar chart of averages) abstract away this detail.

## Signs of Trouble

- **Visual Clutter:** The plot looks like a "ball of yarn" or "confetti," with many colors mixed together, making it hard to distinguish any single group.
- **Group Indistinguishability:** It's hard to visually isolate a single color group to judge its central tendency or spread.
- **Task Failure:** Users give incorrect answers when asked to compare the average value of two different color groups.

## How to Improve

- **Quick Fix: Reduce Opacity.** Lowering the opacity of the points can help reveal areas of high density and reduce the visual impact of occlusion, but it may not solve the core issue for judging averages across intermingled groups.

- **Moderate Redesign: Facet the Chart.** Use small multiples (faceted charts) to give each category its own plot. This completely eliminates cross-category occlusion and has been shown to restore high accuracy for summary tasks. The trade-off is that this approach can be slower for users, especially if it requires scrolling.

- **Comprehensive Redesign: Use a Summary Chart Type.** If the summary statistic is the most important part of the story, pre-calculate it and use a chart designed for comparison, such as a **bar chart** or **dot plot** of the category averages. This makes the summary comparison task much easier and more accurate, though it hides the underlying distribution of the raw data.
