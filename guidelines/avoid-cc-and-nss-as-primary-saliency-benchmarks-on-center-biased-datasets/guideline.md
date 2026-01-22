---
id: avoid-cc-and-nss-as-primary-saliency-benchmarks-on-center-biased-datasets
title: Avoid CC and NSS as primary saliency benchmarks when datasets are center-biased
bibliography: references.bib
description: Do not rely on CC and NSS alone for saliency-model ranking when fixation
  distributions are centrally concentrated.
labels:
- chart:heatmap
- task:evaluate
- visual:position
- impact:validity
- data:spatial
- audience:expert
- domain:saliency
---

## Avoid CC and NSS as headline metrics under center bias <!-- role: advice -->

Avoid using Linear Correlation Coefficient (CC) and Normalized Scanpath Saliency (NSS) as your primary saliency-model comparison metrics when fixation data is strongly center-biased. If you must report them, pair them with a center-bias-robust metric.

## Why CC and NSS can be dominated by center preference <!-- role: reason -->

Both CC and NSS can reward saliency maps that place high mass near the image center when human fixations are centrally clustered, even if the map is not capturing image-specific attentional pulls. This makes model ranking sensitive to dataset priors and to design choices like adding a center Gaussian.

**Mechanism:** When fixations are concentrated centrally, any centrally peaked prediction increases overlap with fixation-derived maps or sampled fixation points, boosting CC/NSS without improving stimulus-specific prediction.

**Evidence:** Multiple widely used eye-tracking image datasets exhibit strong center bias, and a simple centered Gaussian baseline scores competitively under CC and NSS, indicating that these metrics are sensitive to center preference [@borjiQuantitativeAnalysisHumanModel2013]. CC and NSS are explicitly identified as suffering from the center-bias issue and are discouraged for future model comparisons in this evaluation framework [@borjiQuantitativeAnalysisHumanModel2013].

**Notes:** Border-handling can also alter these scores through changes in the saliency distribution away from typical fixation regions.

## When this metric choice matters most <!-- role: context -->

- **User Goal:** Produce fair model rankings and detect real progress in fixation prediction.
- **Task:** Comparing many models across datasets, or publishing benchmark tables.
- **Data:** Fixations with high density near the center (photographer bias or viewing strategy).
- **Chart Setting:** Any report where a single metric determines “best model.”
- **Audience:** Readers who will reuse your reported ranking to choose methods.
- **Success Criterion:** Rankings are robust to center bias and border artifacts.

## When CC or NSS can still be appropriate <!-- role: exceptions -->

**Break it when:** You explicitly study how well a model reproduces the full fixation density including center preference (e.g., modeling viewing strategy). **Why:** In that case, rewarding the center prior is part of the target behavior rather than a confound [@borjiQuantitativeAnalysisHumanModel2013].

## Tradeoffs of deprioritizing CC and NSS <!-- role: costs -->

**Sacrifice:** You may lose continuity with earlier literature that used CC/NSS as defaults. **Risk:** Some audiences may misinterpret lower CC/NSS as worse performance even when center bias is controlled elsewhere. **Mitigation:** Clearly label CC/NSS as center-bias-sensitive and present a robust metric alongside them.

## Common mistakes with CC and NSS reporting <!-- role: mistakes -->

- **Mistake:** Declaring a model “best” because it tops CC or NSS on a center-biased dataset. **Why it fails:** The ranking can reflect center preference rather than stimulus-driven saliency prediction [@borjiQuantitativeAnalysisHumanModel2013].
- **Mistake:** Comparing models with different implicit center priors using CC/NSS without a baseline. **Why it fails:** The scores can be confounded by differing priors rather than differences in feature computation [@borjiQuantitativeAnalysisHumanModel2013].

## Quick tests to detect CC/NSS center-bias domination <!-- role: check -->

**Failure Sign:** A centered Gaussian baseline ranks among top models under CC/NSS. **Quick Check:** Score the centered Gaussian baseline and check whether it places near the top under CC/NSS. **Stronger Test:** Recompute scores on a low-center-bias subset and see whether rankings change substantially.

## What to do instead of CC/NSS-only benchmarking <!-- role: fix -->

- Use shuffled AUC as the primary ranking metric when datasets are center-biased.
- Include a centered Gaussian baseline to quantify how much of the score is explained by center preference.
- Report results on a low-center-bias subset in addition to the full dataset.
- Use multiple metrics but weight conclusions toward the metric that discounts center bias and border effects.
