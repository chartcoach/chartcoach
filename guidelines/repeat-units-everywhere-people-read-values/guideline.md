---
id: repeat-units-everywhere-people-read-values
title: Repeat Units in Axes, Tooltips, and Annotations
bibliography: references.bib
description: Make units unmistakable by repeating them wherever a reader encounters
  values.
labels:
- chart:general
- task:read-value
- visual:text
- impact:clarity
- data:quantitative
- audience:novice
- source:datawrapper
---

## The Rule <!-- role: advice -->

State the measurement units wherever readers read values—axis labels, tooltips, and annotations—not only in the description.

## The Logic <!-- role: reason -->

Repeating units at the point of reading prevents context loss: readers shouldn’t need to remember (or search for) what “40” means while scanning the chart. Keeping unit context attached to values reduces misinterpretation.

- **The Principle:** Keep semantic context (units) colocated with numbers
- **The Evidence:** [@muth_text_in_data_visualizations_2022]

## Where to Apply <!-- role: context -->

- **User Goal:** Correctly interpret magnitudes (e.g., dollars vs. euros, people vs. percent) while scanning values
- **Data Type:** Any quantitative scale where units matter (currency, %, temperature, counts, rates)
- **Audience:** Broad audiences, especially when charts are read quickly or out of context (social, embeds) [@muth_text_in_data_visualizations_2022]

## When to Break It <!-- role: exceptions -->

- **Scenario:** A unit is visually and repeatedly encoded so strongly that repeating it would create clutter (e.g., every label would become long and cramped).
  - **Reason:** Excess repetition can harm readability; you may need to prioritize space and rely on the most proximal unit cues [@muth_text_in_data_visualizations_2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** More text on the chart; increased risk of crowding.
- **The Risk:** Overlong labels can force awkward wrapping or smaller font sizes, hurting readability [@muth_text_in_data_visualizations_2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Putting units only in the chart description.
  - **Why it fails:** Readers may not read (or remember) the description when inspecting axes or hovering tooltips [@muth_text_in_data_visualizations_2022].
- **The Wrong Fix:** Using “in millions/in thousands” and forcing readers to do mental math.
  - **Why it fails:** Increases cognitive effort and slows comprehension; formatted numbers can usually carry the scale more clearly [@muth_text_in_data_visualizations_2022].

## How to Check <!-- role: check -->

- **Visual Sign:** A number on an axis/tooltip could plausibly be interpreted in multiple units without leaving the marks area.
- **The Test:** Hide the description and ask: “Can I still tell what unit each value uses?” If not, repeat units where the values appear [@muth_text_in_data_visualizations_2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add unit text to axis titles and tooltip strings (e.g., “% unemployed,” “$ revenue”).
- **Best Fix:** Ensure every “value surface” (axes, tooltips, key annotations) includes the unit, and use number formats (k/m/b) to avoid long labels instead of multipliers in prose [@muth_text_in_data_visualizations_2022].
