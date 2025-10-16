---
id: avoid-colored-scatter-for-summary-tasks
title: "Avoid colored scatterplots for summary tasks with many categories"
tags:
  - impact:perceptual
  - impact:cognitive
  - chart:scatter
  - task:summary-mean
  - task:summary-median
  - task:compare
  - data:categorical
  - data:cardinality.high
  - visual:color
  - visual:position
  - access:cognitive-load-risk
sources:
  - type: research
    ref: Kim & Heer, 2018
    url: https://doi.org/10.1111/cgf.13409
    note: "The primary source for this finding. The abstract and Section 4.3.1 state that colored scatterplots 'perform poorly for summary tasks as the number of categories increases' due to 'visual congestion'."
examples:
  - type: bad
    description: "A scatterplot with 20 categories encoded by color. It is impossible to perform a summary task like 'Which category has the highest average Y-value?' because the colors are intermingled and occluded, preventing a viewer from mentally isolating and averaging one group."
  - type: good
    description: "The same data is presented using small multiples (faceted charts). Each category gets its own subplot. Now, the task of finding the group with the highest average Y-value is much easier, as each group is visually isolated. Alternatively, one could pre-compute the averages and plot them in a simple bar chart."
---

## Guidance

For summary tasks like comparing the average value of different groups, avoid using a single scatterplot that encodes categories with color, especially when the number of categories is high.

## Why

As the number of categories (and thus colors) increases, or as the number of data points grows, a single scatterplot becomes visually congested. Points from different categories overlap and occlude one another, making it perceptually and cognitively overwhelming for a viewer to mentally isolate a single color group and estimate its aggregate properties (like its center or spread). The task of comparing the average of the blue dots to the average of the red dots becomes nearly impossible.

## When it applies

- The task is a **summary** or **aggregate** task (e.g., "Which group has the higher average?", "Compare the distributions of group A and B").
- The chart is a **scatterplot** where two quantitative variables are mapped to X/Y position.
- A third, **categorical** variable is mapped to **color**.
- The cardinality of the categorical variable is high (e.g., more than 5-7 categories), or the data is dense, leading to overplotting.

## Exceptions

- **Low Cardinality:** If you have only 2 or 3 categories that are well-separated (i.e., they form distinct, non-overlapping clusters), it may be possible to perform summary tasks on a single colored scatterplot.
- **Finding Clusters:** If the primary task is to identify the existence of clusters themselves, rather than comparing their summary statistics, a colored scatterplot is an appropriate choice.

## Trade-offs

- **Space:** A single, dense scatterplot is very space-efficient. The primary alternative, small multiples, uses significantly more screen or page real estate.
- **Direct Comparison:** A single plot theoretically allows for direct comparison of point distributions. However, this benefit is lost once visual congestion becomes too high. Small multiples make individual group distributions clearer at the cost of making direct, overlapping comparison harder.

## Signs of Trouble

- **The "Squint Test":** If you squint your eyes, do the distinct color groups blur into a single, indecipherable mass? If so, summary tasks are likely impossible.
- **"Where's Waldo?" Effect:** It's difficult to find or visually track all the points belonging to a single category.
- **Overplotting:** Many points are plotted on top of each other, hiding the true density and distribution of each category.
- **User Frustration:** Viewers cannot answer questions like "Which category is generally higher on the Y-axis?" without great difficulty.

## How to Improve

- **Quick Fix: Reduce Opacity.** Lowering the opacity of the points can help reveal areas of high density and mitigate some overplotting. However, this often does not solve the fundamental problem of cognitive overload for summary tasks.

- **Moderate Redesign: Use Small Multiples (Faceting).** Instead of one large plot, create a grid of smaller plots, where each plot (or "facet") shows the data for just one category. This completely eliminates the issue of inter-category overplotting and allows the viewer to see the distribution of each group clearly. The trade-off is increased space and a different comparison task (scanning across plots vs. within one).

- **Comprehensive Approach: Plot the Summary Statistic Directly.** If the primary task is to compare the averages, the most effective solution is to pre-calculate the averages for each category and plot them directly. A simple bar chart or dot plot showing the average for each category is far more effective for this specific task than a scatterplot showing all the raw data. This directly visualizes the answer to the user's question.