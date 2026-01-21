---
id: prefer-static-grouped-icon-arrays-for-two-risk-comparisons
title: Use Static Grouped Icon Arrays for Comparing Two Risks
bibliography: references.bib
description: When users must compare two medical risks, static grouped icon arrays
  outperform animated and scattered variants for knowledge, choices, and ratings.
labels:
- chart:icon-array
- task:compare
- visual:position
- impact:clarity
- data:probabilistic
- audience:general-public
- domain:health-risk
- source:zikmund-fisher-2012
---

## The Rule <!-- role: advice -->

Use static, grouped icon arrays (event icons contiguous at the bottom) when asking people to compare two risks and choose the lower-risk option.

## The Logic <!-- role: reason -->

Grouped static arrays make the part-to-whole magnitude easy to apprehend and support accurate comparisons without attention being pulled away by motion or randomness cues.

- **The Principle:** Minimize attentional competition and support magnitude extraction
- **The Evidence:** In a 10-arm randomized online experiment (n=4198), the static grouped icon array condition produced the best or near-best choice accuracy, gist knowledge accuracy, and graph evaluation ratings; no animation significantly improved outcomes over this baseline, and many animations performed worse [@zikmund-fisherAnimatedGraphicsComparing2012].

## Where to Apply <!-- role: context -->

- **User Goal:** Choose which of two options has the lower risk profile; identify which option has higher/lower side-effect risk
- **Data Type:** Two probabilities shown side-by-side (eg, 14% vs 16%) using icon arrays
- **Audience:** General adult audiences with mixed numeracy

## When to Break It <!-- role: exceptions -->

- **Scenario:** You must explicitly emphasize randomness/uncertainty rather than enable precise comparison
- **Reason:** This study’s outcomes prioritized comparative choice and gist accuracy; designs that add randomness cues may serve other goals not improved here [@zikmund-fisherAnimatedGraphicsComparing2012].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less visual emphasis on the randomness of who experiences events
- **The Risk:** Users may interpret the grouped block as less “random-looking,” even though it supports magnitude comparison [@zikmund-fisherAnimatedGraphicsComparing2012].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding animation (“bells and whistles”) to a design that already communicates the needed information
- **Why it fails:** In side-by-side risk comparison, animation often reduced knowledge accuracy and user ratings compared with the static grouped baseline [@zikmund-fisherAnimatedGraphicsComparing2012].

## How to Check <!-- role: check -->

- **Visual Sign:** The display includes motion (building, shuffling, settling) while users must compare two simultaneously moving arrays.
- **The Test:** Ask users to (1) pick the safer option and (2) answer gist questions about which risk is higher/equal; if accuracy drops relative to a static grouped prototype, the animation is hurting [@zikmund-fisherAnimatedGraphicsComparing2012].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Freeze the final view and present only the static grouped arrays for both options.
- **Best Fix:** Default to static grouped icon arrays for the comparison task and remove nonessential motion cues entirely [@zikmund-fisherAnimatedGraphicsComparing2012].
