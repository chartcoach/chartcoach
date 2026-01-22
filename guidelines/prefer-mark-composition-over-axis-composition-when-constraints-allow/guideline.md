---
id: prefer-mark-composition-over-axis-composition-when-constraints-allow
title: Prefer mark composition over axis composition when constraints allow
bibliography: references.bib
description: When combining designs, merge compatible mark sets to avoid adding objects
  and to keep the composite easier to read as a whole.
labels:
- chart:multivariate
- task:compose
- visual:retinal
- impact:clarity
- data:relational
- audience:expert
- concept:mark-composition
---

## Merge marks when the same entities appear across relations <!-- role: advice -->

Prefer composing by merging compatible mark sets (mark composition) when multiple relations refer to the same entities and do not impose conflicting mark constraints.

## Why mark composition is typically the most effective composition <!-- role: reason -->

Mark composition integrates multiple encodings into the same marks, so the number of graphical objects does not increase while more information is carried per object. This tends to be more effective than axis-only compositions that place separate charts adjacent to each other.

**Mechanism:** Reusing the same marks concentrates attention and reduces scanning costs compared with splitting information across separate mark sets or panels.

**Evidence:** Mark composition is described as the most effective of the composition operators because it merges designs without increasing the number of graphical objects, while single-axis composition is least effective because it does not merge designs [@mackinlayAutomatingDesignGraphical1986b]. Examples show integrated composites built by merging mark sets that encode the same domain values under compatible constraints [@mackinlayAutomatingDesignGraphical1986b].

**Notes:** Compatibility requires that shared positional and retinal constraints do not conflict across the marks being merged.

## When this applies <!-- role: context -->

- **User Goal:** See multiple attributes of the same entities in one integrated display.
- **Task:** Compare entities while considering multiple relations at once.
- **Data:** Multiple relations sharing a common domain set of entities.
- **Chart Setting:** Encodings that can coexist on the same marks (position plus retinal channels, or compatible positional constraints).
- **Audience:** Readers who benefit from single-glance integration.
- **Success Criterion:** Integrated reading without increasing object count or forcing excessive scanning.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The component designs require conflicting positional constraints for the same marks (for example, the same mark would need two different axis positions). **Why:** The marks cannot be merged without violating the semantics of one or both encodings [@mackinlayAutomatingDesignGraphical1986b].

## Tradeoffs <!-- role: costs -->

**Sacrifice:** Integrated marks can become visually overloaded, especially if too many encodings are stacked on each mark. **Risk:** Some retinal channel combinations can interact and reduce legibility. **Mitigation:** Limit the number of concurrent encodings per mark and reserve integrated designs for the most important relations.

## Common mistakes <!-- role: mistakes -->

**Mistake:** Forcing mark composition even when two relations require different positions for the same marks. **Why it fails:** The composition cannot satisfy both positional encodings at once, so the design becomes invalid or misleading [@mackinlayAutomatingDesignGraphical1986b].

## Quick tests <!-- role: check -->

**Failure Sign:** A single entity would need to appear in two different places to satisfy two encodings. **Quick Check:** Confirm that any shared axes imply identical mark positions for the merged entities. **Stronger Test:** Check that no retinal property is required to encode two different domain sets simultaneously in the merged marks.

## What to do instead <!-- role: fix -->

- Switch to double-axes composition when both relations can share axes but keep separate mark sets.
- Switch to single-axis composition when only one shared axis exists and marks cannot be merged.
- Reassign one relation to a different encoding channel to remove conflicts before attempting mark composition.
- Partition relations into subsets that can be composed without constraint conflicts.
