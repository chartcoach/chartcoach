---
id: reduce-the-number-of-colors-and-highlight-only-key-values-for-colorblind-accessibility
title: Reduce the number of colors and highlight only key values when many categories
  would be hard to distinguish
bibliography: references.bib
description: Use fewer colored categories and reserve color emphasis for the main
  insight to keep charts readable for colorblind readers.
labels:
- chart:bar
- task:focus
- visual:color
- impact:clarity
- data:categorical
- audience:general
- accessibility:color-vision-deficiency
---

## Use fewer distinct colors and reserve emphasis for what matters most <!-- role: advice -->

Limit the number of distinct category colors and use color primarily to highlight the most important values while muting or grouping the rest.

## Why fewer colors reduces confusion for everyone, especially colorblind readers <!-- role: reason -->

As the number of categories increases, the chance that two colors look similar rises, and decoding becomes more effortful; simplifying the palette lowers perceptual load and makes the intended takeaway easier to spot.

**Mechanism:** Reducing competing color signals increases separability and decreases the need to constantly refer to legends, improving fast scanning.

**Evidence:** Using many colors (more than a few) is described as more likely to cause viewers with color vision deficiencies to tune out unless other indicators like annotations are used, and focusing color on one or two insights is recommended [@muth_colorblindness_2020].

**Notes:** Choosing chart types that rely less on color and more on direct labeling can further reduce dependence on multi-color palettes [@muth_colorblindness_2020].

## When “fewer colors” is the right design move <!-- role: context -->

- **User Goal:** Understand the main message without decoding many categories.
- **Task:** Identify key values, compare a few focal groups, or see a standout.
- **Data:** Many categories or series, especially with small marks or thin lines.
- **Chart Setting:** Static charts, small multiples, dashboards, or mobile layouts.
- **Audience:** Broad audiences that include colorblind readers and skimmers.
- **Success Criterion:** The main insight is detectable at a glance and categories remain distinguishable.

## When not to downplay categories with muted color <!-- role: exceptions -->

**Break it when:** Every category is equally important and must be compared with equal salience. **Why:** Selective highlighting can bias attention and distort what viewers treat as important [@muth_colorblindness_2020].

## Tradeoffs of using fewer colors and selective highlighting <!-- role: costs -->

**Sacrifice:** You may lose immediate visual differentiation for all categories at once. **Risk:** Viewers may assume muted categories are unimportant even if they are merely “context.” **Mitigation:** Make the intended focus explicit with text labels or annotations [@muth_colorblindness_2020].

## Common mistakes when reducing colors <!-- role: mistakes -->

- **Mistake:** Keeping many categories but switching to a “safer” palette without reducing count. **Why it fails:** Distinguishability problems persist when too many colors compete, especially for colorblind readers [@muth_colorblindness_2020].
- **Mistake:** Highlighting multiple “important” categories with similar brightness. **Why it fails:** The emphasis collapses and the chart loses a clear focal point for quick scanning [@muth_colorblindness_2020].

## Quick checks for “too many colors” <!-- role: check -->

**Failure Sign:** You need the legend constantly to know what you’re looking at. **Quick Check:** Count distinct hues used for categories; if it feels crowded beyond a few, try removing or grouping categories. **Stronger Test:** Ask a reader to state the main takeaway in a few seconds without using the legend [@muth_colorblindness_2020].

## What to do instead of relying on many category colors <!-- role: fix -->

- Switch to a chart type that labels values directly (for example, bars with category labels) instead of using many colors [@muth_colorblindness_2020].
- Group minor categories into an “other” category or mute them to a neutral tone [@muth_colorblindness_2020].
- Use direct labels for series and remove the color key where possible [@muth_colorblindness_2020].
- Add a second encoding (symbols, line dashes, patterns) for categories that must remain distinct [@muth_colorblindness_2020].
