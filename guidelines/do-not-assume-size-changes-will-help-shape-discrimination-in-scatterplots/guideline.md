---
id: do-not-assume-size-changes-will-help-shape-discrimination-in-scatterplots
title: Do Not Rely on Size Differences to Improve Shape Discrimination
bibliography: references.bib
description: Varying mark size has only a small effect on how well viewers distinguish
  shapes in scatterplots, except at very small sizes.
labels:
- chart:scatter
- task:sort
- visual:shape
- visual:size
- impact:clarity
- data:categorical
- audience:general
- complexity:advanced
---

## The Rule <!-- role: advice -->

Do not expect changing mark size to meaningfully improve viewers’ ability to distinguish mark shapes in a scatterplot, except when marks are extremely small.

## The Logic <!-- role: reason -->

- **The Principle:** Asymmetric interference (size weakly affects shape perception)
- **The Evidence:** The paper reports that size has only a small effect on shape perception, with notable degradation primarily at the smallest tested sizes; overall, shape discrimination is robust to size compared to the strong effect of shape on size perception [@smartMeasuringSeparabilityShape2019]. This asymmetry is part of the collated graphical perception findings intended for visualization recommendation [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Sorting/distinguishing categories using shape in a scatterplot
- **Data Type:** Categorical classes mapped to shape (with quantitative x/y positioning)
- **Audience:** General audiences on standard displays

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your marks are extremely small and fine shape details are not reliably visible.
- **Reason:** The reported size effect on shape discrimination appears at the smallest tested sizes, consistent with shapes becoming difficult to render/detect [@smartMeasuringSeparabilityShape2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may need to change shapes (or reduce shape complexity) rather than adjusting size.
- **The Risk:** If you increase size too much to “help shapes,” you may create clutter or occlusion without substantially improving shape discrimination.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Making all marks larger to solve shape confusion.
- **Why it fails:** Size changes do not substantially change shape discriminability except at very small sizes; the main driver is the shape itself [@smartMeasuringSeparabilityShape2019].

## How to Check <!-- role: check -->

- **Visual Sign:** Even at larger mark sizes, users still misidentify which shape category a point belongs to.
- **The Test:** Increase mark size in steps; if confusion persists after marks are comfortably visible, changing size is not addressing the root issue [@smartMeasuringSeparabilityShape2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace confusing shapes with a smaller, more distinguishable subset while keeping size constant.
- **Best Fix:** Avoid using detailed shapes at very small sizes; redesign the encoding so shape discrimination is not dependent on tiny mark rendering (e.g., reduce reliance on subtle shape differences) [@smartMeasuringSeparabilityShape2019; @zengReviewCollationGraphical2023].
