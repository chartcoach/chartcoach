---
id: annotate-representative-tracks-with-interpolated-auxiliary-fields-before-rendering
title: Annotate representative tracks by interpolating auxiliary fields per time step
  and resampling onto the tracks
bibliography: references.bib
description: Preserve non-spatial ensemble variables by interpolating spatial fields
  at each time and sampling them along representative tracks.
labels:
- chart:trajectory
- task:encode-multivariate
- visual:color
- impact:clarity
- data:multivariate
- audience:novice
- complexity:advanced
- domain:tropical-cyclone
---

## Interpolate storm attributes into per-time spatial fields and sample them onto displayed tracks <!-- role: advice -->

Compute a continuous spatial field for each non-position variable at every forecast time step using interpolation over ensemble points, then annotate each displayed track point by sampling those fields at the point’s location. Use these sampled values for visual encodings (e.g., intensity color, size glyph radius) on the representative tracks.

## Field-based resampling preserves attribute patterns without forcing attribute-preserving track selection <!-- role: reason -->

A representative subset chosen to preserve spatial distribution will not automatically preserve distributions of other variables (e.g., size, intensity). Building continuous fields from the full ensemble at each time step transfers the ensemble’s auxiliary-variable structure onto the displayed subset, letting the subset remain spatially representative and visually organized while still conveying multivariate information.

**Mechanism:** Interpolation aggregates attribute values across the full ensemble at each time into a spatially varying function; sampling that function on the displayed paths decouples “which tracks you draw” from “which attribute values you show.”

**Evidence:** The workflow constructs representative tracks first, then uses Radial Basis Function (RBF) interpolation per time step for variables like storm size and intensity, and finally annotates representative track points by sampling the interpolated fields [@liuVisualizingUncertainTropical2019].

**Notes:** The paper uses an approach that reduces overfitting by computing RBF weights on a subset of points selected to minimize squared error.

## When this applies: path ensembles with important per-point attributes <!-- role: context -->

- **User Goal:** Understand where/when the phenomenon may occur and what its attributes may be there.
- **Task:** Read multivariate risk along possible paths.
- **Data:** Tracks with attached quantitative attributes per time (e.g., wind intensity, storm size).
- **Chart Setting:** Representative subset display where attributes must be shown without clutter.
- **Audience:** Mixed expertise; needs interpretable attribute cues.
- **Success Criterion:** Displayed tracks show plausible attribute variation consistent with the full ensemble.

## When not to follow it: when interpolation artifacts would be operationally misleading <!-- role: exceptions -->

**Break it when:** Interpolation is known to violate domain constraints (e.g., landfall-driven intensity drops) or can create invalid combinations (e.g., non-zero hurricane-force radius when intensity is below hurricane strength). **Why:** Field interpolation can smooth or decouple variables in ways that misrepresent physically constrained relationships [@liuVisualizingUncertainTropical2019].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You add computational complexity (per-time-step interpolation systems). **Risk:** Interpolation can understate sharp transitions and may produce physically inconsistent attribute pairs. **Mitigation:** Treat interpolated annotations as approximations and validate against domain expectations.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Assuming a spatially representative track subset will also be representative for intensity/size without additional processing. **Why it fails:** The sampling objective preserves spatial distribution, not auxiliary-variable distributions.

## Quick tests <!-- role: check -->

**Failure Sign:** Annotated attributes appear implausible (e.g., size rings present when intensity indicates weak storms) or fail to reflect known patterns around land interaction. **Quick Check:** Compare sampled attribute values on representative tracks against ensemble statistics at matching times. **Stronger Test:** Have domain experts review whether annotated changes over time (e.g., weakening after landfall) are reflected appropriately.

## What to do instead <!-- role: fix -->

- Interpolate each attribute separately per time step using the full ensemble’s points for that time.
- Sample the interpolated attribute fields onto the representative tracks at matching times and locations.
- Validate annotated tracks against time-slice distributions (e.g., attribute histograms at specific forecast times).
- If interpolation causes invalid combinations, constrain or post-process sampled values to respect known domain rules.
