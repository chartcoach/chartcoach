---
id: use-scatterplot-for-correlation
title: "Use scatterplots to show bivariate correlation"

impact:
  - perceptual
  - cognitive
  - logos
  - ethical
  - ethos

tags:
  - scatterplot
  - correlation
  - bivariate-data
  - relationship
  - position
  - quantitative

sources:
  - type: research
    ref: Kay & Heer, 2016
    url: https://doi.org/10.1109/TVCG.2015.2467671
    note: "Finds that scatterplots offer the highest precision (lowest JND) and low individual variation for judging correlation compared to nine other visualization types."

examples:
  - type: good
    description: "A chart showing the relationship between height and weight uses a scatterplot, making the positive correlation easy to see."
  - type: bad
    description: "A stacked area chart is used to show the relationship between advertising spend and sales. The correlation is difficult to judge because the values are not plotted on independent x and y axes."
---

## Guidance

To help your audience judge the strength of a relationship (correlation) between two quantitative variables, use a scatterplot.

## Why

Research shows that people can estimate correlation most accurately and precisely when the data is encoded as points on an x-y coordinate system. Compared to many other chart types (like parallel coordinates, stacked area charts, or radar charts), scatterplots lead to more reliable perceptual judgments. They are highly effective for showing both positive and negative correlations and tend to be interpreted consistently by different people.

## When it applies

- The primary goal is to communicate the relationship, trend, or correlation between two numerical variables (e.g., height and weight, ad spend and revenue).
- Your dataset consists of paired quantitative values.

## Exceptions

- **Overplotting:** With very large datasets, a standard scatterplot can become a dense, unreadable blob. In these cases, the basic guidance still applies, but the implementation needs to be adapted (see Repair).
- **Time-Series Data:** If one of the variables is time, a line chart is the conventional and often more effective choice for showing trends over time, even though it's also a relationship between two quantitative variables.

## Trade-offs

- Scatterplots can take up significant screen space compared to more compact representations.
- They can be difficult to read if too many points are plotted in a small area, a problem known as overplotting. This can obscure the true density and structure of the data.

## Evaluate

- [ ] The visualization is intended to show the correlation between two numeric variables.
- [ ] The chart type used is something other than a scatterplot (e.g., a stacked bar chart, parallel coordinates plot, or radar chart).

## Repair

1.  **Change the chart type to a scatterplot.** Map one variable to the x-axis and the other to the y-axis.
2.  **Address overplotting if necessary.** If points overlap too much, try reducing marker opacity (alpha blending), using smaller markers, or sampling the data. For very dense data, consider using a 2D histogram (heatmap) or contour plot.
3.  **Add a trend line.** A line of best fit can help summarize the direction and strength of the correlation, but be careful not to imply a causal model where one doesn't exist.