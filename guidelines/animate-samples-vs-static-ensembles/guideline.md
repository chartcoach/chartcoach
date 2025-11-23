---
id: animate-samples-vs-static-ensembles
title: Animate Samples Instead of Overplotting
bibliography: references.bib
description: Animate distinct samples over time rather than plotting them all simultaneously
  to avoid clutter and improve trend detection.
labels:
- chart:line
- visual:clutter
- task:trend-detection
- impact:clarity
- data:ensemble
- audience:general
---

## The Rule <!-- role: advice -->
Present uncertainty samples sequentially using animation (HOPs) rather than aggregating them into a single static "spaghetti plot" or ensemble view.

## The Logic <!-- role: reason -->
Displaying too many outcomes in a single static view can lead to crowding and clutter, which disrupts the perception of discrete outcomes. Animation leverages the visual system's ability to process ensembles over time without the visual interference of overlapping lines.
*   **The Principle:** Avoidance of visual crowding / Clutter reduction.
*   **The Evidence:** Participants were more consistently sensitive to underlying trends in noisy time series when viewing "Regular" HOPs compared to static line ensembles that displayed the exact same data simultaneously [@kale_hypothetical_2019].

## Where to Apply <!-- role: context -->
*   **User Goal:** Determining a trend from a set of possible noisy outcomes.
*   **Data Type:** Multiple time-series lines (ensembles) representing uncertainty.
*   **Audience:** Users who need to make decisions based on the likelihood of a trend.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The user needs to compare two specific outlying lines simultaneously for a detailed value check.
*   **Reason:** Animation requires memory integration; if the task relies on direct, simultaneous comparison of specific static values, a static plot may be easier to parse than waiting for the specific frames to appear.

## The Price <!-- role: costs -->
*   **The Sacrifice:** The viewer cannot see the entire "envelope" or range of the data in a single instant static snapshot.
*   **The Risk:** The viewer must allocate attention over time to build the mental model of the distribution.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Plotting 50 semi-transparent lines on top of each other (static ensemble).
*   **Why it fails:** While better than error bars, this approach resulted in lower sensitivity to trends compared to animating those same lines sequentially at a readable speed [@kale_hypothetical_2019].

## How to Check <!-- role: check -->
*   **Visual Sign:** Is your chart a "hairball" or a dense mass of overlapping lines?
*   **The Test:** Can you trace a single potential outcome from start to finish easily? If not, the static display is likely too crowded.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** If static is required, reduce the number of lines (samples) to avoid crowding, though this reduces the fidelity of the distribution.
*   **Best Fix:** Convert the static layers into frames of an animation (HOPs) playing at ~400ms per frame.
