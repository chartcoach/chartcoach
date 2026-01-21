---
id: avoid-high-correlation-between-size-and-position-in-bubble-charts-for-mean-judgments
title: Avoid High Correlation Between Size and Position in Bubble Charts for Mean
  Judgments
bibliography: references.bib
description: Bias in perceived mean position increases as correlation between the
  third (size/lightness) variable and position increases.
labels:
- chart:scatter
- task:aggregate
- visual:position
- visual:area
- visual:color
- impact:bias
- data:quantitative
- audience:general
- data-characteristic:correlation
---

## The Rule <!-- role: advice -->

When users need to judge mean position, avoid mapping a third variable (especially size/area) that is strongly correlated with x/y position.

## The Logic <!-- role: reason -->

- **The Principle:** When the third encoding forms a spatial gradient aligned with position, perceptual weighting concentrates in one region and pulls the perceived mean toward the region with increasing size/darkness.
- **The Evidence:** In the extracted bias rankings, higher-correlation conditions are systematically worse: e.g., for lightness/saturation the high-correlation designs (E-3, E-6, E-9) rank more biased than lower-correlation counterparts, and for size/area the high-correlation designs (E-12, E-15, E-18) appear at the bottom of the bias ranking; the review paper positions this as actionable knowledge for recommendation systems [@zengReviewCollationGraphical2023] based on [@hongWeightedAverageIllusion2022].

## Where to Apply <!-- role: context -->

- **User Goal:** Judging or comparing average x/y values from a scatterplot (aggregate mean position).
- **Data Type:** Quantitative x/y where the third quantitative variable is (or may be) correlated with x/y.
- **Audience:** General audiences.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are intentionally trying to visually emphasize the region where the third variable is large/dark (rather than support accurate mean judgments).
- **Reason:** This guideline is about protecting mean-position judgments; it does not claim that emphasizing correlated structure is always undesirable [@hongWeightedAverageIllusion2022; @zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may lose a compact way to show that the third variable co-varies with x/y.
- **The Risk:** Alternative designs may require separate panels or interaction to show correlation structure.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** “The data is correlated, so a bubble chart will make that even clearer.”
- **Why it fails:** The evidence shows correlation between the third encoding and position increases directional bias in mean estimates, especially for size/area [@hongWeightedAverageIllusion2022; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Bubbles (or darker points) cluster along a diagonal gradient and the “average” seems to lie closer to the heavy cluster than expected.
- **The Test:** Compute the true mean x/y and compare it to a quick human estimate from multiple reviewers; consistent drift toward the gradient direction indicates risk.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Remove size encoding (constant size) and keep only x/y position.
- **Best Fix:** Split the third variable into a separate view (or otherwise decouple the third encoding from the mean-judgment view) when the third variable is highly correlated with position [@hongWeightedAverageIllusion2022; @zengReviewCollationGraphical2023].
