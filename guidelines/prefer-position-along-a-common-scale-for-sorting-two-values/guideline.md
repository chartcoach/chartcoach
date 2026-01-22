---
id: prefer-position-along-a-common-scale-for-sorting-two-values
title: Prefer position along a common scale for sorting two values
bibliography: references.bib
description: For sort judgments of two values, position on a shared axis yields higher
  accuracy than length, angle, or area encodings.
labels:
- chart:generic
- task:sort
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- source:graphical-perception
---

## Prefer shared-axis position encodings for sort judgments <!-- role: advice -->

Use position on a shared axis (a common scale) to support sorting or ranking two quantitative values. Prefer shared-axis position over length, angle, or area encodings for this task.

## Why shared-axis position improves sorting accuracy <!-- role: reason -->

Shared-axis position reduces estimation steps because viewers can compare values directly against a single aligned scale, avoiding extra perceptual inference (such as translating lengths, angles, or areas into comparable magnitudes).

**Mechanism:** Aligning values to a common positional reference enables more precise comparison, which improves accuracy on sorting judgments.

**Evidence:** In a sort (proportional judgment) task, designs that rely on position along a common scale ranked as more accurate than designs using length, angle, or area encodings, with multiple significant pairwise differences favoring the best position-based designs [@heerCrowdsourcingGraphicalPerception2010]. This guidance is captured as an actionable ranking for visualization recommendation in a structured collation of graphical perception findings [@zengReviewCollationGraphical2023].

**Notes:** This guideline is about the encoding channel choice (position vs. others), not about aesthetic styling.

## When this applies to your chart choice <!-- role: context -->

- **User Goal:** Order, rank, or sort values by magnitude.
- **Task:** Sort.
- **Data:** Quantitative values where viewers must compare two marked values.
- **Chart Setting:** Static 2D charts where comparison is done visually from the marks.
- **Audience:** General audiences (including non-experts).
- **Success Criterion:** Higher accuracy in the ordering judgment.

## When not to follow it <!-- role: exceptions -->

**Break it when:** You cannot use a shared axis because the layout requires non-aligned comparisons (for example, the display format forces non-common baselines). **Why:** The rule depends on a common positional reference to enable direct comparison.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may give up compactness or a desired aesthetic if you must restructure the chart to maintain a common scale. **Risk:** If the shared axis becomes crowded or unclear, the accuracy benefit can be reduced. **Mitigation:** Keep the axis readable and avoid unnecessary visual clutter.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Encoding the values as area or angle when the viewer needs to sort them. **Why it fails:** Viewers must infer magnitude from less precise cues, reducing sorting accuracy compared to shared-axis position.

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers hesitate or disagree when asked “which is larger?” for the two highlighted values. **Quick Check:** Ask someone to rank two marked values without reading any numbers; if errors are common, prefer shared-axis position. **Stronger Test:** Run a small A/B check comparing the position-based design against a length/angle/area alternative for accuracy on the same sort prompt.

## What to do instead <!-- role: fix -->

- Use a design where both values share the same axis (common baseline) so their positions are directly comparable.
- Replace angle encodings with an aligned position encoding when the goal is ordering.
- Replace area encodings (circles/rectangles) with an aligned position encoding when the goal is ordering.
- If you must keep the original form, add explicit numeric labels for the compared values to reduce reliance on angle/area judgments.
