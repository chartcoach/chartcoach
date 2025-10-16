---
id: use-scatterplot-for-correlation
title: "Use scatterplots to show correlation between two quantitative variables"

tags:
  - impact:perceptual
  - chart:scatter
  - chart:parallel-coordinates
  - chart:line
  - task:correlation
  - data:quantitative
  - audience:general
  - medium:static

evidence:
  strength: high
  summary: "Multiple empirical studies (e.g., Harrison et al. 2014, Li et al. 2010) consistently find that scatterplots are significantly more effective for judging correlation than other visualizations like parallel coordinates, which can lead to underestimation of correlation strength."

sources:
  - type: research
    ref: Harrison et al., 2014
    url: https://doi.org/10.1109/TVCG.2014.2346979
    note: "Crowdsourced experiment showing significant differences in correlation perception across nine common chart types, with scatterplots performing very well."
    role: primary
  - type: research
    ref: Li, Martens, & van Wijk, 2010
    url: https://doi.org/10.1057/ivs.2008.13
    note: "Found that the degree of correlation is underestimated in parallel coordinate plots, suggesting scatterplots are better for this specific task."
    role: primary
  - type: research
    ref: Zeng & Battle, 2023
    url: https://arxiv.org/abs/2109.01271v3
    note: "Synthesizes the literature and recommends scatterplots as a top choice for the 'correlate' task based on empirical evidence (Table 9)."
    role: supporting

examples:
  - type: bad
    description: "A parallel coordinates plot used to show the relationship between GDP and life expectancy. The crossed lines make it difficult to judge the strength of the correlation."
  - type: good
    description: "A scatterplot showing GDP (x-axis) vs. life expectancy (y-axis). The upward-sloping pattern of the points clearly and intuitively communicates the positive correlation."
---

## Guidance

When the primary task is to help a viewer assess the relationship (correlation) between two quantitative variables, a scatterplot is the most effective chart type.

## Why

Scatterplots map the two variables directly to Cartesian x and y positions. The human visual system is excellent at detecting patterns in 2D point clouds. The strength, direction, and shape of the correlation become visually salient through the overall pattern of the points (e.g., a tight cluster sloping upwards indicates a strong positive correlation). Other chart types, like parallel coordinates, encode the data differently and have been shown to lead to systematic underestimation of correlation strength.

### Core Principle

Choose the chart type that makes the primary analytical task the easiest and most accurate perceptual task.

## When it applies

- The main goal is to see if two quantitative variables are related, and if so, how (e.g., positive, negative, strong, weak, linear, non-linear).
- You are performing exploratory data analysis to find relationships in the data.

## Exceptions

- **Many Variables:** If you need to show the relationships between *many* variables at once (>3-4), a scatterplot matrix (a grid of many small scatterplots) or a parallel coordinates plot may be more space-efficient. However, be aware that judging correlation in a parallel coordinates plot is less accurate. It is better for identifying clusters and outliers across many dimensions.
- **Time-Series Data:** If one of the variables is time, a line chart is the standard convention and is highly effective at showing trends over time. If you are correlating two different time series, you can use a dual-axis line chart (with caution) or a scatterplot where each point represents a single point in time.

## Trade-offs

- **Overplotting:** With very large datasets, a standard scatterplot can suffer from overplotting, where many points are plotted on top of each other, obscuring the true density.
- **Number of Variables:** A single scatterplot can only show the relationship between two variables (or three, by encoding a third with color or size).

## Signs of Trouble

- **Wrong Tool for the Job:** Using a line chart for two non-temporal variables, or using a bar chart where each bar represents a data point from a two-variable set.
- **Ambiguous Patterns:** The visualization used makes it difficult to describe the relationship. Viewers can't tell if there is a positive or negative correlation, or if it is strong or weak.
- **Underestimated Correlation:** Using parallel coordinates for correlation tasks, which has been shown to cause viewers to underestimate the strength of the relationship.

## How to Improve

- **Quick Fix: Switch to a Scatterplot.** If you are using another chart type (like a line chart for non-temporal data, or parallel coordinates) to show a two-variable relationship, the simplest and most effective fix is to switch to a scatterplot.

- **Moderate Approach: Address Overplotting.** If your scatterplot is too dense due to overplotting, adjust the opacity of the points (make them semi-transparent) or reduce the point size. This helps reveal the density and structure of the underlying data.

- **Comprehensive Approach: Use Binned or Density Plots.** For very large datasets, move beyond a simple scatterplot. Use a 2D histogram (which bins points into a grid and colors the grid cells by density) or a 2D kernel density estimate (KDE) plot. These techniques explicitly visualize the density of the data, completely solving the overplotting problem and clearly showing the shape of the correlation.
