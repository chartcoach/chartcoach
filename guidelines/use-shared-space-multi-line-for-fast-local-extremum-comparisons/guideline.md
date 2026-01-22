---
id: use-shared-space-multi-line-for-fast-local-extremum-comparisons
title: Use shared-space multi-line charts for faster local find-extremum judgments
  across multiple time series
bibliography: references.bib
description: For finding which series is highest at a specific time, shared-space
  designs were among the fastest options.
labels:
- chart:line
- task:compare
- visual:position
- impact:speed
- data:temporal
- audience:expert
- complexity:intermediate
---

## Shared-space for local extrema across series <!-- role: advice -->

Use a shared-space multi-line view when the task is to quickly identify which time series has the highest value at a single point in time. Prefer shared-space options over split-space layouts when speed is the priority.

## Why shared-space helps for local extrema <!-- role: reason -->

When series share the same plotting space, the viewer can compare values at one time position using a single aligned vertical reference, reducing the need to move attention between separate panels.

**Mechanism:** Co-located series support direct value comparison at the same x-position, which reduces cross-panel search and alignment effort.

**Evidence:** For the find-extremum task, shared-space and split-space designs were not equally fast: the shared-space line design (E-1) was in the fastest group along with one split-space design (E-2), and both were significantly faster than the row-separated split-space designs (E-3, E-4). [@javedGraphicalPerceptionMultiple2010] The guideline is derived via structured collation for visualization recommendation contexts. [@zengReviewCollationGraphical2023]

**Notes:** This guideline is about completion time, not accuracy; accuracy rankings differed.

## When this applies in multi–time series views <!-- role: context -->

- **User Goal:** Pick the series with the maximum value at a specific time instant.
- **Task:** find-extremum.
- **Data:** Multiple time series (each series is a category) with ordered time points and quantitative values.
- **Chart Setting:** Static chart; no interaction assumed; limited need to inspect long time spans.
- **Audience:** Analysts comfortable with line charts and multi-series comparisons.
- **Success Criterion:** Faster completion time while keeping accuracy acceptable.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The shared-space view becomes too hard to visually separate series (e.g., heavy overlap) and speed depends more on isolating each series than co-location. **Why:** This guideline only reflects the conditions tested; it does not guarantee performance under higher clutter than evaluated.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Shared-space layouts can reduce separability when many series overlap. **Risk:** Users may confuse which series they are comparing if identity cues are weak. **Mitigation:** Ensure series identity is legible (e.g., clear categorical encoding and labeling).

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using a split-space row-separated layout for a local max-at-a-point task by default. **Why it fails:** In the tested conditions, row-separated designs (E-3, E-4) were slower than the fastest designs for find-extremum.

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers spend time scanning up and down between panels before answering. **Quick Check:** Ask a colleague to answer “Which series is highest at time t?” and observe whether they can decide without shifting gaze across multiple small panels. **Stronger Test:** Time a small A/B test of shared-space vs row-separated small multiples on the same task.

## What to do instead <!-- role: fix -->

- Use a non-row-separated design that keeps comparisons co-located for the time point of interest.
- Reduce the number of concurrently displayed series (filter or select a subset) before asking for a maximum-at-a-time judgment.
- Add direct annotations at the queried time point (e.g., highlight the time slice and label candidates).
- Switch to a different technique only after verifying it improves time for your specific find-extremum prompt.
