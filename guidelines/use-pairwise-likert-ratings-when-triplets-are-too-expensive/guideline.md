---
id: use-pairwise-likert-ratings-when-triplets-are-too-expensive
title: Use pairwise Likert ratings to estimate perceptual kernels when triplet comparisons
  are too costly
bibliography: references.bib
description: Pairwise Likert ratings provide kernels broadly consistent with triplet-based
  kernels at lower collection cost.
labels:
- chart:any
- task:evaluate
- visual:color
- visual:shape
- visual:size
- impact:efficiency
- data:any
- audience:practitioner
- complexity:advanced
---

## Use pairwise Likert ratings as a cost-saving kernel method <!-- role: advice -->

Use pairwise Likert ratings to collect perceptual similarity data when you need a perceptual kernel but cannot afford triplet comparison studies.

## Why pairwise ratings can be a practical substitute <!-- role: reason -->

Pairwise ratings directly produce a dense distance matrix with far fewer total judgments than exhaustive triplets, lowering total time and cost while still yielding kernels that correlate well with those from other structured methods.

**Mechanism:** Direct pairwise judgments provide an immediate numeric distance estimate per pair, enabling aggregation with minimal postprocessing.

**Evidence:** Pairwise Likert kernels showed strong rank correlation with kernels from other judgment types, and required less overall experiment time and lower compensation than triplet comparisons because they involve fewer total judgments [@demiralpLearningPerceptualKernels2014a].

**Notes:** In the reported experiments, 5-point and 9-point Likert versions produced similar overall agreement with other methods.

## When you should use pairwise ratings <!-- role: context -->

- **User Goal:** Obtain an approximate but useful perceptual distance kernel under tight budget constraints.
- **Task:** Collect similarity ratings for all pairs in a palette and aggregate to a kernel.
- **Data:** Discrete palettes where full pair coverage is feasible.
- **Chart Setting:** Crowdsourcing or lightweight user studies where simpler tasks reduce coordination overhead.
- **Audience:** Designers needing practical kernels for palette ordering or assignment.
- **Success Criterion:** Acceptable agreement with more robust methods at meaningfully lower cost.

## When not to follow it <!-- role: exceptions -->

**Break it when:** You need the lowest-variance kernel possible for downstream optimization or modeling. **Why:** Triplet matching produced lower cross-subject variance and greater robustness than pairwise ratings in the reported comparisons [@demiralpLearningPerceptualKernels2014a].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Potentially higher variance than triplet matching, depending on palette and task. **Risk:** Ratings may compress differences when the response scale is coarse relative to the number of distinct stimuli. **Mitigation:** Use a rating interface that helps participants distribute ratings consistently across the scale.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Treating pairwise ratings as “ground truth” without checking stability across participants. **Why it fails:** Subjective scaling differences can inflate variance, so the aggregate kernel may shift with the sampled crowd [@demiralpLearningPerceptualKernels2014a].

## Quick tests <!-- role: check -->

**Failure Sign:** Many ties or near-ties in the distance matrix that contradict obvious perceptual groupings for the palette. **Quick Check:** Compute rank correlation between kernels from two random halves of participants. **Stronger Test:** Compare the pairwise kernel against a small triplet-matching pilot for the same palette.

## What to do instead <!-- role: fix -->

- Use triplet matching for a smaller subset of stimuli to validate or refine the pairwise kernel.
- Reduce the palette size to make triplet matching feasible for the most important stimuli.
- If using bivariate palettes, limit factor levels (e.g., 4×4 rather than 10×10) before collecting pairwise ratings.
- Use kernel-based palette re-ordering to mitigate imperfect absolute distances by prioritizing the most separated items first.
