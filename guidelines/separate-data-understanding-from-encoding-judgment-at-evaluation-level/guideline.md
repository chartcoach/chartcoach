---
id: separate-data-understanding-from-encoding-judgment-at-evaluation-level
title: Choose Evaluation Tasks That Match Your Evaluation Target
bibliography: references.bib
description: "At the Evaluation level, decide whether participants should judge the\
  \ chart\u2019s design or instead justify a conclusion using the chart\u2019s data."
labels:
- task:evaluate
- impact:validity
- audience:general-public
- custom:blooms-taxonomy
---

## The Rule <!-- role: advice -->

At the **Evaluation** level, explicitly choose one: either (a) have participants **judge the visualization design** by criteria, or (b) have them **justify a conclusion using data evidence**—and align your prompt to that choice.

## The Logic <!-- role: reason -->

The paper distinguishes two different translations of “Evaluation”: evaluating the visualization itself versus evaluating claims using the data. They recommend the evidence/justification approach when the goal is assessing understanding of the underlying data, and use that approach in their experiment [@burnsHowEvaluateData2020].

- **The Principle:** Construct validity—measure what you intend to measure
- **The Evidence:** [@burnsHowEvaluateData2020]

## Where to Apply <!-- role: context -->

- **User Goal:** Determine whether people can use the chart to support/assess a real-world decision or argument
- **Data Type:** Communication charts intended to influence decisions (policy, public health, business)
- **Audience:** Decision-makers or the general public interpreting claims from charts [@burnsHowEvaluateData2020]

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your study goal is explicitly about comprehension of visual encodings or interface features
- **Reason:** Then judging the visualization itself (e.g., reliability/appropriateness) is the more direct Evaluation task [@burnsHowEvaluateData2020]

## The Price <!-- role: costs -->

- **The Sacrifice:** Evidence-based argument prompts can introduce variability from participants’ beliefs and prior biases
- **The Risk:** Participants may reach similar policy conclusions even from different designs, masking encoding differences (as observed in the COVID case) [@burnsHowEvaluateData2020]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Mixing both targets in one prompt (“Is this chart good and what policy should we do?”)
- **Why it fails:** You conflate design critique with data-based reasoning, making results hard to interpret [@burnsHowEvaluateData2020]

## How to Check <!-- role: check -->

- **Visual Sign:** Your Evaluation responses are hard to interpret because some discuss aesthetics while others discuss policy outcomes
- **The Test:** Confirm the prompt demands either (a) chart-quality criteria or (b) a claim + evidence from the data, but not both [@burnsHowEvaluateData2020]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Rewrite the Evaluation question to require “What claim would you argue for, and what evidence in the chart supports it?”
- **Best Fix:** Run two separate Evaluation tasks—one for design judgment and one for data-based justification—only if you truly need both constructs [@burnsHowEvaluateData2020]
