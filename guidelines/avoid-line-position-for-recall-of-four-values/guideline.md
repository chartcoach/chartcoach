---
id: avoid-line-position-for-recall-of-four-values
title: Avoid line-position encoding when viewers must recall four quantitative values
bibliography: references.bib
description: In immediate recall of four values, line-position had the worst accuracy
  among tested encodings.
labels:
- chart:line
- task:retrieve
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- complexity:advanced
---

## Avoid line-position for 4-value immediate recall <!-- role: advice -->

When viewers must reproduce four quantitative values immediately after a brief view, avoid using line chart position encoding as the primary quantitative channel.

## Why line-position can hurt 4-value recall accuracy <!-- role: reason -->

In a reproduction-from-memory setting, an encoding that is effective for other analytic tasks can still be poor for immediate recall of multiple individual values.

**Mechanism:** Line-position can yield less accurate memory-based reproductions than alternative encodings when multiple values must be held and reproduced.

**Evidence:** For the retrieve-value reproduction task with 4 marks, line-position (E-8) ranked last in accuracy, and multiple other encodings (including area (E-10), orientation (E-12), luminance (E-9), and bar-position (E-7)) were significantly more accurate than line-position under the Bayesian threshold of 0.9 [@mccolemanRethinkingRanksVisual2022; @zengReviewCollationGraphical2023].

**Notes:** This is a recall-oriented result and does not claim line charts are ineffective for trend or shape judgments.

## Where this applies <!-- role: context -->

- **User Goal:** Accurately reproduce four individual values after a glance.
- **Task:** Retrieve Value (immediate reproduction from memory).
- **Data:** Quantitative values with 4 marks.
- **Chart Setting:** Brief exposure with a mask/blank interval and then redraw.
- **Audience:** General audiences.
- **Success Criterion:** Higher reproduction accuracy.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The user’s goal is understanding relative change patterns rather than recalling exact values. **Why:** The measured outcome is immediate value reproduction accuracy, not pattern comprehension.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Avoiding line-position may reduce familiarity for time-series presentations. **Risk:** Alternative encodings may introduce their own interpretation challenges in real-world settings. **Mitigation:** Match the encoding to whether the user must recall exact values or only compare shapes.

## Common mistakes <!-- role: mistakes -->

**Mistake:** Concluding that line charts are categorically inaccurate for quantitative communication. **Why it fails:** The evidence comes from a specific recall-and-reproduce task under brief viewing constraints.

## Quick checks <!-- role: check -->

**Failure Sign:** Users can describe the overall shape but cannot accurately reproduce the individual values. **Quick Check:** Run a quick recall test where users redraw four values after a brief look and compare absolute error across encodings. **Stronger Test:** Replicate the timing and masking conditions of your intended usage and evaluate accuracy distributions.

## What to do instead <!-- role: fix -->

- Use a bar-position encoding when recall of individual values is required.
- Use an area or luminance encoding if recall performance is the primary success criterion and your audience can interpret them in your context.
- Use an orientation encoding if it is supported by your chart semantics and can be interpreted consistently.
- Reduce the number of values that must be remembered at once if the workflow allows chunking.
