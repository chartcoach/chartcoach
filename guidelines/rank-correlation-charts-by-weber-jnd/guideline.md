---
id: rank-correlation-charts-by-weber-jnd
title: Rank Correlation Visualizations Using Weber-Model JND
bibliography: references.bib
description: Use Weber-law models of JND to quantitatively compare and rank chart
  types for correlation judgments.
labels:
- chart:comparative
- task:rank
- task:compare
- impact:accuracy
- impact:clarity
- data:bivariate
- audience:designer
- model:weber-law
- metric:jnd
---

## The Rule <!-- role: advice -->

Rank correlation visualizations by their Weber-model predicted JND over your correlation range, and choose the chart with the lowest JND for the r-values you expect.

## The Logic <!-- role: reason -->

A just-noticeable difference (JND) captures the smallest correlation change that viewers can reliably discriminate; lower JND means higher perceptual precision. The paper shows that for multiple correlation visualizations, JND varies linearly with adjusted correlation (a Weber-law relationship), enabling concise models that can be compared and ranked without exhaustive retesting.

- **The Principle:** Weber’s law modeling of discrimination thresholds (JND as a function of stimulus level)
- **The Evidence:** The authors fit linear Weber models (high r², low RMS) for all included visualization×direction conditions and use the model areas to produce an overall ranking [@harrisonRankingVisualizationsCorrelation2014a].

## Where to Apply <!-- role: context -->

- **User Goal:** Discriminate which of two datasets/relationships is more correlated (precision), or choose the most perceptually precise chart for correlation reading.
- **Data Type:** Two quantitative variables with interest in correlation magnitude (tested with n=100, normally distributed points).
- **Audience:** Visualization designers selecting among multiple “valid” chart forms.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your candidate chart×direction condition yields many near-chance JND outcomes under similar task constraints.
- **Reason:** The paper excluded conditions with frequent near-chance performance; a Weber-model-based rank is not reliable when viewers cannot discriminate correlation well in that condition [@harrisonRankingVisualizationsCorrelation2014a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Requires either using published Weber fits (when applicable) or running a psychophysical JND study to fit your own model.
- **The Risk:** Rankings can change across correlation ranges due to crossings in regression lines, so an “overall best” may not be best at your specific r [@harrisonRankingVisualizationsCorrelation2014a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Picking a chart based on tradition or software defaults (e.g., whatever Excel recommends) instead of measured discrimination performance.
- **Why it fails:** The paper finds large, chart-dependent differences in correlation discrimination precision, so defaults can be substantially worse [@harrisonRankingVisualizationsCorrelation2014a].

## How to Check <!-- role: check -->

- **Visual Sign:** Users struggle to reliably choose the more-correlated view except at extreme correlations.
- **The Test:** For your expected r-range, compare predicted JNDs from the Weber lines; if your chosen chart is not among the lowest JNDs in that band, you’ve likely violated the rule [@harrisonRankingVisualizationsCorrelation2014a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch to a visualization×direction option that has a lower modeled JND at your target r (use the per-r ranking concept shown in the paper).
- **Best Fix:** Fit Weber models for your exact design variants and then rank them by average predicted JND across your intended correlation range [@harrisonRankingVisualizationsCorrelation2014a].
