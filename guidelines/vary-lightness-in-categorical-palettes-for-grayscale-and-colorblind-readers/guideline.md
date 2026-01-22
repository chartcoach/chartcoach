---
id: vary-lightness-in-categorical-palettes-for-grayscale-and-colorblind-readers
title: Vary lightness across categorical hues so categories remain distinguishable
  in greyscale
bibliography: references.bib
description: Ensure categorical colors differ in lightness so they can be distinguished
  without hue, improving robustness and accessibility.
labels:
- chart:general
- task:distinguish
- visual:color
- impact:accessibility
- data:categorical
- audience:colorblind
- complexity:basic
---

## Vary lightness across categorical hues to preserve separation without hue <!-- role: advice -->

When using a categorical palette, choose hues that differ not only in hue but also in lightness so the categories remain distinguishable even in greyscale. Keep the palette readable for color-impaired viewers by avoiding same-lightness colors that only differ by hue [@muth_which_color_scale_2021].

## Lightness differences survive when hue perception fails <!-- role: reason -->

Hue discrimination can break under greyscale viewing, poor displays, printing, or color-vision deficiencies, but lightness differences remain perceivable as contrast. If categorical colors share similar lightness, categories collapse into near-identical tones when hue information is reduced.

**Mechanism:** Lightness contrast provides a redundant cue for separating categories, so the mapping stays legible when hue cues degrade.

**Evidence:** Categorical hues are recommended to have different lightness values so they work in greyscale and become easier to distinguish, especially for colorblind readers [@muth_which_color_scale_2021].

**Notes:** Lightness contrast can improve both aesthetics and separability of categories.

## When you rely on color to label groups <!-- role: context -->

- **User Goal:** Tell categories apart reliably in legends and marks.
- **Task:** Identify series/groups and match marks to legend entries.
- **Data:** Categorical variables with multiple distinct groups.
- **Chart Setting:** Screens, print, PDFs, projectors, and embeds where color fidelity varies.
- **Audience:** Broad audiences, including readers with color-vision deficiencies or low-quality viewing conditions.
- **Success Criterion:** Categories remain distinguishable without relying on hue alone.

## When lightness variation is constrained <!-- role: exceptions -->

**Break it when:** Brand guidelines lock you into same-lightness hues and you cannot change the palette. **Why:** You may not be able to introduce sufficient lightness contrast while staying on-brand [@muth_which_color_scale_2021].

## Tradeoffs of pushing lightness contrast in categorical palettes <!-- role: costs -->

**Sacrifice:** Some brand or aesthetic harmony may be reduced when you introduce stronger lightness differences. **Risk:** Very light colors can become hard to see on white backgrounds, and very dark colors can dominate. **Mitigation:** Balance lightness changes with sufficient stroke/label contrast and background-aware testing.

## Common ways categorical palettes fail accessibility <!-- role: mistakes -->

- **Mistake:** Selecting colors that differ only in hue but share similar lightness. **Why it fails:** Categories become indistinguishable in greyscale and for some colorblind viewers [@muth_which_color_scale_2021].
- **Mistake:** Using too many categorical hues without checking separability. **Why it fails:** Even with varied lightness, crowded palettes reduce reliable matching between marks and legend.

## Quick checks for lightness robustness <!-- role: check -->

**Failure Sign:** Two or more categories look nearly identical when printed or viewed on a low-quality screen. **Quick Check:** Toggle a greyscale view; each category should still look different. **Stronger Test:** Ask someone to match marks to legend entries quickly in greyscale and note confusion pairs.

## What to do instead if categories collapse in greyscale <!-- role: fix -->

- Adjust the palette so each category occupies a distinct lightness level as well as a distinct hue.
- Reduce the number of categories shown at once by grouping minor categories into “other,” then de-emphasize it.
- Add non-color cues (direct labels, line styles, markers) to separate categories when palette changes are constrained.
- Use highlighting to focus attention on a few key categories and mute the rest when you cannot guarantee full separability.
