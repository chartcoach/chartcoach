---
id: encode-direction-in-small-multiples-with-size-ramp
title: Encode Direction in Small Multiples with a Size Ramp
bibliography: references.bib
description: In tiny per-item trace panels, use changing marker size to convey time
  direction when opacity cues become unreadable.
labels:
- chart:small-multiples
- task:understand-change
- visual:size
- impact:clarity
- data:temporal
- audience:general
- method:trace-lines
---

## The Rule <!-- role: advice -->

In small-multiples trace panels where direction is hard to see, encode time direction by increasing marker size from start to end.

## The Logic <!-- role: reason -->

When each trace is tiny, direction-of-flow is no longer discernible; changing size along the path provides a legible directional cue even at small scale.

- **The Principle:** Use a robust directional cue that survives downscaling
- **The Evidence:** The paper’s Small Multiples visualization changed bubble size encoding to show direction from smallest to largest, with the largest reflecting the original size at the end of the sequence [@robertsonEffectivenessAnimationTrend2008].

## Where to Apply <!-- role: context -->

- **User Goal:** Reading start vs end and general movement direction within each mini-panel
- **Data Type:** Many entities shown as small multiples with shared axes
- **Audience:** Analysts scanning many small panels

## When to Break It <!-- role: exceptions -->

- **Scenario:** Marker size is already reserved for an essential quantitative variable that must be read accurately throughout the trajectory.
- **Reason:** Re-encoding size primarily for direction would change the meaning of size over time (the paper explicitly altered size encoding for direction in small multiples) [@robertsonEffectivenessAnimationTrend2008].

## The Price <!-- role: costs -->

- **The Sacrifice:** Consistent quantitative interpretation of size across the entire path.
- **The Risk:** Viewers may misinterpret size changes as data changes rather than a direction cue if not explained [@robertsonEffectivenessAnimationTrend2008].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using the same opacity-only direction cue from a large traces view inside tiny small-multiple panels.
- **Why it fails:** The paper notes direction is no longer discernible at that reduced scale [@robertsonEffectivenessAnimationTrend2008].

## How to Check <!-- role: check -->

- **Visual Sign:** In a mini-panel, the trace looks like a simple line with no obvious start/end.
- **The Test:** Print or zoom out until panels are at intended size; if you can’t point to the end quickly, add a size ramp [@robertsonEffectivenessAnimationTrend2008].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add start-to-end marker sizing (small→large) along the trace.
- **Best Fix:** Keep shared axes across panels and use the size ramp consistently so users learn the directional cue once and reuse it everywhere [@robertsonEffectivenessAnimationTrend2008].
