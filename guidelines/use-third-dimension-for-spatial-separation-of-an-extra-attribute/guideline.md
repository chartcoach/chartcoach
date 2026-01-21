---
id: use-third-dimension-for-spatial-separation-of-an-extra-attribute
title: Use the Third Dimension to Separate Overlapping Events
bibliography: references.bib
description: Map an additional attribute (such as time) to the third axis to reduce
  overlap and reveal structure that is hidden in 2D.
labels:
- chart:scatter
- chart:space-time-cube
- task:trace
- task:detect
- visual:position
- impact:clarity
- data:temporal
- data:geospatial
- audience:expert
- complexity:intermediate
---

## The Rule <!-- role: advice -->

When 2D plots collapse events into overlap, map an extra attribute (e.g., time) onto the third axis to create spatial separation.

## The Logic <!-- role: reason -->

The extra spatial dimension can separate items that would otherwise coincide in 2D, making trajectories or oscillations perceptible without relying on weak encodings like brightness for time [@brath3DInfoVisHere2014].

- **The Principle:** Use dimensional separation instead of overloading color/brightness.
- **The Evidence:** [@brath3DInfoVisHere2014]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand geotemporal movement patterns (what happened when and where).
- **Data Type:** Many events at similar locations across time; “hairball”-prone 2D views.
- **Audience:** Domain professionals doing analysis (e.g., geotemporal analytic tasks) [@brath3DInfoVisHere2014].

## When to Break It <!-- role: exceptions -->

- **Scenario:** The visualization must work as a static snapshot (no interaction) in a collaborative/presentation setting.
- **Reason:** If comprehension requires navigation, static use becomes a failure mode [@brath3DInfoVisHere2014].

## The Price <!-- role: costs -->

- **The Sacrifice:** More complex navigation and viewpoint management.
- **The Risk:** Users may misread depth or miss items outside the viewing frustum [@brath3DInfoVisHere2014].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Encoding time only with brightness in 2D.
- **Why it fails:** Overlap remains and motion/ordering is hard to perceive even with brightness changes [@brath3DInfoVisHere2014].

## How to Check <!-- role: check -->

- **Visual Sign:** In 2D, points stack on top of each other and movement is ambiguous.
- **The Test:** Compare a 2D view vs 3D with time as height—if oscillations/paths become immediately visible in 3D, separation is working [@brath3DInfoVisHere2014].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a third axis mapped to the separating attribute (commonly time).
- **Best Fix:** Design the 3D layout so key patterns remain readable from a primary viewpoint without excessive navigation [@brath3DInfoVisHere2014].
