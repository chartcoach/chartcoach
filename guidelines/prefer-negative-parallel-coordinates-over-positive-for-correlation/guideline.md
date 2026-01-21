---
id: prefer-negative-parallel-coordinates-over-positive-for-correlation
title: Prefer Parallel Coordinates for Negative Correlation, Not Positive
bibliography: references.bib
description: Use parallel coordinates plots preferentially when your dominant relationships
  are negatively correlated, since negative PCPs showed significantly better JND performance
  than positive PCPs.
labels:
- chart:parallel-coordinates
- task:judge-correlation
- impact:accuracy
- data:bivariate
- audience:designer
- concept:asymmetry
---

## The Rule <!-- role: advice -->

Use parallel coordinates plots to communicate correlation primarily when relationships are negative, and avoid relying on them for precise judgments of positive correlation.

## The Logic <!-- role: reason -->

The study found a strong asymmetry: PCPs depicting negative correlation yielded much lower JNDs than PCPs depicting positive correlation. This indicates viewers can discriminate correlation differences more precisely in negative PCP configurations.

- **The Principle:** Direction-dependent discrimination thresholds (JND)
- **The Evidence:** Parallel coordinates negative vs positive differed significantly (Mann–Whitney p < 0.001), and negative PCP performance was comparable to scatterplots in reported comparisons [@harrisonRankingVisualizationsCorrelation2014a].

## Where to Apply <!-- role: context -->

- **User Goal:** Compare strength of negative relationships using PCPs.
- **Data Type:** Two-variable (or PCP axis-pair) correlation judgments where the dominant pattern is negative.
- **Audience:** Analysts using PCPs for multivariate exploration but needing reliable correlation perception on axis pairs.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your task requires comparing positive correlations in PCP specifically.
- **Reason:** The study indicates positive PCPs have substantially worse JNDs; another form may be needed for precision [@harrisonRankingVisualizationsCorrelation2014a].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may need additional chart types (e.g., scatterplots) for positive relationships to keep correlation judgments precise.
- **The Risk:** Mixed-sign datasets can lead to inconsistent precision if PCP is used uniformly [@harrisonRankingVisualizationsCorrelation2014a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Treating axis flipping/reversal as merely aesthetic and not performance-relevant.
- **Why it fails:** The paper suggests that changes affecting whether relationships appear as negative vs positive in PCP can materially change JND performance [@harrisonRankingVisualizationsCorrelation2014a].

## How to Check <!-- role: check -->

- **Visual Sign:** Positive relationships in PCP look “harder” to compare; users hesitate or guess.
- **The Test:** If your PCP view is dominated by positive correlations, compare predicted JND for PCP-positive against alternatives; if higher, you’ve violated the rule [@harrisonRankingVisualizationsCorrelation2014a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** For correlation-focused comparisons, switch positive cases to a scatterplot view.
- **Best Fix:** In PCP-based systems, consider axis flips/reordering strategies that increase the proportion of negative correlations when correlation discrimination is a priority, then validate with JND/Weber modeling [@harrisonRankingVisualizationsCorrelation2014a].
