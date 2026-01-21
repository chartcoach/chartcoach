---
id: use-shades-instead-of-many-hues
title: Use Shades of One Hue Instead of Many Different Hues
bibliography: references.bib
description: Reduce confetti-like visuals by coloring categories with lighter/darker
  shades of one hue rather than many hues.
labels:
- chart:stacked-bar
- task:part-to-whole
- visual:color
- impact:clarity
- data:categorical
- audience:novice
- source:datawrapper
---

## The Rule <!-- role: advice -->

When you must color multiple categories, use lighter and darker shades of a single hue instead of many different hues.

## The Logic <!-- role: reason -->

Using one hue with varying lightness reduces the “confetti” effect and can make a chart feel more coherent, while still allowing categories to be distinguished—though less strongly than distinct hues. Muth notes that shades can also shift what viewers perceive as important in some chart types ([@muth_fewer_colors_2022]).

- **The Principle:** Reduce hue variation; rely on lightness steps to lower visual clutter.
- **The Evidence:** [@muth_fewer_colors_2022]

## Where to Apply <!-- role: context -->

- **User Goal:** Seeing overall totals clearly while still perceiving component parts.
- **Data Type:** Many categories that currently require many colors (e.g., stacked bars).
- **Audience:** General public, especially when the current palette feels overwhelming.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The parts are as important as (or more important than) the totals.
- **Reason:** Muth explains that shades can shift attention toward totals rather than parts, making parts harder to tell apart ([@muth_fewer_colors_2022]).

## The Price <!-- role: costs -->

- **The Sacrifice:** Categories become harder to differentiate than with distinct hues.
- **The Risk:** Viewers may focus on totals and miss differences between similarly shaded parts ([@muth_fewer_colors_2022]).

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Switching to shades without checking whether readers need to compare the parts.
- **Why it fails:** It can hide or de-emphasize the very comparisons the chart is meant to support ([@muth_fewer_colors_2022]).

## How to Check <!-- role: check -->

- **Visual Sign:** Parts blend together; viewers struggle to distinguish adjacent segments.
- **The Test:** Ask whether the chart’s key question is about parts or totals; if it’s about parts, shades are likely working against you ([@muth_fewer_colors_2022]).

## How to Fix <!-- role: fix -->

- **Quick Fix:** Increase the lightness contrast between adjacent shades.
- **Best Fix:** If part-comparison is central, switch back to distinct hues or use another strategy (e.g., emphasis or grouping) rather than relying on subtle shading ([@muth_fewer_colors_2022]).
