---
id: show-form-not-just-color-in-the-color-key
title: Encode Shape and Stroke in the Color Key
bibliography: references.bib
description: "Match the legend markers to the chart\u2019s actual mark types (lines,\
  \ dashes, thickness, hatching) so readers can identify series faster."
labels:
- chart:line
- task:identify
- visual:color
- impact:clarity
- data:categorical
- audience:novice
- complexity:basic
- source:datawrapper-blog
---

## The Rule <!-- role: advice -->

In the color key, show the same mark form used in the chart (line thickness, dashes, rectangles, hatching, outlines), not color swatches alone.

## The Logic <!-- role: reason -->

When categories differ by both color and form, readers search for a combined “signature.” If the legend only shows color, readers must infer the form mapping, slowing identification. Muth emphasizes that reproducing form in the key helps readers quickly find elements in the chart [@muth_color_keys_2023].

- **The Principle:** Increase match accuracy by mirroring visual encoding
- **The Evidence:** [@muth_color_keys_2023]

## Where to Apply <!-- role: context -->

- **User Goal:** Locating the right series/region quickly in the visualization
- **Data Type:** Categorical encodings that use both color and form (e.g., dashed vs solid lines, hatched areas)
- **Audience:** Any, especially readers scanning quickly

## When to Break It <!-- role: exceptions -->

- **Scenario:** The visualization uses only uniform shapes and strokes (only hue varies)
- **Reason:** Adding extra form cues would be redundant and may clutter the key [@muth_color_keys_2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** Slightly more legend design effort and space per item
- **The Risk:** Small legend markers can make subtle dash patterns or hatching hard to perceive [@muth_color_keys_2023].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using identical circular swatches for everything even when the chart uses lines/areas/patterns
- **Why it fails:** Readers can’t quickly connect the legend item to the mark they see in the plot [@muth_color_keys_2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Readers can name a color from the key but still can’t find the corresponding mark quickly.
- **The Test:** Point to a mark in the chart—can you identify its legend entry using shape/stroke alone? If not, the key isn’t reflecting form [@muth_color_keys_2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace simple swatches with miniature versions of the chart marks (short line segments, patterned boxes).
- **Best Fix:** Standardize legend marker sizing so form details (dashes, thickness, hatching) remain legible and match the chart styling [@muth_color_keys_2023].
