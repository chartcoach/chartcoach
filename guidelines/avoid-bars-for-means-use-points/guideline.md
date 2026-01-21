---
id: avoid-bars-for-means-use-points
title: Represent Means With Points, Not Full Bars
bibliography: references.bib
description: Avoid bar charts for means because viewers overestimate the likelihood
  of values that fall within the bar area.
labels:
- chart:bar
- chart:point
- task:estimate
- visual:area
- impact:accuracy
- data:distribution
- audience:general
- bias:within-the-bar
---

## The Rule <!-- role: advice -->

Represent means as points (or another symmetric mark), not as bars anchored to an axis.

## The Logic <!-- role: reason -->

Bar charts depict a mean asymmetrically (as the end of a filled object extending from an axis). Viewers then treat the bar like an object that “contains” plausible data and judge values *inside* the bar as more likely than equally distant values *outside* the bar.

- **The Principle:** Object-based attention and boundary-defined “containment” biases likelihood judgments.
- **The Evidence:** Across multiple experiments, participants rated equidistant test values as more likely when they fell within the displayed bar than when they fell outside it [@newmanBarGraphsDepicting2012].

## Where to Apply <!-- role: context -->

- **User Goal:** Estimating what values are plausible in the underlying distribution around a mean.
- **Data Type:** Averages/means summarizing a distribution (especially when you care about variation above and below the mean).
- **Audience:** General audiences and non-specialists (the effect was found across students and adult samples) [@newmanBarGraphsDepicting2012].

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are not showing a mean but an inherently axis-anchored quantity (e.g., a count or other inherently asymmetric-from-zero quantity).
- **Reason:** The paper’s demonstrated misinterpretation is specifically about bars used to depict *central tendency*; the “containment” implication is less problematic when “filled extent from an axis” is the actual intended meaning [@newmanBarGraphsDepicting2012].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less immediate “mass”/presence compared to filled bars; points can feel visually lighter.
- **The Risk:** Some audiences may be less familiar with point-only summaries and ask “where is the bar?” even though comprehension may improve [@newmanBarGraphsDepicting2012].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding error bars to a mean bar and assuming it prevents misinterpretation.
- **Why it fails:** The within-the-bar bias was observed even when bars included bidirectional error bars [@newmanBarGraphsDepicting2012].

## How to Check <!-- role: check -->

- **Visual Sign:** The mean is shown as the endpoint of a filled rectangle anchored to a baseline.
- **The Test:** Ask a viewer whether a value equally far above and below the mean seems equally likely; if they favor the one “inside the bar,” you’ve triggered the bias [@newmanBarGraphsDepicting2012].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace the bar with a single point at the mean (keeping the same axes and labels).
- **Best Fix:** Use a display that does not create an “inside the bar” region for a mean (i.e., a symmetric mean mark rather than an axis-anchored filled object) [@newmanBarGraphsDepicting2012].
