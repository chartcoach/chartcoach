---
id: prefer-scatterplots-for-correlation
title: "Prefer scatterplots over parallel coordinates for judging correlation"

tags:
  - impact:perceptual
  - chart:scatter
  - chart:parallel-coordinates
  - task:correlation
  - data:quantitative
  - data:cardinality.high

evidence:
  strength: medium
  summary: "Research comparing scatterplots and parallel coordinate plots for correlation tasks found that users systematically underestimate the degree of correlation in parallel coordinates. Scatterplots lead to more accurate judgments of the strength of the relationship between two variables."

sources:
  - type: research
    ref: Li et al., 2010
    note: "The paper's citation is [53] in Zeng & Battle. Found that the degree of correlation between attributes is underestimated in parallel coordinates, suggesting that scatterplots are better options for 'correlate' tasks."
    role: primary
  - type: research
    ref: Harrison et al., 2014
    url: https://doi.org/10.1109/TVCG.2014.2346979
    note: "While focused on ranking correlation visualizations in general, this study reinforces that scatterplots are highly effective for this task, aligning with the findings of Li et al. (2010)."
    role: supporting
  - type: research
    ref: Zeng & Battle, 2023
    url: https://doi.org/10.1145/3544548.3581349
    note: "This review synthesizes the findings from Li et al. (2010) and other papers, recommending scatterplots for correlation tasks in their summary Table 9."
    role: related

examples:
  - type: good
    description: "A scatterplot showing a clear positive correlation between two variables. The pattern of the points forming a rough line from bottom-left to top-right is a strong visual cue for correlation."
  - type: bad
    description: "A parallel coordinates plot showing the same correlated data. While patterns of crossing lines indicate negative correlation, the visual strength of the correlation is much harder to judge accurately compared to the scatterplot."
---

## Guidance

When the primary task is to assess the correlation (the strength and direction of a relationship) between two quantitative variables, use a scatterplot. Avoid using a parallel coordinates plot for this specific task.

## Why

Humans are perceptually well-attuned to judging correlation from the shape of a point cloud in a scatterplot. The alignment of points along an implicit line provides a strong and intuitive visual cue for the strength of a relationship. In contrast, while parallel coordinates plots can reveal correlations through patterns of lines (e.g., many crossing lines suggest a negative correlation), research shows that people systematically underestimate the strength of the correlation from this representation. This makes scatterplots a more reliable and accurate tool for this specific analytical task.

## When it applies

- When the main goal is to determine if two quantitative variables are related, and if so, what the direction (positive or negative) and strength of that relationship is.
- When comparing the effectiveness of different chart types for a multivariate dataset.

## Exceptions

- **Multivariate Pattern Detection:** Parallel coordinates plots are designed to visualize many variables at once (not just two). They are effective for other tasks like identifying clusters, finding outliers, and seeing patterns across multiple dimensions. If the goal is to see relationships between *many* variables simultaneously, a parallel coordinates plot is appropriate, even if it's not optimal for judging the specific correlation strength between any single pair.
- **Interactive Systems:** In an interactive system, a parallel coordinates plot can be used as a filtering tool to select data that is then viewed in a more detailed scatterplot (a technique called "brushing and linking"). In this case, the two chart types complement each other.

## Trade-offs

- **Number of Variables:** A single scatterplot can only show the relationship between two (or maybe three) variables at a time. A parallel coordinates plot can display dozens of variables at once. Choosing a scatterplot prioritizes accuracy for a single relationship over a holistic view of the entire dataset.
- **Data Density:** With very high data density, both chart types can suffer from overplotting, though techniques like transparency or sampling can mitigate this.

## Signs of Trouble

- **Uncertain Judgments:** Users looking at a parallel coordinates plot express low confidence or high uncertainty when asked to estimate the strength of a correlation between two axes.
- **Misleading Comparisons:** Decisions are being made based on perceived correlations from a parallel coordinates plot, which are likely to be underestimates of the true statistical relationship.

## How to Improve

- **Quick Fix: Add a Scatterplot.** If you are already using a parallel coordinates plot, supplement it with scatterplots for the most important variable pairs. This allows users to get both the high-level multivariate view and an accurate bivariate correlation view.
- **Moderate Approach: Use a Scatterplot Matrix (SPLOM).** For a moderate number of variables (e.g., 3-10), replace the parallel coordinates plot with a scatterplot matrix. This shows a small scatterplot for every pair of variables in your dataset, allowing for accurate correlation judgments across all pairs.
- **Comprehensive Approach: Guide the User.** In an interactive tool, default to showing key relationships in a scatterplot. If using a parallel coordinates plot for filtering, ensure that when a user shows interest in a specific pair of axes, the system can automatically generate a detailed scatterplot of just those two variables.
