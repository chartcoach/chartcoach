---
id: account-for-border-effects-when-comparing-saliency-maps-across-implementations
title: Account for border effects when comparing saliency maps across implementations
bibliography: references.bib
description: Control or discount border-handling artifacts because they can inflate
  saliency evaluation scores.
labels:
- chart:heatmap
- task:evaluate
- visual:position
- impact:validity
- data:spatial
- audience:expert
- domain:saliency
---

## Control border effects in saliency evaluation pipelines <!-- role: advice -->

Treat border handling as a first-class evaluation concern when comparing saliency models, because undefined or padded filter responses at edges can change scores. Prefer evaluation setups that reduce border-driven inflation.

## Why border handling can inflate saliency scores <!-- role: reason -->

When filters extend beyond image boundaries, different implementations can introduce systematic low-saliency borders. Because fixations rarely occur at edges, this changes the saliency distribution of negative samples more than positives, increasing separability and inflating ROC-style scores even for non-informative maps.

**Mechanism:** Artificially low border values reduce false positives among edge negatives, raising true-versus-false discrimination without improving prediction at fixation locations.

**Evidence:** Border effects are identified as corrupting ROC and divergence-style scores, where adding black borders to an otherwise uniform saliency map increases ROC values substantially, showing evaluation inflation unrelated to saliency content [@borjiQuantitativeAnalysisHumanModel2013]. Shuffled AUC is emphasized as more robust to center bias and border effects than CC and NSS in comparative evaluation [@borjiQuantitativeAnalysisHumanModel2013].

**Notes:** Border effects can masquerade as model improvements and complicate cross-model fairness.

## When border effects are likely to matter <!-- role: context -->

- **User Goal:** Fairly compare saliency models from different codebases or parameterizations.
- **Task:** Benchmarking or leaderboard-style evaluation.
- **Data:** Saliency maps produced via convolutional or multi-scale filtering where edges require padding/truncation.
- **Chart Setting:** ROC/AUC-style evaluation with negative sampling across the image.
- **Audience:** Model evaluators aggregating results across many implementations.
- **Success Criterion:** Scores reflect attention prediction, not implementation-specific padding artifacts.

## When border effects are less critical <!-- role: exceptions -->

**Break it when:** Fixations frequently occur near borders due to experimental design or stimulus framing. **Why:** Edge artifacts will influence positives as well as negatives, reducing the one-sided inflation described for typical scene viewing [@borjiQuantitativeAnalysisHumanModel2013].

## Tradeoffs of border-effect control <!-- role: costs -->

**Sacrifice:** Some comparability with legacy evaluations that did not control borders. **Risk:** Overcorrecting borders may remove legitimate edge saliency in certain stimuli. **Mitigation:** Validate on a diverse stimulus set and report any preprocessing explicitly.

## Common mistakes with borders in saliency benchmarking <!-- role: mistakes -->

**Mistake:** Treating different padding/truncation choices as “implementation details” that need not be documented. **Why it fails:** Border handling can materially change evaluation scores independent of prediction quality [@borjiQuantitativeAnalysisHumanModel2013].

## Quick tests for border-driven inflation <!-- role: check -->

**Failure Sign:** A uniform or near-uniform saliency map scores well when a dark border is present. **Quick Check:** Score a constant saliency map with and without an artificial border and compare ROC/AUC changes. **Stronger Test:** Verify that shuffled AUC-based rankings are more stable than standard ROC-based rankings under border manipulations.

## What to do instead when border effects are detected <!-- role: fix -->

- Prefer shuffled AUC for headline comparisons when border effects and center bias are concerns.
- Standardize border handling across models by applying consistent resizing and padding conventions before scoring.
- Include sanity-check baselines (uniform map, centered Gaussian) to detect evaluation inflation.
- Report evaluation sensitivity tests (with/without border perturbations) when aggregating multi-source models.
