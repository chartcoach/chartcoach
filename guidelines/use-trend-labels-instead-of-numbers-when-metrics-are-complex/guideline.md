---
id: use-trend-labels-instead-of-numbers-when-metrics-are-complex
title: "Use qualitative trend labels (e.g., \u201Cless/more\u201D) in quantitative\
  \ color keys when numbers distract"
bibliography: references.bib
description: Replace detailed numeric legend labels with simple directional labels
  when exact values are not essential.
labels:
- chart:map
- task:understand
- visual:color
- impact:clarity
- data:quantitative
- audience:novice
- complexity:intermediate
---

## Use “less/more” style labels when exact values are unnecessary for understanding <!-- role: advice -->

If numeric values and units in a quantitative color key would require lots of explanation and aren’t necessary for the takeaway, label the key with a qualitative direction such as “less/more” or “worse/better.”

## Simplified legends help readers grasp the main pattern <!-- role: reason -->

Some metrics are complex or unfamiliar, and detailed numeric labels can add cognitive burden without improving comprehension of the main trend. A directional label can communicate what the colors mean while keeping attention on the spatial or overall pattern.

**Mechanism:** Directional labeling reduces interpretive overhead and focuses the reader on relative differences rather than exact decoding.

**Evidence:** Omitting values and units in favor of general “less/more” style labels is presented as a useful simplification when exact numeric interpretation is not needed and explanation would distract [@muth_color_keys_2023].

**Notes:** This approach is especially compatible with interactive graphics where exact values can be revealed on demand.

## When qualitative legend labels are a good fit <!-- role: context -->

- **User Goal:** Understand overall patterns, hotspots, or relative intensity.
- **Task:** Compare areas by “more vs less” rather than read precise values.
- **Data:** Quantitative measures that are hard to explain succinctly or not central to the message.
- **Chart Setting:** Complex visuals; interactive maps with tooltips; space-constrained layouts.
- **Audience:** General audiences who may not know the metric or units.
- **Success Criterion:** Readers correctly interpret direction and meaning without needing to parse technical labels.

## When not to replace numeric labels with qualitative ones <!-- role: exceptions -->

**Break it when:** The story requires precise numeric reading from the legend (e.g., thresholds, compliance cutoffs, exact ranges). **Why:** Qualitative labels can’t support exact interpretation [@muth_color_keys_2023].

## Tradeoffs of qualitative legend labeling <!-- role: costs -->

**Sacrifice:** Numerical precision and transparency about units/ranges are reduced. **Risk:** Readers may over-interpret small differences as meaningful without seeing the scale. **Mitigation:** Pair with clear text annotation or provide values elsewhere (e.g., tooltips or a small table).

## Common over-simplification mistakes <!-- role: mistakes -->

**Mistake:** Using “less/more” labels while the chart text still implies exact numeric thresholds. **Why it fails:** The legend no longer supports the claims the reader is asked to verify [@muth_color_keys_2023].

## Quick checks for adequacy of qualitative labels <!-- role: check -->

**Failure Sign:** Readers ask “less of what, exactly?” or can’t tell what is being measured. **Quick Check:** Can a reader restate the meaning of the colors in one sentence without mentioning numbers? **Stronger Test:** Ask a reader what decision the map supports; if they need numbers to answer, keep numeric labels.

## What to do instead when you need both simplicity and specificity <!-- role: fix -->

- Keep numeric labels but reduce them to key anchor values (e.g., min/median/max).
- Add a brief explanation of the metric in annotation near the legend.
- Provide both a qualitative direction and a few numeric anchors to ground interpretation.
- Use interaction to show exact values on hover while keeping the static legend minimal.
