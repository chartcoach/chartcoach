---
id: encode-leaf-node-weight-as-rectangle-area-in-a-treemap
title: "Encode each leaf node\u2019s weight as rectangle area in a treemap"
bibliography: references.bib
description: Represent a weighted tree by mapping each node to a rectangle whose area
  is proportional to its size attribute.
labels:
- chart:treemap
- task:overview
- visual:area
- impact:clarity
- data:hierarchical
- audience:expert
- encoding:area
---

## Encode node weight as rectangle area in a treemap <!-- role: advice -->

Map each node in a weighted tree to a rectangle whose area is proportional to a chosen size attribute (for example, file bytes). Ensure the full display region is completely filled by the set of rectangles.

## Why proportional-area rectangles support whole-tree overview <!-- role: reason -->

Using area as the encoding makes relative magnitudes visible at a glance while keeping every item on-screen at once via a space-filling layout. This enables rapid identification of large elements anywhere in the hierarchy without requiring scrolling through separate directory views.

**Mechanism:** Proportional areas create a preattentive “biggest stands out” signal while the space-filling property guarantees global coverage of the tree in fixed screen space.

**Evidence:** A space-filling 2-D representation with rectangle areas proportional to node size is presented as a way to view entire large trees (for example, thousands of files) and quickly spot the largest leaves for actions like deletion when storage is tight [@shneidermanTreeVisualizationTreemaps1992].

**Notes:** The size attribute can be any meaningful weight, not only storage bytes, as long as it is additive over subtrees.

## When proportional-area encoding applies <!-- role: context -->

- **User Goal:** Get an overview of a whole hierarchy while seeing relative magnitude of elements.
- **Task:** Find largest contributors (and their location in the hierarchy) quickly.
- **Data:** Tree-structured data with a nonnegative weight per leaf (and ideally additive totals for internal nodes).
- **Chart Setting:** Fixed 2-D screen or page area where showing “everything at once” is desired.
- **Audience:** Users who need scanning and prioritization rather than reading long labels.
- **Success Criterion:** Large items are immediately discoverable and the entire tree is visible simultaneously.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The tree has many zero or extremely small weights that must still be individually visible. **Why:** Rectangles for tiny or zero weights become too small to represent and may be eliminated or effectively invisible.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Fine-grained readability of small items and labels in exchange for global coverage. **Risk:** Very small or zero-size nodes may disappear, biasing attention toward large nodes only. **Mitigation:** Use interaction (such as zooming or selection) when small items must be inspected.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Treating internal-node sizes as independent rather than the sum of their subtree. **Why it fails:** The layout proportions no longer represent meaningful totals, breaking the hierarchical magnitude interpretation.
- **Mistake:** Expecting all leaves to remain visible regardless of size range. **Why it fails:** Large ranges of weights produce rectangles too small to render for small leaves.

## Quick tests <!-- role: check -->

**Failure Sign:** Numerous leaves are missing or appear as hairline slivers with no selectable area. **Quick Check:** Compare the smallest visible rectangle size to the display’s pixel resolution and count how many leaves fall below that threshold. **Stronger Test:** Ask users to find and select a small-but-important file/topic; if they cannot reliably locate it, the representation is failing for that use.

## What to do instead <!-- role: fix -->

- Filter to a subtree or selected directories/topics to increase effective detail for the remaining leaves.
- Add zooming to reveal small rectangles when users need to inspect small files or deep subtrees.
- Aggregate tiny leaves into a single group node when individual identity is not required at overview scale.
- Provide hover/click lookup so users can retrieve item details without relying on labels inside rectangles.
