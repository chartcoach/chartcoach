---
id: ensure-perspective-cues-are-present-when-using-3d-to-support-comparison
title: Ensure perspective cues are present when using 3D to support comparison
bibliography: references.bib
description: Include adequate depth cues (e.g., grids, lighting, motion parallax,
  stereoscopy) so viewers can interpret size and depth correctly in 3D.
labels:
- chart:3d
- task:compare
- visual:depth
- impact:trust
- data:any
- audience:any
- custom:perspective
---

## Provide strong depth cues whenever 3D perspective could distort reading <!-- role: advice -->

When using 3D perspective for quantitative comparison, include depth cues sufficient for viewers to judge depth and size relationships rather than relying on the projected 2D areas.

## Why depth cues counteract misleading interpretations of perspective <!-- role: reason -->

Perspective can change apparent size, but viewers use depth cues to interpret objects as embedded in 3D space; without those cues, comparisons become ambiguous and can be misread.

**Mechanism:** Depth cues (linear perspective references, lighting that reveals shape, stereoscopic viewing, motion parallax, reference planes) help the viewer infer 3D structure and correctly interpret size and distance despite projection distortions.

**Evidence:** Perspective can be criticized as misleading, but with sufficient cues to gauge depth (e.g., reference grids, lighting, stereoscopic viewing, motion parallax, reference planes) viewers can decode 3D objects for comparison, albeit less accurately than a flat 2D common-baseline view [@brath3DInfoVisHere2014].

**Notes:** The goal is not perfect precision but interpretable comparison consistent with the 3D scene.

## When to apply depth-cue reinforcement <!-- role: context -->

- **User Goal:** Compare sizes/lengths in a 3D scene with perspective.
- **Task:** Relative comparison and estimation in 3D.
- **Data:** Any quantitative encoding using 3D position/length where depth affects appearance.
- **Chart Setting:** Perspective-rendered charts (bars, surfaces) in static or interactive formats.
- **Audience:** Any; the risk is perceptual.
- **Success Criterion:** Viewers can explain why an object appears larger/smaller in the image and still interpret the intended value ordering.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The view is orthographic or otherwise avoids perspective distortion. **Why:** The main risk addressed here is perspective-driven misreading [@brath3DInfoVisHere2014].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Extra visual elements (grids/planes/lines) may reduce minimalism. **Risk:** Too many cues can clutter the scene and obscure the data. **Mitigation:** Use only cues that directly support depth interpretation for the chosen encoding.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Using perspective without a reference grid, plane, or lighting that reveals shape. **Why it fails:** Viewers lack information needed to decode depth and may misinterpret size differences [@brath3DInfoVisHere2014].
- **Mistake:** Expecting 3D perspective to support the same accuracy as a 2D shared-baseline plot. **Why it fails:** Perspective reduces precision even when cues exist [@brath3DInfoVisHere2014].

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers interpret nearer objects as larger in value solely because they appear larger on screen. **Quick Check:** Ask users to compare a foreground and background object and explain how they judged depth. **Stronger Test:** Run a small accuracy test on value comparisons with and without added depth cues.

## What to do instead <!-- role: fix -->

- Use a flat 2D projection with a common baseline when comparison accuracy is paramount.
- Add a linked 2D view for precise reading while keeping the 3D view for context.
- Reduce perspective strength (view angle) if distortion dominates the reading.
- Replace discrete 3D objects with a surface/mesh when shape plus shading can convey structure more reliably.
