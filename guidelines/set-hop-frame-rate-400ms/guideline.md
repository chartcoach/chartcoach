---
id: set-hop-frame-rate-400ms
title: Set HOP Frame Duration to 400ms
bibliography: references.bib
description: When animating uncertainty, set frame duration to approximately 400ms
  to ensure effective cognitive processing.
labels:
- chart:animation
- visual:time
- task:readability
- impact:cognition
- data:uncertainty
- audience:general
---

## The Rule <!-- role: advice -->
Set the duration of each frame in a Hypothetical Outcome Plot (HOP) to approximately 400 milliseconds. Do not speed up the animation to very high frame rates (e.g., 100 milliseconds).

## The Logic <!-- role: reason -->
The human visual system's ability to automatically process ensembles and extract summary statistics breaks down if the information is presented too quickly.
*   **The Principle:** Limits of visual ensemble processing.
*   **The Evidence:** Experiments showed that "Regular" HOPs (400ms) facilitated correct judgments of trends, whereas "Fast" HOPs (100ms) attenuated these performance gains, making users less sensitive to the underlying data trend [@kale_hypothetical_2019].

## Where to Apply <!-- role: context -->
*   **User Goal:** Inferring a model or trend from a set of animated sample outcomes.
*   **Data Type:** Animated visualizations of probability distributions (HOPs).
*   **Audience:** Any user relying on animation to perceive uncertainty.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The visualization is not intended for cognizing individual outcomes, but rather creating a blurred "summary" impression through persistence of vision (though this changes the visualization type away from a standard HOP).
*   **Reason:** The 400ms guideline is specific to allowing users to recognize individual samples while integrating them into a mental distribution.

## The Price <!-- role: costs -->
*   **The Sacrifice:** The visualization takes longer to cycle through a representative number of samples.
*   **The Risk:** If the frame rate is too slow, viewers may become impatient, though 400ms is empirically supported as effective [@kale_hypothetical_2019].

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Speeding up the animation to "show more data" quickly.
*   **Why it fails:** At 100ms per frame, the benefits of the animation for decision-making are lost because the visual system cannot adequately process the distinct samples [@kale_hypothetical_2019].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the animation flicker rapidly like a strobe light?
*   **The Test:** Count the seconds. Can you clearly distinguish one distinct line shape or bar configuration before the next one appears? If not, it is likely too fast.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Adjust the animation delay/timer in your code to 400ms-500ms.
*   **Best Fix:** Use 400ms as a baseline, and consider adding a very short transition (e.g., cubic easing) between frames to smooth the change, as used in the successful trials [@kale_hypothetical_2019].
