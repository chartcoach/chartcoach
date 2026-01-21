---
id: enforce-lightness-order-in-sequential-and-diverging-palettes
title: Enforce a Clear Lightness Gradient
bibliography: references.bib
description: Use light-to-dark progression (and light midpoint for diverging) so readers
  can spot highs and lows quickly.
labels:
- chart:choropleth
- task:discover
- visual:color
- impact:clarity
- data:quantitative
- audience:general
- custom:palette-lightness
---

## The Rule <!-- role: advice -->

Ensure your sequential/diverging palette has a strong lightness progression: low values light, high values dark; for diverging palettes, make the midpoint the lightest and both extremes the darkest.

## The Logic <!-- role: reason -->

Lightness differences create fast, preattentive separation of low vs high regions; without it, users can’t quickly scan for extremes. Muth highlights that a light-to-dark gradient helps readers spot low/high values, and specifies the diverging midpoint should be lightest with darker extremes [@muth_choroplethmaps_2018].

- **The Principle:** Lightness supports rapid magnitude scanning
- **The Evidence:** [@muth_choroplethmaps_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly find extremes and understand directionality (low→high, negative→positive)
- **Data Type:** Ordered quantitative measures (sequential) or deviation data with a center (diverging)
- **Audience:** General readers scanning the map

## When to Break It <!-- role: exceptions -->

- **Scenario:** None stated in the post
- **Reason:** The post treats lightness ordering as a core requirement for readable sequential/diverging schemes [@muth_choroplethmaps_2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may need to abandon multi-hue artistic palettes that lack lightness structure.
- **The Risk:** Overusing multiple hues “to increase contrast” can become visually loud if overdone [@muth_choroplethmaps_2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using multiple hues without a consistent lightness ramp
- **Why it fails:** Readers can’t reliably infer which areas are higher/lower from color alone [@muth_choroplethmaps_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Some “higher” areas look lighter than “lower” areas, or the midpoint in a diverging scale isn’t visually neutral/light.
- **The Test:** Convert the palette to grayscale; it should still read from light (low/center) to dark (high/extremes) [@muth_choroplethmaps_2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Adjust palette lightness so it monotonically increases toward high values (and toward both extremes for diverging) [@muth_choroplethmaps_2018].
- **Best Fix:** Use Datawrapper defaults or ColorBrewer palettes as suggested in the post [@muth_choroplethmaps_2018].
