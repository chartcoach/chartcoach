---
id: map-only-one-variable-in-a-choropleth
title: Map Only One Variable in a Choropleth
bibliography: references.bib
description: Keep choropleths focused on a single variable (including a computed difference)
  to avoid unclear multivariate messages.
labels:
- chart:choropleth
- task:compare
- visual:color
- impact:clarity
- data:geospatial
- audience:general
- complexity:basic
---

## The Rule <!-- role: advice -->

Encode only one variable in a choropleth map (or a single derived metric like a change/difference).

## The Logic <!-- role: reason -->

Color-filled regions are effective for one encoded quantity; adding more variables makes interpretation ambiguous and undermines the map’s “big picture” strength. Muth explicitly recommends choropleths “work best when showing just one variable” [@muth_choroplethmaps_2018].

- **The Principle:** Single-channel, single-variable emphasis
- **The Evidence:** [@muth_choroplethmaps_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand how one measure varies across regions
- **Data Type:** Region-level values; optionally computed change between two points in time
- **Audience:** General audiences scanning for patterns

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your real question is about the relationship between two measures
- **Reason:** Use a dotplot or scatterplot to show correlation instead of forcing it into a choropleth [@muth_choroplethmaps_2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** You can’t show multiple dimensions at once in the same map.
- **The Risk:** If stakeholders expect multivariate insight, a single-variable choropleth may feel incomplete [@muth_choroplethmaps_2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Trying to imply correlation through a single choropleth shading
- **Why it fails:** The map cannot reliably communicate relationships between multiple variables; viewers will overinterpret patterns [@muth_choroplethmaps_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** The caption/legend needs to explain two+ concepts to interpret one color scale.
- **The Test:** Count how many distinct measures a reader must know to interpret the color—if more than one, you’re outside choropleth strengths [@muth_choroplethmaps_2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Convert inputs into one derived metric (e.g., difference) and map only that [@muth_choroplethmaps_2018].
- **Best Fix:** Use a non-map chart (dotplot/scatterplot) for correlation questions [@muth_choroplethmaps_2018].
