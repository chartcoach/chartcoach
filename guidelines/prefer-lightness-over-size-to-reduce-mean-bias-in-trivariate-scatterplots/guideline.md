---
id: prefer-lightness-over-size-to-reduce-mean-bias-in-trivariate-scatterplots
title: Prefer Lightness Over Size to Reduce Mean-Position Bias
bibliography: references.bib
description: When adding a third quantitative dimension to a scatterplot, lightness/saturation
  generally yields lower mean-position bias than size/area.
labels:
- chart:scatter
- task:aggregate
- visual:color
- visual:area
- visual:position
- impact:bias
- data:quantitative
- audience:general
- risk:weighted-average-illusion
---

## The Rule <!-- role: advice -->

If you must encode a third quantitative variable in a scatterplot where users may judge the mean position, use a color-saturation/lightness scale rather than size/area.

## The Logic <!-- role: reason -->

- **The Principle:** Size differences create stronger perceptual weighting than lightness differences, increasing bias in ensemble mean judgments.
- **The Evidence:** In the extracted aggregate-task bias rankings, lightness/saturation designs (E-1–E-9) tend to rank with lower bias than size/area designs (E-10–E-18), with broad significant differences reported between multiple lightness designs and multiple area designs; this is part of the structured graphical-perception knowledge summarized for recommendation systems in [@zengReviewCollationGraphical2023] from [@hongWeightedAverageIllusion2022].

## Where to Apply <!-- role: context -->

- **User Goal:** Estimating the mean x/y position (aggregate) while still seeing a third quantitative attribute.
- **Data Type:** Trivariate quantitative scatterplots.
- **Audience:** General audiences (crowdsourced setting in the study).

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your primary goal is not mean-position judgment.
- **Reason:** The provided evidence is scoped to aggregate mean-position performance, not other scatterplot tasks [@hongWeightedAverageIllusion2022; @zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** Color-saturation/lightness may be less “attention grabbing” than size and may make the third variable less visually prominent.
- **The Risk:** If the third variable must be read precisely, this guideline does not guarantee better value-reading performance (not evaluated in the provided extracted task scope).

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Encode the third variable with both size and lightness “to be safe.”
- **Why it fails:** The evidence distinguishes size/area as a key driver of higher bias; adding it back can reintroduce the weighted-average illusion mechanisms the study measures [@hongWeightedAverageIllusion2022; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** The perceived “average” drifts toward the largest marks more than toward the darkest marks.
- **The Test:** Swap the third-variable encoding between size and saturation/lightness while keeping x/y identical and check whether the perceived mean shifts less in the color condition.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace size/area encoding with a color-saturation/lightness scale while keeping point size constant.
- **Best Fix:** If mean judgments are critical, eliminate the third encoding from the scatterplot and provide it in a separate view (and keep the main scatterplot uniform-mark) [@hongWeightedAverageIllusion2022; @zengReviewCollationGraphical2023].
