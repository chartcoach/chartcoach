---
id: maximize-shape-variance-sci
title: Vary Shapes by Segmentability, Compactness, and Spikiness
bibliography: references.bib
description: Select shape symbols that differ along the three dimensions of preattentive
  processing.
labels:
- visual:shape
- chart:scatter
- task:search
- impact:efficiency
- complexity:advanced
---

## The Rule <!-- role: advice -->
When creating custom shape palettes, ensure symbols differ across three specific dimensions: **Segmentability** (presence of internal intersections), **Compactness** (solid vs. hollow/concave), and **Spikiness** (sharp protrusions). Do not rely solely on geometric rotation or number of sides.

## The Logic <!-- role: reason -->
Shape perception is not a unified process but relies on specific "preattentive" features extracted in parallel.
*   **The Principle:** The SCI Shape Space.
*   **The Evidence:** @huang_space_2020 modeled shape discriminability (d') across 91 pairs of shapes and found that 97.4% of the variance was explained by these three dimensions. For example, an intersection (Segmentability) acts as a "joint" that the eye detects instantly, distinguishing it from non-intersecting shapes.

## Where to Apply <!-- role: context -->
*   **User Goal:** "Texture segregation"—seeing regions of data points as distinct groups without serial scanning.
*   **Data Type:** High-density categorical scatterplots or maps.
*   **Audience:** Analytics users who need to spot patterns quickly.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** One-to-one comparison tasks.
*   **Reason:** @huang_space_2020 notes that while SCI features dominate attention-demanding tasks (like visual search), they are negligible in simple one-to-one comparisons where the user focuses on a single object. Detailed shape nuances matter more there.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You cannot use a "system" of similar shapes (e.g., open circle, filled circle, half-filled circle). You must use radically different shapes.
*   **The Risk:** Visual clutter. High-segmentability shapes (like a grid ⊞) and high-spikiness shapes (like a star ★) create more visual noise than simple dots.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Rotating the same shape (e.g., Square vs. Diamond).
*   **Why it fails:** Rotated shapes share identical values for Segmentability, Compactness, and Spikiness. The brain struggles to segregate them preattentively.
*   **The Wrong Fix:** Using a set like "Square, Circle, Triangle."
*   **Why it fails:** These shapes are overly compressed in the SCI space (all are high-compactness, low-segmentability, low-spikiness).

## How to Check <!-- role: check -->
*   **Visual Sign:** Are your shapes all "closed loops" without holes or crossing lines?
*   **The Test:** Assign each shape a score (Low/High) for: 1. Does it have crossing lines? 2. Does it have a hole/bite taken out? 3. Does it have spikes? If your shapes all have the same score profile, they are too similar.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a "Plus" (✚) or "Cross" (✖) to your set. These score high on Segmentability (intersection) and Spikiness, making them pop against solid shapes.
*   **Best Fix:** Ensure your palette includes at least one "Jointed" shape (e.g., ⊞), one "Hollow/Concave" shape (e.g., ☾ or 〇), and one "Spiky" shape (e.g., ★ or ∿).
