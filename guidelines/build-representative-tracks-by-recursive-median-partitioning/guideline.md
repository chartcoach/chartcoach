---
id: build-representative-tracks-by-recursive-median-partitioning
title: Sample Ensembles with Recursive Median Tracks to Preserve Spatial Distribution
bibliography: references.bib
description: Construct a small, representative, spatially organized set of tracks
  by repeatedly extracting median tracks and partitioning left/right.
labels:
- chart:trajectory
- task:summarize
- visual:position
- impact:clarity
- data:ensemble
- audience:expert
- complexity:advanced
- domain:tropical-cyclone
- source:liu-2019
---

## The Rule <!-- role: advice -->

Create a representative subset of forecast tracks by (1) extracting a median track across time, (2) partitioning the ensemble into left/right groups around that track, and (3) recursively repeating to get (2^r-1) representative tracks.

## The Logic <!-- role: reason -->

A recursively extracted set of median tracks preserves the ensemble’s spatial distribution at each time step while producing a coherent layout that reduces crossings and clutter compared to sampling raw members.

- **The Principle:** Distribution-preserving representative sampling
- **The Evidence:** [@liuVisualizingUncertainTropical2019]

## Where to Apply <!-- role: context -->

- **User Goal:** See the main modes/spread of potential paths without spaghetti clutter
- **Data Type:** Large ensembles of time-parameterized tracks (e.g., 1,000 paths with hourly samples)
- **Audience:** Visualization builders and analysts producing public-facing summaries

## When to Break It <!-- role: exceptions -->

- **Scenario:** Individual member track geometry is meaningful and must be preserved
- **Reason:** The approach reconstructs new, smoothed representative tracks and does not retain original member shapes [@liuVisualizingUncertainTropical2019]

## The Price <!-- role: costs -->

- **The Sacrifice:** Added algorithmic complexity (depth computation, smoothing, recursive partitioning)
- **The Risk:** If pushed to very high sample counts, under-sampled partitions can yield invalid/unstable median tracks [@liuVisualizingUncertainTropical2019]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Randomly select “representative-looking” original tracks
- **Why it fails:** Original NHC Monte Carlo members can be irregular, self-crossing, and visually incoherent, undermining interpretation [@liuVisualizingUncertainTropical2019]

## How to Check <!-- role: check -->

- **Visual Sign:** Representative tracks should reproduce the ensemble’s cross-track spread and densest regions without heavy crossings
- **The Test:** Overlay representative tracks and the full ensemble; the subset should match the ensemble’s main spatial footprint perpendicular to motion [@liuVisualizingUncertainTropical2019]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Increase recursion level modestly (e.g., 7 → 15 tracks) to better cover spread without returning to clutter
- **Best Fix:** Use the full recursive pipeline (median extraction + left/right partitioning + recursion) and filter invalid short tracks when partitions become sparse [@liuVisualizingUncertainTropical2019]
