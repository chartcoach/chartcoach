---
id: model-correlation-discrimination-with-visual-feature-jnds-not-only-correlation-jnds
title: Model scatterplot correlation discrimination using JNDs of visual features,
  not only JNDs of correlation
bibliography: references.bib
description: Just-noticeable differences computed on key visual features can reproduce
  established correlation-perception models.
labels:
- chart:scatter
- task:evaluate
- visual:shape
- impact:validity
- data:quantitative
- audience:expert
- complexity:advanced
---

## Use visual-feature JNDs as the modeled stimulus for correlation discrimination <!-- role: advice -->

When evaluating or predicting correlation discrimination performance in scatterplots, compute Just-Noticeable Differences (JNDs) on candidate visual features and use them as the modeled stimulus in place of correlation.

## Visual-feature substitution reproduces correlation-perception models <!-- role: reason -->

Established correlation-perception models fit well partly because viewers respond to low-level visual proxies; if those proxies are modeled directly, the resulting perceptual model can match the original correlation-based form.

**Mechanism:** If viewers compare plots by detecting changes in a few perceptual features, then the psychophysical threshold should apply to feature magnitude, and correlation-based models can be derived through substitution between correlation and feature magnitude.

**Evidence:** A small set of visual features predicted forced-choice judgments better than correlation difference, and those features could be substituted into linear and log-linear correlation-perception models to reproduce the original correlation model parameters closely [@yangCorrelationJudgmentVisualization2019a]. The analysis pipeline explicitly modeled JND(feature), related feature magnitude to correlation, and derived an equivalent JND(correlation) model via substitution [@yangCorrelationJudgmentVisualization2019a].

**Notes:** The strongest example feature used in substitution was the standard deviation of perpendicular distances to the regression line, but similar results held for other top features in supplemental analyses [@yangCorrelationJudgmentVisualization2019a].

## When this applies: evaluation and modeling workflows <!-- role: context -->

- **User Goal:** Predict or compare how well a scatterplot design supports correlation discrimination.
- **Task:** Build a perceptual model, compare models, or choose a design based on predicted discriminability.
- **Data:** Experimental judgments or logs from forced-choice correlation comparisons; computed feature values per plot.
- **Chart Setting:** Any scatterplot variant where feature extraction is feasible from rendered points.
- **Audience:** Visualization researchers and practitioners doing model-based evaluation.
- **Success Criterion:** Models that fit judgments well and remain interpretable in perceptual terms.

## When not to follow it: no access to point geometry or stable feature computation <!-- role: exceptions -->

**Break it when:** You cannot reliably compute the feature from the displayed marks (e.g., the mark set is unavailable or heavily transformed). **Why:** The method depends on mapping each stimulus to a computed feature magnitude and its JND [@yangCorrelationJudgmentVisualization2019a].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Computing many candidate features increases implementation and analysis complexity. **Risk:** Feature collinearity can distort regression-based inference if not handled carefully. **Mitigation:** Remove trivially dependent features and avoid multi-feature models that reintroduce collinearity without explicit handling [@yangCorrelationJudgmentVisualization2019a].

## Common failure modes <!-- role: mistakes -->

**Mistake:** Fitting many correlated features together without addressing collinearity. **Why it fails:** Collinearity can significantly affect regression outcomes and interpretation, requiring feature filtering or separate modeling [@yangCorrelationJudgmentVisualization2019a].

## Quick tests <!-- role: check -->

**Failure Sign:** Model coefficients are unstable or flip signs when adding/removing features. **Quick Check:** Compute pairwise linear dependence among candidate features and remove linearly dependent ones before modeling. **Stronger Test:** Compare non-nested models (feature-based vs. correlation-based) using a model-comparison test and information criteria to confirm the feature model is competitive [@yangCorrelationJudgmentVisualization2019a].

## What to do instead when feature modeling becomes unstable <!-- role: fix -->

- Fit separate single-feature models to avoid collinearity-driven artifacts when screening candidate features.
- Remove linearly dependent features that can be trivially derived from one another before regression.
- Use a model-comparison workflow (odds ratios, information criterion, non-nested comparison) to select a small set of high-performing features [@yangCorrelationJudgmentVisualization2019a].
