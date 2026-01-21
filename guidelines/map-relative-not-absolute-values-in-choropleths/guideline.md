---
id: map-relative-not-absolute-values-in-choropleths
title: Map Relative Values, Not Absolute Counts
bibliography: references.bib
description: Use choropleths for normalized/relative measures so regions are comparable.
labels:
- chart:choropleth
- task:compare
- visual:color
- impact:honesty
- data:geospatial
- audience:general
- data:quantitative
---

## The Rule <!-- role: advice -->

Use choropleth maps for relative/normalized metrics (rates, percentages), not raw totals.

## The Logic <!-- role: reason -->

Regions differ in population/size, so mapping absolute counts confounds the message; normalization makes region-to-region comparison meaningful. Muth notes unemployment counts aren’t comparable without population, while unemployment rate is [@muth_choroplethmaps_2018].

- **The Principle:** Comparability through normalization
- **The Evidence:** [@muth_choroplethmaps_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Compare intensity or prevalence across regions
- **Data Type:** Counts that can be converted to rates (per capita, percent)
- **Audience:** General audiences who may not adjust mentally for population

## When to Break It <!-- role: exceptions -->

- **Scenario:** You truly want to show where the absolute magnitude is largest
- **Reason:** Then use a symbol map; note it will often answer “Where do most people live?” rather than the intended phenomenon [@muth_choroplethmaps_2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Rates can hide total burden (many affected people) in populous places.
- **The Risk:** Readers may misinterpret a high rate in a small-population region as “more people” without additional context [@muth_choroplethmaps_2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Mapping raw counts and implying fairness of comparison
- **Why it fails:** It reflects population distribution as much as the phenomenon [@muth_choroplethmaps_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Large-population or large-area regions dominate the story without justification.
- **The Test:** Ask: “Would this map change drastically if every region had the same population?” If yes, consider rate normalization [@muth_choroplethmaps_2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Convert counts to a rate/percentage and map that [@muth_choroplethmaps_2018].
- **Best Fix:** If absolute totals are essential, use a symbol map (and explain what question it actually answers) [@muth_choroplethmaps_2018].
