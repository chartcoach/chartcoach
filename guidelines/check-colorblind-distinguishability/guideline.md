---
id: check-colorblind-distinguishability
title: Verify Colorblind Distinguishability
bibliography: references.bib
description: Simulate color vision deficiencies to ensure readers can still distinguish
  your encoded groups and values.
labels:
- chart:any
- task:validate
- visual:color
- impact:accessibility
- data:any
- audience:general
- complexity:basic
---

## The Rule <!-- role: advice -->

Simulate colorblind vision for your palette and revise any colors that become indistinguishable.

## The Logic <!-- role: reason -->

Some color combinations collapse for readers with color vision deficiencies; simulation exposes collisions so you can preserve meaning for more viewers [@muth_colorguide_2018].

- **The Principle:** Robust encoding under color vision variation
- **The Evidence:** [@muth_colorguide_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Correctly differentiate categories or value steps regardless of color vision.
- **Data Type:** Any color-encoded chart or map, especially multi-category palettes.
- **Audience:** General public (includes colorblind readers by default).

## When to Break It <!-- role: exceptions -->

- **Scenario:** Color is purely decorative and not used to encode meaning.
- **Reason:** If no information is carried by color, indistinguishability does not break interpretation (though it may still affect aesthetics) [@muth_colorguide_2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may need to abandon preferred hues or trendy palettes.
- **The Risk:** Over-correcting may reduce brand alignment or emotional tone if not handled carefully [@muth_colorguide_2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming a palette is “accessible” because it looks distinct to you.
- **Why it fails:** Your perception isn’t representative; problematic pairs may only appear under deficiency simulation [@muth_colorguide_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Two categories/steps become the same or nearly the same under simulation.
- **The Test:** Run a colorblindness simulator on the full chart/map (not just the legend) and look for merges [@muth_colorguide_2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Swap one of the colliding colors for a hue that remains distinct under simulation.
- **Best Fix:** Redesign the palette with colorblind simulation turned on throughout, iterating until all encoded elements stay separable [@muth_colorguide_2018].
