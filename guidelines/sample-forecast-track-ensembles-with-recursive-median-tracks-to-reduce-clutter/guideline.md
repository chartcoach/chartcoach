---
id: sample-forecast-track-ensembles-with-recursive-median-tracks-to-reduce-clutter
title: Sample forecast track ensembles with recursive median tracks to preserve spread
  while reducing clutter
bibliography: references.bib
description: Construct a small, coherent subset of tracks by recursively extracting
  median paths that partition the ensemble.
labels:
- chart:trajectory
- task:summarize
- visual:position
- impact:clarity
- data:uncertainty
- audience:novice
- complexity:advanced
- domain:tropical-cyclone
---

## Build a representative track subset by recursively extracting median tracks that bisect the ensemble <!-- role: advice -->

Construct a small subset of representative tracks by repeatedly extracting a smoothed median track, partitioning ensemble points into two sides of that track, and recursing on each side. Stop after the desired recursion depth so the subset size is (2^r - 1) tracks.

## Recursive medians preserve spatial distribution while imposing visual organization <!-- role: reason -->

Directly plotting large ensembles can be unreadable because member tracks are irregular and overdrawn, but purely picking random members can preserve the irregularity rather than the meaningful distribution. Recursive median extraction forces each added track to represent a large remaining portion of the distribution, while the bisection creates a structured layout that makes the final set more separable and legible.

**Mechanism:** Each median track captures the central tendency of a partition; recursive left/right partitioning ensures coverage across the ensemble’s cross-track spread while limiting crossings and dense overlap in the displayed set.

**Evidence:** The paper’s recursive sampling framework reconstructs coherent representative tracks that visually match key ensemble density patterns and cross-track spread while reducing clutter compared to randomly selected members [@liuVisualizingUncertainTropical2019].

**Notes:** The method is intended for cases where preserving exact individual member shapes is not important, but preserving the ensemble’s spatial distribution is.

## When this applies: large, irregular ensembles that cannot be drawn directly <!-- role: context -->

- **User Goal:** See plausible paths and overall uncertainty without spaghetti-plot clutter.
- **Task:** Overview the distribution of possible trajectories across time.
- **Data:** Large track ensemble (e.g., ~1,000 members) with irregular, crossing trajectories.
- **Chart Setting:** Static or lightly interactive map display with limited screen space.
- **Audience:** Mixed expertise; needs readable, structured display.
- **Success Criterion:** Subset reflects cross-track spread and central density patterns without heavy overdraw.

## When not to follow it: when speed/along-track timing uncertainty must be preserved by design <!-- role: exceptions -->

**Break it when:** The audience must see uncertainty in forward speed (arrival time) expressed as variation in how far tracks progress at a given time. **Why:** The representative median-track reconstruction preserves directional spread well but does not preserve along-track (speed) distribution in the same way [@liuVisualizingUncertainTropical2019].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may lose fidelity to individual simulated track shapes and along-track speed variability. **Risk:** Deep recursion can produce invalid/undersampled median tracks in small partitions. **Mitigation:** Limit subset size to be much smaller than the ensemble, and filter out reconstructed tracks with too few time samples.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Randomly selecting a handful of original ensemble members and expecting them to be readable. **Why it fails:** Individual Monte Carlo members can be irregular and crossing, creating clutter without improving distribution understanding.
- **Mistake:** Increasing recursion until you nearly match the original ensemble size. **Why it fails:** Small partitions become under-sampled and can yield poor or invalid reconstructed tracks.

## Quick tests <!-- role: check -->

**Failure Sign:** The subset under-represents the ensemble’s cross-track spread or produces many short/broken reconstructed tracks. **Quick Check:** Compare point distributions at selected forecast times; the subset should cover the central high-density region and approximate cross-track outliers. **Stronger Test:** Render both ensemble and subset as thin lines and visually compare density patterns over the map.

## What to do instead <!-- role: fix -->

- Reduce the target subset size (use fewer recursion levels) so each partition remains well-sampled.
- Filter out reconstructed tracks that contain substantially fewer time samples than the original tracks.
- If forward-speed uncertainty must be shown, use a point-based display at specific times rather than relying on time-parameterized reconstructed tracks.
- Add interaction to switch between overview subset tracks and time-slice point distributions.
