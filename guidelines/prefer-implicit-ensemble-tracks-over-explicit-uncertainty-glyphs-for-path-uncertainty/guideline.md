---
id: prefer-implicit-ensemble-tracks-over-explicit-uncertainty-glyphs-for-path-uncertainty
title: Show Uncertainty with Discrete Ensemble Tracks, Not Expanding Summary Shapes
bibliography: references.bib
description: Use a set of forecast tracks to let viewers infer uncertainty from spatial
  spread instead of encoding it with a cone-like area.
labels:
- chart:trajectory
- task:judge-risk
- visual:position
- impact:reduce-bias
- data:uncertainty
- audience:novice
- domain:tropical-cyclone
- source:liu-2019
---

## The Rule <!-- role: advice -->

Depict track-path uncertainty by drawing a discrete set of forecast trajectories (an implicit uncertainty display) instead of a widening cone or other area-based summary glyph.

## The Logic <!-- role: reason -->

Implicit uncertainty uses spatial distribution itself to communicate variability, avoiding the common confound where an expanding summary shape is misread as the storm growing in size or intensity.

- **The Principle:** Avoid channel confounds between uncertainty area and phenomenon magnitude
- **The Evidence:** [@liuVisualizingUncertainTropical2019]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand where the storm might go without misreading uncertainty as storm growth
- **Data Type:** Path/track prediction ensembles with spatial uncertainty over time
- **Audience:** General public and other non-expert decision makers

## When to Break It <!-- role: exceptions -->

- **Scenario:** You must show an explicit probability region rather than a sample-based depiction
- **Reason:** A discrete set of tracks may not satisfy requirements for explicit containment/coverage regions

## The Price <!-- role: costs -->

- **The Sacrifice:** Less compact than a single summary shape
- **The Risk:** Overdrawing/clutter if too many tracks are shown or if tracks are disorganized

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Replace the cone with a “spaghetti plot” of many raw ensemble tracks
- **Why it fails:** Dense, irregular, crossing tracks can become structurally disorganized and hard to interpret [@liuVisualizingUncertainTropical2019]

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers could plausibly interpret widening shapes as increasing storm size/intensity
- **The Test:** Remove all annotations and ask whether “storm gets bigger over time” is a likely takeaway; if yes, the design is vulnerable to the confound

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch from an area-based cone/boxplot-style region to a small set of discrete tracks
- **Best Fix:** Use a representative, spatially organized subset of tracks (not raw spaghetti) and add separate encodings for size/intensity [@liuVisualizingUncertainTropical2019]
