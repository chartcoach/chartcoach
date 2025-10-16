---
id: avoid-colored-scatterplots-for-high-cardinality-summary-tasks
title: "Avoid colored scatterplots for summary tasks with many categories"

tags:
  - impact:perceptual
  - impact:cognitive
  - chart:scatter
  - task:summary-mean
  - task:aggregate
  - data:categorical
  - data:cardinality.high
  - visual:color
  - visual:position
  - audience:general
  - medium:static
  - medium:interactive
  - access:cognitive-load-risk

evidence:
  strength: medium
  summary: "An experiment with 1,920 participants (Kim & Heer, 2018) found that the effectiveness of colored scatterplots for summary tasks (e.g., comparing averages) degrades significantly as the number of color-coded categories increases, due to visual congestion and occlusion."

sources:
  - type: research
    ref: Kim & Heer, 2018
    url: https://doi.org/10.1111/cgf.13409
    note: "Primary experiment showing that colored scatterplots (Q1:y, Q2:x, N:color) perform well for value tasks but poorly for summary tasks, with error rates increasing as categorical cardinality increases."
    role: primary
  - type: research
    ref: Zeng & Battle, 2023
    url: https://doi.org/10.1145/3544548.3581349
    note: "This review paper contextualizes findings like Kim & Heer's, showing how they can be used to form specific, evidence-based rules for visualization recommendation systems."
    role: related
---

## Guidance

When the task is to perform summary judgments (e.g., comparing the average value of different groups), avoid using a single scatterplot where a categorical variable with many unique values (high cardinality) is encoded by color.

## Why

While colored scatterplots are effective for identifying individual points, they become perceptually challenging for summary tasks as the number of categories grows. With many overlapping colors, it is difficult for the human visual system to mentally group all points of a single color and estimate their aggregate properties (like their average position or density). This visual congestion and occlusion leads to higher error rates.

### Core Principle

The effectiveness of a visual encoding is highly dependent on the analytical task. An encoding that is good for looking up individual values (e.g., color for identification) may be poor for judging group properties (e.g., color for aggregation).

## When it applies

- The analytical task is a summary or aggregation task, such as "Which category has the higher average?" or "Identify the cluster of points for Category X."
- The categorical variable being encoded with color has a high cardinality (e.g., more than 5-7 categories).
- The data points for different categories are likely to overlap spatially.

## Exceptions

- When the task is a value-lookup or identification task (e.g., "What category is this specific point?"). Color is excellent for this.
- If the categories are spatially well-separated (i.e., they form distinct, non-overlapping clusters). In this case, color can effectively delineate the groups.
- When the categorical variable has very low cardinality (e.g., 2-3 categories), making it easier to mentally segregate the groups.

## Trade-offs

- **Density vs. Clarity:** A single colored scatterplot is very data-dense, showing all data in one view. Switching to an alternative like small multiples uses more space but provides greater clarity for each category.
- **Directness vs. Abstraction:** The scatterplot shows the raw data. Alternatives like a bar chart of averages show a statistical abstraction, which is easier to compare but hides the underlying distribution and uncertainty.

## Signs of Trouble

- **The "Hairball" Effect:** The chart is a dense cloud of overlapping, multi-colored points, making it impossible to distinguish groups.
- **Inaccurate Takeaways:** Viewers consistently misjudge which category has a higher average or greater spread.
- **Slow Performance:** It takes users a very long time to answer a summary question because they have to visually hunt for and mentally isolate all points of a given color.
- **Color Overload:** You have more colors in your legend than you can easily distinguish in the plot itself.

## How to Improve

- **Quick Fix: Use Opacity.** If you must use a single plot, reduce the opacity of the marks. This can help reveal the density of overlapping points and make dense clusters more apparent.
- **Moderate Redesign: Switch to a Summary Chart.** Instead of showing all the raw points, calculate the summary statistic of interest (e.g., the average for each category) and display it in a chart better suited for comparison, such as a bar chart or dot plot.
- **Comprehensive Redesign: Use Small Multiples (Faceting).** Create a separate scatterplot for each category. This completely eliminates the problem of color-based grouping and allows for clean, accurate comparison of the patterns within each category, though it may take longer to view.
