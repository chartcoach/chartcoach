---
id: use-perceptual-kernels-for-distance-preserving-encoding-assignment
title: Use Perceptual Kernels for Distance-Preserving Encoding Assignment
bibliography: references.bib
description: Assign palette items to data points by optimizing preservation of data-space
  distances in kernel-defined perceptual space.
labels:
- chart:any
- task:map
- visual:color
- visual:shape
- impact:faithfulness
- data:relational
- audience:designer
- method:visual-embedding
- source:demiralp-2014
---

## The Rule <!-- role: advice -->

When mapping discrete palette items to data points or clusters, optimize the assignment to **preserve data-space distances** using perceptual distances from a kernel.

## The Logic <!-- role: reason -->

Perceptual kernels provide the distance function needed to evaluate whether a mapping preserves structure; optimizing assignments against kernel distances can make encoded differences align with meaningful data differences (the paper demonstrates this via visual embedding examples) [@demiralpLearningPerceptualKernels2014a].

- **The Principle:** Structure-preserving mappings reduce misleading perceptual groupings.
- **The Evidence:** The paper applies kernel distances to visual embedding to assign shapes/colors reflecting similarities among metrics and inter-community relationships in a graph [@demiralpLearningPerceptualKernels2014a].

## Where to Apply <!-- role: context -->

- **User Goal:** Make cluster-to-color/shape assignments reflect inter-cluster relationships (e.g., adjacency/connection strength).
- **Data Type:** Graph/community structures or any domain with a meaningful distance/dissimilarity matrix between categories.
- **Audience:** Designers and developers implementing automated styling for clustered/relational visualizations.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The design goal is categorical separability only (all categories equally distinct), not distance preservation.
- **Reason:** Distance-preserving assignments can intentionally place some categories closer together to reflect data relationships, which may be undesirable if you want uniform discriminability [@demiralpLearningPerceptualKernels2014a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Requires an optimization step (search over assignments) and a defined data-space distance matrix.
- **The Risk:** If the data-space distances are poorly chosen or arbitrarily scaled, the resulting encoding may encode the wrong relationships (the paper rescales distances to manage dynamic range in an example) [@demiralpLearningPerceptualKernels2014a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assigning palette items arbitrarily or by input order, then claiming the visualization “reflects” relationships.
- **Why it fails:** Without using perceptual distances, the mapping can accidentally place related categories far apart (or unrelated ones close), contradicting the intended structure [@demiralpLearningPerceptualKernels2014a].

## How to Check <!-- role: check -->

- **Visual Sign:** Categories that should be similar appear highly distinct (or vice versa).
- **The Test:** Compare rank order of pairwise distances in data space vs perceptual space (kernel distances among assigned items); large mismatches indicate poor preservation [@demiralpLearningPerceptualKernels2014a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Swap assignments among a few categories to reduce the worst distance mismatches (largest data distance paired with smallest perceptual distance).
- **Best Fix:** Perform a discrete visual embedding optimization that minimizes distance distortion using kernel distances as the perceptual metric [@demiralpLearningPerceptualKernels2014a].
