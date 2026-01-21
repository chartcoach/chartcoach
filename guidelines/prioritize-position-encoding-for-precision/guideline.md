---
id: prioritize-position-encoding-for-precision
title: Use Position Encoding When Users Must Read Values Precisely
bibliography: references.bib
description: Prefer position over size, angle/rotation, and area when tasks require
  accurate perceptual judgments.
labels:
- visual:position
- visual:size
- task:retrieve-value
- task:compare
- impact:accuracy
- audience:novice
- source:borner-2019
---

## The Rule <!-- role: advice -->

When users must read or compare values accurately, encode the key quantity with position rather than size, angle/rotation, or area.

## The Logic <!-- role: reason -->

Human perceptual accuracy differs by encoding channel; the cited studies rank position as most accurate, followed by length (size), then angle/rotation, then area.

- **The Principle:** Perceptual effectiveness ordering of channels
- **The Evidence:** [@bornerDataVisualizationLiteracy2019]

## Where to Apply <!-- role: context -->

- **User Goal:** Retrieve exact values, identify maxima, or make close comparisons
- **Data Type:** Quantitative measures where small differences matter
- **Audience:** General audiences and students taking literacy-style tasks

## When to Break It <!-- role: exceptions -->

- **Scenario:** When position is already reserved for other essential variables (e.g., geographic coordinates must occupy x/y)
- **Reason:** You may need other channels for the remaining quantities, but expect reduced precision [@bornerDataVisualizationLiteracy2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** Limited dimensionality (2D/3D position can encode only a few variables cleanly)
- **The Risk:** Overplotting if too many items share similar positions

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Switching to bubble/area encodings to “fit more variables” while still expecting precise reading
- **Why it fails:** Area is less accurately perceived than position (and even length), increasing error [@bornerDataVisualizationLiteracy2019].

## How to Check <!-- role: check -->

- **Visual Sign:** Users must estimate areas/angles to answer questions about small numeric differences.
- **The Test:** If the primary question is a precise comparison, verify the primary quantity is mapped to x/y (or aligned position) [@bornerDataVisualizationLiteracy2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Remap the main quantitative variable from area/angle/size to a positional axis.
- **Best Fix:** Change the visualization type to one whose reference system supports positional encoding for the key comparisons [@bornerDataVisualizationLiteracy2019].
