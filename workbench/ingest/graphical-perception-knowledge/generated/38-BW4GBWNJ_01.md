---
id: use-dot-plots-for-mean-estimation
title: "Use dot plots to help viewers accurately judge an average"

tags:
  - impact:perceptual
  - chart:dot
  - chart:strip-plot
  - task:summary-mean
  - data:quantitative
  - visual:position
  - audience:general
  - medium:static

evidence:
  strength: medium
  summary: "In a direct comparison, Godau et al. (2016, n=53) found that dot plots (point graphs) do not cause the systematic underestimation of the average value that is observed in bar charts. Viewers' judgments of the mean in dot plots were not significantly different from the true mean."

sources:
  - type: research
    ref: Godau et al., 2016
    url: https://doi.org/10.1016/j.chb.2016.01.036
    note: "Compared bar graphs to point graphs (dot plots) for a mean-estimation task. While bar graphs produced significant underestimation (p < .001), point graphs did not, showing they are a more perceptually accurate choice for this task."
    role: primary

examples:
  - type: good
    description: "A dot plot shows the individual ratings for a product from 50 different users. The viewer can easily and accurately perceive the overall average rating by visually centering the cluster of dots."
  - type: bad
    description: "The same 50 product ratings are shown in a bar chart with 50 bars. The viewer will likely perceive the average rating to be lower than it actually is, potentially forming an inaccurately negative impression of the product."
---

## Guidance

To help your audience accurately perceive the average of a set of values, use a dot plot (or strip plot) instead of a bar chart.

## Why

Dot plots encode data values using position, which is a perceptually "clean" visual channel for this task. Unlike bar charts, which use length and area, dot plots are not subject to the perceptual bias that causes viewers to systematically underestimate the average. Research shows that when viewers judge the average of values in a dot plot, their perception is accurate and unbiased.

### Core Principle

Encoding quantitative values with a minimal mark like a point (position) can lead to more accurate perceptual judgments than using a larger mark like a bar (length/area), especially for summary tasks like estimating an average.

## When it applies

- When you are displaying a series of quantitative values and the primary task for the viewer is to estimate or understand the overall average or central tendency.
- When you want to ensure your audience has an unbiased perception of the data's overall level.

## Exceptions

- If the data has a meaningful starting point of zero and the primary task is to compare the *magnitudes* of individual values (e.g., "how much bigger is A than B?"), a bar chart may be more conventional and effective. This guidance is specific to the task of judging the *average*.

## Trade-offs

- Dot plots are perceptually more accurate for judging an average, but they may feel less "substantial" or be slightly less familiar to some audiences than bar charts.
- Bar charts strongly emphasize comparison to a zero baseline, while dot plots emphasize the position of values along a scale. Choose based on which of these is more important for your message.

## Signs of Trouble

- **Misleading Impressions:** You have previously used a bar chart for this purpose and found that audience interpretations of the "overall level" were consistently lower than the actual data average.
- **Seeking Perceptual Accuracy:** You are working in a context where a precise, unbiased understanding of the average is critical (e.g., scientific communication, financial reporting, public policy).

## How to Improve

- **Minimal Change:** If you are currently using a bar chart in your software, switch the mark type from a "bar" to a "point," "dot," or "circle." This is often a one-click change that immediately improves perceptual accuracy for this task.

- **Moderate approach:** After converting to a dot plot, consider adding a faint reference line or a simple box plot-style element to explicitly visualize the mean and key parts of the distribution. This provides further visual support without re-introducing the bias of bars.