---
id: align-computed-summaries-to-the-users-comparison-blocks
title: "Align Computed Summaries to the User\u2019s Comparison Blocks"
bibliography: references.bib
description: Compute aggregates in the same discrete segments users compare (e.g.,
  months) instead of continuous summaries when the task is blockwise comparison.
labels:
- chart:composite
- task:compare
- task:locate
- visual:position
- impact:accuracy
- data:temporal
- audience:novice
- custom:design-variable-computation
- source:albers-2014
---

## The Rule <!-- role: advice -->

If users answer questions at a known granularity (e.g., months), compute and show statistics using those same discrete blocks, not continuous computations that cut across block boundaries.

## The Logic <!-- role: reason -->

When computation aligns with the unit of comparison, the visualization directly supports the decision and reduces ambiguity about which samples “belong” to each block. The study found clear benefits of discrete, task-aligned aggregation for average comparisons, and framed this as a computational design variable affecting performance.

- **The Principle:** Task-aligned discrete computation reduces cognitive translation between display and question.
- **The Evidence:** For average comparisons, discrete monthly aggregation outperformed continuous variants; the authors highlight task-aligned discrete aggregation as beneficial relative to continuous computation [@albersTaskdrivenEvaluationAggregation2014a].

## Where to Apply <!-- role: context -->

- **User Goal:** Compare blocks (months) by an aggregate statistic (especially mean).
- **Data Type:** Continuous time series presented in discrete comparison bins.
- **Audience:** Users answering questions framed in discrete periods.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Users do not share a fixed comparison unit or need to flexibly change the aggregation window.
- **Reason:** Hard-coding a single block size assumes prior task knowledge and can misfit other tasks or granularities [@albersTaskdrivenEvaluationAggregation2014a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Flexibility to support multiple granularities with one static view.
- **The Risk:** Users may generalize the shown blockwise statistic to questions it does not match (e.g., week-based questions) [@albersTaskdrivenEvaluationAggregation2014a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a moving average line to answer “which month has the highest average.”
- **Why it fails:** Moving averages are continuous and not explicitly aligned to month boundaries; the study indicates discrete, month-aligned aggregation improves accuracy for blockwise average comparisons [@albersTaskdrivenEvaluationAggregation2014a].

## How to Check <!-- role: check -->

- **Visual Sign:** Boundaries between months are unclear in the summary encoding, or the summary visibly “bleeds” across boundaries.
- **The Test:** For a month-based question, verify the shown aggregate can be read without integrating values that belong to adjacent months [@albersTaskdrivenEvaluationAggregation2014a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add explicit month segmentation and compute per-month summary marks.
- **Best Fix:** Redesign the summary layer so every displayed statistic is computed strictly within each comparison block (e.g., per-month bars/marks), optionally retaining raw data in a separate layer for context [@albersTaskdrivenEvaluationAggregation2014a].
