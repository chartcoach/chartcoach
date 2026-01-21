---
id: add-tooltips-and-labels-to-communicate-region-names-and-values
title: Use Tooltips and Labels to Provide Details
bibliography: references.bib
description: "Add tooltips and labels so readers can access region names, exact values,\
  \ and helpful context that the map alone can\u2019t show."
labels:
- chart:choropleth
- task:lookup
- visual:annotation
- impact:clarity
- data:geospatial
- audience:general
- custom:tooltips
---

## The Rule <!-- role: advice -->

Add tooltips to show each region’s name and value, and add labels when readers may not know the geography.

## The Logic <!-- role: reason -->

Regions are often hard to identify and values are hard to read from color alone; tooltips deliver exact numbers and names on demand and can also convey extra context. Labels reduce reliance on prior geographic knowledge. Muth recommends tooltips for names/values and extra info, and notes labels become more important when the mapped area is unfamiliar [@muth_choroplethmaps_2018].

- **The Principle:** On-demand detail and orientation support
- **The Evidence:** [@muth_choroplethmaps_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Look up a specific region’s value or confirm what a region is
- **Data Type:** Any choropleth where regions aren’t inherently readable
- **Audience:** Especially readers unfamiliar with the mapped geography

## When to Break It <!-- role: exceptions -->

- **Scenario:** None stated in the post
- **Reason:** The post treats tooltips/labels as broadly helpful where readability is limited [@muth_choroplethmaps_2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Labels can clutter; tooltips require interaction and may not help in static outputs.
- **The Risk:** Over-labeling can obscure the color pattern the choropleth is meant to show [@muth_choroplethmaps_2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Expecting readers to infer exact values from shading alone
- **Why it fails:** Choropleths are not good for subtle/precise differences; tooltips supply the missing precision [@muth_choroplethmaps_2018].
- **The Wrong Fix:** Labeling too many regions
- **Why it fails:** Visual clutter competes with the map’s primary signal [@muth_choroplethmaps_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Readers can’t identify regions or must guess values from similar colors.
- **The Test:** Try to find and name three regions and their values without interaction; if it’s difficult, add tooltips/labels [@muth_choroplethmaps_2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Enable tooltips with region name + exact value [@muth_choroplethmaps_2018].
- **Best Fix:** Add a small set of strategic labels (key regions) when geography familiarity is low, and keep the rest accessible via tooltips [@muth_choroplethmaps_2018].
