---
id: avoid-luminance-and-orientation-for-least-bias-at-eight-values
title: Avoid luminance and orientation when minimizing bias in immediate recall of
  eight values
bibliography: references.bib
description: For immediate recall of eight values, length and bar-position showed
  less bias than luminance and orientation.
labels:
- chart:heatmap
- chart:bar
- chart:line
- task:retrieve
- visual:color
- visual:orientation
- visual:length
- visual:position
- impact:bias
- data:quantitative
- audience:general
- complexity:advanced
---

## Prefer length or bar-position over luminance/orientation to minimize bias for 8-value recall <!-- role: advice -->

When viewers must reproduce eight quantitative values immediately after a brief view and your priority is minimizing systematic bias, prefer a length encoding or a bar-position encoding over luminance or orientation encodings.

## Why some encodings reduce bias for high mark counts <!-- role: reason -->

With larger numbers of marks, memory-based reproduction becomes more error-prone, and choosing an encoding can meaningfully shift systematic bias even if no encoding fully solves the memory load.

**Mechanism:** Certain encodings can produce reproduced values that deviate less systematically from true values, even under high memory load.

**Evidence:** For the retrieve-value reproduction task with 8 marks, length (E-23) ranked best (least biased), and bar-position (E-19) was also less biased than luminance (E-21) and orientation (E-24) with significant pairwise differences reported (E-19 better than E-22 and E-24; E-21 better than E-24; E-23 better than E-22 and E-24) under a Bayesian threshold of 0.9 [@mccolemanRethinkingRanksVisual2022; @zengReviewCollationGraphical2023].

**Notes:** This guideline is specifically about bias; other measures (like absolute error) may behave differently.

## Where this bias-minimization guidance applies <!-- role: context -->

- **User Goal:** Reproduce many values with minimal systematic over/underestimation.
- **Task:** Retrieve Value (immediate reproduction from memory).
- **Data:** Quantitative values with 8 marks.
- **Chart Setting:** Brief exposure, then redraw/reproduce.
- **Audience:** General audiences.
- **Success Criterion:** Lower bias across reproduced marks.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The task is not recall-based (viewers can keep the chart visible while answering). **Why:** The evidence is derived from a memory reproduction paradigm rather than persistent reading.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Length encodings without a shared baseline may be harder to interpret in some conventional analysis settings. **Risk:** Even the “best” bias option may still yield unacceptable overall error with eight values due to memory limits. **Mitigation:** Reduce the number of values that must be recalled at once or provide ways to re-check values.

## Common mistakes <!-- role: mistakes -->

**Mistake:** Assuming that switching encodings will fully fix poor performance with eight marks. **Why it fails:** The evidence indicates mark count strongly impacts performance, so encoding changes alone may not overcome memory constraints.

## Quick checks <!-- role: check -->

**Failure Sign:** Users consistently drift high or low when reproducing many values, regardless of effort. **Quick Check:** Compare mean signed error (bias) across candidate encodings with an eight-value recall task. **Stronger Test:** Evaluate both bias and absolute error distributions for your target dataset and viewing duration.

## What to do instead <!-- role: fix -->

- Use a length encoding if your primary objective is minimizing bias under eight-value immediate recall.
- Use a bar-position encoding if you need a position-based alternative that also reduces bias relative to luminance/orientation in this setting.
- Decompose the task so users recall fewer values per view (e.g., split into smaller groups).
- Provide a workflow that does not require immediate recall of all eight values (e.g., allow revisiting the view).
