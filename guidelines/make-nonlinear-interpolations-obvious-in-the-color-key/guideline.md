---
id: make-nonlinear-interpolations-obvious-in-the-color-key
title: Reveal Non-Linear Class Ranges in the Color Key
bibliography: references.bib
description: If color classes cover unequal numeric ranges, show that explicitly in
  the legend through labels and proportional class widths.
labels:
- chart:map
- task:interpret
- visual:color
- impact:truthfulness
- data:quantitative
- audience:novice
- complexity:advanced
- source:datawrapper-blog
---

## The Rule <!-- role: advice -->

When your color scale uses unequal class ranges or non-linear interpolation, make it explicit in the color key by labeling min/max and, when possible, varying class widths to reflect their numeric ranges.

## The Logic <!-- role: reason -->

Unequal ranges can be misleading if the legend implies uniform steps; readers won’t infer the interpolation unless you communicate it. Muth advises labeling min/max in such cases and suggests proportionally wide classes as an elegant way to show interpolation truthfully [@muth_color_keys_2023].

- **The Principle:** Prevent false assumptions about scale uniformity
- **The Evidence:** [@muth_color_keys_2023]

## Where to Apply <!-- role: context -->

- **User Goal:** Correctly interpreting what differences in color mean
- **Data Type:** Classed quantitative scales where class intervals are not equal (e.g., expanding upper bins, custom breaks)
- **Audience:** Readers prone to assume evenly spaced classes unless shown otherwise

## When to Break It <!-- role: exceptions -->

- **Scenario:** Classes are equal-width and clearly presented as such
- **Reason:** Extra interpolation signaling may be unnecessary; Muth notes labeling min/max isn’t required when classes are consistent (though it can remove doubt) [@muth_color_keys_2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** More complicated legend construction and possibly more space
- **The Risk:** Variable-width classes could be misread as showing data distribution if the design resembles a histogram rather than a scale [@muth_color_keys_2023].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Drawing equal-size class blocks for unequal numeric ranges without clear min/max labeling
- **Why it fails:** Readers assume uniform steps and misinterpret the magnitude represented by each color [@muth_color_keys_2023].

## How to Check <!-- role: check -->

- **Visual Sign:** The legend looks like evenly spaced steps even though the numeric breaks aren’t.
- **The Test:** Ask: “Could a reader infer that the first/last classes are larger?” If not, the interpolation isn’t communicated [@muth_color_keys_2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add explicit min and max labels (and key break labels) to signal uneven ranges.
- **Best Fix:** Make class block widths proportional to their numeric ranges so the legend’s geometry reflects the interpolation (space permitting) [@muth_color_keys_2023].
