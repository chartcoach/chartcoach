---
id: ensure-color-differences-are-distinguishable-in-lightness
title: Vary Lightness So the Chart Works in Black and White
bibliography: references.bib
description: Make color encodings separable by ensuring clear lightness differences,
  so the visualization remains readable in grayscale.
labels:
- chart:multi
- task:distinguish
- visual:color
- impact:accessibility
- data:categorical
- audience:general
- visual:lightness
- source:datawrapper
---

## The Rule <!-- role: advice -->

Choose colors that differ clearly in lightness so the visualization remains readable in grayscale (“get it right in black & white”).

## The Logic <!-- role: reason -->

If elements are distinguishable by lightness, the encoding survives common color vision deficiencies because the viewer can rely on brightness contrast rather than hue. The blog frames grayscale readability as a practical proxy for colorblind readability and highlights yellow as especially light and thus often high-contrast [@muth_colorblindness_2020].

- **The Principle:** Redundant separability via luminance contrast
- **The Evidence:** “Get it right in black & white” is presented as a core tactic; examples show combinations working when lightness differs, and failing when it doesn’t [@muth_colorblindness_2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Distinguishing categories, statuses (e.g., “good/bad”), or map regions without confusion
- **Data Type:** Categorical or binned values where color is used as the primary cue
- **Audience:** Mixed audiences, including colorblind readers and readers in low light or print contexts [@muth_colorblindness_2020]

## When to Break It <!-- role: exceptions -->

- **Scenario:** You must use equal-lightness brand colors and cannot adjust them
- **Reason:** Lightness contrast can’t be introduced; you’ll need a second visual variable (symbols, patterns, dashes) [@muth_colorblindness_2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** Some hues will need to be lightened/darkened, changing the “pure” brand look
- **The Risk:** Very light colors can reduce legibility on white backgrounds if not handled carefully [@muth_colorblindness_2020].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming hue difference alone (e.g., red vs. green) guarantees distinction
- **Why it fails:** For many colorblind readers, those hues can converge, especially when lightness is similar [@muth_colorblindness_2020].

## How to Check <!-- role: check -->

- **Visual Sign:** Categories merge when viewed without color
- **The Test:** Convert the chart to grayscale (or print in black and white) and confirm every encoded category remains separable [@muth_colorblindness_2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Darken one category and lighten another until they separate in grayscale
- **Best Fix:** Rebuild the palette with deliberate lightness steps and reserve very light hues (like yellow) for categories that need maximum contrast [@muth_colorblindness_2020].
