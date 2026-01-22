---
id: use-optimizer-generated-scatterplot-presets-to-match-cluster-accuracy
title: Use optimizer-generated scatterplot presets when class/cluster judgments must
  match common software-default accuracy
bibliography: references.bib
description: For cluster/class-related judgments, optimizer-generated scatterplots
  can achieve accuracy comparable to MATLAB, R, and prior-study presets.
labels:
- chart:scatter
- task:cluster
- visual:position
- impact:accuracy
- data:quantitative
- audience:novice
- complexity:advanced
---

## Cluster/class judgment accuracy parity with common defaults <!-- role: advice -->

Use an optimizer-generated scatterplot preset when you need cluster/class judgments from a scatterplot and want accuracy comparable to typical MATLAB, R, or prior-study defaults.

## Why cluster/class accuracy can be comparable across presets <!-- role: reason -->

If the scatterplot uses the same positional encodings for the two quantitative axes, multiple reasonable renderings can support similar accuracy for cluster/class-related judgments, enabling an optimizer to provide a viable default without manual design work.

**Mechanism:** Position encodings preserve spatial grouping cues that can remain usable across different parameter presets.

**Evidence:** In cluster tasks, accuracy rankings placed the optimizer-generated design in the same performance group as MATLAB, R, and a prior-study scatterplot preset, with no significant pairwise differences reported at the specified threshold [@micallefPerceptualOptimizationVisual2017; @zengReviewCollationGraphical2023].

**Notes:** This guideline does not claim that any one preset improves cluster accuracy beyond the others.

## When cluster/class accuracy parity applies <!-- role: context -->

- **User Goal:** Make a correct cluster/class-related judgment from a scatterplot without hand-tuning design parameters.
- **Task:** Cluster.
- **Data:** Two quantitative attributes (with points potentially belonging to groups/classes).
- **Chart Setting:** Static scatterplot with point marks and linear position scales.
- **Audience:** Non-experts using defaults/presets.
- **Success Criterion:** Comparable accuracy across presets.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Completion time is the main constraint and you can choose a faster preset without harming accuracy. **Why:** Time differences can exist even when accuracy is comparable.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may accept no accuracy gain relative to existing defaults. **Risk:** Overfitting your expectation to one dataset type can reduce generalization. **Mitigation:** Test on multiple representative datasets before standardizing on a single preset.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Treating an optimizer-generated preset as a guarantee of better cluster accuracy. **Why it fails:** The reported results show cluster accuracy parity, not superiority.

## Quick tests <!-- role: check -->

**Failure Sign:** Users report that groups “blend together” and give inconsistent answers. **Quick Check:** Run a small set of cluster questions comparing your default and the optimizer preset and check whether accuracy differs meaningfully. **Stronger Test:** Use a within-subjects study measuring both accuracy and time on representative datasets.

## What to do instead <!-- role: fix -->

- Keep your existing default if it already matches your product constraints, and use the optimizer preset as an optional alternative.
- Evaluate multiple presets with your users when time-to-answer matters in addition to correctness.
- If the task is actually anomaly finding rather than clustering, switch to a preset optimized for anomaly finding and re-test.
