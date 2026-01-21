---
id: avoid-misleading-correlation-comparisons-by-monitoring-confidence-bounding-box-perpendicular-width
title: Control Perpendicular Thickness in Confidence Bounding Boxes
bibliography: references.bib
description: Reduce misleading correlation impressions by ensuring perpendicular thickness
  cues are consistent across scatterplots.
labels:
- chart:scatter
- task:compare
- visual:length
- impact:clarity
- data:bivariate
- audience:general
- source:yang-correlation-features
---

## The Rule <!-- role: advice -->

When creating scatterplots intended for correlation comparison, keep the **perpendicular thickness** of the point cloud (as captured by the perpendicular side of a confidence bounding box) consistent with the intended correlation differences.

## The Logic <!-- role: reason -->

A bounding-box–based length feature—**the perpendicular side of the confidence bounding box** (conf_bounding_box_perp)—was one of the top four features predicting participants’ correctness, outperforming correlation-based predictors [@yangCorrelationJudgmentVisualization2019a].

- **The Principle:** Viewers use simple length/thickness heuristics as proxies for correlation.
- **The Evidence:** conf_bounding_box_perp was among the strongest features in the paper’s standardized weighted logistic regression comparisons [@yangCorrelationJudgmentVisualization2019a].

## Where to Apply <!-- role: context -->

- **User Goal:** Decide which of two scatterplots shows stronger correlation.
- **Data Type:** Bivariate scatterplots, especially in dashboards with multiple small multiples.
- **Audience:** Mixed audiences making fast judgments [@yangCorrelationJudgmentVisualization2019a].

## When to Break It <!-- role: exceptions -->

- **Scenario:** The goal is to highlight extreme points/outliers rather than correlation strength.
- **Reason:** Outliers can legitimately expand bounding dimensions; constraining thickness could hide what you want users to notice [@yangCorrelationJudgmentVisualization2019a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional effort to ensure comparable perceptual thickness across views.
- **The Risk:** If you suppress thickness cues too aggressively, genuine differences in dispersion may be under-communicated [@yangCorrelationJudgmentVisualization2019a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming matching correlation values guarantees matching perceived “tightness.”
- **Why it fails:** The paper shows that, for the same Δr, judgments can differ due to variation in perceptual features like perpendicular thickness [@yangCorrelationJudgmentVisualization2019a].

## How to Check <!-- role: check -->

- **Visual Sign:** Two plots with similar correlation look very different in “width” perpendicular to the trend.
- **The Test:** Side-by-side inspection: if perpendicular thickness differs strongly, expect biased correlation comparisons even when correlations are similar [@yangCorrelationJudgmentVisualization2019a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce visual artifacts that inflate perceived perpendicular width (e.g., excessive overlap that makes the cloud look thicker).
- **Best Fix:** In comparative settings, standardize presentation so perpendicular thickness reliably tracks dispersion rather than incidental rendering effects [@yangCorrelationJudgmentVisualization2019a].
