---
id: avoid-using-luminance-differences-when-numerosity-comparisons-matter
title: Avoid Luminance Differences When Numerosity Comparisons Matter
bibliography: references.bib
description: Do not use darker vs. lighter marks to encode categories when users must
  judge which group has more items, because darkness can bias perceived counts.
labels:
- chart:unit
- task:compare
- task:summarize
- visual:luminance
- impact:accuracy
- data:categorical
- audience:general
---

## The Rule <!-- role: advice -->

Do not encode category membership with luminance (dark vs. light) if users need to judge which group is more numerous.

## The Logic <!-- role: reason -->

- **The Principle:** Luminance can bias perceived numerosity.
- **The Evidence:** The paper notes that darker collections can appear more numerous, creating biased numerosity judgments, and flags this as a visualization design concern [@szafirFourTypesEnsemble2016a].

## Where to Apply <!-- role: context -->

- **User Goal:** Estimate or compare counts across categories (e.g., “Are there more purple than orange points?”).
- **Data Type:** Dot plots, unit charts, tagged-text marks, or any display where item count is inferred from repeated marks.
- **Audience:** General readers and analysts making fast “more vs. less” judgments.

## When to Break It <!-- role: exceptions -->

- **Scenario:** When exact numerosity is irrelevant and luminance is used purely for emphasis or hierarchy.
- **Reason:** The bias only matters when numerosity is a decision variable [@szafirFourTypesEnsemble2016a].

## The Price <!-- role: costs -->

- **The Sacrifice:** You lose a simple, compact way to distinguish categories.
- **The Risk:** Switching away from luminance may require using hue or another channel that could be reserved for a different variable [@szafirFourTypesEnsemble2016a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Making one category darker “for contrast” while still expecting fair count comparisons.
- **Why it fails:** Increased darkness can inflate perceived numerosity even if the actual counts are equal [@szafirFourTypesEnsemble2016a].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers consistently report the darker group as “more,” even when balanced.
- **The Test:** Temporarily equalize luminance (or swap the luminance assignment between categories). If perceived “more” flips, luminance bias is present [@szafirFourTypesEnsemble2016a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Match luminance across categories and use hue or shape instead.
- **Best Fix:** Use an encoding shown to be robust for numerosity comparisons in the paper’s discussion (e.g., color hue or orientation differences) while keeping luminance constant [@szafirFourTypesEnsemble2016a].
