---
id: optimize-color-to-cluster-separability-in-multiclass-scatterplots
title: Optimize nominal color-hue assignment to maximize class separability in multiclass
  scatterplots (for cluster counting)
bibliography: references.bib
description: When using color hue to encode nominal classes in a scatterplot, optimize
  the mapping of colors to classes to improve perceived class separability for cluster
  tasks.
labels:
- chart:scatter
- task:cluster
- visual:color
- impact:clarity
- data:categorical
- audience:novice
- complexity:advanced
---

## Optimize class-to-color mapping for separability in multiclass scatterplots <!-- role: advice -->

When using color hue to encode nominal classes in a multiclass scatterplot for a cluster task, optimize which class gets which color to maximize perceived class separability rather than assigning colors in an arbitrary/default order.

## Why optimized color assignment improves class separability judgments <!-- role: reason -->

Class separability in multiclass scatterplots depends not only on the palette itself but also on how colors are assigned to spatially adjacent or overlapping classes; better assignments make class structure easier to discriminate during clustering judgments.

**Mechanism:** Optimized assignments increase color differences between neighboring/overlapping classes and maintain adequate contrast to the background, making clusters more visually separable.

**Evidence:** In multiclass scatterplots using nominal color hue, different class-to-color assignments (from the same palette) lead to different perceived separability, and optimized assignments improve users’ ability to distinguish class/cluster counts versus default assignments in a controlled study. [@wangOptimizingColorAssignment2019; @zengReviewCollationGraphical2023]

**Notes:** This guideline applies to the encoding-level choice of mapping classes to colors, not to choosing which palette to use.

## When to apply color-assignment optimization <!-- role: context -->

- **User Goal:** Identify or judge how many classes/clusters are present (class separability).
- **Task:** Cluster.
- **Data:** Two quantitative variables plus one nominal class label (multiclass), with potential overlap/adjacency of classes.
- **Chart Setting:** Static 2D scatterplot using point marks with nominal color hue for class labels.
- **Audience:** General audiences or analysts who need fast, accurate cluster perception.
- **Success Criterion:** Fewer errors (and potentially lower time) when judging class separation/cluster counts.

## When not to follow this rule <!-- role: exceptions -->

**Break it when:** Color hue is not used to encode the class label (e.g., no class encoding or a different channel is used). **Why:** This guideline targets optimizing the class-to-color-hue mapping and does not apply without that encoding.

## Tradeoffs and risks of optimizing class-to-color mapping <!-- role: costs -->

**Sacrifice:** Implementation complexity, since optimization requires computation beyond default assignment. **Risk:** Optimizing for separability can yield assignments that are not aligned with other goals like subjective aesthetic preference. **Mitigation:** Treat the optimized assignment as a candidate to review rather than an immutable default.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Treating a “good categorical palette” as sufficient and leaving class-to-color assignment as the software default. **Why it fails:** The same palette can yield poor separability if colors are assigned to classes in a way that places similar colors on neighboring/overlapping clusters.

## Quick checks for whether assignment optimization is needed <!-- role: check -->

**Failure Sign:** Classes that are spatially adjacent or overlapping look hard to distinguish even though the palette is categorical. **Quick Check:** Shuffle the class-to-color mapping and see whether separability visibly changes; high sensitivity indicates assignment matters. **Stronger Test:** Run a small internal task check where users count clusters/classes under the default vs an optimized assignment and compare errors.

## What to do instead if you cannot optimize <!-- role: fix -->

- Randomly generate multiple class-to-color assignments and pick the one that yields the clearest perceived separation in a quick spot-check.
- Allow analysts to interactively cycle through a small set of alternative assignments and select the clearest one for their task.
- If separability remains poor under many assignments, reduce the number of simultaneously shown classes (e.g., filter/facet) so the cluster task becomes feasible.
