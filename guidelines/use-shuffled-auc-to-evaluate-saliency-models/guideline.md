---
id: use-shuffled-auc-to-evaluate-saliency-models
title: Use Shuffled AUC to Evaluate Saliency Models
bibliography: references.bib
description: Prefer shuffled AUC over CC/NSS/AUC to reduce center-bias and border-effect
  confounds when comparing saliency models.
labels:
- chart:roc
- task:evaluate
- visual:position
- impact:validity
- data:spatial
- audience:expert
- metric:shuffled-auc
---

## The Rule <!-- role: advice -->

Use **shuffled AUC** (not CC, NSS, or standard AUC) as your primary metric when comparing visual saliency models against human fixations.

## The Logic <!-- role: reason -->

Shuffled AUC uses other-image fixations as negatives, which discounts dataset viewing biases (especially center bias) and reduces sensitivity to border artifacts that can inflate ROC-like scores.

- **The Principle:** Bias-resistant evaluation via matched negative sampling
- **The Evidence:** The paper reports that CC and NSS are sensitive to center preference (e.g., Gaussian-center baseline scoring high), while shuffled AUC makes the Gaussian baseline near chance and is recommended as “the best option” for comparison [@borjiQuantitativeAnalysisHumanModel2013].

## Where to Apply <!-- role: context -->

- **User Goal:** Fairly ranking models by how well they predict *non-trivial* fixation locations
- **Data Type:** Eye-tracking fixations on images or videos (free viewing)
- **Audience:** Researchers/engineers benchmarking saliency or attention models

## When to Break It <!-- role: exceptions -->

- **Scenario:** You need to score “how centered” gaze is (e.g., quantifying center preference itself).
- **Reason:** Shuffled AUC intentionally discounts center bias, so it is the wrong tool if center bias is the phenomenon of interest [@borjiQuantitativeAnalysisHumanModel2013].

## The Price <!-- role: costs -->

- **The Sacrifice:** Comparability to older work that reports only CC/NSS/standard AUC.
- **The Risk:** With very few subjects per stimulus, the shuffled negative set can be noisy and may affect stability of estimates [@borjiQuantitativeAnalysisHumanModel2013].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Reporting only CC or NSS because they are easy to compute.
- **Why it fails:** These metrics can reward a trivial centered Gaussian baseline on center-biased datasets, overstating model quality [@borjiQuantitativeAnalysisHumanModel2013].

## How to Check <!-- role: check -->

- **Visual Sign:** A centered Gaussian “model” appears to rank surprisingly high.
- **The Test:** Score a simple central Gaussian baseline; if it scores well, your metric/dataset is likely still dominated by center bias (shuffled AUC should keep it ~chance) [@borjiQuantitativeAnalysisHumanModel2013].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add shuffled AUC alongside existing metrics and base conclusions primarily on it.
- **Best Fix:** Standardize benchmarking around shuffled AUC for model ranking and significance testing [@borjiQuantitativeAnalysisHumanModel2013].
