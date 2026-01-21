---
id: quantify-and-report-center-bias-with-center-bias-ratio
title: Quantify and Report Dataset Center Bias Before Claiming Improvements
bibliography: references.bib
description: Measure and disclose center bias (e.g., via Center-Bias Ratio curves)
  because it can dominate saliency-model evaluation.
labels:
- chart:line
- task:diagnose
- visual:position
- impact:validity
- data:spatial
- audience:expert
- bias:center
---

## The Rule <!-- role: advice -->

Compute and report **center-bias** for each dataset (and optionally each image) using a center-bias ratio-style analysis before interpreting saliency scores.

## The Logic <!-- role: reason -->

If fixations cluster near the center, many models (or even a trivial Gaussian) can score well without capturing stimulus-driven saliency; you must quantify the bias to interpret results.

- **The Principle:** Confound measurement before inference
- **The Evidence:** The paper finds widely used datasets are highly center-biased and proposes a Center-Bias Ratio (CBR) approach to quantify the fraction of fixations inside concentric central regions [@borjiQuantitativeAnalysisHumanModel2013].

## Where to Apply <!-- role: context -->

- **User Goal:** Understanding whether evaluation results reflect dataset bias vs model capability
- **Data Type:** Eye fixation coordinates over images/videos
- **Audience:** Researchers curating datasets or publishing benchmark results

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are not using eye tracking/fixation ground truth.
- **Reason:** Center-bias ratio is defined on fixation distributions; it does not apply without fixations [@borjiQuantitativeAnalysisHumanModel2013].

## The Price <!-- role: costs -->

- **The Sacrifice:** Extra preprocessing and reporting.
- **The Risk:** Overemphasis on “de-biasing” may hide real behavioral center preferences that are part of human viewing strategies [@borjiQuantitativeAnalysisHumanModel2013].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming all datasets are equally unbiased or that “large dataset” implies “fair dataset.”
- **Why it fails:** The paper shows even popular datasets can have strong center fixation concentrations, which shifts rankings under some metrics [@borjiQuantitativeAnalysisHumanModel2013].

## How to Check <!-- role: check -->

- **Visual Sign:** A fixation heatmap shows a strong central hot spot and steep drop-off outward.
- **The Test:** Plot fixation percentages within increasing-radius central regions; very high fractions at moderate radii indicate strong center bias [@borjiQuantitativeAnalysisHumanModel2013].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a dataset-level fixation heatmap plus a center-bias ratio curve to your benchmark documentation.
- **Best Fix:** Use bias-aware evaluation (e.g., shuffled AUC) and/or run a secondary analysis on a low-center-bias subset (selected by a CBR threshold) [@borjiQuantitativeAnalysisHumanModel2013].
