---
id: avoid-free-floating-3d-scatterplots-without-depth-cues
title: Add Depth Cues or Avoid Non-Anchored 3D Points
bibliography: references.bib
description: Avoid 3D scatterplots of unstructured points unless the data or design
  provides strong cues for depth and position.
labels:
- chart:scatter
- task:explore
- visual:position
- impact:clarity
- data:multivariate
- audience:general
- complexity:intermediate
---

## The Rule <!-- role: advice -->

Do not use free-floating 3D scatterplots of random points unless you provide strong depth cues or the data’s structure makes depth self-evident.

## The Logic <!-- role: reason -->

With non-anchored points, viewers cannot reliably determine 3D location without cues (e.g., stereoscopic viewing, shadows, reference lines); however, some datasets (e.g., structured time series) can be readable because the structure of the data itself supplies positional cues [@brath3DInfoVisHere2014].

- **The Principle:** 3D position is ambiguous without anchors or redundant depth signals.
- **The Evidence:** [@brath3DInfoVisHere2014]

## Where to Apply <!-- role: context -->

- **User Goal:** Read relative positions or shapes in 3D space.
- **Data Type:** Point clouds in 3D where depth ordering matters.
- **Audience:** Any audience relying on a single view (especially non-expert viewers) [@brath3DInfoVisHere2014].

## When to Break It <!-- role: exceptions -->

- **Scenario:** Data has intrinsic structure that provides cues (e.g., time advances in one direction with constrained change rates).
- **Reason:** Structure can substitute for explicit depth cues and keep the 3D scatter readable [@brath3DInfoVisHere2014].

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional visual elements or interaction to supply depth cues.
- **The Risk:** Added cues can increase clutter if not integrated carefully [@brath3DInfoVisHere2014].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Plotting points in 3D with no reference plane, shadows, or other cues and expecting viewers to “see” depth.
- **Why it fails:** Depth becomes guesswork; position decoding collapses [@brath3DInfoVisHere2014].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers disagree on which points are in front/behind or where clusters sit in depth.
- **The Test:** Hide axes/labels and ask users to describe spatial relationships; if answers vary wildly, depth cues are insufficient [@brath3DInfoVisHere2014].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add reference cues (planes, grid, shadows, projection lines) that help decode depth.
- **Best Fix:** Re-encode the data using anchored structures (regular grids, surfaces) or a different representation that does not require ambiguous 3D point position reading [@brath3DInfoVisHere2014].
