---
id: use-matrix-views-for-large-dense-networks-to-avoid-hairballs
title: Use Matrix Views for Large, Dense Networks to Eliminate Edge Crossings
bibliography: references.bib
description: Use adjacency matrix visualizations to reveal clusters and bridges in
  dense networks without line-crossing clutter.
labels:
- chart:matrix
- task:find-clusters
- visual:color
- impact:clarity
- data:network
- audience:analyst
- custom:seriation
---

## The Rule <!-- role: advice -->

For large, highly connected networks, use an adjacency matrix view and sort rows/columns to expose clusters and bridges.

## The Logic <!-- role: reason -->

Node-link diagrams can become unreadable “hairballs” as size and density increase; matrix views avoid line crossings entirely, and with effective ordering you can quickly spot clusters and bridging structure.

- **The Principle:** Replace edge-drawing with a crossing-free adjacency encoding plus ordering
- **The Evidence:** [@heerTourVisualizationZoo2010]

## Where to Apply <!-- role: context -->

- **User Goal:** Detect clusters, blocks, and bridges in dense graphs
- **Data Type:** Large networks with many edges
- **Audience:** Analysts exploring network structure

## When to Break It <!-- role: exceptions -->

- **Scenario:** The primary task is path-following between specific nodes
- **Reason:** Path-following is more difficult in a matrix than in a node-link diagram [@heerTourVisualizationZoo2010]

## The Price <!-- role: costs -->

- **The Sacrifice:** Ease of tracing multi-step paths visually
- **The Risk:** Poor ordering hides structure; the matrix can look like noise

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Showing the adjacency matrix without thoughtful ordering
- **Why it fails:** Ordering is crucial to revealing clusters; seriation still matters [@heerTourVisualizationZoo2010]

## How to Check <!-- role: check -->

- **Visual Sign:** The matrix looks like random speckle with no visible blocks
- **The Test:** Reorder by a grouping (e.g., community detection); if blocks emerge, your prior ordering was the problem [@heerTourVisualizationZoo2010]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Apply a clustering/community-based ordering to rows and columns
- **Best Fix:** Add interactive grouping and reordering to support deeper exploration of network structure [@heerTourVisualizationZoo2010]
