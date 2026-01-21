---
id: use-power-transformation-for-individual-level-correlation-jnd-models
title: Prefer Power-Transformed JND Models for Correlation Discrimination
bibliography: references.bib
description: Use power transformation (rather than only log transformation) to better
  model individual-level JND data for correlation judgments.
labels:
- chart:scatter
- task:model
- visual:position
- impact:predictability
- data:bivariate
- audience:expert
- complexity:advanced
- source:yang-correlation-features
---

## The Rule <!-- role: advice -->

When fitting individual-level discrimination-threshold (JND) models for correlation judgments, use a **power transformation** of JNDs to improve model fit and residual behavior.

## The Logic <!-- role: reason -->

The paper tested linear, log-linear, and power-transformed models (with random intercepts) on individual observations; the power transformation improved fit metrics (e.g., AIC) and produced more normal-like residuals compared to the log-linear model, while still allowing substitution of visual-feature proxies to reproduce correlation models [@yangCorrelationJudgmentVisualization2019a].

- **The Principle:** Flexible psychophysical scaling (power laws) can better capture perception than fixed log transforms.
- **The Evidence:** Power transformation improved AIC and residual diagnostics relative to log-linear models in their individual-observation modeling [@yangCorrelationJudgmentVisualization2019a].

## Where to Apply <!-- role: context -->

- **User Goal:** Build predictive perceptual models of correlation discrimination; compare design alternatives quantitatively.
- **Data Type:** Individual-level JND observations from discrimination experiments (e.g., staircase procedures).
- **Audience:** Visualization researchers and practitioners building perceptual performance models [@yangCorrelationJudgmentVisualization2019a].

## When to Break It <!-- role: exceptions -->

- **Scenario:** You only have aggregated mean observations with very small n (e.g., 12 points).
- **Reason:** The paper notes diagnostics are less meaningful with small sample sizes; benefits of the power approach were shown primarily with individual observations and residual diagnostics [@yangCorrelationJudgmentVisualization2019a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Added modeling complexity (choosing/estimating the power exponent; more parameters).
- **The Risk:** A more flexible model can be harder to interpret or compare across studies if not reported clearly [@yangCorrelationJudgmentVisualization2019a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming a log transform is always sufficient once linear-model residuals are skewed.
- **Why it fails:** The paper found remaining non-normality/skewness under log-linear models, while power transformation improved diagnostics [@yangCorrelationJudgmentVisualization2019a].

## How to Check <!-- role: check -->

- **Visual Sign:** Detrended Q-Q plots show systematic curvature or residual skew after log transformation.
- **The Test:** Fit log-linear and power-transformed models and compare AIC and residual normality/homoscedasticity tests; prefer the power model when it improves these diagnostics [@yangCorrelationJudgmentVisualization2019a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Try a power transform on JNDs and refit the same fixed/random effects structure.
- **Best Fix:** Use a power-transformation framework (as implemented in their approach) and report fit + residual diagnostics to justify the chosen exponent and model form [@yangCorrelationJudgmentVisualization2019a].
