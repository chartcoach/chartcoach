---
id: reorder-categorical-palettes-by-maximizing-minimum-perceptual-distance
title: Re-order categorical palette items by repeatedly adding the item with the largest
  minimum perceptual distance
bibliography: references.bib
description: A perceptual-kernel-driven greedy ordering front-loads the most discriminable
  palette items for categorical encodings.
labels:
- chart:any
- task:design
- visual:color
- visual:shape
- impact:clarity
- data:categorical
- audience:practitioner
- complexity:intermediate
---

## Re-order a palette to front-load perceptually distinct items using a maximin rule <!-- role: advice -->

Given a perceptual distance kernel for a palette, re-order items by starting with the most distant pair and then repeatedly adding the item whose minimum distance to the current set is largest.

## Why maximin ordering improves early discriminability <!-- role: reason -->

When viewers can only rely on a subset of palette entries (because the chart has few categories or because attention is limited), selecting items that maximize separation from what is already used increases the chance that categories remain visually distinct.

**Mechanism:** The maximin criterion increases the smallest pairwise distance among selected items at each step, which promotes discriminability for the first k assignments.

**Evidence:** A greedy ordering based on kernel distances produced re-ordered shape, color, and size palettes in which early items were more perceptually discriminable, and the procedure was chosen to be stable as the palette grows (existing assignments need not change when new categories appear) [@demiralpLearningPerceptualKernels2014a].

**Notes:** The paper describes this as iteratively maximizing the minimum distance (related to Hausdorff distance between sets).

## When this applies <!-- role: context -->

- **User Goal:** Improve categorical palette usability when only the first few distinct symbols/colors are likely to be used.
- **Task:** Choose an ordering for palette entries so sequential assignment yields high discriminability.
- **Data:** Categorical group labels mapped to a discrete palette.
- **Chart Setting:** Systems that assign palette items in order (e.g., auto-encoding in tools).
- **Audience:** General audiences where fast discrimination of category markers matters.
- **Success Criterion:** Early categories are easier to distinguish without manual palette tweaking.

## When not to follow it <!-- role: exceptions -->

**Break it when:** You must preserve an existing semantic or conventional ordering of palette items. **Why:** Distance-driven ordering can conflict with semantic consistency even if it improves perceptual separation [@demiralpLearningPerceptualKernels2014a].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** The resulting order may look irregular or non-intuitive compared to handcrafted sequences. **Risk:** If the kernel does not reflect your deployment context, the ordering may optimize the wrong notion of difference. **Mitigation:** Estimate kernels using stimuli and contexts close to intended use.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Ordering palette items by a single visual dimension’s nominal order rather than perceptual distances. **Why it fails:** The kernel can reveal clusters of confusable items that simple ordering does not avoid, especially for shape palettes [@demiralpLearningPerceptualKernels2014a].

## Quick tests <!-- role: check -->

**Failure Sign:** The first few palette entries include multiple items that viewers frequently confuse. **Quick Check:** Compute the minimum pairwise distance among the first k items; if it is low relative to other possible k-subsets, the order is weak. **Stronger Test:** Run a small discrimination pilot on the first k assignments and compare confusion rates before and after re-ordering.

## What to do instead <!-- role: fix -->

- Use the kernel-based maximin ordering for automatic assignments and allow manual overrides for semantic constraints.
- Re-estimate the kernel for your exact mark sizes, stroke widths, and display conditions before re-ordering.
- If only a fixed-size subset is ever used, directly search for the subset that maximizes minimum pairwise distance under the kernel.
- If categories are many, switch to a different encoding channel or add redundant encoding rather than relying on a long palette.
