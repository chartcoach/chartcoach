---
id: model-bivariate-encoding-distance-from-univariate-kernels-with-weighted-power-metric
title: Model Bivariate Encoding Distance from Univariate Kernels with a Weighted Power
  Metric
bibliography: references.bib
description: Estimate how two visual channels combine perceptually by fitting a weighted
  power model to predict bivariate distances from univariate perceptual kernels.
labels:
- chart:any
- task:evaluate
- visual:color
- visual:shape
- visual:size
- impact:predictability
- data:multivariate
- audience:researcher
- method:modeling
- source:demiralp-2014
---

## The Rule <!-- role: advice -->

When you need a predictive model of combined encodings (e.g., shape+color), fit a **weighted power model** to predict bivariate perceptual distances from the two corresponding univariate kernels.

## The Logic <!-- role: reason -->

The fitted exponent n indicates where the pair lies on the separable–integral continuum (n≈1 suggests city-block-like separability; n≈2 suggests Euclidean-like integrality), and the weights capture relative dominance of dimensions; in the paper, this model achieved best fit when kernels came from triplet matching [@demiralpLearningPerceptualKernels2014a].

- **The Principle:** Interactions between perceptual dimensions can be approximated by a parameterized metric combining univariate distances.
- **The Evidence:** The paper fits (d\_{ij} \\sim b0 + ((b1 d1)^n + (b2 d2)^n)^{1/n}) to shape-color, shape-size, and size-color kernels and reports intermediate n values and dimension scaling parameters, with Tm yielding best likelihoods [@demiralpLearningPerceptualKernels2014a].

## Where to Apply <!-- role: context -->

- **User Goal:** Predict perceptual distances for bivariate palette items without fully re-measuring all combinations.
- **Data Type:** Two-channel encodings where you already have univariate kernels (e.g., separate shape and color kernels).
- **Audience:** Researchers and tool builders modeling perceptual interaction effects.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your collected kernel method is spatial arrangement-based.
- **Reason:** The paper reports SA behaving inconsistently and producing weaker fits/less reliable structures for multidimensional relations [@demiralpLearningPerceptualKernels2014a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Requires nonlinear regression and careful interpretation of parameters (b0, b1/b2, n).
- **The Risk:** A fitted model can oversimplify if the true perceptual interaction is not well captured by a single exponent/weighting across all distances [@demiralpLearningPerceptualKernels2014a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming channels combine purely additively (L1) or purely Euclidean (L2) without checking.
- **Why it fails:** The paper finds intermediate n values that vary by channel pair (e.g., interactions involving size showing more integrality) [@demiralpLearningPerceptualKernels2014a].

## How to Check <!-- role: check -->

- **Visual Sign:** Predicted bivariate similarities don’t match observed cluster structure in the bivariate kernel.
- **The Test:** Fit the model and compare log-likelihood across kernels collected via different judgment types; triplet matching should provide the best predictive fit in their findings [@demiralpLearningPerceptualKernels2014a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Refit using bivariate kernels estimated via triplet matching rather than Td/SA.
- **Best Fix:** Use triplet matching kernels for univariate inputs and bivariate targets, then use the fitted parameters to inform how strongly each channel should be weighted in combined encodings [@demiralpLearningPerceptualKernels2014a].
