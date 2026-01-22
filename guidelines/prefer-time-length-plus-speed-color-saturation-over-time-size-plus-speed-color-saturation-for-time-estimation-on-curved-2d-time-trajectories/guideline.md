---
id: prefer-time-length-plus-speed-color-saturation-over-time-size-plus-speed-color-saturation-for-time-estimation-on-curved-2d-time-trajectories
title: Prefer time as segment length (ticks) plus speed as color saturation over time
  as size plus speed as color saturation for time estimation on curved 2D+time trajectories
bibliography: references.bib
description: For curved 2D+time trajectories, encoding time with segment length and
  speed with color saturation yields better time-task accuracy than encoding time
  with size and speed with color saturation.
labels:
- chart:trajectory
- task:aggregate
- visual:length
- visual:color
- impact:accuracy
- data:temporal
- audience:general
- shape:curved
- encoding:double
---

## Use ticks for time when also using color saturation for speed on curved paths <!-- role: advice -->

When you encode speed with color saturation on a curved 2D+time trajectory and users must estimate time elapsed, encode time with segment length (ticks) rather than size.

## Why ticks+color separates time from speed more reliably than size+color <!-- role: reason -->

This works because segment length provides discrete time structure while color saturation highlights speed, reducing reliance on thickness gradients for time judgments on curved geometry.

**Mechanism:** Time ticks create stable spatial reference intervals for time, while size gradients require continuous interpolation that is less reliable on curved paths.

**Evidence:** In the curved-path time task, the design encoding time with length and speed with color saturation ranked highest and was significantly better than alternatives lower in the ranking, while the time-with-size and speed-with-color design did not occupy the top position [@perinAssessingGraphicalPerception2018]. This comparative design preference is included in the collated knowledge intended for visualization recommendation constraints [@zengReviewCollationGraphical2023].

**Notes:** This guideline is specific to time estimation performance, not necessarily to speed extrema performance.

## When this applies: curved path + dual encoding + time estimation <!-- role: context -->

- **User Goal:** Locate a target time point while still conveying speed variation.
- **Task:** aggregate (time lookup/estimation).
- **Data:** Time increases monotonically; speed varies along the path.
- **Chart Setting:** Curved 2D+time trajectory with two variables to encode on the stroke.
- **Audience:** General audiences making quick judgments.
- **Success Criterion:** Lower error on time judgments.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Ticks/segment marks cannot be displayed clearly at the intended scale (e.g., the path is too short on screen). **Why:** Segment-length encoding needs resolvable tick spacing to carry time.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Adding ticks consumes visual bandwidth and can add clutter. **Risk:** Too many ticks can make the path harder to read as a shape. **Mitigation:** Ensure tick density stays legible and does not visually merge.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Encoding time with size while also using color saturation for speed on curved paths and assuming the thickness gradient is easy to read. **Why it fails:** The recorded ranking shows better time-task accuracy for the time-as-length plus speed-as-color configuration on curved paths.

## Quick tests <!-- role: check -->

**Failure Sign:** People can find fast/slow regions but miss intermediate time targets. **Quick Check:** Ask someone to locate 25%, 50%, and 75% time points; if answers drift widely, time encoding is not working. **Stronger Test:** Run a brief pilot comparing error for time targets with (ticks+color) vs (size+color) on the same curved paths.

## What to do instead <!-- role: fix -->

- Add time ticks so time is encoded by segment length along the path.
- Keep speed encoded with color saturation on the stroke to preserve extrema salience.
- Reduce other line decorations that could be confused with tick marks.
