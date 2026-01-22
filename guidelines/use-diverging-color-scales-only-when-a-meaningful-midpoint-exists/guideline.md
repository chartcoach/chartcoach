---
id: use-diverging-color-scales-only-when-a-meaningful-midpoint-exists
title: Use a diverging color scale only when your data has a meaningful midpoint
bibliography: references.bib
description: Apply a diverging palette when values meaningfully split into two directions
  around a central reference such as zero or neutral.
labels:
- chart:general
- task:compare
- visual:color
- impact:clarity
- data:quantitative
- audience:general
- complexity:basic
---

## Use a diverging scale only for two-sided meaning around a middle value <!-- role: advice -->

Use a diverging color scale when the data has a meaningful midpoint and values on both sides should be read as opposite directions (e.g., negative vs positive or disagree vs agree). Otherwise, use a sequential scale to communicate simple low-to-high magnitude [@muth_which_color_scale_2021].

## Diverging palettes encode direction, not just magnitude <!-- role: reason -->

A diverging scale visually asserts that the midpoint is special and that deviations to either side have different meaning. Without a meaningful midpoint, the two hues can imply an artificial split and encourage readers to interpret directionality where none exists.

**Mechanism:** A bright center plus two hue directions makes viewers look for a reference point and interpret colors as “above vs below” rather than “less vs more.”

**Evidence:** Diverging scales are described as gradients with a bright middle value that go darker toward both ends in different hues, commonly used for negative/positive values, election results, or Likert-style responses [@muth_which_color_scale_2021].

**Notes:** Diverging scales can be classed or unclassed; the key requirement is the meaningful midpoint.

## When your variable is centered and two directions matter <!-- role: context -->

- **User Goal:** See which items fall on either side of a reference point and how far they deviate.
- **Task:** Detect sign/direction (above/below) and compare deviation magnitude.
- **Data:** Quantitative values with a semantic center (e.g., 0, average, neutral response).
- **Chart Setting:** Maps or charts where color carries the burden of showing directionality.
- **Audience:** General readers who will infer meaning from the midpoint cue.
- **Success Criterion:** Viewers correctly read both direction (side of midpoint) and intensity (distance from midpoint).

## When a midpoint is arbitrary <!-- role: exceptions -->

**Break it when:** The midpoint is only a convenient numeric value (e.g., the median) and does not carry distinct semantic meaning for the reader. **Why:** The diverging split can overemphasize the center and mislead interpretation about “two sides” [@muth_which_color_scale_2021].

## Tradeoffs of diverging palettes <!-- role: costs -->

**Sacrifice:** You give up a single continuous “low-to-high” read and add cognitive work to interpret two hue families. **Risk:** A poorly chosen midpoint can bias attention toward the split rather than the overall distribution. **Mitigation:** Ensure the midpoint is explicitly meaningful in your framing and labeling.

## Common misuses of diverging scales <!-- role: mistakes -->

**Mistake:** Using a diverging palette for values that only vary from low to high with no directional meaning. **Why it fails:** It implies a qualitative difference between “low side” and “high side” that is not actually present [@muth_which_color_scale_2021].

## Quick checks for whether you need diverging <!-- role: check -->

**Failure Sign:** You cannot explain in a short phrase what the center color means (e.g., “neutral” or “zero change”). **Quick Check:** Ask, “Do values on either side of the midpoint mean opposite things?” **Stronger Test:** Remove the midpoint label; if the chart becomes ambiguous or misleading, the midpoint likely needs clearer justification or a sequential scale.

## What to do instead if there is no meaningful midpoint <!-- role: fix -->

- Switch to a sequential color scale that runs from light to dark to encode increasing magnitude.
- Reframe the measure so a meaningful reference point exists (e.g., convert to change from baseline) before using a diverging scale.
- If the story is about a specific threshold, keep a sequential scale and highlight the threshold range rather than splitting the entire palette.
- Add clear labeling of the reference point if you keep a diverging scale because direction is essential.
