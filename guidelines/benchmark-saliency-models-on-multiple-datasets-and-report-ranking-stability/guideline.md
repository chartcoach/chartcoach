---
id: benchmark-saliency-models-on-multiple-datasets-and-report-ranking-stability
title: Benchmark saliency models on multiple datasets and report ranking stability
  across them
bibliography: references.bib
description: Use multiple image and video datasets to avoid overfitting conclusions
  to dataset-specific statistics and biases.
labels:
- chart:table
- task:compare
- visual:position
- impact:trust
- data:spatial
- audience:expert
- domain:saliency
---

## Evaluate across multiple datasets before concluding a model is best <!-- role: advice -->

Benchmark saliency models across multiple datasets with different content and fixation statistics, and report how rankings change across datasets. Treat a model as reliably strong only if it performs well under several dataset/metric combinations.

## Why multi-dataset evaluation prevents misleading conclusions <!-- role: reason -->

Different datasets vary in content categories, photographer bias, number of subjects, and fixation centrality, all of which can change which features appear predictive. A single dataset can reward models that match its idiosyncrasies rather than general attention mechanisms.

**Mechanism:** When dataset statistics shift, models tuned to particular feature distributions or priors can rise or fall in rank; cross-dataset consistency is a proxy for robustness.

**Evidence:** Model rankings vary across datasets and across evaluation scores, while some models perform more consistently; dataset center bias and category composition are shown to influence evaluation outcomes and apparent performance [@borjiQuantitativeAnalysisHumanModel2013]. Performance differences across image categories (e.g., nature vs. human/car scenes) further indicate dataset composition can change difficulty and rankings [@borjiQuantitativeAnalysisHumanModel2013].

**Notes:** This applies to both static images and videos, where temporal and cognitive factors also shift performance.

## When multi-dataset benchmarking is required <!-- role: context -->

- **User Goal:** Claim general improvement or select a model for broad deployment.
- **Task:** Model selection, leaderboard reporting, or ablation validation.
- **Data:** Multiple public datasets or internally collected datasets with differing scene types and biases.
- **Chart Setting:** Summary tables/plots of scores and ranks per dataset.
- **Audience:** Readers who will generalize results beyond one benchmark.
- **Success Criterion:** Conclusions remain stable under dataset changes.

## When single-dataset benchmarking may be acceptable <!-- role: exceptions -->

**Break it when:** You are optimizing for a narrowly defined application domain with a fixed stimulus distribution. **Why:** Generalization beyond that domain is not the objective, so dataset-specific tuning is appropriate [@borjiQuantitativeAnalysisHumanModel2013].

## Tradeoffs of multi-dataset benchmarking <!-- role: costs -->

**Sacrifice:** More computation and more complex reporting. **Risk:** Conflicting rankings can be difficult to summarize into a single “winner.” **Mitigation:** Emphasize rank stability and metric robustness rather than a single-number summary.

## Common mistakes in multi-dataset comparisons <!-- role: mistakes -->

**Mistake:** Averaging scores across datasets with different biases and treating the average as definitive. **Why it fails:** Differences in center bias and difficulty can dominate the combined number and hide failure modes [@borjiQuantitativeAnalysisHumanModel2013].

## Quick tests for ranking robustness <!-- role: check -->

**Failure Sign:** The “best” model changes dramatically when switching datasets or when using low-center-bias subsets. **Quick Check:** Compute ranks per dataset under the same metric and compare the top set overlap. **Stronger Test:** Recompute ranks under shuffled AUC and on low-center-bias subsets to see if conclusions persist.

## What to do instead of single-dataset claims <!-- role: fix -->

- Report per-dataset rankings using a center-bias-robust metric as the primary comparator.
- Add a low-center-bias subset analysis to test off-center fixation prediction.
- Break down results by content category when a dataset provides categories to reveal selective strengths.
- Include baseline and human inter-observer references on each dataset to contextualize scale and difficulty.
