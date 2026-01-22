---
id: double-encode-categories-with-non-color-cues-when-colors-cannot-be-made-colorblind-safe
title: Double-encode categories with non-color cues when colors cannot be made colorblind-safe
bibliography: references.bib
description: Add symbols, shapes, patterns, or line styles so categories remain distinguishable
  without relying on color.
labels:
- chart:scatter
- task:distinguish
- visual:shape
- impact:accessibility
- data:categorical
- audience:general
- accessibility:color-vision-deficiency
---

## Add a second visual encoding so color is not the only category cue <!-- role: advice -->

When colors may be ambiguous for colorblind readers or cannot be changed, encode categories with an additional channel such as symbols, shapes, patterns, or line dashes/widths.

## Why redundant encoding protects comprehension when hue collapses <!-- role: reason -->

Color vision deficiencies can collapse hue differences, and simulations are not fully reliable for every individual; a second channel preserves category identity even when color fails.

**Mechanism:** Redundant encoding creates an alternate decoding path that does not depend on hue discrimination, improving robustness across viewers and viewing conditions.

**Evidence:** Simulators are described as helpful but not “100% correct,” and the only “bulletproof” approach presented is to encode data with a second visual variable such as position, shape, or patterns [@muth_colorblindness_2020].

**Notes:** Overusing many shapes can make a plot look like confetti, so the intent is robustness, not maximal variety [@muth_colorblindness_2020].

## When to add non-color cues <!-- role: context -->

- **User Goal:** Identify categories correctly even if colors look similar.
- **Task:** Distinguish groups/series, especially where marks overlap or are small.
- **Data:** Categorical groupings with two or more groups; potentially many series.
- **Chart Setting:** Brand palettes you must keep, thin lines, dense scatterplots, choropleth maps, or print.
- **Audience:** Readers with color vision deficiencies and mixed-ability audiences.
- **Success Criterion:** Categories are distinguishable without relying solely on the legend and hue.

## When not to add more encodings <!-- role: exceptions -->

**Break it when:** The chart is meant for a very quick “at a glance” read and extra glyph complexity would slow interpretation. **Why:** Some multi-part markers (glyphs) are described as a “slow read” for everyone [@muth_colorblindness_2020].

## Tradeoffs of double-encoding <!-- role: costs -->

**Sacrifice:** You spend visual bandwidth and may increase clutter. **Risk:** Too many shapes/patterns can overwhelm and reduce readability. **Mitigation:** Keep the number of distinct non-color forms small and consistent [@muth_colorblindness_2020].

## Common mistakes with redundant cues <!-- role: mistakes -->

- **Mistake:** Adding many different shapes for many categories. **Why it fails:** The plot can look like confetti and becomes hard to scan [@muth_colorblindness_2020].
- **Mistake:** Using patterns without checking how they change perceived brightness. **Why it fails:** Patterns can alter lightness perception and unintentionally change contrast relationships [@muth_colorblindness_2020].

## Quick checks for non-color distinguishability <!-- role: check -->

**Failure Sign:** Two categories become indistinguishable when you ignore color. **Quick Check:** Temporarily view the chart in grayscale and see if categories are still separable by shape/pattern/line style. **Stronger Test:** Have a reader identify categories using only the non-color cue, without reading a legend first [@muth_colorblindness_2020].

## What to do instead when color-only categorization fails <!-- role: fix -->

- Add symbols (for example, check marks) in tables to reinforce “good/bad” or category status [@muth_colorblindness_2020].
- Use a small set of point shapes in scatterplots to encode groups alongside color [@muth_colorblindness_2020].
- Apply patterns to map regions that would otherwise be separated only by confusing hues [@muth_colorblindness_2020].
- Use distinct line dashes and/or line widths to separate similarly bright lines where overlap occurs [@muth_colorblindness_2020].
