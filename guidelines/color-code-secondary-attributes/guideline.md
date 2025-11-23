---
id: color-code-secondary-attributes
title: Code Secondary Attributes with Color
bibliography: references.bib
description: Use color or shading to represent categorical or secondary quantitative
  data in space-filling charts.
labels:
- chart:treemap
- visual:color
- data:categorical
- data:temporal
- task:categorize
---

## The Rule <!-- role: advice -->
Use color variations (hue or gray shading) within rectangles to encode a second attribute distinct from the one controlling size.

## The Logic <!-- role: reason -->
Since the shape and position are determined by the hierarchy and size, color is the remaining channel available to show differentiation without text.
*   **The Principle:** Dual Encoding (Size + Color).
*   **The Evidence:** [@shneiderman_tree_1992] suggests that "color coding could represent different types of files... owners... frequency of use... or the age." This creates a "checkerboard" effect that reveals patterns (e.g., old files vs. new files) independent of the size.

## Where to Apply <!-- role: context -->
This advice is designed for multivariate hierarchical data.
*   **User Goal:** Correlating size with another factor (e.g., "Are the largest files also the oldest?").
*   **Data Type:** Nodes with multiple attributes (e.g., File Size + File Type).
*   **Audience:** Users needing to filter or spot properties visually.

## When to Break It <!-- role: exceptions -->
No rule is absolute. When is this advice actually WRONG?
*   **Scenario:** High-fidelity color reproduction is unavailable.
*   **Reason:** If limited to black and white, simple gray shading may be insufficient to distinguish many categories.

## The Price <!-- role: costs -->
Every design choice has a cost.
*   **The Sacrifice:** You must introduce boundary lines if adjacent colors are identical.
*   **The Risk:** "The effect of seeing thousands of small rectangles is like a checkerboard with varying sized spots," which may be visually overwhelming without careful palette selection [@shneiderman_tree_1992].

## Common Mistakes <!-- role: mistakes -->
How do people usually screw this up?
*   **The Wrong Fix:** Random coloring.
*   **Why it fails:** It wastes the channel. Color should be meaningful (e.g., brighter colors for more frequent use, yellow/gray for older files) [@shneiderman_tree_1992].

## How to Check <!-- role: check -->
How can I tell if I've broken this rule?
*   **Visual Sign:** Are all rectangles the same color?
*   **The Test:** Can you distinguish between two different types of data (e.g., text vs. graphics) without reading labels?

## How to Fix <!-- role: fix -->
I've broken the rule. How do I solve it?
*   **Quick Fix:** Assign colors to data types (e.g., Blue = Image, Red = Application).
*   **Best Fix:** Implement a control panel allowing the user to map specific attributes (owner, age, type) to the color channel dynamically [@shneiderman_tree_1992].
