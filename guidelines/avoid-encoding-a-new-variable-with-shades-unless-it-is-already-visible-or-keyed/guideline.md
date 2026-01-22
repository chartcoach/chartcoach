---
id: avoid-encoding-a-new-variable-with-shades-unless-it-is-already-visible-or-keyed
title: Use shades to double-encode an already-visible order (not to introduce a new
  variable)
bibliography: references.bib
description: Avoid using a quantitative color scale to encode a second, otherwise
  hidden variable unless the value is already visible or strongly keyed elsewhere.
labels:
- chart:general
- task:compare
- visual:color
- impact:clarity
- data:multivariate
- audience:general
- complexity:intermediate
---

## Use shades to double-encode an already-visible order (not to introduce a new variable) <!-- role: advice -->

Use shades to reinforce an order that is already visible from position, size, sorting, or explicit labeling, and avoid using shades as the only encoding for an additional variable. If you do encode a new variable with shades, make it immediately obvious what the colors refer to via strong visual “keys” in the same view.

## Why double-encoding works better than “color as a side channel” <!-- role: reason -->

Color is easy to notice but hard to quantify precisely, so using it as the sole carrier of a second dimension can overload readers and make the chart slow to decode. When the value is already perceptible without color, shades act as reinforcement rather than a puzzle.

**Mechanism:** Double-encoding (e.g., size plus shade, or x-position plus shade) reduces decoding effort because the reader can infer meaning without relying on color alone; a “side-gig” color encoding is often missed or misread.

**Evidence:** Adding a new variable via color in many chart types makes the chart hard to read, whereas using shades to reinforce values already visible (or providing strong within-chart color keys such as companion views) supports comprehension; scatter plots are highlighted as a case where a second variable in color can work better, especially when keyed by other elements [@muth_quantitative_vs_qualitative_2021].

**Notes:** The core issue is not “two variables are always bad,” but whether viewers can quickly detect what color is encoding.

## When this applies: deciding whether color should encode another variable <!-- role: context -->

- **User Goal:** Communicate a multivariate story without making the chart hard to decode.
- **Task:** Compare groups while also understanding an ordering or intensity dimension.
- **Data:** Two or more variables per mark (category + value + secondary attribute).
- **Chart Setting:** Commonly affected in treemaps, grouped bars, line charts, and scatter plots.
- **Audience:** Readers skimming quickly, with limited patience for decoding legends.
- **Success Criterion:** The meaning of color is obvious and the chart remains quickly readable.

## When not to follow it <!-- role: exceptions -->

- **Break it when:** The chart type supports “color as an attribute” reading and the view provides strong in-context keys for the color meaning (for example, companion panels that effectively teach the palette). **Why:** Readers can learn the mapping from nearby, redundant cues and then apply it reliably [@muth_quantitative_vs_qualitative_2021].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may forgo showing an extra variable directly in the same chart. **Risk:** If you rely on color alone for a new variable, many readers will not notice it or will misattribute what it means. **Mitigation:** Prefer redundancy (position/order/labels) so color reinforces rather than replaces the encoding [@muth_quantitative_vs_qualitative_2021].

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Encoding a second variable only in color in a chart where color already identifies categories (for example, grouped bars where hue already labels groups). **Why it fails:** Readers don’t expect color to carry two meanings at once and will miss the “side-gig” encoding [@muth_quantitative_vs_qualitative_2021].
- **Mistake:** Using shades to encode a hidden order while the visual ordering is inconsistent (for example, line ranks that change position without stable ordering). **Why it fails:** The chart offers no stable scaffold for interpreting the shading as rank [@muth_quantitative_vs_qualitative_2021].

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers can’t tell what the colors mean without reading the legend carefully, or they misinterpret color as group identity instead of magnitude. **Quick Check:** Temporarily remove the legend and ask whether the chart still suggests what color is encoding; if not, the color channel is doing too much. **Stronger Test:** Ask a test reader to describe the role of color after a five-second glance; if they can’t, add redundancy or drop the extra encoding [@muth_quantitative_vs_qualitative_2021].

## What to do instead <!-- role: fix -->

- Use shades to reinforce a value already evident through size, position, or sorting (for example, treemap box size and shade aligned) [@muth_quantitative_vs_qualitative_2021].
- Add in-chart keys that teach the palette (for example, a companion view where the same colors are also encoded by position) when color must carry an extra variable [@muth_quantitative_vs_qualitative_2021].
- Reduce the number of simultaneously encoded variables by splitting into small multiples or separate charts when decoding becomes slow [@muth_quantitative_vs_qualitative_2021].
- Directly label categories so color is freed to reinforce ordering rather than identify groups [@muth_quantitative_vs_qualitative_2021].
