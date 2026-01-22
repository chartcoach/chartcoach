---
id: avoid-3d-text-as-a-primary-carrier-of-information-on-low-resolution-displays
title: Avoid 3D text as a primary carrier of information on low-resolution displays
bibliography: references.bib
description: Do not rely on small 3D-rendered fonts for essential reading when display
  resolution and rendering make them muddy compared to 2D text.
labels:
- chart:3d
- task:read
- visual:text
- impact:accessibility
- data:any
- audience:any
- custom:typography
---

## Do not make critical labels depend on small 3D-rendered text at low resolution <!-- role: advice -->

Avoid using 3D-rendered fonts as the primary way to convey essential labels or values when the display resolution and rendering quality make the text hard to read.

## Why 3D fonts can degrade legibility relative to 2D text rendering <!-- role: reason -->

On low-resolution displays, 2D text benefits from specialized subpixel rendering optimizations, while 3D text often relies on simpler antialiasing that can blur fine typographic detail and letter spacing.

**Mechanism:** Reduced pixel density and lack of 2D subpixel optimizations cause thin strokes, serifs, and counters to render poorly in 3D, lowering readability for small type.

**Evidence:** Small 3D text can be significantly less readable than comparable 2D text on low-resolution displays due to differences in rendering approaches, while higher-resolution displays make detailed rendering more feasible [@brath3DInfoVisHere2014].

**Notes:** Labelling in 3D is further complicated by changing viewpoints that affect contrast, occlusion, and orientation.

## When this applies <!-- role: context -->

- **User Goal:** Read labels reliably and quickly.
- **Task:** Identify items, read annotations, or interpret text-based encodings.
- **Data:** Any visualization where labels are required for understanding.
- **Chart Setting:** 3D scenes with potentially changing camera angles; especially low-PPI displays.
- **Audience:** General audiences, including users with limited visual acuity.
- **Success Criterion:** Labels remain legible without zooming or repositioning the camera.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The display environment provides sufficiently high resolution such that 3D text remains clear at the required size. **Why:** Higher pixel density supports finer typographic detail and improved legibility [@brath3DInfoVisHere2014].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Reducing 3D text may reduce direct in-scene labeling. **Risk:** Removing labels can harm interpretability if no alternative is provided. **Mitigation:** Use alternative label delivery that is not view-dependent.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Placing many small labels directly on 3D objects in the scene. **Why it fails:** Rendering and viewpoint changes can make labels muddy, occluded, or poorly oriented [@brath3DInfoVisHere2014].
- **Mistake:** Assuming higher aesthetic appeal of 3D text guarantees readability. **Why it fails:** Legibility depends on resolution, rendering, and background contrast, not dimensionality [@brath3DInfoVisHere2014].

## Quick tests <!-- role: check -->

**Failure Sign:** Users need to zoom in just to read labels. **Quick Check:** View the scene at the most common camera angle and verify label legibility at typical viewing distance. **Stronger Test:** Run a timed label-finding task and track error rate.

## What to do instead <!-- role: fix -->

- Render labels in a coordinated 2D overlay or separate 2D view rather than embedding them as 3D geometry.
- Reduce label density by showing labels on demand through interaction (e.g., selection/hover) when interaction exists.
- Increase effective resolution or font size when 3D text must be used.
- Use a secondary device/view for text if the 3D scene cannot keep labels readable.
