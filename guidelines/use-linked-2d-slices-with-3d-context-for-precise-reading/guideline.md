---
id: use-linked-2d-slices-with-3d-context-for-precise-reading
title: Pair 3D Context With 2D Slices for Precision
bibliography: references.bib
description: Use a 3D view for the overall model and coordinated 2D slices for accurate
  estimation and comparison.
labels:
- chart:surface
- task:explore
- task:compare
- visual:position
- impact:clarity
- data:multivariate
- audience:expert
- complexity:advanced
---

## The Rule <!-- role: advice -->

When 3D provides the right mental model but hurts precision, show a linked 3D overview plus coordinated 2D slice views for exact reading.

## The Logic <!-- role: reason -->

A 3D representation can communicate the structure of an information space, while 2D slices allow accurate estimations and comparisons; the 3D view can also act as an index to select which slice to inspect [@brath3DInfoVisHere2014].

- **The Principle:** Combine a 3D mental model with 2D perceptual accuracy.
- **The Evidence:** [@brath3DInfoVisHere2014]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand a multivariate surface/global shape and then read precise values on a chosen cross-section.
- **Data Type:** Surface-like models where slices are meaningful (e.g., valuation surfaces with parameter cuts).
- **Audience:** Professional users performing specialized analysis [@brath3DInfoVisHere2014].

## When to Break It <!-- role: exceptions -->

- **Scenario:** The task does not benefit from a 3D mental model (the 3D view adds no structural understanding).
- **Reason:** You add interface complexity without analytical gain [@brath3DInfoVisHere2014].

## The Price <!-- role: costs -->

- **The Sacrifice:** More screen real estate and coordination complexity.
- **The Risk:** Users may focus on the 3D view and ignore the 2D slice needed for accurate judgments [@brath3DInfoVisHere2014].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Forcing users to read precise values directly off the 3D surface.
- **Why it fails:** Perspective and depth cues reduce the accuracy of length/position judgments compared with a 2D slice [@brath3DInfoVisHere2014].

## How to Check <!-- role: check -->

- **Visual Sign:** Users rotate the 3D view repeatedly to “measure” values.
- **The Test:** If users can’t confidently answer “what’s the value at this point?” without rotating, you need a 2D slice [@brath3DInfoVisHere2014].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a single coordinated 2D cross-section view for the currently selected point/line.
- **Best Fix:** Make the 3D view an interactive index that drives multiple 2D slices targeted to the key analytic questions [@brath3DInfoVisHere2014].
