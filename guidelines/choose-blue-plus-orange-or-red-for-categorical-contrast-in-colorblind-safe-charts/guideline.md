---
id: choose-blue-plus-orange-or-red-for-categorical-contrast-in-colorblind-safe-charts
title: Choose blue paired with orange or red when you need two categorical colors
  that remain distinguishable for colorblind readers
bibliography: references.bib
description: Use blue as the safest hue and pair it with orange or red to preserve
  category contrast across common color vision deficiencies.
labels:
- chart:line
- task:compare
- visual:color
- impact:accessibility
- data:categorical
- audience:general
- accessibility:color-vision-deficiency
---

## Use blue paired with orange or red for two-color category encoding <!-- role: advice -->

Choose blue as one category color and pair it with orange or red when you need two categorical colors that most colorblind readers can still tell apart.

## Why blue–orange/red preserves distinguishability across color vision deficiencies <!-- role: reason -->

Color perception changes under common color vision deficiencies in ways that collapse some hue differences (especially along red–green confusions), but blue tends to remain closer to its appearance for many readers and stays separable from orange/red in multiple deficiency types.

**Mechanism:** Using a hue that stays perceptually stable (blue) and pairing it with a hue that shifts differently under deficiencies (orange/red) reduces the chance that two categories collapse into the same perceived color.

**Evidence:** Blue is presented as the “safest hue” for red-/green-blind readers, and blue paired with orange/red is described as a particularly robust two-color choice across red-, green-, and blue-blind simulations [@muth_colorblindness_2020].

**Notes:** Nearby hues (like blue/purple) can look cohesive but can collapse for colorblind readers, making categories hard to decode [@muth_colorblindness_2020].

## When to use blue plus orange/red <!-- role: context -->

- **User Goal:** Tell two groups, series, or statuses apart quickly and reliably.
- **Task:** Compare categories (e.g., two lines, two bars, two map regions).
- **Data:** Categorical or binary grouping where color is the primary differentiator.
- **Chart Setting:** Static or interactive charts where viewers may not read long legends carefully.
- **Audience:** Mixed audiences that include readers with color vision deficiencies.
- **Success Criterion:** Categories remain distinguishable without relying on perfect color vision.

## When not to rely on this pairing <!-- role: exceptions -->

**Break it when:** You must use fixed brand colors that cannot be adjusted to a blue–orange/red scheme. **Why:** You may be unable to achieve a reliable separation with color alone and will need non-color encodings [@muth_colorblindness_2020].

## Tradeoffs of standardizing on blue with orange/red <!-- role: costs -->

**Sacrifice:** You give up some freedom to use other brand or thematic hues. **Risk:** Overuse can make different charts look too similar or imply unintended semantic meaning (e.g., “good vs bad”). **Mitigation:** Keep semantics explicit with labels or symbols rather than assuming viewers infer meaning from the palette [@muth_colorblindness_2020].

## Common ways this still fails <!-- role: mistakes -->

**Mistake:** Choosing two nearby hues (e.g., blue and purple) for aesthetic cohesion. **Why it fails:** Similar hues can “torpedo” category distinguishability for red–green colorblind readers [@muth_colorblindness_2020].

## Quick checks for blue–orange/red distinguishability <!-- role: check -->

**Failure Sign:** Two categories look like the same color or nearly the same when you scan the chart quickly. **Quick Check:** View the chart in grayscale and see whether the two categories remain separable by lightness. **Stronger Test:** Run a colorblind simulation and confirm the two categories remain distinct under multiple deficiency types [@muth_colorblindness_2020].

## What to do if you can’t use blue–orange/red or it still isn’t clear <!-- role: fix -->

- Use two colors that differ strongly in lightness so the chart remains readable in black and white [@muth_colorblindness_2020].
- Add a second visual encoding such as line dashes/widths, symbols, or patterns so color is not the only cue [@muth_colorblindness_2020].
- Replace a legend-driven design with direct labels on the marks to reduce reliance on color decoding [@muth_colorblindness_2020].
- Reduce the number of colored categories and highlight only the most important values while toning down the rest [@muth_colorblindness_2020].
