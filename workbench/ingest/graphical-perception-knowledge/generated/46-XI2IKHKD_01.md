---
id: use-line-charts-for-correlation
title: "Use line charts or scatterplots to identify correlations"

tags:
  - impact:perceptual
  - impact:performance
  - chart:line
  - chart:scatter
  - task:correlation
  - data:quantitative
  - visual:position
  - audience:general
  - medium:static

evidence:
  strength: medium
  summary: "In an experiment with 180 participants, Saket et al. (2019) found that line charts and scatterplots were significantly more accurate for correlation tasks than bar charts, pie charts, and tables (p<0.05). Line charts were also significantly faster and highly preferred by users for this task."

sources:
  - type: research
    ref: Saket et al., 2019
    url: https://doi
.org/10.1109/TVCG.2018.2829750
    note: "Found line charts and scatterplots significantly more accurate for correlation tasks (p<0.05, η²=0.41). Line charts, scatterplots, and bar charts were also significantly faster than pie charts and tables (p<0.05, η²=0.70)."
    role: primary
  - type: research
    ref: Zeng & Battle, 2023
    url: https://doi.org/10.1145/3544548.3581349
    note: "This literature review includes and corroborates the findings from Saket et al., recommending scatterplots and line charts for correlation tasks in its summary of empirical work (Table 9)."
    role: supporting

---

## Guidance

To help users determine if a correlation exists between two variables, use a line chart (for ordered data) or a scatterplot.

## Why

Line charts and scatterplots both use position on a 2D plane to encode two variables. This representation allows the human visual system to perceive the overall shape and direction of the data points, making it effective for judging trends and relationships. Empirical studies show that users are significantly more accurate and faster at identifying correlations with these chart types compared to others like pie charts or tables, which are not designed for this task.

### Core Principle

The overall shape formed by a collection of marks (points, lines) is a powerful visual cue for judging a relationship between variables. Chart types that create a clear visual pattern of the relationship, like scatterplots and line charts, are superior for correlation tasks.

## When it applies

- The primary task is to assess the relationship (positive, negative, or none) between two quantitative variables.
- The x-axis variable is ordered (e.g., time, dose), making a line chart a particularly strong choice.
- The x-axis variable is not ordered, in which case a scatterplot is the standard choice.

## Exceptions

- When the number of data points is very low (e.g., less than 5), a correlation may not be visually apparent or meaningful, and a simple table might be sufficient.
- If there is a third categorical variable, a grouped scatterplot (using color or shape) can be effective, but too many categories can lead to clutter.

## Trade-offs

- While excellent for seeing the overall trend, both line charts and scatterplots can make it difficult to look up the precise value of a single data point, especially in dense plots.
- Overplotting in scatterplots with many data points can obscure the true density and strength of a correlation.

## Signs of Trouble

- **Incorrect Conclusions:** Users incorrectly identify a positive correlation as negative, or see a correlation where none exists, when using a pie chart or table.
- **Slow Performance:** Users take an excessively long time or give up when asked to describe the relationship between variables.
- **Low Confidence:** Users express that they are "just guessing" about the correlation.

## How to Improve

- **Quick Fix: Switch to a Scatterplot.** If currently using a pie chart, bar chart, or table to show a potential correlation, the most impactful and immediate improvement is to switch to a scatterplot. This is the standard and most effective visualization for this task.

- **Moderate Approach: Use a Line Chart for Ordered Data.** If the variable on the x-axis has a natural order (like time), connecting the points with a line chart can make the trend and correlation even clearer. Saket et al. (2019) found line charts were highly accurate, fast, and preferred for this task.

- **Comprehensive Approach: Add a Trend Line.** Enhance a scatterplot or line chart by adding a calculated regression line (trend line). This provides a single, clear visual summary of the direction and strength of the correlation, reducing the cognitive load on the user.