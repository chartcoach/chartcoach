---
id: design-3d-to-manage-occlusion-instead-of-assuming-its-unique
title: Treat Occlusion as a Design Variable in 3D
bibliography: references.bib
description: Plan for occlusion in 3D by leveraging data distributions and layouts
  where overlap remains low, rather than dismissing 3D categorically.
labels:
- task:explore
- impact:clarity
- data:any
- audience:expert
- complexity:intermediate
---

## The Rule <!-- role: advice -->

Use 3D only when you can keep occlusion low through dataset characteristics or layout choices; don’t assume occlusion automatically invalidates 3D.

## The Logic <!-- role: reason -->

Occlusion exists in both 2D (overplotting, overlapping bubbles) and 3D; in specialized domains, typical data distributions (e.g., long-tail) and expected patterns can keep occlusion manageable so major structure and anomalies remain visible [@brath3DInfoVisHere2014].

- **The Principle:** Manage overlap by matching representation to expected data structure.
- **The Evidence:** [@brath3DInfoVisHere2014]

## Where to Apply <!-- role: context -->

- **User Goal:** Preserve visibility of large patterns and anomalies while using 3D benefits (height, separation, surfaces).
- **Data Type:** Datasets with predictable structure/distributions where occlusion can be anticipated.
- **Audience:** Designers building specialized, domain-targeted 3D visualizations [@brath3DInfoVisHere2014].

## When to Break It <!-- role: exceptions -->

- **Scenario:** The dataset commonly produces dense, uniform occlusion from most viewpoints.
- **Reason:** Overlap overwhelms the encoding and forces excessive navigation/interaction [@brath3DInfoVisHere2014].

## The Price <!-- role: costs -->

- **The Sacrifice:** Freedom to use arbitrary 3D layouts.
- **The Risk:** A change in dataset characteristics can suddenly make a previously workable 3D view unreadable [@brath3DInfoVisHere2014].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Declaring “3D is bad because occlusion” without checking whether 2D already suffers from occlusion too.
- **Why it fails:** It ignores that occlusion is not unique to 3D and may be addressable by designing for typical domain data [@brath3DInfoVisHere2014].

## How to Check <!-- role: check -->

- **Visual Sign:** Important items are frequently hidden or only discoverable after extensive rotation.
- **The Test:** Test multiple representative datasets; if occlusion spikes for typical cases (not edge cases), the 3D design is not robust [@brath3DInfoVisHere2014].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Adjust camera defaults and layout to reduce overlap in the most common cases.
- **Best Fix:** Redesign the visualization around domain-typical structure (e.g., long-tail expectations, regular intervals, anchored geometry) so occlusion stays predictably low [@brath3DInfoVisHere2014].
