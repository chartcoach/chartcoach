---
id: use-a-colorblind-safe-palette-and-keep-it-robust-to-tweaks
title: Use a Colorblind-Safe Palette Designed for Distinctness
bibliography: references.bib
description: Adopt a palette verified for separability under color vision deficiencies,
  and keep colors robust to small adjustments.
labels:
- chart:multi
- task:distinguish
- visual:color
- impact:accessibility
- data:categorical
- audience:general
- complexity:intermediate
- source:datawrapper
---

## The Rule <!-- role: advice -->

Start from a colorblind-safe palette and keep each color distinct in both hue and lightness; avoid adding colors that become confusable under colorblind simulation.

## The Logic <!-- role: reason -->

Purpose-built palettes reduce the chance that two categories collapse into the same perceived color under different color vision deficiencies. The post discusses established palettes (e.g., Okabe & Ito) and emphasizes verifying separability (e.g., warning that some pairs may still be too close, especially for thin marks) [@muth_colorblindness_2020].

- **The Principle:** Pre-validated categorical color sets minimize perceptual collisions
- **The Evidence:** The article presents known “colorblind-safe” palettes, notes remaining confusable pairs, and describes constructing a reduced warm/cool palette optimized for contrast and resilience to small changes [@muth_colorblindness_2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Distinguish 3–7 categories reliably
- **Data Type:** Categorical series across charts (lines, bars, donuts, legends)
- **Audience:** General audiences where you can’t assume normal color vision [@muth_colorblindness_2020]

## When to Break It <!-- role: exceptions -->

- **Scenario:** The visualization requires many categories beyond what a safe palette can support clearly
- **Reason:** Even “safe” palettes can break down with many colors; you’ll need fewer colors or non-color encodings [@muth_colorblindness_2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** Limited palette variety; some colors you like may be excluded
- **The Risk:** If you apply palette colors to very thin lines or small marks, near-colors may still become hard to tell apart [@muth_colorblindness_2020].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Copying a “colorblind-safe” palette and assuming every pair works in every mark type
- **Why it fails:** The post notes that some palette colors can still be confusable, especially for fine lines [@muth_colorblindness_2020].

## How to Check <!-- role: check -->

- **Visual Sign:** Two categories look identical in thin strokes or small symbols
- **The Test:** Run a colorblind simulation and specifically inspect the smallest/thinnest marks (not just large areas) [@muth_colorblindness_2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Swap one confusable color for a more separated warm/cool alternative (often shifting lightness)
- **Best Fix:** Reduce the number of active category colors and combine the palette with direct labels or shape/dash encoding [@muth_colorblindness_2020].
