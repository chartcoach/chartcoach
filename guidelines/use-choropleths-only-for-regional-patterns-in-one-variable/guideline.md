---
id: use-choropleths-only-for-regional-patterns-in-one-variable
title: Use choropleth maps only to show clear regional patterns in a single variable
bibliography: references.bib
description: Choropleths are best for big-picture geographic patterns in one variable,
  not for correlations or fine-grained numeric comparison.
labels:
- chart:choropleth
- task:discover
- visual:color
- impact:clarity
- data:geospatial
- audience:general
- complexity:foundational
---

## Use choropleths for one-variable geographic patterns, not multi-variable analysis <!-- role: advice -->

Use a choropleth map when you need to reveal a clear geographic pattern or communicate local variation in one variable. If your goal is to show correlations or subtle numeric differences, choose another chart type instead.

## Choropleths support pattern-seeking more than precise comparison <!-- role: reason -->

Choropleths encode values as filled areas, which encourages viewers to scan for spatial clusters and broad contrasts rather than read exact magnitudes. Because people perceive color differences imprecisely and classed color intervals may not match equal numeric intervals, choropleths communicate “where” patterns occur better than “how much” regions differ.

**Mechanism:** Area-filling color makes spatial grouping salient, but color steps/gradients are harder to translate into precise numeric comparisons across regions.

**Evidence:** Choropleths are recommended for showing clear regional patterns or local data, and they work best for a single variable rather than correlations between variables [@muth_choroplethmaps_2018]. Choropleths are described as effective for “the big picture” but not for subtle differences or exact value comparisons across regions [@muth_choroplethmaps_2018].

**Notes:** A choropleth can still be worthwhile when the mapped area is where readers live, because audiences like locating themselves geographically.

## Situations where this guideline applies <!-- role: context -->

- **User Goal:** Understand where values are high/low and whether neighboring regions share similar values.
- **Task:** Identify clusters, regional divides (e.g., urban vs rural), or hotspots/coldspots.
- **Data:** One metric per region (including a derived metric like year-over-year change), aligned to administrative boundaries.
- **Chart Setting:** A map view where readers can scan geography; optional tooltips for exact values.
- **Audience:** General readers who benefit from spatial context and self-location.
- **Success Criterion:** Viewers can quickly see the overall spatial structure without needing exact numeric comparisons.

## When not to follow it <!-- role: exceptions -->

- **Break it when:** The main goal is to show correlation between two variables. **Why:** Choropleths are not well-suited for communicating relationships between variables compared with charts designed for correlation judgments [@muth_choroplethmaps_2018].
- **Break it when:** The story depends on subtle numeric differences or precise cross-region comparison. **Why:** Small differences between colors are hard to perceive, and class boundaries can distort perceived numeric intervals [@muth_choroplethmaps_2018].
- **Break it when:** The most important regions are too small to see clearly at the intended size. **Why:** The map will hide key areas and undermine the point of the visualization [@muth_choroplethmaps_2018].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You give up precision and easy numeric comparison in exchange for spatial pattern visibility. **Risk:** Viewers may over-interpret minor color differences or treat class breaks as meaningful gaps. **Mitigation:** Treat the map as an overview and rely on complementary displays or interactivity for exact values.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Using a choropleth to show multi-variable relationships (e.g., “does X relate to Y by region?”). **Why it fails:** The map emphasizes geography and color, not the relationship between two measures [@muth_choroplethmaps_2018].
- **Mistake:** Using a choropleth as if it supports precise numeric comparisons across many regions. **Why it fails:** Viewers struggle to perceive small color differences and the legend intervals may not correspond to equal value differences [@muth_choroplethmaps_2018].

## Quick tests <!-- role: check -->

**Failure Sign:** People ask “what are the exact values?” or disagree on which of two similarly colored regions is higher. **Quick Check:** If you removed the map and used a non-map chart, would the message become clearer for the same data? **Stronger Test:** Ask a few readers to identify the main pattern and compare two specified regions; if they can’t do both reliably, the choropleth is misapplied.

## What to do instead <!-- role: fix -->

- Use a scatterplot or dot plot to show correlation between variables rather than mapping it.
- Use a table or short annotated text when exact numeric differences between regions are the point.
- Use a different mapping approach (e.g., symbol map) when you need to show absolute totals rather than rates.
- Aggregate or redesign the geographic display when critical regions are too small to read at the intended size.
