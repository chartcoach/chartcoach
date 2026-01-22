---
id: encode-speed-with-color-saturation-for-finding-extrema-on-curved-2d-time-trajectories
title: Encode speed with color saturation when users must find fastest/slowest points
  on curved 2D+time trajectories
bibliography: references.bib
description: For curved 2D+time trajectories, use color saturation to encode speed
  to improve extrema-finding accuracy.
labels:
- chart:trajectory
- task:find-extremum
- visual:color
- impact:accuracy
- data:temporal
- audience:general
- shape:curved
---

## Encode speed with color saturation for curved-path extrema tasks <!-- role: advice -->

Encode speed with color saturation when users must locate the fastest or slowest point on a curved 2D+time trajectory.

## Why color saturation helps for speed extrema on curved trajectories <!-- role: reason -->

This works because the extremum task can be solved by visually searching for the strongest color intensity, which supports rapid detection of maxima/minima without requiring precise comparisons across many locations.

**Mechanism:** A single salient “most saturated” (or “least saturated”) region acts as a visual target for extrema, reducing the need to integrate information along the whole path.

**Evidence:** In curved-trajectory extrema tasks, the speed-as-color-saturation design ranked highest in accuracy and was significantly better than multiple alternatives that encoded time or used size-based encodings [@perinAssessingGraphicalPerception2018]. This result is captured as a reusable recommendation rule through the graphical-perception knowledge collation pipeline [@zengReviewCollationGraphical2023].

**Notes:** This guideline is about finding extrema (fastest/slowest), not about estimating intermediate speed values.

## When this applies: curved 2D+time trajectory speed extrema <!-- role: context -->

- **User Goal:** Identify where along a path speed is highest or lowest.
- **Task:** find-extremum (speed).
- **Data:** Temporal sequence mapped onto a 2D path with varying speed.
- **Chart Setting:** Static 2D+time trajectory with a curved path.
- **Audience:** General audiences performing quick read-offs.
- **Success Criterion:** Lower error in locating the correct extremum point.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The task is to estimate time elapsed (not speed extrema) at a specific point on the path. **Why:** The evidence here concerns speed extrema accuracy, not time estimation performance.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Color becomes committed to speed, reducing availability of color for other variables. **Risk:** If other elements already use strong color, the speed encoding may visually compete. **Mitigation:** Keep surrounding elements visually quiet so the saturation cue remains dominant.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Encoding speed with size on a curved path as the primary cue for an extrema task. **Why it fails:** Size-based speed encodings ranked lower for curved-path extrema accuracy than the color-saturation speed encoding in the recorded results.

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers hesitate or pick points near the wrong peak/valley on the path. **Quick Check:** Ask a colleague to point to the fastest and slowest points; if they do not key off the most/least saturated region, the cue is not salient enough. **Stronger Test:** Run a small timed pilot with extrema prompts and compare error rates across encodings.

## What to do instead <!-- role: fix -->

- Encode speed with color saturation on the path stroke.
- If you cannot use color for speed, encode speed via segment-length (tick spacing) rather than size on curved paths.
- Reduce competing color elements near the trajectory so the saturation cue remains the most prominent signal.
