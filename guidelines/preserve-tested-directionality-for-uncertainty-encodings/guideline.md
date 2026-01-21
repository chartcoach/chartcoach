---
id: preserve-tested-directionality-for-uncertainty-encodings
title: Preserve the Tested Directionality of Uncertainty Encodings
bibliography: references.bib
description: Ensure the most uncertain and most certain symbols are mapped in the
  empirically supported direction for each visual variable.
labels:
- chart:map
- task:interpret
- visual:encoding-direction
- impact:clarity
- data:ordinal
- audience:expert
- domain:uncertainty-visualization
---

## The Rule <!-- role: advice -->

Use the empirically supported direction for each uncertainty encoding: more fuzzy, farther from center, lighter value, poorer arrangement, smaller size, and more obscured (via transparency) must correspond to higher uncertainty.

## The Logic <!-- role: reason -->

Experiment #1 found that for every visual variable judged good/marginal for uncertainty, only one polarity was judged intuitive; reversing the mapping reduced intuitiveness, meaning directionality is part of the encoding’s semantics, not a cosmetic choice [@maceachrenVisualSemioticsUncertainty2012].

- **The Principle:** Semantic polarity of visual variables
- **The Evidence:** Experiment #1 directionality findings for good/marginal variables [@maceachrenVisualSemioticsUncertainty2012]

## Where to Apply <!-- role: context -->

- **User Goal:** Immediate interpretation of “more vs less certain”
- **Data Type:** Ordinal uncertainty on discrete symbols
- **Audience:** Users making quick judgments (as in the timed tasks)

## When to Break It <!-- role: exceptions -->

- **Scenario:** You must align with a strong, existing house convention in a deployed system.
- **Reason:** Changing polarity can be costly; however, the paper indicates polarity changes can harm intuitiveness, so this should be a conscious trade-off and tested [@maceachrenVisualSemioticsUncertainty2012].

## The Price <!-- role: costs -->

- **The Sacrifice:** Reduced freedom to stylistically “invert” designs.
- **The Risk:** If other encodings in the same display use opposite polarity (e.g., light = good), users may be conflicted.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Making uncertain items bigger/brighter to draw attention while claiming it indicates “more uncertainty.”
- **Why it fails:** Size was only marginally acceptable and only in the direction “smaller = less certain” in this study’s general uncertainty test [@maceachrenVisualSemioticsUncertainty2012].

## How to Check <!-- role: check -->

- **Visual Sign:** Users repeatedly ask which end of the legend is “uncertain.”
- **The Test:** Flash a legend briefly and ask users to point to “most uncertain”; slow or inconsistent answers suggest polarity confusion.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Flip the mapping to match the tested polarity.
- **Best Fix:** Standardize polarity across the product and reinforce it with a clear legend ordering “uncertain → certain” as done in the experiments [@maceachrenVisualSemioticsUncertainty2012].
