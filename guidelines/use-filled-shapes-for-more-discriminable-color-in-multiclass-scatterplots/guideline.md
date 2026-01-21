---
id: use-filled-shapes-for-more-discriminable-color-in-multiclass-scatterplots
title: Use Filled Shapes to Improve Color Discriminability
bibliography: references.bib
description: In multiclass scatterplots, use filled mark shapes to make color differences
  easier to perceive.
labels:
- chart:scatter
- task:sort
- visual:color
- visual:shape
- impact:clarity
- data:categorical
- audience:general
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

Use filled mark shapes (rather than unfilled outlines) when you rely on color differences to distinguish categories in a scatterplot.

## The Logic <!-- role: reason -->

- **The Principle:** Visual channel interference (shape affects color discriminability)
- **The Evidence:** In a scatterplot context, mark shape changes how easily viewers detect color differences; filled shapes support higher color discriminability than unfilled counterparts [@smartMeasuringSeparabilityShape2019]. This guideline is included as perception knowledge for recommendation in the collation dataset [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Sorting/visually separating groups by color in a multiclass scatterplot
- **Data Type:** Quantitative x/y positions with a nominal (categorical) grouping encoded by color
- **Audience:** General audiences using common screens

## When to Break It <!-- role: exceptions -->

- **Scenario:** You cannot use filled marks because overlapping points must remain visible.
- **Reason:** Filled marks can occlude one another, reducing visibility of dense regions; the rule targets color discriminability, not overplotting behavior [@smartMeasuringSeparabilityShape2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** Potentially worse readability under overplotting (filled marks can cover points behind them).
- **The Risk:** Dense clusters may look like solid blobs, making individual points harder to distinguish.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Switching to unfilled outlines to “reduce clutter” while still expecting color to separate classes.
- **Why it fails:** Unfilled shapes reduce color discriminability, making category separation by color harder [@smartMeasuringSeparabilityShape2019].

## How to Check <!-- role: check -->

- **Visual Sign:** Colors look “less different” across categories when marks are outlines, especially at smaller mark sizes.
- **The Test:** Flip your marks from filled to unfilled (or vice versa) and see whether you can still quickly sort/segment by color at a glance; if not, your shape choice is likely undermining color [@smartMeasuringSeparabilityShape2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Change outline-only symbols to filled symbols for the same set of categories.
- **Best Fix:** Redesign the categorical encoding so the class-distinguishing color is paired with filled shapes consistently across the plot (rather than mixing filled and unfilled styles), to avoid shape-driven shifts in color discriminability [@smartMeasuringSeparabilityShape2019; @zengReviewCollationGraphical2023].
