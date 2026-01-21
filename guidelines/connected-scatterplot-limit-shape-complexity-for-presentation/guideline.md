---
id: connected-scatterplot-limit-shape-complexity-for-presentation
title: Use Connected Scatterplots Only at Low Visual Complexity
bibliography: references.bib
description: Avoid unreadable spaghetti shapes by keeping connected scatterplots simple
  for presentation contexts.
labels:
- chart:scatter
- task:explain
- visual:shape
- impact:clarity
- data:temporal
- audience:novice
- chart:connected-scatterplot
- complexity:low
---

## The Rule <!-- role: advice -->

Use connected scatterplots for presentation only when the resulting path has a small number of salient, readable features.

## The Logic <!-- role: reason -->

The technique can generate extremely complex shapes that are difficult or impossible to read; the paper positions CS as workable for communication when complexity is kept low [@harozConnectedScatterplotPresenting2016].

- **The Principle:** Readability limits under visual complexity
- **The Evidence:** The authors note that connected scatterplots can become extremely complex and hard to read, and that this is less problematic in journalism because designers can choose not to publish unreadable results [@harozConnectedScatterplotPresenting2016].

## Where to Apply <!-- role: context -->

- **User Goal:** Understand a relationship and its evolution without intensive analysis.
- **Data Type:** Two time series that form a coherent, interpretable trajectory when connected.
- **Audience:** General readers in communication/presentation settings (e.g., journalism-style explanations).

## When to Break It <!-- role: exceptions -->

- **Scenario:** Exploratory analysis tools where complexity is expected and supported by interaction.
- **Reason:** The guideline is specific to presentation clarity; exploratory contexts may tolerate complexity [@harozConnectedScatterplotPresenting2016].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may have to abandon the connected scatterplot even if it seems stylistically appealing.
- **The Risk:** Over-simplifying (e.g., heavy aggregation) can hide important structure.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Publishing a highly tangled connected scatterplot because it looks “interesting.”
- **Why it fails:** Complexity can make the sequence and relationships effectively unreadable [@harozConnectedScatterplotPresenting2016].

## How to Check <!-- role: check -->

- **Visual Sign:** Many crossings/loops/segments that are hard to trace without effort.
- **The Test:** If you cannot follow the path from start to end without losing your place, it is too complex for presentation.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce the time span or sampling density to lower the number of segments.
- **Best Fix:** Use an alternative presentation (e.g., dual-axis line chart or small multiples) when the connected scatterplot becomes visually tangled [@harozConnectedScatterplotPresenting2016].
