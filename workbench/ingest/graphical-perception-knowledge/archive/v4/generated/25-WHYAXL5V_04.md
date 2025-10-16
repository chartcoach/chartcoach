---
id: use-scatterplots-for-correlation
title: "Use scatterplots to show the relationship between two quantitative variables"

tags:
  - impact:perceptual
  - impact:logos
  - chart:scatter
  - task:correlation
  - task:cluster
  - task:find-anomalies
  - data:quantitative
  - visual:position

sources:
  - type: research
    ref: Harrison et al., 2014
    url: https://doi.org/10.1109/TVCG.2014.2346979
    note: "Cited as [33] in the review paper, this study evaluated how people perceive correlation in nine different visualization types and found significant differences, with scatterplots being a top performer."
  - type: research
    ref: Li et al., 2010
    url: https://doi.org/10.1057/ivs.2008.13
    note: "Cited as [53], this study compared scatterplots and parallel coordinate plots for correlation tasks, finding that scatterplots are generally better."

tools:
  - type: learn
    name: "Data Viz Project: Scatterplot"
    url: https://datavizproject.com/data-type/scatterplot/
    description: "A clear description of scatterplots with multiple visual examples."

examples:
  - type: good
    description: "A chart plotting car weight (x-axis) vs. miles per gallon (y-axis). The downward-sloping pattern of points clearly reveals a negative correlation: as weight increases, MPG tends to decrease."
  - type: bad
    description: "A dual-axis line chart trying to show the same weight vs. MPG relationship. The two lines and their independent scales make it very difficult to judge the underlying correlation between the two variables."
---

## Guidance

To help viewers understand the relationship, correlation, and clustering patterns between two quantitative variables, use a scatterplot. Map each variable to a position on the X and Y axes.

## Why

Scatterplots are the most effective visualization for showing the relationship between two numeric variables. They map data to a 2D Cartesian plane, allowing the human visual system's powerful pattern-detection capabilities to identify trends (positive, negative, or no correlation), clusters, gaps, and outliers. Alternative visualizations, like parallel coordinates or dual-axis line charts, are significantly less effective for this specific task.

## When it applies

- When you have two quantitative variables and want to see if and how they are related.
- When the task is to identify correlation, find clusters of data points, or spot anomalies that deviate from the main pattern.

## Exceptions

- **Overplotting:** When you have a very large number of data points, a standard scatterplot can become a dense, unreadable blob where individual points are obscured. In this case, the relationship is hidden.
- **More than two variables:** A single scatterplot can only show two variables. To explore relationships among three or more, you would need a scatterplot matrix (SPLOM) or a different chart type like parallel coordinates.

## Trade-offs

- **Detail vs. Overview:** A scatterplot shows every individual data point. This can be a drawback if the overall trend (like a regression line) is more important than the individual points, or if the number of points is overwhelming.
- **Requires two quantitative variables:** Scatterplots are not suitable for categorical data, unless used in variations like strip plots.

## Signs of Trouble

- **Overplotting:** The chart is a solid mass of color, and you cannot distinguish individual points or see the density of the data in different regions.
- **Misleading Trend Line:** A regression or trend line is added to the plot, but it hides or misrepresents the true underlying pattern (e.g., a linear trend line on non-linear data).
- **Using a less effective chart:** You are trying to show correlation with a dual-axis line chart or by placing two pie charts side-by-side.

## How to Improve

- **Quick Fix: Adjust Transparency.** If overplotting is an issue, reduce the opacity of the points. This allows overlapping points to create darker areas, revealing the density of the data.
- **Moderate Approach: Use a 2D Density Plot.** For very dense datasets, switch from a scatterplot to a 2D histogram or a contour plot (often represented as a heatmap). This aggregates the points into bins and uses color to show the number of points in each area, solving the overplotting problem and revealing the density distribution.
- **Comprehensive Redesign: Use a Scatterplot Matrix (SPLOM).** If you need to explore correlations among multiple quantitative variables (more than two), create a scatterplot matrix. This is a grid of scatterplots that shows the relationship between every pair of variables in your dataset, providing a comprehensive overview.