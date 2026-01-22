---
id: prefer-discrete-clicks-over-continuous-mouse-movements-in-bubbleview-to-reduce-noise
title: Prefer discrete BubbleView clicks over continuous mouse movements to reduce
  trajectory noise
bibliography: references.bib
description: Use clicks instead of continuous mouse tracking to avoid transition-path
  artifacts and reduce post-processing.
labels:
- chart:other
- task:measure-attention
- visual:interaction
- impact:data-quality
- data:behavioral
- audience:researcher
- method:bubbleview
---

## Use clicks to capture points of interest directly <!-- role: advice -->

Collect discrete BubbleView clicks rather than continuous mouse movements when your goal is a clean set of points of interest without heavy post-processing.

## Why continuous movement adds transition artifacts <!-- role: reason -->

Continuous cursor traces include both dwell-like behavior and movement between targets, so the raw data contains many samples that do not correspond to stable attention points. Clicks add an effort barrier that encourages selectivity and directly records intentional inspection locations.

**Mechanism:** Clicks sample intentional targets; movements sample both targets and transitions, which inflates noise unless thresholds or segmentation are applied.

**Evidence:** BubbleView clicks produced cleaner, more consistent data than movement-based approaches and performed better than SALICON mouse movements for feasible participant counts when predicting fixation locations on a natural-image dataset [@kimBubbleViewInterfaceCrowdsourcing2017]. Movement traces visibly include path artifacts between regions, motivating additional post-processing that clicks avoid [@kimBubbleViewInterfaceCrowdsourcing2017].

**Notes:** The tradeoff is that clicking is slower than moving, so fewer locations may be sampled per unit time.

## When this guideline applies <!-- role: context -->

- **User Goal:** Build aggregate importance maps or approximate fixations with minimal cleaning.
- **Task:** Free-viewing or task-guided exploration on static images.
- **Data:** Any image type where transition traces would be misleading as “attention.”
- **Chart Setting:** Crowdsourcing where you want to minimize analysis complexity.
- **Audience:** Participants using a mouse/trackpad.
- **Success Criterion:** Stable hotspots with low noise and minimal preprocessing.

## When not to prefer clicks <!-- role: exceptions -->

**Break it when:** You need higher spatial coverage within very short per-image time budgets. **Why:** Continuous movement can sample more locations quickly, though it may require additional processing to extract points of interest [@kimBubbleViewInterfaceCrowdsourcing2017].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Clicking increases task time relative to movement-based exploration. **Risk:** Clicks may under-sample regions that would receive quick glances in natural viewing. **Mitigation:** Increase viewing time or participants if coverage is insufficient [@kimBubbleViewInterfaceCrowdsourcing2017].

## Common failure modes <!-- role: mistakes -->

**Mistake:** Treating raw mouse-movement paths as equivalent to fixations without segmentation. **Why it fails:** Transitions between targets appear as data and can distort the estimated importance distribution [@kimBubbleViewInterfaceCrowdsourcing2017].

## Quick tests <!-- role: check -->

**Failure Sign:** Heatmaps show streaks or elongated trails that follow plausible cursor paths rather than localized targets. **Quick Check:** Visualize a few individual participant traces to see whether transitions dominate. **Stronger Test:** Compare fixation-prediction performance using clicks versus movements at the same participant count on a pilot [@kimBubbleViewInterfaceCrowdsourcing2017].

## What to do instead <!-- role: fix -->

- Use discrete clicks when you want points of interest without post-processing.
- If you use movements, apply a method to discretize trajectories into interest points before analysis.
- Increase task time when switching from movements to clicks so participants can inspect enough regions.
- Monitor for trajectory artifacts during data collection and adjust interaction mode if needed [@kimBubbleViewInterfaceCrowdsourcing2017].
