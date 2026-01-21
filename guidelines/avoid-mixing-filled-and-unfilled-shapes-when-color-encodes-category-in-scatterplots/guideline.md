---
id: avoid-mixing-filled-and-unfilled-shapes-when-color-encodes-category-in-scatterplots
title: Avoid Mixing Filled and Unfilled Shapes When Color Encodes Category
bibliography: references.bib
description: Do not mix filled and unfilled mark styles if you need color to be equally
  readable across categories in a scatterplot.
labels:
- chart:scatter
- task:sort
- visual:color
- visual:shape
- impact:fairness
- data:categorical
- audience:general
- complexity:advanced
---

## The Rule <!-- role: advice -->

Do not mix filled and unfilled mark shapes across categories when color hue is used to distinguish classes in a scatterplot.

## The Logic <!-- role: reason -->

- **The Principle:** Asymmetric separability (shape strongly influences color perception)
- **The Evidence:** Shape influences how discriminable colors are; filled vs. unfilled shapes differ in color difference perception, meaning categories rendered with different shape “styles” can end up with unequal color readability [@smartMeasuringSeparabilityShape2019]. This type of encoding-interaction knowledge is explicitly collated for visualization recommendation use cases [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Sorting or separating points into categories using color (and potentially also using shape to distinguish groups)
- **Data Type:** Multiclass scatterplots where color hue encodes nominal groups
- **Audience:** General audiences (including non-experts), especially when quick visual separation matters

## When to Break It <!-- role: exceptions -->

- **Scenario:** You intentionally want certain categories to be more visually prominent than others.
- **Reason:** Mixing filled/unfilled can act like an unintended emphasis cue by changing color discriminability for some categories [@smartMeasuringSeparabilityShape2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** Reduced flexibility in styling categories (fewer distinct “looks” if you enforce a consistent filled/unfilled policy).
- **The Risk:** If you keep everything filled, overplotting can become harder to interpret in dense regions.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Treating fill vs. outline as a purely aesthetic choice while relying on color to do the categorical work.
- **Why it fails:** The paper reports that shape affects color difference perception; different shape styles can make some colors effectively harder to distinguish than others [@smartMeasuringSeparabilityShape2019].

## How to Check <!-- role: check -->

- **Visual Sign:** Some categories feel easier to separate by color than others, even when the palette is consistent.
- **The Test:** Temporarily standardize all categories to the same shape style (all filled or all unfilled) and see if category separability by color becomes more uniform [@smartMeasuringSeparabilityShape2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Standardize categories to all-filled or all-unfilled marks.
- **Best Fix:** If you must use both color and shape, keep shape styles consistent (e.g., all filled geometries) and vary only the geometric form (circle/triangle/square) rather than mixing fill states, to reduce shape-driven differences in color discriminability [@smartMeasuringSeparabilityShape2019; @zengReviewCollationGraphical2023].
