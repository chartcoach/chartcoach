---
id: choose-the-smallest-feasible-geographic-units
title: Choose the Smallest Feasible Geographic Units
bibliography: references.bib
description: Prefer smaller administrative units to reveal finer regional patterns
  in choropleth maps.
labels:
- chart:choropleth
- task:discover
- visual:color
- impact:insight
- data:geospatial
- audience:general
- complexity:intermediate
---

## The Rule <!-- role: advice -->

Map the smallest geographic units you can credibly use (e.g., counties instead of states) to reveal regional patterns.

## The Logic <!-- role: reason -->

Smaller units increase spatial resolution, making local variation and clusters visible that would be averaged away at larger units. Muth recommends using the smallest units possible to give a “more refined image” and let readers “spot more regional pattern” [@muth_choroplethmaps_2018].

- **The Principle:** Higher spatial resolution reveals structure
- **The Evidence:** [@muth_choroplethmaps_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Detect localized hotspots/coldspots and within-region variation
- **Data Type:** Data available at multiple administrative levels
- **Audience:** Readers comfortable navigating more detailed boundaries

## When to Break It <!-- role: exceptions -->

- **Scenario:** The larger unit is the meaningful unit of outcome (e.g., winner-takes-it-all election results by state)
- **Reason:** A finer unit may be less informative for the system being explained [@muth_choroplethmaps_2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** More visual complexity and potentially harder region recognition.
- **The Risk:** Small units can become tiny on screen and harder to interpret without tooltips/labels [@muth_choroplethmaps_2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Defaulting to the coarsest available geography
- **Why it fails:** It smooths away meaningful local differences and reduces pattern detection [@muth_choroplethmaps_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Large areas appear uniform, but you suspect internal variation.
- **The Test:** If you have data at a finer level, render both and see whether patterns emerge only at the smaller unit [@muth_choroplethmaps_2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch to the next smaller available unit level [@muth_choroplethmaps_2018].
- **Best Fix:** Use the smallest unit that remains readable and add tooltips/labels to support navigation [@muth_choroplethmaps_2018].
