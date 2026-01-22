---
id: prefer-animated-donut-transitions-for-max-delta
title: Use animated transitions to find the largest change between two donut-chart
  series
bibliography: references.bib
description: For donut charts, animated transitions allow viewers to detect the biggest
  mover more precisely than adjacent, mirrored, or overlaid layouts.
labels:
- chart:pie
- task:compare
- task:aggregate
- visual:animation
- visual:angle
- impact:accuracy
- data:categorical
- audience:novice
- comparison:two-series
---

## Prefer animation for biggest-mover judgments in donut charts <!-- role: advice -->

Use an animated transition between two donut-chart states when the goal is to identify the slice that changed the most between the two series.

## Why animation helps max-delta in donut charts <!-- role: reason -->

When a donut chart transitions between two series, the perceptual system can treat the amount of change as a motion signal rather than requiring a careful static comparison of two angular extents.

**Mechanism:** Motion during the transition acts as a direct cue for change magnitude, improving discrimination of the largest delta relative to distractor deltas.

**Evidence:** For a max-delta (“biggest mover”) task in donut charts, the animated arrangement outperformed the other tested arrangements (including adjacent and overlaid), and mirrored did not outperform adjacent. [@ondovFaceFaceEvaluating2019; @zengReviewCollationGraphical2023]

**Notes:** This guideline is about identifying a single biggest change, not about estimating overall similarity or correlation.

## When you should apply animated transitions for donut max-delta <!-- role: context -->

- **User Goal:** Identify which category’s share changed the most between two conditions/time points.
- **Task:** Aggregate (max-delta / “biggest mover”).
- **Data:** Two series over the same set of categories (mapped consistently to slices).
- **Chart Setting:** Donut chart with an animated morph/transition between series states.
- **Audience:** Viewers doing quick comparison.
- **Success Criterion:** Higher accuracy at smaller change signals.

## When not to use animation for donut max-delta <!-- role: exceptions -->

**Break it when:** The output must be static or the viewer cannot reliably see the transition. **Why:** The advantage depends on motion cues during the transition.

## Tradeoffs of animated donut transitions <!-- role: costs -->

**Sacrifice:** The comparison is time-dependent rather than continuously inspectable.\
**Risk:** If the transition is missed, the viewer may not be able to recover the comparison from the final static frame.\
**Mitigation:** Support replay in the viewing experience.

## Common mistakes with animated donut comparisons <!-- role: mistakes -->

**Mistake:** Assuming mirror-splitting a donut view will reliably improve biggest-mover detection. **Why it fails:** The mirrored donut arrangement did not outperform the adjacent donut arrangement for the max-delta task.

## Quick tests for whether animation is helping <!-- role: check -->

**Failure Sign:** Users only succeed when one slice change is extremely obvious.\
**Quick Check:** Show one transition and ask users to identify the biggest mover immediately; frequent disagreement suggests the motion cue is weak in this setup.\
**Stronger Test:** Run an A/B comparison of animated versus adjacent donut layouts on the same max-delta questions.

## What to do instead if animation is not viable <!-- role: fix -->

- Use an overlaid donut comparison if you can keep slice correspondence clear.
- Use adjacent donuts when viewers need stable, side-by-side inspection.
- Reduce the number of slices shown so the largest change is not masked by many small slices.
- Add a textual annotation naming the biggest-mover category when correctness is critical.
