---
id: use-annotated-timeline-to-convey-arrival-status-probability
title: Use an Annotated Timeline to Convey Arrival-Status Probability
bibliography: references.bib
description: Let users infer probabilities like 'already arrived' by segmenting time
  into status regions on a shared timeline.
labels:
- chart:timeline
- task:infer
- visual:position
- impact:clarity
- data:temporal
- audience:novice
- domain:transit
---

## The Rule <!-- role: advice -->

Annotate the time axis with status regions (e.g., “departed / now / on the way”) so users can read arrival-status probabilities directly from the uncertainty distribution.

## The Logic <!-- role: reason -->

When the predictive distribution is plotted against an annotated “now” reference and status regions, users can infer probabilities like “bus has already arrived” from the area (or count) of the distribution that falls into each region, without adding a separate status-probability widget [@kayWhenIshMy2016].

## Where to Apply <!-- role: context -->

- **User Goal:** Decide whether to stay, reroute, or take a backup bus when predictions are unreliable.
- **Data Type:** Predicted arrival time distributions relative to the current time.
- **Audience:** Riders who experience “it said arriving/departed but it wasn’t” failures.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The visualization is not time-referenced to “now” (e.g., it shows only absolute clock times without a current-time marker).
- **Reason:** Status regions are meaningless without a clear “now” anchor [@kayWhenIshMy2016].

## The Price <!-- role: costs -->

- **The Sacrifice:** Consumes horizontal/labeling space on small screens.
- **The Risk:** Poorly labeled regions can confuse users or imply false categorical certainty [@kayWhenIshMy2016].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Add a separate “probability arrived” number while leaving the distribution unanchored.
- **Why it fails:** Users must reconcile two encodings and may trust the categorical status over the distribution [@kayWhenIshMy2016].

## How to Check <!-- role: check -->

- **Visual Sign:** Users cannot tell which parts of the distribution correspond to “already” vs. “not yet.”
- **The Test:** Ask a user to estimate “chance it has arrived already” without extra explanation; if they can’t point to the region, the annotation is insufficient.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a clear “now” marker and label the pre-/post-now regions.
- **Best Fix:** Integrate labeled status bands across the top of the shared timeline so probabilities are read “for free” from the same display [@kayWhenIshMy2016].
