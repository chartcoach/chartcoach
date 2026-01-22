---
id: include-fixed-background-and-foreground-colors-in-categorical-palette-optimization
title: Include fixed background and foreground colors as constraints when optimizing
  categorical palettes
bibliography: references.bib
description: Prevent low-contrast category colors by optimizing with background/foreground
  colors treated as fixed constraints.
labels:
- chart:general
- task:distinguish
- visual:color
- impact:clarity
- data:categorical
- audience:general
- method:constraints
---

## Optimize categorical colors against fixed background/foreground colors <!-- role: advice -->

When category colors appear on a known background (and/or alongside fixed foreground elements like labels), treat those background/foreground colors as fixed constraints during palette optimization.

## Contrast depends on surrounding colors, not just category-to-category distance <!-- role: reason -->

A categorical palette can be internally well-separated yet still fail in use if some colors are too close to the background or other fixed elements. Including fixed background/foreground colors in the optimization forces the resulting category colors to maintain separation from those constant reference colors as well.

**Mechanism:** Adding fixed background/foreground colors effectively introduces additional “do not collide with” distances, reducing cases where a category color blends into the canvas or conflicts with static marks.

**Evidence:** A constrained optimization setup explicitly supports fixing background/foreground colors and demonstrates that optimizing with a fixed white background leads to different and faster-converging solutions than optimizing without background constraints [@fangCategoricalColormapOptimization2017; @zengReviewCollationGraphical2023].

**Notes:** This is especially relevant when the same palette is reused across many views, where manual tuning per-view is impractical.

## Context for background/foreground-aware optimization <!-- role: context -->

- **User Goal:** Distinguish colored categories reliably in the actual rendered view.
- **Task:** Identify categories in situ (not just in an isolated legend).
- **Data:** Nominal categories mapped to color hue.
- **Chart Setting:** A stable background (e.g., white canvas, map base layers) and/or stable foreground (e.g., black borders/labels) used across many charts.
- **Audience:** General audiences; also expert analysts doing repeated rapid reading.
- **Success Criterion:** Category colors remain distinguishable from the background and from fixed annotation colors.

## Exceptions: When not to follow it <!-- role: exceptions -->

**Break it when:** The background is not stable (e.g., multiple themes, unknown embedding surfaces). **Why:** Optimizing against one background can reduce performance on a different background.

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Fewer degrees of freedom; the optimized palette may be less saturated or shift in lightness to maintain contrast. **Risk:** Overfitting to one background can make colors less robust elsewhere. **Mitigation:** Optimize separately per theme or pick a small set of supported background conditions.

## Mistakes: Common failure modes <!-- role: mistakes -->

**Mistake:** Optimizing only category-to-category distances and ignoring the canvas/label colors. **Why it fails:** Some categories may become hard to see or read when rendered on the actual background.

## Check: Quick tests <!-- role: check -->

**Failure Sign:** A category disappears or becomes hard to label when placed on the chart background. **Quick Check:** Render each category color as the actual mark on the actual background and verify it remains clearly visible at typical mark sizes. **Stronger Test:** Run a quick “find the highlighted category” task on realistic backgrounds with representative mark sizes.

## Fix: What to do instead <!-- role: fix -->

- Add the background (and key foreground colors like text/borders) to the set of colors considered during optimization as fixed colors.
- Provide separate optimized palettes for light and dark themes.
- Increase non-color separation (spacing, outlines) if background variation cannot be controlled.
- Use alternative encodings (e.g., texture or shape) when background contrast cannot be guaranteed.
