---
id: prefer-position-over-gradients-for-key-values
title: Use Position or Length for Key Values, Not Color Gradients
bibliography: references.bib
description: Encode your most important quantitative values with position/length instead
  of gradients to make precise reading and comparisons easier.
labels:
- chart:choropleth
- task:compare
- visual:color
- impact:clarity
- data:quantitative
- audience:novice
- source:datawrapper
---

## The Rule <!-- role: advice -->

Encode your most important quantitative values with position or length (e.g., bars or dot plots), and use color gradients only for showing overall patterns—not for values readers need to read precisely.

## The Logic <!-- role: reason -->

Color gradients make it hard to decipher exact values and small differences, while position/length can be read and compared faster and more reliably, as emphasized by Muth [@muth_colors_2018].

- **The Principle:** Use stronger visual channels (position/length) for precise quantitative reading.
- **The Evidence:** [@muth_colors_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly decipher values and see differences between values.
- **Data Type:** Quantitative measures where exact comparison matters.
- **Audience:** General readers who shouldn’t need to decode subtle color steps.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You primarily need to show a spatial pattern across geography (e.g., a choropleth map).
- **Reason:** Gradients can be effective for revealing broad patterns even when exact values are not the main task [@muth_colors_2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may lose some compactness or the ability to show values directly on a map-like surface.
- **The Risk:** Switching encodings (e.g., to bars/dots) can reduce the immediate “pattern” impression that gradients provide [@muth_colors_2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a gradient because it “looks nice,” even when readers need to compare exact values.
- **Why it fails:** Readers struggle to interpret actual values and differences from gradients [@muth_colors_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers must rely on the legend to interpret most values, and small differences are visually ambiguous.
- **The Test:** Ask someone to estimate or rank a few close values without reading the legend; if they can’t, gradients are doing the wrong job [@muth_colors_2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce reliance on the gradient by highlighting only categories with color and moving key values to labels/annotations.
- **Best Fix:** Change the chart to bars or a dot plot so values are encoded by length/position, keeping color for categories or context [@muth_colors_2018].
