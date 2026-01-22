---
id: expect-clutter-and-scaling-failures-above-roughly-200-entities-in-trend-views
title: Constrain multivariate trend views to modest entity counts to avoid clutter
  and illegible small multiples
bibliography: references.bib
description: Animation, traces, and small multiples all degrade beyond modest numbers
  of entities due to clutter or tiny panels.
labels:
- chart:scatter
- task:overview
- visual:layout
- impact:readability
- data:temporal
- audience:general
- complexity:scaling
---

## Keep entity counts modest in animated and static multivariate trend displays <!-- role: advice -->

Keep animated bubble trends, overlaid traces, and small multiples trend grids to a modest number of entities, and reduce or restructure the display when the count grows.

## Why scale breaks across all three approaches <!-- role: reason -->

As entity count rises, animation and overlaid traces become visually cluttered and hard to track, while small multiples shrink each panel until the trace is difficult to perceive.

**Mechanism:** Overplotting increases occlusion and tracking failures in shared-space views, and limited display area forces a resolution tradeoff in faceted views.

**Evidence:** All three techniques were observed to fail to scale beyond roughly 200 data points because animation/traces become extremely cluttered and small multiples panels become too small to see the trace effectively [@robertsonEffectivenessAnimationTrend2008]. Participants also reported difficulty tracking “flying” points in larger animated datasets [@robertsonEffectivenessAnimationTrend2008].

**Notes:** Dataset size also affected accuracy; smaller datasets yielded better correctness overall.

## When this applies <!-- role: context -->

- **User Goal:** Understand trends across many entities at once.
- **Task:** Identify anomalies or summarize overall movement.
- **Data:** Many entities (dozens to hundreds) with time trajectories.
- **Chart Setting:** Fixed screen area (projected slide, desktop window).
- **Audience:** Mixed; includes viewers who cannot interact deeply.
- **Success Criterion:** Anomalies remain visible and entities remain trackable.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The task only concerns a small, preselected subset of entities. **Why:** The effective entity count on screen is already constrained by selection, so scaling pressure is reduced [@robertsonEffectivenessAnimationTrend2008].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Reduced completeness of the “show everything” view. **Risk:** Filtering or restructuring can hide rare but important items. **Mitigation:** Make it easy to change the subset being shown.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Adding more entities to an animated bubble chart without changing the design. **Why it fails:** Viewers lose track of moving points and miss events in dense motion [@robertsonEffectivenessAnimationTrend2008].
- **Mistake:** Solving clutter by shrinking small multiples indefinitely. **Why it fails:** The traces become too small to read, defeating the purpose [@robertsonEffectivenessAnimationTrend2008].

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers describe the display as confusing or cannot reliably follow a single entity. **Quick Check:** Ask a user to track one named entity for a full run; if they lose it, the view is over capacity. **Stronger Test:** Measure anomaly-finding accuracy as you increase entity count; stop increasing when accuracy drops sharply.

## What to do instead <!-- role: fix -->

- Reduce the number of entities displayed at once by selecting a subset relevant to the question.
- Use selection/highlighting to focus on a few entities while de-emphasizing the rest.
- Switch from animation to static views when tracking failures dominate.
- Restructure the display into grouped blocks (e.g., by category) to reduce within-view density.
