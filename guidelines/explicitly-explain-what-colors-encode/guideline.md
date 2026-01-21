---
id: explicitly-explain-what-colors-encode
title: Explain What Each Color Encodes
bibliography: references.bib
description: Always provide a clear key or labeling that tells readers what colors
  mean in the chart.
labels:
- chart:all
- task:decode
- visual:color
- impact:clarity
- data:categorical
- audience:novice
- accessibility:basic
---

## The Rule <!-- role: advice -->

Always tell readers what your colors represent using a clear key or labeling.

## The Logic <!-- role: reason -->

Unexplained color encodings leave readers guessing; Muth states that every visual mark representing a variable—including color—should be explained [@muth_colors_2018].

- **The Principle:** Reduce ambiguity by making encodings explicit.
- **The Evidence:** [@muth_colors_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Correctly interpret categories/variables without inference.
- **Data Type:** Any chart where color encodes categories or values.
- **Audience:** General readers, especially in fast-reading contexts.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Color is purely decorative or only used to make shapes visible (not encoding data).
- **Reason:** If color carries no data meaning, a key is unnecessary [@muth_colors_2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Space for a legend/key or direct labels.
- **The Risk:** Poorly placed keys can clutter or pull attention away from the data [@muth_colors_2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming meanings are “obvious” (e.g., readers will just know).
- **Why it fails:** Color meaning can be culturally variable or context-dependent, and readers may misinterpret it [@muth_colors_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** A reader cannot state what a color means without asking or guessing.
- **The Test:** Hide the title/caption and ask: “What does blue mean here?” If it’s not answerable from the graphic, the encoding isn’t explained [@muth_colors_2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a concise legend or color key near the marks it explains.
- **Best Fix:** Use direct labeling where possible so readers don’t need to move between plot and legend [@muth_colors_2018].
