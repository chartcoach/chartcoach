---
id: choose-hues-for-unordered-categories
title: Use Hues for Unordered Categories
bibliography: references.bib
description: Use distinct hues for categories without inherent order, and use quantitative
  color scales only when values are ordered.
labels:
- chart:general
- task:categorize
- visual:color
- impact:clarity
- data:categorical
- audience:novice
- source:datawrapper
---

## The Rule <!-- role: advice -->

Use distinct hues for categories that have no inherent order; use a sequential or diverging (quantitative) color scale only when the values can be meaningfully ordered.

## The Logic <!-- role: reason -->

Qualitative (categorical) values don’t imply “more/less,” so mapping them to light-to-dark gradients invites readers to infer rank or magnitude that isn’t there. Using different hues communicates “different kinds,” while quantitative scales communicate “ordered amounts,” aligning the color channel with how viewers interpret it [@muth_quantitative_vs_qualitative_2021].

- **The Principle:** Match color semantics to data measurement (unordered vs ordered)
- **The Evidence:** [@muth_quantitative_vs_qualitative_2021]

## Where to Apply <!-- role: context -->

- **User Goal:** Identify and differentiate categories without comparing magnitude
- **Data Type:** Nominal categories (e.g., industries, countries) and other values without inherent order
- **Audience:** General audiences who will default to interpreting gradients as “more/less”

## When to Break It <!-- role: exceptions -->

- **Scenario:** You want to emphasize an underlying order that exists behind the categories (e.g., size/rank already visible via position/area).
- **Reason:** A quantitative scale can be used to reinforce that already-visible order (double-encoding) [@muth_quantitative_vs_qualitative_2021].
- **Scenario:** You need shades to structure subcategories under a few parent categories (hue for parent, shade for child).
- **Reason:** Shades can help group and differentiate subcategories without relying on a rainbow of unrelated hues [@muth_quantitative_vs_qualitative_2021].

## The Price <!-- role: costs -->

- **The Sacrifice:** You lose the ability to communicate ordering or intensity through lightness.
- **The Risk:** With many categories, distinct hues can become visually busy (“confetti”) and harder to scan [@muth_quantitative_vs_qualitative_2021].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a light-to-dark gradient for countries/industries “just because it looks tidy.”
- **Why it fails:** Readers will search for meaning (rank, importance, higher/lower) in the shading even when none exists [@muth_quantitative_vs_qualitative_2021].
- **The Wrong Fix:** Coloring categories by a second variable that is only shown via color.
- **Why it fails:** Most charts become very hard to read when color is the only encoding of an additional variable [@muth_quantitative_vs_qualitative_2021].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers could reasonably ask, “Does darker mean more/better/important?” even though your categories are unordered.
- **The Test:** Ask a colleague what the darkest category “means.” If they infer magnitude/rank, the palette is misaligned [@muth_quantitative_vs_qualitative_2021].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace the gradient with a qualitative palette of clearly distinct hues.
- **Best Fix:** If you actually need ordering, switch to a sequential/diverging scale and make the order explicit (e.g., sort categories or add supporting encodings/labels) [@muth_quantitative_vs_qualitative_2021].
