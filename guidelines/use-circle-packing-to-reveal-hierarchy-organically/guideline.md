---
id: use-circle-packing-to-reveal-hierarchy-organically
title: Use Circle Packing When You Want Hierarchy to Be Visually Salient
bibliography: references.bib
description: Use circle-packing layouts to emphasize hierarchical nesting with an
  organic appearance and area-based size comparison.
labels:
- chart:circle-packing
- task:understand-structure
- visual:area
- impact:engagement
- data:hierarchical
- audience:novice
- complexity:intermediate
---

## The Rule <!-- role: advice -->

Use a circle-packing enclosure diagram when you want hierarchical nesting to stand out visually and can tolerate lower space efficiency than a treemap.

## The Logic <!-- role: reason -->

Circle packing uses containment to reveal hierarchy and the “wasted space” can make the hierarchy more apparent; node sizes can still be compared via area judgments.

- **The Principle:** Use enclosure with perceptible negative space to emphasize nesting
- **The Evidence:** [@heerTourVisualizationZoo2010]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand hierarchical grouping and relative sizes with strong visual cues
- **Data Type:** Hierarchies with size metrics
- **Audience:** Mixed audiences when an engaging, interpretable nesting cue is helpful

## When to Break It <!-- role: exceptions -->

- **Scenario:** Space is tight and you need maximum density
- **Reason:** Circle packing is less space-efficient than treemaps [@heerTourVisualizationZoo2010]

## The Price <!-- role: costs -->

- **The Sacrifice:** Space efficiency and sometimes precise area comparison
- **The Risk:** Small circles become hard to label

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Choosing circle packing to maximize the number of nodes shown
- **Why it fails:** It wastes space compared to treemaps [@heerTourVisualizationZoo2010]

## How to Check <!-- role: check -->

- **Visual Sign:** Many small circles with unreadable labels; lots of unused whitespace while you still need more room
- **The Test:** If you’re constrained primarily by space, a treemap is likely a better fit [@heerTourVisualizationZoo2010]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce displayed depth (show fewer levels) to improve legibility
- **Best Fix:** Switch to a treemap when the priority is space-efficient size comparison [@heerTourVisualizationZoo2010]
