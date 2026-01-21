---
id: use-cartograms-when-people-affected-matters-more-than-land-area
title: Use Cartograms When People Affected Matters
bibliography: references.bib
description: Switch from choropleths to population cartograms when land area misrepresents
  how many people are impacted.
labels:
- chart:map
- task:compare
- visual:area
- impact:honesty
- data:geospatial
- audience:general
- custom:cartogram
---

## The Rule <!-- role: advice -->

Use a population cartogram when you need the map to reflect how many people are affected, not how much land is affected.

## The Logic <!-- role: reason -->

Choropleths weight visual attention by geographic area; sparsely populated large regions can dominate. Cartograms reallocate space toward populated areas to provide a more honest emphasis when population density varies strongly. This tradeoff is described directly by Muth [@muth_choroplethmaps_2018].

- **The Principle:** Visual weighting should match the analytic weighting (people vs land)
- **The Evidence:** [@muth_choroplethmaps_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand impact on people or voters rather than territory
- **Data Type:** Region-level rates/values where population distribution is highly uneven
- **Audience:** Readers familiar enough with geography to tolerate distortion

## When to Break It <!-- role: exceptions -->

- **Scenario:** Readers are unlikely to recognize regions once distorted
- **Reason:** Cartograms make region recognition harder; avoid if geographic familiarity is low [@muth_choroplethmaps_2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Geographic shape fidelity and easy place recognition.
- **The Risk:** Readers may get lost or distrust the map if they can’t identify regions [@muth_choroplethmaps_2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a cartogram without considering recognizability
- **Why it fails:** The audience can’t map the distorted shapes back to known places, losing comprehension [@muth_choroplethmaps_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers need excessive labels/tooltips just to know where they are.
- **The Test:** Ask a few target readers to locate 3–5 key regions quickly; if they struggle, the cartogram may not be appropriate [@muth_choroplethmaps_2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add labels/tooltips for key regions to support recognition [@muth_choroplethmaps_2018].
- **Best Fix:** Use a standard choropleth when recognizability is the priority, or pair cartogram with a reference map if needed [@muth_choroplethmaps_2018].
