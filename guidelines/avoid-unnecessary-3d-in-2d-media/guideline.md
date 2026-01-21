---
id: avoid-unnecessary-3d-in-2d-media
title: Avoid Unnecessary 3D in 2D Media
bibliography: references.bib
description: Do not use 3D chart effects on slides or paper because occlusion, projection
  distortion, and depth ambiguity bias perception.
labels:
- chart:bar
- task:compare
- visual:depth
- impact:accuracy
- data:multivariate
- audience:general
- source:szafir-2018
---

## The Rule <!-- role: advice -->

Do not use 3D chart effects (e.g., 3D bars or tilted 3D pies) in 2D outputs like papers and slide decks unless 3D is essential to the data.

## The Logic <!-- role: reason -->

3D in 2D media biases analysis through (1) occlusion (data becomes hidden), (2) projection distortion (shapes/areas/angles change with depth), and (3) perceptual ambiguity (size can mean value or distance), as outlined in [@szafirGoodBadBiased2018].

- **The Principle:** Occlusion + projection distortion + depth ambiguity
- **The Evidence:** [@szafirGoodBadBiased2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Compare values accurately across categories or dimensions
- **Data Type:** Standard statistical charts rendered with faux-3D perspective
- **Audience:** Any audience; errors occur even when axes are labeled

## When to Break It <!-- role: exceptions -->

- **Scenario:** The data has inherent 3D structure (e.g., spatial forms) and 3D provides necessary context
- **Reason:** 3D can be justified for inherently spatial data, though still limited from a single view, per [@szafirGoodBadBiased2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** “Futuristic” aesthetics and perceived sophistication
- **The Risk:** Switching to 2D may require alternative encodings for additional dimensions

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping 3D but adding shadows/stronger gridlines to “clarify”
- **Why it fails:** The core issues (occlusion, projection, ambiguity) remain, per [@szafirGoodBadBiased2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Some marks are partially hidden; identical values appear different sizes due to depth; slices/bars closer to the viewer look bigger
- **The Test:** Ask whether any value would change if the camera angle changed—if yes, the encoding is vulnerable to projection bias described in [@szafirGoodBadBiased2018]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Remove the 3D perspective and render the chart in 2D
- **Best Fix:** Encode the additional dimension using another visual variable (e.g., color or size) or pair 2D summaries with 3D context when 3D is inherently needed, as recommended in [@szafirGoodBadBiased2018]
