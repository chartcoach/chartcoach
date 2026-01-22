---
id: pair-3d-context-with-linked-2d-slices-for-precise-reading
title: Pair 3D context with linked 2D slices for precise reading
bibliography: references.bib
description: Use a 3D view as a mental model and index, and provide coordinated 2D
  slice views to support accurate estimation and comparison.
labels:
- chart:surface
- task:inspect
- visual:position
- impact:accuracy
- data:multivariate
- audience:expert
- custom:linked-views
---

## Combine a 3D overview with coordinated 2D slice views <!-- role: advice -->

Use a linked 3D+2D design where the 3D view provides global context and selection, and a coordinated 2D view provides a precise slice for reading and comparison.

## Why context-plus-slice balances mental model and precision <!-- role: reason -->

3D can help users understand the structure of an information space as a coherent object, while 2D slices preserve the high precision of common-baseline comparisons for specific cross-sections.

**Mechanism:** The 3D representation supports orientation and conceptual understanding of how dimensions relate, and the 2D slice reduces perspective and occlusion issues when users need exact readings.

**Evidence:** A deployed professional application uses a 3D surface for overall valuation context and a 2D slice through the surface for accurate estimation and comparison, with the 3D view acting as context and index [@brath3DInfoVisHere2014].

**Notes:** This pattern generalizes beyond surfaces to other 3D forms when a “detail view” can be defined.

## When to apply 3D context + 2D focus <!-- role: context -->

- **User Goal:** Understand a multidimensional shape while reading exact values in a subset.
- **Task:** Explore a 3D representation and then make precise judgments on selected sections.
- **Data:** Multidimensional data where meaningful slices exist (e.g., fixing one variable).
- **Chart Setting:** Interactive system that supports coordinated selection between views.
- **Audience:** Professional/analytic users who need both intuition and precision.
- **Success Criterion:** Users navigate with the 3D model but rely on the 2D slice for accurate reading.

## When not to use it <!-- role: exceptions -->

**Break it when:** The workflow cannot support interaction or coordination between views. **Why:** The 3D view alone may require navigation to be comprehensible, and the precision benefit of the 2D slice would be unavailable [@brath3DInfoVisHere2014].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** More screen space and implementation complexity than a single chart. **Risk:** Users may become confused if the slice is not clearly linked to the 3D selection. **Mitigation:** Keep the linkage explicit through coordinated highlighting and consistent scales.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Using only a 3D view for tasks that require accurate value estimation. **Why it fails:** Perspective and occlusion reduce precision compared to 2D slices [@brath3DInfoVisHere2014].
- **Mistake:** Showing a 2D slice without a clear mapping back to the 3D context. **Why it fails:** The user loses the mental model benefit that motivates the 3D view [@brath3DInfoVisHere2014].

## Quick tests <!-- role: check -->

**Failure Sign:** Users repeatedly rotate the 3D view to “measure” values. **Quick Check:** Confirm that selecting a point/region in 3D immediately yields a readable 2D slice. **Stronger Test:** Measure accuracy of value comparisons using the 2D slice versus the 3D view alone.

## What to do instead <!-- role: fix -->

- Use only 2D views (small multiples or coordinated charts) when a stable 3D mental model is not needed.
- Use a 3D view only for presentation of overall form when precise analysis is out of scope.
- Use computed summaries (e.g., a derived curve) if a meaningful slice cannot be defined.
- Reduce dimensionality so the key relationship fits in a single precise 2D chart.
