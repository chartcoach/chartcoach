---
id: trust-viewers-to-estimate-nonlinear-trends
title: "Trust viewers to visually estimate simple non-linear trends"
tags:
  - impact:perceptual
  - impact:cognitive
  - chart:scatter
  - chart:line
  - task:trend
  - task:correlation
  - data:quantitative
  - data:non-linear
  - audience:general
  - medium:interactive
  - medium:static
sources:
  - type: research
    ref: Correll & Heer, 2017
    url: https://doi.org/10.1145/3025453.3025922
    note: "Found no significant difference in accuracy when viewers estimated linear, quadratic, or trigonometric trends, suggesting 'regression by eye' is also effective for simple non-linear relationships."
---
## Guidance

For simple, clear non-linear patterns (like a basic curve or cyclical wave), you can often trust viewers to accurately perceive the general shape and direction of the trend without explicitly plotting a regression model.

## Why

Research shows that people are capable of performing "regression by eye" on simple non-linear data, not just straight lines. For basic curves, their estimation accuracy is comparable to their accuracy with linear trends. This means you do not always need to add a complex formula or trend line, which can clutter the chart, if the pattern is visually apparent.

## When it applies

- When visualizing data with a clear, simple non-linear relationship (e.g., a simple parabolic curve, a seasonal sine wave).
- During exploratory data analysis where the primary goal for the viewer is to identify the basic shape of the relationship.
- When you want to minimize visual clutter by not adding an explicit trend line.

## Exceptions

- For complex or noisy non-linear relationships where the underlying pattern is not visually obvious.
- When the specific parameters of the non-linear model (e.g., the exact coefficient of a polynomial regression) are important for the audience to know.
- When comparing the fit of multiple different non-linear models to the data.

## Trade-offs

- **Clutter vs. Precision:** Omitting the trend line keeps the visualization clean but relies on the viewer's perceptual system, which may introduce small inaccuracies. Adding the trend line provides precision and specifies a model but adds visual elements to the chart.

## Signs of Trouble

- **Model Misidentification:** Viewers misinterpret the shape of the trend, for instance by trying to fit a straight line to clearly curved data.
- **Inconsistent Interpretations:** Different viewers describe the non-linear trend in wildly different ways, indicating the pattern is not clear enough to be interpreted consistently without guidance.
- **High Noise:** If the data is very noisy, the underlying non-linear pattern may be obscured, making visual estimation unreliable.

## How to Improve

- **Quick Fix: Use Annotations.** Add a simple text annotation like "Note the curving pattern" or "Data shows a cyclical trend" to guide the viewer's attention without adding a full trend line.

- **Moderate Redesign: Add a Smoothed Trend Line.** Use a non-parametric smoother (like LOESS) to add a flexible trend line. This captures the general shape of the data without committing to a specific mathematical model, balancing guidance and flexibility.

- **Comprehensive Redesign: Add a Parametric Trend Line.** If a specific model is appropriate (e.g., a quadratic fit), plot that trend line. For expert audiences, consider including the model's equation or R² value to provide maximum clarity and precision.