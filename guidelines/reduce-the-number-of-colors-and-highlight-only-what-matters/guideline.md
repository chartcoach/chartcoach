---
id: reduce-the-number-of-colors-and-highlight-only-what-matters
title: Use Fewer Colors and Color Only Key Values
bibliography: references.bib
description: Minimize the number of distinct colors and reserve strong color for the
  main insights to reduce confusion for colorblind readers.
labels:
- chart:multi
- task:highlight
- visual:color
- impact:clarity
- impact:accessibility
- data:categorical
- audience:general
- source:datawrapper
---

## The Rule <!-- role: advice -->

Limit distinct colors (aim for 3–4 or fewer when possible) and use color selectively to emphasize the most important values; tone down or group the rest.

## The Logic <!-- role: reason -->

As the number of colors increases, distinguishing categories becomes harder for everyone and especially for colorblind readers; selective coloring focuses attention on the intended takeaway and reduces the decoding burden [@muth_colorblindness_2020].

- **The Principle:** Reduce encoding load by limiting category channels
- **The Evidence:** The article states that more colors are harder to tell apart and includes a colorblind reader’s quote about tuning out when charts use lots of colors without other aids; it recommends choosing chart types that rely less on colors and coloring only the most important values [@muth_colorblindness_2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Identify the main insight (top performers, exceptions, key group vs. rest)
- **Data Type:** Many-category categorical data or multi-series comparisons
- **Audience:** Readers scanning quickly (news, dashboards, presentations) [@muth_colorblindness_2020]

## When to Break It <!-- role: exceptions -->

- **Scenario:** Every category must be equally prominent and distinguishable (e.g., a small set of official categories with equal importance)
- **Reason:** De-emphasizing “other” categories could mislead; instead use non-color encodings or direct labels [@muth_colorblindness_2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less ability to give each category a unique color identity
- **The Risk:** Over-grouping can hide meaningful differences among the “toned down” categories [@muth_colorblindness_2020].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assigning a unique hue to every category in a long list
- **Why it fails:** The palette becomes indistinguishable, and colorblind readers may disengage without additional cues [@muth_colorblindness_2020].

## How to Check <!-- role: check -->

- **Visual Sign:** The legend becomes a rainbow and categories can’t be reliably matched to marks
- **The Test:** Count distinct category colors; if you can’t name-match them quickly (or they blur in simulation), reduce them [@muth_colorblindness_2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Gray out non-essential categories and keep 1–2 highlight colors for the key message
- **Best Fix:** Change to a chart type that relies less on color (e.g., direct-labeled bars) and restructure categories (grouping, filtering, small multiples) [@muth_colorblindness_2020].
