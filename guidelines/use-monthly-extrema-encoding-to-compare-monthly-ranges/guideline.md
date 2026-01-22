---
id: use-monthly-extrema-encoding-to-compare-monthly-ranges
title: Use an encoding that explicitly shows monthly minima and maxima to compare
  monthly ranges
bibliography: references.bib
description: "For month-level range comparisons, explicitly encode each month\u2019\
  s minimum and maximum to improve accuracy."
labels:
- chart:line
- chart:boxplot
- task:determine-range
- visual:position
- impact:accuracy
- data:temporal
- audience:general
- granularity:monthly
---

## Encode monthly minima and maxima to support monthly range comparisons <!-- role: advice -->

Use a time-series design that explicitly encodes each month’s minimum and maximum when viewers must pick the month with the largest range.

## Why explicit month-level extrema support range judgments <!-- role: reason -->

Range is a comparison of two extreme values per month, so making those extremes explicit reduces the need to hunt for them and mentally subtract.

**Mechanism:** By exposing both endpoints (min and max) as clear marks per month, the viewer can compare ranges more directly across months.

**Evidence:** For the monthly range task (determine-range), the modified stock chart with explicit monthly extrema (E-2) ranked highest, and designs that explicitly encoded extrema (including E-2 and the box-plot design E-3) significantly outperformed designs that did not. [@albersTaskdrivenEvaluationAggregation2014; @zengReviewCollationGraphical2023]

**Notes:** The evidence here is about accuracy for selecting the correct month, not estimating the numeric range.

## When users must choose the month with the largest spread between max and min <!-- role: context -->

- **User Goal:** Identify which month has the largest difference between its highest and lowest day.
- **Task:** Determine range across discrete time windows.
- **Data:** Temporal quantitative values grouped into months (or another fixed window).
- **Chart Setting:** Static; aggregation window is known and stable.
- **Audience:** General audiences doing comparative judgments.
- **Success Criterion:** Higher accuracy for selecting the correct month.

## When not to rely on extrema-based range displays <!-- role: exceptions -->

**Break it when:** The task is about variability across all points (not just endpoints). **Why:** Range ignores internal distribution, so an extrema-focused design can misrepresent what “variation” means for the viewer’s question.

## Tradeoffs of explicit extrema for range <!-- role: costs -->

**Sacrifice:** Additional computed marks per month (more ink and complexity).\
**Risk:** Viewers may conflate range with other concepts like typical variability if only endpoints are emphasized.\
**Mitigation:** Ensure the task prompt clearly defines range as max-minus-min.

## Common range-comparison mistakes <!-- role: mistakes -->

**Mistake:** Asking viewers to infer the largest month range from a dense raw line without explicit extrema. **Why it fails:** Designs without explicit extrema ranked lower in accuracy for the range task.

## Quick tests for range legibility <!-- role: check -->

**Failure Sign:** People answer based on the highest peak rather than the max-minus-min span.\
**Quick Check:** Ask a few readers to explain their strategy; if they mention only maxima, range is not being supported.\
**Stronger Test:** Pilot two encodings and measure accuracy on the “largest range month” question.

## What to do instead if extrema encoding is not available <!-- role: fix -->

- Use a per-month summary chart that explicitly represents spread between min and max.
- Add annotations that highlight each month’s min and max points on the raw series.
- Split the task into two steps: identify candidate months by maxima/minima, then compare ranges among candidates.
