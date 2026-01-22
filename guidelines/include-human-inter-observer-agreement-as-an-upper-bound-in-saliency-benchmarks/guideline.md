---
id: include-human-inter-observer-agreement-as-an-upper-bound-in-saliency-benchmarks
title: Include human inter-observer agreement as an upper bound when benchmarking
  saliency models
bibliography: references.bib
description: Use inter-observer fixation prediction as a reference ceiling to quantify
  the remaining gap for computational saliency.
labels:
- chart:bar
- task:benchmark
- visual:position
- impact:interpretability
- data:spatial
- audience:expert
- domain:saliency
---

## Add an inter-observer baseline to contextualize model performance <!-- role: advice -->

Compute a Human Inter-Observer (IO) prediction baseline and report it alongside model scores to provide an empirical upper bound. Use it to interpret whether improvements are meaningful relative to human-to-human agreement.

## Why inter-observer baselines calibrate the scale of performance <!-- role: reason -->

Absolute metric values can be hard to interpret across datasets and scores; an inter-observer baseline anchors the evaluation to how predictable one human is from others under the same data collection. The model–human gap indicates remaining unexplained variance and whether small score gains are substantial.

**Mechanism:** IO aggregates fixations from other viewers to predict a held-out viewer; this captures shared attentional tendencies and sets a ceiling for stimulus-driven predictability under the dataset’s noise and variability.

**Evidence:** Inter-observer performance is used as an expected upper bound for computational models, and a significant gap remains between best models and IO on many datasets and metrics, indicating substantial headroom [@borjiQuantitativeAnalysisHumanModel2013]. IO can behave differently depending on subject count and metric (e.g., sparse hits affecting NSS), showing why it is essential as a calibration reference rather than a single fixed value [@borjiQuantitativeAnalysisHumanModel2013].

**Notes:** IO may be less reliable with very few subjects, especially in video datasets.

## When IO baselines are most important <!-- role: context -->

- **User Goal:** Quantify headroom and avoid overstating progress.
- **Task:** Benchmark reporting and cross-paper comparability.
- **Data:** Eye fixations from multiple subjects per stimulus.
- **Chart Setting:** Score plots that include computational models plus baselines.
- **Audience:** Researchers interpreting whether a model is near human-level.
- **Success Criterion:** Readers can see both chance level and human-level reference.

## When IO may be misleading without caveats <!-- role: exceptions -->

**Break it when:** The dataset has too few subjects per stimulus to form a stable IO map. **Why:** IO may underestimate true human agreement and can distort comparisons, particularly under metrics sensitive to sparse overlap [@borjiQuantitativeAnalysisHumanModel2013].

## Tradeoffs of adding IO baselines <!-- role: costs -->

**Sacrifice:** Requires subject-separated fixation data and extra computation. **Risk:** Misinterpretation if IO is treated as a strict ceiling across different subject counts or metrics. **Mitigation:** Report subject counts and interpret IO as dataset-conditional.

## Common mistakes with IO baselines <!-- role: mistakes -->

**Mistake:** Reporting only model scores without any human reference and calling small gains “near-human.” **Why it fails:** Without IO, it is unclear how close scores are to human predictability on that dataset [@borjiQuantitativeAnalysisHumanModel2013].

## Quick tests for IO usefulness <!-- role: check -->

**Failure Sign:** Model scores appear high but IO is much higher, or IO is unstable across metrics. **Quick Check:** Compute IO under the same metric and verify it is above chance and meaningfully above models. **Stronger Test:** Check IO stability by resampling subjects to estimate variability.

## What to do if IO cannot be computed <!-- role: fix -->

- Use datasets with subject-separated fixation data when the goal is benchmarking.
- Report chance-level baselines (e.g., centered Gaussian and/or uniform) and subject counts prominently.
- Avoid interpreting absolute scores as “human-level” without an IO reference.
- Prefer metrics less sensitive to sparse overlap when subject counts are small.
