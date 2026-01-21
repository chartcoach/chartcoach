---
id: encode-higher-quantities-in-darker-colors-when-colormap-does-not-appear-translucent
title: Encode Higher Quantities in Darker Colors When the Colormap Does Not Appear
  Translucent
bibliography: references.bib
description: For standard sequential colormaps that do not look like they vary in
  opacity, map larger values to darker colors regardless of background.
labels:
- chart:heatmap
- chart:choropleth
- task:interpret
- visual:color
- impact:clarity
- data:quantitative
- audience:novice
- complexity:basic
---

## The Rule <!-- role: advice -->

If your sequential colormap does not appear to vary in opacity, encode larger quantities with darker colors (dark-more), even on dark backgrounds.

## The Logic <!-- role: reason -->

This works because viewers show a robust **dark-is-more bias**: when opacity variation is not perceptually suggested, people infer “more” from darker colors and interpret dark-more encodings faster than light-more encodings across backgrounds [@schlossMappingColorMeaning2019a].

- **The Principle:** Dark-is-more bias dominates when opacity variation is absent.
- **The Evidence:** Response-time advantages for dark-more encoding for multiple monotonic-lightness scales with no background interaction (e.g., Autumn, Hot) in Experiment 1 [@schlossMappingColorMeaning2019a].

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly decide which region/time/category has “more” vs “less.”
- **Data Type:** Sequential quantitative data shown with a monotonic-lightness color scale.
- **Audience:** General audiences or mixed expertise, especially when you want interpretation to be effortless.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The colormap is intentionally designed to look like it varies in opacity (e.g., looks like a translucent overlay on the background).
- **Reason:** In that case, an opaque-is-more bias can conflict with dark-is-more, especially on dark backgrounds [@schlossMappingColorMeaning2019a].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may forgo “inverted” light-on-dark aesthetic conventions some teams prefer.
- **The Risk:** If the scale unintentionally looks translucent on some background, the intended dark-more mapping may become less intuitive on dark backgrounds [@schlossMappingColorMeaning2019a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Flipping to light-more just because the background is dark.
- **Why it fails:** Background alone does not reliably reverse inferred mappings unless the colormap appears to vary in opacity [@schlossMappingColorMeaning2019a].

## How to Check <!-- role: check -->

- **Visual Sign:** On both white and black backgrounds, the scale reads as “solid color differences,” not as “ink/paint strength” fading into the background.
- **The Test:** Place the same legend/scale on both white and black; if it does not look like it’s blending toward the background, treat it as “no opacity variation” and use dark-more [@schlossMappingColorMeaning2019a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reverse the numeric mapping so higher values are assigned to darker colors (keep the same colors, flip the data-to-color direction).
- **Best Fix:** Choose or redesign a sequential scale that remains perceptually “opaque” (not background-interpolated) on your intended backgrounds, then use dark-more encoding [@schlossMappingColorMeaning2019a].
