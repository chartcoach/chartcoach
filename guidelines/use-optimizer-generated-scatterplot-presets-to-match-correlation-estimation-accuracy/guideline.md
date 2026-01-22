---
id: use-optimizer-generated-scatterplot-presets-to-match-correlation-estimation-accuracy
title: Use optimizer-generated scatterplot presets when correlation estimation accuracy
  must match common software defaults
bibliography: references.bib
description: For correlation estimation, optimizer-generated scatterplot designs can
  achieve accuracy comparable to MATLAB, R, and prior-study presets.
labels:
- chart:scatter
- task:correlate
- visual:position
- impact:accuracy
- data:quantitative
- audience:novice
- complexity:advanced
---

## Correlation estimation parity with common defaults <!-- role: advice -->

Use an optimizer-generated scatterplot preset when your goal is correlation estimation and you want accuracy comparable to typical MATLAB, R, or prior-study defaults.

## Why correlation estimation can be comparable across presets <!-- role: reason -->

When scatterplots keep the same core encoding (quantitative values on x/y position), some design-parameter variation can yield similar correlation-judgment accuracy across reasonable presets, so an optimizer can reach “good enough” performance without manual tuning.

**Mechanism:** Different presets can produce visually sufficient cues for correlation (global trend and spread) when the underlying positional encoding remains the same.

**Evidence:** In correlation tasks, accuracy rankings placed the optimizer-generated design in the same performance group as MATLAB, R, and a prior-study scatterplot preset, with no significant pairwise differences reported at the specified threshold [@micallefPerceptualOptimizationVisual2017; @zengReviewCollationGraphical2023].

**Notes:** This guideline is about matching accuracy, not about preferring any specific preset.

## When correlation-estimation parity applies <!-- role: context -->

- **User Goal:** Estimate linear association between two quantitative variables with acceptable correctness.
- **Task:** Correlate.
- **Data:** Two quantitative attributes.
- **Chart Setting:** Static scatterplot with point marks and linear position scales.
- **Audience:** Non-experts who need a reliable default without manual parameter tuning.
- **Success Criterion:** Accuracy parity with common software defaults.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Your primary success criterion is speed rather than correctness. **Why:** The evidence here establishes parity on accuracy for correlation, not superiority on completion time.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may give up stylistic consistency with an organization’s existing plotting defaults. **Risk:** Treating parity as superiority can lead to overconfidence in one preset. **Mitigation:** Validate with a small task-focused pilot if the decision stakes are high.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Assuming the optimizer-generated preset is always more accurate than MATLAB or R. **Why it fails:** The reported ranking shows no accuracy differences among these designs for correlation.

## Quick tests <!-- role: check -->

**Failure Sign:** Users disagree widely on whether the relationship is weak vs. moderate for the same plot. **Quick Check:** Compare a small set of correlation questions using your current default vs. the optimizer preset and look for large accuracy gaps. **Stronger Test:** Run a short within-subjects timing+accuracy test on representative datasets.

## What to do instead <!-- role: fix -->

- Run a small A/B test comparing your current default and the optimizer preset on correlation questions.
- If time is the dominant constraint, prioritize presets that reduce completion time for your context and device.
- Add minimal guidance (e.g., reference lines or annotations) only if your workflow allows it, then re-test correlation judgments.
