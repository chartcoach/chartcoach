---
id: select-uncertain-points-by-integrating-distribution-mass-inside-the-brush
title: Brush uncertain data by selecting distributions whose integrated probability
  mass inside the brush exceeds a confidence threshold
bibliography: references.bib
description: Replace inside/outside tests with probability-mass integration so uncertain
  values require larger brushes to select.
labels:
- chart:scatter
- chart:parallel-coordinates
- task:select
- visual:interaction
- impact:trust
- data:uncertain
- audience:expert
- complexity:advanced
---

## Use probability-mass selection for brushing uncertain data <!-- role: advice -->

When brushing uncertain data, select a sample only if the integrated area (probability mass) of its uncertainty distribution inside the brush exceeds a chosen confidence threshold (for example, 0.95). Treat brushing as selection of distributions rather than selection of point locations.

## Probability-mass brushing matches interaction behavior to uncertainty magnitude <!-- role: reason -->

Uncertain samples have infinite support as distributions, so a geometric inside/outside test is not meaningful. Integrating probability mass inside the brush yields a likelihood that the brush contains a draw from the distribution; requiring high mass forces larger brushes for uncertain samples and prevents accidental selection of unreliable values.

**Mechanism:** The same brush geometry captures less probability mass for higher-variance distributions, so a fixed mass threshold automatically scales selection strictness with uncertainty.

**Evidence:** Brushing uncertain samples is defined by integrating each distribution within the brush bounds and thresholding the resulting area, and a 95% confidence threshold is advocated so uncertain values require larger brushes to select [@fengMatchingVisualSaliency2010].

**Notes:** For uncorrelated normal distributions, the paper describes fast analytical integration using the error function, including separable 2D box integration [@fengMatchingVisualSaliency2010].

## When to use probability-mass brushing <!-- role: context -->

- **User Goal:** Make interactive selections that reflect data reliability rather than precise but uncertain coordinates.
- **Task:** Interval queries, box brushing in scatter plots, and range selection analogs in parallel coordinates.
- **Data:** Per-sample uncertainty represented as distributions; uncorrelated normal distributions enable especially fast evaluation.
- **Chart Setting:** Linked views where selection propagates and should not over-select uncertain samples.
- **Audience:** Analysts who interpret selections as evidence-bearing subsets.
- **Success Criterion:** Selected items are those that are likely to truly fall in the brushed region, not those whose uncertain means happen to lie there.

## When not to use probability-mass brushing <!-- role: exceptions -->

**Break it when:** The goal is exploratory “maybe-in-region” inclusion where partial overlap is valuable rather than strict confidence. **Why:** A high mass threshold can intentionally exclude uncertain items unless the brush is very large [@fengMatchingVisualSaliency2010].

## Tradeoffs of probability-mass brushing <!-- role: costs -->

**Sacrifice:** Selection is computationally heavier than an inside/outside test, especially without analytic integrals. **Risk:** Users may be surprised that some means inside the brush are not selected because their distributions are too uncertain. **Mitigation:** Communicate the confidence threshold as a property of the brush interaction.

## Common mistakes in uncertainty-aware brushing <!-- role: mistakes -->

- **Mistake:** Select uncertain samples based only on whether the mean lies inside the brush. **Why it fails:** It ignores uncertainty extent and can over-select unreliable samples, contradicting the goal of aligning interaction with confidence [@fengMatchingVisualSaliency2010].
- **Mistake:** Use a binary inside/outside test for distributions. **Why it fails:** Distributions are not bounded objects, so the test does not reflect likelihood of membership [@fengMatchingVisualSaliency2010].

## Quick checks for brushing behavior under uncertainty <!-- role: check -->

**Failure Sign:** Large-uncertainty samples are selected as easily as small-uncertainty samples with the same brush. **Quick Check:** Compare selection results for two samples with different variances but similar means; the uncertain one should require a larger brush to pass the confidence threshold [@fengMatchingVisualSaliency2010]. **Stronger Test:** For normal distributions, verify that computed mass increases smoothly as the brush expands around the mean.

## What to do instead if integration is too slow <!-- role: fix -->

- Use analytical integration for normal distributions via the error function when the uncertainty model supports it [@fengMatchingVisualSaliency2010].
- Use numerical integration only within the brush bounds when analytic forms are unavailable [@fengMatchingVisualSaliency2010].
- Perform selection in data space on distributed nodes and combine results, rather than selecting in rendered pixel space [@fengMatchingVisualSaliency2010].
- Use probabilistic plots and sample-based estimates of brush membership probability when full integration is impractical [@fengMatchingVisualSaliency2010].
