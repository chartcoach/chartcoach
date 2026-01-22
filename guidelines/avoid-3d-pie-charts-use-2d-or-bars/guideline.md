---
id: avoid-3d-pie-charts-use-2d-or-bars
title: Avoid 3D pie charts because perspective distorts slice angles; use 2D pies
  or bar charts instead
bibliography: references.bib
description: Tilting pies into 3D changes apparent angles and areas, which can make
  a category look larger than the data supports.
labels:
- chart:pie
- task:compare
- visual:angle
- impact:trust
- data:part-to-whole
- audience:general
- risk:projection-distortion
---

## Keep pies 2D or replace them with bars when accurate part-to-whole comparison matters <!-- role: advice -->

Do not render pie charts in 3D when people must compare shares. Use a 2D pie or switch to a bar chart to support more accurate comparisons.

## Why 3D pies bias perceived shares <!-- role: reason -->

When a pie is tilted in 3D, the projection to 2D distorts slice geometry, so equal angles can look unequal and front-facing slices can appear larger than they are. This changes the perceived part-to-whole relationship and can cause incorrect judgments about which category dominates.

**Mechanism:** Perspective projection alters perceived angles and areas based on depth and orientation, breaking the mapping between slice angle and value.

**Evidence:** 3D projection distortion can make a slice appear to represent a much larger share than the underlying data, changing conclusions about market share or dominance [@szafirGoodBadBiased2018]. 2D representations avoid the viewpoint-dependent distortions introduced by 3D rendering in flat media [@szafirGoodBadBiased2018].

**Notes:** The problem is not “pie charts in general” in this scope; it is the 3D perspective distortion of a pie’s encodings.

## When this applies <!-- role: context -->

- **User Goal:** Judge category shares and compare which segments are larger.
- **Task:** Identify dominant categories; estimate relative proportions.
- **Data:** Part-to-whole categorical shares.
- **Chart Setting:** Slides, reports, or screenshots where the pie is shown with perspective.
- **Audience:** General audiences scanning quickly.
- **Success Criterion:** Perceived slice sizes match underlying proportions.

## When not to follow it <!-- role: exceptions -->

**Break it when:** No quantitative comparison is intended and the pie is purely decorative. **Why:** The distortion still exists, but it is less likely to be used for decision-making in that limited case [@szafirGoodBadBiased2018].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** 3D pies can look more visually striking. **Risk:** Switching to bars may change the aesthetic or layout expectations of stakeholders. **Mitigation:** Preserve branding with typography and color while keeping geometry honest.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Tilting the pie “for style” while expecting viewers to read shares from labels. **Why it fails:** Viewers rely on perceived geometry at a glance, and the projection changes that geometry [@szafirGoodBadBiased2018].

## Quick tests to catch problems <!-- role: check -->

**Failure Sign:** A front slice looks dominant even when the legend values are similar. **Quick Check:** Remove the 3D tilt; if apparent ranks change, the 3D view was biasing perception. **Stronger Test:** Ask viewers to rank slices by size; large disagreement with the data indicates distortion.

## What to do instead <!-- role: fix -->

- Render the pie in 2D with no tilt and keep the mapping between slice angle and value intact.
- Use a horizontal bar chart for share comparisons when ranking accuracy matters.
- Add clear labels for shares, but do not rely on labels to “fix” geometric distortion.
- If many categories exist, group minor categories rather than compressing slices into a distorted 3D view.
