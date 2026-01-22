---
id: mirror-uneven-extremes-in-diverging-color-keys
title: Make asymmetric diverging scales obvious by shifting the legend center toward
  the smaller range
bibliography: references.bib
description: When diverging extremes cover unequal ranges, design the legend so the
  midpoint is visually closer to the smaller side.
labels:
- chart:map
- task:interpret
- visual:color
- impact:trust
- data:quantitative
- audience:novice
- complexity:advanced
---

## Reflect asymmetric ranges in diverging legends by positioning the center accordingly <!-- role: advice -->

For diverging color scales whose negative and positive ranges are not equal, design the color key so the center is visually closer to the side with the smaller numeric range.

## Symmetric-looking diverging legends imply symmetric data ranges <!-- role: reason -->

A diverging legend that looks balanced suggests equal distance from the midpoint to each extreme. If the numeric ranges differ, a visually symmetric legend can mislead readers about how much change each side represents.

**Mechanism:** Adjusting the midpoint position aligns the legend’s geometry with the underlying numeric domain, preventing false assumptions of symmetry.

**Evidence:** When diverging extremes cover different ranges from the center, the legend should make that unevenness obvious by mirroring it in the key’s design [@muth_color_keys_2023].

**Notes:** This complements other cues like explicit labeling of key values around the midpoint.

## When asymmetric diverging legend design is required <!-- role: context -->

- **User Goal:** Understand direction and magnitude around a central reference value.
- **Task:** Compare deviations above vs below a midpoint (often zero or a baseline).
- **Data:** Diverging scales with unequal min/max distances from the center.
- **Chart Setting:** Maps or heatmaps where legend is the primary numeric guide.
- **Audience:** Readers likely to assume diverging scales are symmetric by default.
- **Success Criterion:** Readers correctly infer that one side spans a smaller/larger numeric range.

## When not to visually offset the midpoint <!-- role: exceptions -->

**Break it when:** The scale is intentionally symmetric and the data domain is symmetric around the center. **Why:** Offsetting would imply asymmetry that isn’t present [@muth_color_keys_2023].

## Tradeoffs of asymmetric diverging legends <!-- role: costs -->

**Sacrifice:** Familiarity; readers may expect a centered midpoint and need a moment to adjust. **Risk:** Without clear labels, the offset may look like a layout mistake. **Mitigation:** Pair the offset with clear numeric labels around the midpoint and extremes.

## Common failure modes in diverging legends <!-- role: mistakes -->

**Mistake:** Using a perfectly centered midpoint in the legend even though the numeric domain is uneven. **Why it fails:** The legend implies equal magnitude on both sides, which can skew interpretation [@muth_color_keys_2023].

## Quick checks for diverging-scale honesty <!-- role: check -->

**Failure Sign:** The negative and positive ends cover different numeric spans but the legend looks mirrored. **Quick Check:** If you compute distance from center to min and to max and they differ, the legend should not appear symmetric. **Stronger Test:** Ask a reader which side has “more room” in values; if they say “they’re the same,” the legend design is underspecified.

## What to do instead if you can’t redesign the legend geometry <!-- role: fix -->

- Label the center and both extremes clearly so asymmetry is explicit in text.
- Use proportional segment widths for classed scales to show unequal spans.
- Add a short annotation stating the asymmetric range (e.g., “Scale runs from A to B with center at C”).
- Consider separate sequential scales if the diverging framing is not essential.
