---
id: viewer-trend-estimation-is-robust-to-outliers
title: "Be aware that viewers' trend estimates are robust to outliers"

tags:
  - impact:perceptual
  - impact:cognitive
  - chart:scatter
  - chart:line
  - chart:area
  - task:trend
  - task:correlation
  - data:quantitative
  - data:outliers
  - audience:general
  - medium:static
  - medium:interactive

evidence:
  strength: medium
  summary: "A 2017 study found that when visually estimating trends, people give significantly less weight to outliers than standard Ordinary Least Squares (OLS) regression. Their 'regression by eye' is more akin to a robust regression model."

sources:
  - type: research
    ref: Correll & Heer, 2017
    url: https://doi.org/10.1145/3025453.3025922
    note: "Primary experiment (Experiment 3) found that viewers' trend estimations down-weight outliers, diverging from outlier-sensitive OLS models."
    role: primary
  - type: research
    ref: Zeng & Battle, 2023
    url: https://doi.org/10.1145/3544548.3581349
    note: "Collated this finding as part of a systematic review, highlighting the difference between human perceptual models and standard statistical models."
    role: supporting

examples:
  - type: bad
    description: "A chart of sales data with a few extreme outlier days is presented without a trend line. The designer expects the audience to perceive the OLS trend, but viewers will likely estimate a trend that ignores the outliers, leading to a disconnect between human and statistical conclusions."
  - type: good
    description: "The same sales chart with an explicitly drawn OLS trend line. The annotation makes it clear which trend model (the outlier-sensitive one) the viewer should consider, preventing ambiguity."
---

## Guidance

When visualizing data with outliers, explicitly decide whether the viewer should perceive the outlier-sensitive trend (e.g., Ordinary Least Squares) or a more robust, outlier-resistant trend. Annotate the chart to guide them to your intended interpretation.

## Why

Human visual perception is not a statistical algorithm. When estimating trends by eye, people naturally filter out or give less weight to extreme values. This "robust estimation" is a powerful heuristic, but it differs from standard statistical models like OLS regression that are highly sensitive to outliers. If your analysis or story relies on the influence of outliers, you cannot depend on the viewer to see that trend naturally. You must explicitly draw it for them.

### Core Principle

Human visual processing often defaults to robust estimation, automatically discounting extreme values that standard statistical models may include. Make the implicit explicit to bridge the gap between human perception and formal statistics.

## When it applies

- When creating bivariate visualizations (scatter plots, line charts, etc.) that contain significant outliers.
- When the interpretation of a trend is a key takeaway for the viewer.
- When there is a potential discrepancy between what a statistical model shows and what a person might visually perceive.

## Exceptions

- When the goal is specifically to leverage the audience's robust estimation capabilities—for example, during informal data exploration where quick, outlier-filtered trend assessment is desired.
- In visualizations for expert statisticians who are fully aware of the difference between robust and non-robust models and are using the chart to make their own informed judgments.

## Trade-offs

- **Clarity vs. Complexity:** Annotating a chart with a specific trend line provides statistical clarity but adds visual complexity and "chart junk." It also forces a single model onto the viewer.
- **Flexibility vs. Specificity:** Omitting a trend line allows for perceptual flexibility (letting the viewer use their own robust judgment) but risks a discrepancy between their interpretation and your intended statistical conclusion.

## Signs of Trouble

- **Divergent Conclusions:** Your team's statistical model shows a strong trend influenced by outliers, but stakeholders looking at the raw chart say "I don't see it."
- **Outlier-Driven Story:** The key insight from your data is driven by a few extreme points, but this is not obvious from a simple visual inspection of the plot.
- **Ambiguous Task:** Viewers are asked to "find the trend" in a plot with outliers, but it's unclear whether they should include or exclude them in their mental model.

## How to Improve

- **Quick Fix: Highlight the Outliers.** If you don't want to draw a trend line, at least make the outliers visually distinct (e.g., with a different color or shape) and add a note explaining their context. This signals to the viewer that these points are special and should be considered deliberately.

- **Moderate Redesign: Draw the Intended Trend Line.** If the outlier-sensitive (e.g., OLS) trend is important to your story, explicitly draw that trend line on the chart. This removes ambiguity and directs the viewer to the specific statistical interpretation you want to communicate.

- **Comprehensive Approach: Show Both Trends.** For a more nuanced discussion, display both the robust trend (what people see) and the OLS trend (what a standard model shows). You can do this with two different lines, perhaps with text annotations explaining, "Trend including all data" and "Trend ignoring extreme values." This educates the viewer about the impact of outliers.
