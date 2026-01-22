---
id: prefer-dispersion-around-regression-line-as-primary-cue-for-scatterplot-correlation
title: Emphasize dispersion around the regression line when designing scatterplots
  for correlation comparison
bibliography: references.bib
description: Scatterplot correlation judgments track a small set of dispersion-related
  visual features more closely than the correlation coefficient itself.
labels:
- chart:scatter
- task:compare
- visual:position
- impact:accuracy
- data:quantitative
- audience:novice
- complexity:advanced
---

## Dispersion around the regression line should dominate correlation cues <!-- role: advice -->

Design scatterplots for correlation comparison so the perceived dispersion of points around the implied regression line is the most salient cue.

## Dispersion-based features align with correlation judgments <!-- role: reason -->

Correlation discrimination in scatterplots can be explained by a small number of perceivable features, and the strongest ones are all measures of how tightly the point cloud hugs the regression line; strengthening that cue makes judgments more consistent with intended correlation differences.

**Mechanism:** When dispersion perpendicular to the trend is easy to perceive, viewers can use it as a stable proxy for “more vs. less correlated” without explicitly estimating a statistical coefficient.

**Evidence:** Viewers’ pairwise “which is more correlated” judgments were better predicted by dispersion-related features than by the actual correlation difference, with top predictors including the standard deviation of perpendicular distances to the regression line and prediction-ellipse measures [@yangCorrelationJudgmentVisualization2019a]. The same top feature(s) could replace correlation in Weber-style and log-linear correlation-perception models without loss of precision, indicating interchangeability for modeling judgments [@yangCorrelationJudgmentVisualization2019a].

**Notes:** The best-performing cues were redundant in meaning (all encode tightness around the trend) even though they came from different feature families (length/area/density).

## When this applies: correlation comparison from scatterplots <!-- role: context -->

- **User Goal:** Decide which of two relationships is “more correlated.”
- **Task:** Binary discrimination (higher vs. lower correlation) from side-by-side scatterplots.
- **Data:** Two quantitative variables shown as points; moderate-to-high point counts typical of scatterplots.
- **Chart Setting:** Static scatterplots, potentially compared in small multiples.
- **Audience:** General audiences, including people without formal statistical training.
- **Success Criterion:** Higher accuracy and consistency in correlation ranking/discrimination.

## When not to follow it: non-correlation reading goals <!-- role: exceptions -->

**Break it when:** The main task is not correlation discrimination (e.g., identifying clusters or outliers). **Why:** Emphasizing trend-tightness can de-emphasize other patterns that may be more task-relevant [@yangCorrelationJudgmentVisualization2019a].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Some designs that amplify dispersion cues can reduce attention to other structures in the data cloud. **Risk:** Viewers may over-focus on a single “tightness” cue even when other cues (e.g., nonlinearity) matter. **Mitigation:** Treat correlation-reading as a specific task and evaluate with a discrimination-style test rather than open-ended interpretation [@yangCorrelationJudgmentVisualization2019a].

## Common failure modes <!-- role: mistakes -->

**Mistake:** Assuming viewers directly perceive the correlation coefficient rather than perceiving visual proxies. **Why it fails:** Judgments align more strongly with a small set of dispersion-related visual features than with correlation itself [@yangCorrelationJudgmentVisualization2019a].

## Quick tests <!-- role: check -->

**Failure Sign:** People disagree about which plot is “more correlated” even when the intended correlation difference is fixed. **Quick Check:** Compare candidate designs by whether the point cloud’s perpendicular spread around the trend is visually obvious in both plots. **Stronger Test:** Run a forced-choice (which is more correlated) discrimination task and verify judgments track intended ordering [@yangCorrelationJudgmentVisualization2019a].

## What to do instead when dispersion is not readable <!-- role: fix -->

- Increase the readability of the point cloud’s spread around the trend by adjusting the design so perpendicular dispersion is visually salient.
- Use a design variant that makes the data cloud’s “tightness” around the trend easier to see as a first-order cue.
- If correlation ranking is critical, validate the design with a discrimination-threshold procedure rather than relying on subjective estimation [@yangCorrelationJudgmentVisualization2019a].
