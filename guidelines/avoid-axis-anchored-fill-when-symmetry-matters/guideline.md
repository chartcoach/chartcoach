---
id: avoid-axis-anchored-fill-when-symmetry-matters
title: Avoid Axis-Anchored Filled Shapes for Symmetric Quantities
bibliography: references.bib
description: Axis-anchored bars create an inside/outside asymmetry that biases how
  viewers judge symmetric deviations from a mean.
labels:
- chart:bar
- task:infer
- visual:shape
- impact:accuracy
- data:symmetric
- audience:general
- bias:within-the-bar
---

## The Rule <!-- role: advice -->

When communicating a symmetric quantity (like a mean), do not encode it using a shape that creates an “inside” region anchored to one axis.

## The Logic <!-- role: reason -->

A mean is symmetric with respect to equal deviations above and below. A bar anchored to one axis is not symmetric: it creates a bounded region on one side of the mean. Viewers then treat the bounded region as more probable/representative, producing asymmetric judgments about equally distant values.

- **The Principle:** Graphical asymmetry induces cognitive asymmetry through object perception and boundary effects.
- **The Evidence:** Viewers rated equidistant values as more likely when the value fell within the bar, including in designs centered at zero with equally extreme numeric labels [@newmanBarGraphsDepicting2012].

## Where to Apply <!-- role: context -->

- **User Goal:** Reasoning symmetrically about deviations around a central value.
- **Data Type:** Mean-centered or zero-centered quantities where both directions are meaningful (positive/negative, above/below mean).
- **Audience:** Mixed audiences; the bias was observed across multiple participant populations [@newmanBarGraphsDepicting2012].

## When to Break It <!-- role: exceptions -->

- **Scenario:** The underlying construct is inherently one-sided from a meaningful baseline (so “inside the bar” is intended to be special).
- **Reason:** The demonstrated problem is that the bar’s bounded region becomes special even when it should not be; if it *should* be special, the asymmetry may be acceptable [@newmanBarGraphsDepicting2012].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may lose the convenience of standard bar-chart defaults in tools/templates.
- **The Risk:** Designers may reintroduce asymmetry by adding filled regions that again create a “contained” side of the mean [@newmanBarGraphsDepicting2012].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Flipping the bar to descend from the top (instead of rising from the bottom) and assuming that removes the issue.
- **Why it fails:** The within-the-bar bias occurred for both rising and falling bars; reversing the direction just reverses which values are judged “more likely” [@newmanBarGraphsDepicting2012].

## How to Check <!-- role: check -->

- **Visual Sign:** The mean is the edge of a filled region that exists only on one side.
- **The Test:** Imagine two candidate values equally distant from the mean on opposite sides; if one lies in the filled region and the other does not, your encoding invites the bias [@newmanBarGraphsDepicting2012].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace the filled region with an unfilled mark at the mean (e.g., a point).
- **Best Fix:** Use a symmetric depiction of central tendency that does not create an “inside vs. outside” boundary around one side of the mean [@newmanBarGraphsDepicting2012].
