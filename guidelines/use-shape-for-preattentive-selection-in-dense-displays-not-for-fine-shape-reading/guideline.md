---
id: use-shape-for-preattentive-selection-in-dense-displays-not-for-fine-shape-reading
title: Use Shape for Preattentive Category Selection in Dense Displays
bibliography: references.bib
description: Rely on shape primarily to support fast, parallel selection and segregation
  of groups, consistent with preattentive processing.
labels:
- chart:scatter
- chart:matrix
- task:filter
- visual:shape
- impact:clarity
- data:categorical
- audience:general
- complexity:intermediate
- source:huang-2020
---

## The Rule <!-- role: advice -->

Use shape encodings to help viewers **preattentively segregate** groups in dense views, and avoid designs that require viewers to **inspect and compare detailed shape geometry** item-by-item.

## The Logic <!-- role: reason -->

The SCI findings are built from an attention-demanding texture segregation task designed to measure what can be extracted in parallel as preattentive shape features, not what requires focused, postattentive inspection. Shape advantages are substantial in attention-demanding tasks but not necessarily in one-to-one comparison tasks, so shape should be deployed where parallel segregation is the bottleneck.

- **The Principle:** Preattentive shape features support parallel selection; detailed shape understanding is postattentive.
- **The Evidence:** [@huangSpacePreattentiveShape2020]

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly finding/segmenting a subset of points by category.
- **Data Type:** Many marks on screen at once (high density), where parallel processing matters.
- **Audience:** Any audience; especially useful when viewers must scan rather than read.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The visualization’s core task is deliberate identification of specific icons (e.g., a legend-like symbol dictionary that viewers must learn and read precisely).
- **Reason:** That task is closer to postattentive shape processing, where the SCI-based preattentive advantages may be reduced [@huangSpacePreattentiveShape2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** Some semantic/iconic symbol systems (rich pictograms) may be inappropriate if they demand careful reading.
- **The Risk:** Overcomplicating shapes can slow recognition if viewers must identify exact icons rather than segregate groups.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Encoding many categories with subtly different “decorative” icons and assuming viewers will separate them quickly.
- **Why it fails:** Preattentive discriminability is governed largely by SCI distances; subtle stylistic changes may not move symbols far in that space [@huangSpacePreattentiveShape2020].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers can’t quickly isolate a group without repeatedly consulting the legend or focusing on individual marks.
- **The Test:** If a viewer must “read” each marker to know the category, the encoding is operating postattentively rather than preattentively [@huangSpacePreattentiveShape2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce the number of categories encoded by shape and increase separability by swapping in symbols that differ strongly on SCI dimensions.
- **Best Fix:** Redesign the encoding so categories form separable preattentive groups (high SCI distances) and the viewer’s main effort shifts to interpreting the data, not decoding the symbols [@huangSpacePreattentiveShape2020].
