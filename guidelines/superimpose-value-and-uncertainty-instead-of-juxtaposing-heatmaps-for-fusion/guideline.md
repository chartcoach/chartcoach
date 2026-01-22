---
id: superimpose-value-and-uncertainty-instead-of-juxtaposing-heatmaps-for-fusion
title: Superimpose value and uncertainty in one map (not two juxtaposed maps) for
  information-fusion tasks
bibliography: references.bib
description: Avoid juxtaposed value/uncertainty maps when users must integrate both
  variables to make a single judgment.
labels:
- chart:heatmap
- task:identify
- visual:color
- impact:accuracy
- data:quantitative
- audience:general
- uncertainty:explicit
- layout:juxtaposition
---

## Superimpose value and uncertainty encodings when users must fuse them <!-- role: advice -->

Superimpose value and uncertainty in a single chart when a task requires integrating both at the same location. Avoid splitting value and uncertainty into separate side-by-side heatmaps for these fusion tasks.

## Why juxtaposition increases errors in fusion tasks <!-- role: reason -->

Juxtaposition forces viewers to perform correspondence across two displays, effectively adding an additional search-and-match step before they can interpret a single location. This added step increases error when value and uncertainty patterns do not provide shared landmarks.

**Mechanism:** Requiring cross-map matching introduces opportunities for misalignment and memory error during the search process.

**Evidence:** In a location-identification task with value and uncertainty, superimposed designs achieved higher accuracy than juxtaposed univariate maps (58% vs. 51%) [@correllValueSuppressingUncertaintyPalettes2018]. The performance cost was attributed to the extra search required to connect locations across separate maps [@correllValueSuppressingUncertaintyPalettes2018].

**Notes:** The result was observed in a setting where value and uncertainty were not strongly correlated, reducing natural landmarks for correspondence.

## When superposition is the right default <!-- role: context -->

- **User Goal:** Read both value and uncertainty for the same region/item to make a single judgment.
- **Task:** Identify or select locations meeting combined criteria (value and uncertainty together).
- **Data:** Dense grid or spatial regions where each cell/area has both value and uncertainty.
- **Chart Setting:** Static or low-interaction displays where cross-highlighting is unavailable.
- **Audience:** General audiences performing quick, repeated lookups.
- **Success Criterion:** Higher identification accuracy and fewer mismatches between value and uncertainty.

## When to allow juxtaposed maps anyway <!-- role: exceptions -->

- **Break it when:** Users need to separately study the global patterns of value and uncertainty rather than combine them per-location. **Why:** Separate maps can support independent pattern reading without interference from bivariate encodings.

## Tradeoffs of superposition <!-- role: costs -->

**Sacrifice:** Superposition increases encoding complexity and may require a bivariate legend. **Risk:** Poorly designed bivariate encodings can be hard to decode, especially with continuous scales. **Mitigation:** Use discrete encodings and keep the legend interpretable.

## Common mistakes with superposition vs. juxtaposition <!-- role: mistakes -->

- **Mistake:** Using juxtaposed maps for a task phrased as “find the place with value X and uncertainty Y.” **Why it fails:** The task becomes an error-prone cross-chart matching exercise.
- **Mistake:** Assuming juxtaposition is always easier because each legend is univariate. **Why it fails:** The integration burden can outweigh the simplicity of separate legends.

## Quick checks for fusion-readiness <!-- role: check -->

**Failure Sign:** Users point to correct value regions but wrong uncertainty regions (or vice versa). **Quick Check:** Count how many times users must look back and forth between charts to answer a single combined query. **Stronger Test:** Run a short identification task; if accuracy drops with juxtaposition, switch to a superimposed design.

## What to do instead when superposition is impractical <!-- role: fix -->

- Add linked interaction (e.g., hover/selection highlighting across maps) to reduce correspondence errors in juxtaposed designs.
- Use explicit encoding that collapses value and uncertainty into one derived metric when users only need one decision variable.
- Reduce density (aggregate or filter) so shared landmarks are clearer if juxtaposition must be kept.
- Replace the task flow: inspect uncertainty separately first, then make value comparisons only within acceptable-uncertainty regions.
