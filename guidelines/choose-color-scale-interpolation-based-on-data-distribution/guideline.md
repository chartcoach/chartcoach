---
id: choose-color-scale-interpolation-based-on-data-distribution
title: Choose Interpolation Based on Data Distribution
bibliography: references.bib
description: Pick a color-scale interpolation that matches your data distribution
  to balance pattern visibility and truthful emphasis on outliers.
labels:
- chart:choropleth
- task:encode
- visual:color
- impact:clarity
- data:quantitative
- audience:general
- complexity:intermediate
- source:datawrapper-blog
---

## The Rule <!-- role: advice -->

Choose your color-scale interpolation by first inspecting the distribution of your data (e.g., via a histogram), then select an interpolation that fits that distribution instead of defaulting to linear. [@muth_interpolation_2022]

## The Logic <!-- role: reason -->

A single min→max linear mapping can collapse most values into a narrow, similar-looking color range when the data has strong outliers; distribution-aware interpolation re-allocates more of the color range to where values are dense, changing what patterns become visible. [@muth_interpolation_2022]

- **The Principle:** Distribution-aware color allocation
- **The Evidence:** [@muth_interpolation_2022]

## Where to Apply <!-- role: context -->

- **User Goal:** Seeing meaningful geographic (or spatial) patterns without being misled by a few extreme values
- **Data Type:** Quantitative values with potential skew and outliers (e.g., county-level rates)
- **Audience:** General readers who need an intuitive legend and interpretable differences [@muth_interpolation_2022]

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your main message is explicitly about extremes/outliers (e.g., “where are the worst values?”)
- **Reason:** A linear interpolation can be the most straightforward way to emphasize outliers and preserve a direct linear mapping from value to color. [@muth_interpolation_2022]

## The Price <!-- role: costs -->

- **The Sacrifice:** You may lose the simplicity and immediate intuitiveness of a pure min→max linear scale.
- **The Risk:** Distribution-aware interpolations can shift perceived severity by making more areas look “high” (darker) than a linear mapping would suggest. [@muth_interpolation_2022]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using linear interpolation on highly skewed data and then assuming the map “has no pattern.”
- **Why it fails:** Most regions end up in the lightest shades, hiding variation among typical values. [@muth_interpolation_2022]
- **The Wrong Fix:** Choosing the most contrast-heavy option just because it looks dramatic.
- **Why it fails:** It can imply stark differences where the data differences are small and compress differences among true outliers. [@muth_interpolation_2022]

## How to Check <!-- role: check -->

- **Visual Sign:** Most regions share nearly the same light color, with only a few very dark regions.
- **The Test:** Plot or review a histogram (or rug/strip plot) of the mapped values; if values cluster tightly with long-tail outliers, a linear interpolation will likely underuse much of the gradient. [@muth_interpolation_2022]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Try a distribution-aware interpolation (e.g., Natural breaks / Natural interpolation) after confirming skew/outliers in the histogram. [@muth_interpolation_2022]
- **Best Fix:** Align interpolation choice with the story goal: use linear to spotlight outliers, or use distribution-aware/quantile-style approaches to reveal regional variation among common values—then verify the legend and map still communicate the intended takeaway. [@muth_interpolation_2022]
