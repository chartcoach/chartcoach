---
id: use-sci-optimized-shape-palette
title: Use the SCI-Optimized Shape Palette for Scatterplots
bibliography: references.bib
description: Use a specific set of six shapes (Window, Crescent, Ring, Plus, Disc,
  Squiggle) that are mathematically optimized for distinctiveness.
labels:
- chart:scatterplot
- visual:shape
- task:distinguish
- impact:clarity
- data:categorical
- audience:general
---

## The Rule <!-- role: advice -->
When encoding categorical data with shapes (glyphs), use the following six shapes in this order of priority: Window (⊞), Crescent (☾), Ring (〇), Plus (✚), Solid Disc (●), and Squiggle (∿).

## The Logic <!-- role: reason -->
Human vision processes shapes preattentively using three specific dimensions: **S**egmentability (intersections), **C**ompactness (holes/concavity), and **S**pikiness (sharp points). Standard shape palettes (like circles vs. squares) often cluster too closely in this perceptual space.

The recommended set is optimized to maximize the distance between items within this 3D "SCI" space.
*   **The Principle:** SCI Shape Space (Segmentability, Compactness, Spikiness).
*   **The Evidence:** @huang_space_2020 demonstrably proves that this specific set improves discriminability compared to default palettes found in tools like Excel or Tableau (specifically comparing against sets like `Diamond, Circle, Square` which are perceptually similar).

## Where to Apply <!-- role: context -->
*   **User Goal:** Rapidly distinguishing between different categories in a dense display.
*   **Data Type:** Nominal (categorical) data mapped to shape.
*   **Audience:** Users performing visual search or texture segregation tasks (finding a specific category among many).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Semantic mapping is required.
*   **Reason:** If a specific shape has a strong semantic meaning for the data (e.g., using an airplane icon for airport data), the semantic value outweighs the abstract perceptual optimization.
*   **Scenario:** Very small sizes.
*   **Reason:** Complex shapes like the "Window" (⊞) may become muddy at very low pixel resolutions (e.g., < 6px).

## The Price <!-- role: costs -->
*   **The Sacrifice:** Aesthetic consistency. The shapes are geometrically diverse (some curved, some straight, some filled, some open) and may look less "clean" than a set of uniform filled polygons.
*   **The Risk:** The "Squiggle" (∿) or "Window" (⊞) might look like unfamiliar or non-standard chart symbols to conservative audiences.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using filled polygons that only differ by number of sides (e.g., Triangle, Square, Pentagon, Hexagon).
*   **Why it fails:** @huang_space_2020 notes that simple polygons often reside on the same dimension of compactness and lack spikiness or segmentation, making them preattentively difficult to separate.

## How to Check <!-- role: check -->
*   **Visual Sign:** Do your shapes look like a "family" of solid blobs?
*   **The Test:** Glance at the scatterplot for 200ms. Can you instantly identify the distinct groups, or do you have to scan shape-by-shape?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Replace your third and fourth categories with the Plus (✚) and Ring (〇) to introduce segmentation and holes.
*   **Best Fix:** Adopt the full SCI sequence: ⊞, ☾, 〇, ✚, ●, ∿.
