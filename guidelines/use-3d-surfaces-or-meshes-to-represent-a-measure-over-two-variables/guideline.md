---
id: use-3d-surfaces-or-meshes-to-represent-a-measure-over-two-variables
title: Use 3D surfaces or meshes to represent a measure over two variables
bibliography: references.bib
description: Represent a dependent measure across two independent variables with a
  3D surface/mesh to reveal global form and local variation.
labels:
- chart:surface
- task:explore
- visual:position
- impact:insight
- data:multivariate
- audience:expert
- complexity:advanced
---

## Represent a bivariate field as a 3D surface/mesh <!-- role: advice -->

Use a 3D surface or mesh to encode a quantitative measure across two independent variables when understanding overall shape and local deviations matters.

## Why surfaces reveal structure that bars may hide <!-- role: reason -->

A continuous surface supports reading “shape” as a coherent object, and a regular mesh/grid provides depth cues that help viewers interpret the 3D structure without needing many extra annotations.

**Mechanism:** The surface turns many individual values into a visible geometry, supporting perception of smooth trends, curvature, and localized anomalies as changes in the surface.

**Evidence:** Surfaces and meshes are highlighted as uniquely effective 3D representations for measures over two variables, and converting a bar grid into a surface can make local structure and overall form more visible [@brath3DInfoVisHere2014].

**Notes:** Showing grid lines on regularly spaced meshes strengthens perspective cues.

## When to use surfaces/meshes <!-- role: context -->

- **User Goal:** Understand global form (trend/curvature) while noticing localized changes.
- **Task:** Explore and interpret a quantitative field over two variables.
- **Data:** One dependent quantitative measure; two independent variables (continuous or discretized).
- **Chart Setting:** Screen-based visualization where a stable default viewpoint can be set; optional interaction.
- **Audience:** Domain users comfortable reasoning about “shape” (e.g., function-like views).
- **Success Criterion:** The viewer can describe both broad structure and local anomalies from the same view.

## When not to use surfaces/meshes <!-- role: exceptions -->

- **Break it when:** The task demands precise value readout at many specific points with minimal error. **Why:** 3D perspective reduces the precision of length judgments compared to flat, common-baseline 2D views [@brath3DInfoVisHere2014].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Exact numeric comparison can be harder than in 2D. **Risk:** Poor lighting or weak depth cues can flatten the surface and hide structure. **Mitigation:** Use regular mesh cues and a view that supports stable depth interpretation.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Showing the same data as a dense grid of 3D bars instead of a surface when the intent is to see shape. **Why it fails:** Uniformly shaded bar faces can make subtle variation hard to see [@brath3DInfoVisHere2014].
- **Mistake:** Removing grid/mesh cues in a regular field. **Why it fails:** The scene loses strong perspective cues that aid reading the surface [@brath3DInfoVisHere2014].

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers describe the plot as “a pile of blocks” rather than a coherent trend. **Quick Check:** Ask someone to point out the main ridge/valley and a local anomaly without rotating. **Stronger Test:** Compare anomaly-finding accuracy for surface vs. bar-grid encodings on the same data.

## What to do instead <!-- role: fix -->

- Use 2D slices (coordinated line charts) when precise comparisons along one variable dominate.
- Use a linked 2D slice view alongside the 3D surface for accurate readout of a selected cross-section.
- Use small multiples of 2D heatmaps when 3D depth cues cannot be reliably perceived in the viewing context.
- Use a simplified surface (reduced resolution) if the full mesh is visually noisy.
