---
id: use-scatterplot-for-correlation
title: "Use scatterplots to show correlation between two variables"

tags:
  - impact:perceptual
  - task:correlation
  - data:quantitative
  - chart:scatter
  - chart:parallel-coordinates

evidence:
  strength: medium
  summary: "Empirical studies consistently show that scatterplots are a top-performing visualization for identifying correlation. Zeng & Battle's (2023) review notes that scatterplots are recommended for correlation tasks based on work by Harrison et al. (2014) and Saket et al. (2019), and are superior to parallel coordinates for this specific task according to Li et al. (2010)."

sources:
  - type: research
    ref: Zeng & Battle, 2023
    url: https://doi.org/10.1145/3544548.3581349
    note: "Synthesizes empirical results in Table 9, showing scatterplots as a recommended design for 'Correlate' tasks, citing sources [53, 20, 78]. Also notes Li et al. [53] found scatterplots better than parallel coordinates for this task."
    role: primary
  - type: research
    ref: Harrison et al., 2014
    url: https://doi.org/10.1109/TVCG.2014.2346979
    note: "A crowdsourced experiment (n=1,755) that evaluated human perception of correlation across nine visualization types, finding scatterplots to be highly effective."
    role: supporting
  - type: research
    ref: Kay & Heer, 2015
    url: https://doi.org/10.1109/TVCG.2015.2467671
    note: "A re-analysis and extension of Harrison et al.'s work, providing a more nuanced model for correlation perception in scatterplots."
    role: related
---

## Guidance

When the primary goal is to show the relationship or correlation between two quantitative variables, use a scatterplot.

## Why

Scatterplots directly map two quantitative variables to the two positional axes (X and Y). This direct mapping allows the human visual system to effectively perceive the overall shape, direction, and strength of the relationship as a visual pattern. Empirical studies have confirmed that viewers are better at estimating correlation from scatterplots than from many other visualization types, including parallel coordinate plots.

## When it applies

- When you have two paired quantitative variables (e.g., 'Height' and 'Weight', 'Temperature' and 'Ice Cream Sales').
- When the main question is "Is there a relationship between variable A and variable B?".
- For identifying patterns like linear trends, non-linear trends, and clusters.

## Exceptions

- **Many variables:** A standard scatterplot only shows two variables. For exploring correlations across many variables, a scatterplot matrix (SPLOM) or other multivariate visualization techniques might be necessary.
- **Overplotting:** If you have a very large number of data points, a standard scatterplot can become a dense, unreadable blob. In this case, techniques like transparency, binning (creating a 2D histogram or hexbin plot), or sampling are needed to reveal the underlying density and patterns.

## Trade-offs

- **Clutter:** With a large dataset, a simple scatterplot can become cluttered and unreadable (overplotting).
- **Limited Variables:** A single scatterplot is limited to showing the relationship between two (or maybe 3-4, with color and size) variables at a time.

## Signs of Trouble

- **Correlation Obscured:** You are trying to describe a correlation using a chart type not suited for it, such as a dual-axis line chart or a grouped bar chart, making the relationship difficult or impossible to see.
- **"Hairball" Plot:** In a parallel coordinates plot with many data points, the lines are so dense that it's impossible to discern the pattern of correlation between any two axes.
- **Overplotted Mess:** The scatterplot is just a solid block of color, obscuring the density and distribution of points within it.

## How to Improve

- **Quick Fix: Adjust Transparency.** If a scatterplot is overplotted, make the points semi-transparent. This allows dense regions to appear darker, revealing the underlying data distribution.
- **Moderate Approach: Switch to a Scatterplot.** If you are using another chart type to show correlation, switch to a scatterplot. This is almost always the most direct and effective method.
- **Comprehensive Approach: Use Binning for Large Datasets.** For very large datasets, replace the scatterplot of individual points with a 2D histogram or a hexbin plot. These charts divide the canvas into a grid and use color intensity to show the number of data points that fall into each bin, effectively solving the overplotting problem while still showing the correlation pattern.