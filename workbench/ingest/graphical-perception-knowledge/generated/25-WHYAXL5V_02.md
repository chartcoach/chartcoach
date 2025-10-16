---
id: use-size-for-min-max-judgment
title: "Use Size to Encode Values for Accurate Min/Max Judgments"
tags:
  - impact:perceptual
  - task:find-extremum
  - task:compare
  - task:rank
  - data:quantitative
  - visual:size
  - chart:bubble
  - chart:glyphs
  - chart:scatter
  - medium:screen
  - medium:static
evidence:
  strength: medium
  summary: "In an experiment requiring participants (n=87) to find minimum and maximum values, Chung et al. (2016) found that encoding values with size resulted in significantly fewer errors than using value (lightness), texture, hue, orientation, or shape."
sources:
  - type: research
    ref: Chung et al., 2016
    url: https://doi.org/10.1111/cgf.12889
    note: "Experiment 2 directly tested the accuracy of finding min/max values. Size encoding had a mean error rate of ~5%, compared to ~17-22% for value/texture and over 40% for hue/orientation, making it the most accurate visual channel tested."
    role: primary
examples:
  - type: bad
    description: "In this chart, a quantitative value (e.g., population) is encoded using color hue. It is extremely difficult to accurately determine which country has the highest or lowest population just by looking at the colors."
  - type: good
    description: "In a bubble chart, the same quantitative value is encoded by the area of the circles. It is much easier and more accurate to identify the largest and smallest circles, and thus the extreme values in the data."
---

## Guidance

When the primary task is for a viewer to find the minimum or maximum value in a dataset, use **size** (e.g., the area of a circle, the height of a bar) to encode the quantitative values.

## Why

Among common visual channels (excluding position), `size` is the most accurately judged for quantitative tasks. Viewers can make more precise magnitude comparisons and identify extreme values with fewer errors when data is encoded by size compared to color, texture, or shape. This is because size is a quantitative channel, meaning our visual system can estimate numerical ratios between different sizes.

## When it applies

This is most relevant when a key goal of the visualization is to draw attention to outliers, find the highest/lowest performers, or make general magnitude comparisons. This often occurs in:
- Bubble charts
- Scatterplots where a third variable is encoded by size
- Maps with sized glyphs (proportional symbol maps)

## Exceptions

- **Dense Plots:** In visualizations with many data points, large marks can overlap and hide smaller ones (occlusion), making it impossible to see all the data and find the true minimum. In this case, `value` (lightness) or reducing opacity might be a better, though less accurate, alternative.
- **Position is Available:** If you can use `position` on a common scale (e.g., a bar chart), it will be even more accurate than `size`. This guideline applies when `position` is already used for other data dimensions (like in a scatterplot or map).

## Trade-offs

- **Occlusion:** The main drawback is that larger marks can obscure smaller ones in crowded plots.
- **Slower than Value:** While more accurate, judging `size` can be slightly slower than judging `value` (lightness).
- **Scaling Issues:** Incorrectly scaling marks by `radius` instead of `area` can lead to perceptual distortions where differences are exaggerated.

## Signs of Trouble

- **High Error Rate:** Users frequently fail to identify the largest or smallest mark in a set.
- **Occlusion:** In dense plots, you can see large marks completely hiding smaller marks, meaning some data is invisible.
- **Ambiguous Legends:** The legend doesn't make it clear if `area` or `radius` is being used to scale the marks.

## How to Improve

- **Quick Fix:** Ensure you are scaling the **area** of the mark, not its radius or diameter, directly to the data value. This provides a more perceptually accurate representation.
- **Moderate Redesign:** If occlusion is a problem, apply a semi-transparent fill to all marks. This allows marks below to be seen, mitigating the occlusion issue.
- **Comprehensive Redesign:** If finding extremes with perfect accuracy is critical and occlusion is unavoidable, change the chart type to one that uses `position` on a common scale. For example, instead of a bubble chart, use a bar chart or a dot plot sorted by value.