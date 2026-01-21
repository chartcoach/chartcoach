---
id: use-adjacency-diagrams-to-encode-size-in-hierarchies
title: Use Adjacency Diagrams When Node Size Is a Key Dimension
bibliography: references.bib
description: Use icicle or sunburst layouts to represent hierarchy with space-filling
  nodes that can encode size.
labels:
- chart:icicle
- task:part-to-whole
- visual:length
- impact:insight
- data:hierarchical
- audience:analyst
- complexity:intermediate
---

## The Rule <!-- role: advice -->

When you need the hierarchy and a quantitative size per node, use an adjacency diagram (icicle or sunburst) so node length/arc size encodes magnitude.

## The Logic <!-- role: reason -->

Adjacency diagrams are space-filling variants of node-link trees; because nodes become solid bars/arcs, you can encode node size with length while still revealing hierarchical position via adjacency.

- **The Principle:** Space-filling adjacency enables an additional quantitative encoding
- **The Evidence:** [@heerTourVisualizationZoo2010]

## Where to Apply <!-- role: context -->

- **User Goal:** See hierarchical structure and compare sizes of branches/nodes
- **Data Type:** Trees with a meaningful size metric per node (e.g., file/class size)
- **Audience:** Analysts exploring composition across levels

## When to Break It <!-- role: exceptions -->

- **Scenario:** Precise tracing of parent–child links is more important than size comparison
- **Reason:** Node-link diagrams may make relational paths more explicit [@heerTourVisualizationZoo2010]

## The Price <!-- role: costs -->

- **The Sacrifice:** Some immediate intuitiveness compared to a classic node-link “tree”
- **The Risk:** Small nodes become too thin to label

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding size labels everywhere in a node-link diagram to compensate
- **Why it fails:** The visualization still doesn’t make size comparisons quick; space-filling length encoding is the point [@heerTourVisualizationZoo2010]

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers ask “which branch is biggest?” and you can’t answer visually
- **The Test:** If you can’t compare sibling magnitudes at a glance, you’re missing a size encoding [@heerTourVisualizationZoo2010]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch to an icicle layout (Cartesian) for easier length comparison
- **Best Fix:** Use icicle or sunburst generated from a partition layout and ensure size is mapped to bar length/arc extent [@heerTourVisualizationZoo2010]
