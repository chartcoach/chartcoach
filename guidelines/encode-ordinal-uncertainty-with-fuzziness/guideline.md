---
id: encode-ordinal-uncertainty-with-fuzziness
title: Encode Ordinal Uncertainty With Fuzziness
bibliography: references.bib
description: Use increasing fuzziness to depict decreasing certainty for discrete
  symbols.
labels:
- chart:map
- task:judge
- visual:fuzziness
- impact:clarity
- data:ordinal
- audience:expert
- domain:uncertainty-visualization
---

## The Rule <!-- role: advice -->

Represent ordinal levels of uncertainty on point symbols by making marks progressively fuzzier as uncertainty increases.

## The Logic <!-- role: reason -->

Fuzziness was among the highest-rated visual-variable encodings for general uncertainty, with strong intuitiveness (mean > 5; mode at the top of the scale) when mapped as “more fuzzy = less certain,” indicating a robust perceptual association for ordinal uncertainty [@maceachrenVisualSemioticsUncertainty2012].

- **The Principle:** Intuitive sign-vehicle–referent mapping via a single visual variable
- **The Evidence:** Experiment #1 Series #1 results and directionality finding [@maceachrenVisualSemioticsUncertainty2012]

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly judging which items are more/less certain
- **Data Type:** Discrete entities with ordinal uncertainty levels (3-step in the study)
- **Audience:** Map/vis-literate users (GIScience students/professionals as sampled)

## When to Break It <!-- role: exceptions -->

- **Scenario:** You must encode a different variable with “clarity/focus” already.
- **Reason:** Fuzziness becomes ambiguous when it conflicts with another intended meaning, reducing interpretability [@maceachrenVisualSemioticsUncertainty2012].

## The Price <!-- role: costs -->

- **The Sacrifice:** Fine shape details become harder to recognize.
- **The Risk:** Overuse can make symbols look like rendering artifacts rather than intentional uncertainty encoding.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Making high-uncertainty symbols crisper to “stand out.”
- **Why it fails:** The tested intuitive direction was specifically “more fuzzy = less certain”; reversing it reduces intuitiveness [@maceachrenVisualSemioticsUncertainty2012].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers interpret the sharpest marks as least reliable or “most uncertain.”
- **The Test:** Show a 3-level legend and ask users which end is “most certain”; if they hesitate or invert, the mapping is wrong.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Flip the mapping so the most certain symbol is the crispest.
- **Best Fix:** Pair fuzziness with a clear legend that explicitly orders “uncertain → certain,” as in Experiment #2’s legend screen [@maceachrenVisualSemioticsUncertainty2012].
