---
id: prioritize-dispersion-around-regression-line-for-correlation-judgments
title: Emphasize Dispersion Around the Regression Line
bibliography: references.bib
description: Design scatterplots so that dispersion around the implied regression
  line is easy to perceive when users judge correlation.
labels:
- chart:scatter
- task:judge
- visual:position
- impact:clarity
- data:bivariate
- audience:general
- source:yang-correlation-features
---

## The Rule <!-- role: advice -->

Make the point cloud’s dispersion *perpendicular to the implied trend line* easy to see, because users rely on it to judge correlation.

## The Logic <!-- role: reason -->

People appear to judge correlation via visual proxies rather than correlation itself; the strongest proxy identified is the **standard deviation of perpendicular distances to the regression line** (dist_line_sd), which predicted judgment correctness better than Δr in their logistic models [@yangCorrelationJudgmentVisualization2019a].

- **The Principle:** Correlation judgments use salient dispersion cues around the trend.
- **The Evidence:** dist_line_sd was one of the top-performing features across odds ratio, AIC, and Cox tests, outperforming correlation-based predictors [@yangCorrelationJudgmentVisualization2019a].

## Where to Apply <!-- role: context -->

- **User Goal:** Decide which of two scatterplots is “more correlated,” or discriminate small correlation differences.
- **Data Type:** Bivariate numeric data displayed as points (scatterplots).
- **Audience:** Non-experts and experts alike, especially in quick, comparative viewing situations [@yangCorrelationJudgmentVisualization2019a].

## When to Break It <!-- role: exceptions -->

- **Scenario:** The task is to estimate slope (direction/steepness) rather than strength of association.
- **Reason:** Dispersion around the trend line is tuned for correlation discrimination, not for recovering slope magnitude [@yangCorrelationJudgmentVisualization2019a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Other potentially relevant cues (e.g., clusters, outliers) may receive less design emphasis.
- **The Risk:** Over-emphasizing dispersion cues could reduce attention to other analytic goals (e.g., subgroup structure) [@yangCorrelationJudgmentVisualization2019a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming viewers “see correlation directly” and ignoring how point dispersion reads perceptually.
- **Why it fails:** The paper’s feature analysis shows judgments align more with dispersion-derived features than with correlation values themselves [@yangCorrelationJudgmentVisualization2019a].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers struggle to reliably pick the more-correlated plot when differences are small.
- **The Test:** Compare two plots where Δr is the same: if perceived difficulty varies a lot, dispersion cues may be inconsistent or misleading [@yangCorrelationJudgmentVisualization2019a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce perceptual clutter so the thickness of the point cloud around the implied trend is visible.
- **Best Fix:** Redesign to make perpendicular spread around the trend line the dominant visible cue (i.e., ensure the cloud’s “thickness” is readable as the primary signal of correlation strength) [@yangCorrelationJudgmentVisualization2019a].
