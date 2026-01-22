---
id: include-a-centered-gaussian-baseline-and-sweep-its-size-to-diagnose-center-bias
title: Include a centered Gaussian baseline and sweep its size to diagnose center-bias
  sensitivity in metrics
bibliography: references.bib
description: Use a Gaussian-blob baseline and vary its spread to reveal whether scores
  are driven by center bias.
labels:
- chart:line
- task:benchmark
- visual:position
- impact:validity
- data:spatial
- audience:expert
- domain:saliency
---

## Use a Gaussian center baseline as a metric sensitivity probe <!-- role: advice -->

Add a centered Gaussian-blob baseline to your saliency evaluation and vary its standard deviation to test how sensitive your metrics are to center bias. Prefer metrics whose Gaussian-baseline score remains near chance across blob sizes.

## Why Gaussian-blob sweeps expose center-bias dependence <!-- role: reason -->

A centered Gaussian contains no image information and encodes only a center prior; if a metric rewards it strongly, that metric (or dataset) is dominated by center bias. Sweeping the blob size shows whether a score can be tuned by changing only the center spread, indicating susceptibility to inflated performance.

**Mechanism:** Center-biased datasets align with the Gaussian prior; metrics that compare distributions over the whole map can increase as overlap with the central fixation density increases, while robust metrics should not materially change.

**Evidence:** Varying Gaussian size changes CC and NSS substantially and shows peak performance at certain blob sizes, while shuffled AUC remains near chance and is largely invariant to Gaussian size, demonstrating robustness to center bias [@borjiQuantitativeAnalysisHumanModel2013]. A centered Gaussian baseline is used as a diagnostic comparator and performs strongly on center-biased datasets under center-sensitive metrics [@borjiQuantitativeAnalysisHumanModel2013].

**Notes:** This is a diagnostic for the evaluation pipeline, not a competitor model.

## When to run a Gaussian-blob sweep <!-- role: context -->

- **User Goal:** Validate that your evaluation metric reflects stimulus-driven prediction.
- **Task:** Metric selection, benchmark auditing, or sanity checking reported results.
- **Data:** Eye fixations over images/frames where center bias may exist.
- **Chart Setting:** Reporting metric curves versus Gaussian spread.
- **Audience:** Benchmark designers and model evaluators.
- **Success Criterion:** A non-informative center prior does not achieve high scores under the primary metric.

## When a Gaussian-blob sweep is less informative <!-- role: exceptions -->

**Break it when:** Stimuli are designed so targets/fixations are uniformly distributed by experimental constraint. **Why:** The centered baseline will be uniformly poor regardless of metric sensitivity, providing less diagnostic separation [@borjiQuantitativeAnalysisHumanModel2013].

## Tradeoffs of baseline sweeps <!-- role: costs -->

**Sacrifice:** Additional compute and reporting space. **Risk:** Readers may misinterpret the best-performing Gaussian size as an acceptable modeling shortcut. **Mitigation:** Frame it explicitly as a confound probe rather than a saliency approach.

## Common mistakes using Gaussian baselines <!-- role: mistakes -->

**Mistake:** Using a single arbitrary Gaussian size and treating its score as a fixed reference. **Why it fails:** Some metrics and datasets show strong dependence on Gaussian spread, so one size can under- or overstate center-bias influence [@borjiQuantitativeAnalysisHumanModel2013].

## Quick tests for center-bias sensitivity <!-- role: check -->

**Failure Sign:** CC or NSS increases markedly as the Gaussian blob broadens, despite no image content. **Quick Check:** Plot score versus Gaussian standard deviation for the centered baseline. **Stronger Test:** Verify shuffled AUC stays near chance for all blob sizes while CC/NSS vary.

## What to do if the evaluation is center-bias sensitive <!-- role: fix -->

- Switch the headline metric to shuffled AUC for model ranking.
- Add a low-center-bias subset analysis to demonstrate stimulus-driven performance.
- Report Gaussian-sweep curves to document metric sensitivity transparently.
- Include the Gaussian baseline score in the main comparison table to contextualize results.
