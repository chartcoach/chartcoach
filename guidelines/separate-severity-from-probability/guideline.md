---
id: separate-severity-from-probability
title: Do Not Mix Severity Scales with Probability
bibliography: references.bib
description: Avoid adding visual severity indicators to probability displays, as they
  distract from statistical understanding.
labels:
- chart:combined
- visual:emphasis
- impact:distraction
- data:multivariate
- audience:novice
---

## The Rule <!-- role: advice -->
Do not augment probability visualizations with prominent visual scales depicting the severity of the outcome (e.g., "mild" to "severe" color scales).

## The Logic <!-- role: reason -->
High visual salience of "harm" or "severity" captures attention and interferes with the cognitive processing of the statistical likelihood.
*   **The Principle:** Salience Imbalance / Distraction. If the visual weight of the "badness" of the event is too high, users may ignore the "rareness" of the event.
*   **The Evidence:** [@tait_effect_2010] found that parents who saw a "Risk Severity Graphic" (colored blocks ranging from yellow to red) alongside the probability data had significantly lower "gist" understanding of the statistics (60.9% vs 65.3%). The severity graphic also made risks perceive as higher and participation less likely, effectively scaring users away from the math.

## Where to Apply <!-- role: context -->
*   **User Goal:** Understanding the *likelihood* (probability) of an event.
*   **Data Type:** Risk/benefit statistics combined with qualitative severity ratings.
*   **Audience:** People making high-stakes health or safety decisions.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When the severity of the outcome is actually the primary decision factor, and probability is negligible or constant.
*   **Reason:** If the risk is 100%, severity becomes the only relevant variable.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Context. The user might understand *how often* something happens without understanding *how bad* it is. (Note: This information should still be provided textually, just not as a competing visual element).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Color-coding the probability pictograph blocks red to indicate "severe."
*   **Why it fails:** It draws excessive emotional attention to the event, potentially causing the user to overestimate the threat regardless of the actual frequency.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are there bright, alarming colors (red/orange) used to denote the quality of the risk next to the quantity?
*   **The Test:** Does the graphic make the event look "scary" rather than just "frequent"?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Move severity information to text descriptions.
*   **Best Fix:** Present probability (likelihood) and severity (impact) in separate, distinct visual spaces to avoid cognitive interference.
