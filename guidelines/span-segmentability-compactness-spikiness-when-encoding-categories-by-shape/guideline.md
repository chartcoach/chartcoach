---
id: span-segmentability-compactness-spikiness-when-encoding-categories-by-shape
title: Span Segmentability, Compactness, and Spikiness When Using Shape as a Channel
bibliography: references.bib
description: "Design or select shape encodings to vary across three preattentive dimensions\u2014\
  segmentability, compactness, spikiness\u2014rather than relying on a single notion\
  \ of shape difference."
labels:
- chart:scatter
- chart:dotplot
- task:distinguish
- visual:shape
- impact:clarity
- data:categorical
- audience:general
- model:sci-shape-space
- source:huang-2020
---

## The Rule <!-- role: advice -->

When encoding categories with shape, ensure your chosen shapes collectively vary on **all three** SCI dimensions: **segmentability** (joints/intersections), **compactness** (holes/concavities vs. convex fill), and **spikiness** (sharp outward spikes).

## The Logic <!-- role: reason -->

A large majority of variance in pairwise shape discriminability in an attention-demanding task is captured by a 3D SCI space (r ≈ 0.974). This implies that “shape difference” that matters preattentively is largely organized along these three axes; failing to vary along an axis leaves discriminability on the table.

- **The Principle:** Preattentive shape is low-dimensional (SCI) and distance-based.
- **The Evidence:** [@huangSpacePreattentiveShape2020]

## Where to Apply <!-- role: context -->

- **User Goal:** Rapidly segmenting/grouping items by category in cluttered or high-item-count views.
- **Data Type:** Many marks requiring parallel processing (arrays of points, dense scatterplots, symbol maps).
- **Audience:** General viewers and time-pressured analysts.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You only need 2 categories and can rely on a single strong SCI separation (e.g., hole vs. no-hole).
- **Reason:** With very few categories, spanning all three dimensions may be unnecessary overhead; one strong axis may suffice while keeping the design simpler [@huangSpacePreattentiveShape2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** A fully “matched” look (e.g., all rounded shapes) may be impossible if you must include spiky or highly segmented symbols.
- **The Risk:** Some chosen shapes may be harder to render cleanly at very small sizes.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Treating “intersection,” “closure,” and “line termination” as separate checkboxes without considering their unified roles (segmentability, compactness, spikiness).
- **Why it fails:** The paper argues these classic notions are better captured by broader SCI dimensions; optimizing for the wrong proxies can miss the real discriminability drivers [@huangSpacePreattentiveShape2020].

## How to Check <!-- role: check -->

- **Visual Sign:** Your palette feels diverse in name (“triangle vs. diamond vs. star”) but still confusable in rapid viewing.
- **The Test:** Map each symbol to an SCI intuition check:
  - Does it have joints/intersections (segmentability)?
  - Does it have a hole or strong concavity (compactness)?
  - Does it have sharp outward spikes (spikiness)?
    If most of your symbols answer “yes” to the same subset, you are not spanning SCI [@huangSpacePreattentiveShape2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Swap one symbol for one that introduces the missing property (add a holed symbol; add a clearly jointed symbol; add a sharply spiky symbol).
- **Best Fix:** Construct the full set by deliberately selecting representatives near different “corners” of SCI space (high vs. low on each axis), maximizing pairwise distances [@huangSpacePreattentiveShape2020].
