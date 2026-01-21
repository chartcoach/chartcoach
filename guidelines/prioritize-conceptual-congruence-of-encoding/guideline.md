---
id: prioritize-conceptual-congruence-of-encoding
title: Prioritize Conceptual Congruence of the Encoding
bibliography: references.bib
description: "Choose encodings whose metaphors match the concept being communicated\
  \ so the visualization \u2018affords\u2019 the right interpretation."
labels:
- task:interpret
- visual:metaphor
- impact:comprehension
- audience:novice
- audience:expert
- source:bertini-why-not-scatterplots
---

## The Rule <!-- role: advice -->

Select encodings and chart forms whose visual metaphor matches the concept you want viewers to infer (e.g., discrete comparison vs continuous trend, part-to-whole).

## The Logic <!-- role: reason -->

The paper argues that beyond precision, charts carry metaphors and affordances that guide interpretation; even if two charts use the same quantitative channel (e.g., vertical position), changes in form (bars vs lines) can shift what viewers naturally describe and infer. This reflects “congruence” and “cognitive fit” between representation and task [@bertiniWhyShouldntAll2020].

- **The Principle:** Congruence principle / cognitive fit
- **The Evidence:** [@bertiniWhyShouldntAll2020]

## Where to Apply <!-- role: context -->

- **User Goal:** Correct interpretation (e.g., seeing trends as continuous, understanding part-to-whole, spotting correlation/grouping).
- **Data Type:** Any; especially temporal data (trend metaphor) and compositional data (part-to-whole metaphor).
- **Audience:** General audiences who rely heavily on visual affordances.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You explicitly want to discourage a common interpretation (e.g., avoid implying continuity).
- **Reason:** Congruent metaphors can strongly steer interpretation; if that interpretation is undesirable, you may intentionally choose a different form [@bertiniWhyShouldntAll2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may forego the most “precise” encoding per classic rankings.
- **The Risk:** A mismatched metaphor can cause misinterpretation even when values are encoded accurately [@bertiniWhyShouldntAll2020].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Choosing a chart solely because it uses position, ignoring what the form suggests people should do (e.g., compare discrete items vs read trend).
- **Why it fails:** The paper shows that the form changes the judgments viewers are invited to make, not just the precision of decoding [@bertiniWhyShouldntAll2020].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers talk about the “wrong” thing (e.g., describe correlation when you wanted per-item comparison, or describe trend when you wanted discrete differences).
- **The Test:** Ask a viewer to describe what the chart “is about” in one sentence; if it conflicts with your intent, congruence is off [@bertiniWhyShouldntAll2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Swap the chart form to match the intended concept (e.g., bars for discrete comparisons; lines for continuous trend).
- **Best Fix:** Reframe the design around the intended judgment the chart should “afford,” aligning representation with task as recommended in the paper [@bertiniWhyShouldntAll2020].
