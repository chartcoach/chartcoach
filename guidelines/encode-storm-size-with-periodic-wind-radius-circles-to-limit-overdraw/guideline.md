---
id: encode-storm-size-with-periodic-wind-radius-circles-to-limit-overdraw
title: Encode storm size with periodic wind-radius circles instead of continuous footprints
bibliography: references.bib
description: Show storm size by drawing circles at coarse time intervals whose radii
  represent hurricane-force wind extent.
labels:
- chart:trajectory
- task:estimate-impact-area
- visual:size
- impact:readability
- data:temporal
- audience:novice
- domain:tropical-cyclone
---

## Depict storm size using circles at spaced time intervals, with radius mapped to the hurricane-force wind radius <!-- role: advice -->

Represent storm size by drawing circles centered on selected track positions at coarse time intervals, with circle radius set to the predicted radius of hurricane-force winds. Avoid drawing size circles at every time step to prevent severe overlap.

## Coarse, periodic glyphs preserve legibility while still conveying footprint scale and timing <!-- role: reason -->

Frequent size glyphs along multiple tracks can quickly saturate the map, making both paths and sizes unreadable. Showing size at a reduced cadence retains an interpretable sense of footprint magnitude and also provides implicit timing markers along the forecast horizon.

**Mechanism:** Lower glyph frequency reduces occlusion and clutter; repeated-but-spaced circles create a readable pattern that communicates both size and temporal progression.

**Evidence:** The paper encodes size as circles using the radius of 64-kt winds, but places them only every 12 hours to avoid overdrawing, using the circle positions as half-day time markers [@liuVisualizingUncertainTropical2019].

**Notes:** The design further spaces circle placement across tracks to maintain separation.

## When this applies: showing footprint/extent alongside uncertain paths on a map <!-- role: context -->

- **User Goal:** Understand how large the hazardous wind field might be around possible storm centers.
- **Task:** Estimate whether a location might fall within damaging winds over time.
- **Data:** Predicted wind radii (e.g., 64-kt radius) attached to track points.
- **Chart Setting:** Multi-track map display where overlap is a major risk.
- **Audience:** Non-experts needing an intuitive footprint cue.
- **Success Criterion:** Size is visible without obscuring the track distribution or geography.

## When not to follow it: when continuous footprint boundaries are required at all times <!-- role: exceptions -->

**Break it when:** The task requires a continuous footprint envelope at fine temporal resolution. **Why:** Periodic circles intentionally omit intermediate-time size information.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You reduce temporal resolution of size display. **Risk:** Viewers may assume size is constant between circles. **Mitigation:** Make the interval visually obvious (e.g., consistent spacing) and clarify the time step represented by each circle.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Drawing size circles at every hour for many tracks. **Why it fails:** Overdraw makes both size and path uncertainty hard to interpret.

## Quick tests <!-- role: check -->

**Failure Sign:** Circles overlap so much that the underlying track distribution is no longer visible. **Quick Check:** Temporarily toggle circles on/off and verify that adding circles does not erase track separation. **Stronger Test:** Ask users to estimate whether a marked location lies within the wind-radius circles at a given forecast time and check accuracy.

## What to do instead <!-- role: fix -->

- Draw size circles at a coarser cadence (e.g., every 12 hours) rather than at every time step.
- Choose circle placement across tracks to maintain spacing and reduce overlaps.
- Limit circle drawing to a subset of tracks if necessary to keep the footprint readable.
- If finer timing is required, switch to a time-slice view that shows size at a single selected time.
