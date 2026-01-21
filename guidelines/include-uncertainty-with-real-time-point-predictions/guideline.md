---
id: include-uncertainty-with-real-time-point-predictions
title: Show Uncertainty Alongside Real-Time Point Predictions
bibliography: references.bib
description: Avoid false precision by pairing arrival-time point estimates with an
  uncertainty visualization.
labels:
- chart:distribution
- task:estimate
- visual:position
- impact:trust
- data:temporal
- audience:novice
- domain:transit
---

## The Rule <!-- role: advice -->

Show an uncertainty visualization with every real-time point prediction of arrival time; do not show a point estimate alone.

## The Logic <!-- role: reason -->

Point-only predictions encourage users to treat the estimate as precise, which can mislead decisions; adding uncertainty communicates that earlier/later outcomes are plausible and supports risk-aware choices in the moment [@kayWhenIshMy2016].

## Where to Apply <!-- role: context -->

- **User Goal:** Decide whether to wait, leave now, or do another activity before the bus arrives (schedule risk/opportunity).
- **Data Type:** Predictive distributions over time-to-arrival.
- **Audience:** Everyday transit riders using mobile apps.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You can only show a single number with no room for any additional mark.
- **Reason:** The interface cannot display uncertainty at all (space is the limiting constraint, not the design choice) [@kayWhenIshMy2016].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less space for listing many upcoming buses; added visual complexity.
- **The Risk:** Some users may feel overwhelmed or prefer the simplicity of point estimates [@kayWhenIshMy2016].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Add a point estimate plus a separate, de-emphasized uncertainty indicator elsewhere.
- **Why it fails:** Users may ignore the uncertainty and still perceive false precision [@kayWhenIshMy2016].

## How to Check <!-- role: check -->

- **Visual Sign:** A single arrival-time number is presented without any distributional mark.
- **The Test:** Ask, “Can a user see at a glance that earlier-than-the-point time is plausible?” If not, uncertainty is missing.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a compact distribution visualization (e.g., density or low-count quantile dotplot) adjacent to the time.
- **Best Fix:** Integrate the point estimate into the uncertainty graphic so they are read together [@kayWhenIshMy2016].
