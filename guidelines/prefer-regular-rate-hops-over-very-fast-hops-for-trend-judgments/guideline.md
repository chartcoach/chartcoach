---
id: prefer-regular-rate-hops-over-very-fast-hops-for-trend-judgments
title: Prefer Regular-Rate HOPs (~400 ms per Sample) Over Very Fast HOPs for Trend
  Judgments
bibliography: references.bib
description: HOPs improved trend judgments most reliably at a moderate frame rate;
  very fast frame rates reduced or weakened the benefit.
labels:
- chart:time-series
- task:classify
- visual:animation
- impact:accuracy
- data:temporal
- audience:novice
- uncertainty:sampling
- parameter:frame-rate
---

## Use a moderate HOP frame rate when viewers must integrate uncertainty over time <!-- role: advice -->

Set Hypothetical Outcome Plot (HOP) playback to a moderate rate where each sample is visible long enough to be cognitively registered (around 400 ms per sample). Avoid extremely fast HOP playback (around 100 ms per sample) for this task.

## Why HOP speed affects decision performance <!-- role: reason -->

The trend-judgment benefit depends on the viewer extracting and integrating information across many sampled frames. If frames change too quickly, the viewer may not form stable impressions of each sample, weakening the perceptual evidence they can accumulate.

**Mechanism:** Moderate pacing supports temporal integration of sample outcomes; overly rapid pacing can exceed limits on processing dynamic ensembles for this decision task.

**Evidence:** Regular-rate line HOPs (400 ms/sample) produced reliably lower JNDs than static line ensembles in the trend inference task, while fast HOPs (100 ms/sample) showed a smaller, unreliable improvement relative to line ensembles [@kaleHypotheticalOutcomePlots2019].

**Notes:** The study evaluated only two frame rates for line HOPs; the evidence supports “moderate beats very fast” within that tested range [@kaleHypotheticalOutcomePlots2019].

## When you are tuning HOP parameters for public-facing uncertainty communication <!-- role: context -->

- **User Goal:** Judge which candidate trend is more likely given noisy temporal data.
- **Task:** Repeated perceptual decisions supported by an uncertainty display that must be watched.
- **Data:** Time series outcomes drawn from distributions with sampling error.
- **Chart Setting:** Animated uncertainty display intended to be observed for multiple frames.
- **Audience:** Untrained viewers who may not patiently scrutinize every frame.
- **Success Criterion:** More reliable sensitivity to evidence across viewers (fewer low-sensitivity users).

## When deviating from moderate pacing is reasonable <!-- role: exceptions -->

**Break it when:** The goal is to test limits of ensemble processing rather than maximize judgment accuracy. **Why:** Very fast playback can be useful as an experimental manipulation even if it reduces practical decision performance [@kaleHypotheticalOutcomePlots2019].

## Tradeoffs of slowing HOPs down to moderate rates <!-- role: costs -->

**Sacrifice:** You increase time-on-task because viewers need to watch longer to see enough samples. **Risk:** Slower playback can frustrate impatient viewers, reducing attention. **Mitigation:** Keep the number of required frames reasonable for the context.

## Common frame-rate mistakes for HOPs <!-- role: mistakes -->

**Mistake:** Selecting the fastest possible playback to “reduce time” without testing comprehension. **Why it fails:** The fast HOP condition showed attenuated, unreliable gains compared to static ensembles for the same task [@kaleHypotheticalOutcomePlots2019].

## Checks for whether HOP speed is too fast <!-- role: check -->

**Failure Sign:** Users report guessing or appear to respond without watching multiple frames. **Quick Check:** Ask viewers to describe what varies from frame to frame; inability to do so suggests the pace is too fast. **Stronger Test:** Compare psychometric-function JNDs across candidate frame rates and choose the rate that lowers JND most consistently [@kaleHypotheticalOutcomePlots2019].

## What to do if you must run HOPs faster <!-- role: fix -->

- Reduce the number of visual elements per frame so each sample is easier to parse at speed.
- Use a static line ensemble instead of a very fast HOP if animation cannot be slowed.
- Provide controls to pause or scrub frames so viewers can self-pace.
- Increase per-sample dwell time while reducing transition emphasis to keep overall animation tolerable.
