---
id: use-3d-transitions-to-maintain-object-constancy-between-2d-views
title: Animate Through 3D to Preserve Object Constancy
bibliography: references.bib
description: Use 3D transition animations between familiar 2D charts to help viewers
  track elements and understand relationships.
labels:
- chart:bar
- chart:line
- task:explain
- task:trace
- visual:motion
- impact:comprehension
- data:multivariate
- audience:general
- complexity:advanced
---

## The Rule <!-- role: advice -->

When switching between two related 2D chart types, animate the change through a 3D transition so viewers can track the same objects across views.

## The Logic <!-- role: reason -->

Animated transitions can reduce cognitive burden by letting viewers use motion to visually track objects rather than re-reading labels; a 3D transition can provide object constancy between two familiar 2D representations and can reduce some occlusion issues during transformation [@brath3DInfoVisHere2014].

- **The Principle:** Use motion-driven object constancy to support correspondence.
- **The Evidence:** [@brath3DInfoVisHere2014]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand how two representations relate (e.g., a time series view vs a categorical summary).
- **Data Type:** Multidimensional datasets where different projections are useful (e.g., company revenue over time vs revenue by company).
- **Audience:** Viewers who benefit from explanation and continuity (presentations, exploratory UI) [@brath3DInfoVisHere2014].

## When to Break It <!-- role: exceptions -->

- **Scenario:** Transition creates heavy occlusion/confusion mid-animation.
- **Reason:** If objects become indistinguishable during motion, object tracking fails [@brath3DInfoVisHere2014].

## The Price <!-- role: costs -->

- **The Sacrifice:** Time to animate and added implementation complexity.
- **The Risk:** The intermediate 3D state may distract or be misread as a meaningful data view [@brath3DInfoVisHere2014].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Abruptly switching chart types with no transition.
- **Why it fails:** Viewers must re-establish correspondence by re-reading labels, increasing cognitive load [@brath3DInfoVisHere2014].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers lose track of which mark became which after the change.
- **The Test:** Ask a viewer to follow a specific entity across the transition; if they can’t, object constancy is broken [@brath3DInfoVisHere2014].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a smooth transition that preserves mark identity across frames.
- **Best Fix:** Use a 3D transition path that reduces mid-transition occlusion while exposing a coherent relationship between the two 2D encodings [@brath3DInfoVisHere2014].
