---
id: choose-color-stops-to-reveal-differences-without-exaggeration
title: Tune Color Stops to Show Real Differences
bibliography: references.bib
description: "Choose stop counts and thresholds so different values look different,\
  \ extremes get extremes, and contrast isn\u2019t overstated."
labels:
- chart:choropleth
- task:encode
- visual:color
- impact:honesty
- data:quantitative
- audience:general
- custom:binning
---

## The Rule <!-- role: advice -->

Set your color stops so that (1) different values can appear as different colors, (2) the brightest/darkest colors are reserved for true extremes, and (3) contrast reveals patterns without exaggerating differences.

## The Logic <!-- role: reason -->

Color stops control perceived drama: too few or poorly placed stops hide variation; overly aggressive stops overstate differences. Muth advises ensuring readers “see all the differences,” reserving brightest/darkest for extremes, and taking time choosing the number of stops to avoid blowing up differences [@muth_choroplethmaps_2018].

- **The Principle:** Binning controls perceived effect size
- **The Evidence:** [@muth_choroplethmaps_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** See meaningful spatial variation without misleading emphasis
- **Data Type:** Quantitative region-level data mapped with discrete steps
- **Audience:** General audiences likely to infer importance from strong contrast

## When to Break It <!-- role: exceptions -->

- **Scenario:** You use a continuous color scale instead of discrete steps
- **Reason:** Continuous scales reduce reliance on stop placement for nuance (though legend design still matters) [@muth_choroplethmaps_2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** More time iterating thresholds and checking how patterns appear.
- **The Risk:** If stops are tuned for drama, the map can become misleading; if tuned too gently, patterns may be hard to see [@muth_choroplethmaps_2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using default stop counts/thresholds without checking whether different values become visually distinct
- **Why it fails:** It can either flatten variation or overemphasize noise [@muth_choroplethmaps_2018].
- **The Wrong Fix:** Spending darkest/brightest colors on midrange values
- **Why it fails:** Extremes stop standing out, and the legend becomes deceptive [@muth_choroplethmaps_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Many regions with different values share the same shade, or the map looks overly dramatic compared to the data spread.
- **The Test:** Compare the distribution of values to the number of stops; verify that extremes in the data align with the extremes in the palette [@muth_choroplethmaps_2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Adjust the number of stops and reassign darkest/brightest to the true min/max range [@muth_choroplethmaps_2018].
- **Best Fix:** Switch to a continuous color scale (and use tooltips for exact values) if nuance between neighbors matters [@muth_choroplethmaps_2018].
