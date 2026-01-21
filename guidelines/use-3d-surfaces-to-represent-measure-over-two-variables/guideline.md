---
id: use-3d-surfaces-to-represent-measure-over-two-variables
title: Use 3D Surfaces for Measures Over Two Independent Variables
bibliography: references.bib
description: Represent a dependent measure across two independent variables with 3D
  meshes/surfaces to reveal global form and local variation.
labels:
- chart:surface
- task:explore
- task:compare
- visual:position
- visual:length
- impact:insight
- data:bivariate
- audience:expert
- complexity:intermediate
---

## The Rule <!-- role: advice -->

When you have one measure over two independent variables, use a 3D mesh or surface instead of a grid of bars.

## The Logic <!-- role: reason -->

Meshes/surfaces are intrinsically 3D representations that can convey global structure as continuous form, especially when the grid structure provides strong depth cues; they can support exploratory analysis across two variables in one coherent shape [@brath3DInfoVisHere2014].

- **The Principle:** Use 3D form (surface) to encode continuous variation across two axes.
- **The Evidence:** [@brath3DInfoVisHere2014]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand overall shape/trend plus local deviations across two dimensions.
- **Data Type:** Dense bivariate grids (regular intervals) such as function models or rates over time and maturity.
- **Audience:** Professional/technical users doing exploratory interpretation [@brath3DInfoVisHere2014].

## When to Break It <!-- role: exceptions -->

- **Scenario:** Users must make precise numeric comparisons against a common baseline without interaction.
- **Reason:** Perspective and 3D viewing reduce accuracy compared to flat 2D aligned baselines [@brath3DInfoVisHere2014].

## The Price <!-- role: costs -->

- **The Sacrifice:** Some precision in reading exact heights.
- **The Risk:** Poor depth cues or occlusion can make the surface ambiguous [@brath3DInfoVisHere2014].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Rendering the same data as a 3D field of bars.
- **Why it fails:** Uniformly shaded bar faces can hide subtle variation; the surface can reveal structure more effectively [@brath3DInfoVisHere2014].

## How to Check <!-- role: check -->

- **Visual Sign:** You can’t tell whether variations are smooth or noisy; the chart reads as cluttered blocks.
- **The Test:** Ask whether you can perceive both the macro shape and local anomalies without switching views; if not, bars may be obscuring structure [@brath3DInfoVisHere2014].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Convert bar grids to a continuous surface/mesh.
- **Best Fix:** Ensure regular grid cues are visible (e.g., explicit mesh lines) so viewers can decode the surface geometry [@brath3DInfoVisHere2014].
