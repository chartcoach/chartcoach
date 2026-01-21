---
id: avoid-stripeplots-for-static-mobile-uncertainty-judgments
title: Avoid Stripeplots for Static Probability Estimation on Mobile
bibliography: references.bib
description: Do not use static stripeplots when users need to estimate probabilities
  precisely from transit arrival uncertainty.
labels:
- chart:stripeplot
- task:estimate
- visual:opacity
- impact:precision
- data:temporal
- audience:novice
- domain:transit
---

## The Rule <!-- role: advice -->

Do not use static stripeplots to communicate predictive uncertainty when users must estimate probabilities; use density or (preferably) low-count quantile dotplots instead.

## The Logic <!-- role: reason -->

In the experiment, stripeplots produced the least precise probability estimates (highest variance) and were rated hardest to use relative to the other tested encodings [@kayWhenIshMy2016]. The paper argues stripeplots can behave like a discrete analog of gradient/opacity encodings, which can be difficult to read for precise judgments in this setting.

## Where to Apply <!-- role: context -->

- **User Goal:** Read odds of arriving before/after a threshold or within an interval.
- **Data Type:** Predictive distributions rendered as compact, static marks in a list.
- **Audience:** Non-expert mobile users.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The task is not estimation (e.g., purely qualitative “more/less uncertain”).
- **Reason:** The study’s measured disadvantage is on probability estimation precision, not necessarily qualitative impression [@kayWhenIshMy2016].

## The Price <!-- role: costs -->

- **The Sacrifice:** You lose a potentially compact, “textural” look.
- **The Risk:** Replacing stripeplots may require redesigning the mark style across the app.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Increase stripe density to “make it clearer.”
- **Why it fails:** More stripes can push users toward continuous, gradient-like reading rather than countable events, undermining estimation [@kayWhenIshMy2016].

## How to Check <!-- role: check -->

- **Visual Sign:** Users describe the plot as “hard to read” or cannot estimate tail probabilities consistently.
- **The Test:** Compare estimation variance in quick user tests across encodings; stripeplots should not be the worst.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch to a density plot if you need a familiar continuous form.
- **Best Fix:** Switch to a low-count quantile dotplot to support frequency-based estimation with higher confidence [@kayWhenIshMy2016].
