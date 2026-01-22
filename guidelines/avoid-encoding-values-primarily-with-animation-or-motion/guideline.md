---
id: avoid-encoding-values-primarily-with-animation-or-motion
title: Avoid encoding values primarily with animation or motion when viewers must
  compare many items or time points
bibliography: references.bib
description: Motion and animation overwhelm attention and memory, so use static comparison
  designs to support reliable change detection.
labels:
- chart:scatter
- task:compare
- visual:motion
- impact:accuracy
- data:temporal
- audience:general
- risk:change-blindness
---

## Prefer static time comparisons over animation for analytical reading <!-- role: advice -->

When viewers need to compare many values or time points, use static comparison designs rather than relying on animation. Only use animation when the message depends on a small number of tracked elements and you can direct attention to them.

## Why animation hides change in data <!-- role: reason -->

Attention is limited, and animated displays force viewers to allocate attention to only a small subset of moving elements at a time. This produces change blindness—viewers miss important changes outside their focus—and memory limits make it hard to retain precise differences across frames.

**Mechanism:** Motion tracking capacity is small and attention is selective, so many simultaneous changes become invisible and frame-to-frame comparisons become unreliable.

**Evidence:** People can track only a few moving points at once and distinguish only a small number of motion speeds/directions, limiting motion as a quantitative encoding [@szafirGoodBadBiased2018]. Change blindness causes viewers to miss meaningful changes when attention is directed elsewhere, which makes animated data over time easy to misread [@szafirGoodBadBiased2018].

**Notes:** Animation can still work as narration when a presenter tightly guides attention, but it is weaker for self-directed analysis.

## When this applies <!-- role: context -->

- **User Goal:** Detect what changed, compare before/after, or understand trends across time.
- **Task:** Compare multiple time points; spot anomalies; assess trajectories.
- **Data:** Time series or repeated measures with many entities (multiple lines/points).
- **Chart Setting:** Dashboards, reports, or interactive visuals where viewers explore without a narrator.
- **Audience:** Analysts and decision makers who need correctness more than entertainment.
- **Success Criterion:** Viewers can find and explain changes without missing key events.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The visualization is a guided presentation and the story hinges on a small number of highlighted elements. **Why:** Directed attention can compensate for some attention limits in a narrated sequence [@szafirGoodBadBiased2018].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Animation can be engaging and can convey a sense of “movement through time” quickly. **Risk:** Static small multiples or overlays can increase space usage or visual clutter. **Mitigation:** Limit the number of series shown at once and use filtering or grouping to keep comparisons legible.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Animating all entities and assuming viewers will notice the important changes. **Why it fails:** Viewers attend to a few elements and miss changes elsewhere due to change blindness and limited tracking capacity [@szafirGoodBadBiased2018].

## Quick tests to catch problems <!-- role: check -->

**Failure Sign:** Viewers disagree on what changed or cannot recall specific changes after watching the animation once. **Quick Check:** Pause at random frames and ask viewers to describe differences from the prior frame. **Stronger Test:** Give viewers a set of change-detection questions and compare accuracy on animated vs. static versions.

## What to do instead <!-- role: fix -->

- Use juxtaposition (small multiples) to show multiple time points side by side for scanning across time.
- Use superposition (overlay) when comparing a small number of time points precisely on the same axes.
- Use explicit change encodings (for example, trajectories) when the primary question is “how did it move or change?”
- Add interaction that supports scrubbing and persistent traces rather than transient frame updates.
