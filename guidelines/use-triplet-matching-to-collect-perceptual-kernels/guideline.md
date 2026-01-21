---
id: use-triplet-matching-to-collect-perceptual-kernels
title: Use Triplet Matching to Collect Perceptual Kernels
bibliography: references.bib
description: Prefer ordinal triplet matching judgments to estimate perceptual distance
  matrices for visual encodings with low variance and high robustness.
labels:
- chart:any
- task:evaluate
- visual:color
- visual:shape
- visual:size
- impact:clarity
- data:categorical
- audience:designer
- method:crowdsourcing
- source:demiralp-2014
---

## The Rule <!-- role: advice -->

Collect perceptual similarity using **ordinal triplet matching**: show a reference stimulus A and ask whether B or C is **more similar** to A.

## The Logic <!-- role: reason -->

Triplet matching is a simple two-alternative forced choice that yields kernels with **low cross-subject variance**, **high stability under subject removal**, and the **best predictive fit** when modeling bivariate distances from univariate kernels.

- **The Principle:** Reliable ordinal judgments outperform noisier or over-parameterized similarity reports.
- **The Evidence:** Across palettes and task types, triplet matching had the lowest variance and highest robustness, and best log-likelihood when fitting bivariate kernels from univariate ones [@demiralpLearningPerceptualKernels2014a].

## Where to Apply <!-- role: context -->

- **User Goal:** Build a reusable perceptual distance matrix (kernel) for a palette to drive evaluation or automated assignment.
- **Data Type:** Discrete palette items (e.g., 10 shapes, 10 colors, 10 sizes; or smaller bivariate combinations).
- **Audience:** Visualization tool builders and designers collecting perception data via crowdsourcing.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You only have budget/time for very fast elicitation.
- **Reason:** Exhaustive triplets scale cubically with palette size and increase total experiment duration/cost [@demiralpLearningPerceptualKernels2014a].

## The Price <!-- role: costs -->

- **The Sacrifice:** More total judgments than pairwise rating for the same palette size.
- **The Risk:** Cost/time can become prohibitive for large palettes unless you use sampling/partitioning strategies (not resolved in this paper) [@demiralpLearningPerceptualKernels2014a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using triplet discrimination (“pick the odd one out”) as a drop-in replacement.
- **Why it fails:** Discrimination can miss fine-grained distinctions because many triplets collapse to the same “most dissimilar” choice, yielding less informative constraints [@demiralpLearningPerceptualKernels2014a].

## How to Check <!-- role: check -->

- **Visual Sign:** The resulting kernel is unstable across resamples of participants (rank correlations drop quickly when removing participants).
- **The Test:** Run a sensitivity check by randomly dropping large fractions of subjects and computing Spearman rank correlation to the full kernel; triplet matching should degrade the slowest among tested methods [@demiralpLearningPerceptualKernels2014a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch from triplet discrimination to **triplet matching** while keeping similar total judgment count.
- **Best Fix:** Use triplet matching and derive distances with non-metric MDS from the ordinal constraints, then average per-user kernels into an aggregate kernel [@demiralpLearningPerceptualKernels2014a].
