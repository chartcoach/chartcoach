---
id: include-trivial-baselines-and-human-inter-observer-upper-bound
title: Benchmark Against a Center Gaussian and Human Inter-Observer Maps
bibliography: references.bib
description: Always include a center-Gaussian baseline and a human inter-observer
  reference to contextualize saliency-model scores.
labels:
- chart:bar
- task:benchmark
- visual:position
- impact:comparability
- data:spatial
- audience:expert
- baseline:gaussian
- baseline:inter-observer
---

## The Rule <!-- role: advice -->

Always report performance for (1) a **central Gaussian blob baseline** and (2) a **human inter-observer (IO) model** when evaluating saliency models.

## The Logic <!-- role: reason -->

A central Gaussian reveals how much your scores are driven by center bias, while IO provides an empirical upper bound on predictability (how well humans predict each other).

- **The Principle:** Anchored evaluation with floor/ceiling references
- **The Evidence:** The study uses Gauss as a center-bias baseline and IO as an upper bound, and shows that many datasets are strongly center-biased and that a gap often remains between models and IO [@borjiQuantitativeAnalysisHumanModel2013].

## Where to Apply <!-- role: context -->

- **User Goal:** Interpreting whether a “good” score reflects real fixation prediction or just center bias; estimating headroom vs humans
- **Data Type:** Eye-tracking datasets with multiple observers per stimulus
- **Audience:** Researchers comparing models across datasets/metrics

## When to Break It <!-- role: exceptions -->

- **Scenario:** Fixations are not available per subject (only aggregated).
- **Reason:** The IO construction requires separating fixations by observer; otherwise IO cannot be computed as described [@borjiQuantitativeAnalysisHumanModel2013].

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional implementation and reporting complexity.
- **The Risk:** IO may be underestimated when few observers watched a stimulus, making the “upper bound” appear artificially low [@borjiQuantitativeAnalysisHumanModel2013].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Comparing models only to each other (no baselines).
- **Why it fails:** You can’t tell whether all models are merely exploiting center bias, or how far they are from human consistency [@borjiQuantitativeAnalysisHumanModel2013].

## How to Check <!-- role: check -->

- **Visual Sign:** Your best model is only marginally above a centered Gaussian on CC/NSS.
- **The Test:** Compute Gauss and IO scores; if Gauss is high on CC/NSS or near top ranks, center bias is likely inflating those metrics; if IO is far above all models, substantial headroom remains [@borjiQuantitativeAnalysisHumanModel2013].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add Gauss and IO rows to every results table/figure.
- **Best Fix:** Treat Gauss as a “sanity check” and IO as a “ceiling,” and reweight conclusions toward metrics/datasets where Gauss is near chance (e.g., shuffled AUC) [@borjiQuantitativeAnalysisHumanModel2013].
