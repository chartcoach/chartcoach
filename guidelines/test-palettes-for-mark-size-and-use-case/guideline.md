---
id: test-palettes-for-mark-size-and-use-case
title: "Test Colors at the Sizes You\u2019ll Use"
bibliography: references.bib
description: Validate that your palette works for tiny lines, large areas, and real
  chart contexts before publishing.
labels:
- chart:any
- task:validate
- visual:color
- impact:clarity
- data:any
- audience:general
- complexity:intermediate
---

## The Rule <!-- role: advice -->

Test your palette in the actual mark types and sizes you will use (tiny lines, big areas, map regions) before finalizing it.

## The Logic <!-- role: reason -->

Colors that look distinct in swatches can merge when used as thin strokes or small regions; checking performance across mark scales prevents false confidence from palette-only previews [@muth_colorguide_2018].

- **The Principle:** Context- and scale-dependent color perception
- **The Evidence:** [@muth_colorguide_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Reliably distinguish series/regions in real reading conditions.
- **Data Type:** Any; especially multi-series charts and choropleth maps.
- **Audience:** Everyone, including mobile readers.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The chart uses only one data color plus neutrals (minimal palette).
- **Reason:** With very few colors and clear hierarchy, scale-induced confusion is less likely (though still possible) [@muth_colorguide_2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Extra time iterating and previewing.
- **The Risk:** Over-optimizing for one context might reduce harmony in another (e.g., lines vs areas) [@muth_colorguide_2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Approving a palette by looking only at isolated color chips.
- **Why it fails:** It ignores how marks, proximity, and size change perceived distinctness [@muth_colorguide_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Lines become indistinguishable; large filled areas look fine but small ones blur together (or vice versa).
- **The Test:** Preview the palette on both thin-line and large-area samples (as suggested via palette-checking tools) [@muth_colorguide_2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Increase contrast between the most-confused colors (swap one hue, or widen differences).
- **Best Fix:** Iterate with a palette testing tool that explicitly previews tiny lines and big areas, and adjust until both pass [@muth_colorguide_2018].
