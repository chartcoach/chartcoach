---
id: annotate-tracks-with-intensity-color-and-periodic-size-circles-to-convey-risk-factors
title: Add Intensity Color and Sparse Size Circles to Track Displays
bibliography: references.bib
description: Encode intensity with categorical line color and storm size with occasional
  radius circles to communicate risk without relying on uncertainty glyphs.
labels:
- chart:trajectory
- task:judge-risk
- visual:color
- impact:clarity
- data:multivariate
- audience:novice
- domain:tropical-cyclone
- source:liu-2019
---

## The Rule <!-- role: advice -->

Encode storm intensity along tracks using categorical color per segment, and show storm size using circles centered on the track at sparse time intervals (e.g., every 12 hours) instead of drawing size glyphs at every step.

## The Logic <!-- role: reason -->

Implicit uncertainty frees visual channels so intensity and size can be encoded directly; sparse size glyphs reduce overdrawing while still conveying when and how large the storm could be at key intervals.

- **The Principle:** Use annotation to convey multivariate risk while managing clutter
- **The Evidence:** [@liuVisualizingUncertainTropical2019]

## Where to Apply <!-- role: context -->

- **User Goal:** Estimate damage/risk based on both likelihood of impact (spread) and hazard magnitude (size/intensity)
- **Data Type:** Forecast tracks with intensity categories and size measures over time
- **Audience:** Non-experts making risk judgments

## When to Break It <!-- role: exceptions -->

- **Scenario:** You need hour-by-hour size values without any loss of temporal granularity
- **Reason:** Drawing size circles at every hour causes severe overdrawing in track ensembles [@liuVisualizingUncertainTropical2019]

## The Price <!-- role: costs -->

- **The Sacrifice:** Size information becomes temporally sampled rather than continuous
- **The Risk:** Users may interpolate size changes between glyphs incorrectly

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Draw size circles at every time step on every track
- **Why it fails:** The display becomes cluttered and size encodings overlap, reducing interpretability [@liuVisualizingUncertainTropical2019]

## How to Check <!-- role: check -->

- **Visual Sign:** Size circles overlap heavily, obscuring tracks and each other
- **The Test:** Zoom out to the full forecast extent; if circles form a dense texture rather than distinct samples, the frequency is too high [@liuVisualizingUncertainTropical2019]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce circle frequency (e.g., show every 12 hours) and limit circles to selected tracks to maintain spacing
- **Best Fix:** Place circles every 12 hours and distribute them across tracks to preserve separation (e.g., emphasize outermost tracks and space circles across inner tracks) while keeping intensity on the line segments [@liuVisualizingUncertainTropical2019]
