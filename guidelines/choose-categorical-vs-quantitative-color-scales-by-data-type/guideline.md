---
id: choose-categorical-vs-quantitative-color-scales-by-data-type
title: Match Your Color Scale to the Data You Encode
bibliography: references.bib
description: Use categorical hues for unordered categories and sequential/diverging
  gradients for quantitative values, based on what your color is encoding.
labels:
- chart:general
- task:encode
- visual:color
- impact:clarity
- impact:accessibility
- data:categorical
- data:quantitative
- audience:general
- complexity:foundational
- source:datawrapper
---

## The Rule <!-- role: advice -->

Use **categorical hues** to encode **unordered categories**; use **color gradients** to encode **quantitative values**—**sequential** for low→high and **diverging** for two-sided scales with a meaningful midpoint. Also, first decide **which variable should be encoded by color** based on what your chart type already encodes by position. [@muth_which_color_scale_2021]

## The Logic <!-- role: reason -->

Explain color so it matches what it stands for: discrete hues communicate “different kinds,” while ordered lightness gradients communicate “more vs. less,” and two-direction gradients communicate “away from a center in two directions.” Choosing color based on what the chart already encodes avoids redundant encoding and clarifies what color is meant to mean. [@muth_which_color_scale_2021]

- **The Principle:** Map color scale type to the semantics of the encoded variable (categorical vs. quantitative; one-direction vs. two-direction).
- **The Evidence:** [@muth_which_color_scale_2021]

## Where to Apply <!-- role: context -->

- **User Goal:** Correctly interpret what color signifies (categories vs. magnitude vs. direction from a midpoint).
- **Data Type:**
  - Unordered groups (e.g., countries, industries, genders) → categorical
  - Numeric ranges (e.g., income, temperature, age) → sequential
  - Signed/centered values (e.g., negative vs. positive, Likert-style scales) → diverging
- **Audience:** General audiences and mixed audiences who rely on intuitive color meaning. [@muth_which_color_scale_2021]

## When to Break It <!-- role: exceptions -->

- **Scenario:** You intentionally want to highlight or de-emphasize specific categories/value ranges (e.g., one country, “no data,” “other”).
- **Reason:** Highlighting/de-emphasis can override the “pure” scale choice because the primary goal becomes directing attention rather than representing all items uniformly. [@muth_which_color_scale_2021]

## The Price <!-- role: costs -->

- **The Sacrifice:** Less freedom to pick aesthetically preferred colors if they conflict with the data meaning (e.g., wanting a gradient for categories).
- **The Risk:** If you force the wrong scale type, readers may infer order, magnitude, or polarity that isn’t in the data. [@muth_which_color_scale_2021]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Coloring a choropleth by state identity (a category) instead of the quantitative metric that the map is meant to show.
- **Why it fails:** Position already identifies the state; color becomes redundant and wastes the channel that could encode the numeric rate. [@muth_which_color_scale_2021]
- **The Wrong Fix:** Using a categorical palette to encode a low→high numeric variable.
- **Why it fails:** Hues don’t inherently communicate order, so magnitude comparisons become ambiguous. [@muth_which_color_scale_2021]
- **The Wrong Fix:** Using a sequential gradient when the key message depends on deviation around a meaningful midpoint.
- **Why it fails:** Without a bright/neutral center and two hues, the “two directions” meaning is harder to read. [@muth_which_color_scale_2021]

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers must repeatedly consult the legend to know whether color means “category,” “more/less,” or “negative/positive.”
- **The Test:** Ask: “If I only look at the colors, do they imply (1) different kinds, (2) more vs. less, or (3) two-sided deviation from a center?” If the implication doesn’t match your variable, the scale type is wrong. [@muth_which_color_scale_2021]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch the palette type without changing the chart: categorical → sequential/diverging (or vice versa) so the color meaning matches the encoded field. [@muth_which_color_scale_2021]
- **Best Fix:** Reconsider what to color by: use color for the variable that is *not* already encoded by position in your chosen chart type (e.g., in a line chart color the category; in a choropleth color the numeric value). [@muth_which_color_scale_2021]
