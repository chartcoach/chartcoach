---
id: model-correlation-perception-with-weber-law-jnd
title: "Model correlation-discrimination precision as JND linear in adjusted correlation\
  \ (Weber\u2019s law)"
bibliography: references.bib
description: Treat correlation perception precision as a Weber-law process by fitting
  JND vs adjusted correlation.
labels:
- chart:scatter
- task:compare
- visual:position
- impact:predictability
- data:quantitative
- audience:researcher
- method:psychophysics
---

## Fit a Weber model using JNDs computed from an above/below staircase and adjusted correlation <!-- role: advice -->

Measure just-noticeable differences (JNDs) for correlation with an adaptive staircase, then fit a linear model of JND as a function of adjusted correlation (shift r by half the mean JND from above/below) to obtain a Weber model.

## Why adjusted-correlation linear fits summarize correlation perception precision <!-- role: reason -->

The staircase procedure estimates the smallest reliably discriminable change in correlation at each base correlation value. Adjusting the base correlation by half the JND (toward the approached boundary) aligns “above” and “below” measurements into a common perceptual scale, allowing a simple linear fit that captures Weber-like proportional sensitivity.

**Mechanism:** The fitted line (intercept and slope) compresses many discrimination judgments into a predictive function: given a correlation level, it predicts how large a change must be for viewers to notice it.

**Evidence:** The paper replicated a prior in-lab scatterplot result via crowdsourcing and found JNDs could be modeled as a linear function of adjusted correlation with high fit (for scatterplots, r² near 0.98 in the replication), validating the approach [@harrisonRankingVisualizationsCorrelation2014a]. Extending to nine visualization types, each tested visualization showed a strong linear relationship between JND and adjusted correlation for at least one correlation direction, enabling concise Weber models (reported intercepts/slopes and r² values) [@harrisonRankingVisualizationsCorrelation2014a].

**Notes:** The methodology defines a chance boundary and ceiling effects inherent to the staircase parameters; these bounds help interpret when correlation is not being reliably perceived.

## When to use a Weber-law JND model of correlation perception <!-- role: context -->

- **User Goal:** Predict or compare how precisely people can discriminate correlation differences from a given visualization.
- **Task:** Forced-choice judgment of which of two displays is more correlated (precision).
- **Data:** Bivariate quantitative data with controlled correlation levels; repeated resampling is acceptable.
- **Chart Setting:** Stimuli can be regenerated per trial; side-by-side comparisons are feasible.
- **Audience:** Any; the paper demonstrates feasibility with crowdsourced participants after training.
- **Success Criterion:** High linear fit of JND vs adjusted correlation and JND values meaningfully below chance boundary.

## When not to use this modeling approach <!-- role: exceptions -->

- **Break it when:** Participants frequently hit the procedure’s chance boundary or ceiling effects for a visualization×direction condition. **Why:** The staircase cannot converge on a stable JND, so the fitted model is unreliable.
- **Break it when:** Your correlation task is not discrimination between two displays (for example, identifying exact r values). **Why:** The model parameterizes discrimination thresholds, not numeric estimation.

## Tradeoffs of Weber-law JND modeling <!-- role: costs -->

**Sacrifice:** Collecting JNDs requires many judgments per condition and careful control of staircase parameters. **Risk:** Bounds (chance boundary, ceiling) depend on staircase settings, so changing parameters changes interpretability. **Mitigation:** Keep staircase parameters consistent across compared visualizations when the goal is ranking.

## Common mistakes in Weber-law modeling for correlation charts <!-- role: mistakes -->

- **Mistake:** Pooling “above” and “below” JNDs without the adjusted-correlation step. **Why it fails:** The model-fitting procedure in the paper relies on adjustment to align measurements before linear regression.
- **Mistake:** Assuming one model covers both positive and negative correlations for a visualization. **Why it fails:** The paper finds strong asymmetries for many visualization forms, implying separate models may be needed.

## Quick checks for a valid Weber model fit <!-- role: check -->

**Failure Sign:** Large fractions of JND values cluster at the chance boundary or at a ceiling limit for a condition. **Quick Check:** Confirm the fitted JND-vs-adjusted-correlation line shows a strong linear fit and small residual error for the condition being modeled. **Stronger Test:** Re-run the staircase simulation for chance performance under your exact parameters to recompute the chance boundary, then verify observed JNDs sit well below it.

## What to do instead if the model fit is unreliable <!-- role: fix -->

- Increase the starting distance and adjust staircase step sizes so the procedure can escape the chance boundary for difficult visualization×direction conditions.
- Restrict modeling to the visualization×direction conditions where JNDs are reliably measurable, and report exclusions explicitly.
- Collect additional trials at correlation levels where ceiling effects occur to better characterize the measurable region.
- If your application needs numeric correlation estimates, use an accuracy-focused evaluation method rather than a JND staircase.
