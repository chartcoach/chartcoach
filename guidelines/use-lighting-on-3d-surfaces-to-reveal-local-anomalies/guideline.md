---
id: use-lighting-on-3d-surfaces-to-reveal-local-anomalies
title: Use Surface Lighting to Reveal Subtle Variations
bibliography: references.bib
description: Apply effective lighting and shading on 3D surfaces to make small surface
  deviations perceptible.
labels:
- chart:surface
- task:detect
- visual:lighting
- impact:clarity
- data:continuous
- audience:expert
- complexity:advanced
---

## The Rule <!-- role: advice -->

For 3D surfaces, use lighting and shading that produces highlights and gradients to expose subtle local anomalies.

## The Logic <!-- role: reason -->

3D renderers provide lighting models that can make small changes in surface orientation visible via shading/specular highlights; this can reveal local structure that uniform-color faces (e.g., bar sides) hide, while still communicating global form [@brath3DInfoVisHere2014].

- **The Principle:** Use illumination as a perceptual amplifier for surface curvature and micro-structure.
- **The Evidence:** [@brath3DInfoVisHere2014]

## Where to Apply <!-- role: context -->

- **User Goal:** See both broad surface shape and small day-to-day (or local) deviations.
- **Data Type:** Surface-like data where local change matters (e.g., rates over time).
- **Audience:** Analysts doing pattern/anomaly inspection [@brath3DInfoVisHere2014].

## When to Break It <!-- role: exceptions -->

- **Scenario:** The scene is lit in a way that flattens form (e.g., simplistic headlight/single directional setups).
- **Reason:** Bad lighting reduces shape perception, undermining the benefit of using a surface [@brath3DInfoVisHere2014].

## The Price <!-- role: costs -->

- **The Sacrifice:** More design effort; lighting choices become part of the encoding.
- **The Risk:** Poor lighting can mislead or hide key variation [@brath3DInfoVisHere2014].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a surface but rendering it with flat, uniform shading.
- **Why it fails:** Without shading variation, the viewer loses cues needed to see subtle changes [@brath3DInfoVisHere2014].

## How to Check <!-- role: check -->

- **Visual Sign:** The surface looks visually flat; small bumps/creases are not visible.
- **The Test:** Rotate the light/view slightly—if structure “pops” only then, your default lighting is insufficient [@brath3DInfoVisHere2014].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Adjust lighting to create readable gradients and highlights on the surface.
- **Best Fix:** Iterate lighting to preserve both global shape readability and local anomaly visibility in the primary view [@brath3DInfoVisHere2014].
