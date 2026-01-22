---
id: use-scatterplots-for-bivariate-correlation-estimation
title: Use scatterplots when people must estimate bivariate correlation (positive
  or negative)
bibliography: references.bib
description: For correlation-estimation tasks, scatterplots provide higher precision
  than several alternative bivariate visualizations for both positive and negative
  correlations.
labels:
- chart:scatter
- task:correlate
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- metric:jnd
- complexity:advanced
---

## Prefer scatterplots for correlation estimation <!-- role: advice -->

Use a scatterplot (points with x-position and y-position) when viewers must judge the strength of correlation between two quantitative variables. Prefer it for both positively and negatively correlated data.

## Correlation precision is highest with position-position points <!-- role: reason -->

Estimating correlation depends on how clearly viewers can perceive the joint pattern formed by paired quantitative values. Using 2D position with point marks supports precise discrimination of changes in correlation strength, yielding lower Just Noticeable Difference (JND), which indicates higher precision.

**Mechanism:** Point marks placed by x-position and y-position preserve the geometric structure of the bivariate relationship, enabling finer discrimination of correlation differences.

**Evidence:** In a correlate task measured by JND, the scatterplot designs for positive and negative correlations were in the top performance group and were ranked ahead of multiple other chart designs (including bar-/area-/arc-based designs and some line-based designs), with Bayesian credible differences reported between the top group and lower groups [@kayWebersLawSecond2016; @zengReviewCollationGraphical2023].

**Notes:** This evidence is specific to correlation judgments evaluated via JND (precision), not speed or preference.

## Correlation-estimation recommendation context <!-- role: context -->

- **User Goal:** Decide which of two relationships is more strongly correlated, or estimate correlation strength.
- **Task:** Correlate (bivariate correlation judgment).
- **Data:** Two quantitative variables with either positive or negative correlation.
- **Chart Setting:** Static visualization (no interaction assumed).
- **Audience:** General audiences where consistent interpretability is needed.
- **Success Criterion:** Higher precision in correlation discrimination (lower JND).

## When not to rely on a scatterplot for correlation estimation <!-- role: exceptions -->

**Break it when:** Your visualization is not supporting correlation estimation (e.g., the user is not doing a correlate judgment). **Why:** The evidence only covers the correlate task measured by JND, so it does not justify a general preference outside that scope.

## Tradeoffs of choosing scatterplots for correlation estimation <!-- role: costs -->

**Sacrifice:** Scatterplots may require more space to avoid overplotting at higher densities. **Risk:** If overplotting obscures the point pattern, the intended precision advantage may not materialize. **Mitigation:** Validate legibility under your expected point density before relying on correlation judgments.

## Common failure modes in applying this guidance <!-- role: mistakes -->

**Mistake:** Using a non-scatter alternative (e.g., bar-/area-/arc-based encodings) for correlation estimation without checking whether it preserves correlation perception precision. **Why it fails:** The collated ranking shows multiple non-scatter designs fall into lower-precision groups for the correlate task measured by JND [@kayWebersLawSecond2016; @zengReviewCollationGraphical2023].

## Quick checks for correlation-estimation fitness <!-- role: check -->

**Failure Sign:** Viewers struggle to distinguish slightly different correlation strengths (they guess or disagree widely). **Quick Check:** Ask a few readers to pick which of two plotted relationships is more correlated; if performance seems unreliable, treat the design as risky for correlation judgments. **Stronger Test:** Run a small forced-choice pilot similar to a correlate discrimination task and compare error rates or discrimination thresholds across candidate charts.

## What to do instead if a scatterplot cannot be used <!-- role: fix -->

- Use another position-based bivariate design only if you can validate correlation-discrimination precision for your audience and setting.
- If you must use a non-position-centric chart type, add a workflow step that avoids relying on visual correlation estimation (e.g., compute and show the correlation value alongside the chart).
- Reduce reliance on fine-grained correlation discrimination by reframing the task (e.g., present only coarse categories like “low/medium/high correlation” with explicit thresholds).
- If space or legibility is the blocker, reduce marks (sampling/aggregation) so a scatterplot remains readable while preserving the correlation pattern.
