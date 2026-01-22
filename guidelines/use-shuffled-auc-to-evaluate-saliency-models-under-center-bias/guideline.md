---
id: use-shuffled-auc-to-evaluate-saliency-models-under-center-bias
title: Use shuffled AUC to evaluate saliency models when fixation data is center-biased
bibliography: references.bib
description: Prefer shuffled AUC for saliency-model evaluation to reduce center-bias
  and border-effect confounds.
labels:
- chart:roc
- task:evaluate
- visual:position
- impact:validity
- data:spatial
- audience:expert
- domain:saliency
---

## Use shuffled AUC for center-bias-robust saliency evaluation <!-- role: advice -->

Use shuffled Area Under the Curve (AUC) when scoring saliency maps against eye fixations, especially when fixations are concentrated near the image center. Treat fixations on other images as negatives to discount center bias.

## Why shuffled AUC reduces confounds in saliency scoring <!-- role: reason -->

Shuffled AUC changes the negative sample distribution from uniform image locations to a distribution that matches typical human fixation tendencies (including center preference). This makes the score sensitive to stimulus-driven deviations from the generic fixation prior and reduces inflation from center bias and border artifacts.

**Mechanism:** By sampling negatives from fixations on other stimuli, the classifier test becomes “can the map predict where people looked on this stimulus beyond where people usually look,” instead of “can the map exploit the center.”

**Evidence:** Existing eye-tracking image datasets show strong center bias, which inflates scores for center-peaked predictions under several metrics; shuffled AUC makes a centered Gaussian baseline perform near chance while distinguishing models by off-center predictive power [@borjiQuantitativeAnalysisHumanModel2013]. Shuffled AUC is identified as the most reliable option among the compared scores for mitigating center bias and border effects in model comparisons [@borjiQuantitativeAnalysisHumanModel2013].

**Notes:** This metric supports fairer ranking when some models implicitly or explicitly include a center prior.

## When shuffled AUC is the right evaluation setup <!-- role: context -->

- **User Goal:** Rank or compare saliency models for eye-fixation prediction fairly.
- **Task:** Benchmarking models across datasets or reporting state-of-the-art performance.
- **Data:** Eye fixation locations over images or video frames with strong central clustering.
- **Chart Setting:** ROC/AUC-style evaluation of saliency maps as binary classifiers over sampled points.
- **Audience:** Researchers or engineers comparing attention models across methods.
- **Success Criterion:** Model ranking reflects stimulus-driven prediction, not dataset priors.

## When not to use shuffled AUC <!-- role: exceptions -->

**Break it when:** Your goal is to measure performance including center preference as part of the intended behavior (e.g., you explicitly want a “typical viewing strategy” prior). **Why:** Shuffled AUC intentionally discounts center bias and will under-reward models that encode that prior [@borjiQuantitativeAnalysisHumanModel2013].

## Tradeoffs of shuffled AUC <!-- role: costs -->

**Sacrifice:** Results are less comparable to older papers that report only standard AUC, Correlation Coefficient (CC), or Normalized Scanpath Saliency (NSS). **Risk:** If the “other-image fixation” pool differs greatly from the test setting, the negative distribution may be mismatched. **Mitigation:** Keep the shuffled-negative pool within the same dataset or collection protocol.

## Common mistakes when applying shuffled AUC <!-- role: mistakes -->

**Mistake:** Reporting only CC or NSS as the headline benchmark score on center-biased datasets. **Why it fails:** These metrics can be dominated by center preference and can overstate performance of centered predictions [@borjiQuantitativeAnalysisHumanModel2013].

## Quick tests for center-bias-robust evaluation <!-- role: check -->

**Failure Sign:** A simple centered Gaussian baseline ranks unusually high across models. **Quick Check:** Score a centered Gaussian “blob” baseline and verify it is near chance under shuffled AUC. **Stronger Test:** Repeat scoring on a subset of low center-bias images and check whether rankings remain consistent.

## What to do instead if shuffled AUC is not available <!-- role: fix -->

- Use a negative sample set derived from fixation locations on other images (the shuffled-negative construction) rather than uniform random negatives.
- Report shuffled AUC alongside any legacy metric to show whether rankings are stable under center-bias control.
- Evaluate on a subset of images selected to have low center-bias ratio before comparing models.
- Include a centered Gaussian baseline as a diagnostic to reveal center-bias sensitivity in the evaluation.
