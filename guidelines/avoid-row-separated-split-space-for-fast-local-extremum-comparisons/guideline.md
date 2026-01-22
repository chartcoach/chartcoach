---
id: avoid-row-separated-split-space-for-fast-local-extremum-comparisons
title: Avoid row-separated split-space designs when speed is critical for local find-extremum
  comparisons
bibliography: references.bib
description: Row-separated split-space designs were slower than alternatives for local
  max-at-a-point judgments.
labels:
- chart:line
- task:compare
- visual:facet
- impact:speed
- data:temporal
- audience:expert
- complexity:intermediate
---

## Avoid row-separated panels for local max-at-a-point tasks <!-- role: advice -->

Avoid splitting series into separate rows when the task is to identify the maximum series at a single time point and speed is important. Choose an alternative that does not require scanning across multiple rows for the comparison.

## Why row-separated panels slow local point comparisons <!-- role: reason -->

Local max-at-a-point comparisons benefit from a single shared reference at the queried time; separating series forces vertical scanning and mental alignment.

**Mechanism:** Cross-panel comparisons add attentional travel and increase the effort to align values that share the same time coordinate.

**Evidence:** For the find-extremum task, row-separated designs (E-3 and E-4) were slower than the fastest designs (E-1 and E-2), with significant pairwise differences indicating E-1 and E-2 were faster than E-3 and E-4. [@javedGraphicalPerceptionMultiple2010] This pattern is captured as part of a collated knowledge base intended to support visualization recommendation. [@zengReviewCollationGraphical2023]

**Notes:** This is a performance guideline about time, not a claim that row-separated designs are always inaccurate.

## When this applies in multi–time series views <!-- role: context -->

- **User Goal:** Quickly determine which series is highest at a specified time.
- **Task:** find-extremum.
- **Data:** Multiple categorical series; quantitative values; ordered time.
- **Chart Setting:** Static chart with a single queried time point; viewers must answer quickly.
- **Audience:** Analysts doing quick comparisons.
- **Success Criterion:** Minimize completion time.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The task is an aggregate judgment or requires scanning across the whole time window. **Why:** Row-separated split-space designs can be faster for aggregate tasks under the tested conditions.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Avoiding row separation may increase overlap between series in a shared view. **Risk:** Higher overlap can harm series identification. **Mitigation:** If overlap becomes problematic, reduce the number of displayed series for the task.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using small multiples (row-separated) as a default for any multi-series time chart. **Why it fails:** For local find-extremum comparisons, the tested row-separated approaches were slower than alternatives.

## Quick tests <!-- role: check -->

**Failure Sign:** Users compare rows one-by-one instead of making a direct decision at the time point. **Quick Check:** In a quick hallway test, see whether users need to look at every row before answering. **Stronger Test:** Time the same find-extremum prompt across layouts with the same series count.

## What to do instead <!-- role: fix -->

- Use a shared-space view so the compared values are co-located at the queried time.
- Add a clear visual cue for the queried time point (e.g., a vertical guide) to support direct comparison.
- Reduce the number of series in view for the find-extremum question.
- If you must use split space, avoid configurations that separate series into many rows for this task.
