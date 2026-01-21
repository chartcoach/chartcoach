---
id: use-color-weaving-to-improve-average-and-spread-judgments-within-month-blocks
title: Use Color Weaving to Improve Average and Spread Judgments Within Blocks
bibliography: references.bib
description: Randomly permute values within time blocks (color weaving) to enhance
  distributional summarization for average and spread comparisons.
labels:
- chart:heatmap
- task:compare
- task:rank
- visual:color
- impact:accuracy
- data:temporal
- audience:novice
- custom:technique-color-weaving
- source:albers-2014
---

## The Rule <!-- role: advice -->

To support month-by-month judgments of distributional properties (especially average and spread), use color weaving: break within-block temporal structure by permuting values inside each block.

## The Logic <!-- role: reason -->

Permuting values within a block converts a temporally ordered signal into a texture-like distribution, improving the visual system’s ability to summarize the set of values in that block. In the paper’s results, woven colorfields performed strongly for average and were the best-performing color approach for spread (though still below box plots).

- **The Principle:** Making distributions “texture-like” improves ensemble/statistical perception.
- **The Evidence:** Woven colorfields were among the top performers for average comparison and outperformed most other encodings for spread comparison, consistent with improved summarization of within-month distributions [@albersTaskdrivenEvaluationAggregation2014a].

## Where to Apply <!-- role: context -->

- **User Goal:** Identify which month has the highest average or greatest spread around its mean.
- **Data Type:** Dense time series where within-block ordering is less important than the distribution.
- **Audience:** Users making fast comparative judgments across many blocks.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Users need to read temporal order within the month (e.g., “did values spike early or late in the month?”).
- **Reason:** Weaving intentionally destroys local temporal structure, making sequence questions hard or impossible [@albersTaskdrivenEvaluationAggregation2014a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Interpretability of within-block time patterns.
- **The Risk:** Users may assume there is no meaningful within-block ordering even when there is, because it has been removed [@albersTaskdrivenEvaluationAggregation2014a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using weaving to answer point questions like maxima/minima.
- **Why it fails:** Weaving makes it harder to locate a particular day/value, and the paper shows woven colorfields performed poorly on point tasks [@albersTaskdrivenEvaluationAggregation2014a].

## How to Check <!-- role: check -->

- **Visual Sign:** Months look like textured blocks rather than continuous strips.
- **The Test:** If you can no longer trace a within-month trend linearly left-to-right, you have (correctly) removed temporal order—confirm the task does not require that order [@albersTaskdrivenEvaluationAggregation2014a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Limit weaving to a secondary view used for summary comparison, while keeping a standard time-ordered view elsewhere.
- **Best Fix:** Use weaving only at the exact granularity users compare (e.g., month blocks) and keep other views/encodings for point tasks [@albersTaskdrivenEvaluationAggregation2014a].
