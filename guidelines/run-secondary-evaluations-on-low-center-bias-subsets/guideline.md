---
id: run-secondary-evaluations-on-low-center-bias-subsets
title: Evaluate Separately on Low Center-Bias Stimuli
bibliography: references.bib
description: Create and report results on a low-center-bias subset to focus evaluation
  on off-center fixations that are more diagnostic.
labels:
- chart:bar
- task:compare
- visual:position
- impact:robustness
- data:spatial
- audience:expert
- bias:center
---

## The Rule <!-- role: advice -->

In addition to full-dataset results, report model performance on a **subset of stimuli with low center bias**.

## The Logic <!-- role: reason -->

Off-center fixations are more informative and harder to predict; separating them reduces the chance that rankings are driven primarily by central viewing tendencies.

- **The Principle:** Stratified evaluation on diagnostically difficult cases
- **The Evidence:** The paper selects least-center-biased images (via a CBR threshold) and shows rankings and the Gaussian baseline change, while models are closer to IO on these subsets under shuffled AUC [@borjiQuantitativeAnalysisHumanModel2013].

## Where to Apply <!-- role: context -->

- **User Goal:** Distinguishing true saliency prediction from center-prior exploitation
- **Data Type:** Image datasets with many stimuli where center bias varies across images
- **Audience:** Benchmark maintainers and model authors

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your dataset is too small; subset selection would leave too few samples.
- **Reason:** Very small subsets increase variance and may make rankings unstable [@borjiQuantitativeAnalysisHumanModel2013].

## The Price <!-- role: costs -->

- **The Sacrifice:** Reduced sample size and possibly lower statistical power.
- **The Risk:** Results may be less representative of typical real-world viewing if center bias is a genuine behavioral component in your use case [@borjiQuantitativeAnalysisHumanModel2013].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Hand-picking a few “interesting” off-center examples.
- **Why it fails:** It introduces subjective selection bias; the paper uses a quantitative criterion (CBR threshold) [@borjiQuantitativeAnalysisHumanModel2013].

## How to Check <!-- role: check -->

- **Visual Sign:** The centered Gaussian baseline collapses in rank on the subset.
- **The Test:** Compute the subset’s fixation heatmap; confirm reduced central concentration and re-run scoring to see whether rankings change materially [@borjiQuantitativeAnalysisHumanModel2013].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Define a CBR threshold at a chosen radius and include all images below it.
- **Best Fix:** Publish both full and low-center-bias leaderboards, emphasizing shuffled AUC on the subset as the more diagnostic comparison [@borjiQuantitativeAnalysisHumanModel2013].
