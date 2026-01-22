---
id: encode-time-with-segment-length-not-color-saturation-for-estimating-time-on-2d-time-trajectories
title: Encode time with segment length (tick spacing) instead of color saturation
  for estimating time on 2D+time trajectories
bibliography: references.bib
description: Use segment length (time ticks) rather than color saturation when users
  must estimate time elapsed along a 2D+time path.
labels:
- chart:trajectory
- task:aggregate
- visual:length
- impact:accuracy
- data:temporal
- audience:general
- encoding:time
---

## Encode time using segment length (time ticks) for time estimation <!-- role: advice -->

Encode time using segment length (tick spacing) rather than color saturation when users must estimate time elapsed along a 2D+time trajectory.

## Why segment length supports time estimation better than color saturation <!-- role: reason -->

This works because time ticks externalize the passage of time into countable/spatial intervals along the path, while a color-saturation gradient requires fine discrimination of intermediate shades.

**Mechanism:** Tick spacing and the distribution of segments provide discrete anchors that let viewers localize a target time by relative position among segments, instead of interpolating within a continuous color ramp.

**Evidence:** For the time-estimation task, the time-as-color-saturation encoding performed worse than multiple alternatives that represent time differently, while designs using segment-length for time were among the top-performing options in the study’s recommendations and recorded outcomes [@perinAssessingGraphicalPerception2018]. This finding is included as an actionable guideline through the broader graphical perception collation for recommendation systems [@zengReviewCollationGraphical2023].

**Notes:** This guideline targets time estimation along a single trajectory (e.g., locating a percentage of elapsed time).

## When this applies: time estimation on a 2D+time path <!-- role: context -->

- **User Goal:** Locate where a given amount of time has elapsed along the path.
- **Task:** aggregate (time lookup/estimation along the trajectory).
- **Data:** Time mapped monotonically along a 2D trajectory.
- **Chart Setting:** Static 2D+time trajectory (straight or curved).
- **Audience:** General audiences needing quick judgments.
- **Success Criterion:** Lower error in locating the correct time point.

## When not to follow it <!-- role: exceptions -->

**Break it when:** You cannot add ticks/segment marks because they would visually conflict with required path annotations (e.g., dense overlays that would make ticks unreadable). **Why:** Segment-length encoding relies on visible tick structure to convey time.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Additional visual marks (ticks) add clutter and can increase visual density. **Risk:** If ticks are too dense, the spacing cue becomes hard to parse. **Mitigation:** Use a tick frequency that remains legible at the intended display size.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using only a color-saturation gradient to encode time and expecting accurate intermediate time read-offs. **Why it fails:** Time-as-color-saturation ranked low for the time task compared to other time encodings in the recorded results.

## Quick tests <!-- role: check -->

**Failure Sign:** People guess quickly and inconsistently for intermediate time targets (e.g., 25%, 50%, 75%). **Quick Check:** Ask someone to point to the 50% time point; if they cannot justify it using the tick structure, the time cue is not doing its job. **Stronger Test:** Time a small set of users on the same time targets and compare errors with/without ticks.

## What to do instead <!-- role: fix -->

- Add time ticks so time is represented by segment length (tick spacing) along the path.
- If you must keep a color encoding, reserve color saturation for speed rather than time.
- Reduce other line patterns or marks near the trajectory that could be confused with ticks.
