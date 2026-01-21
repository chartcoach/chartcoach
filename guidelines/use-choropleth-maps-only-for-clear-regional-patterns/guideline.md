---
id: use-choropleth-maps-only-for-clear-regional-patterns
title: Use Choropleth Maps Only for Clear Regional Patterns
bibliography: references.bib
description: Use choropleth maps when the story is geographic patterns or local context,
  not when geography is incidental.
labels:
- chart:choropleth
- task:discover
- visual:color
- impact:clarity
- data:geospatial
- audience:general
- source:datawrapper
---

## The Rule <!-- role: advice -->

Use a choropleth map only when your data has a meaningful regional pattern (or when local geography itself is the point for your readers); otherwise, choose a non-map chart type.

## The Logic <!-- role: reason -->

Explain geography only when geography explains something: choropleths are good at revealing spatial clusters and contrasts, but weak when geography adds no structure to the message, making the display feel arbitrary or decorative. This is the decision principle emphasized in the choropleth guidance by Muth [@muth_choroplethmaps_2018].

- **The Principle:** Map only when location is explanatory
- **The Evidence:** [@muth_choroplethmaps_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Spot regional clusters, neighboring-area contrasts, or “where is this high/low?” patterns
- **Data Type:** One variable (or a derived single variable like a year-over-year change) indexed to regions
- **Audience:** Readers who recognize the mapped area or benefit from locating themselves

## When to Break It <!-- role: exceptions -->

- **Scenario:** The goal is to show correlation between two variables
- **Reason:** Choropleths are not the best choice for showing correlations; use a dotplot or scatterplot instead [@muth_choroplethmaps_2018].
- **Scenario:** The data shows no clear regional pattern
- **Reason:** A different chart type will communicate the message more directly [@muth_choroplethmaps_2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may lose the “reader looks for their place” engagement benefit if you switch away from maps.
- **The Risk:** Keeping a choropleth when geography isn’t informative can bury the point and make comparisons feel vague [@muth_choroplethmaps_2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Mapping data just because it’s available by region
- **Why it fails:** It produces a map without a geographic story, so readers learn little beyond “things are somewhere” [@muth_choroplethmaps_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** The map shows scattered, patternless coloring or no interpretable clusters.
- **The Test:** Ask: “If I shuffled the values across regions, would the takeaway change?” If not, geography isn’t doing work [@muth_choroplethmaps_2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** State the takeaway in text and reduce emphasis on the map if geography is secondary.
- **Best Fix:** Replace the map with a chart suited to the task (e.g., dotplot/scatterplot for relationships) [@muth_choroplethmaps_2018].
