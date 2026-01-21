---
id: discretely-aggregate-at-task-granularity-for-average-comparisons
title: Discretely Aggregate at Task Granularity for Average Comparisons
bibliography: references.bib
description: Compute and show per-block averages (e.g., monthly) when users must compare
  averages across blocks.
labels:
- chart:bar
- chart:composite
- task:compare
- task:rank
- visual:position
- impact:accuracy
- data:temporal
- audience:novice
- source:albers-2014
---

## The Rule <!-- role: advice -->

If users must compare averages across time blocks (e.g., months), compute and display the average discretely per block rather than relying on continuous smoothing or raw data alone.

## The Logic <!-- role: reason -->

Task-aligned discrete aggregation matches the decision unit (month) and reduces the viewer’s need to mentally average many points. In the study’s average task, displays that discretely aggregated per month (or discretely blocked values into months) outperformed continuous approaches.

- **The Principle:** Task-aligned discrete aggregation improves aggregate comparison accuracy.
- **The Evidence:** For average comparisons, encodings with discrete monthly aggregation (e.g., composite graphs, box plots, color stock charts, woven colorfields blocked by month) significantly outperformed other encodings; discrete aggregation effects were more strongly supported than purely “color vs position” [@albersTaskdrivenEvaluationAggregation2014a].

## Where to Apply <!-- role: context -->

- **User Goal:** Choose which month has the highest average.
- **Data Type:** Dense daily time series summarized into months (or another explicit block).
- **Audience:** Non-expert viewers making comparative judgments without calculators.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Users need to see within-month temporal structure (e.g., sequences, trends, or exact days) as a primary goal.
- **Reason:** Discrete aggregation can hide within-block patterns by summarizing them away [@albersTaskdrivenEvaluationAggregation2014a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Loss of raw point detail when summaries dominate the display.
- **The Risk:** If the chosen block size does not match the user’s actual question, the visualization may encourage wrong inferences [@albersTaskdrivenEvaluationAggregation2014a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding a continuous moving average and assuming it will support “monthly average” comparisons.
- **Why it fails:** Continuous aggregation is not aligned to discrete month-level comparisons; the paper notes better performance when aggregation is discrete and task-aligned [@albersTaskdrivenEvaluationAggregation2014a].

## How to Check <!-- role: check -->

- **Visual Sign:** Users average by “eyeballing” the overall fill/line height across a month and frequently confuse high maxima with high averages.
- **The Test:** Run a quick internal test where max month and average month are intentionally different; if users pick the max month, the design isn’t supporting average comparisons [@albersTaskdrivenEvaluationAggregation2014a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a per-month mean mark or bar for each month.
- **Best Fix:** Use a composite design that overlays raw data with discrete monthly mean encoding (e.g., bars for monthly mean plus the raw line for context) [@albersTaskdrivenEvaluationAggregation2014a].
