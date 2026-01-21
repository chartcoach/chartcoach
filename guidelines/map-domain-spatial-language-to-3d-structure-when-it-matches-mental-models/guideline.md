---
id: map-domain-spatial-language-to-3d-structure-when-it-matches-mental-models
title: Map Domain Spatial Concepts Directly Into 3D Layout
bibliography: references.bib
description: Use 3D layouts when domain language and reasoning already use spatial
  concepts like opposite, close, and orthogonal.
labels:
- chart:network
- task:relate
- task:cluster
- visual:position
- impact:comprehension
- data:relational
- audience:expert
- complexity:advanced
---

## The Rule <!-- role: advice -->

Choose a 3D spatial layout when it directly matches the domain’s conceptual language (e.g., opposite, close, orthogonal), and use that geometry to make relationships intuitive.

## The Logic <!-- role: reason -->

If users already think and speak in spatial terms, a 3D layout can externalize that mental model—e.g., placing correlated items close, inversely correlated items on opposite sides of a sphere, and uncorrelated items between—so the geometry itself communicates meaning; the same force-directed layout on a 2D plane can make “opposite” ambiguous and introduce edge/center bias [@brath3DInfoVisHere2014].

- **The Principle:** Align spatial encoding with users’ existing mental models and vocabulary.
- **The Evidence:** [@brath3DInfoVisHere2014]

## Where to Apply <!-- role: context -->

- **User Goal:** Reason about relationships like similarity, inversion, and orthogonality.
- **Data Type:** Relational measures that naturally map to “near/far/opposite” (e.g., correlations).
- **Audience:** Domain experts whose workflows already use these spatial metaphors [@brath3DInfoVisHere2014].

## When to Break It <!-- role: exceptions -->

- **Scenario:** The same relationship concepts cannot be made legible without heavy interaction or strong depth cues.
- **Reason:** If viewers can’t reliably decode 3D position, the mental-model advantage collapses [@brath3DInfoVisHere2014].

## The Price <!-- role: costs -->

- **The Sacrifice:** Increased complexity in navigation and potential occlusion.
- **The Risk:** Users may misinterpret depth or miss relationships if the view is not comprehensible from key angles [@brath3DInfoVisHere2014].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Forcing a 2D layout for relationships that depend on “opposite” semantics.
- **Why it fails:** “Opposite side” is not well-defined in 2D and the layout can be constrained, creating ambiguity and perceptual bias toward the center [@brath3DInfoVisHere2014].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers can’t confidently identify “inverse” vs “unrelated” items from the layout.
- **The Test:** Pick a target item and ask users to find the most inverse item; if the answer isn’t visually obvious, the mapping is failing [@brath3DInfoVisHere2014].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Move from a 2D plane to a 3D spherical layout where “opposite” is geometrically explicit.
- **Best Fix:** Design interaction/viewpoints so any node’s “opposite” and neighborhood remain discoverable and stable in the 3D geometry [@brath3DInfoVisHere2014].
