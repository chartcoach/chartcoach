---
id: explicitly-define-what-color-encodes-with-a-legend-or-direct-labeling
title: Explicitly define what color encodes with a legend or direct labeling
bibliography: references.bib
description: Explain color encodings so readers know what the hues and shades mean.
labels:
- chart:multi
- task:decode
- visual:color
- impact:clarity
- data:categorical
- audience:novice
- complexity:basic
---

## Make color meaning explicit in the chart itself <!-- role: advice -->

Always explain what your colors encode by providing a clear color key or an equivalent labeling approach in the graphic.

## Why unexplained color becomes ambiguous <!-- role: reason -->

Color can represent categories, values, interaction states, or emphasis; without an explicit mapping, readers must guess, which invites misunderstanding.

**Mechanism:** A visible mapping turns color from decoration into an interpretable variable, reducing cognitive load and preventing incorrect inferences.

**Evidence:** Every visual mark that represents a value or variable should be explained, and the same is true for colors; a color key can be created in multiple ways [@muth_colors_2018].

**Notes:** The explanation can take different forms (e.g., a key), but it must be present and legible.

## When this applies to color encodings <!-- role: context -->

- **User Goal:** Correctly interpret what each colored mark represents.
- **Task:** Map visual appearance (hue/shade) to a category or value range.
- **Data:** Any chart where color carries meaning (not just visibility).
- **Chart Setting:** Static or interactive charts where color encodes data, state, or emphasis.
- **Audience:** Readers unfamiliar with your internal conventions.
- **Success Criterion:** The mapping from color to meaning is unambiguous without external explanation.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Color is purely decorative and does not encode any data or state. **Why:** If color carries no meaning, a key would add unnecessary clutter [@muth_colors_2018].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Keys and labels take space and can add visual elements. **Risk:** A poorly placed or overly complex key can distract. **Mitigation:** Keep the mapping minimal and align it closely with the marks it explains.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using meaningful colors but omitting any explanation of what they represent. **Why it fails:** Readers must guess the mapping and may interpret the colors incorrectly [@muth_colors_2018].

## Quick tests <!-- role: check -->

**Failure Sign:** A reader asks “What do these colors mean?” **Quick Check:** Hide surrounding text and see if the chart alone explains its color mapping. **Stronger Test:** Ask a new reader to describe what each color represents after a brief glance.

## What to do instead <!-- role: fix -->

- Add a clear legend that maps each color to its category or value range.
- Label series directly on the marks where feasible to reduce legend hopping.
- Use annotation text to clarify highlight colors or interaction states (e.g., selected vs unselected).
- Reduce the number of color-encoded items so the key is short and readable.
