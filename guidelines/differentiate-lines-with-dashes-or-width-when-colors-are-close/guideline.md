---
id: differentiate-lines-with-dashes-or-width-when-colors-are-close
title: Differentiate Lines with Dashes or Width, Not Just Color
bibliography: references.bib
description: In line charts with similar colors, use different dash styles or line
  widths so overlapping series remain separable for colorblind readers.
labels:
- chart:line
- task:compare
- visual:line-style
- visual:color
- impact:accessibility
- data:temporal
- audience:general
- source:datawrapper
---

## The Rule <!-- role: advice -->

If line colors are similar (especially when lines overlap), differentiate series with distinct dash patterns and/or line widths.

## The Logic <!-- role: reason -->

When hues converge for colorblind readers, line style remains a readable cue; dashes and width differences prevent confusion where series overlap in time [@muth_colorblindness_2020].

- **The Principle:** Use line texture/weight as a redundant categorical channel
- **The Evidence:** The post shows two similarly bright lines (gold vs. bitcoin) becoming confusing when overlapping and fixes it by dotting one line; it notes width changes as an alternative [@muth_colorblindness_2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Track and compare multiple time series accurately, including at intersections/overlaps
- **Data Type:** Temporal series with two or more lines
- **Audience:** Broad audiences, including colorblind readers [@muth_colorblindness_2020]

## When to Break It <!-- role: exceptions -->

- **Scenario:** Many series (e.g., 8–12 lines) where multiple dash patterns become hard to distinguish
- **Reason:** Too many styles reduce clarity; you may need fewer series, highlighting, or direct labels [@muth_colorblindness_2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** Visual elegance; dashes can look busy
- **The Risk:** Dash patterns can become hard to see at small sizes or low resolution [@muth_colorblindness_2020].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping similar colors and hoping the legend resolves ambiguity
- **Why it fails:** The viewer cannot reliably follow a series through overlaps if the mark itself is indistinct [@muth_colorblindness_2020].

## How to Check <!-- role: check -->

- **Visual Sign:** You lose track of which line is which during overlaps
- **The Test:** View under a colorblind simulation and specifically inspect crossover periods; verify each line remains trackable [@muth_colorblindness_2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Apply a dotted/dashed style to one of the confusing lines
- **Best Fix:** Combine line style differences with direct end-of-line labels and reduce reliance on a legend [@muth_colorblindness_2020].
