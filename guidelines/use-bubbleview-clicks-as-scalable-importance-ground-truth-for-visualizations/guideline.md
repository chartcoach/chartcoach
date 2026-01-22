---
id: use-bubbleview-clicks-as-scalable-importance-ground-truth-for-visualizations
title: Collect BubbleView clicks to approximate attention/importance for training
  on data visualizations
bibliography: references.bib
description: Use BubbleView (click-to-reveal on blurred images) to gather scalable
  crowd data correlated with eye fixations for visualizations.
labels:
- chart:hybrid
- task:collect
- visual:attention
- impact:scalability
- data:mixed
- audience:researcher
- method:crowdsourcing
---

## Collect BubbleView clicks to approximate importance for data visualizations <!-- role: advice -->

Use a BubbleView-style click-to-reveal task on blurred visualizations to collect crowd click maps as scalable supervision for importance prediction.

## Why BubbleView is effective supervision for importance models <!-- role: reason -->

Eye tracking is expensive at dataset scale, but BubbleView induces purposeful exploration by requiring users to reveal details through clicks, producing spatial click distributions that are related to where people look and what they treat as important.

**Mechanism:** Blurring removes fine detail, and the click-to-reveal interaction makes users sample regions they need to understand the visualization; aggregating clicks across people yields a stable importance-like map.

**Evidence:** BubbleView click maps on data visualizations were shown to be related to lab-collected eye fixation maps, and an FCN trained on BubbleView clicks produced predictions that were also representative of eye fixation patterns on test visualizations [@bylinskiiLearningVisualImportance2017].

**Notes:** The collected click maps can be blurred to match fixation-map formats for training/evaluation comparability.

## When BubbleView click collection fits <!-- role: context -->

- **User Goal:** Build training data for importance prediction when eye tracking is impractical.
- **Task:** Gather spatial supervision at scale across many visualization images.
- **Data:** Visualization images with legible text; diverse chart/infographic types.
- **Chart Setting:** Online crowdsourcing studies; limited lab resources; need hundreds to thousands of samples.
- **Audience:** Researchers and tool builders training learned importance models.
- **Success Criterion:** Click maps are stable across participants and correlate sufficiently with attention/fixation patterns to train useful predictors.

## When BubbleView is a poor substitute <!-- role: exceptions -->

**Break it when:** The goal is to model natural free-viewing fixation behavior without task-induced interaction effects. **Why:** Click-to-reveal can concentrate sampling differently than passive viewing (for example, more concentrated around text) [@bylinskiiLearningVisualImportance2017].

## Tradeoffs of BubbleView supervision <!-- role: costs -->

**Sacrifice:** You trade direct measurement (eye movements) for an interactive proxy. **Risk:** Click maps may emphasize different regions than fixations and may not assign uniform importance across whole elements. **Mitigation:** Evaluate both against click ground truth and, when available, against eye fixations on a held-out subset.

## Common failure modes in BubbleView data collection <!-- role: mistakes -->

**Mistake:** Treating raw clicks as directly comparable to element-level importance masks. **Why it fails:** Clicks may be non-uniform within an element and can differ from explicit importance annotations intended to weight whole elements [@bylinskiiLearningVisualImportance2017].

## Quick tests for BubbleView quality <!-- role: check -->

**Failure Sign:** Click maps cluster in a few arbitrary spots with little coverage of interpretable regions. **Quick Check:** Confirm users meaningfully explored by pairing the task with a description requirement and inspecting whether aggregated clicks cover explanatory text and key marks. **Stronger Test:** On a subset, compute similarity between click maps and available fixation maps.

## What to do instead if BubbleView is misaligned with your target <!-- role: fix -->

- Collect explicit importance annotations (for example, region masking) when you need element-uniform importance signals.
- Use a lab eye-tracking subset to calibrate whether click behavior matches your target viewing condition.
- Redesign the crowd task to better match the intended viewing goal (for example, adjust prompts or interaction constraints).
