---
id: compute-internal-node-weights-by-summing-leaf-weights
title: Aggregate Leaf Weights Up the Tree Before Drawing a Treemap
bibliography: references.bib
description: "Compute each internal node\u2019s weight as the sum of its subtree leaves\
  \ so treemap areas remain proportional."
labels:
- chart:treemap
- task:encode
- visual:area
- impact:accuracy
- data:hierarchical
- audience:expert
- source:shneiderman-1992
---

## The Rule <!-- role: advice -->

Before laying out a treemap, compute and store each internal node’s weight as the total weight of all leaves in its subtree.

## The Logic <!-- role: reason -->

Treemap partitioning allocates area by the ratio `Size(child)/Size(parent)`. If internal nodes don’t equal subtree totals, the proportional areas will be wrong and the visual encoding breaks.

- **The Principle:** Consistent hierarchical aggregation for proportional partitioning
- **The Evidence:** Shneiderman notes that interior nodes “must have the total size of its subtree” and may require a preliminary pass to propagate sums to the root [@shneidermanTreeVisualizationTreemaps1992].

## Where to Apply <!-- role: context -->

- **User Goal:** Trust that rectangle areas correctly reflect relative contributions within any directory/subtree.
- **Data Type:** Leaf-weighted hierarchies (e.g., files as leaves; folders as internal nodes).
- **Audience:** Users making decisions from magnitude comparisons (e.g., what to delete).

## When to Break It <!-- role: exceptions -->

- **Scenario:** You intentionally want internal nodes to represent something other than the sum of descendants.
- **Reason:** Summation would misrepresent that alternate meaning; the treemap would be encoding the wrong quantity [@shneidermanTreeVisualizationTreemaps1992].

## The Price <!-- role: costs -->

- **The Sacrifice:** Extra preprocessing pass and storage of computed weights.
- **The Risk:** If the underlying data changes frequently, cached aggregates can become stale unless recomputed [@shneidermanTreeVisualizationTreemaps1992].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using only leaf sizes and leaving internal node sizes undefined or inconsistent.
- **Why it fails:** Partition ratios become meaningless, producing misleading area allocations [@shneidermanTreeVisualizationTreemaps1992].

## How to Check <!-- role: check -->

- **Visual Sign:** A child region appears larger than the parent’s other children despite having smaller total weight.
- **The Test:** For a few internal nodes, verify `Size(parent) = sum(Size(children))`.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Run a bottom-up traversal to compute subtree totals once before rendering.
- **Best Fix:** Store the computed `Size` at each node and keep it updated when leaves change [@shneidermanTreeVisualizationTreemaps1992].
