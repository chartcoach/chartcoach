---
id: use-treemap-space-filling-rectangles-to-show-weighted-trees
title: Visualize Weighted Trees as Space-Filling Rectangles
bibliography: references.bib
description: Show an entire weighted tree by filling a 2D region with nested rectangles
  whose areas represent node weights.
labels:
- chart:treemap
- task:overview
- visual:area
- impact:clarity
- data:hierarchical
- audience:novice
- source:shneiderman-1992
---

## The Rule <!-- role: advice -->

Visualize a weighted tree using a treemap: draw each node as a rectangle whose area is proportional to its weight (e.g., bytes), filling the available 2D space.

## The Logic <!-- role: reason -->

A space-filling layout lets users see the whole hierarchy at once and immediately perceive relative magnitudes via area, even when there are thousands of leaves.

- **The Principle:** Space-filling overview + magnitude-by-area encoding
- **The Evidence:** Shneiderman introduces treemaps specifically to show entire trees within limited screen space while revealing relative leaf sizes through rectangle area [@shneidermanTreeVisualizationTreemaps1992].

## Where to Apply <!-- role: context -->

- **User Goal:** Get a quick overview and spot the largest leaves anywhere in the hierarchy (e.g., large files to delete).
- **Data Type:** Tree-structured data with a quantitative weight per leaf (and/or aggregated to internal nodes).
- **Audience:** Users who need an at-a-glance picture of large hierarchies (e.g., disk usage).

## When to Break It <!-- role: exceptions -->

- **Scenario:** The primary task is understanding explicit parent–child link structure/path tracing.
- **Reason:** Treemaps emphasize space and size; they do not show connecting edges like node-link diagrams, which may better support path-following [@shneidermanTreeVisualizationTreemaps1992].

## The Price <!-- role: costs -->

- **The Sacrifice:** You lose explicit edges and familiar “root-at-top” tree layout conventions.
- **The Risk:** Small or zero-weight leaves can become too small to see or may be omitted [@shneidermanTreeVisualizationTreemaps1992].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a standard node-link tree and trying to show “everything” at once.
- **Why it fails:** The display space is quickly overwhelmed and users cannot grasp the entire picture [@shneidermanTreeVisualizationTreemaps1992].

## How to Check <!-- role: check -->

- **Visual Sign:** Users can’t see the whole hierarchy on one screen, or large leaves are not immediately obvious.
- **The Test:** Ask a user to identify the largest items; if they must scroll/traverse many nodes, the overview is failing.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch from node-link to a treemap with area proportional to weight.
- **Best Fix:** Ensure internal nodes aggregate subtree weights so every partition correctly represents totals [@shneidermanTreeVisualizationTreemaps1992].
