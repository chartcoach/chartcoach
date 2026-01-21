---
id: add-non-color-indicators-to-distinguish-categories
title: Add Non-Color Indicators to Distinguish Categories
bibliography: references.bib
description: Reduce reliance on many colors by using symbols, patterns, line widths,
  dashes, or opacity as additional indicators.
labels:
- chart:line
- task:distinguish
- visual:shape
- impact:accessibility
- data:categorical
- audience:novice
- source:datawrapper
---

## The Rule <!-- role: advice -->

Differentiate categories using non-color cues (symbols, patterns, line widths, dashes, opacity), and keep the number of such cues small.

## The Logic <!-- role: reason -->

Non-color indicators can separate categories without requiring many hues, which helps when color becomes overloaded. Muth cautions these indicators are limited—using too many makes the chart hard to decipher—so they work best in combination with restrained color use ([@muth_fewer_colors_2022]).

- **The Principle:** Multi-channel encoding without overloading any single channel.
- **The Evidence:** [@muth_fewer_colors_2022]

## Where to Apply <!-- role: context -->

- **User Goal:** Distinguishing categories when color alone is insufficient or should be minimized.
- **Data Type:** Scatterplots/symbol maps (shapes), bar/column charts (patterns), line charts (width/dashes), multi-mark displays (opacity).
- **Audience:** Especially useful where colorblind accessibility is a concern.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You would need more than three or four different non-color indicators to cover all categories.
- **Reason:** Muth notes the indicator set becomes hard to decipher when overused ([@muth_fewer_colors_2022]).

## The Price <!-- role: costs -->

- **The Sacrifice:** Visual simplicity; additional encodings add complexity.
- **The Risk:** Readers may misread or miss subtle differences in patterns/dashes/opacity if too many are used ([@muth_fewer_colors_2022]).

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Introducing many different dash styles, patterns, and shapes to replace a large palette.
- **Why it fails:** The chart becomes difficult to decode—just with a different kind of clutter ([@muth_fewer_colors_2022]).

## How to Check <!-- role: check -->

- **Visual Sign:** Readers struggle to tell which style corresponds to which category; the styling feels “busy.”
- **The Test:** Count distinct non-color styles; if you’re above ~3–4, you’re in the danger zone Muth describes ([@muth_fewer_colors_2022]).

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce the number of style variants and reserve them for the most important distinctions.
- **Best Fix:** Combine a small set of non-color indicators with selective color emphasis or category grouping to reduce the total number of distinguishable categories needed ([@muth_fewer_colors_2022]).
