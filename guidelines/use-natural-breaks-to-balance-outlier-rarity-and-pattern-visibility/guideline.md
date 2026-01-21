---
id: use-natural-breaks-to-balance-outlier-rarity-and-pattern-visibility
title: Use Natural Breaks to Reflect Clusters and Outliers
bibliography: references.bib
description: "Select Natural breaks (Jenks) to create classes that follow the data\u2019\
  s clustering, showing variation among common values while keeping outliers distinct."
labels:
- chart:choropleth
- task:reveal-patterns
- visual:color
- impact:balance
- data:quantitative
- audience:general
- complexity:intermediate
- source:datawrapper-blog
---

## The Rule <!-- role: advice -->

Use Natural breaks (Jenks) when your distribution has clusters and outliers and you need a compromise: clear variation among typical values while keeping the darkest class reserved for true outliers. [@muth_interpolation_2022]

## The Logic <!-- role: reason -->

Natural breaks form groups where values within each group are as close together as possible, so dense clusters get broader groups and sparse outlier ranges get narrower groups—preserving the “rarity” signal of extremes while improving within-cluster differentiation. [@muth_interpolation_2022]

- **The Principle:** Cluster-preserving classification
- **The Evidence:** [@muth_interpolation_2022]

## Where to Apply <!-- role: context -->

- **User Goal:** Seeing regional differences in the main mass of the data without pretending outliers are common
- **Data Type:** Quantitative data with uneven distribution and visible clustering in a histogram
- **Audience:** Readers who need both interpretability and a defensible link between bins and the data’s structure [@muth_interpolation_2022]

## When to Break It <!-- role: exceptions -->

- **Scenario:** You need simple, predictable cut points (e.g., evenly spaced thresholds) for policy or reporting consistency.
- **Reason:** Natural breaks can produce non-round, harder-to-read class boundaries. [@muth_interpolation_2022]

## The Price <!-- role: costs -->

- **The Sacrifice:** Less “nice” legend numbers; breakpoints may look arbitrary to readers.
- **The Risk:** If the legend numbers are awkward, readers may struggle to interpret thresholds quickly. [@muth_interpolation_2022]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Accepting Natural breaks but leaving hard-to-read break values in the legend.
- **Why it fails:** The classification may be good, but comprehension suffers if users can’t parse the thresholds. [@muth_interpolation_2022]

## How to Check <!-- role: check -->

- **Visual Sign:** The map shows more mid-range variation than linear, and only a few regions occupy the darkest color—but legend breaks are “ugly” (e.g., 4.1, 5.7, 7.9).
- **The Test:** Read the legend out loud; if breakpoints are difficult to communicate, you likely need rounding or custom steps. [@muth_interpolation_2022]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Move from Natural breaks to a Custom interpolation that rounds the Natural breakpoints to readable numbers with minimal visual change. [@muth_interpolation_2022]
- **Best Fix:** Keep Natural as the analytical basis, then define custom, readable thresholds that preserve the same overall grouping logic and map impression. [@muth_interpolation_2022]
