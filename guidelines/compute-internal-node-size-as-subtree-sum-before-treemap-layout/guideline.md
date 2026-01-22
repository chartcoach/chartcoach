---
id: compute-internal-node-size-as-subtree-sum-before-treemap-layout
title: "Compute each internal node\u2019s size as the sum of its subtree before laying\
  \ out a treemap"
bibliography: references.bib
description: "Precompute additive subtree totals so each partition\u2019s area matches\
  \ the total weight of its descendants."
labels:
- chart:treemap
- task:prepare-data
- visual:area
- impact:integrity
- data:hierarchical
- audience:expert
- dataops:aggregation
---

## Precompute subtree totals for treemap sizing <!-- role: advice -->

Before generating a treemap, propagate leaf sizes upward so every internal node stores the total size of its subtree. Use these totals as the basis for partition proportions.

## Why subtree sums preserve meaning across levels <!-- role: reason -->

Treemap partitions rely on dividing a parent region among children in proportion to their sizes; this only remains coherent if a parent’s size equals the total of its descendants. Without additive totals, the relative areas at each level no longer correspond to the same underlying quantity.

**Mechanism:** Additive subtree totals create consistent conservation of area from parent to children, letting viewers interpret nested regions as “parts of a whole” at every level.

**Evidence:** Internal nodes are required to hold the total size of their subtree, and if the system does not maintain it, a preliminary pass is needed to collect and place totals at each interior node for correct treemap generation [@shneidermanTreeVisualizationTreemaps1992].

**Notes:** This also enables showing utilization versus unused capacity by adding a dummy child sized to the remainder.

## When subtree-total computation applies <!-- role: context -->

- **User Goal:** Trust that area proportions represent a single consistent measure across the hierarchy.
- **Task:** Compare magnitudes between sibling subtrees and across different branches.
- **Data:** Tree with weights at leaves (or at any nodes) where “total under this node” is meaningful.
- **Chart Setting:** Any treemap layout based on proportional partitioning.
- **Audience:** Users making decisions from relative size (deletion candidates, budget allocation, portfolio weight).
- **Success Criterion:** Child rectangles within a parent visually sum to the parent’s magnitude.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The chosen metric is not additive over descendants (for example, an average or a maximum). **Why:** Summing would misrepresent the intended meaning of the metric in area proportions.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Additional preprocessing time and storage to maintain totals. **Risk:** Stale totals lead to incorrect partitioning if the underlying leaf values change. **Mitigation:** Recompute totals on demand or update totals incrementally when leaves change.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Computing proportions from leaf sizes only while leaving internal sizes unset or inconsistent. **Why it fails:** Partition ratios become undefined or arbitrary at higher levels.
- **Mistake:** Mixing different size definitions at different depths. **Why it fails:** Viewers cannot interpret area consistently across levels.

## Quick tests <!-- role: check -->

**Failure Sign:** The areas of children do not appear to “add up” within their parent, or proportions differ depending on traversal order. **Quick Check:** For several internal nodes, verify that stored size equals the sum of descendant leaf sizes. **Stronger Test:** Recompute totals from leaves and diff against stored values; any mismatch indicates layout integrity risk.

## What to do instead <!-- role: fix -->

- Choose a different treemap encoding where area represents an additive metric, and show non-additive metrics via color.
- Store the additive measure used for area separately from other metrics to avoid accidental mixing.
- If you must use a non-additive metric, switch to a node-link tree view where size is not required to “conserve” area.
- Add a validation step that rejects treemap rendering when subtree totals are missing or inconsistent.
