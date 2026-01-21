---
id: treat-positive-and-negative-correlation-as-separate-design-cases
title: Model Positive and Negative Correlation Separately
bibliography: references.bib
description: Account for asymmetric perception by evaluating positive and negative
  correlations as different conditions for many chart types.
labels:
- chart:comparative
- task:judge-correlation
- impact:accuracy
- data:bivariate
- audience:designer
- model:weber-law
- concept:asymmetry
---

## The Rule <!-- role: advice -->

Do not assume a chart’s correlation readability is the same for positive and negative relationships; evaluate and choose separately for each direction.

## The Logic <!-- role: reason -->

Many visualization forms change their salient visual features when switching from positive to negative correlation, leading to different discrimination thresholds. The study reports “striking variation” between negative and positive correlations for multiple visualizations and notes that many may require two Weber models (one per direction).

- **The Principle:** Perceptual asymmetry driven by direction-dependent visual form/features
- **The Evidence:** Significant direction effects (overall Kruskal–Wallis on visualization×direction), and specific asymmetries such as parallel coordinates performing significantly better for negative than positive correlation (p\<0.001) [@harrisonRankingVisualizationsCorrelation2014a].

## Where to Apply <!-- role: context -->

- **User Goal:** Compare correlations where sign varies (some relationships positive, others negative).
- **Data Type:** Bivariate data where both directions are plausible and meaningful.
- **Audience:** Designers building dashboards/analysis tools that may present mixed-sign relationships.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are using a visualization that demonstrates symmetric performance across directions in the study.
- **Reason:** Scatterplots showed no significant positive/negative difference, and ordered line charts were also close to symmetric in their reported comparison [@harrisonRankingVisualizationsCorrelation2014a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional evaluation and potentially different chart choices for positive vs negative cases.
- **The Risk:** Interface inconsistency (different chart types for different signs) if you optimize separately [@harrisonRankingVisualizationsCorrelation2014a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Selecting one “best” correlation chart and reusing it everywhere regardless of sign.
- **Why it fails:** For several forms, sign changes materially affect JND and can flip which visualization is more precise [@harrisonRankingVisualizationsCorrelation2014a].

## How to Check <!-- role: check -->

- **Visual Sign:** Users are much better at judging correlation for one sign than the other in the same chart form.
- **The Test:** Compare JND (or Weber-model) curves separately for positive and negative correlation; large separation indicates you must treat them as separate cases [@harrisonRankingVisualizationsCorrelation2014a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** If sign is known, pick the direction-specific better-performing chart condition.
- **Best Fix:** Maintain separate Weber/JND models for positive and negative correlation for each candidate visualization and choose per sign and r-range [@harrisonRankingVisualizationsCorrelation2014a].
