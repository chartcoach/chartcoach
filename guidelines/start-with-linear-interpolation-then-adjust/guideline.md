---
id: start-with-linear-interpolation-then-adjust
title: Start with Linear Interpolation, Then Iterate
bibliography: references.bib
description: Begin map design with a linear interpolation as a baseline, then change
  interpolation if the distribution makes the map unreadable.
labels:
- chart:choropleth
- task:iterate
- visual:color
- impact:workflow
- data:quantitative
- audience:general
- complexity:beginner
- source:datawrapper-blog
---

## The Rule <!-- role: advice -->

Start with a linear interpolation as your baseline, then switch to another interpolation only if the distribution (and resulting map) demands it. [@muth_interpolation_2022]

## The Logic <!-- role: reason -->

Linear interpolation is the most intuitive first cut because it maps values proportionally from minimum to maximum; using it first gives you a truthful, easy-to-explain reference point to judge whether outliers are dominating the color range. [@muth_interpolation_2022]

- **The Principle:** Baseline-first iteration
- **The Evidence:** [@muth_interpolation_2022]

## Where to Apply <!-- role: context -->

- **User Goal:** Rapidly producing an interpretable first draft and diagnosing whether outliers are flattening the color variation
- **Data Type:** Any quantitative data mapped to a gradient (classed or unclassed)
- **Audience:** Teams or readers who benefit from simple, explainable defaults [@muth_interpolation_2022]

## When to Break It <!-- role: exceptions -->

- **Scenario:** You already know the data are heavily skewed with extreme outliers and you must show within-range variation prominently.
- **Reason:** A linear first draft can be predictably uninformative (most areas the same color), so you may move directly to a distribution-aware option. [@muth_interpolation_2022]

## The Price <!-- role: costs -->

- **The Sacrifice:** Extra iteration time if linear predictably fails.
- **The Risk:** Stakeholders may anchor on the first (linear) view and resist changing interpolation later. [@muth_interpolation_2022]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Treating the default linear interpolation as “correct” and never testing alternatives.
- **Why it fails:** With uneven distributions, linear can hide geographic patterns by placing most regions into the lightest range. [@muth_interpolation_2022]

## How to Check <!-- role: check -->

- **Visual Sign:** The first (linear) map uses only a small portion of the darker colors.
- **The Test:** Compare the map’s color usage to the histogram; if most values sit in a narrow low range, linear will over-allocate gradient to rare high values. [@muth_interpolation_2022]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch from linear to Natural (distribution-aware) or to a quantile-based option and compare side-by-side. [@muth_interpolation_2022]
- **Best Fix:** Keep the linear version as a reference, then select the interpolation that best matches the communication goal (outlier emphasis vs. pattern discovery). [@muth_interpolation_2022]
