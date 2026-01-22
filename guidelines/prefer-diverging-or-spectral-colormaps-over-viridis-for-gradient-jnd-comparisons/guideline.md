---
id: prefer-diverging-or-spectral-colormaps-over-viridis-for-gradient-jnd-comparisons
title: Prefer diverging or spectral colormaps over viridis for JND-based gradient
  comparison tasks
bibliography: references.bib
description: When people compare average gradient between two color-coded scalar fields,
  diverging (cool-warm) and spectral (rainbow) schemes yield lower JND thresholds
  than viridis.
labels:
- chart:heatmap
- task:compare
- visual:color
- impact:accuracy
- data:quantitative
- audience:general
- metric:jnd
- domain:scalar-field
---

## Prefer diverging or spectral colormaps over viridis for gradient discrimination <!-- role: advice -->

Use a diverging cool-warm or spectral rainbow colormap instead of viridis when the task is to discriminate which of two color-coded scalar fields has a higher average gradient.

## Lower JND improves sensitivity to gradient differences <!-- role: reason -->

Lower just-noticeable difference (JND) thresholds mean viewers can reliably detect smaller differences between two stimuli, increasing sensitivity in forced-choice comparisons of gradient magnitude.

**Mechanism:** Lower JND reduces the minimum gradient difference required for reliable discrimination between two fields.

**Evidence:** In an aggregate task comparing average gradient between two scalar fields, cool-warm and rainbow produced lower JND thresholds than viridis, and both differences were statistically significant (cool-warm > viridis; rainbow > viridis) [@redaEvaluatingGradientPerception2019; @zengReviewCollationGraphical2023].

**Notes:** No significant difference was observed between cool-warm and rainbow for JND in this task [@redaEvaluatingGradientPerception2019; @zengReviewCollationGraphical2023].

## Context for gradient-comparison map judgments <!-- role: context -->

- **User Goal:** Decide which of two scalar fields varies more rapidly on average (higher average gradient).
- **Task:** Aggregate (summary) comparison using JND as the sensitivity criterion.
- **Data:** 2D quantitative scalar field values encoded as color on a regular grid.
- **Chart Setting:** Static, side-by-side comparison of two color-coded fields using the same colormap.
- **Audience:** Any audience performing perceptual comparison (including non-experts).
- **Success Criterion:** Lower JND (better sensitivity) in discriminating gradient differences.

## Exceptions for this evidence scope <!-- role: exceptions -->

**Break it when:** You are not doing a side-by-side aggregate comparison of average gradient between two scalar fields using a JND/sensitivity criterion. **Why:** The evidence only covers this specific task and metric, so it does not justify choices for other tasks or objectives [@redaEvaluatingGradientPerception2019; @zengReviewCollationGraphical2023].

## Costs of prioritizing lower JND in this task <!-- role: costs -->

**Sacrifice:** You may reduce alignment with goals not measured here (such as other accuracy notions or preference).\
**Risk:** Overgeneralizing this colormap choice to other tasks can lead to unsupported design decisions.\
**Mitigation:** Treat the choice as task- and metric-specific to gradient discrimination sensitivity.

## Mistakes that misuse the finding <!-- role: mistakes -->

**Mistake:** Applying “cool-warm or rainbow is best” as a general rule for all scalar-field tasks. **Why it fails:** The evidence only ranks these schemes above viridis for JND in an aggregate gradient comparison task, not for other tasks or metrics [@redaEvaluatingGradientPerception2019; @zengReviewCollationGraphical2023].

## Check that the guideline fits your use case <!-- role: check -->

**Failure Sign:** Viewers struggle to tell which field is steeper unless the difference is made large.\
**Quick Check:** If your core question is “which field has higher average gradient?” and you plan a forced-choice comparison, treat JND sensitivity as the success metric.\
**Stronger Test:** Run a small forced-choice pilot with your intended stimuli and compare observed discrimination thresholds across candidate colormaps.

## Fixes if you must keep viridis <!-- role: fix -->

- Increase the gradient difference between the two fields so the comparison is less reliant on small JND thresholds.
- Add a non-color cue that makes the comparison less dependent on color-based discrimination (e.g., an additional derived field view focused on gradients).
- Change the task framing so users do not need to discriminate subtle differences in average gradient.
- Use cool-warm or rainbow for the comparison view while keeping viridis for other views where this specific sensitivity advantage is not required.
