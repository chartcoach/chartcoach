---
id: choose-shape-symbols-that-are-far-apart-in-sci-shape-space
title: "Choose categorical shape symbols that are far apart in Segmentability\u2013\
  Compactness\u2013Spikiness space"
bibliography: references.bib
description: Maximize shape discriminability by selecting symbols separated along
  segmentability, compactness, and spikiness.
labels:
- chart:scatter
- task:identify
- visual:shape
- impact:clarity
- data:categorical
- audience:novice
- domain:dataviz
---

## Use large SCI separation for shape symbol sets <!-- role: advice -->

Choose shape symbols that are widely separated across segmentability, compactness, and spikiness so viewers can distinguish categories quickly in dense displays. Prefer sets that differ on more than one of these dimensions rather than small variations within the same dimension.

## Why SCI separation improves shape discriminability <!-- role: reason -->

When shapes differ along the primary preattentive dimensions extracted in parallel, the visual system can separate regions or groups without item-by-item inspection, improving discrimination in attention-demanding displays.

**Mechanism:** Greater distance in Segmentability–Compactness–Spikiness (SCI) feature space corresponds to higher perceptual discriminability between shapes in texture-based selection.

**Evidence:** Discriminability (d′) between 91 shape pairs in a masked texture segregation task was strongly predicted by log Euclidean distance in a three-dimensional SCI space (r = 0.974), indicating that separating shapes along SCI increases preattentive discriminability [@huangSpacePreattentiveShape2020].

**Notes:** SCI here is about preattentive shape features in attention-demanding selection, not detailed postattentive shape recognition.

## When SCI-based shape selection applies <!-- role: context -->

- **User Goal:** Identify which points/marks belong to which category using shape alone.
- **Task:** Rapid grouping/segmentation of intermixed marks by shape.
- **Data:** Categorical series with multiple groups shown simultaneously.
- **Chart Setting:** Dense plots (e.g., scatterplots) or any display where many marks appear at once.
- **Audience:** Mixed literacy audiences; viewers who benefit from fast, low-effort discrimination.
- **Success Criterion:** Fewer confusions between categories and faster visual separation of groups.

## When not to rely on SCI separation <!-- role: exceptions -->

**Break it when:** The task is a one-to-one careful comparison of two individual shapes rather than attention-demanding selection among many items. **Why:** SCI characterizes preattentive shape features that drive parallel extraction in tasks like texture segregation, not full postattentive shape processing.

## Tradeoffs and risks of maximizing SCI separation <!-- role: costs -->

**Sacrifice:** You may give up brand-specific or conventional symbol choices to get better discriminability. **Risk:** A maximally separated set may look stylistically inconsistent across symbols. **Mitigation:** Treat SCI separation as a constraint on symbol choice, then apply consistent stroke/size styling within that constraint.

## Common failures when choosing shape symbol sets <!-- role: mistakes -->

- **Mistake:** Choosing several symbols that are all compact and non-spiky (or all spiky but similarly segmentable). **Why it fails:** They cluster in SCI space and become hard to discriminate preattentively.
- **Mistake:** Using “many different” shapes that differ mainly by small contour tweaks. **Why it fails:** Small within-cluster variations do not add much SCI distance, so discriminability barely improves.

## Quick ways to check SCI separation <!-- role: check -->

**Failure Sign:** Viewers need to repeatedly look back at the legend because categories look interchangeable. **Quick Check:** Glance at the plot for about a tenth of a second and see if you can still separate categories by shape without reading the legend. **Stronger Test:** Run a brief in-house pilot where users must identify category membership in a dense mixed display, then compare confusion rates across symbol sets.

## What to do instead when shapes are too similar <!-- role: fix -->

- Use a smaller set of shapes that are more separated in SCI space rather than a larger set of subtly different shapes.
- Replace one or more symbols with shapes that differ strongly on segmentability (e.g., adding intersections/joints), compactness (e.g., introducing a hole/strong concavity), or spikiness (e.g., adding sharp outward spikes).
- If you must support many categories, switch some categories from shape to another channel rather than overloading shape with near-neighbors.
- Reduce mark density (filter, aggregate, or facet) so postattentive inspection is less necessary.
