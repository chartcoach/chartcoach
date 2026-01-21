---
id: avoid-spatial-arrangement-for-high-dimensional-perceptual-kernels
title: Avoid Spatial Arrangement for High-Dimensional Perceptual Kernels
bibliography: references.bib
description: Do not rely on 2D spatial arrangement tasks to estimate perceptual kernels
  when the underlying perceptual structure is higher-dimensional or multi-channel.
labels:
- chart:any
- task:evaluate
- visual:color
- visual:shape
- visual:size
- impact:reliability
- data:categorical
- audience:designer
- method:crowdsourcing
- source:demiralp-2014
---

## The Rule <!-- role: advice -->

Do **not** use 2D spatial arrangement as your primary method for learning perceptual kernels for color or multi-dimensional encodings.

## The Logic <!-- role: reason -->

Spatial arrangement is less structured and constrains judgments to a 2D layout, which can’t faithfully express higher-dimensional perceptual relations; the paper found it had the **lowest agreement with other methods**, **lowest robustness**, and even produced **model-inconsistent results** for size (power-law exponent > 1) [@demiralpLearningPerceptualKernels2014a].

- **The Principle:** Forcing high-dimensional similarity structure into 2D increases distortion and between-subject variability.
- **The Evidence:** SA had the lowest average rank correlations to other kernels and was least robust to participant removal; it also yielded a size exponent inconsistent with known psychophysical patterns in their analysis [@demiralpLearningPerceptualKernels2014a].

## Where to Apply <!-- role: context -->

- **User Goal:** Estimate accurate perceptual distances to support automated palette assignment or evaluation.
- **Data Type:** Color palettes (often >2D perceptual structure) and bivariate palettes (multiple perceptual dimensions).
- **Audience:** Designers/researchers choosing a crowdsourcing protocol for similarity judgments.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You need the cheapest/fastest rough estimate and can tolerate lower fidelity.
- **Reason:** SA is by far the fastest and cheapest elicitation method in their cost/time comparison [@demiralpLearningPerceptualKernels2014a].

## The Price <!-- role: costs -->

- **The Sacrifice:** You give up speed and cost advantages if you avoid SA.
- **The Risk:** If you use SA anyway, you may encode spurious structure caused by 2D projection constraints rather than true perceptual distances [@demiralpLearningPerceptualKernels2014a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Treating the 2D arrangement distances as “ground truth” for perceptual distances across any channel.
- **Why it fails:** The method itself imposes a 2D geometry that can’t capture 3D+ relations and increases variance across participants [@demiralpLearningPerceptualKernels2014a].

## How to Check <!-- role: check -->

- **Visual Sign:** Kernels from SA disagree noticeably with kernels from triplets/pairwise (e.g., different clustering).
- **The Test:** Compute Spearman rank correlation between SA-derived kernel and a triplet-matching kernel for the same palette; SA should be notably lower on average in their findings [@demiralpLearningPerceptualKernels2014a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace SA with pairwise Likert ratings (if you need cheaper than triplets).
- **Best Fix:** Use triplet matching and aggregate per-user distance matrices; reserve SA only for exploratory or cost-constrained contexts [@demiralpLearningPerceptualKernels2014a].
