---
id: explicitly-encode-extrema-for-range-and-extrema-tasks
title: Explicitly encode per-interval extrema when users compare extrema or range
bibliography: references.bib
description: Add explicit per-bin minima and maxima encodings to improve accuracy
  for maximum, minimum, and range comparisons.
labels:
- chart:time-series
- task:compare
- visual:position
- visual:color
- impact:accuracy
- data:temporal
- audience:general
- complexity:intermediate
---

## Encode per-interval minima/maxima for extrema and range judgments <!-- role: advice -->

When users must compare maxima, minima, or ranges across intervals, use an encoding that explicitly shows the minimum and maximum for each interval instead of requiring viewers to infer them from raw traces.

## Why explicit extrema mappings help these tasks <!-- role: reason -->

Extrema and range tasks depend directly on knowing interval endpoints. Showing those endpoints reduces the amount of visual search and mental reconstruction needed, which improves comparison accuracy within both position- and color-based families.

**Mechanism:** Explicitly mapped extrema reduce cognitive and perceptual work by making the task-relevant statistics directly available at the interval level.

**Evidence:** For minima and range tasks, encodings that explicitly displayed local extrema outperformed other encodings within their visual-variable group (e.g., designs with per-month extrema versus those without) [@albersTaskdrivenEvaluationAggregation2014a]. For maxima, the one color-based encoding that explicitly encoded per-month maxima outperformed other color encodings [@albersTaskdrivenEvaluationAggregation2014a].

**Notes:** Explicit extrema do not guarantee top performance if the primary channel still limits discrimination (e.g., color for exact point values).

## When explicit extrema encoding applies <!-- role: context -->

- **User Goal:** Identify which interval has the highest point, lowest point, or largest gap between them.
- **Task:** Compare per-interval extrema or per-interval range.
- **Data:** Time series binned into meaningful intervals (e.g., months) where the within-bin extreme matters.
- **Chart Setting:** Static reporting or dashboards where users must answer without interaction.
- **Audience:** General audiences; cannot be assumed to compute extrema mentally.
- **Success Criterion:** Fewer errors on extrema/range comparisons across bins.

## When not to follow this <!-- role: exceptions -->

**Break it when:** Users need to inspect local shape, sequences, or specific non-extreme events within intervals. **Why:** Replacing raw data with only extrema can remove information needed for other judgments [@albersTaskdrivenEvaluationAggregation2014a].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may lose visibility into within-interval structure if you only encode extrema.\
**Risk:** Users may over-trust extrema summaries and miss important non-extreme patterns.\
**Mitigation:** Preserve access to the underlying series when additional tasks are likely.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Asking users to compare ranges using a display that does not make minima and maxima per interval visually salient. **Why it fails:** Range required comparing two points per interval, and displays without explicit extrema underperformed those that provided them [@albersTaskdrivenEvaluationAggregation2014a].

## Quick tests <!-- role: check -->

**Failure Sign:** Users frequently answer range questions as if they were maxima questions.\
**Quick Check:** Verify that the minimum and maximum for each interval are visually separable and easy to point to.\
**Stronger Test:** Pilot range questions and check whether accuracy increases when extrema are explicitly encoded.

## What to do instead <!-- role: fix -->

- Add explicit per-interval minima and maxima marks to the display.
- Use an interval-level summary form that directly encodes endpoints when range is a primary task.
- Keep a raw-data layer available if users also need to answer non-extrema questions.
