---
id: prefer-rainbow-isarithmic-over-rainbow-choropleth-for-determining-range-in-quantitative-maps
title: Prefer a rainbow isarithmic scheme over a rainbow choropleth scheme for determining
  range in quantitative maps
bibliography: references.bib
description: For determining the span of values in quantitative maps, a rainbow isarithmic
  condition outperformed a rainbow choropleth condition in accuracy.
labels:
- chart:map
- task:determine-range
- visual:color
- impact:accuracy
- data:quantitative
- audience:novice
- domain:cartography
---

## Use RC-Isa rather than RC-Choro for range judgments <!-- role: advice -->

If you are using a rainbow color scheme and the user task is to determine the range (span) of values, use an isarithmic-style map condition rather than a choropleth-style one.

## Why isarithmic can help range judgments under a rainbow palette <!-- role: reason -->

Range judgments depend on perceiving the overall span of encoded values, which can be influenced by how ordered color transitions appear across space.

**Mechanism:** A representation where colors appear in an ordered spatial progression can make it easier to perceive the extent of values present than when colors are spatially fragmented.

**Evidence:** For determine-range accuracy, the ranking placed rainbow-isarithmic above rainbow-choropleth, and the significance pairs included rainbow-isarithmic outperforming rainbow-choropleth [@golbiowskaRainbowDashIntuitiveness2022]. This task- and design-specific ranking is included as part of a structured collation to support visualization recommendation rules [@zengReviewCollationGraphical2023].

**Notes:** This is a conditional guideline that applies only when a rainbow scheme is already chosen.

## When determining range applies <!-- role: context -->

- **User Goal:** Understand the minimum-to-maximum span present in the data shown.
- **Task:** Determine range.
- **Data:** Quantitative values encoded via ordered color classes.
- **Chart Setting:** Static map-like display; rainbow palette in use.
- **Audience:** General audiences or learners reading maps.
- **Success Criterion:** Higher accuracy in identifying the value span.

## When not to follow this range rule <!-- role: exceptions -->

**Break it when:** The task is to find extrema quickly and you are free to change the palette type. **Why:** Sequential schemes outperform rainbow schemes for extrema-finding in the same experimental context.

## Tradeoffs of using RC-Isa over RC-Choro <!-- role: costs -->

**Sacrifice:** You may lose the discrete regional boundary emphasis that choropleths provide.\
**Risk:** Users may still not interpret rainbow hues as globally ordered, affecting other ordered judgments.\
**Mitigation:** Make the legend explicit and consider adding numeric annotations for endpoints.

## Common mistakes in range tasks with color <!-- role: mistakes -->

**Mistake:** Keeping the same palette and assuming map type cannot affect range judgments. **Why it fails:** Accuracy differed between isarithmic and choropleth conditions under the rainbow scheme.

## Quick tests for range comprehension <!-- role: check -->

**Failure Sign:** Users report a narrower or wider span than what is actually shown, despite having a legend.\
**Quick Check:** Ask users to state the minimum and maximum values present; compare to the ground truth.\
**Stronger Test:** Run a brief accuracy check across choropleth vs isarithmic renderings using the same palette.

## What to do instead if RC-Isa is not feasible <!-- role: fix -->

- Switch from choropleth to an isarithmic/continuous-field rendering if your data and interpolation support it.
- Add explicit min/max callouts and a clearly labeled legend to support the range judgment.
- If the range task is central, switch to a sequential saturation palette rather than relying on hue order.
- Provide a separate numeric summary of min and max alongside the map to reduce dependence on color interpretation.
