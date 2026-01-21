---
id: use-arc-diagrams-with-good-ordering-to-spot-cliques-and-bridges
title: Use Arc Diagrams with Careful Ordering to Reveal Cliques and Bridges
bibliography: references.bib
description: Use arc diagrams to show network links along a one-dimensional node order
  that highlights structure.
labels:
- chart:arc-diagram
- task:find-clusters
- visual:position
- impact:clarity
- data:network
- audience:analyst
- custom:seriation
---

## The Rule <!-- role: advice -->

Use an arc diagram only if you can order nodes well; rely on the ordering to reveal cliques and bridges.

## The Logic <!-- role: reason -->

Arc diagrams place nodes on a line and encode links as arcs; while they may convey overall structure less well than 2D layouts, a good node ordering makes clusters and bridges easier to identify, and supports showing extra attributes alongside nodes.

- **The Principle:** One-dimensional layout shifts the problem to ordering (seriation)
- **The Evidence:** [@heerTourVisualizationZoo2010]

## Where to Apply <!-- role: context -->

- **User Goal:** Identify cliques, bridges, and local connectivity patterns
- **Data Type:** Networks where a meaningful ordering can be computed or is inherent
- **Audience:** Analysts; settings where side-by-side node attributes are useful

## When to Break It <!-- role: exceptions -->

- **Scenario:** You cannot produce a meaningful ordering
- **Reason:** Without good seriation, arcs become visually uninformative and cluttered [@heerTourVisualizationZoo2010]

## The Price <!-- role: costs -->

- **The Sacrifice:** Some global structure readability compared to 2D network layouts
- **The Risk:** Poor ordering obscures patterns rather than revealing them

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using an arbitrary node order (e.g., alphabetical) and expecting clusters to emerge
- **Why it fails:** The effectiveness depends on ordering; seriation is the core problem [@heerTourVisualizationZoo2010]

## How to Check <!-- role: check -->

- **Visual Sign:** Arcs are uniformly tangled with no clear groupings
- **The Test:** Try an alternative ordering; if structure changes drastically, ordering is driving perception and needs to be computed intentionally [@heerTourVisualizationZoo2010]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reorder nodes using a clustering/community result if available
- **Best Fix:** Treat ordering as a first-class step (seriation) and iterate until cliques/bridges become visually distinct [@heerTourVisualizationZoo2010]
