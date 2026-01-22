---
id: design-choropleth-legends-with-even-intervals-and-explicit-center
title: Design choropleth legends with evenly spaced intervals and an explicit center
  for diverging scales
bibliography: references.bib
description: 'Legends should be quickly decipherable: show low/high and intermediate
  values at consistent intervals, and include the midpoint for diverging palettes.'
labels:
- chart:choropleth
- task:interpret
- visual:legend
- impact:clarity
- data:quantitative
- audience:general
- complexity:foundational
---

## Build a decipherable legend with consistent intervals, and include the midpoint for diverging scales <!-- role: advice -->

Make the choropleth legend easy to decode by showing the lowest and highest values plus a few evenly spaced intermediate values. For diverging palettes, explicitly include the center value in the legend.

## Legends teach the mapping from color to number <!-- role: reason -->

Because the map itself often cannot communicate exact values, viewers rely on the legend to translate color into magnitude and direction. Uneven or sparse legend labeling forces guesswork, while evenly spaced labels provide a stable numeric scaffold; diverging schemes need a clear center to define what “above” and “below” mean.

**Mechanism:** Clear, evenly spaced legend anchors reduce decoding effort and prevent misinterpretation of scale structure, especially around a diverging midpoint.

**Evidence:** Color keys are described as crucial; for sequential schemes they should show lowest and highest values plus two to four in-between values, and values should use the same interval (e.g., 0, 25, 50 rather than 0, 15, 50); for diverging schemes the key should also display the center value [@muth_choroplethmaps_2018].

**Notes:** A well-designed legend supports both quick scanning and more careful reading.

## Situations where this guideline applies <!-- role: context -->

- **User Goal:** Understand what a color implies numerically.
- **Task:** Translate colors into approximate values or ranges.
- **Data:** Quantitative values encoded with sequential or diverging color.
- **Chart Setting:** Any choropleth where colors represent magnitude; static or interactive.
- **Audience:** Readers who need quick decoding without deep map-reading expertise.
- **Success Criterion:** Readers can approximate values from the legend without confusion.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The map uses categorical colors rather than a numeric scale. **Why:** Even-interval numeric ticks are not meaningful for unordered categories [@muth_choroplethmaps_2018].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Legend simplicity may require rounding or choosing representative tick values. **Risk:** Overly detailed legends can become cluttered and slow scanning. **Mitigation:** Keep intermediate ticks to a small number while maintaining consistent intervals.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Using uneven tick intervals in a numeric legend (e.g., 0, 15, 50). **Why it fails:** It makes the scale hard to interpret quickly and can mislead about spacing between values [@muth_choroplethmaps_2018].
- **Mistake:** Omitting the midpoint in a diverging legend. **Why it fails:** Readers cannot tell what color represents the center reference value [@muth_choroplethmaps_2018].

## Quick tests <!-- role: check -->

**Failure Sign:** People misread mid-range colors or can’t tell what “neutral” means in a diverging map. **Quick Check:** Look only at the legend and see if you can estimate a mid-tone value in under a few seconds. **Stronger Test:** Ask someone to estimate the value of three differently colored regions using only the legend; large errors indicate legend design problems.

## What to do instead <!-- role: fix -->

- Label the legend with the minimum and maximum values plus a few intermediate values at equal intervals.
- Add the center value explicitly for diverging scales.
- Reduce the number of labeled ticks if the legend becomes visually busy while keeping intervals consistent.
- Use tooltips to provide exact values so the legend can stay simple.
