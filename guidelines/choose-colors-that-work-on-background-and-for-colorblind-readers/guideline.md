---
id: choose-colors-that-work-on-background-and-for-colorblind-readers
title: Choose categorical colors that separate on your background and remain distinguishable
  for colorblind readers
bibliography: references.bib
description: Pick palette colors that contrast with the background, differ clearly
  from each other, and stay separable under color-vision deficiencies.
labels:
- chart:generic
- task:categorize
- visual:color
- impact:accessibility
- data:categorical
- audience:general
- complexity:foundational
---

## Make palette colors contrast with the background and with each other, including under colorblindness <!-- role: advice -->

Choose categorical colors that stand out from the chart background, are clearly distinct from each other at small sizes, and remain separable for colorblind readers.

## Color separation depends on contrast, distinctness, and color-vision robustness <!-- role: reason -->

A categorical palette works when viewers can reliably map each category to a unique visual signal, even when marks are small or when color perception varies. If colors are too similar, too light on a light background, or rely on confusing hue pairs, categories collapse into ambiguity and decoding becomes error-prone.

**Mechanism:** Increasing background contrast and inter-color distinctness reduces perceptual confusion, and avoiding problematic hue pairings improves robustness for color-vision deficiencies.

**Evidence:** Practical palette requirements emphasize background contrast (including meeting contrast targets when needed), distinctness between colors (especially at small sizes), and colorblind separability as non-negotiable constraints for usable categorical palettes [@muth_good_color_palettes_2024].

**Notes:** A palette can look attractive in isolation but fail once applied to actual chart marks, sizes, and backgrounds.

## Use this when you need reliable category decoding in charts and maps <!-- role: context -->

- **User Goal:** Identify, track, or compare categories without misreading which color corresponds to which group.
- **Task:** Decode category identity from marks (lines, points, bars, areas) and legends.
- **Data:** Categorical groups, often multiple series, potentially many categories.
- **Chart Setting:** White or light backgrounds are common; marks may be thin (lines) or small (points), or large (areas).
- **Audience:** Broad audiences, including readers with color-vision deficiencies; accessibility expectations may apply.
- **Success Criterion:** Categories are easy to tell apart quickly and correctly, and colors do not disappear into the background.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Color is not the primary channel for category identity (for example, labels or direct annotations carry identity). **Why:** If color is redundant, strict palette separability constraints can be relaxed without harming comprehension [@muth_good_color_palettes_2024].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may give up subtle, aesthetic, or brand-preferred colors that do not separate well on the chosen background. **Risk:** Over-correcting can lead to an overly saturated palette that feels harsh, especially on large filled areas. **Mitigation:** Treat distinctness as a requirement, then fine-tune saturation and lightness to suit the mark type and tone [@muth_good_color_palettes_2024].

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Choosing a favorite light/pastel color on a white background. **Why it fails:** The mark loses contrast and becomes hard to see or read [@muth_good_color_palettes_2024].
- **Mistake:** Using two dark hues that are too close (for example, dark purple and dark blue). **Why it fails:** They merge at small sizes and become difficult to distinguish [@muth_good_color_palettes_2024].
- **Mistake:** Pairing red and green with similar brightness for categories. **Why it fails:** The palette becomes unreliable for colorblind readers [@muth_good_color_palettes_2024].

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers hesitate when matching legend items to marks, or two categories look interchangeable. **Quick Check:** Shrink the chart until marks are small and see whether each category still reads as unique. **Stronger Test:** Run a contrast check against the background when needed and use a colorblindness simulation or checker to confirm separability [@muth_good_color_palettes_2024].

## What to do instead <!-- role: fix -->

- Choose a darker or more contrasting version of any color that fades into the background.
- Increase the lightness difference between colors so they stay distinct even when hue perception varies.
- Replace confusing hue pairs with alternatives that separate more cleanly for common color-vision deficiencies.
- Reduce saturation for palettes intended for large filled areas while preserving distinctness between categories [@muth_good_color_palettes_2024].
