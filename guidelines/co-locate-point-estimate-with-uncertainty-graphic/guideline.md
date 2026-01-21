---
id: co-locate-point-estimate-with-uncertainty-graphic
title: Co-locate the Point Estimate with the Uncertainty Display
bibliography: references.bib
description: Resolve the glanceability vs. false-precision tradeoff by placing the
  point estimate inside the uncertainty visualization.
labels:
- chart:distribution
- task:estimate
- visual:position
- impact:clarity
- data:temporal
- audience:novice
- domain:transit
---

## The Rule <!-- role: advice -->

Place the point estimate directly on top of (or within) the uncertainty visualization, not in a separate area of the UI.

## The Logic <!-- role: reason -->

Separating the point estimate from the uncertainty mark allows users to focus only on the number, reinforcing false precision; spatially coinciding them makes looking at the point estimate also expose the uncertainty [@kayWhenIshMy2016].

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly scan multiple upcoming buses and decide which one to catch.
- **Data Type:** A list of predicted arrivals with uncertainty per arrival.
- **Audience:** Mobile users making time-constrained decisions.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The uncertainty visualization is only available on demand (e.g., a drill-down view), while the list view must remain purely textual.
- **Reason:** Co-location is impossible if the distribution isn’t shown in the same view [@kayWhenIshMy2016].

## The Price <!-- role: costs -->

- **The Sacrifice:** Slightly reduces readability of the point number or the distribution if crowded.
- **The Risk:** Overplotting can reduce glanceability if not sized carefully [@kayWhenIshMy2016].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keep the point time aligned at the far right while placing uncertainty elsewhere in the row.
- **Why it fails:** Users can read only the number and ignore uncertainty, recreating the original problem [@kayWhenIshMy2016].

## How to Check <!-- role: check -->

- **Visual Sign:** The point estimate can be read without the eyes ever crossing the uncertainty mark.
- **The Test:** Cover the uncertainty area with your hand—if the point estimate still feels “complete,” it’s too separated.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Move the point label onto the distribution area (e.g., at the mode/median mark).
- **Best Fix:** Design the row so the distribution is the primary substrate and the point estimate is an annotation on it [@kayWhenIshMy2016].
