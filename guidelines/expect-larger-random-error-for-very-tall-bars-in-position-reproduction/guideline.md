---
id: expect-larger-random-error-for-very-tall-bars-in-position-reproduction
title: Expect Larger Random Error for Very Tall Bars in Position Reproduction
bibliography: references.bib
description: Tall, slender bars produce much more variable position reproductions
  than square or wide bars.
labels:
- chart:bar
- task:estimate
- visual:position
- impact:accuracy
- data:quantitative
- audience:novice
- robustness:variance
---

## Avoid very tall, slender bars when precise reproduction is required <!-- role: advice -->

Avoid designs that create extremely tall, slender bar marks when users must precisely reproduce or match bar-top positions. Prefer square-ish or wider marks for tasks demanding low variability.

## Why tall bars increase variability <!-- role: reason -->

Across experiments, tall aspect ratio bars did not just shift mean responses downward in memory; they also produced much higher absolute error (greater variability) than square or wide bars. This indicates that tall, slender shapes can degrade precision in position reproduction tasks even when the encoding is still “position.”

**Mechanism:** Tall, slender marks appear to be harder to reproduce consistently, increasing random error in matching the bar-top position.

**Evidence:** Absolute error differed by aspect ratio, with tall bars showing substantially higher absolute error than square bars in multiple experiments and replications [@cejaTruthSquareAspect2021a]. Wide and square bars were closer to each other in absolute error, while tall bars were consistently worse [@cejaTruthSquareAspect2021a].

**Notes:** This guideline concerns variability (absolute error), not the direction of bias (signed error), which is addressed separately.

## When this applies <!-- role: context -->

- **User Goal:** Make precise readings or reproduce values with minimal noise.
- **Task:** Match bar heights, enter values based on bars, or redraw values from a chart.
- **Data:** Quantitative values where small differences matter.
- **Chart Setting:** Narrow columns, dense category sets, or layouts that force bars into very thin widths relative to height.
- **Audience:** Any audience; especially important when downstream decisions depend on fine-grained differences.
- **Success Criterion:** Low absolute error (high precision) in value judgments.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The chart is intended only for coarse pattern recognition and not for precise value retrieval or reproduction. **Why:** Increased variability may be acceptable when precision is not a success criterion.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Increasing bar width or changing layout can reduce the number of categories visible at once. **Risk:** Wider bars can create a perception of crowding or require interaction (scrolling/paging). **Mitigation:** Prioritize precision-critical views for redesign rather than changing every view.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Compressing a bar chart into a narrow container until bars become needle-thin. **Why it fails:** Tall, slender bars show higher absolute error in position reproduction, reducing precision [@cejaTruthSquareAspect2021a].
- **Mistake:** Treating all bar shapes as equally readable because the encoding is “position.” **Why it fails:** Aspect ratio changes precision, with tall shapes producing more variable responses [@cejaTruthSquareAspect2021a].

## Quick tests <!-- role: check -->

**Failure Sign:** Users’ repeated estimates of the same tall bar vary widely, even when they are attentive. **Quick Check:** Inspect the bar width:height ratios; flag bars that are much taller than they are wide. **Stronger Test:** Run a quick repeated-matching task and compare absolute error across aspect ratios [@cejaTruthSquareAspect2021a].

## What to do instead <!-- role: fix -->

- Increase bar width (or reduce chart height range) to move away from extremely tall, slender marks.
- Split dense category sets into multiple views that keep bars from becoming needle-thin.
- Use an interaction that allows users to keep the target bar visible while matching or reading it.
- If precise values are required, support the task with a workflow that avoids manual reproduction of tall-bar positions.
