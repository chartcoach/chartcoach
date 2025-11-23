---
id: integrate-point-estimates
title: Place Point Estimates Inside Uncertainty Distributions
bibliography: references.bib
description: Overlay specific numerical predictions directly onto the uncertainty
  visualization to prevent users from ignoring risk.
labels:
- chart:combination
- task:read-value
- visual:layout
- impact:attention
- data:uncertainty
- audience:non-expert
---

## The Rule <!-- role: advice -->
Position the point estimate (e.g., the specific predicted time or value) spatially coincident with the uncertainty distribution, rather than separating them.

## The Logic <!-- role: reason -->
Users prefer precise numbers (point estimates) and will ignore uncertainty information if the point estimate is displayed separately or more prominently.
*   **The Principle:** Glanceability/False Precision Tradeoff. By forcing the user to look at the distribution to find the point estimate, you ensure they perceive the uncertainty context.
*   **The Evidence:** In design iterations, separating the point estimate (e.g., right-aligned text) caused users to pay too little attention to the probabilistic estimates. Moving the point estimate onto the distribution resolved this tension [@kay_when_2016].

## Where to Apply <!-- role: context -->
*   **User Goal:** Users who want a quick answer (e.g., "When is the bus coming?") but need to be aware of the risk of error.
*   **Data Type:** Single-value predictions accompanied by a probability distribution.
*   **Audience:** Users prone to "false precision" bias (trusting a single number too much).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When the uncertainty is negligible or irrelevant to the decision.
*   **Reason:** If the variance is extremely low, the distribution may just add visual clutter without aiding the decision.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Cleanliness of the text. Overlaying text on a chart can create occlusion or contrast issues.
*   **The Risk:** Text readability may suffer if the underlying distribution is dark or complex.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Placing a large, bold number next to a small sparkline or error bar.
*   **Why it fails:** Users will read the number and ignore the graphic entirely, leading to decisions that fail to account for risk (e.g., missing a bus because the user didn't see the "late" tail) [@kay_when_2016].

## How to Check <!-- role: check -->
*   **Visual Sign:** Is the number sitting in a separate column or box away from the chart?
*   **The Test:** If you cover the chart with your hand, does the user still feel like they have the "complete" answer? If yes, the design is not forcing engagement with uncertainty.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Move the text label to sit directly above or below the center of the distribution.
*   **Best Fix:** Embed the point estimate as a specific annotation (e.g., a vertical line with a label) directly within the density or dotplot area.
