---
id: choose-culturally-intuitive-colors-and-avoid-gender-stereotypes
title: Use Intuitive, Audience-Appropriate Colors
bibliography: references.bib
description: "Choose colors that match your audience\u2019s learned associations,\
  \ and avoid stereotypical gender color pairings."
labels:
- chart:all
- task:encode
- visual:color
- impact:interpretability
- data:categorical
- audience:general
- ethics:stereotypes
---

## The Rule <!-- role: advice -->

Choose colors that align with your audience’s cultural and learned associations, and avoid stereotypical pink/blue encoding for gender.

## The Logic <!-- role: reason -->

Muth argues that intuitive palettes reduce confusion because readers already associate certain colors with certain concepts (e.g., parties, nature, stop/go). She also recommends avoiding stereotypical gender palettes and suggests using a colder hue for men and a warmer hue for women if you must differentiate [@muth_colors_2018].

- **The Principle:** Leverage learned color associations to reduce decoding effort.
- **The Evidence:** [@muth_colors_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand category meaning quickly and correctly.
- **Data Type:** Categorical encodings with well-known associations (politics, nature, good/bad) or gender categories.
- **Audience:** A defined target audience with shared conventions.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your audience’s conventions differ from common ones (e.g., different political color mappings).
- **Reason:** The “intuitive” choice depends on the target culture; using mismatched conventions can mislead [@muth_colors_2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less freedom to use arbitrary brand palettes.
- **The Risk:** If you assume the wrong cultural association, you can confuse readers more than neutral colors would [@muth_colors_2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Defaulting to pink vs. blue for gender because it’s familiar.
- **Why it fails:** It reinforces stereotypes that Muth explicitly advises to avoid [@muth_colors_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Readers could plausibly infer a different meaning from the chosen colors (e.g., “red means bad” vs. “red means party A”).
- **The Test:** Ask whether the palette would be interpreted correctly without a legend by the target audience; if not, revise [@muth_colors_2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Swap to more neutral warm/cool pairings for gender (cold hue for men, warmer hue for women) rather than pink/blue.
- **Best Fix:** Choose a palette grounded in your audience’s established associations (and still label/legend it clearly) [@muth_colors_2018].
