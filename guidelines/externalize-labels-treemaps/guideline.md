---
id: externalize-labels-treemaps
title: Externalize Text Details for Small Regions
bibliography: references.bib
description: Use interaction techniques like hover or click-to-view for labels, rather
  than forcing text inside small rectangles.
labels:
- chart:treemap
- visual:text
- task:identify
- interaction:hover
- impact:legibility
---

## The Rule <!-- role: advice -->
Do not attempt to write text labels inside every rectangle; instead, display details (name, date, extension) in a fixed area or pop-up when the user interacts with a region.

## The Logic <!-- role: reason -->
In a space-filling visualization showing thousands of nodes, many rectangles will be too small to contain legible text.
*   **The Principle:** Details on Demand.
*   **The Evidence:** [@shneiderman_tree_1992] notes that displaying names via "nested rectangles... would reduce the effective display space." Instead, the paper recommends users "move a cursor onto a candidate region, and then click to obtain the relevant information at the bottom line of the screen."

## Where to Apply <!-- role: context -->
This advice is designed for high-density displays.
*   **User Goal:** Identifying the specific entity represented by a visual block.
*   **Data Type:** Large trees with deep nesting or many leaf nodes.
*   **Audience:** Users interacting with a digital display (mouse/cursor).

## When to Break It <!-- role: exceptions -->
No rule is absolute. When is this advice actually WRONG?
*   **Scenario:** Static media (print).
*   **Reason:** Interaction is impossible. In print, only the largest nodes should be labeled, or a numbered legend system used (as seen in Figure 1 of [@shneiderman_tree_1992]).

## The Price <!-- role: costs -->
Every design choice has a cost.
*   **The Sacrifice:** Immediate identification of all nodes is lost; interaction is required.
*   **The Risk:** Users may lose context of which directory a file belongs to if path information isn't clearly shown during the interaction.

## Common Mistakes <!-- role: mistakes -->
How do people usually screw this up?
*   **The Wrong Fix:** Using nested frames for every directory level to hold labels.
*   **Why it fails:** It significantly reduces the screen space available for the actual data (the leaf nodes) [@shneiderman_tree_1992].

## How to Check <!-- role: check -->
How can I tell if I've broken this rule?
*   **Visual Sign:** Is text overlapping, clipped, or microscopic inside the boxes?
*   **The Test:** Can you read the label of a file that represents 0.1% of the disk space?

## How to Fix <!-- role: fix -->
I've broken the rule. How do I solve it?
*   **Quick Fix:** Show the label in a tooltip on hover.
*   **Best Fix:** Reserve a status bar at the bottom of the screen to display full attribute details (Name, Size, Date) of the node currently under the cursor [@shneiderman_tree_1992].
