---
id: use-triplet-matching-to-collect-perceptual-similarity-kernels
title: Use ordinal triplet matching to collect perceptual similarity kernels unless
  cost or time prohibits
bibliography: references.bib
description: Triplet matching yields the most consistent and robust perceptual distance
  kernels across subjects for visualization encodings.
labels:
- chart:any
- task:evaluate
- visual:color
- visual:shape
- visual:size
- impact:clarity
- data:any
- audience:practitioner
- complexity:advanced
---

## Prefer ordinal triplet matching for kernel collection <!-- role: advice -->

Use ordinal triplet matching judgments to estimate perceptual distance kernels for visual encodings unless time or budget constraints force a cheaper method.

## Why triplet matching produces better kernels <!-- role: reason -->

Triplet matching uses a two-alternative forced choice (“which option is more similar to the reference?”), which reduces cognitive load per judgment while still extracting fine-grained ordinal constraints that scaling methods can convert into stable distance estimates.

**Mechanism:** Binary comparative judgments reduce subjective scale calibration issues and encourage discrimination among close alternatives, producing lower-variance aggregate distances.

**Evidence:** Triplet matching had the lowest cross-subject variance, the strongest robustness to subject removal, and produced the best prediction of bivariate perceptual distances from univariate kernels (highest log-likelihood in model fits) across palettes [@demiralpLearningPerceptualKernels2014a].

**Notes:** The overall study compared five elicitation methods (pairwise Likert ratings, two triplet variants, and spatial arrangement) over shape, color, size, and bivariate combinations.

## When you should use triplet matching <!-- role: context -->

- **User Goal:** Build a reusable perceptual distance model for a palette or encoding channel to guide evaluation or automated design.
- **Task:** Elicit similarity/dissimilarity judgments among discrete visual stimuli and aggregate them into a distance matrix (kernel).
- **Data:** A finite palette of marks (e.g., 10 shapes, 10 colors, 10 sizes; or smaller bivariate combinations).
- **Chart Setting:** Any tool or workflow where you can run structured perception studies (often crowdsourced).
- **Audience:** Designers or researchers needing robust aggregate perceptual distances.
- **Success Criterion:** Low-variance, stable kernels that remain similar as the participant pool changes.

## When not to follow it <!-- role: exceptions -->

**Break it when:** You cannot afford the larger number of judgments required by triplet comparisons for large palettes. **Why:** Triplet designs scale poorly in total comparisons as palette size grows, increasing time and monetary cost [@demiralpLearningPerceptualKernels2014a].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Higher overall experiment duration and cost than pairwise Likert ratings for the same palette size. **Risk:** Practical infeasibility for very large stimulus sets due to cubic growth in possible triplets. **Mitigation:** Limit the stimulus set size or distribute subsets across participants.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using triplet discrimination (“pick the most dissimilar item”) as a drop-in replacement for triplet matching. **Why it fails:** Triplet discrimination can collapse fine-grained distinctions by focusing on the outlier rather than forcing close comparisons, leading to less informative constraints in some palettes [@demiralpLearningPerceptualKernels2014a].

## Quick tests <!-- role: check -->

**Failure Sign:** Kernels change noticeably (low rank correlation) when you drop many participants from the dataset. **Quick Check:** Randomly remove a large fraction of participants and compute rank correlation between the reduced-kernel and full-kernel. **Stronger Test:** Compare cross-subject variance across judgment types on a pilot palette and select the method with the lowest variance under your budget.

## What to do instead <!-- role: fix -->

- Use pairwise Likert ratings when you need a cheaper study while still producing broadly compatible kernels.
- Restrict bivariate palette sizes to keep triplet collection feasible.
- Partition the stimulus set and collect judgments on subsets to reduce total comparisons per participant.
- Use a faster elicitation method only for rough structure exploration, then validate critical palettes with triplet matching.
