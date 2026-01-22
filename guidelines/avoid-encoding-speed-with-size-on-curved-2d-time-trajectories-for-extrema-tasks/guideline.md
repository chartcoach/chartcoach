---
id: avoid-encoding-speed-with-size-on-curved-2d-time-trajectories-for-extrema-tasks
title: Avoid encoding speed with size on curved 2D+time trajectories for fastest/slowest-point
  tasks
bibliography: references.bib
description: On curved 2D+time trajectories, size-based speed encodings reduce extrema-finding
  accuracy compared to color-based speed encodings.
labels:
- chart:trajectory
- task:find-extremum
- visual:area
- impact:accuracy
- data:temporal
- audience:general
- shape:curved
- encoding:speed
---

## Avoid size as the primary speed cue on curved trajectories for extrema <!-- role: advice -->

Avoid using size (stroke width) as the primary encoding for speed when users need to find the fastest or slowest point on curved 2D+time trajectories.

## Why size hurts speed extrema perception on curved paths <!-- role: reason -->

This fails because curvature distorts the apparent thickness/width signal along the path, making local comparisons less stable than a color cue when searching for maxima/minima.

**Mechanism:** On curved strokes, thickness perception can be influenced by local geometry and visual crowding, reducing the reliability of “thickest/thinnest point” as a target.

**Evidence:** In curved-path extrema tasks, the size-based speed encoding ranked below the color-saturation speed encoding, and multiple designs that relied on size did not match the top accuracy tier recorded for speed-as-color-saturation [@perinAssessingGraphicalPerception2018]. This relationship is preserved in the extracted design-ranking knowledge for recommendation workflows [@zengReviewCollationGraphical2023].

**Notes:** The evidence here is about curved trajectories; straight trajectories showed less separation among several encodings.

## When this applies: curved trajectories + speed extrema <!-- role: context -->

- **User Goal:** Identify where the path is fastest/slowest.
- **Task:** find-extremum (speed).
- **Data:** Speed varies along a 2D+time trajectory.
- **Chart Setting:** Curved trajectory, static display.
- **Audience:** General audiences doing quick judgments.
- **Success Criterion:** Lower error locating speed extrema.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The path is straight and the study’s straight-path conditions do not show a clear disadvantage for size relative to other top encodings. **Why:** The observed drawback is tied to curved-path distortion.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may lose an encoding option when color is unavailable. **Risk:** Replacing size with another cue may require adding marks (e.g., ticks) that increase clutter. **Mitigation:** Prefer cues that remain robust under curvature even if they add minimal structure.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Keeping size for speed on curved paths and “fixing it” by increasing thickness range. **Why it fails:** A larger thickness range does not address curvature-related distortion and can create occlusion or clutter.

## Quick tests <!-- role: check -->

**Failure Sign:** People choose extrema points that track curvature or local bends rather than true speed peaks/troughs. **Quick Check:** Present two curved paths with known maxima and see whether selections cluster around visually thick segments regardless of true location. **Stronger Test:** A/B compare size vs color-saturation for the same extrema prompts and compute error.

## What to do instead <!-- role: fix -->

- Encode speed with color saturation on the path stroke for curved trajectories.
- If color cannot be used for speed, represent time with segment length and allow speed to be inferred from segment length.
- Reduce competing width changes caused by styling (e.g., decorative stroke caps) so any remaining width variation is not ambiguous.
