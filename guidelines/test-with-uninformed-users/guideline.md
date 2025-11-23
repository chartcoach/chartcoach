---
id: test-with-uninformed-users
title: Test Designs With Uninformed Users
bibliography: references.bib
description: Designers cannot accurately simulate the perspective of a novice; valid
  feedback requires users who lack the designer's private knowledge.
labels:
- impact:clarity
- audience:novice
- task:evaluation
- impact:accessibility
---

## The Rule <!-- role: advice -->
Do not rely on your own judgment or the judgment of subject matter experts to determine if a visualization is clear. You must test the design with users who do not possess the private information or background knowledge you have.

## The Logic <!-- role: reason -->
*   **The Principle:** The Curse of Knowledge.
*   **The Evidence:** Research by @camerer_curse_1989 demonstrates that better-informed agents are "unable to ignore private information even when it is in their interest to do so." In experiments predicting corporate earnings, subjects who knew the actual outcome could not accurately reconstruct the forecasts of those who did not. Even with financial incentives and feedback, they consistently overestimated how much the less-informed group knew. This implies a designer cannot "un-know" their data to simulate a novice's perspective.

## Where to Apply <!-- role: context -->
*   **User Goal:** When designing for an audience with less domain expertise than the creator.
*   **Data Type:** Complex datasets where the "insight" is already known to the designer.
*   **Audience:** General public or stakeholders unfamiliar with the specific dataset.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Designing exploratory tools for experts.
*   **Reason:** If the target audience possesses the same high level of prior knowledge as the designer, the information asymmetry (and thus the curse) is minimal or non-existent.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Testing with true novices takes time and resources compared to self-evaluation or peer review.
*   **The Risk:** You may receive feedback on basic legibility rather than deep insight if the test subjects are too detached from the domain context.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Trying "harder" to be empathetic or offering financial incentives for accurate communication.
*   **Why it fails:** @camerer_curse_1989 found that "incentives and feedback do not reduce the bias." Cognitive effort alone is insufficient to overcome the curse of knowledge.

## How to Check <!-- role: check -->
*   **Visual Sign:** The visualization relies on acronyms, subtle patterns, or context that is not explicitly explained in the chart itself.
*   **The Test:** Ask a user to explain the chart's message. If they miss the "obvious" insight you see, you are suffering from the curse of knowledge.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add explicit annotations that explain *what* to look at, rather than just showing the data.
*   **Best Fix:** Conduct usability testing with a representative sample of the actual target audience (who do not know the data) and iterate based on their confusion.
