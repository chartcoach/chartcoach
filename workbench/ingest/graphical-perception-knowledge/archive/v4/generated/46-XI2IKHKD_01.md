---
id: use-line-charts-for-correlation
title: "Use line charts to identify correlations"

tags:
  - impact:perceptual
  - impact:performance
  - chart:line
  - task:correlation
  - data:quantitative
  - data:ordinal
  - audience:general
  - medium:static

sources:
  - type: research
    ref: Saket et al., 2019
    url: https://doi.org/10.1109/TVCG.2018.2829750
    note: "The study found line charts and scatterplots were fastest and most accurate for correlation tasks, but user preference was significantly higher for line charts (Guideline G2)."

examples:
  - type: good
    description: A line chart shows the relationship between movie budget and profit over time. The upward or downward trend of the line makes the correlation clear.
  - type: bad
    description: A pie chart attempts to show the same relationship. It is impossible to determine the correlation from the angles of the slices.
---

## Guidance

For tasks that require users to determine if a correlation exists between two variables (especially when one is ordered, like time), use a line chart.

## Why

Line charts connect data points, creating a single, continuous object. The human visual system is excellent at perceiving the overall slope and direction of this line, which directly maps to the concept of a positive or negative correlation (a trend). An empirical study demonstrated that for correlation tasks, line charts are not only fast and accurate but also significantly more preferred by users than other effective charts like scatterplots.

## When it applies

- The primary task is to assess the relationship between two variables: "Is there a correlation between X and Y?".
- At least one of the variables has a natural order (e.g., time, age groups, rating levels).

## Exceptions

- **When data is not ordered:** If neither variable has a natural order, a scatterplot is the more appropriate and conventional choice for showing correlation. Using a line chart would imply a false sequence.
- **To see distribution and outliers:** A scatterplot is superior at revealing the underlying distribution, density, and specific outliers in the data, which a line chart can obscure. If these aspects are more important than the overall trend, prefer a scatterplot.

## Trade-offs

- **Obscures individual points:** A line chart emphasizes the overall trend at the expense of individual data points. If outliers or the precise location of each point are important, a scatterplot is better.
- **Implies continuity:** The connecting line can suggest that data exists between the measured points, which may not be true.

## Signs of Trouble

- **Low accuracy:** Users incorrectly identify the presence, absence, or direction of a correlation.
- **Slow performance:** Users take a long time to answer questions about the relationship between two variables.
- **Wrong tool for the job:** A table, pie chart, or bar chart is being used, requiring users to perform slow, cognitively demanding mental calculations to infer a correlation.

## How to Improve

- **Quick approach:** If stuck with a scatterplot, add a trend line (line of best fit) to make the correlation more explicit.
- **Comprehensive approach:** If the data has an ordered attribute, switch to a line chart to leverage its perceptual advantages for trend and correlation identification. This aligns with both user performance and preference.
