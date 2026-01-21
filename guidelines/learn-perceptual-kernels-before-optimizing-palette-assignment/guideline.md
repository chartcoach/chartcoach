---
id: learn-perceptual-kernels-before-optimizing-palette-assignment
title: Learn Perceptual Kernels Before Optimizing Palette Assignment
bibliography: references.bib
description: Base palette optimization and value-to-mark assignments on empirically
  learned perceptual distance matrices, not default palettes alone.
labels:
- chart:any
- task:assign
- visual:color
- visual:shape
- visual:size
- impact:clarity
- data:categorical
- audience:designer
- method:automated-design
- source:demiralp-2014
---

## The Rule <!-- role: advice -->

Before automatically assigning colors/shapes/sizes to data values, compute or use a **perceptual kernel** and optimize assignments against its distances.

## The Logic <!-- role: reason -->

Default palettes and encoding rankings say *which channel* to use but not *which specific items* to assign; perceptual kernels capture empirically judged within-channel and cross-channel distances so assignments can preserve intended differences and avoid unintended clusters [@demiralpLearningPerceptualKernels2014a].

- **The Principle:** Use measured perceptual distances as the objective function for encoding assignments.
- **The Evidence:** The paper defines perceptual kernels as reusable distance matrices and demonstrates using them for palette re-ordering and distance-preserving visual embedding assignments [@demiralpLearningPerceptualKernels2014a].

## Where to Apply <!-- role: context -->

- **User Goal:** Make categorical encodings more discriminable or make assignments reflect data-space relationships.
- **Data Type:** Nominal/cluster labels, or discrete assignments from a fixed palette.
- **Audience:** Visualization tool builders implementing automated styling or recommendation.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You already have a validated perceptual model for the channel and task.
- **Reason:** If a suitable perceptual space is available (e.g., a standard color space), you may not need to learn a kernel for that channel (the paper notes this contrast) [@demiralpLearningPerceptualKernels2014a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Up-front effort to collect judgments and construct the kernel.
- **The Risk:** Kernels are palette-specific; changing the stimulus set requires re-collecting or extending judgments [@demiralpLearningPerceptualKernels2014a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using default palette order or arbitrary ordering as a proxy for perceptual spacing.
- **Why it fails:** The paper’s kernels show clustering (e.g., among triangles or stroked shapes) that can contradict assumed equal spacing, causing unintended similarity in the display [@demiralpLearningPerceptualKernels2014a].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers confuse categories that were intended to be distinct, or categories appear grouped despite no data grouping.
- **The Test:** Inspect the kernel heatmap: if assigned items are close (high similarity), the visualization will likely produce confusions consistent with those clusters [@demiralpLearningPerceptualKernels2014a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Re-assign categories to increase minimum pairwise perceptual distance using the kernel.
- **Best Fix:** Use kernel-based optimization (e.g., distance-preserving visual embedding or discriminability-driven ordering) to choose assignments systematically [@demiralpLearningPerceptualKernels2014a].
