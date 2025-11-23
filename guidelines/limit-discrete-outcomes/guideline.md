---
id: limit-discrete-outcomes
title: Limit Discrete Outcomes to Enable Subitizing
bibliography: references.bib
description: Restrict discrete uncertainty plots to small numbers (e.g., 20 dots)
  to facilitate fast counting and subitizing.
labels:
- chart:dotplot
- task:estimate-probability
- visual:density
- impact:glanceability
- data:uncertainty
- audience:general
---

## The Rule <!-- role: advice -->
When using discrete plots to show uncertainty, use a small number of outcomes (e.g., 20 to 50 dots) rather than a large number (e.g., 100+).

## The Logic <!-- role: reason -->
Discrete plots rely on the user's ability to count or quickly perceive quantities. When the number of items is small, users can utilize "subitizing"—the ability to instantly recognize small groups of items—to make fast, accurate judgments.
*   **The Principle:** Subitizing and Countability.
*   **The Evidence:** A dotplot with 20 dots ("Dotplot-20") yielded the lowest variance in user estimates. A dotplot with 100 dots ("Dotplot-100") performed similarly to a continuous density plot because counting became too arduous, leading users to estimate area instead [@kay_when_2016].

## Where to Apply <!-- role: context -->
*   **User Goal:** Making quick, "glanceable" decisions on mobile devices (e.g., checking a bus arrival while walking).
*   **Data Type:** Quantile functions of predictive distributions.
*   **Audience:** Users in time-constrained environments.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When high-resolution probability precision is required (e.g., distinguishing between 1% and 2% risk).
*   **Reason:** A 20-dot plot forces a granularity of 5% per dot. If the decision requires finer granularity, a low-count dotplot is mathematically insufficient [@kay_when_2016].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Resolution. You cannot represent probabilities smaller than $1/N$ (where N is the number of dots).
*   **The Risk:** Rounding errors might oversimplify tail risks if the outcome count is too low.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using 100 or 1000 dots to be "more accurate."
*   **Why it fails:** Users will not count them. They will treat the mass of dots as a solid shape, losing the cognitive benefit of discrete frequency reasoning [@kay_when_2016].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are the dots merging into a solid blob?
*   **The Test:** Attempt to count the dots in the "tail" of the distribution. If it takes longer than a second or two, there are likely too many outcomes for glanceable frequency estimation.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Downsample the distribution to display only 20 or 50 representative quantiles.
*   **Best Fix:** Use a "Dotplot-20" (20 stacked dots), where each dot represents exactly 5% probability.
