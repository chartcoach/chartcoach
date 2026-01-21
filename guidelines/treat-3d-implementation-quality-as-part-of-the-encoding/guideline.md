---
id: treat-3d-implementation-quality-as-part-of-the-encoding
title: Engineer 3D Carefully to Avoid Self-Inflicted Failures
bibliography: references.bib
description: Treat encoding, interaction, lighting, and typography as critical components
  of 3D success; poor implementation can nullify 3D benefits.
labels:
- task:design
- impact:quality
- data:any
- audience:expert
- complexity:advanced
---

## The Rule <!-- role: advice -->

If you choose 3D, design the encoding, interaction, lighting, and text handling deliberately; do not ship a default/naive 3D implementation.

## The Logic <!-- role: reason -->

The paper argues it is easy to create bad 3D—through poor encoding choices, interaction paradigms, lighting, or unreadable fonts—and that extra care is required so 3D produces net benefit rather than confusion [@brath3DInfoVisHere2014].

- **The Principle:** 3D adds degrees of freedom that amplify both strengths and failures.
- **The Evidence:** [@brath3DInfoVisHere2014]

## Where to Apply <!-- role: context -->

- **User Goal:** Achieve a functional advantage from 3D (separation, surfaces, mental models) without degrading usability.
- **Data Type:** Any specialized 3D visualization intended for real use.
- **Audience:** Teams building production visualization systems [@brath3DInfoVisHere2014].

## When to Break It <!-- role: exceptions -->

- **Scenario:** None—if you cannot invest in these basics, don’t use 3D.
- **Reason:** The implementation risk is high and can negate the intended benefits [@brath3DInfoVisHere2014].

## The Price <!-- role: costs -->

- **The Sacrifice:** More design and engineering time than a comparable 2D view.
- **The Risk:** Without iteration, 3D can fail via navigation confusion, occlusion, poor perception, or unreadable labeling [@brath3DInfoVisHere2014].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Blaming “3D” after deploying poorly lit scenes, awkward navigation modes, or low-legibility type.
- **Why it fails:** The failure may be implementation quality, not the dimensionality itself [@brath3DInfoVisHere2014].

## How to Check <!-- role: check -->

- **Visual Sign:** Users rotate excessively, misread depth/values, can’t select items reliably, or can’t read labels.
- **The Test:** Try key tasks (navigate, select, compare, read labels) under realistic constraints (static screenshot, presentation, single-controller collaboration); if any break, implementation is not robust [@brath3DInfoVisHere2014].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Improve the biggest failure mode first (lighting, navigation mapping, label strategy).
- **Best Fix:** Redesign the 3D experience around domain-typical data structure and user tasks so interaction, cues, and encodings work together as a coherent system [@brath3DInfoVisHere2014].
