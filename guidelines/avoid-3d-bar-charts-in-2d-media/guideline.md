---
id: avoid-3d-bar-charts-in-2d-media
title: Avoid 3D bar charts in 2D media; encode extra dimensions with color or size
  instead of depth
bibliography: references.bib
description: 3D charts on flat media cause occlusion, projection distortion, and depth
  ambiguity that reduce accuracy and can hide data.
labels:
- chart:bar
- task:compare
- visual:depth
- impact:accuracy
- data:multivariate
- audience:general
- risk:occlusion
---

## Do not use 3D bars on slides or paper; use 2D encodings for additional variables <!-- role: advice -->

Avoid 3D bar charts in 2D media such as slides and documents. If you need to show a third variable, encode it with a non-depth channel such as color or size in a 2D design.

## Why 3D in 2D media misleads <!-- role: reason -->

3D displays projected onto 2D remove key depth cues and introduce occlusion, making some marks hard or impossible to see. Projection also distorts perceived sizes and shapes by viewpoint, and depth creates perceptual ambiguity because a small-looking mark can be either small in value or simply farther away.

**Mechanism:** Occlusion hides information, projection changes geometric measurements, and missing binocular depth cues make depth judgments unreliable in static 2D renderings.

**Evidence:** 3D bar charts can occlude central data and distort perceived values, making comparisons difficult or incorrect; alternative 2D encodings better support accurate comparisons across multiple dimensions [@szafirGoodBadBiased2018]. Projecting 3D charts into 2D can distort mark geometry (for example, slice angles) in ways that bias interpretation [@szafirGoodBadBiased2018].

**Notes:** Even when interaction allows rotation, occlusion and viewpoint dependence can still make it unclear what is being compared.

## When this applies <!-- role: context -->

- **User Goal:** Compare magnitudes across categories and an additional dimension.
- **Task:** Rank, estimate differences, identify maxima/minima in a grid.
- **Data:** Multivariate tables or grids where designers are tempted to add depth for the third variable.
- **Chart Setting:** Static screenshots, papers, slide decks, and dashboards viewed from a fixed angle.
- **Audience:** General readers and decision makers who need quick, correct comparisons.
- **Success Criterion:** All marks are visible and comparable without mental reconstruction of depth.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The data is inherently three-dimensional geometry (such as molecular surfaces or architectural forms) where 3D provides necessary spatial context. **Why:** The shape itself is part of the data and cannot be faithfully represented as purely 2D without losing essential context [@szafirGoodBadBiased2018].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** 3D can feel “engaging” and may appear to pack more information into one view. **Risk:** Replacing depth with color/size can require careful legend design and may reduce immediate visual novelty. **Mitigation:** Use layout, labeling, and interaction to keep multi-encoding views readable without depth.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Adding 3D purely for style on charts meant for precise value comparison. **Why it fails:** Occlusion and projection distortions reduce readability and can change perceived values [@szafirGoodBadBiased2018].

## Quick tests to catch problems <!-- role: check -->

**Failure Sign:** Some bars or labels are partially hidden, or bar heights differ depending on viewpoint. **Quick Check:** Ask whether every bar can be read without rotating or guessing its base. **Stronger Test:** Flatten the chart to 2D and see whether the rank order or apparent gaps change.

## What to do instead <!-- role: fix -->

- Convert 3D bars to a 2D grouped/stacked layout when comparisons remain clear.
- Encode the third variable with color or size in a 2D grid or heatmap-like design.
- Use small multiples to separate dimensions when a single view becomes cluttered.
- Pair any necessary 3D view with a 2D summary that supports accurate comparison from one glance.
