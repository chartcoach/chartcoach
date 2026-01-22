---
id: use-perceptual-kernels-as-the-distance-function-for-optimized-palette-to-data-assignment
title: Use perceptual kernels as the distance function when optimizing palette-to-data
  assignments to preserve structure
bibliography: references.bib
description: Kernel-defined perceptual distances enable automated assignment of symbols
  or colors that preserves data-space distances.
labels:
- chart:any
- task:optimize
- visual:color
- visual:shape
- impact:automation
- data:relational
- audience:researcher
- complexity:advanced
---

## Optimize visual assignments using kernel-defined perceptual distances <!-- role: advice -->

When assigning discrete visual encodings to items where pairwise relations matter, optimize the assignment by matching data-space distances to perceptual distances taken from a perceptual kernel.

## Why kernel-based assignment preserves perceived structure <!-- role: reason -->

If the optimization uses perceptual distances that reflect how viewers actually judge differences among palette items, the resulting mapping can better preserve relational structure in the viewer’s perceptual space than mappings based on ad hoc or purely physical differences.

**Mechanism:** Structure-preserving assignment minimizes distortion between the data distance matrix and the perceptual distance matrix induced by chosen visual tokens.

**Evidence:** Perceptual kernels were applied as the perceptual distance metric for discrete visual embedding to automatically select shapes and colors that reflect relationships among variables or graph communities, demonstrating structure-preserving assignments driven by learned perceptual distances [@demiralpLearningPerceptualKernels2014a].

**Notes:** The paper notes that such assignments can be found using optimization methods such as simulated annealing.

## When this applies <!-- role: context -->

- **User Goal:** Make similarities and dissimilarities in the data perceptually apparent through discrete encodings.
- **Task:** Assign palette entries to labels, clusters, or model components to reflect pairwise relationships.
- **Data:** A distance or dissimilarity matrix among categories, clusters, or models (e.g., inter-cluster connection strengths).
- **Chart Setting:** Any setting where discrete encodings (shape/color) represent entities whose relationships should be compared.
- **Audience:** Analysts and readers relying on perceived similarity to interpret structure.
- **Success Criterion:** The perceptual pattern of differences among assigned encodings mirrors the data-space pattern.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The task is purely identification (distinguish categories) and does not require preserving pairwise relational structure. **Why:** Structure preservation adds optimization complexity without guaranteed benefit for simple labeling tasks [@demiralpLearningPerceptualKernels2014a].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Additional computation and the need for a distance matrix in the data domain. **Risk:** A kernel learned on one display context may not generalize to another, reducing fidelity of structure preservation. **Mitigation:** Reuse kernels only when the palette and rendering conditions match the learned stimuli.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Optimizing assignments using an unvalidated proxy distance (e.g., arbitrary index differences) instead of perceptual distances. **Why it fails:** Proxy distances can disagree with human judgments, producing assignments that preserve structure mathematically but not perceptually [@demiralpLearningPerceptualKernels2014a].

## Quick tests <!-- role: check -->

**Failure Sign:** Items that are close in the data are assigned visually dissimilar tokens, or distant items get visually similar tokens. **Quick Check:** Compute rank correlation between data distances and kernel distances for the final assignment. **Stronger Test:** Run a small user study asking participants to group or compare items and verify the perceived structure matches the intended one.

## What to do instead <!-- role: fix -->

- Collect or derive a perceptual kernel for the exact palette items you will use before optimizing.
- If you lack a kernel, restrict to encodings with existing validated perceptual models, or collect a small triplet-matching kernel for your palette.
- Simplify the objective to preserve only the most important neighborhood relations rather than all pairwise distances.
- If the mapping must be stable under added categories, combine kernel-based ordering with incremental assignment constraints.
