---
id: treat-donut-as-equivalent-to-stacked-bar-for-negative-correlation-precision
title: Treat Donut and Stacked Bar as Comparable for Negative Correlation Precision
bibliography: references.bib
description: For negative correlations, donut charts performed similarly to stacked
  bar charts in correlation discrimination precision under the tested conditions.
labels:
- chart:donut
- chart:stacked-bar
- task:judge-correlation
- impact:accuracy
- data:bivariate
- audience:designer
- concept:coordinate-transform
---

## The Rule <!-- role: advice -->

If you are choosing between a donut chart and a stacked bar chart to convey negative correlation, treat them as comparable in discrimination precision and decide based on other constraints.

## The Logic <!-- role: reason -->

The study did not find a statistically significant difference between stacked bar-negative and donut-negative in their JND data at the corrected threshold, suggesting similar perceptual precision for negative correlation discrimination in these two forms under the experiment’s conditions.

- **The Principle:** Empirical equivalence in discrimination threshold (JND)
- **The Evidence:** Stacked bar-negative vs donut-negative comparison was not significant under Bonferroni-corrected α (reported p=0.037, α=0.0036) [@harrisonRankingVisualizationsCorrelation2014a].

## Where to Apply <!-- role: context -->

- **User Goal:** Compare strengths of negative correlations using a stacked/part-to-whole-like radial vs rectangular form.
- **Data Type:** The study’s tested correlation stimuli mapped to stacked bar or donut encodings.
- **Audience:** Designers deciding between rectangular and radial presentation for layout/space reasons.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You need validated performance for positive correlations with donut-like encodings.
- **Reason:** Donut-positive was excluded as unreliable in the paper’s analysis, so this equivalence is supported only for the negative condition included [@harrisonRankingVisualizationsCorrelation2014a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Treating them as equivalent on precision means you must weigh other factors (space, aesthetics, consistency) without a precision “tie-breaker.”
- **The Risk:** Small differences could exist outside the tested stimulus characteristics (the paper’s scope) [@harrisonRankingVisualizationsCorrelation2014a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Choosing donut over stacked bar assuming radial form is inherently more/less precise for correlation.
- **Why it fails:** The paper’s evidence suggests no reliable precision difference for negative correlation in these conditions [@harrisonRankingVisualizationsCorrelation2014a].

## How to Check <!-- role: check -->

- **Visual Sign:** Users’ ability to discriminate negative correlation differences appears similar across the two options in practice.
- **The Test:** Compare their modeled JND curves for negative conditions; if they are close across your r-range, precision likely shouldn’t decide between them [@harrisonRankingVisualizationsCorrelation2014a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Choose based on non-precision constraints (space, compositional fit) when negative correlation is the focus.
- **Best Fix:** If your context differs from the paper’s stimuli, run a small JND staircase study and fit Weber lines for both encodings to confirm equivalence [@harrisonRankingVisualizationsCorrelation2014a].
