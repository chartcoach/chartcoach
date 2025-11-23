---
id: use-matrix-dense-networks
title: Use Matrix Views for Dense Networks
bibliography: references.bib
description: Switch to adjacency matrices to avoid 'hairballs' in dense network visualizations.
labels:
- chart:matrix
- chart:network
- visual:layout
- data:network
- impact:readability
---

## The Rule <!-- role: advice -->
When visualizing large, highly connected networks, use a Matrix View (adjacency matrix) instead of a node-link diagram.

## The Logic <!-- role: reason -->
Node-link diagrams degrade into unreadable "hairballs" as connectivity increases.
*   **The Principle:** Elimination of Occlusion
*   **The Evidence:** In matrix views, line crossings are impossible. Each value corresponds to a grid cell (link from node i to node j). This makes it easier to spot clusters and bridges in dense data, provided the matrix is sorted effectively [@heer_tour_2010].

## Where to Apply <!-- role: context -->
*   **User Goal:** identifying clusters or saturation in a network.
*   **Data Type:** Large, highly connected networks (graphs).
*   **Audience:** Researchers or data scientists analyzing network structure.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When the user needs to follow a path through the network (e.g., "Who is a friend of a friend of X?").
*   **Reason:** Path-following is significantly more difficult in a matrix view than in a node-link diagram [@heer_tour_2010].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the intuitive "map-like" structure of the node-link diagram.
*   **The Risk:** The visualization is useless if the rows and columns are not sorted (seriation) to reveal structure.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a force-directed layout for a dense graph without filtering.
*   **Why it fails:** It results in a "giant hairball" of crossings where structure cannot be seen.

## How to Check <!-- role: check -->
*   **Visual Sign:** Is your network visualization a solid mass of overlapping lines?
*   **The Test:** Can you clearly see individual relationships? If not, switch to Matrix.

## How to Fix <!-- role: fix -->
*   **Best Fix:** Convert the graph to an adjacency matrix and apply a seriation (sorting) algorithm to group related nodes [@heer_tour_2010].
