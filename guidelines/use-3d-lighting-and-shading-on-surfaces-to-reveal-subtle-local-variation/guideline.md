---
id: use-3d-lighting-and-shading-on-surfaces-to-reveal-subtle-local-variation
title: Use 3D lighting and shading on surfaces to reveal subtle local variation
bibliography: references.bib
description: Apply effective lighting on 3D surfaces so shading/specular highlights
  expose subtle structural deviations that uniform fills can hide.
labels:
- chart:surface
- task:detect
- visual:lighting
- impact:clarity
- data:quantitative
- audience:expert
- complexity:advanced
---

## Light 3D surfaces to make deviations visible <!-- role: advice -->

Use a well-lit 3D surface with shading and highlights when you need viewers to see subtle local variations that are hard to detect with uniform shading or flat 2D encodings.

## Why lighting makes anomalies pop on 3D geometry <!-- role: reason -->

Lighting converts small geometric changes into visible intensity changes, allowing local structure to be perceived without adding extra encodings that may obscure global form.

**Mechanism:** Shading and specular highlights act as visual derivatives of the surface shape, exposing ridges, bumps, and day-to-day irregularities as changes in reflected light.

**Evidence:** A surface representation with shading/highlights can reveal local structure in interest-rate data more clearly than a bar representation where each face has uniform shade, while still preserving the global surface form [@brath3DInfoVisHere2014].

**Notes:** Lighting can also be done poorly; the benefit depends on avoiding simplistic lighting setups that reduce shape legibility.

## When to use lighting-driven surface emphasis <!-- role: context -->

- **User Goal:** Notice subtle departures from an expected smooth pattern while keeping context.
- **Task:** Detect anomalies, texture, and local change on a continuous field.
- **Data:** Quantitative field that forms a surface; small local changes are meaningful.
- **Chart Setting:** 3D rendering environment where lighting can be controlled.
- **Audience:** Analysts accustomed to reading shape from shading cues.
- **Success Criterion:** Local deviations are visible without sacrificing the global trend.

## When not to use it <!-- role: exceptions -->

**Break it when:** You cannot control lighting quality (or the renderer forces poor lighting). **Why:** Bad lighting can hide structure or mislead the viewer about shape [@brath3DInfoVisHere2014].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Lighting adds visual complexity and can distract if overdone. **Risk:** Viewers may interpret lighting artifacts as data features. **Mitigation:** Keep lighting consistent and avoid effects that create false edges.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Using a bar grid with uniform face shading for a task that depends on seeing fine variation. **Why it fails:** Uniform shading suppresses cues to subtle shape differences [@brath3DInfoVisHere2014].
- **Mistake:** Using simplistic lighting (e.g., single headlight) that flattens form. **Why it fails:** Shape cues become weak and local anomalies are less perceptible [@brath3DInfoVisHere2014].

## Quick tests <!-- role: check -->

**Failure Sign:** The surface looks flat, and users can’t point to small bumps/creases that exist in the data. **Quick Check:** Toggle lighting on/off and confirm that structure becomes easier to see with lighting on. **Stronger Test:** Measure anomaly detection accuracy with the chosen lighting versus a flat color surface.

## What to do instead <!-- role: fix -->

- Use a 2D derived-difference view when the task is only local change and global form is not needed.
- Add explicit projection lines or reference cues to support decoding the surface when lighting is insufficient.
- Use a linked 2D slice view for precise comparison while keeping the 3D surface for structure.
- Reduce surface noise (aggregation/smoothing) if lighting emphasizes irrelevant texture.
