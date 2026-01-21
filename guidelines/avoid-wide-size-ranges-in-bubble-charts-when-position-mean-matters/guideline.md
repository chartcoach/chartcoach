---
id: avoid-wide-size-ranges-in-bubble-charts-when-position-mean-matters
title: Avoid Wide Size Ranges in Bubble Charts When Position Mean Matters
bibliography: references.bib
description: In high-correlation settings, wider size ranges produce more mean-position
  bias than narrower size ranges.
labels:
- chart:scatter
- task:aggregate
- visual:area
- visual:position
- impact:bias
- data:quantitative
- audience:general
- parameter:encoding-range
---

## The Rule <!-- role: advice -->

If you must use size/area in a scatterplot and users may judge the mean position, keep the size range narrow—especially when the third variable is correlated with position.

## The Logic <!-- role: reason -->

- **The Principle:** Larger differences in mark size amplify unequal perceptual weighting, which increases mean-position bias when size is spatially structured.
- **The Evidence:** In the extracted bias ranking for the aggregate task, the worst-performing designs include size/area with high correlation and wider ranges (E-15 and E-18), while the high-correlation narrow size condition (E-12) ranks less biased than those; this pattern is captured as collated knowledge in [@zengReviewCollationGraphical2023] from [@hongWeightedAverageIllusion2022].

## Where to Apply <!-- role: context -->

- **User Goal:** Mean (average) position estimation in scatterplots that also encode a third quantitative variable via size.
- **Data Type:** Trivariate quantitative scatterplots where size is correlated with position (medium/high).
- **Audience:** General audiences.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The primary purpose is to make size differences visually prominent (not to support mean estimation).
- **Reason:** The evidence is about bias/accuracy for aggregate mean judgments, not about achieving salience for size itself [@hongWeightedAverageIllusion2022; @zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** Narrowing the size range compresses perceived variation in the third variable.
- **The Risk:** Users may miss real variation in the third variable if size differences become too subtle.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Max out bubble sizes “so people can see them.”
- **Why it fails:** Wide size ranges in correlated settings are associated with larger bias ranks (worse) in the extracted results [@hongWeightedAverageIllusion2022; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** A few very large bubbles dominate attention and appear to define the “center.”
- **The Test:** Reduce the size range by half and see whether viewers’ mean estimates become less consistently pulled toward the large-bubble region.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce the min–max bubble size span (narrow the size range) without changing x/y.
- **Best Fix:** Remove size encoding entirely for the mean-judgment view and move the third variable to another view/encoding [@hongWeightedAverageIllusion2022; @zengReviewCollationGraphical2023].
