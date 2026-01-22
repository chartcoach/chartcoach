---
id: derive-bivariate-perceptual-distances-from-univariate-kernels-using-a-weighted-power-metric
title: Model bivariate perceptual distances from univariate kernels with a weighted
  power metric when combining encodings
bibliography: references.bib
description: Bivariate perceptual distance can be approximated from univariate perceptual
  kernels using a weighted power model with an exponent between city-block and Euclidean.
labels:
- chart:any
- task:model
- visual:color
- visual:shape
- visual:size
- impact:automation
- data:multivariate
- audience:researcher
- complexity:advanced
---

## Predict combined-encoding distances from single-encoding kernels using a weighted power model <!-- role: advice -->

When you need perceptual distances for a combined (bivariate) encoding, approximate them from the corresponding univariate perceptual kernels using a weighted power metric with fitted scaling weights and exponent.

## Why the weighted power model helps combine perceptual dimensions <!-- role: reason -->

Combined stimuli reflect interactions between perceptual dimensions, so a simple additive rule can be inaccurate; a weighted power metric interpolates between city-block behavior (separable dimensions) and Euclidean behavior (integral dimensions) while allowing one dimension to dominate via learned weights.

**Mechanism:** The exponent controls how dimensions combine (from more separable to more integral), and weights account for unequal salience or scaling across dimensions.

**Evidence:** Bivariate kernels for shape–color, shape–size, and size–color were predicted from univariate kernels using a weighted power model with fitted exponent values generally between 1 and 2, and triplet-matching-derived kernels provided the best predictive fits by log-likelihood [@demiralpLearningPerceptualKernels2014a].

**Notes:** The fitted exponent varied by palette and judgment type, indicating different degrees of dimensional interaction.

## When this applies <!-- role: context -->

- **User Goal:** Obtain perceptual distances for combined encodings without running a full bivariate similarity study.
- **Task:** Predict bivariate distances from already-collected univariate kernels.
- **Data:** Two-dimensional stimuli built from combinations of two discrete palettes (e.g., 4×4 combinations).
- **Chart Setting:** Automated design systems that need perceptual distances to optimize assignments.
- **Audience:** Researchers or tool builders implementing perceptual models.
- **Success Criterion:** Bivariate distance predictions that closely match empirically estimated bivariate kernels.

## When not to follow it <!-- role: exceptions -->

**Break it when:** You can afford direct collection of bivariate judgments for the exact combined stimuli you will deploy. **Why:** Direct bivariate kernels can capture palette-specific interactions and dominance effects that a derived model may smooth over [@demiralpLearningPerceptualKernels2014a].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You trade direct measurement accuracy for reusability and reduced data collection. **Risk:** A fitted model may not transfer if the palette composition changes substantially or if one dimension dominates in unexpected ways. **Mitigation:** Validate predicted bivariate distances against a small sampled set of direct bivariate judgments.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Assuming bivariate perceptual distance is always Euclidean (L2) or always city-block (L1) without fitting. **Why it fails:** The observed exponent varied across dimension pairs and judgment types, indicating intermediate integrality rather than a fixed metric form [@demiralpLearningPerceptualKernels2014a].

## Quick tests <!-- role: check -->

**Failure Sign:** Predicted bivariate distances do not reproduce the major clusters seen when you directly inspect or embed the combined stimuli. **Quick Check:** Fit the weighted power model and inspect whether the exponent lands between 1 and 2 and whether prediction error is low. **Stronger Test:** Collect a small bivariate triplet-matching sample and compute rank correlation between predicted and measured bivariate distances.

## What to do instead <!-- role: fix -->

- Collect bivariate triplet matching judgments for the combined palette when high accuracy is required.
- Reduce the combined palette cardinality to make direct bivariate collection feasible.
- Treat one dimension as dominant and use it as the primary distance if your application can tolerate that simplification.
- Use the derived model only to initialize an optimization that is later refined with direct bivariate judgments.
