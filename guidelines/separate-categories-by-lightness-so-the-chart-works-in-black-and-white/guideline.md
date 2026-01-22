---
id: separate-categories-by-lightness-so-the-chart-works-in-black-and-white
title: Separate category colors by lightness so the chart remains readable in black
  and white
bibliography: references.bib
description: Ensure colors differ in brightness so categories remain distinguishable
  for colorblind readers and in grayscale.
labels:
- chart:bar
- task:compare
- visual:color
- impact:accessibility
- data:categorical
- audience:general
- accessibility:color-vision-deficiency
---

## Make color choices that still work in grayscale <!-- role: advice -->

Choose colors that differ clearly in lightness so the visualization remains readable when viewed in black and white.

## Why lightness contrast survives color vision deficiencies <!-- role: reason -->

Many color vision deficiencies reduce or remove discrimination between certain hues, but differences in perceived brightness remain a reliable cue that can keep categories separable even when hue cues collapse.

**Mechanism:** When hue distinctions become ambiguous, viewers can still parse marks by relative lightness, preserving grouping and decoding.

**Evidence:** The guideline “get it right in black & white” is presented as a practical way to make charts readable for colorblind readers, and yellow is highlighted as often effective because it is very light relative to other hues [@muth_colorblindness_2020].

**Notes:** Using red/green can still work for distinguishability if their lightness differs, but colorblind readers may not perceive the intended “good/bad” semantics from hue alone [@muth_colorblindness_2020].

## When grayscale robustness is the right target <!-- role: context -->

- **User Goal:** Distinguish groups quickly without misreading categories.
- **Task:** Identify, compare, or track multiple categories in the same view.
- **Data:** Categorical series, segmented bars/areas, or grouped marks.
- **Chart Setting:** Screens with low contrast, printouts, small marks (thin lines), or mobile viewing.
- **Audience:** General audiences including older readers and people with color vision deficiencies.
- **Success Criterion:** Categories remain distinct under grayscale viewing and common colorblind conditions.

## When not to depend on lightness alone <!-- role: exceptions -->

**Break it when:** Your marks are so thin or dense that even lightness differences are hard to see. **Why:** Fine detail can erase effective contrast, requiring additional encodings like labels, patterns, or line styles [@muth_colorblindness_2020].

## Tradeoffs of prioritizing lightness contrast <!-- role: costs -->

**Sacrifice:** Some palettes will look less “on brand” or less harmonious. **Risk:** Large lightness gaps can overemphasize some categories visually. **Mitigation:** Pair lightness differences with direct labeling so attention follows meaning, not just contrast [@muth_colorblindness_2020].

## Common mistakes with lightness-based safety <!-- role: mistakes -->

- **Mistake:** Using a vibrant hue that appears strong to you but has low lightness contrast against its background. **Why it fails:** It can become barely visible for some colorblind readers, especially when the hue difference is the main cue [@muth_colorblindness_2020].
- **Mistake:** Treating red and green as inherently “good vs bad” without other cues. **Why it fails:** Colorblind readers may not read that semantic mapping from hue and will see them as different shades rather than opposites [@muth_colorblindness_2020].

## Quick checks for lightness separability <!-- role: check -->

**Failure Sign:** Categories merge when you squint or when the chart is small. **Quick Check:** Convert the visualization to grayscale and confirm categories are still separable. **Stronger Test:** Use a colorblind simulator and verify that category differences remain visible without relying on hover or tooltips [@muth_colorblindness_2020].

## What to do if lightness separation isn’t enough <!-- role: fix -->

- Add direct labels to series/segments to remove reliance on legend decoding [@muth_colorblindness_2020].
- Use symbols or shapes to double-encode categories where color is ambiguous [@muth_colorblindness_2020].
- Use dashes and varying line widths in line charts to separate similarly bright series [@muth_colorblindness_2020].
- Reduce the number of colored categories and group or mute the remainder [@muth_colorblindness_2020].
