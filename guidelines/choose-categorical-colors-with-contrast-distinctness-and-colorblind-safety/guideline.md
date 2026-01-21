---
id: choose-categorical-colors-with-contrast-distinctness-and-colorblind-safety
title: Choose Categorical Colors That Stay Distinct and High-Contrast
bibliography: references.bib
description: Select categorical palette colors that work on your background, remain
  distinguishable from each other (including for colorblind viewers), and avoid unintended
  emphasis.
labels:
- chart:all
- task:categorize
- visual:color
- impact:accessibility
- data:categorical
- audience:general
- source:datawrapper
---

## The Rule <!-- role: advice -->

Pick categorical colors that (1) clearly contrast with the background, (2) are distinct from each other at small sizes, and (3) remain distinct for colorblind readers; avoid palettes where some colors look more important unless that hierarchy is intended.

## The Logic <!-- role: reason -->

Explain the principle at work here. Connect the rule to human perception or clear communication.

- **The Principle:** Robust discriminability and legibility of color encodings
- **The Evidence:** Muth notes that palettes that don’t contrast with the background, contain similar-looking hues (e.g., dark purple vs. dark blue), or rely on red/green with similar brightness can fail—especially at small sizes and for colorblind readers; she also cautions that some palettes unintentionally create unequal “importance” among categories [@muth_good_color_palettes_2024].

## Where to Apply <!-- role: context -->

This advice is designed for specific moments.

- **User Goal:** Identify and compare categories quickly and correctly
- **Data Type:** Categorical series (bars, lines, points, legend keys, map regions)
- **Audience:** Broad audiences, including colorblind readers and small-screen viewers

## When to Break It <!-- role: exceptions -->

List the specific scenarios where you should ignore this rule.

- **Scenario:** You intentionally need unequal salience (e.g., one “highlight” category vs. muted context categories)
- **Reason:** Equal visual importance is not the goal; purposeful emphasis can be clearer than forcing parity [@muth_good_color_palettes_2024].

## The Price <!-- role: costs -->

Be honest about the downsides.

- **The Sacrifice:** You may give up “pretty” but low-contrast/pastel colors and some trendy palettes that look good in isolation
- **The Risk:** Over-optimizing for distinction can produce palettes that feel less on-brand or less emotionally aligned with the topic [@muth_good_color_palettes_2024].

## Common Mistakes <!-- role: mistakes -->

Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.

- **The Wrong Fix:** Using a palette designed for UI/interior accents (few strong colors + many near-background colors) as a categorical palette
- **Why it fails:** Categories end up with unequal importance and/or weak background contrast, harming readability [@muth_good_color_palettes_2024].
- **The Wrong Fix:** Pairing similar dark hues (e.g., dark purple and dark blue) or red/green of similar brightness
- **Why it fails:** Colors collapse together at small sizes and for colorblind readers [@muth_good_color_palettes_2024].

## How to Check <!-- role: check -->

- **Visual Sign:** Two or more categories look identical in the legend or in thin lines/small marks; one category “pops” without meaning
- **The Test:** Shrink the chart until marks are small; convert to grayscale to see if categories still separate by lightness; run a colorblindness check (e.g., your tool’s simulator) [@muth_good_color_palettes_2024].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Increase background contrast by darkening colors; separate similar hues by adjusting lightness/saturation; replace red/green pairs with combinations that differ more in brightness [@muth_good_color_palettes_2024].
- **Best Fix:** Rebuild the palette around distinct lightness steps (so it “works in black and white”) and then choose hues that remain distinct while keeping roughly equal visual importance [@muth_good_color_palettes_2024].
