---
id: use-linear-or-rounded-steps-for-even-distributions-or-to-highlight-outliers
title: Use Linear or Rounded Steps for Even Data or Outlier Emphasis
bibliography: references.bib
description: Prefer linear (or rounded) class breaks when values are fairly evenly
  distributed or when you want outliers to stand out strongly.
labels:
- chart:choropleth
- task:highlight
- visual:color
- impact:truthfulness
- data:quantitative
- audience:general
- complexity:beginner
- source:datawrapper-blog
---

## The Rule <!-- role: advice -->

Use linear (equi-distant) class breaks—or rounded linear breaks—when your data distribution is fairly even, or when your intent is to spotlight extreme outliers. [@muth_interpolation_2022]

## The Logic <!-- role: reason -->

Equal-width steps allocate the same value range to each color; this preserves a straightforward relationship between numeric differences and color differences and naturally pushes rare extremes into the darkest bins, making them pop. [@muth_interpolation_2022]

- **The Principle:** Equal-width binning emphasizes extremes
- **The Evidence:** [@muth_interpolation_2022]

## Where to Apply <!-- role: context -->

- **User Goal:** Truthfully showing magnitude on a linear value scale; calling attention to unusually high/low regions
- **Data Type:** Quantitative data without strong skew/outliers (or where outliers are the story)
- **Audience:** General readers who benefit from intuitive, simple breaks (especially rounded ones) [@muth_interpolation_2022]

## When to Break It <!-- role: exceptions -->

- **Scenario:** Most values cluster tightly with a long tail of outliers, and you need to reveal patterns among the clustered “typical” values.
- **Reason:** Equal-width steps can place most regions into the lightest class, obscuring variation and patterns. [@muth_interpolation_2022]

## The Price <!-- role: costs -->

- **The Sacrifice:** Reduced pattern visibility among common values when outliers stretch the scale.
- **The Risk:** The map can look “flat” (many regions same color), leading readers to miss meaningful regional differences. [@muth_interpolation_2022]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping equal-width breaks even after noticing that most regions fall into the first class.
- **Why it fails:** The first bin can absorb a majority of regions, underusing mid/dark colors. [@muth_interpolation_2022]
- **The Wrong Fix:** Using rounded breaks without checking whether rounding worsens bin imbalance.
- **Why it fails:** Readability improves, but distribution problems remain if the data are skewed. [@muth_interpolation_2022]

## How to Check <!-- role: check -->

- **Visual Sign:** One class (usually the lightest) dominates the map.
- **The Test:** Count (or estimate) how many regions land in each class; if a large majority occupy one class, linear/rounded breaks are likely a poor fit unless outlier emphasis is intended. [@muth_interpolation_2022]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch to quantiles or natural breaks to redistribute colors across regions. [@muth_interpolation_2022]
- **Best Fix:** Decide whether you’re optimizing for outlier spotlighting (keep linear/rounded) or for pattern discovery (move to Natural/quantile-based). [@muth_interpolation_2022]
