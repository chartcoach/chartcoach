---
id: make-nonlinear-or-uneven-color-classes-obvious-in-the-legend
title: Visually encode uneven or non-linear class ranges in quantitative color keys
bibliography: references.bib
description: When class ranges are uneven, show that unevenness directly in the legend
  through labels and proportional widths.
labels:
- chart:map
- task:interpret
- visual:color
- impact:trust
- data:quantitative
- audience:novice
- complexity:advanced
---

## Show non-linear class ranges explicitly in the color key design <!-- role: advice -->

If your quantitative color scale uses uneven class ranges or a non-linear interpolation, make that obvious in the legend with clear min/max labeling and, when possible, proportional class widths.

## Uneven ranges can mislead unless the legend signals them <!-- role: reason -->

When legend steps look equal, readers may assume each color covers the same numeric interval. If the underlying classing is uneven, failing to show it can distort interpretation of how much change each step represents.

**Mechanism:** Proportional legend segments and explicit anchors align the visual appearance of the key with the numeric structure of the scale, reducing false assumptions.

**Evidence:** Non-linear or uneven class structures should be communicated clearly, including labeling min/max when needed and using different class widths to reflect unequal ranges [@muth_color_keys_2023].

**Notes:** Proportional segment widths can also make the legend more visually engaging while improving honesty.

## When proportional or explicit legends are necessary <!-- role: context -->

- **User Goal:** Understand what numeric ranges each color represents.
- **Task:** Interpret thresholds and relative magnitude from a classed legend.
- **Data:** Classed sequential/diverging scales with unequal bin widths or non-linear steps.
- **Chart Setting:** Static maps or charts where legend is the primary guide to values.
- **Audience:** Readers likely to assume equal steps unless shown otherwise.
- **Success Criterion:** Readers do not misinterpret the scale as linear or evenly classed.

## When not to use proportional widths in the legend <!-- role: exceptions -->

**Break it when:** The legend would be confused with a distribution display (e.g., mistaken for a histogram) in your specific layout and context. **Why:** Readers might read segment widths as frequency instead of numeric span [@muth_color_keys_2023].

## Tradeoffs of proportional legend segments <!-- role: costs -->

**Sacrifice:** Layout simplicity and space; proportional legends often need more room. **Risk:** Readers may confuse proportional widths with data distribution if other cues resemble a histogram. **Mitigation:** Keep the legend visually distinct from distribution plots and label ranges clearly.

## Common ways uneven scales get obscured <!-- role: mistakes -->

**Mistake:** Using equal-width legend blocks for unequal numeric ranges without explicit anchors. **Why it fails:** Readers infer a linear/equal-step scale and misjudge the meaning of color changes [@muth_color_keys_2023].

## Quick checks for honesty about non-linearity <!-- role: check -->

**Failure Sign:** The legend looks evenly stepped but the bins are not. **Quick Check:** Compare each class’s numeric span; if spans differ, the legend should not look uniform. **Stronger Test:** Ask a reader what numeric difference one step represents; if they answer “the same each time,” your legend is undersignaling unevenness.

## What to do instead if proportional widths won’t fit <!-- role: fix -->

- Add explicit min and max labels (and key breakpoints) even if you keep equal-width blocks.
- Reduce the number of classes so labels can clearly communicate the uneven steps.
- Add a brief annotation describing the non-linear scaling or binning logic.
- Switch to a continuous scale with ticks if uneven classing isn’t essential to the message.
