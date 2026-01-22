---
id: use-indexing-line-plots-for-higher-accuracy-than-log-superimposed
title: Use indexed (percent-based) line plots instead of superimposed log-scale line
  plots for more accurate multivariate time-series comparison tasks
bibliography: references.bib
description: Indexed (percent-based) line plots can yield better accuracy than superimposed
  log-scale line plots for multivariate time-series comparison tasks.
labels:
- chart:line
- task:compare
- visual:position
- impact:accuracy
- data:temporal
- audience:general
- scale:log
- transformation:indexing
---

## Prefer indexed line plots over log-scale superimposed line plots for accuracy <!-- role: advice -->

Use indexed (percent-based) line plots rather than superimposed log-scale line plots when your priority is accurate multivariate time-series comparisons.

## Why indexing improves correctness in this comparison <!-- role: reason -->

Indexing normalizes series into directly comparable percent units anchored to a chosen reference point, which can reduce interpretation errors when comparing across series.

**Mechanism:** A shared percent-based reference reduces ambiguity from comparing raw magnitudes across series, even when a log scale is used.

**Evidence:** In extracted results, indexed (percent-based) line plots ranked higher than the log-scale line-plot alternative on accuracy for correlate, aggregate, and overall comparisons (E-2 better than E-1 in all three), with the study reporting significance-testing procedures for these accuracy results. [@aignerBertinWasRight2011; @zengReviewCollationGraphical2023]

**Notes:** The extracted significance pairs list for these accuracy rankings was empty, so treat the direction as a ranking signal rather than a confirmed pairwise significant difference in this representation.

## When this applies to your visualization <!-- role: context -->

- **User Goal:** Make correct judgments when comparing multiple time-series.
- **Task:** Correlate; Aggregate.
- **Data:** Temporal sequences with multiple series.
- **Chart Setting:** Line charts where series are intended to be compared as relative change.
- **Audience:** General audiences doing analytical comparisons.
- **Success Criterion:** Higher accuracy (fewer errors).

## When not to follow it <!-- role: exceptions -->

**Break it when:** Users must read precise absolute values (in original units) from the y-axis. **Why:** Indexing changes the unit to percent-based values, which can conflict with absolute-value reading tasks.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Absolute magnitude information becomes less directly accessible from the plot. **Risk:** Users may incorrectly treat percent-indexed series as if they were still in original units. **Mitigation:** Clearly label the y-axis as an indexed percent scale and state the reference point used.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using indexing but failing to communicate what the index reference is (what equals 100%). **Why it fails:** Without a clear reference point, readers cannot reliably interpret the transformed values.

## Quick tests <!-- role: check -->

**Failure Sign:** Different readers give inconsistent answers to the same comparison question (e.g., which series changed more). **Quick Check:** Ask two readers to answer one correlate and one aggregate comparison; if answers diverge, try an indexed view. **Stronger Test:** A/B test an indexed view vs. a log-scale superimposed view using the same tasks and measure error rate.

## What to do instead <!-- role: fix -->

- Use an indexed (percent-based) line plot for the comparison view.
- If you must keep a log-scale view, provide an indexed toggle specifically for comparison tasks.
- If absolute value reading is the dominant task, keep the log-scale (or linear-scale) view and add separate summaries for relative change rather than transforming the primary chart.
