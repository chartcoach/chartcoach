---
id: do-not-assume-position-encoding-advantage-for-mean-tasks
title: Do Not Assume Bar-Top Position Precision Carries Over to Mean Judgments
bibliography: references.bib
description: The classic position-over-area precision hierarchy for single values
  does not reliably apply when viewers compare averages across multiple values.
labels:
- chart:bar
- task:compare
- visual:position
- impact:accuracy
- data:categorical
- audience:general
- statistic:mean
- source:paper-yuan-haroz-franconeri
---

## The Rule <!-- role: advice -->

If users must compare group means, do not rely on the fact that a bar chart has aligned tops to guarantee precise judgments.

## The Logic <!-- role: reason -->

For single-value comparisons (1vs1), normal bars behave like position encodings (similar precision to dots), but for multi-value mean comparisons (e.g., 2vs2, 6vs6), normal bars no longer outperform misaligned (extent-only) bars—implying that viewers are not consistently using bar-top positions to compute means. This breaks the expected extrapolation from the single-value precision hierarchy.

- **The Principle:** Precision hierarchy (position > length/area) does not extrapolate to multivalue averaging tasks
- **The Evidence:** [@yuanPerceptualProxiesExtracting2019]

## Where to Apply <!-- role: context -->

- **User Goal:** Compare averages across two groups of multiple observations
- **Data Type:** Small-to-moderate sets per group (the effect appears even for 2vs2)
- **Audience:** Anyone making perceptual comparisons rather than doing explicit calculation

## When to Break It <!-- role: exceptions -->

- **Scenario:** The task is explicitly a single-value comparison (e.g., one bar vs one bar)
- **Reason:** In 1vs1 comparisons, the paper finds bars and dots yield similar high precision, consistent with position use [@yuanPerceptualProxiesExtracting2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may need additional encodings or explicit summaries rather than “just bars”
- **The Risk:** Overcomplicating a simple chart if the task is actually single-value comparison

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding more bars (more observations) and expecting the average to become easier to “see”
- **Why it fails:** The paper shows discrimination gets worse as set size increases, and bar-based mean judgments remain low-precision [@yuanPerceptualProxiesExtracting2019].

## How to Check <!-- role: check -->

- **Visual Sign:** Users struggle or disagree on which group’s mean is larger even when bar tops suggest a clear mean difference
- **The Test:** Compare performance/clarity between a bars view and a dots view of the same observations; if dots feel easier for mean judgment, your bar chart is not delivering the presumed position advantage [@yuanPerceptualProxiesExtracting2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Offer a dot-plot alternative view for the same data
- **Best Fix:** Use a position-only representation for observations when the key task is comparing means across groups [@yuanPerceptualProxiesExtracting2019].
