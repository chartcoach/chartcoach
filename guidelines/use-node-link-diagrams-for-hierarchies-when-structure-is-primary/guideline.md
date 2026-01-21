---
id: use-node-link-diagrams-for-hierarchies-when-structure-is-primary
title: Use Node-Link Tree Diagrams When Hierarchy Structure Matters Most
bibliography: references.bib
description: "Use node-link diagrams to communicate hierarchical parent\u2013child\
  \ structure clearly."
labels:
- chart:tree
- task:understand-structure
- visual:position
- impact:clarity
- data:hierarchical
- audience:analyst
- complexity:intermediate
---

## The Rule <!-- role: advice -->

Use a node-link diagram to show hierarchical structure when the primary need is understanding parent–child relationships.

## The Logic <!-- role: reason -->

Tree layout algorithms (e.g., tidy layouts) position nodes to reveal branching structure; node-link diagrams map hierarchy to an easily recognized “tree” form.

- **The Principle:** Explicit links make hierarchy relationships legible
- **The Evidence:** [@heerTourVisualizationZoo2010]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand the structure of a hierarchy (what contains what)
- **Data Type:** Trees (packages/classes, organizational charts, phylogenies)
- **Audience:** Users scanning relationships more than quantities

## When to Break It <!-- role: exceptions -->

- **Scenario:** You need to compare node sizes across the hierarchy efficiently
- **Reason:** Space-filling approaches (icicle/treemap) better reveal size as an additional dimension [@heerTourVisualizationZoo2010]

## The Price <!-- role: costs -->

- **The Sacrifice:** Efficient use of space compared to space-filling layouts
- **The Risk:** Labels can become crowded in large trees

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Forcing size comparisons into node-link diagrams without space-filling encoding
- **Why it fails:** Quantity is harder to compare without consistent length/area encoding [@heerTourVisualizationZoo2010]

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers can follow links but can’t judge “what’s big” versus “what’s small”
- **The Test:** If quantitative comparison is central, try a space-filling alternative [@heerTourVisualizationZoo2010]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Choose a tidy layout that reduces wasted space and improves readability
- **Best Fix:** Switch to an adjacency or enclosure diagram when size encoding is required [@heerTourVisualizationZoo2010]
