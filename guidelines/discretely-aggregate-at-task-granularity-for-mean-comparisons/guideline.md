---
id: discretely-aggregate-at-task-granularity-for-mean-comparisons
title: "Discretely aggregate at the task\u2019s interval granularity for mean comparisons"
bibliography: references.bib
description: Compute and show per-interval means as discrete units when users compare
  averages across bins like months.
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

## Aggregate means per interval when the question is per interval <!-- role: advice -->

If users must decide which interval has the highest average, show the mean computed per interval as a discrete value for each interval rather than relying on continuous smoothing.

## Why task-aligned discrete aggregation improves mean comparisons <!-- role: reason -->

Mean comparisons across bins are easiest when the visualization matches the binning used by the task. Discrete per-bin aggregation aligns the computation and the decision unit, reducing ambiguity introduced by continuous aggregates that blend across boundaries.

**Mechanism:** Task-aligned binning reduces boundary-crossing interference and makes per-interval comparisons direct.

**Evidence:** For average-comparison tasks, encodings that discretely aggregated by month (including explicit per-month averages or discrete blocked designs) outperformed encodings that did not provide task-aligned discrete aggregation [@albersTaskdrivenEvaluationAggregation2014a]. A design with discrete monthly averages outperformed a similar design using a continuous moving average for this task [@albersTaskdrivenEvaluationAggregation2014a].

**Notes:** Discrete blocking can improve average comparisons even when the mean is not explicitly encoded, if the design supports visual summarization within each block.

## When discrete mean aggregation applies <!-- role: context -->

- **User Goal:** Pick the interval with the highest average level.
- **Task:** Compare per-interval means (e.g., monthly average sales).
- **Data:** Dense observations within each interval; too many points for mental averaging.
- **Chart Setting:** Fixed interval questions (months, quarters) known at design time.
- **Audience:** General; limited statistical computation capacity under time constraints.
- **Success Criterion:** Higher accuracy on “which interval has higher average” questions.

## When not to follow this <!-- role: exceptions -->

**Break it when:** Users need averages at multiple unknown granularities in the same view. **Why:** Hard-coding one discrete granularity can misalign with other question scales [@albersTaskdrivenEvaluationAggregation2014a].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Flexibility to answer questions at other granularities without re-aggregation.\
**Risk:** Users may infer that only the chosen binning is meaningful.\
**Mitigation:** Provide mechanisms to switch aggregation granularity when multiple scales are important.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using a moving average overlay as the primary support for per-interval mean comparisons. **Why it fails:** Continuous averaging can blur interval boundaries and underperformed discrete monthly averages for monthly mean comparison [@albersTaskdrivenEvaluationAggregation2014a].

## Quick tests <!-- role: check -->

**Failure Sign:** Readers disagree about which interval has the highest average even when differences are moderate.\
**Quick Check:** Confirm that each interval has one clearly comparable mean value.\
**Stronger Test:** Compare accuracy on a small set of “highest average interval” questions between discrete and continuous aggregation designs.

## What to do instead <!-- role: fix -->

- Compute and display a single mean value per task-relevant interval.
- Use a composite design that keeps raw data visible while adding per-interval averages for direct comparison.
- If interval granularity is uncertain, offer an alternative view that supports multiple bin sizes rather than committing to one.
