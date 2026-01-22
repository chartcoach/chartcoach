---
id: avoid-area-arc-and-stacked-encodings-for-correlation-judgment-when-precision-matters
title: Avoid area/arc/stacked-style encodings for correlation judgment when precision
  (low JND) matters
bibliography: references.bib
description: For correlation estimation tasks, several non-scatter encodings (including
  area/arc/stacked-style representations) show lower precision than the top-performing
  group.
labels:
- chart:area
- chart:pie
- chart:bar
- task:correlate
- visual:area
- visual:angle
- impact:accuracy
- data:quantitative
- audience:general
- metric:jnd
- complexity:advanced
---

## Avoid lower-precision encodings for correlation estimation <!-- role: advice -->

Avoid using area-, angle/arc-, or stacked-style encodings as the primary means for viewers to judge correlation strength when you need high precision (low Just Noticeable Difference). Prefer designs that are known to yield higher precision for correlation discrimination.

## Lower-ranked designs yield higher JND for correlation discrimination <!-- role: reason -->

When the task is correlation discrimination, chart designs differ in how precisely viewers can perceive changes in correlation. Higher JND means viewers need larger correlation differences to reliably notice a difference, which is worse for precise judgments.

**Mechanism:** Encodings that do not directly preserve the bivariate spatial relationship can reduce discriminability of correlation differences, increasing the threshold at which differences become noticeable.

**Evidence:** In correlate tasks measured by JND, the collated results group multiple non-scatter designs—including area-based and arc/angle-based designs—into lower-performing rank groups than the top group, with Bayesian credible differences reported between the better-performing group(s) and these lower groups [@kayWebersLawSecond2016; @zengReviewCollationGraphical2023].

**Notes:** This guidance is about precision in correlation judgments (JND), not about aesthetics or suitability for other tasks.

## Precision-first correlation judgment context <!-- role: context -->

- **User Goal:** Make fine-grained judgments about correlation strength.
- **Task:** Correlate (forced-choice discrimination / estimation).
- **Data:** Two quantitative variables with positive or negative correlation.
- **Chart Setting:** Static, where the visualization must carry the judgment without interaction.
- **Audience:** General audiences where consistent precision is needed.
- **Success Criterion:** Lower JND (higher precision).

## When to ignore this precision-focused rule <!-- role: exceptions -->

**Break it when:** Precision in correlation judgment is not a requirement (e.g., correlation is only a secondary, qualitative takeaway). **Why:** The evidence concerns JND-based precision for correlation tasks, so it does not cover non-precision goals.

## Tradeoffs of avoiding these encodings <!-- role: costs -->

**Sacrifice:** You may lose a chart form that matches existing conventions in your organization. **Risk:** Switching chart types can reduce familiarity, even if it improves correlation precision. **Mitigation:** Pair the alternative chart with short explanatory labeling if the audience expects a different form.

## Common failure modes in correlation-encoding choice <!-- role: mistakes -->

**Mistake:** Choosing an area/arc/stacked-style visualization for correlation because it is visually distinctive, without validating correlation-discrimination performance. **Why it fails:** The collated ranking places multiple such designs in lower precision groups for correlate tasks measured by JND [@kayWebersLawSecond2016; @zengReviewCollationGraphical2023].

## Quick checks for precision risk <!-- role: check -->

**Failure Sign:** Small differences in correlation look similar or ambiguous across comparisons. **Quick Check:** Create two versions of the same relationship with slightly different correlation strength and ask a few readers to identify the stronger one; frequent mistakes indicate low precision. **Stronger Test:** Compare designs using a small discrimination study and estimate an empirical threshold for reliable judgments.

## What to do instead when these encodings are already mandated <!-- role: fix -->

- Add a numeric correlation statistic (e.g., Pearson’s r) near the visualization so the judgment does not rely on visual estimation alone.
- Provide a secondary view optimized for correlation estimation (e.g., a scatterplot) alongside the mandated primary chart.
- Reduce the need for fine discrimination by summarizing correlation into bins and labeling them explicitly.
- If you must keep the same chart type, constrain the use case to qualitative narration rather than precise correlation comparisons.
