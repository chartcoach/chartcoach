---
id: use-perceptual-kernels-to-space-nominal-areas-for-cluster-separability
title: Use Perceptual Kernels to Space Nominal Marker Sizes for Clustering
bibliography: references.bib
description: When clustering categorical groups with size-coded markers, choose marker
  sizes whose perceptual distances are maximized using a perceptual kernel.
labels:
- chart:scatter
- task:cluster
- visual:area
- impact:discriminability
- data:categorical
- audience:general
- method:perceptual-kernel
- source:paper
---

## The Rule <!-- role: advice -->

If you encode nominal categories using marker area (size), select size steps using a perceptual-kernel distance matrix so the used sizes are as perceptually distinct as possible.

## The Logic <!-- role: reason -->

- **The Principle:** Use empirically estimated perceptual distances to pick separable symbol magnitudes.
- **The Evidence:** Perceptual kernels provide distance matrices for size (area-circle stimuli) and enable palette re-ordering/selection to maximize discriminability [@demiralpLearningPerceptualKernels2014]; this paper’s encoding-level knowledge is collated for recommendation use cases [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Cluster nominal groups when size is (unusually) used as the category channel.
- **Data Type:** Nominal categories encoded using marker area.
- **Audience:** General viewers.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The visual variable (area/size) is already reserved for quantitative meaning.
- **Reason:** Using size for nominal groups can imply ordinality/quantity; the kernel only helps separability, not semantic correctness of the encoding choice [@demiralpLearningPerceptualKernels2014].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may end up with a non-intuitive or uneven-looking set of size steps because it is optimized for perceptual distance.
- **The Risk:** Over-emphasizing some categories due to larger marker sizes, even if the goal is just categorical separation [@demiralpLearningPerceptualKernels2014].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using evenly spaced numeric size increments (linear steps) and assuming they look evenly spaced perceptually.
- **Why it fails:** Perceptual distances can be nonlinear with respect to physical size differences; kernels capture the perceived distances directly [@demiralpLearningPerceptualKernels2014], which collation work aims to make accessible to recommenders [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Some size categories look nearly identical while others look dramatically different.
- **The Test:** Lay out one example mark from each category side-by-side; if separations are inconsistent, your sizes likely weren’t chosen using perceptual distances [@demiralpLearningPerceptualKernels2014].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace the most-confusable adjacent sizes with alternatives that have larger kernel distance.
- **Best Fix:** Recompute the set of sizes used for categories by maximizing the minimum perceptual distance in the kernel among chosen sizes [@demiralpLearningPerceptualKernels2014; @zengReviewCollationGraphical2023].
