---
id: enforce-lightness-order-in-sequential-and-diverging-choropleths
title: Make lightness increase monotonically in sequential palettes and place the
  lightest color at the diverging midpoint
bibliography: references.bib
description: Use light-to-dark progression for low-to-high values; for diverging schemes,
  keep the midpoint lightest and extremes darkest.
labels:
- chart:choropleth
- task:compare
- visual:color
- impact:readability
- data:geospatial
- audience:general
- complexity:intermediate
---

## Use a light-to-dark progression, with the diverging center as the lightest <!-- role: advice -->

In sequential choropleths, map lower values to lighter colors and higher values to darker colors using a clear lightness difference. In diverging choropleths, make the midpoint the lightest color and the two extremes the darkest.

## Lightness supports fast scanning of highs and lows <!-- role: reason -->

Lightness differences let viewers quickly identify extremes without needing to interpret hue changes precisely. In diverging maps, a light midpoint creates a visual “neutral” anchor so regions on either side are read as departures in opposite directions.

**Mechanism:** Light-to-dark gradients provide a strong visual ordering cue; a light diverging midpoint acts as a perceptual reference point.

**Evidence:** A gradient from light to dark is recommended to help readers quickly spot low and high values, and in diverging schemes the middle color is recommended to be the lightest with extremes darkest [@muth_choroplethmaps_2018]. Default palettes and ColorBrewer palettes are suggested when unsure [@muth_choroplethmaps_2018].

**Notes:** Using multiple hues can increase contrast, but overuse can reduce coherence.

## Situations where this guideline applies <!-- role: context -->

- **User Goal:** Identify low, medium, and high regions quickly.
- **Task:** Scan for extremes and compare neighboring regions.
- **Data:** Ordered numeric values; optionally signed values around a center.
- **Chart Setting:** Choropleth with sequential or diverging legend.
- **Audience:** Mixed expertise; needs fast comprehension.
- **Success Criterion:** Extremes are visually obvious and the legend order matches visual order.

## When not to follow it <!-- role: exceptions -->

**Break it when:** You are using a qualitative/categorical palette with no inherent order. **Why:** Imposing lightness order can falsely imply ranking among categories [@muth_choroplethmaps_2018].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Strict lightness ordering can constrain brand palettes. **Risk:** If the midpoint is not actually meaningful, a diverging light center can suggest neutrality where none exists. **Mitigation:** Ensure the legend labeling makes the center value explicit when diverging.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Using a sequential palette with little or no lightness change. **Why it fails:** Viewers struggle to distinguish low from high at a glance [@muth_choroplethmaps_2018].
- **Mistake:** Making diverging extremes lighter than the midpoint. **Why it fails:** It reverses the intended emphasis and obscures departures from the center [@muth_choroplethmaps_2018].

## Quick tests <!-- role: check -->

**Failure Sign:** High and low regions do not “pop out” without reading the legend carefully. **Quick Check:** Convert the map to grayscale; the ordering should still be apparent. **Stronger Test:** Ask someone to point to the highest and lowest regions within a few seconds; they should succeed without hovering tooltips.

## What to do instead <!-- role: fix -->

- Adjust the palette so lightness changes clearly from low to high for sequential maps.
- Rebuild diverging palettes so the center is light and both ends are dark.
- Use default palettes or ColorBrewer-style palettes when constructing a coherent lightness order is difficult.
- Add tooltips for exact values when color cannot carry fine distinctions alone.
