---
id: visualize-hierarchies-space-filling
title: Visualize Large Hierarchies with Space-Filling Rectangles
bibliography: references.bib
description: Use tree-maps to display large hierarchical structures within a fixed
  screen space by utilizing 100% of the area.
labels:
- chart:treemap
- task:overview
- visual:area
- impact:efficiency
- data:hierarchical
- audience:analyst
---

## The Rule <!-- role: advice -->
Represent complex hierarchical tree structures as nested rectangles where 100% of the designated space is utilized, rather than using traditional node-link diagrams.

## The Logic <!-- role: reason -->
Traditional node-link graphs (root at top, connections below) often waste significant background screen space and become unreadable when the node count exceeds practical limits (e.g., requiring scrolling or page turning).
*   **The Principle:** Space-filling Visualization.
*   **The Evidence:** [@shneiderman_tree_1992] argues that node-link layouts "soon overwhelm the available display space and users cannot grasp the entire picture." By contrast, the tree-map algorithm ensures the entire designated area is partitioned, maximizing data density for human visualization.

## Where to Apply <!-- role: context -->
This advice is designed for visualizing deep or wide hierarchies where the global context is necessary.
*   **User Goal:** Recognizing patterns in large datasets, such as identifying large files on a hard drive or budget allocations in an organization.
*   **Data Type:** Hierarchical trees with weighted leaf nodes (e.g., file directories, organizational charts).
*   **Audience:** Users needing to manage resources or analyze distribution across a whole system.

## When to Break It <!-- role: exceptions -->
No rule is absolute. When is this advice actually WRONG?
*   **Scenario:** The structural relationships (parent-child links) are more important than the node attributes (size/weight).
*   **Reason:** Tree-maps emphasize the weight (area) of leaf nodes; the structural topology is implicit in the nesting and harder to trace than in a node-link diagram.

## The Price <!-- role: costs -->
Every design choice has a cost.
*   **The Sacrifice:** Explicit visibility of the tree topology (edges and levels) is reduced compared to a standard graph.
*   **The Risk:** Users may struggle to distinguish hierarchy levels without additional cues like borders or margins.

## Common Mistakes <!-- role: mistakes -->
How do people usually screw this up?
*   **The Wrong Fix:** Using standard indentation lists for thousands of items.
*   **Why it fails:** As noted in [@shneiderman_tree_1992], "even elegant tree-like layouts... soon overwhelm the available display space."

## How to Check <!-- role: check -->
How can I tell if I've broken this rule?
*   **Visual Sign:** Are there large gaps of white space (background) between nodes?
*   **The Test:** If the visualization contains thousands of nodes, can the entire structure be viewed without scrolling?

## How to Fix <!-- role: fix -->
I've broken the rule. How do I solve it?
*   **Quick Fix:** Recursively partition the display area into rectangles alternating horizontal and vertical cuts.
*   **Best Fix:** Implement the Tree-Map algorithm where a root rectangle is sliced based on the weight of its children [@shneiderman_tree_1992].
