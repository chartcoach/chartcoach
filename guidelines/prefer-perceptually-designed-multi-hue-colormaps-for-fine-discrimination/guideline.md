---
id: prefer-perceptually-designed-multi-hue-colormaps-for-fine-discrimination
title: Use Perceptually-Designed Multi-Hue Colormaps for Fine Value Discrimination
bibliography: references.bib
description: Multi-hue sequential colormaps can reduce errors compared to single-hue
  ramps when users must distinguish small value differences.
labels:
- chart:heatmap
- task:compare
- visual:color
- impact:resolution
- data:quantitative
- audience:general
- colormap:multi-hue
---

## The Rule <!-- role: advice -->

When users need to distinguish small differences along a continuous scale, prefer a perceptually-designed multi-hue sequential colormap (e.g., UCS-based schemes) over a single-hue luminance ramp.

## The Logic <!-- role: reason -->

- **The Principle:** Adding hue variation (while maintaining ordering) can increase discriminability (“resolution”) for near-neighbor comparisons.
- **The Evidence:** Single-hue colormaps showed notably higher error for the smallest span condition, while multi-hue UCS colormaps (viridis/plasma/magma) had the lowest error across studies and were comparable in speed within their group [@liuSomewhereRainbowEmpirical2018a].

## Where to Apply <!-- role: context -->

- **User Goal:** Decide which of two values is closer to a reference; detect subtle differences on a continuous legend.
- **Data Type:** Quantitative scalar data with frequent small differences or dense gradients.
- **Audience:** General users; settings where misreading small differences matters.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your task is coarse reading with only a few discrete bins (e.g., very few levels).
- **Reason:** The paper notes single-hue may be acceptable for discrete scales with 5–7 colors; the “resolution” failure was most evident in small-span conditions resembling too-fine binning or close values [@liuSomewhereRainbowEmpirical2018a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Multi-hue maps can be slightly slower on average than the very fastest single-hue cases in some settings.
- **The Risk:** Poorly-designed multi-hue maps can reintroduce rainbow-like issues; the benefit depends on “judicious design” [@liuSomewhereRainbowEmpirical2018a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Switching from rainbow to any arbitrary multi-hue map without checking ordering and performance.
- **Why it fails:** The paper’s results support multi-hue only when designed to preserve perceptual ordering; rainbow (jet) was still worst [@liuSomewhereRainbowEmpirical2018a].

## How to Check <!-- role: check -->

- **Visual Sign:** Users confuse adjacent values near each other on the legend (especially at tight ranges).
- **The Test:** Sample triplets with small numeric spans (like the paper’s lowest-span condition); if error spikes for a single-hue ramp, switch to a perceptually-designed multi-hue alternative [@liuSomewhereRainbowEmpirical2018a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace a single-hue ramp with a validated multi-hue sequential colormap from a perceptually-uniform design approach.
- **Best Fix:** Use a multi-hue sequential colormap designed in a perceptually-uniform space (the paper evaluates UCS-derived maps and finds them strong overall) [@liuSomewhereRainbowEmpirical2018a].
