---
id: match-evaluation-metric-to-ground-truth-structure
title: Choose Metrics That Match Your Ground Truth Structure
bibliography: references.bib
description: Use NSS for single-target synthetic patterns and fixation-based metrics
  for natural scenes, aligned to what the ground truth represents.
labels:
- chart:bar
- task:evaluate
- visual:position
- impact:validity
- data:spatial
- audience:expert
- metric:nss
---

## The Rule <!-- role: advice -->

Use **NSS** for single-target detection in synthetic search arrays, and use fixation-prediction metrics (preferably **shuffled AUC**) for natural image/video eye-tracking benchmarks.

## The Logic <!-- role: reason -->

NSS directly measures saliency values at known target locations and is appropriate when the “truth” is one target point; for fixation prediction, the truth is a distribution of gaze points where center bias and sampling matter, making shuffled AUC more diagnostic.

- **The Principle:** Metric–task alignment
- **The Evidence:** The paper uses NSS to score target localization in synthetic patterns (one tagged target per stimulus) and uses CC/NSS/shuffled AUC for fixation prediction, concluding shuffled AUC is the most reliable for model comparison on eye-tracking datasets [@borjiQuantitativeAnalysisHumanModel2013].

## Where to Apply <!-- role: context -->

- **User Goal:** Fairly scoring model performance given different definitions of “ground truth”
- **Data Type:** (a) Synthetic arrays with one target; (b) Natural scenes/videos with many fixations
- **Audience:** Researchers designing benchmarks across heterogeneous stimuli

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your synthetic stimulus has multiple valid targets or region-level ground truth (not a point).
- **Reason:** A single-point NSS setup no longer matches the ground truth definition and may mis-score correct region predictions [@borjiQuantitativeAnalysisHumanModel2013].

## The Price <!-- role: costs -->

- **The Sacrifice:** Multiple metrics across tasks reduce simplicity of reporting.
- **The Risk:** Readers may over-compare numbers across tasks even though the metrics capture different constructs [@borjiQuantitativeAnalysisHumanModel2013].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using one metric (e.g., CC) for everything, including single-target arrays.
- **Why it fails:** Distribution-oriented metrics can be uninformative or confounded when the truth is a single location and map normalization dominates [@borjiQuantitativeAnalysisHumanModel2013].

## How to Check <!-- role: check -->

- **Visual Sign:** A model that clearly peaks at the target is not rewarded, or a diffuse map is rewarded more than a correct sharp peak.
- **The Test:** For single-target stimuli, verify the score increases when the map peak aligns with the tagged target; if not, your metric is mismatched [@borjiQuantitativeAnalysisHumanModel2013].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Use NSS for single-target arrays; report mean±SEM across stimuli.
- **Best Fix:** Maintain separate evaluation protocols per stimulus class (synthetic target detection vs natural fixation prediction), using shuffled AUC as the anchor for the latter [@borjiQuantitativeAnalysisHumanModel2013].
