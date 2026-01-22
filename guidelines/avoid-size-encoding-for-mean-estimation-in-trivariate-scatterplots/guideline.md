---
id: avoid-size-encoding-for-mean-estimation-in-trivariate-scatterplots
title: Avoid encoding a third quantitative variable with point area when viewers must
  estimate the mean position in a scatterplot
bibliography: references.bib
description: Bubble-style (area-encoded) trivariate scatterplots introduce larger
  mean-estimation errors than lightness-encoded alternatives.
labels:
- chart:scatter
- task:aggregate
- visual:area
- impact:accuracy
- data:quantitative
- audience:general
- encoding:trivariate
---

## Mean-position task: avoid bubble-style (area) encodings <!-- role: advice -->

Avoid encoding a third quantitative variable with point area in scatterplots when viewers need to estimate the average (mean) x/y position. Prefer a lightness-based encoding when you must add a third quantitative variable to the same scatterplot.

## Mean-estimation error increases with area-encoded points <!-- role: reason -->

Using area (bubble) encodings changes the perceptual salience of marks, causing mean-position judgments to be pulled by visually stronger marks and increasing overall mean-estimation error relative to lightness-based encodings.

**Mechanism:** Visual emphasis from larger marks alters how viewers implicitly weight points when judging an overall average position, producing larger deviations from the true mean.

**Evidence:** In an aggregate (mean-position) task, designs using point area for the third quantitative variable (E-10 to E-18) ranked consistently worse on accuracy than corresponding designs using color saturation/lightness (E-1 to E-9), with many significant pairwise differences reported via bootstrapping. [@hongWeightedAverageIllusion2022; @zengReviewCollationGraphical2023]

**Notes:** This guideline is about mean-position estimation (a summary/aggregate judgment), not about reading individual point values.

## Applies to mean (average) position judgments in trivariate scatterplots <!-- role: context -->

- **User Goal:** Judge whether values are above/below “average” or locate the average point location in a 2D field.
- **Task:** Aggregate (mean position estimation).
- **Data:** Two quantitative variables mapped to x/y position plus a third quantitative variable mapped to a visual channel.
- **Chart Setting:** Static scatterplot with point marks; bubble chart variant is available.
- **Audience:** General audiences, including viewers with limited statistical training.
- **Success Criterion:** Lower mean-estimation error (more accurate mean location judgments).

## When not to use this rule <!-- role: exceptions -->

**Break it when:** The visualization does not require viewers to estimate or rely on the mean position (e.g., the goal is not an aggregate/mean judgment). **Why:** The evidence only covers an aggregate mean-position task and does not establish harms for other tasks.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You lose the ability to represent the third quantitative variable with size-based emphasis in the same view. **Risk:** Viewers may have a harder time comparing the third variable if they strongly expect size encodings. **Mitigation:** Consider separating tasks (e.g., provide a different view for the third variable) so the mean-position judgment is not confounded.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using bubble charts for mean-position judgments because “more encodings in one chart is more informative.” **Why it fails:** Area-encoded designs show worse mean-estimation accuracy rankings than lightness-encoded alternatives under the tested aggregate task.

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers’ indicated “average” point location appears systematically displaced toward regions with larger points. **Quick Check:** Compare a lightness-encoded version to an area-encoded version and see if the perceived mean shifts more with the bubble version. **Stronger Test:** Run a small click-the-mean pilot and compare mean error between area vs lightness encodings.

## What to do instead <!-- role: fix -->

- Use a lightness-based encoding (color saturation/lightness) for the third quantitative variable when mean-position estimation is required.
- Remove the third encoding channel for the mean-position task and show only x/y position.
- Split the third variable into a separate view rather than layering it into the same scatterplot used for mean estimation.
- Add an explicit mean marker computed from the data so the task does not depend on perceptual averaging.
