---
id: use-splom-for-pairwise-multivariate-relationships
title: Use a Scatterplot Matrix to Inspect Pairwise Correlations
bibliography: references.bib
description: Use a SPLOM to examine correlations and patterns across multiple variables
  via pairwise scatterplots.
labels:
- chart:splom
- task:find-correlation
- visual:position
- impact:insight
- data:multivariate
- audience:analyst
- complexity:intermediate
---

## The Rule <!-- role: advice -->

When you need to inspect relationships among many variables, use a scatterplot matrix (SPLOM) of pairwise plots.

## The Logic <!-- role: reason -->

Multivariate data is hard to mentally visualize beyond three dimensions; a SPLOM decomposes the problem into multiple two-dimensional views so correlations between any pair can be visually inspected.

- **The Principle:** Reduce multivariate complexity via systematic pairwise projections
- **The Evidence:** [@heerTourVisualizationZoo2010]

## Where to Apply <!-- role: context -->

- **User Goal:** Detect correlations, clusters, and anomalies between variable pairs
- **Data Type:** Multivariate tables (many quantitative attributes)
- **Audience:** Analysts performing exploratory analysis

## When to Break It <!-- role: exceptions -->

- **Scenario:** You have many variables such that the matrix becomes too large to scan
- **Reason:** The number of pairwise plots grows quickly, reducing usability [@heerTourVisualizationZoo2010]

## The Price <!-- role: costs -->

- **The Sacrifice:** Space and scanning effort
- **The Risk:** Viewers miss patterns if the grid is too dense

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Trying to encode many dimensions in one scatterplot using many aesthetics
- **Why it fails:** The underlying issue is dimensionality; SPLOM addresses it by decomposition [@heerTourVisualizationZoo2010]

## How to Check <!-- role: check -->

- **Visual Sign:** You keep asking “How does X relate to Y?” for multiple pairs
- **The Test:** Count the number of pairwise questions; if it’s many, SPLOM fits [@heerTourVisualizationZoo2010]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Build a SPLOM for the key variables only
- **Best Fix:** Add brushing-and-linking so selections in one plot highlight corresponding points across all plots [@heerTourVisualizationZoo2010]
