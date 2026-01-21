---
id: use-box-plots-to-support-spread-comparisons-via-iqr
title: Use Box Plots to Support Spread Comparisons via IQR
bibliography: references.bib
description: Prefer box plots when users must compare month-to-month spread, because
  they explicitly encode dispersion (IQR) tied to the task.
labels:
- chart:box
- task:compare
- task:rank
- visual:position
- impact:accuracy
- data:temporal
- audience:novice
- source:albers-2014
---

## The Rule <!-- role: advice -->

For comparing spread across time blocks, use box plots so each block explicitly encodes dispersion (e.g., IQR) rather than forcing viewers to infer spread from raw traces.

## The Logic <!-- role: reason -->

Spread comparisons require judging variation among all points, which is hard from raw time-ordered data. Box plots encode a dispersion statistic (IQR) that serves as a strong proxy for the spread measure used in the paper (absolute deviation), reducing mental estimation.

- **The Principle:** Explicitly mapping a dispersion statistic improves accuracy on variability judgments.
- **The Evidence:** In the spread experiment, box plots outperformed all other tested encodings [@albersTaskdrivenEvaluationAggregation2014a].

## Where to Apply <!-- role: context -->

- **User Goal:** Choose which month’s values are most spread out from that month’s average.
- **Data Type:** Time series segmented into comparable blocks (months).
- **Audience:** Users who need reliable comparative variability judgments.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The user needs to see the raw temporal pattern or shape within each month (trend/sequence).
- **Reason:** Box plots remove within-block temporal order and can hide important time-dependent structure [@albersTaskdrivenEvaluationAggregation2014a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Loss of detail about when within the month variation occurs.
- **The Risk:** Users may over-trust IQR as “the whole story” and miss multimodality or structured patterns that raw traces would reveal [@albersTaskdrivenEvaluationAggregation2014a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a raw line graph and asking viewers to judge “spread” by eyeballing jaggedness.
- **Why it fails:** Jaggedness/noise and extremes can confound perceived spread; the paper notes the need to decorrelate range and spread because people confuse them [@albersTaskdrivenEvaluationAggregation2014a].

## How to Check <!-- role: check -->

- **Visual Sign:** Users confuse “largest range” with “most spread.”
- **The Test:** Use stimuli where the month with largest range is not the month with largest spread; if users still pick the range month, add an explicit dispersion encoding (like IQR) [@albersTaskdrivenEvaluationAggregation2014a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a per-month dispersion glyph or summary (e.g., box) beside the existing time series.
- **Best Fix:** Replace the main view with per-month box plots when spread comparison is primary, optionally paired with a separate raw-series view for context [@albersTaskdrivenEvaluationAggregation2014a].
