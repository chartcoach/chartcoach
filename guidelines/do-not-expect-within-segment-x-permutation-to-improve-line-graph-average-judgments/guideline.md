---
id: do-not-expect-within-segment-x-permutation-to-improve-line-graph-average-judgments
title: Do not rely on within-segment horizontal permutation to improve average-judgment
  accuracy in line graphs
bibliography: references.bib
description: Shuffling x-order within segments does not improve accuracy for maximum-average
  segment judgments in line graphs.
labels:
- chart:line
- task:compare
- visual:position
- impact:accuracy
- data:temporal
- audience:novice
- task:aggregate
- technique:permutation
---

## Avoid x-permutation as an accuracy fix for line graphs <!-- role: advice -->

Do not apply within-segment horizontal permutation of points in a line graph as a method to help users find the segment with the maximum average. Treat line-graph permutation as unlikely to improve average-judgment performance for this task.

## Why line-graph permutation does not help here <!-- role: reason -->

The studied permutation disrupts continuity without giving the viewer a new perceptual cue for averaging; it removes meaningful shape structure while leaving the task dependent on integrating vertical position across many points.

**Mechanism:** When the decision requires an average over time, breaking the temporal order inside a line does not create a stable “average signal” and may instead reduce useful structure that viewers could otherwise use as heuristics.

**Evidence:** In the maximum-average month task, ordered versus permuted line graphs showed no significant difference in overall performance, while permutation did improve performance for colorfields [@correllComparingAveragesTime2012a]. The significant interaction between display type and permutation indicates the benefit of permutation is specific to the colorfield encoding, not the line graph [@correllComparingAveragesTime2012a].

**Notes:** This guidance is about average-comparison performance, not other potential reasons to randomize order (which were not evaluated).

## When this warning applies <!-- role: context -->

- **User Goal:** Identify which segment has the highest average.
- **Task:** Forced-choice selection among fixed segments using a line chart.
- **Data:** Dense time series where within-segment values can be reordered without changing the set of values.
- **Chart Setting:** Static line graph used for summary judgment rather than point lookup.
- **Audience:** General viewers relying on the chart to make a single decision under time or attention limits.
- **Success Criterion:** Higher accuracy in selecting the highest-average segment.

## When you might ignore this warning <!-- role: exceptions -->

**Break it when:** Your goal is explicitly to remove within-segment temporal meaning to prevent trend-based interpretations, and accuracy on average selection is not the priority. **Why:** The tested outcome was correctness for average-based selection, not interpretive bias or narrative goals [@correllComparingAveragesTime2012a].

## Tradeoffs and risks of permuting line graphs anyway <!-- role: costs -->

**Sacrifice:** Loss of temporal continuity cues that many viewers rely on for understanding time series. **Risk:** The chart can become harder to interpret while not improving average-comparison accuracy. **Mitigation:** Separate “average comparison” from “trend reading” into different views.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Permuting a line graph and assuming it now supports “visual averaging” like a colorfield. **Why it fails:** The study observed no accuracy gain from permutation in the line graph condition for the average-selection task [@correllComparingAveragesTime2012a].

## Quick tests <!-- role: check -->

**Failure Sign:** The permuted line graph looks more chaotic but users are not more accurate at picking the correct segment. **Quick Check:** Show both versions to a few users and compare correctness and response time for the same stimuli. **Stronger Test:** Run a small randomized test with your real series and compute accuracy differences between ordered and permuted line graphs.

## What to do instead <!-- role: fix -->

- Use a colorfield when the primary task is selecting the maximum-average segment.
- If you must keep a line graph, add a separate per-segment average cue outside the line itself.
- Reduce within-segment noise or compress the data so the viewer integrates fewer points for the average judgment.
