---
id: use-position-encodings-for-point-extrema-comparisons
title: Use position encodings for point extrema comparisons (maxima and minima)
bibliography: references.bib
description: Prefer position-based time series displays when users must find which
  interval contains the highest or lowest single data point.
labels:
- chart:time-series
- task:locate
- visual:position
- impact:accuracy
- data:temporal
- audience:general
- complexity:basic
---

## Prefer position for locating maxima/minima across intervals <!-- role: advice -->

Use a position-based encoding (such as a line-based time series view) when the task is to identify which interval contains the single highest or lowest value.

## Why position improves point-extrema judgments <!-- role: reason -->

Point-extrema tasks require extracting and comparing individual values across intervals. Position provides higher perceptual fidelity for such point comparisons than color-based value encodings, which makes exact-value extraction harder.

**Mechanism:** Position supports more precise discrimination of individual values, so locating the single most extreme point is more reliable.

**Evidence:** Across tasks that asked which month contained the day with the highest or lowest sales, position-based encodings were generally more accurate than color-based encodings, consistent with point-comparison advantages for position [@albersTaskdrivenEvaluationAggregation2014a].

**Notes:** Encoding extrema explicitly can help within each visual channel, but does not fully remove the point-extraction disadvantage of color.

## When point-extrema guidance applies <!-- role: context -->

- **User Goal:** Determine which interval contains the most extreme single observation.
- **Task:** Locate-and-compare maxima or minima across fixed temporal bins (e.g., months).
- **Data:** Dense time series where single-day peaks/troughs matter.
- **Chart Setting:** Static view or limited time-to-view; no guarantee of interactive inspection.
- **Audience:** Mixed statistical literacy; needs to answer from the graphic.
- **Success Criterion:** Higher answer accuracy for which interval contains the extreme point.

## When not to follow this <!-- role: exceptions -->

**Break it when:** The user is comparing summary properties (such as mean or spread) rather than individual points. **Why:** Position-based line views were not consistently best for summary comparison tasks in the evaluated set [@albersTaskdrivenEvaluationAggregation2014a].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Position views can make summary judgments less direct when the statistic is not explicitly encoded.\
**Risk:** Users may shift to a wrong-but-easy strategy (e.g., choosing the interval with the highest average) if the display encourages it.\
**Mitigation:** Align the display with the intended statistic when summary judgments are primary.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using a colorfield-like encoding for maxima/minima location without any positional cue. **Why it fails:** Color-based encodings were less accurate for locating extreme individual points in the tested tasks [@albersTaskdrivenEvaluationAggregation2014a].

## Quick tests <!-- role: check -->

**Failure Sign:** People hesitate and frequently disagree on which interval contains the single highest/lowest point.\
**Quick Check:** Ask a few readers to answer “which interval contains the highest day” from a static image; frequent mismatches indicate point extraction is too hard.\
**Stronger Test:** Run a small accuracy pilot across candidate encodings using the same tasks and interval granularity.

## What to do instead <!-- role: fix -->

- Use a position-based time series view when point extrema must be found reliably.
- If you must use color, switch to a design that explicitly encodes per-interval extrema rather than raw point colors.
- If users need both point extrema and summaries, use a composite design that preserves a positional trace while adding task-relevant summaries.
