---
id: prioritize-data-variation-over-design-variation-in-recommendation-galleries
title: Prioritize Data Variation Over Design Variation
bibliography: references.bib
description: Show many different variable subsets and transformations before showing
  multiple encodings of the same data.
labels:
- chart:small-multiples
- task:explore
- visual:faceting
- impact:coverage
- data:multivariate
- audience:analyst
- system:recommendation
---

## The Rule <!-- role: advice -->

In a visualization recommendation gallery, show different variable selections and transformations first; show alternate encodings only on demand.

## The Logic <!-- role: reason -->

Prioritizing data variation supports breadth-oriented exploration and helps users cover more of an unfamiliar dataset rather than fixating on a single view design. Voyager is explicitly designed around this principle and found to increase exposure to and interaction with more unique variable sets in a user study [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

- **The Principle:** Breadth-first exploration via dataset coverage
- **The Evidence:** [@wongsuphasawatVoyagerExploratoryAnalysis2016a]

## Where to Apply <!-- role: context -->

- **User Goal:** Get an overview; discover potentially relevant variables and relationships in unfamiliar data
- **Data Type:** Multivariate tabular data with many fields
- **Audience:** Analysts doing early-stage exploratory analysis

## When to Break It <!-- role: exceptions -->

- **Scenario:** The user is already focused on a specific question and needs the “best” encoding for a fixed variable set.
- **Reason:** Depth-first question answering benefits from direct control and iterative encoding refinement rather than browsing many variable combinations [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Fewer immediate encoding alternatives for any one data subset.
- **The Risk:** Users may feel the system is “cumbersome for specific tasks” if they can’t quickly fine-tune one chart [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Filling the gallery with many stylistic variants (e.g., color/shape swaps) of the same variable set.
- **Why it fails:** It consumes space and attention without increasing dataset coverage, counter to the goal of breadth-oriented exploration [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## How to Check <!-- role: check -->

- **Visual Sign:** Many adjacent thumbnails look like the same chart with minor encoding changes.
- **The Test:** Count unique variable sets represented in the first screen of recommendations; if it’s low relative to the number of views, you’re over-emphasizing design variation.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Cluster visually similar encodings and show only the top-ranked exemplar per underlying data table.
- **Best Fix:** Put encoding alternatives in an “expand” or drill-down view so the main gallery remains dominated by distinct variable subsets and transformations [@wongsuphasawatVoyagerExploratoryAnalysis2016a].
