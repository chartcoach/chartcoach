---
id: use-choropleths-for-big-picture-not-precise-or-subtle-comparisons
title: Use Choropleths for Big Patterns, Not Precise Comparisons
bibliography: references.bib
description: Choropleths are for spotting broad geographic patterns, not reading fine-grained
  numeric differences.
labels:
- chart:choropleth
- task:explore
- visual:color
- impact:clarity
- data:geospatial
- audience:general
- task:compare
---

## The Rule <!-- role: advice -->

Use choropleth maps to show broad regional patterns; do not rely on them to communicate subtle or precise differences between regions.

## The Logic <!-- role: reason -->

Small color differences are hard to perceive, and classed color intervals can distort how numeric differences feel; choropleths therefore support pattern recognition more than exact comparison. Muth cautions they’re “great to see the big picture, but not for subtle differences” and suggests tables/text when numeric differences are the point [@muth_choroplethmaps_2018].

- **The Principle:** Limited precision of color-based comparison
- **The Evidence:** [@muth_choroplethmaps_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Identify hotspots/coldspots, clusters, urban–rural contrasts
- **Data Type:** Region-level measures where approximate magnitude is sufficient
- **Audience:** General readers scanning rather than measuring

## When to Break It <!-- role: exceptions -->

- **Scenario:** You need readers to understand exact values or small differences
- **Reason:** Use a different chart type, a table, or text to communicate numeric differences clearly [@muth_choroplethmaps_2018].
- **Scenario:** Your key regions are too small to see on the map
- **Reason:** The map will hide what matters most; use another form of display [@muth_choroplethmaps_2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** You give up precision and straightforward rank/interval comparisons.
- **The Risk:** Readers may infer false magnitude differences from class boundaries or similar shades [@muth_choroplethmaps_2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Treating the choropleth like a table of values
- **Why it fails:** Colors don’t support fine measurement; similar shades look alike and discrete bins can mislead [@muth_choroplethmaps_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** You find yourself explaining exact numbers in the legend or paragraph because the map can’t carry them.
- **The Test:** Ask a colleague to estimate which of two similar-shaded regions is higher without tooltips; if they can’t, the map isn’t fit for precise comparison [@muth_choroplethmaps_2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add tooltips to provide exact values on demand [@muth_choroplethmaps_2018].
- **Best Fix:** Replace or complement the map with a table/text (or another chart type) when precise differences matter [@muth_choroplethmaps_2018].
