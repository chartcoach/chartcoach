---
id: treat-pie-and-donut-as-equally-accurate-for-percentage-retrieval
title: Treat pie and donut charts as equally accurate for retrieving a percentage
  value
bibliography: references.bib
description: For reading a single part-to-whole percentage, donuts performed about
  as accurately as pies.
labels:
- chart:pie
- chart:donut
- task:retrieve-value
- impact:accuracy
- data:quantitative
- audience:general
- comparison:between-chart-variants
---

## Choose pie or donut interchangeably when accuracy is the main concern <!-- role: advice -->

When the task is to read a single percentage value, you can use either a pie chart or a donut chart without expecting a meaningful accuracy difference.

## Removing the center does not measurably harm percent readout accuracy <!-- role: reason -->

A donut removes the central meeting point of wedge boundaries, but viewers can still rely on remaining cues (such as arc length and area) to estimate the percentage, yielding similar accuracy.

**Mechanism:** The visual system can estimate the proportion without needing the exact center-point angle intersection, as long as the segment remains a coherent wedge on a circle.

**Evidence:** In a percentage retrieval task, the baseline donut and baseline pie showed essentially the same accuracy (reported as approximately no different in ordering), and the donut ranked at least as well as the pie in the recorded accuracy ranking. [@skauArcsAnglesAreas2016; @zengReviewCollationGraphical2023]

**Notes:** This equivalence is about accuracy for retrieving a value, not about performance for multi-slice comparison or other analytic tasks.

## Where this applies: part-to-whole value readout in a radial chart <!-- role: context -->

- **User Goal:** Read off a single part-to-whole percentage.
- **Task:** Retrieve value.
- **Data:** A highlighted quantitative portion against the remaining portion.
- **Chart Setting:** Static chart where the viewer reports the percentage.
- **Audience:** General audiences.
- **Success Criterion:** Comparable estimation accuracy between design variants.

## When not to follow it <!-- role: exceptions -->

**Break it when:** You need to compare multiple nested rings or make cross-ring comparisons. **Why:** This guideline only covers single-ring pie vs donut accuracy for retrieving one percentage, not multi-ring designs.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Treating them as interchangeable may ignore layout needs (e.g., whether you need a center space). **Risk:** You might assume the equivalence extends to other tasks beyond value retrieval. **Mitigation:** Re-check the task type before reusing the choice rule.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Avoiding donut charts solely because you assume removing the center necessarily reduces readout accuracy. **Why it fails:** The recorded results show baseline donut accuracy is about the same as baseline pie for percentage retrieval. [@skauArcsAnglesAreas2016; @zengReviewCollationGraphical2023]

## Quick tests <!-- role: check -->

**Failure Sign:** Stakeholders claim the donut “must be less precise” without task-specific evidence. **Quick Check:** Substitute a donut for a pie (or vice versa) and spot-check percent readouts with a few viewers. **Stronger Test:** A/B test pie vs donut on the same values and compare absolute error.

## What to do instead <!-- role: fix -->

- If you need the center for a label or KPI, use a donut and place the annotation in the hole.
- If you do not need the center space, select pie or donut based on layout and aesthetics rather than assumed accuracy differences.
- Keep the proportion depiction simple (single highlighted segment vs remainder) when the goal is pure value retrieval.
