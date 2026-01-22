---
id: prefer-power-transformation-over-log-transform-when-fitting-individual-level-correlation-jnd-models
title: Use a power transformation for individual-level JND models when log-linear
  residuals remain skewed
bibliography: references.bib
description: Power-transformed JND models improve fit and residual behavior over log-linear
  models for correlation discrimination data.
labels:
- chart:scatter
- task:model
- visual:none
- impact:validity
- data:quantitative
- audience:expert
- complexity:advanced
---

## Prefer a power transformation when modeling individual-level JNDs <!-- role: advice -->

When fitting individual-level Just-Noticeable Difference (JND) models for scatterplot correlation discrimination and log-linear models leave non-normal or skewed residuals, fit a power-transformed JND model instead.

## Power transformations better match the distributional structure of JND data <!-- role: reason -->

Individual-level JND observations can violate linear-model assumptions; a power transformation provides flexibility beyond a log transform and can better normalize residuals while improving model fit.

**Mechanism:** Adjusting the exponent in a power transform can reduce skewness and kurtosis in residuals and yield a model that better captures individual variability in discrimination thresholds.

**Evidence:** A power transformation model (using a Box-Cox t distribution framework) improved fit metrics (including information criterion) and produced more normal-like residuals compared to a log-linear model with random intercepts for individual observations [@yangCorrelationJudgmentVisualization2019a]. The resulting power-transformed model could still be reproduced via substitution using a top visual feature, preserving the interpretability link to perceptual proxies [@yangCorrelationJudgmentVisualization2019a].

**Notes:** Improvements were reported as incremental but consistent across multiple diagnostics, addressing remaining skewness seen under log transformation [@yangCorrelationJudgmentVisualization2019a].

## When this applies: individual-observation modeling of discrimination thresholds <!-- role: context -->

- **User Goal:** Build a perceptual model of correlation discrimination that generalizes across participants.
- **Task:** Regression modeling on individual JND observations with participant-level effects.
- **Data:** Individual participant JNDs across correlation levels and approaches; enough observations to assess residual diagnostics.
- **Chart Setting:** Scatterplot correlation discrimination experiments (forced-choice).
- **Audience:** Researchers building or validating perceptual models.
- **Success Criterion:** Improved model fit and residual diagnostics without losing interpretability.

## When not to follow it: aggregated mean-only modeling goals <!-- role: exceptions -->

**Break it when:** You only need a population-level model on aggregated mean observations and are not modeling individual variance. **Why:** The power transformation was motivated by improving individual-level fit and residual behavior beyond linear/log-linear forms [@yangCorrelationJudgmentVisualization2019a].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Power-transformed models are harder to interpret directly in the original JND scale. **Risk:** Overfitting can occur if the added flexibility is not justified by diagnostics. **Mitigation:** Select the exponent using explicit fit and diagnostic criteria rather than convenience [@yangCorrelationJudgmentVisualization2019a].

## Common failure modes <!-- role: mistakes -->

**Mistake:** Applying a log transform and assuming residual problems are solved without checking diagnostics. **Why it fails:** Log-linear models can still leave skewness and non-normality in residuals for correlation JND data [@yangCorrelationJudgmentVisualization2019a].

## Quick tests <!-- role: check -->

**Failure Sign:** Residual diagnostics indicate non-normality or strong skew after fitting a log-linear model. **Quick Check:** Run a normality test and inspect a detrended Q-Q plot for systematic deviation. **Stronger Test:** Compare information criteria and residual skewness/kurtosis between log-linear and power-transformed models with the same random-effects structure [@yangCorrelationJudgmentVisualization2019a].

## What to do instead if power modeling is impractical <!-- role: fix -->

- Use an individual-observation model with random intercepts to account for participant-specific baselines.
- Evaluate multiple transformations explicitly and select based on fit and residual diagnostics rather than defaulting to log.
- If transformation choice is unclear, report both log-linear and power-transformed results and compare diagnostics transparently [@yangCorrelationJudgmentVisualization2019a].
