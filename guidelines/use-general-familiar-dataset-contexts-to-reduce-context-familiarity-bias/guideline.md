---
id: use-general-familiar-dataset-contexts-to-reduce-context-familiarity-bias
title: Use General, Familiar Dataset Contexts to Reduce Context-Familiarity Bias
bibliography: references.bib
description: Choose datasets whose contexts and attributes do not require specific
  expertise so performance reflects visualization reading, not domain knowledge.
labels:
- impact:fairness
- impact:validity
- audience:novice
- custom:dataset-selection
- custom:measurement
---

## The Rule <!-- role: advice -->

Use real-world datasets with general contexts and attributes that do not require specialized expertise, so test performance reflects visualization literacy rather than domain familiarity.

## The Logic <!-- role: reason -->

Dataset context familiarity can influence comprehension; if contexts or attributes require domain expertise, the assessment measures prior knowledge instead of chart reading skill. VLAT mitigates this by selecting real datasets with general contexts (e.g., oil price, height vs. weight) and by checking not just the context label but also whether attributes would be unfamiliar.

- **The Principle:** Control contextual confounds in comprehension
- **The Evidence:** [@leeVLATDevelopmentVisualization2017]

## Where to Apply <!-- role: context -->

- **User Goal:** Fairly comparing visualization literacy across diverse users
- **Data Type:** Real datasets that can be understood without specialized background
- **Audience:** General public / non-experts

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are intentionally assessing domain visualization literacy (e.g., medical chart comprehension).
- **Reason:** Then domain context is part of the construct and should not be removed. [@leeVLATDevelopmentVisualization2017]

## The Price <!-- role: costs -->

- **The Sacrifice:** Less realism for specialized professional scenarios.
- **The Risk:** Over-sanitizing contexts may reduce engagement or omit important domain-specific difficulties. [@leeVLATDevelopmentVisualization2017]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming a context is “familiar” because the topic word is common (e.g., “cars”), while using obscure attributes.
- **Why it fails:** Users may know the topic but not the variables, which still biases performance. [@leeVLATDevelopmentVisualization2017]

## How to Check <!-- role: check -->

- **Visual Sign:** Users struggle with interpreting what variables mean rather than reading values/relations from marks.
- **The Test:** Review each dataset attribute and ask whether a typical adult can interpret it without domain training; if not, replace it. [@leeVLATDevelopmentVisualization2017]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Swap obscure attributes for everyday ones (keeping the same chart type and task).
- **Best Fix:** Build a dataset-selection checklist that explicitly screens both context and attribute familiarity, as described in VLAT. [@leeVLATDevelopmentVisualization2017]
