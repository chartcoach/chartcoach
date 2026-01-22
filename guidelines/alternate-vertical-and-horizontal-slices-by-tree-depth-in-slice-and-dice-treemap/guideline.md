---
id: alternate-vertical-and-horizontal-slices-by-tree-depth-in-slice-and-dice-treemap
title: Alternate vertical and horizontal partitions by depth in a slice-and-dice treemap
bibliography: references.bib
description: Generate a treemap by slicing a parent rectangle among children proportionally,
  alternating the cut axis at each depth.
labels:
- chart:treemap
- task:layout
- visual:position
- impact:readability
- data:hierarchical
- audience:expert
- layout:slice-and-dice
---

## Alternate cut direction at each depth for treemap partitioning <!-- role: advice -->

Partition each node’s rectangle among its children in proportion to child size, and alternate the cut axis at each depth (vertical at one level, horizontal at the next). Recurse into each child using its allocated slice.

## Why alternating axes yields a simple linear-time layout <!-- role: reason -->

A deterministic alternation of cut direction avoids complex bin-packing while still filling space and preserving proportionality. The recursion assigns each subtree a contiguous region, making the algorithm straightforward and fast for large trees.

**Mechanism:** Axis alternation provides a consistent rule for placing partitions, enabling a recursive layout that only requires computing cumulative proportions along one dimension at each step.

**Evidence:** The described treemap algorithm divides the initial rectangle into proportional vertical slices for the root’s children, then recurses with a 90-degree rotation so that even levels partition vertically and odd levels partition horizontally; the algorithm runs linearly in the number of nodes [@shneidermanTreeVisualizationTreemaps1992].

**Notes:** Traversal order affects drawing order and whether deeper rectangles cover earlier paint operations.

## When axis alternation applies <!-- role: context -->

- **User Goal:** Display the entire hierarchy in a space-filling view with proportional areas.
- **Task:** Scan for large leaves and understand rough grouping by subtree.
- **Data:** Weighted tree with nonnegative sizes available at each node.
- **Chart Setting:** Need a fast, implementable layout without expensive packing optimization.
- **Audience:** Users who benefit from overview more than precise shape regularity.
- **Success Criterion:** Layout is fast to compute and consistently fills the available rectangle.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Extremely elongated rectangles severely hinder selection or perception for many items. **Why:** Repeated slicing can create thin strips that are hard to see or interact with at typical screen resolutions.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Rectangle aspect ratios can become extreme, reducing usability for dense data. **Risk:** Visual patterns and perceived grouping can depend heavily on child ordering. **Mitigation:** Control child ordering intentionally for the intended reading task.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Ignoring child ordering and accepting arbitrary filesystem or input order. **Why it fails:** The resulting visual arrangement may obscure meaningful structure or make comparisons harder.
- **Mistake:** Using the wrong denominator (not the parent’s total size) when computing slice boundaries. **Why it fails:** Areas no longer correspond to proportions of the parent, breaking interpretation.

## Quick tests <!-- role: check -->

**Failure Sign:** Many rectangles are so thin they cannot be reliably pointed at or distinguished. **Quick Check:** Measure the minimum rectangle width and height in pixels and compare to the target pointer/selection tolerance. **Stronger Test:** Time layout generation on large trees and verify linear scaling as nodes increase.

## What to do instead <!-- role: fix -->

- Reorder children by size or another meaningful attribute to reduce visually noisy striping in critical regions.
- Render only selected subtrees at once when the full tree produces too many thin slices for the display.
- Add zooming so users can expand a region to obtain usable aspect ratios for its descendants.
- Use nested frames for directories only when hierarchy boundaries must be emphasized, accepting reduced effective space.
