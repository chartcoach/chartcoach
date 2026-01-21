---
id: increase-sequential-gradient-discriminability-with-multiple-hues
title: Use Multiple Hues in Sequential Gradients for Stronger Contrast
bibliography: references.bib
description: Prefer sequential gradients that shift across two or more hues to increase
  contrast between segments and improve readability.
labels:
- chart:map
- chart:general
- task:compare
- visual:color
- impact:clarity
- data:quantitative
- audience:general
- complexity:practical
- source:datawrapper
---

## The Rule <!-- role: advice -->

For sequential color scales, prefer gradients that use **two or more hues** (not just one hue from light to dark) to increase contrast and make steps in the gradient easier to distinguish. [@muth_which_color_scale_2021]

## The Logic <!-- role: reason -->

Adding hue change increases perceived color contrast between adjacent parts of the scale, making it easier for readers to see differences across ranges—especially in classed/stepped legends where viewers compare bins. [@muth_which_color_scale_2021]

- **The Principle:** More perceptual separation between adjacent scale steps improves quantitative discrimination.
- **The Evidence:** [@muth_which_color_scale_2021]

## Where to Apply <!-- role: context -->

- **User Goal:** See low-to-high differences clearly (e.g., identify higher vs. lower rates on a choropleth).
- **Data Type:** Quantitative data with an ordered range (income, temperature, age). [@muth_which_color_scale_2021]
- **Audience:** General audiences, especially when the visualization has many regions/marks that must be compared quickly. [@muth_which_color_scale_2021]

## When to Break It <!-- role: exceptions -->

- **Scenario:** You need a very restrained, single-color aesthetic (e.g., one-hue branding constraint).
- **Reason:** Multi-hue gradients may conflict with strict style requirements, even if they improve discriminability. [@muth_which_color_scale_2021]

## The Price <!-- role: costs -->

- **The Sacrifice:** A multi-hue gradient may feel more “colorful” than desired and can compete with other colored elements.
- **The Risk:** If hue transitions are too strong, readers may perceive artificial boundaries that aren’t in the data. [@muth_which_color_scale_2021]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a single-hue light-to-dark gradient and then increasing the number of classes to compensate.
- **Why it fails:** More classes without stronger perceptual separation can make bins harder—not easier—to tell apart. [@muth_which_color_scale_2021]

## How to Check <!-- role: check -->

- **Visual Sign:** Adjacent bins/areas look nearly identical unless you stare at the legend.
- **The Test:** Look at the map/chart and try to sort a few areas into “low/mid/high” without reading the legend; if it’s difficult, contrast is too low. [@muth_which_color_scale_2021]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch to a sequential palette that transitions across at least two hues (e.g., light yellow → dark blue) rather than only light blue → dark blue. [@muth_which_color_scale_2021]
- **Best Fix:** Rebuild the gradient with clear hue and lightness progression and then re-evaluate classing (binned vs. continuous) to match how precisely viewers need to read differences. [@muth_which_color_scale_2021]
