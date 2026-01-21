---
id: use-distinct-point-shapes-in-scatterplots-and-limit-the-set
title: Use a Small Set of Distinct Point Shapes
bibliography: references.bib
description: In scatterplots, differentiate groups with shapes (not just color) and
  keep the number of shapes to a manageable few.
labels:
- chart:scatter
- task:group
- visual:shape
- impact:accessibility
- data:categorical
- audience:general
- source:datawrapper
---

## The Rule <!-- role: advice -->

In scatterplots, encode group membership with different point shapes as well as (or instead of) color, and limit yourself to about three or four shapes.

## The Logic <!-- role: reason -->

Shape is a non-color channel that remains readable under color vision deficiencies; limiting the variety prevents the plot from becoming visually noisy and hard to parse [@muth_colorblindness_2020].

- **The Principle:** Substitute/augment hue with form while controlling visual noise
- **The Evidence:** The post recommends using different shapes (triangles, crosses, stars, etc.) for scatterplots but warns that too many shapes “quickly looks like confetti,” advising to limit to three or four [@muth_colorblindness_2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Distinguish clusters/groups of points
- **Data Type:** Two quantitative axes with a categorical grouping variable
- **Audience:** General audiences, including colorblind readers [@muth_colorblindness_2020]

## When to Break It <!-- role: exceptions -->

- **Scenario:** Very high point density where shape differences are not visible
- **Reason:** Overplotting makes shapes indistinguishable; another strategy (e.g., fewer groups, faceting) is needed [@muth_colorblindness_2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** Limited number of groups you can show distinctly in one panel
- **The Risk:** Too many shapes reduces readability and can overwhelm the viewer [@muth_colorblindness_2020].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assigning a unique shape to every category in a long legend
- **Why it fails:** The plot becomes “confetti,” slowing interpretation and increasing error [@muth_colorblindness_2020].

## How to Check <!-- role: check -->

- **Visual Sign:** The scatterplot looks busy and shapes are hard to recognize at normal viewing distance
- **The Test:** Step back (or zoom out) and see if you can still separate groups by shape without color [@muth_colorblindness_2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce the number of categories shown and reuse a small, distinct set of shapes
- **Best Fix:** Split into small multiples or other layouts that reduce simultaneous group decoding demands [@muth_colorblindness_2020].
