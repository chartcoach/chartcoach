---
id: avoid-horizon-graphs-for-fast-time-series-similarity-search
title: Avoid horizon graphs when you need fast time-series similarity selection
bibliography: references.bib
description: Horizon graphs can be slower than other encodings for choosing the most
  similar time series among candidates.
labels:
- chart:horizon
- chart:line
- chart:heatmap
- task:cluster
- task:compare
- visual:color
- visual:position
- impact:speed
- data:temporal
- audience:novice
- complexity:intermediate
---

## Avoid horizon graphs when speed is the main success criterion <!-- role: advice -->

Avoid horizon graphs for similarity-based selection tasks when faster completion time is a primary requirement.

## Why horizon graphs can slow similarity decisions <!-- role: reason -->

Horizon graphs combine banding and color changes that can increase visual decoding work, slowing the process of judging similarity across candidates.

**Mechanism:** Band boundaries introduce additional discrete steps viewers must interpret, increasing cognitive load relative to single-trace position encodings or continuous colorfield scanning.

**Evidence:** In a time-series similarity-selection task, horizon graphs were slower than colorfields and also slower than line charts in completion time (bootstrap comparisons; horizon graphs ranked slowest) [@gogolouComparingSimilarityPerception2019; @zengReviewCollationGraphical2023].

**Notes:** This guidance is specifically about task completion time, not about space efficiency or other benefits of horizon graphs.

## When this applies to your visualization setting <!-- role: context -->

- **User Goal:** Make rapid similarity judgments among several candidate time series.
- **Task:** Similarity-based selection (recorded under a clustering-related task category).
- **Data:** Temporal quantitative sequences displayed together for comparison.
- **Chart Setting:** Static small-multiple presentation of query plus candidates.
- **Audience:** General audience or time-constrained analysts.
- **Success Criterion:** Lower decision time.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Vertical space is extremely constrained and you must compress many time series into a small height per series. **Why:** Horizon graphs may be chosen for layout constraints even if they cost time.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may give up compact, banded representations that can fit more series vertically. **Risk:** Switching away from horizon graphs can increase screen space needs. **Mitigation:** Use a scrollable or paginated layout if space is the binding constraint.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Choosing horizon graphs because they are compact, without checking decision speed. **Why it fails:** Compactness does not guarantee faster similarity judgments.

## Quick tests <!-- role: check -->

**Failure Sign:** Users take longer on horizon graphs and report difficulty recognizing patterns.\
**Quick Check:** Compare median completion time for a handful of representative trials across encodings.\
**Stronger Test:** Run a counterbalanced within-subject timing study on your own dataset.

## What to do instead <!-- role: fix -->

- Use colorfields to prioritize fast scanning for similarity.
- Use line charts to support slower but more shape-faithful comparisons.
- Offer an optional toggle between horizon graphs and line charts so users can choose based on the case.
