---
id: design-categorical-palettes-with-lightness-contrast
title: Vary Lightness Across Categorical Hues
bibliography: references.bib
description: Ensure categorical colors differ in lightness so categories remain distinguishable
  in grayscale and for colorblind readers.
labels:
- chart:general
- task:distinguish
- visual:color
- impact:accessibility
- impact:clarity
- data:categorical
- audience:general
- complexity:practical
- source:datawrapper
---

## The Rule <!-- role: advice -->

When using categorical hues, choose colors with **different lightness levels** so categories remain distinguishable even in **grayscale** and are easier to tell apart for **colorblind readers**. [@muth_which_color_scale_2021]

## The Logic <!-- role: reason -->

Lightness differences add a second cue beyond hue. If hues collapse to similar tones (or to similar grays), categories become hard to separate; varying lightness improves separability and robustness when hue perception is limited. [@muth_which_color_scale_2021]

- **The Principle:** Redundant coding within color (hue + lightness) increases categorical discriminability.
- **The Evidence:** [@muth_which_color_scale_2021]

## Where to Apply <!-- role: context -->

- **User Goal:** Identify and compare categories reliably (e.g., which line/segment belongs to which group).
- **Data Type:** Unordered categories (countries, ethnicities, genders, industries). [@muth_which_color_scale_2021]
- **Audience:** Broad audiences, including colorblind readers and anyone viewing in poor display conditions. [@muth_which_color_scale_2021]

## When to Break It <!-- role: exceptions -->

- **Scenario:** You intentionally want most categories to recede (e.g., de-emphasized “others”) while one category stands out.
- **Reason:** Uniform lightness can be used as a deliberate de-emphasis strategy, but only when attention control is the primary goal. [@muth_which_color_scale_2021]

## The Price <!-- role: costs -->

- **The Sacrifice:** Fewer “pretty” same-lightness palettes to choose from; some hues may feel less balanced aesthetically.
- **The Risk:** Overdoing lightness differences can make some categories feel visually heavier than others, implying importance that you didn’t intend. [@muth_which_color_scale_2021]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Picking many hues that look distinct on a white background but share similar lightness.
- **Why it fails:** They can merge when printed, screens are dim, or when viewed in grayscale; category identification suffers. [@muth_which_color_scale_2021]

## How to Check <!-- role: check -->

- **Visual Sign:** Several categories look “equally dark” and are easy to confuse, especially thin lines or small areas.
- **The Test:** Convert the chart to grayscale (or mentally ignore hue): if categories become hard to distinguish, lightness contrast is insufficient. [@muth_which_color_scale_2021]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Adjust the palette so each categorical color has a noticeably different lightness (make some lighter/darker). [@muth_which_color_scale_2021]
- **Best Fix:** Replace the palette with a proven set of hues that already includes lightness variation rather than inventing one from scratch. [@muth_which_color_scale_2021]
