---
id: prefer-3d-volume-over-3d-surface-when-using-3d
title: Prefer 3D volume graphs over 3D surface graphs when adding depth cues
bibliography: references.bib
description: If using 3D styling for 2D data, choose volume-rendered forms rather
  than floating surface forms.
labels:
- chart:bar
- task:communicate
- visual:depth
- impact:preference
- data:quantitative
- audience:novice
- complexity:intermediate
---

## Choose 3D volume instead of 3D surface when using 3D <!-- role: advice -->

If you decide to use a 3D-styled chart for 2D data, use a 3D volume rendering rather than a 3D surface rendering.

## Why volume renderings are preferred to surface renderings <!-- role: reason -->

Different “3D” treatments are not interchangeable: viewers distinguish between depth that creates a solid-looking object and depth that creates a floating surface, and they show consistent preferences between them.

**Mechanism:** Volume renderings read as more concrete objects, while surface renderings can appear less grounded, affecting perceived suitability.

**Evidence:** In preference selections, 3D volume variants were chosen more often than 3D surface variants within both line and bar families, and this difference appeared consistently across scenarios [@levyGratuitousGraphicsPutting1996].

**Notes:** The surveys treated “volume” and “surface” as distinct categories and found substantial preference differences.

## When this applies <!-- role: context -->

- **User Goal:** Use 3D styling for rhetorical impact, memorability, or presentation.
- **Task:** Communicate or emphasize content using depth cues.
- **Data:** 2D quantitative data where depth does not encode additional variables.
- **Chart Setting:** Slideware or packaged visualization tools offering multiple 3D styles.
- **Audience:** General audiences who will interpret “3D-ness” holistically.
- **Success Criterion:** Preference, acceptance, and perceived suitability of the display style.

## When not to follow it <!-- role: exceptions -->

**Break it when:** You are not using 3D at all. **Why:** The rule is only about choosing among 3D styles once depth cues have already been selected [@levyGratuitousGraphicsPutting1996].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Volume styling can add visual mass and occupy more apparent space. **Risk:** The chart can feel heavier or more decorative than necessary. **Mitigation:** Use volume styling only when the scenario benefits (for example, memorability-focused use).

## Common failure modes <!-- role: mistakes -->

**Mistake:** Treating “3D graphs” as one uniform design option. **Why it fails:** Viewers’ preferences differed strongly between volume and surface 3D forms, indicating that the 3D subtype matters [@levyGratuitousGraphicsPutting1996].

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers describe the chart as “weird” or “floating” rather than focusing on the data. **Quick Check:** If choosing between 3D surface and 3D volume, default to volume. **Stronger Test:** Run a quick preference check with target viewers using the intended scenario framing.

## What to do instead <!-- role: fix -->

- Switch from 3D surface to 3D volume if you must retain a 3D look.
- Use a 2D area or simple version if the goal is immediate comprehension rather than presentation impact.
- If detail reading is critical, consider whether changing chart family (bar vs line) better matches the task than changing 3D subtype.
