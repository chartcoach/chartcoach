---
id: demonstrate-summary-stats-can-hide-structure-with-same-stats-different-graphs
title: Show Multiple Graphs When Summary Statistics Match
bibliography: references.bib
description: Use multiple visually distinct plots that share the same summary statistics
  to demonstrate why visualization is necessary.
labels:
- chart:scatter
- task:educate
- visual:position
- impact:trust
- data:bivariate
- audience:novice
- source:matejka-fitzmaurice-2017
---

## The Rule <!-- role: advice -->

Show multiple graphs that share identical summary statistics to illustrate that the same stats can imply very different data shapes.

## The Logic <!-- role: reason -->

- **The Principle:** Summary statistics are not shape-identifying; different point configurations can preserve means/spreads/correlation while changing visual structure.
- **The Evidence:** The paper presents many datasets that match the same mean, standard deviation, and correlation to two decimals while producing markedly different scatterplots [@matejkaSameStatsDifferent2017].

## Where to Apply <!-- role: context -->

- **User Goal:** Learn why “looking at the data” matters beyond computing summary statistics.
- **Data Type:** 2D point data summarized by a small set of aggregate metrics (e.g., mean, SD, correlation).
- **Audience:** Students, analysts-in-training, or stakeholders who over-trust summary numbers.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The task is purely to verify numeric reproducibility of the reported statistics.
- **Reason:** Multiple alternative plots may distract from the numeric-validation goal.

## The Price <!-- role: costs -->

- **The Sacrifice:** More space and cognitive load (multiple panels rather than one plot).
- **The Risk:** Viewers may misinterpret the exercise as “statistics are useless” rather than “statistics are incomplete.”

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Showing alternative datasets that look like random noise without clear visual structure.
- **Why it fails:** Unstructured alternatives are less effective at demonstrating meaningful differences in underlying patterns [@matejkaSameStatsDifferent2017].

## How to Check <!-- role: check -->

- **Visual Sign:** The alternative plots look indistinct or “samey,” even if they are technically different.
- **The Test:** Ask a viewer to describe the pattern in each panel; if they can’t articulate distinct structures, the demonstration is weak.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Choose target patterns with clearly recognizable shapes (e.g., lines, curves, clusters).
- **Best Fix:** Generate a curated set of datasets that preserve the same chosen statistics while being directed toward distinctly interpretable shapes [@matejkaSameStatsDifferent2017].
