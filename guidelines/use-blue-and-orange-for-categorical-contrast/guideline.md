---
id: use-blue-and-orange-for-categorical-contrast
title: "Prefer Blue\u2013Orange Pairings for Category Contrast"
bibliography: references.bib
description: Use blue (and orange/red) as the most robust hue pairing for readers
  with common forms of color vision deficiency.
labels:
- chart:multi
- task:distinguish
- visual:color
- impact:accessibility
- data:categorical
- audience:general
- source:datawrapper
---

## The Rule <!-- role: advice -->

Use blue as your primary hue for categorical encoding, and pair it with orange (or red) when you need a second distinct color; avoid green paired with red/orange or with similarly light blue.

## The Logic <!-- role: reason -->

Blue changes least between normal vision and common red/green color vision deficiencies, and blue–orange sits far apart in hue, increasing the chance that categories remain separable across different types of colorblindness.

- **The Principle:** Choose hue pairings that remain discriminable under color vision deficiencies
- **The Evidence:** The post notes “Blue is the safest hue,” and recommends mixing blue with orange/red as the safest multi-color choice while warning against green–red/orange and green–blue of similar lightness [@muth_colorblindness_2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Telling categories/series apart quickly
- **Data Type:** Nominal categories (e.g., two groups, two series)
- **Audience:** Broad/public audiences including colorblind and colorweak readers [@muth_colorblindness_2020]

## When to Break It <!-- role: exceptions -->

- **Scenario:** You must use fixed brand colors that don’t include usable blues/oranges
- **Reason:** You may be unable to change hues; you’ll need to add non-color encodings (symbols, patterns, line dashes) instead [@muth_colorblindness_2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less freedom to use cohesive “nearby” hues (e.g., blue/purple aesthetics)
- **The Risk:** Overusing the same blue–orange look can reduce novelty or brand alignment [@muth_colorblindness_2020].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Picking multiple adjacent hues (e.g., blue vs. purple) because they “look cohesive”
- **Why it fails:** Small hue differences can collapse for colorblind readers, “torpedoing” comprehension [@muth_colorblindness_2020].

## How to Check <!-- role: check -->

- **Visual Sign:** Two categories become similar-looking (muddy/olive-ish) under colorblind viewing
- **The Test:** Simulate red-/green-/blue-blindness with a colorblind simulator (or your tool’s warnings) and verify the categories still separate [@muth_colorblindness_2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Swap one problematic hue (often green) for blue or orange while keeping other styling unchanged
- **Best Fix:** Reduce to a blue vs. orange/red scheme for the key comparison and de-emphasize remaining categories [@muth_colorblindness_2020].
