---
id: use-prediction-ellipse-cues-to-support-correlation-judgment
title: Make Prediction-Ellipse Shape Readable
bibliography: references.bib
description: Support correlation judgments by making prediction-ellipse cues (area
  and minor axis) perceptually available in scatterplots.
labels:
- chart:scatter
- task:judge
- visual:shape
- impact:clarity
- data:bivariate
- audience:general
- source:yang-correlation-features
---

## The Rule <!-- role: advice -->

Ensure the scatterplot visually communicates an “ellipse-like” point-cloud shape, especially its **ellipse area** and **minor-axis thickness**, because viewers use these cues to judge correlation.

## The Logic <!-- role: reason -->

Among 44 non-collinear candidate features, **prediction ellipse area** (ellipse_area) and **prediction ellipse minor axis** (ellipse_minor) were top predictors of judgment correctness, outperforming correlation-based baselines in multiple model metrics [@yangCorrelationJudgmentVisualization2019a].

- **The Principle:** Correlation is inferred from the overall shape and thickness of the point cloud.
- **The Evidence:** ellipse_area and ellipse_minor were among the four best-performing features across odds ratio, AIC, and Cox tests [@yangCorrelationJudgmentVisualization2019a].

## Where to Apply <!-- role: context -->

- **User Goal:** Compare correlation strength across multiple scatterplots (ranking or pairwise comparisons).
- **Data Type:** Bivariate point clouds where correlation varies.
- **Audience:** General audiences and analysts making quick discriminations [@yangCorrelationJudgmentVisualization2019a].

## When to Break It <!-- role: exceptions -->

- **Scenario:** The data are intentionally non-elliptical (e.g., strong clustering or non-linear patterns) and the goal is to notice those structures.
- **Reason:** Ellipse-based cues assume a roughly elliptical cloud; emphasizing them may mislead interpretation of non-elliptical structure [@yangCorrelationJudgmentVisualization2019a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Ellipse-like emphasis can deemphasize local structures (clusters, gaps).
- **The Risk:** Users may over-trust a global “ellipse impression” when structure is multi-modal or non-linear [@yangCorrelationJudgmentVisualization2019a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Treating ellipse cues as purely statistical constructs irrelevant to perception.
- **Why it fails:** The study found ellipse-derived visual features are strongly aligned with human judgments in correlation discrimination tasks [@yangCorrelationJudgmentVisualization2019a].

## How to Check <!-- role: check -->

- **Visual Sign:** The point cloud’s “thickness” and overall footprint are hard to summarize at a glance.
- **The Test:** Brief-view test: if you can’t quickly see whether the cloud is narrow vs wide (minor axis) or compact vs large (area), ellipse cues are not readable [@yangCorrelationJudgmentVisualization2019a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce overplotting so the cloud’s boundary and thickness are visible.
- **Best Fix:** Adjust the presentation so the point cloud’s global shape (its footprint and minor-axis thickness) is perceptually salient for fast comparison [@yangCorrelationJudgmentVisualization2019a].
