---
id: choose-marker-shapes-far-apart-in-sci-shape-space
title: Choose Marker Shapes That Are Far Apart in SCI Shape Space
bibliography: references.bib
description: Use shape symbols that differ strongly on segmentability, compactness,
  and spikiness to maximize rapid, preattentive separability.
labels:
- chart:scatter
- task:group
- visual:shape
- impact:clarity
- data:categorical
- audience:general
- model:sci-shape-space
- source:huang-2020
---

## The Rule <!-- role: advice -->

Choose symbol shapes that are maximally separated along the three SCI dimensions—**segmentability**, **compactness**, and **spikiness**—rather than choosing several shapes that only vary slightly within one “shape family.”

## The Logic <!-- role: reason -->

Preattentive shape discriminability is well predicted by distances in a 3D feature space: segmentability, compactness, and spikiness. Larger featural distance corresponds to higher discriminability in an attention-demanding segregation task, so selecting shapes far apart in this space makes categories easier to separate rapidly.

- **The Principle:** Discriminability increases with featural distance in SCI space.
- **The Evidence:** [@huangSpacePreattentiveShape2020]

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly separating categories/series by marker shape (preattentively), before reading values.
- **Data Type:** Categorical series encoded by shape (e.g., multiple groups plotted together).
- **Audience:** Mixed or general audiences; especially when viewers must parse dense displays fast.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The task requires fine, deliberate one-to-one shape comparison (not attention-demanding selection).
- **Reason:** The SCI space is derived from a preattentive, attention-demanding texture segregation task and may not fully predict postattentive, detailed shape judgments [@huangSpacePreattentiveShape2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** Some “brand-consistent” or stylistically matched symbol sets may be ruled out.
- **The Risk:** Highly distinctive shapes can feel visually heavy or inconsistent across a design system.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Picking many symbols from a single cluster (e.g., several crosses/plus-like or several triangle-like variants).
- **Why it fails:** Those shapes are close in SCI space (small featural distance), so they are less discriminable preattentively [@huangSpacePreattentiveShape2020].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers confuse series that “look like the same kind of shape” at a glance.
- **The Test:** Brief-glance test—look for 100 ms-equivalent separability: can you reliably tell groups apart without focusing on one symbol at a time? (This mirrors the attention-demanding premise of the SCI evidence.) [@huangSpacePreattentiveShape2020]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace one or more symbols with shapes that differ strongly on a missing SCI dimension (e.g., add a hole/closure difference, or add an intersection/joint).
- **Best Fix:** Build the symbol palette by explicitly spanning all three SCI dimensions—include at least one shape with high segmentability (junctions), one with low compactness (hole/strong concavity), and one with high spikiness (sharp outward spikes) [@huangSpacePreattentiveShape2020].
