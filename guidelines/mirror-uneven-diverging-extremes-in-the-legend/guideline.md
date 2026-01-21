---
id: mirror-uneven-diverging-extremes-in-the-legend
title: Reflect Uneven Diverging Extremes in the Color Key
bibliography: references.bib
description: "When a diverging scale\u2019s negative and positive ranges aren\u2019\
  t symmetric, visually encode that asymmetry in the legend layout."
labels:
- chart:map
- task:interpret
- visual:color
- impact:truthfulness
- data:quantitative
- audience:novice
- complexity:advanced
- source:datawrapper-blog
---

## The Rule <!-- role: advice -->

If a diverging color scale has unequal ranges on either side of the center, make the legend asymmetric too—position the center closer to the shorter side and show the unequal coverage clearly.

## The Logic <!-- role: reason -->

Symmetric legend designs imply symmetric numeric ranges; if the center is closer to one extreme in value, the legend should communicate that to prevent misinterpretation. Muth explicitly recommends mirroring uneven extremes in both colors and the key design [@muth_color_keys_2023].

- **The Principle:** Keep legend geometry consistent with numeric meaning
- **The Evidence:** [@muth_color_keys_2023]

## Where to Apply <!-- role: context -->

- **User Goal:** Understanding direction and magnitude around a meaningful midpoint (e.g., 0)
- **Data Type:** Diverging scales where min-to-center and center-to-max spans differ
- **Audience:** Readers who may assume diverging scales are balanced unless shown otherwise

## When to Break It <!-- role: exceptions -->

- **Scenario:** The diverging scale is truly symmetric around the center
- **Reason:** For symmetric ranges, asymmetry would incorrectly suggest imbalance [@muth_color_keys_2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** A visually “neat” mirrored legend
- **The Risk:** Some readers may need a moment to adjust expectations if they’re used to perfectly symmetric diverging keys [@muth_color_keys_2023].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a perfectly symmetric diverging legend even when the numeric ranges aren’t symmetric
- **Why it fails:** It suggests equal magnitude and can distort how readers interpret color intensity on either side [@muth_color_keys_2023].

## How to Check <!-- role: check -->

- **Visual Sign:** The legend’s midpoint is centered visually but the numeric labels show unequal spans.
- **The Test:** Compare the absolute numeric range on each side—if they differ, the legend layout should differ too [@muth_color_keys_2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Adjust labels to clearly indicate unequal endpoints and the true center.
- **Best Fix:** Redesign the diverging key so the center point and segment lengths visually match the unequal numeric ranges [@muth_color_keys_2023].
