---
id: prefer-triplet-matching-over-triplet-discrimination
title: Prefer Triplet Matching Over Triplet Discrimination
bibliography: references.bib
description: When collecting ordinal similarity judgments, ask which item matches
  a reference rather than which item is the odd-one-out.
labels:
- chart:any
- task:evaluate
- visual:color
- visual:shape
- visual:size
- impact:reliability
- data:categorical
- audience:designer
- method:ordinal-judgments
- source:demiralp-2014
---

## The Rule <!-- role: advice -->

Use **triplet matching with a reference** (A: is B or C more similar to A?) instead of **triplet discrimination** (which is most dissimilar?) to elicit similarity structure.

## The Logic <!-- role: reason -->

Triplet discrimination produces fewer fine-grained constraints: many triplets collapse to the same “most dissimilar” choice, whereas triplet matching forces distinctions even among two relatively similar alternatives, yielding more informative judgments and better downstream kernels [@demiralpLearningPerceptualKernels2014a].

- **The Principle:** Forced comparisons near decision boundaries increase information gained per judgment.
- **The Evidence:** The authors’ analysis and examples show Td can under-elicit fine distinctions, and empirically Tm was more robust and better for predicting bivariate kernels from univariate ones [@demiralpLearningPerceptualKernels2014a].

## Where to Apply <!-- role: context -->

- **User Goal:** Learn a perceptual kernel that will be used for optimizing palette assignments or evaluating encodings.
- **Data Type:** Discrete stimuli sets where many pairs are moderately similar (common in designed palettes).
- **Audience:** Designers and researchers implementing ordinal elicitation tasks.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You specifically want coarse grouping into broad clusters and don’t need fine-grained distances.
- **Reason:** Td can emphasize large separations and may be “good enough” for coarse partitioning, though the paper recommends Tm overall [@demiralpLearningPerceptualKernels2014a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Total experiment duration/cost can be high for triplet methods in general (relative to pairwise ratings).
- **The Risk:** If you cannot collect enough triplets, the kernel may be underconstrained (the paper notes scaling challenges for larger palettes) [@demiralpLearningPerceptualKernels2014a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming Td and Tm are interchangeable because both use triplets.
- **Why it fails:** The decision structure differs (trinary vs binary) and Td can skip informative comparisons that Tm captures [@demiralpLearningPerceptualKernels2014a].

## How to Check <!-- role: check -->

- **Visual Sign:** In bivariate palettes, one channel dominates unexpectedly (e.g., Td yielding shape-dominated clusters in shape-color).
- **The Test:** Compare Td vs Tm kernels for the same palette; Td may show coarser structure and less balanced influence of dimensions in their reported results [@demiralpLearningPerceptualKernels2014a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Change the prompt to “Which is more similar to the reference?” and keep the same UI structure.
- **Best Fix:** Collect Tm judgments and reconstruct per-user distance matrices using generalized non-metric MDS, then aggregate [@demiralpLearningPerceptualKernels2014a].
