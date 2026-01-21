---
id: use-scatterplots-for-precise-correlation-judgments
title: Use Scatterplots When Correlation Precision Matters
bibliography: references.bib
description: Prefer scatterplots for correlation judgments because they yield among
  the lowest JNDs and show symmetric performance for positive vs negative correlation.
labels:
- chart:scatter
- task:compare
- task:judge-correlation
- impact:accuracy
- data:bivariate
- audience:designer
- metric:jnd
---

## The Rule <!-- role: advice -->

Use scatterplots to communicate correlation when you need viewers to discriminate small differences in correlation.

## The Logic <!-- role: reason -->

Lower JND means viewers can detect smaller correlation differences more reliably. In the study’s Weber-model fits, scatterplots were among the best-performing visualizations, and scatterplot performance did not differ significantly between positive and negative correlations (symmetric precision).

- **The Principle:** Discrimination-based precision measured by JND (modeled via Weber’s law)
- **The Evidence:** Scatterplots produced low JNDs and no significant positive-vs-negative difference (Mann–Whitney p=0.54) [@harrisonRankingVisualizationsCorrelation2014a].

## Where to Apply <!-- role: context -->

- **User Goal:** Decide which of two relationships is more strongly correlated; detect subtle changes in correlation.
- **Data Type:** Two quantitative variables; dense point clouds (tested with 100 points).
- **Audience:** General viewers or analysts who must make reliable comparative judgments.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You must use a non-bivariate “ordered” form (e.g., when the task requires an explicit x-order encoding unrelated to the two variables).
- **Reason:** The paper’s strongest precision evidence applies to correlation discrimination; it does not claim scatterplots are best for tasks that depend on an imposed order [@harrisonRankingVisualizationsCorrelation2014a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less direct support for explicit ordering than order-based charts.
- **The Risk:** If the design context forces ordering or aggregation, a scatterplot may not match the communication constraints even if it is precise for correlation [@harrisonRankingVisualizationsCorrelation2014a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Replacing a scatterplot with stacked or line-based alternatives assuming they are equivalent for correlation.
- **Why it fails:** The paper shows large JND differences across forms; many alternatives performed substantially worse or were unreliable in some directions [@harrisonRankingVisualizationsCorrelation2014a].

## How to Check <!-- role: check -->

- **Visual Sign:** Users confidently and consistently pick the more-correlated plot across a range of r, not only near |r|≈1.
- **The Test:** Compare predicted JNDs (from the paper’s Weber fits) against your chosen alternative; if the alternative’s JND is higher in your r-range, prefer the scatterplot [@harrisonRankingVisualizationsCorrelation2014a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Swap the correlation view to a scatterplot representation for the correlation comparison step.
- **Best Fix:** Use scatterplots as the baseline, and only deviate if you can justify a different form with comparable JND in your r-range (via Weber/JND evaluation) [@harrisonRankingVisualizationsCorrelation2014a].
