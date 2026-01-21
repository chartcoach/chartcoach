---
id: normalize-values-in-choropleth-maps
title: Normalize Values Before Coloring a Choropleth Map
bibliography: references.bib
description: Use normalized (rate/density) values rather than raw totals when shading
  regions in a choropleth.
labels:
- chart:choropleth
- task:compare
- visual:color
- impact:correctness
- data:geospatial
- audience:novice
- complexity:foundational
---

## The Rule <!-- role: advice -->

In a choropleth map, color regions using normalized values (rates/densities), not raw totals.

## The Logic <!-- role: reason -->

Choropleths shade geographic areas; using raw totals confounds the intended meaning and can mislead, while normalization produces a more meaningful “density map.”

- **The Principle:** Avoid misleading magnitude encodings by matching measurement to area-based display
- **The Evidence:** [@heerTourVisualizationZoo2010]

## Where to Apply <!-- role: context -->

- **User Goal:** Compare prevalence or intensity across regions (e.g., percent obese by state)
- **Data Type:** Region-aggregated data (states, counties, countries)
- **Audience:** General public and policymakers

## When to Break It <!-- role: exceptions -->

- **Scenario:** The explicit goal is to show total counts by region regardless of population/area
- **Reason:** Then the map is about totals, not prevalence; consider alternative encodings to avoid area confounds [@heerTourVisualizationZoo2010]

## The Price <!-- role: costs -->

- **The Sacrifice:** Hides absolute totals that might matter for resource planning
- **The Risk:** Viewers may assume totals if the normalization unit isn’t stated

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Shading by population (or other raw totals) because “that’s what we have”
- **Why it fails:** It produces misleading interpretations in an area-shaded map [@heerTourVisualizationZoo2010]

## How to Check <!-- role: check -->

- **Visual Sign:** Large regions appear “important” despite low rate, or small regions disappear despite high rate
- **The Test:** Inspect whether the legend is a rate (%, per-capita) vs a raw count; if it’s a raw count, reconsider [@heerTourVisualizationZoo2010]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Convert totals to rates (per-capita, percentage) before mapping
- **Best Fix:** If totals must be shown, switch to a symbol-based map or cartogram designed for totals [@heerTourVisualizationZoo2010]
