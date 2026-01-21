---
id: avoid-same-family-shape-palettes-in-default-symbol-sets
title: Avoid Same-Family Shape Palettes in Default Symbol Sets
bibliography: references.bib
description: Do not rely on default marker sets that cluster in the same region of
  preattentive shape space; replace confusable symbols with SCI-separated alternatives.
labels:
- chart:scatter
- task:distinguish
- visual:shape
- impact:clarity
- data:categorical
- audience:general
- tool:tableau
- tool:excel
- source:huang-2020
---

## The Rule <!-- role: advice -->

Audit default marker palettes (e.g., common software defaults) and replace shapes that are too similar to each other with shapes that are more widely separated in SCI space.

## The Logic <!-- role: reason -->

The paper argues that some commonly used symbol sets group into subsets that are not very distinguishable because they do not differ greatly on segmentability, compactness, or spikiness; using SCI-separated shapes improves discriminability for series separation.

- **The Principle:** Preattentive confusion occurs when symbols cluster in SCI space.
- **The Evidence:** [@huangSpacePreattentiveShape2020]

## Where to Apply <!-- role: context -->

- **User Goal:** Distinguish multiple plotted series/categories quickly.
- **Data Type:** Multi-series scatterplots or dot-based displays where shape carries category.
- **Audience:** Broad audiences; dashboards and reports where defaults are commonly used.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The display uses shape only redundantly (another strong channel already separates groups), and symbol differentiation is not required for task success.
- **Reason:** If shape is not the primary separator, investing in palette replacement may not materially change performance [@huangSpacePreattentiveShape2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less consistency with software defaults and templates.
- **The Risk:** Custom symbols may not export/render consistently across platforms.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Increasing the number of different symbols without checking whether they are genuinely discriminable (e.g., adding more variants of crosses/triangles).
- **Why it fails:** More symbols can still be crowded in SCI space, so the effective discriminability does not improve [@huangSpacePreattentiveShape2020].

## How to Check <!-- role: check -->

- **Visual Sign:** Two or more legend entries still look interchangeable at a glance even though their outlines differ.
- **The Test:** Grouping check—if symbols naturally “cluster” perceptually into subgroups (e.g., three cross-like marks vs. three triangle-like marks), you likely have SCI crowding [@huangSpacePreattentiveShape2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace one symbol from each confusable cluster with a symbol that introduces a missing SCI dimension (e.g., add a holed shape; add a strongly jointed/intersecting shape; add a spiky shape).
- **Best Fix:** Build a palette by selecting shapes that are well-separated across SCI, prioritizing maximal pairwise separation for the first N categories [@huangSpacePreattentiveShape2020].
