---
id: map-weight-to-area
title: Map Node Importance to Rectangle Area
bibliography: references.bib
description: Assign the area of each rectangle in a hierarchy to a quantitative attribute
  like size or cost.
labels:
- chart:treemap
- visual:area
- task:compare
- data:quantitative
- impact:clarity
---

## The Rule <!-- role: advice -->
Calculate the dimensions of each rectangle in the hierarchy so that its area is strictly proportional to a specific quantitative attribute (weight) of that node.

## The Logic <!-- role: reason -->
Allocating space based on an attribute allows users to instantly spot anomalies or dominant elements within a large set.
*   **The Principle:** Proportional Area Encoding.
*   **The Evidence:** In the context of hard disk management, [@shneiderman_tree_1992] states the goal is to "allow users to recognize rapidly the larger files." The algorithm partitions the region $[x1, x2]$ based on the fraction $(Size(child)/Size(root))$, ensuring the visual weight matches the data weight.

## Where to Apply <!-- role: context -->
This advice is designed for moments where relative magnitude matters more than count.
*   **User Goal:** finding "candidates for deletion" on a disk, identifying costly stocks, or spotting large budget items.
*   **Data Type:** Hierarchical data where leaf nodes have a value (size, cost, time) that sums up the branch.
*   **Audience:** Users performing optimization or auditing tasks.

## When to Break It <!-- role: exceptions -->
No rule is absolute. When is this advice actually WRONG?
*   **Scenario:** All leaf nodes are of equal importance, regardless of size.
*   **Reason:** If the user needs to see the *count* of items rather than their *value*, area coding by value is misleading. (In this case, every leaf could be assigned a size of 1).

## The Price <!-- role: costs -->
Every design choice has a cost.
*   **The Sacrifice:** Small items become very difficult to see or select.
*   **The Risk:** Very small files or zero-byte files "become too small to represent and are currently eliminated" [@shneiderman_tree_1992].

## Common Mistakes <!-- role: mistakes -->
How do people usually screw this up?
*   **The Wrong Fix:** Making all directory rectangles equal size to ensure visibility.
*   **Why it fails:** It destroys the ability to "gain a better representation of the utilization of storage space" [@shneiderman_tree_1992].

## How to Check <!-- role: check -->
How can I tell if I've broken this rule?
*   **Visual Sign:** Do large values appear visually smaller than small values?
*   **The Test:** Compare a rectangle representing 10 units vs 100 units. The second should be visually 10x larger.

## How to Fix <!-- role: fix -->
I've broken the rule. How do I solve it?
*   **Quick Fix:** Adjust the drawing algorithm to calculate split positions based on cumulative subtree weights.
*   **Best Fix:** Ensure interior nodes propagate the sums of their children so the root represents the total, then partition recursively [@shneiderman_tree_1992].
