---
id: use-quantile-dotplots-for-uncertainty
title: Represent Probabilistic Predictions with Quantile Dotplots
bibliography: references.bib
description: Use discrete dotplots to represent uncertainty, as they outperform continuous
  density plots and intervals for decision-making.
labels:
- chart:dotplot
- chart:quantile-dotplot
- task:decision-making
- visual:frequency
- impact:accuracy
- audience:general-public
- complexity:intermediate
---

## The Rule <!-- role: advice -->
Display uncertainty in predictive systems using **quantile dotplots** (discrete outcomes) rather than probability density functions (PDFs), text intervals, or simple error bars.

## The Logic <!-- role: reason -->
Quantile dotplots translate abstract probability density into discrete "countable" outcomes. This frequency-based representation helps users make better decisions by allowing them to estimate probabilities via counting or subitizing (rapidly recognizing small numbers), rather than estimating the area under a curve.
*   **The Principle:** Frequency Framing / Discrete Outcome Representation.
*   **The Evidence:** In a controlled experiment regarding bus arrival times, quantile dotplots yielded decisions that were better on average (97% of optimal expected payoff) and more consistent (lower variance) than control conditions or other chart types [@fernandes_uncertainty_2018].

## Where to Apply <!-- role: context -->
This technique is highly effective for everyday decision-making contexts where users must weigh risks against rewards.
*   **User Goal:** Making a binary decision based on a continuous variable (e.g., "Should I leave now to catch the bus?").
*   **Data Type:** Predictive distributions (e.g., arrival times, weather forecasts).
*   **Audience:** Non-expert users (laypeople) accessing information on mobile or glanceable displays.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When screen space is extremely limited and cannot support a readable resolution of dots.
*   **Reason:** While 20 dots (Dot20) performed well, the paper found that 50 dots (Dot50) provided better consistency. If the display cannot support enough dots to represent the distribution shape accurately, the benefit may diminish [@fernandes_uncertainty_2018].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Visual clutter compared to a simple text interval or a clean line.
*   **The Risk:** Initial unfamiliarity, though the study showed users learned to use them effectively over a short period (approx. 30-40 trials) [@fernandes_uncertainty_2018].

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a Probability Density Function (PDF).
*   **Why it fails:** PDFs require users to estimate probability by calculating area, which is perceptually difficult. Dotplots allow users to think in terms of "counts" (e.g., 3 dots out of 20) [@fernandes_uncertainty_2018].
*   **The Wrong Fix:** Using too few dots (e.g., <10) for complex distributions.
*   **Why it fails:** The paper suggests higher density (50 dots) leads to more consistent decisions than lower density (20 dots) because it better approximates the full distribution shape while retaining discreteness [@fernandes_uncertainty_2018].

## How to Check <!-- role: check -->
*   **Visual Sign:** Can you count individual circles or icons representing the probability?
*   **The Test:** Ask a user, "What are the chances the event happens after time X?" If they have to estimate the area of a shape, it's a PDF. If they can count distinct units, it's a dotplot.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** If using a PDF, discretize the area into a stack of circles.
*   **Best Fix:** Implement a Wilkinson dotplot or quantile dotplot with 20 to 50 dots representing the predictive distribution.
