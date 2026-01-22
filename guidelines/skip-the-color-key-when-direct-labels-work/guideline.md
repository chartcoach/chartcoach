---
id: skip-the-color-key-when-direct-labels-work
title: Replace the color key with direct labels when categories can be labeled in
  the chart
bibliography: references.bib
description: Use direct labels instead of a legend when you can label the colored
  elements where they appear.
labels:
- chart:multiple
- task:identify
- visual:color
- impact:clarity
- data:categorical
- audience:novice
- complexity:basic
---

## Prefer direct labels over a color key when labels fit near the marks <!-- role: advice -->

Replace the color key with direct labels on or next to the colored elements whenever you can label them without clutter or ambiguity.

## Direct labeling removes the legend lookup step <!-- role: reason -->

A color key forces readers to bounce between legend and marks to translate color into meaning. Direct labels eliminate this translation step, making it easier to start reading and harder to misunderstand which color refers to which category.

**Mechanism:** Removing the “match this color to that label” step reduces visual search and working-memory load, so readers can interpret the chart directly.

**Evidence:** Direct labels are presented as a way to avoid needing a color key when an explanation can be placed on the marks themselves [@muth_color_keys_2023].

**Notes:** When direct labels are hard to place (e.g., dense lines), pointers or callouts can support them without reintroducing a full legend.

## When direct labels are the right substitute for a legend <!-- role: context -->

- **User Goal:** Identify what each colored mark represents quickly.
- **Task:** Match categories to colored marks with minimal effort.
- **Data:** Categorical series or groups with names that can be displayed near marks.
- **Chart Setting:** Static or interactive charts where labels can be placed without overlap.
- **Audience:** Broad audiences who may not invest effort in legend decoding.
- **Success Criterion:** Readers can understand the mapping from color to meaning at a glance.

## When not to use direct labels instead of a color key <!-- role: exceptions -->

**Break it when:** The chart is too dense to label clearly (e.g., many overlapping elements) or labels would obscure the data. **Why:** Direct labeling would create clutter and reduce readability more than a color key would [@muth_color_keys_2023].

## Tradeoffs of direct labeling <!-- role: costs -->

**Sacrifice:** You give up space inside the plotting area and may need more careful layout. **Risk:** Labels can overlap, hide data, or introduce ambiguity if they are not placed close enough to their marks. **Mitigation:** Use selective labeling or callouts for the most important elements.

## Common ways this goes wrong <!-- role: mistakes -->

**Mistake:** Adding direct labels but keeping a full color key anyway. **Why it fails:** It duplicates information, consumes space, and can make the graphic feel more complex than necessary [@muth_color_keys_2023].

## Quick tests for whether direct labeling is working <!-- role: check -->

**Failure Sign:** Readers still need to scan back and forth to decode colors, or labels collide with marks. **Quick Check:** If you hide the legend, can a reader still name what each color represents from the labels alone? **Stronger Test:** Ask someone to interpret the chart in a few seconds; note whether they hesitate looking for a legend.

## What to do instead if direct labels won’t fit <!-- role: fix -->

- Use a compact color key but keep it close to the colored elements it explains.
- Label only the most important categories directly and keep the rest in a key.
- Add pointers or small callouts for hard-to-label elements (e.g., crowded lines).
- Reduce the number of categories shown or split the view into small multiples.
