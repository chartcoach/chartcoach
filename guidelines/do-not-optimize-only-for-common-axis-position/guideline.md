---
id: do-not-optimize-only-for-common-axis-position
title: Do Not Optimize Only for Common-Axis Position
bibliography: references.bib
description: "Do not treat position on a common axis as universally best; choose encodings\
  \ based on the viewer\u2019s task and goal."
labels:
- chart:scatter
- chart:dot
- task:choose
- visual:position
- impact:clarity
- audience:designer
- source:bertini-why-not-scatterplots
---

## The Rule <!-- role: advice -->

Do not default to dot/scatter plots just because position on a common axis is the most precise channel for reading individual values.

## The Logic <!-- role: reason -->

The paper argues that channel rankings based on precise ratio judgments are often over-generalized into a “scatterplots only” mindset; precision for extracting individual values is only one constraint among many, and is not sufficient to determine visualization quality or appropriateness [@bertiniWhyShouldntAll2020].

- **The Principle:** Precision is not a universal objective
- **The Evidence:** [@bertiniWhyShouldntAll2020]

## Where to Apply <!-- role: context -->

- **User Goal:** Any goal beyond extracting exact values (e.g., “big picture,” trend, persuasion, learning, exploration).
- **Data Type:** Any, especially complex/multivariate or narrative/geographic contexts.
- **Audience:** Designers choosing chart types; readers who need interpretation, not just lookup.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The primary task is accurate, fast comparison of specific values (e.g., “Which is bigger?” “What is the ratio?”).
- **Reason:** The paper acknowledges the foundational evidence for position’s superiority for such value-extraction tasks, even while critiquing its overuse [@bertiniWhyShouldntAll2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may give up maximum per-value read-off accuracy.
- **The Risk:** Viewers may misestimate exact quantities when a less precise channel is chosen [@bertiniWhyShouldntAll2020].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Rewriting every chart (including maps or narrative graphics) into aligned dot plots to “increase efficiency.”
- **Why it fails:** It can strip away meaning, metaphor, and higher-level usefulness that the original form supported [@bertiniWhyShouldntAll2020].

## How to Check <!-- role: check -->

- **Visual Sign:** The redesign looks like a generic dot plot even though the communication goal is narrative, spatial, or explanatory.
- **The Test:** Ask: “Is my success metric only response time/accuracy for reading single values?” If yes, you may be over-optimizing [@bertiniWhyShouldntAll2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Write down the top 1–2 intended user tasks before choosing encodings.
- **Best Fix:** Choose (or retain) a chart form that supports the intended task(s) even if it uses “less precise” channels, as argued in the paper’s Minard example [@bertiniWhyShouldntAll2020].
