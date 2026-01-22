---
id: quantify-and-report-center-bias-ratio-before-comparing-saliency-models
title: Quantify and report center-bias ratio before comparing saliency models across
  datasets
bibliography: references.bib
description: Measure how centrally concentrated fixations are so model rankings can
  be interpreted and compared fairly.
labels:
- chart:heatmap
- task:diagnose
- visual:position
- impact:trust
- data:spatial
- audience:expert
- domain:saliency
---

## Quantify fixation center bias before benchmarking models <!-- role: advice -->

Compute and report a center-bias ratio for each dataset (and optionally each image) before interpreting saliency-model scores. Use this measurement to select low-center-bias subsets when you want to emphasize off-center fixation prediction.

## Why center-bias measurement changes how scores should be read <!-- role: reason -->

If a dataset concentrates fixations near the center, many evaluation scores and many models will appear better simply by predicting the center. Quantifying center bias provides a dataset-level diagnostic that explains why simple centered baselines can score well and why rankings may shift across datasets.

**Mechanism:** A center-bias ratio summarizes how many fixations fall within central regions; higher ratios imply more of the measured “performance” can be explained by a center prior rather than image-driven saliency.

**Evidence:** Fixation distributions in common image datasets are shown to be highly center-biased, and a Center-Bias Ratio (CBR) procedure is introduced to quantify this concentration via fixation ratios within increasing-radius central circles [@borjiQuantitativeAnalysisHumanModel2013]. Selecting images by a CBR threshold yields small low-bias subsets, demonstrating that much of typical data can be dominated by central fixations [@borjiQuantitativeAnalysisHumanModel2013].

**Notes:** This does not deny that center bias may be real behavior; it isolates it as a confound for model comparison.

## When center-bias ratio reporting is most useful <!-- role: context -->

- **User Goal:** Make benchmarking results interpretable across datasets and over time.
- **Task:** Dataset audit, benchmark design, or model comparison.
- **Data:** Eye fixations pooled over subjects for images or frames.
- **Chart Setting:** Reporting dataset statistics alongside model score tables.
- **Audience:** Researchers selecting datasets or evaluating reported performance claims.
- **Success Criterion:** Readers can tell whether gains reflect center bias or stimulus-driven prediction.

## When you can skip center-bias ratio reporting <!-- role: exceptions -->

**Break it when:** Fixations are known to be experimentally constrained to non-central targets by design. **Why:** Center bias is not the dominant confound under that collection protocol [@borjiQuantitativeAnalysisHumanModel2013].

## Tradeoffs of adding center-bias measurement <!-- role: costs -->

**Sacrifice:** Extra preprocessing and reporting overhead. **Risk:** Over-filtering to low-center-bias images can reduce dataset size and statistical power. **Mitigation:** Report both full-dataset and low-bias-subset results.

## Common mistakes in center-bias handling <!-- role: mistakes -->

**Mistake:** Treating dataset-to-dataset score differences as model quality differences without checking fixation centrality. **Why it fails:** Different datasets can have different center-bias levels that shift rankings and inflate baseline performance [@borjiQuantitativeAnalysisHumanModel2013].

## Quick tests for problematic center bias <!-- role: check -->

**Failure Sign:** A high fraction of fixations fall within a moderate-radius central region and centered baselines score well. **Quick Check:** Plot pooled fixation heatmaps with concentric rings and compute fixation fractions by ring. **Stronger Test:** Re-rank models on a low-center-bias subset and compare rank correlations.

## What to do if center bias is too strong <!-- role: fix -->

- Select a subset of images using a center-bias ratio threshold to emphasize off-center fixations.
- Use shuffled AUC as the primary metric when center bias cannot be reduced.
- Include a centered Gaussian baseline and report its score to contextualize model performance.
- Report fixation distribution diagnostics (heatmap and ring histogram) alongside model rankings.
