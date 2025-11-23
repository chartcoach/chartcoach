---
id: visual-interference-small-marks
title: Do Not Combine Shape and Small Size
bibliography: references.bib
description: Prevent visual interference where reducing the size of a mark makes its
  shape indistinguishable.
labels:
- visual:shape
- visual:size
- design:composition
- impact:legibility
- source:implementation
---

## The Rule <!-- role: advice -->
When composing visual variables, do not use **Shape** to encode information if the marks are also being varied by **Size** such that they become very small.

## The Logic <!-- role: reason -->
Composition of visual designs can have side effects. Specifically, the perception of shape requires a minimum resolution. When size is used as an encoding variable, the smaller values may render the object too small for the eye to distinguish its shape.
*   **The Principle:** Side Effects of Composition (Interference)
*   **The Evidence:** [@mackinlay_automating_1986] notes that "the shapes of the small objects begin to look the same" when size and shape are composed, reducing the effectiveness of the design.

## Where to Apply <!-- role: context -->
*   **User Goal:** Simultaneously reading two variables encoded on the same set of marks.
*   **Data Type:** Multivariate data (one nominal variable mapped to Shape, one quantitative mapped to Size).
*   **Audience:** Any viewer.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The "small" end of the size range is explicitly clamped to a minimum readable threshold.
*   **Reason:** If the smallest mark is still large enough to identify the shape clearly, the rule is satisfied.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the dynamic range of the Size variable (you must make the minimum size larger, consuming more screen space).
*   **The Risk:** Clutter increases as minimum mark size increases.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Allowing the size variable to scale down to a single pixel or very few pixels while still relying on shape (squares vs triangles).
*   **Why it fails:** At small sizes, all shapes perceptually degrade into "points" or "blobs" [@mackinlay_automating_1986].

## How to Check <!-- role: check -->
*   **Visual Sign:** Can you distinguish the square from the circle in the smallest cluster of data points?
*   **The Test:** Squint at the chart. If the shapes blend into generic dots in the dense/small areas, the encoding has failed.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Increase the minimum size of the marks (scale up).
*   **Best Fix:** Split the visualization into multiple charts (Small Multiples) or map the Shape variable to Color instead.
