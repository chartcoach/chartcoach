---
id: expect-increasing-mean-bias-with-higher-correlation-in-trivariate-scatterplots
title: Treat higher correlation between a third-channel encoding and position as a
  bias risk for mean-position judgments in scatterplots
bibliography: references.bib
description: As correlation between a third encoded variable and position increases,
  mean-position estimates become more biased toward visually emphasized marks.
labels:
- chart:scatter
- task:aggregate
- visual:color
- visual:area
- impact:bias
- data:quantitative
- audience:general
- data-characteristic:correlation
---

## Correlation increases mean-position bias in trivariate scatterplots <!-- role: advice -->

Assume that increasing correlation between a third encoded quantitative variable (mapped to lightness or area) and x/y position will increase mean-position bias in scatterplots. Avoid designing mean-position judgments that depend on such correlated third-channel encodings.

## Correlated third-channel structure pulls perceived means <!-- role: reason -->

Correlation aligns visually emphasized marks along spatial gradients, increasing directional pull in ensemble judgments and shifting the perceived mean toward regions with higher encoded values.

**Mechanism:** When the third channel is correlated with x/y, marks with stronger visual weight become spatially clustered, so ensemble averaging is displaced toward those clusters.

**Evidence:** In bias rankings for the aggregate task, higher-correlation conditions appear later (worse) than lower-correlation conditions within both lightness-encoded (E-1/4/7 vs E-3/6/9) and area-encoded (E-10/13/16 vs E-12/15/18) design sets, indicating increased bias as correlation increases. [@hongWeightedAverageIllusion2022; @zengReviewCollationGraphical2023]

**Notes:** This guideline is about the relationship between correlation and bias direction/magnitude, not about which channel is best overall.

## Applies when a third encoding is spatially correlated with x/y and mean matters <!-- role: context -->

- **User Goal:** Make an above/below-average decision using the mean as a reference.
- **Task:** Aggregate (mean position estimation).
- **Data:** Quantitative x/y plus a third quantitative variable; the third variable is correlated with x/y position.
- **Chart Setting:** Trivariate scatterplot with point marks using either lightness (color saturation) or area (bubble size).
- **Audience:** General audiences.
- **Success Criterion:** Reduced systematic bias in perceived mean position.

## When not to use this rule <!-- role: exceptions -->

**Break it when:** The audience is not asked to estimate or use the mean position as part of their interpretation. **Why:** The evidence is specific to mean-position estimation bias.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may limit the ability to show meaningful joint structure between the third variable and position in a single view. **Risk:** Suppressing correlated encodings can hide patterns users might want to see. **Mitigation:** Provide alternative summaries that communicate the relationship without requiring perceptual mean estimation.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Adding a third encoding that is strongly correlated with position and then asking viewers to “eyeball the average.” **Why it fails:** Higher correlation aligns with more biased mean estimates in the reported rankings.

## Quick tests <!-- role: check -->

**Failure Sign:** The perceived mean moves in the direction of the third-variable gradient as correlation increases. **Quick Check:** Generate low- vs high-correlation variants and see if the mean estimate drifts systematically. **Stronger Test:** Collect click-the-mean responses across correlation levels and compare directional bias.

## What to do instead <!-- role: fix -->

- Avoid mean-position estimation tasks on trivariate scatterplots when the third variable is strongly correlated with x/y.
- Provide an explicit computed mean marker for x/y so the viewer does not infer it from the plotted marks.
- Separate the third variable into another view when mean-position judgments are required in the x/y view.
- Use a design where the third variable does not change point salience in ways that alter mean judgments.
