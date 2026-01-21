---
id: control-border-effects-in-saliency-evaluation
title: Guard Against Border Effects in Saliency Scoring
bibliography: references.bib
description: Prevent border handling artifacts from inflating evaluation metrics,
  especially ROC/AUC-style measures.
labels:
- chart:roc
- task:evaluate
- visual:position
- impact:validity
- data:spatial
- audience:expert
- bias:border
---

## The Rule <!-- role: advice -->

Verify that your evaluation pipeline is not artificially boosting scores due to **image border effects**, and prefer metrics less sensitive to these artifacts.

## The Logic <!-- role: reason -->

Filter responses near borders can be ill-defined; adding dark borders (or handling invalid responses inconsistently) changes the saliency distribution at “negative” samples and can inflate ROC/KL-like measures because humans rarely fixate near edges.

- **The Principle:** Metric sensitivity to sampling distribution shifts
- **The Evidence:** The paper summarizes evidence that ROC and KL can increase when a black border is added even to a uniform map, and recommends shuffled AUC as more robust to borders [@borjiQuantitativeAnalysisHumanModel2013].

## Where to Apply <!-- role: context -->

- **User Goal:** Ensuring model improvements reflect fixation prediction, not implementation artifacts
- **Data Type:** Saliency maps produced by convolutional/multi-scale filtering pipelines
- **Audience:** Engineers implementing benchmarking code and model pipelines

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your model and evaluation explicitly model/measure edge fixations as a target behavior.
- **Reason:** Border suppression is not an artifact in that case; it is part of the intended signal [@borjiQuantitativeAnalysisHumanModel2013].

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional validation tests and potential re-implementation of border handling.
- **The Risk:** Over-correcting could remove legitimate saliency near borders in rare stimuli [@borjiQuantitativeAnalysisHumanModel2013].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Ignoring border handling differences across models when resizing or filtering saliency maps.
- **Why it fails:** Border behavior can systematically change score distributions, confounding comparisons [@borjiQuantitativeAnalysisHumanModel2013].

## How to Check <!-- role: check -->

- **Visual Sign:** A uniform/near-uniform saliency map scores above chance under ROC/AUC.
- **The Test:** Score a dummy uniform map with and without added borders; if scores rise with borders, your metric/pipeline is border-sensitive [@borjiQuantitativeAnalysisHumanModel2013].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add border-sensitivity sanity checks (uniform map, border perturbations) to your evaluation suite.
- **Best Fix:** Use shuffled AUC as the primary ROC-style metric and standardize border handling across model outputs before scoring [@borjiQuantitativeAnalysisHumanModel2013].
