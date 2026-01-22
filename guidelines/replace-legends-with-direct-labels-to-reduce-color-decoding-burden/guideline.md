---
id: replace-legends-with-direct-labels-to-reduce-color-decoding-burden
title: Replace legends with direct labels when color decoding would slow down colorblind
  readers
bibliography: references.bib
description: Label lines, areas, and slices directly to avoid legend lookups that
  are harder under color vision deficiencies.
labels:
- chart:line
- task:identify
- visual:text
- impact:clarity
- data:categorical
- audience:general
- accessibility:color-vision-deficiency
---

## Label series and categories directly instead of relying on a color key <!-- role: advice -->

Use direct labels on the marks (such as at the end of lines or inside slices) so readers do not need to decode categories through a color legend.

## Why direct labels reduce errors from ambiguous colors and legend matching <!-- role: reason -->

Legend decoding requires matching a mark to a legend swatch by color, which becomes slower and more error-prone when colors are hard to distinguish; direct labels remove the matching step and make identification immediate.

**Mechanism:** Direct labeling turns category identification into reading text at the mark, avoiding hue discrimination and reducing visual search between plot and legend.

**Evidence:** Color keys are described as difficult for colorblind people to decipher, and direct labeling is recommended as a way to get rid of legends and save readers time broadly, not only for colorblind audiences [@muth_colorblindness_2020].

**Notes:** This is especially relevant in line, area, and pie/donut-style charts where legends are common [@muth_colorblindness_2020].

## When direct labels are most useful <!-- role: context -->

- **User Goal:** Identify which series or segment corresponds to which category quickly.
- **Task:** Identify categories and compare values across series.
- **Data:** A small to moderate number of series/segments that can be labeled without excessive overlap.
- **Chart Setting:** Static charts, presentations, print, and mobile where legend lookups are costly.
- **Audience:** Broad audiences, including people with color vision deficiencies.
- **Success Criterion:** Viewers can identify categories without scanning back and forth to a legend.

## When direct labels may be the wrong choice <!-- role: exceptions -->

**Break it when:** There are too many series or segments to label without collisions or clutter. **Why:** Labels can overlap and reduce overall readability, undermining the goal [@muth_colorblindness_2020].

## Tradeoffs of direct labeling <!-- role: costs -->

**Sacrifice:** You spend space and may need careful label placement. **Risk:** Labels can clutter dense charts and distract from the data. **Mitigation:** Reduce the number of emphasized series or simplify the chart so labels remain legible [@muth_colorblindness_2020].

## Common mistakes when switching to direct labels <!-- role: mistakes -->

**Mistake:** Keeping the legend and adding many labels everywhere. **Why it fails:** Redundant labeling can create clutter without improving identification [@muth_colorblindness_2020].

## Quick checks for legend dependence <!-- role: check -->

**Failure Sign:** You cannot name a series/category without consulting the legend. **Quick Check:** Hide the legend and see whether categories are still identifiable from labels. **Stronger Test:** Ask someone to identify a series within a few seconds without using the legend [@muth_colorblindness_2020].

## What to do if direct labels don’t fit <!-- role: fix -->

- Reduce the number of categories shown at once and group or mute less important ones [@muth_colorblindness_2020].
- Add interaction-based identification (hover tooltips or highlight-on-hover) for web charts where labels would clutter [@muth_colorblindness_2020].
- Double-encode categories with shapes, patterns, or line styles so a small legend is still usable [@muth_colorblindness_2020].
- Switch to a chart type that naturally supports labeling categories (for example, bars with category names) [@muth_colorblindness_2020].
