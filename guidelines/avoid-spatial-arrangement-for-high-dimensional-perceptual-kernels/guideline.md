---
id: avoid-spatial-arrangement-for-high-dimensional-perceptual-kernels
title: Avoid spatial arrangement tasks for perceptual kernels when the stimulus space
  is higher-dimensional than 2D
bibliography: references.bib
description: Spatial arrangement is fast but less reliable and cannot faithfully capture
  higher-dimensional perceptual structure.
labels:
- chart:any
- task:evaluate
- visual:color
- visual:shape
- visual:size
- impact:accuracy
- data:any
- audience:practitioner
- complexity:advanced
---

## Do not use spatial arrangement to capture higher-dimensional perceptual structure <!-- role: advice -->

Avoid spatial arrangement similarity tasks when the perceptual structure of your stimuli is not well represented in two dimensions.

## Why spatial arrangement underperforms for kernels <!-- role: reason -->

Spatial arrangement forces participants to express all relationships as 2D Euclidean proximity, which limits expressiveness for inherently higher-dimensional perceptual spaces and increases variability because the task is less structured.

**Mechanism:** A 2D layout collapses degrees of freedom, so distinct stimuli can become artificially close, and participants can adopt inconsistent layout strategies that inflate between-subject variance.

**Evidence:** Spatial arrangement produced the lowest agreement with other judgment types and was least robust to subject removal; it also produced an area-perception exponent inconsistent with established size perception behavior compared to pairwise and triplet-derived kernels [@demiralpLearningPerceptualKernels2014a].

**Notes:** The limitations are especially salient for color and for multi-attribute (bivariate) stimuli where higher-dimensional structure is expected.

## When this applies <!-- role: context -->

- **User Goal:** Estimate a perceptual distance kernel that will be reused for evaluation or automated assignment.
- **Task:** Collect perceptual similarities for palettes where the underlying perceptual space likely exceeds two dimensions.
- **Data:** Color palettes or combined encodings (e.g., shape–color, size–color, shape–size).
- **Chart Setting:** Crowdsourced studies where you might be tempted to use the fastest elicitation method.
- **Audience:** Designers needing stable, generalizable perceptual distances.
- **Success Criterion:** High agreement across elicitation methods and stability under smaller participant samples.

## When not to follow it <!-- role: exceptions -->

**Break it when:** You only need a quick, rough 2D organization of a small set of stimuli and do not require a faithful distance kernel. **Why:** Spatial arrangement is extremely fast and inexpensive compared to structured pairwise or triplet judgments [@demiralpLearningPerceptualKernels2014a].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You give up speed and cost advantages if you switch away from spatial arrangement. **Risk:** Using spatial arrangement anyway can yield misleading distances for downstream optimization or modeling. **Mitigation:** Treat spatial arrangement outputs as exploratory and validate with structured judgments before using them for automated design.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using spatial arrangement distances as if they were equivalent to kernels learned from structured comparisons. **Why it fails:** The 2D constraint and higher variance can distort both global structure and fine-grained distances, particularly for color and multi-attribute stimuli [@demiralpLearningPerceptualKernels2014a].

## Quick tests <!-- role: check -->

**Failure Sign:** The kernel changes substantially when you remove many participants, or predicted perceptual relationships contradict known qualitative structure of the palette. **Quick Check:** Run a sensitivity analysis by dropping a large fraction of participants and recomputing rank correlation. **Stronger Test:** Collect a smaller triplet-matching dataset for the same stimuli and compare rank correlation between kernels.

## What to do instead <!-- role: fix -->

- Use ordinal triplet matching to estimate kernels when you need robust distances.
- Use pairwise Likert ratings when you need a cheaper but structured alternative.
- Reduce the stimulus set size for combined encodings so structured judgments remain feasible.
- Use spatial arrangement only for early exploration, then replace it with structured elicitation for final kernels.
