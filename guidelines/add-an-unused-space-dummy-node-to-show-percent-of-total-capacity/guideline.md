---
id: add-an-unused-space-dummy-node-to-show-percent-of-total-capacity
title: Add a Dummy Node to Visualize Unused Capacity
bibliography: references.bib
description: To show utilization as a fraction of total capacity, add a dummy child
  whose size equals the unused portion.
labels:
- chart:treemap
- task:part-to-whole
- visual:area
- impact:clarity
- data:hierarchical
- audience:novice
- source:shneiderman-1992
---

## The Rule <!-- role: advice -->

If you want the treemap to represent percentage of total capacity (e.g., disk utilization), add a dummy child node sized to the unused portion.

## The Logic <!-- role: reason -->

Treemaps allocate 100% of the available rectangle among children. Adding an “unused” node ensures the visualization partitions space into used vs. unused, making utilization explicit.

- **The Principle:** Complete the part-to-whole denominator with an explicit remainder category
- **The Evidence:** Shneiderman recommends adding a dummy record whose size is the entire unused portion when displaying disk space utilization percentages [@shneidermanTreeVisualizationTreemaps1992].

## Where to Apply <!-- role: context -->

- **User Goal:** Understand how much capacity is used vs. free at a glance.
- **Data Type:** Storage-like totals where “unused” is meaningful and quantifiable.
- **Audience:** Users managing limited resources (e.g., disk space).

## When to Break It <!-- role: exceptions -->

- **Scenario:** There is no meaningful “total capacity” (only totals of observed items).
- **Reason:** A dummy “unused” category would be arbitrary and could mislead [@shneidermanTreeVisualizationTreemaps1992].

## The Price <!-- role: costs -->

- **The Sacrifice:** Adds one more region that may distract from the hierarchy of actual items.
- **The Risk:** If capacity is misreported, the unused region will distort perceived proportions [@shneidermanTreeVisualizationTreemaps1992].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Presenting a treemap of only used files but describing it as “percent of disk.”
- **Why it fails:** The treemap will always appear “full,” hiding the magnitude of free space [@shneidermanTreeVisualizationTreemaps1992].

## How to Check <!-- role: check -->

- **Visual Sign:** The treemap has no visible region representing free/unused capacity.
- **The Test:** Verify that the sum of child sizes under the root equals total capacity.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Create a single dummy child under the root with `size = totalCapacity - usedCapacity`.
- **Best Fix:** Label and color the unused region distinctly so users can interpret utilization immediately [@shneidermanTreeVisualizationTreemaps1992].
