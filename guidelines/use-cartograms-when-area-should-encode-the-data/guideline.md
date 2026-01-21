---
id: use-cartograms-when-area-should-encode-the-data
title: Use Cartograms When You Want Area to Encode a Variable
bibliography: references.bib
description: Use cartograms to resize geographic regions so their area directly represents
  a data variable.
labels:
- chart:cartogram
- task:compare
- visual:area
- impact:insight
- data:geospatial
- audience:novice
- complexity:advanced
---

## The Rule <!-- role: advice -->

When the key message is a magnitude by region (e.g., total affected people), use a cartogram that resizes regions so area encodes that magnitude.

## The Logic <!-- role: reason -->

Cartograms intentionally distort geography so region area directly represents a data variable; Dorling cartograms replace regions with sized circles placed to resemble geographic configuration, enabling area-based comparison of totals while optionally coloring by a rate.

- **The Principle:** Deliberate geographic distortion to align area with data meaning
- **The Evidence:** [@heerTourVisualizationZoo2010]

## Where to Apply <!-- role: context -->

- **User Goal:** Compare totals by region and make magnitude differences visually unavoidable
- **Data Type:** Region totals (e.g., total obese people per state), potentially paired with a rate via color
- **Audience:** Broad audiences when geographic recognition is supported

## When to Break It <!-- role: exceptions -->

- **Scenario:** Precise geographic shape and location are critical for the task
- **Reason:** Cartograms distort shapes/placement and can hinder exact geographic reading [@heerTourVisualizationZoo2010]

## The Price <!-- role: costs -->

- **The Sacrifice:** Geographic fidelity
- **The Risk:** Users may struggle to identify regions without labels due to distortion

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a standard choropleth to imply totals via color alone
- **Why it fails:** Choropleths can mislead when totals and area interact; cartograms explicitly encode magnitude as area [@heerTourVisualizationZoo2010]

## How to Check <!-- role: check -->

- **Visual Sign:** The map’s story is “where the most is,” but the largest totals aren’t visually dominant
- **The Test:** If you want area to carry the magnitude message, a non-distorted map is working against you [@heerTourVisualizationZoo2010]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Use a Dorling-style sized-circle cartogram
- **Best Fix:** Encode total via circle area and encode a complementary rate via color, as in the obesity example [@heerTourVisualizationZoo2010]
