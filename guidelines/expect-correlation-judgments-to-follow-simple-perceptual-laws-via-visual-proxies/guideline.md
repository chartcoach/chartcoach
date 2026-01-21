---
id: expect-correlation-judgments-to-follow-simple-perceptual-laws-via-visual-proxies
title: Model Correlation Discrimination Using Visual-Feature Proxies
bibliography: references.bib
description: Treat correlation discrimination as driven by a small set of visual features,
  not direct perception of correlation.
labels:
- chart:scatter
- task:model
- visual:shape
- impact:predictability
- data:bivariate
- audience:expert
- complexity:advanced
- source:yang-correlation-features
---

## The Rule <!-- role: advice -->

When predicting or evaluating users’ correlation discrimination performance, model the task using a small set of **visual-feature proxies** (e.g., dispersion-to-line and ellipse measures), not correlation alone.

## The Logic <!-- role: reason -->

The study extracted 49 candidate features and found that a small subset (notably dispersion-to-line and ellipse-derived features) aligned with participant judgments better than correlation-based predictors; further, substituting these features into existing JND-based models reproduced prior correlation models without loss of precision [@yangCorrelationJudgmentVisualization2019a].

- **The Principle:** People use heuristic visual features as proxies for abstract statistics.
- **The Evidence:** Feature-based models matched or exceeded correlation-based models and could algebraically reproduce the original correlation JND models via substitution [@yangCorrelationJudgmentVisualization2019a].

## Where to Apply <!-- role: context -->

- **User Goal:** Predict where users will confuse correlation strengths; compare visualization designs for correlation tasks.
- **Data Type:** Scatterplots (and potentially other bivariate encodings) evaluated via discrimination (which is “more correlated?”).
- **Audience:** Visualization researchers, evaluators, and designers building quantitative evaluation pipelines [@yangCorrelationJudgmentVisualization2019a].

## When to Break It <!-- role: exceptions -->

- **Scenario:** Tasks require explicit numeric estimation of correlation (not discrimination) or require reasoning beyond visual heuristics.
- **Reason:** The paper’s evidence is grounded in discrimination experiments (pairwise “which is more correlated?”) and JND modeling, not direct numeric estimation tasks [@yangCorrelationJudgmentVisualization2019a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional computation/engineering to extract features from plots or underlying data.
- **The Risk:** Overfitting to the tested feature set; features may be incomplete for new plot styles or tasks [@yangCorrelationJudgmentVisualization2019a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Evaluating “correlation readability” solely by mapping between perceived correlation and Pearson r.
- **Why it fails:** The paper demonstrates that participants’ judgments are more directly explained by a few visual features than by r itself [@yangCorrelationJudgmentVisualization2019a].

## How to Check <!-- role: check -->

- **Visual Sign:** A model using only r poorly predicts which trials users get wrong.
- **The Test:** Compare feature-based vs r-based predictors using model-selection metrics (e.g., AIC) on judgment correctness; if features win, your evaluation should incorporate them [@yangCorrelationJudgmentVisualization2019a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a proxy feature (e.g., dispersion-to-regression-line) to your evaluation model.
- **Best Fix:** Build an evaluation pipeline that extracts and tests multiple candidate visual features, then retains the smallest set that best predicts judgments for your chart family [@yangCorrelationJudgmentVisualization2019a].
