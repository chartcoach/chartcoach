---
id: use-fewer-colors-by-switching-encodings
title: Replace categorical color encoding with other encodings whenever position,
  labels, or interaction can carry identity
bibliography: references.bib
description: Reduce category colors by relying on non-color encodings (position, labeling,
  grouping, and interaction) to distinguish categories.
labels:
- chart:categorical
- task:compare
- visual:color
- impact:clarity
- data:categorical
- audience:novice
- complexity:intermediate
---

## Reduce category colors by switching encodings away from color <!-- role: advice -->

Use fewer colors by encoding category identity with position, direct labels, grouping, shape/line style, or interaction, and reserve distinct hues for categories that truly need emphasis.

## Why switching encodings reduces reliance on many colors <!-- role: reason -->

Using fewer hues reduces confetti-like appearance and can improve legibility, especially when many categories compete for attention; distinctness can be maintained by other channels like position, labeling, or line style.

**Mechanism:** Viewers can distinguish categories through separations in space (position and gaps), explicit text (direct labels), structural grouping (totals and “Other”), and non-color marks (strokes, dashes, widths, symbols), so color no longer has to do all the identification work.

**Evidence:** A set of practical techniques reduces the number of distinct hues needed by shifting category identification to other visual variables (position, labels, grouping, strokes, patterns, line dashes/widths) and to interaction (tooltips/hover), while reserving color for emphasis and key categories [@muth_fewer_colors_2022].

**Notes:** Shades (light/dark of one hue) can reduce “confetti” but also shift attention from parts to totals.

## When this applies: too many categorical colors in one view <!-- role: context -->

- **User Goal:** Understand or communicate patterns without overwhelming readers with many category colors.
- **Task:** Identify, track, or compare categories and their values/trends.
- **Data:** Many categories (often 10+), especially when some are small or secondary.
- **Chart Setting:** Static or interactive charts/maps/tables where space for legends and labels is limited.
- **Audience:** Mixed audiences including colorblind readers; readers who may not know the categories in advance.
- **Success Criterion:** Categories remain distinguishable and the main message is clear with fewer distinct hues.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Parts are as important as totals in a composition chart and using shades would reduce part distinctness. **Why:** Shades make adjacent segments harder to tell apart and can shift focus toward totals over parts [@muth_fewer_colors_2022].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Some alternatives (direct labels, small multiples) require more space and design effort. **Risk:** Overusing non-color indicators (too many shapes, patterns, dash types) can create a new decoding burden. **Mitigation:** Keep the number of non-color variants small and prioritize labeling or structural changes instead [@muth_fewer_colors_2022].

## Common failure modes when trying to “use fewer colors” <!-- role: mistakes -->

- **Mistake:** Keeping many categories but only switching them to many similar shades. **Why it fails:** Similar lightness values are hard to discriminate, especially in dense charts [@muth_fewer_colors_2022].
- **Mistake:** Relying on tooltips for key categories. **Why it fails:** Tooltips show one label at a time and slow searching/comparison of important items [@muth_fewer_colors_2022].

## Quick tests <!-- role: check -->

**Failure Sign:** The chart looks like “confetti,” and readers must constantly consult a legend to identify categories. **Quick Check:** Temporarily set all categories to one neutral color and see if the chart is still understandable via position/gaps/labels. **Stronger Test:** Ask a new reader to find and compare two specific categories quickly without using the legend [@muth_fewer_colors_2022].

## What to do instead <!-- role: fix -->

- Give identical or near-identical colors to marks already separated by position (for example, simple bar charts) and rely on spacing to distinguish them [@muth_fewer_colors_2022].
- Directly label lines/areas/bars so categories can share similar colors without losing identification [@muth_fewer_colors_2022].
- Merge minor categories into an “Other” group or aggregate to higher-level groupings to reduce the number of distinct categories shown [@muth_fewer_colors_2022].
- Switch to a chart type or layout that uses position rather than color for categories, or split into small multiples when tracking many series in one plot becomes unreadable [@muth_fewer_colors_2022].
