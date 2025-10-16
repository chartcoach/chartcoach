---
id: use-scatterplot-for-correlation
title: "Use scatterplots to reveal correlation between two quantitative variables"

tags:
  - impact:perceptual
  - impact:logos
  - task:correlation
  - task:cluster
  - task:outlier-detection
  - data:quantitative
  - chart:scatter
  - medium:screen
  - medium:static

evidence:
  strength: high
  summary: "Empirical studies consistently show that scatterplots are the most effective visualization for perceiving correlation between two quantitative variables. A meta-analysis by Zeng & Battle (2023) synthesizes findings from multiple papers (e.g., Saket et al. 2018, Harrison et al. 2014) that recommend scatterplots for correlation and anomaly detection tasks."

sources:
  - type: research
    ref: Zeng & Battle, 2023
    url: https://doi.org/10.48550/arXiv.2109.01271
    note: "This meta-analysis (Table 9) identifies scatterplots as the top recommended visualization type for the 'Correlate' task, based on a synthesis of empirical work from sources like [20, 53, 78]."
    role: primary
  - type: research
    ref: Saket et al., 2019
    url: https://doi.org/10.1109/TVCG.2018.2864525
    note: "This study (referenced as [78] in Zeng & Battle) empirically tested ten visualization types across ten tasks and found scatterplots were highly effective for correlation and finding anomalies."
    role: supporting
  - type: research
    ref: Harrison et al., 2014
    url: https://doi.org/10.1109/TVCG.2014.2346979
    note: "This study (referenced as [33] in Zeng & Battle) specifically evaluated the human perception of correlation in nine different visualization types and found scatterplots performed best, with perception following Weber's Law."
    role: supporting

tools:
  - type: learn
    name: "From Data to Viz: Correlation"
    url: https://www.data-to-viz.com/story/TwoNum.html
    description: "An educational resource that guides users to choose a scatterplot for visualizing the relationship between two continuous variables, explaining why and providing code examples."

examples:
  - type: good
    description: "A classic scatterplot showing the relationship between height and weight. Each person is a dot. The upward-trending pattern of dots clearly and intuitively communicates the positive correlation between the two variables."
  - type: bad
    description: "Two separate bar charts, one for height and one for weight, sorted alphabetically. While each chart is valid on its own, placing them side-by-side makes it impossible to see the correlation between the variables at an individual level."
---

## Guidance

When the primary goal is to understand the relationship (correlation) between two continuous, quantitative variables, use a scatterplot.

## Why

A scatterplot maps two quantitative variables to a 2D Cartesian plane, with one variable on the x-axis and the other on the y-axis. This design makes the relationship between the variables emerge as a direct visual pattern. The human visual system is adept at identifying patterns like lines, curves, and clusters from clouds of points. A positive correlation appears as an upward trend, a negative correlation as a downward trend, and no correlation as a random cloud, making scatterplots the most direct and intuitive tool for this specific task.

### Core Principle

Effective visualization directly maps the structure of the analytical task onto a visual representation that the brain can process efficiently. For correlation, the task is to see a bivariate relationship, and the scatterplot's 2D structure provides a direct visual analogue.

## When it applies

- When you have two continuous, quantitative variables (e.g., height vs. weight, temperature vs. ice cream sales, years of experience vs. salary).
- When the main question is "How are these two variables related?" or "Is there a connection between X and Y?".
- For related tasks like identifying clusters (groups of similar points) and finding outliers (points that deviate from the main pattern).

## Exceptions

- **Overplotting:** If you have a very large number of data points, a standard scatterplot can become a solid, unreadable blob. In this case, modifications are needed.
- **Time Series Data:** While you can use a scatterplot to compare two time series, a line chart with two lines is often a more conventional and effective way to show trends over time.

## Trade-offs

- **Individual Value Lookup:** While possible, looking up the exact x and y values for a specific point in a dense scatterplot can be difficult without interactivity (e.g., tooltips). Bar charts or tables are better for precise value lookup.
- **Limited Variables:** A basic scatterplot is limited to two primary quantitative variables. Additional variables can be encoded with color, size, or shape, but this can add complexity and perceptual biases.

## Signs of Trouble

- **"Correlation" from Separate Charts:** You are trying to infer a relationship by looking at two or more separate charts (e.g., two bar charts or two pie charts). This requires cognitive, not visual, integration and is highly ineffective.
- **Using a Line Chart for Non-Temporal Data:** A line is drawn connecting points that do not have a sequential relationship (e.g., connecting points for different people sorted alphabetically). This implies a trend that doesn't exist.
- **Massive Overplotting:** The plot is a solid block of color where individual points are indistinguishable, hiding the underlying structure of the data.

## How to Improve

- **Create a Scatterplot:** If you have two quantitative variables, the default choice for exploring their relationship should be a scatterplot.

- **For Overplotting (Moderate):** If your scatterplot is too dense, use semi-transparent marks (alpha blending). This allows areas with more points to appear darker, revealing density patterns.

- **For Overplotting (Comprehensive):** For very large datasets, move from a simple scatterplot to a 2D density plot, a contour plot, or a heatmap (also known as a 2D histogram). These techniques aggregate points into bins and use color to show the number of points in each area, solving the overplotting problem while still revealing the overall relationship.
