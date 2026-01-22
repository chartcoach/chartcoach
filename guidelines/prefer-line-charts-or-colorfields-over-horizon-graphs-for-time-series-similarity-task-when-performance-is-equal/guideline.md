---
id: prefer-line-charts-or-colorfields-over-horizon-graphs-for-time-series-similarity-task-when-performance-is-equal
title: Prefer line charts or colorfields over horizon graphs when they are equally
  fast for time-series similarity selection
bibliography: references.bib
description: If line charts and colorfields tie on time, choose between them rather
  than using horizon graphs, which is slower.
labels:
- chart:line
- chart:heatmap
- chart:horizon
- task:cluster
- task:compare
- visual:color
- visual:position
- impact:speed
- data:temporal
- audience:novice
- complexity:intermediate
---

## Choose line charts or colorfields instead of horizon graphs when they are not slower <!-- role: advice -->

When line charts and colorfields perform about the same in completion time for similarity selection, pick either of them rather than using horizon graphs.

## Why this choice reduces time risk <!-- role: reason -->

If two encodings are statistically indistinguishable on time, selecting either avoids the slower option without requiring additional assumptions.

**Mechanism:** Choosing among time-equivalent encodings preserves speed while allowing you to optimize for other constraints (space, aesthetics) outside this rule.

**Evidence:** For one measured similarity-selection condition, line charts and colorfields were tied in completion time while both were faster than horizon graphs (pairwise bootstrap significance showed horizon graphs slower than both) [@gogolouComparingSimilarityPerception2019; @zengReviewCollationGraphical2023].

**Notes:** This rule applies only when your own setting matches the condition where LC and CF are time-equivalent.

## When this applies to your visualization setting <!-- role: context -->

- **User Goal:** Maintain fast similarity judgments while choosing an encoding.
- **Task:** Similarity-based selection (recorded under a clustering-related task category).
- **Data:** Temporal quantitative sequences; time is ordered.
- **Chart Setting:** Static comparison of one query and multiple candidate series.
- **Audience:** General audience or mixed experience.
- **Success Criterion:** Avoid slower completion time.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Your users must read exact magnitudes or specific waveform shapes as part of the decision. **Why:** In that case, speed parity is less important than representational fidelity.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** This rule does not tell you whether to pick line charts or colorfields; it only rules out horizon graphs under the time-equivalence condition. **Risk:** You may still pick an encoding that mismatches the intended similarity criterion. **Mitigation:** Validate the choice with a small task-focused pilot.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Treating “line charts and colorfields tie on time” as a universal truth across datasets and layouts. **Why it fails:** The evidence is condition-specific, and time can shift with design and data.

## Quick tests <!-- role: check -->

**Failure Sign:** Users are slower on horizon graphs in quick timing trials even when LC/CF seem comparable.\
**Quick Check:** Time 10–20 representative judgments with each encoding.\
**Stronger Test:** Run a counterbalanced within-subject study and compare confidence intervals for time.

## What to do instead <!-- role: fix -->

- Use line charts when you want position-based shape reading to remain primary.
- Use colorfields when you want fast scanning via color continuity across time.
- Provide both options as a toggle if different users or cases need different similarity cues.
