---
id: use-quantile-dotplots
title: Use Quantile Dotplots for Precise Probability Estimation
bibliography: references.bib
description: Use discrete dotplots instead of density plots or error bars to improve
  user precision in probability tasks.
labels:
- chart:dotplot
- task:estimate-probability
- visual:position
- impact:precision
- data:uncertainty
- audience:non-expert
---

## The Rule <!-- role: advice -->
Represent continuous probability distributions as a set of discrete outcomes (specifically, a quantile dotplot) rather than continuous density plots or error bars.

## The Logic <!-- role: reason -->
Human reasoning about probability improves when information is framed as discrete frequencies (e.g., "3 out of 50 times") rather than abstract probabilities or areas.
*   **The Principle:** Frequency Framing and Discrete Outcomes. Discrete plots allow users to count outcomes to determine intervals, rather than relying on visual estimation of area or opacity.
*   **The Evidence:** In a controlled experiment regarding transit predictions, quantile dotplots reduced the variance of probabilistic estimates by approximately 1.15 times compared to density plots and facilitated higher user confidence [@kay_when_2016].

## Where to Apply <!-- role: context -->
This advice is ideal for mobile or space-constrained interfaces where non-expert users need to make decisions based on predictive models.
*   **User Goal:** Determining the likelihood of an event falling within a specific timeframe or range (e.g., "Will I miss the bus?").
*   **Data Type:** Predictive probability distributions (continuous variables).
*   **Audience:** Laypeople/General Public using everyday applications.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When visual appeal is the primary constraint over precision.
*   **Reason:** Users rated density plots (smooth curves) as significantly more visually appealing than dotplots, even though density plots resulted in slightly higher variance in estimation [@kay_when_2016].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Aesthetic smoothness. Dotplots can look "busier" or less polished than smooth density curves.
*   **The Risk:** If the plot is too dense, users may stop counting and revert to estimating area, negating the benefits of the discrete format.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a Stripeplot (barcode-like density).
*   **Why it fails:** Stripeplots were found to be the least precise and most difficult to use, performing worse than both dotplots and standard density plots [@kay_when_2016].

## How to Check <!-- role: check -->
*   **Visual Sign:** Can you count the individual units representing the probability?
*   **The Test:** Ask a user to estimate the chance of an event occurring before a specific threshold. If they have to estimate the "area under a curve" rather than counting units, the visualization is continuous, not discrete.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Convert a density curve into a histogram with very distinct, countable bars.
*   **Best Fix:** Implement a Wilkinson dotplot algorithm to stack distinct circles (representing quantiles) to form the distribution shape.
