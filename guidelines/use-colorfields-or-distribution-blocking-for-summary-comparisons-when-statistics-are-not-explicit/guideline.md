---
id: use-colorfields-or-distribution-blocking-for-summary-comparisons-when-statistics-are-not-explicit
title: "Use Color-Based Visual Summarization for Summary Comparisons When Stats Aren\u2019\
  t Explicit"
bibliography: references.bib
description: Prefer color-based encodings that support preattentive summarization
  for comparing aggregate properties like averages when you are not explicitly plotting
  the statistic.
labels:
- chart:heatmap
- task:compare
- visual:color
- impact:accuracy
- data:temporal
- audience:novice
- source:albers-2014
---

## The Rule <!-- role: advice -->

When you are not explicitly encoding the summary statistic, use color-based encodings that enable preattentive summarization (e.g., colorfields) to support summary comparisons such as comparing averages.

## The Logic <!-- role: reason -->

The visual system can summarize ensembles of color efficiently, supporting judgments of aggregate properties over regions without requiring point-by-point reading. In the average task, standard colorfields outperformed line graphs even though neither explicitly encoded the mean, consistent with color’s advantage for summary comparison when aggregation is visual rather than computational.

- **The Principle:** Preattentive ensemble summarization supports visual aggregation.
- **The Evidence:** For average comparisons, colorfields outperformed line graphs, indicating an advantage for color-based summarization when the statistic is not explicitly encoded [@albersTaskdrivenEvaluationAggregation2014a].

## Where to Apply <!-- role: context -->

- **User Goal:** Compare aggregate levels across months (especially averages) without needing exact daily values.
- **Data Type:** High-density time series where per-point reading is impractical.
- **Audience:** Broad audiences in quick-comparison settings.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The task requires locating a specific day/month containing an extreme value (max/min) or computing range from extrema.
- **Reason:** The paper shows color encodings generally underperform position for point comparisons and paired point computations like range [@albersTaskdrivenEvaluationAggregation2014a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Reduced precision for extracting specific point values.
- **The Risk:** Users may misread extremes or ranges because color does not support exact value extraction as well [@albersTaskdrivenEvaluationAggregation2014a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a colorfield and expecting users to accurately answer max/min questions.
- **Why it fails:** Color supports summarization, not precise point extraction; the study found point tasks favored position encodings [@albersTaskdrivenEvaluationAggregation2014a].

## How to Check <!-- role: check -->

- **Visual Sign:** Users can tell “overall brighter month” but can’t reliably point to the single highest/lowest day.
- **The Test:** Ask both an average question and a maxima question; if average accuracy is strong but maxima accuracy drops, the encoding is summary-biased (as expected) [@albersTaskdrivenEvaluationAggregation2014a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add an explicit per-month statistic (e.g., mean bar/marker) if the summary must be more precise.
- **Best Fix:** Use a design that combines summary-friendly encoding with task-aligned discrete aggregation when the task unit is known (e.g., monthly blocks) [@albersTaskdrivenEvaluationAggregation2014a].
