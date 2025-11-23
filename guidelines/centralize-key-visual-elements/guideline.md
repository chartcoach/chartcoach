---
id: centralize-key-visual-elements
title: Centralize Key Visual Elements
bibliography: references.bib
description: Place the most important visual information near the center of the composition,
  as human gaze is naturally biased toward this region.
labels:
- visual:position
- impact:engagement
- audience:general
- task:explore
---

## The Rule <!-- role: advice -->
Place the primary subject or most critical data visualization components near the physical center of the display or image canvas.

## The Logic <!-- role: reason -->
Human observers exhibit a strong "center-bias" when viewing scenes. According to @borji_quantitative_2013, the majority of eye fixations occur near the image center. This behavior may stem from a "viewing strategy" where subjects first inspect the center to rapidly gather the "gist" of a scene, or from "photographer bias" where interesting objects are typically framed centrally.

*   **The Principle:** Center-Bias (Center-Preference)
*   **The Evidence:** @borji_quantitative_2013

## Where to Apply <!-- role: context -->
This advice applies to static displays where the user's initial attention is required immediately.
*   **User Goal:** Rapidly understanding the main subject of a visualization or dashboard.
*   **Data Type:** Static images, single-screen dashboards, or search arrays.
*   **Audience:** General observers engaging in free-viewing.

## When to Break It <!-- role: exceptions -->
Do not force centering if the data has an intrinsic spatial structure that demands otherwise (e.g., a map) or if the workflow is linear (e.g., F-pattern scanning).
*   **Scenario:** Reading-heavy interfaces or geographic maps.
*   **Reason:** In these cases, spatial location conveys semantic meaning (location on a map) or follows a learned reading order (top-left start) that overrides general scene viewing strategies.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the ability to use the center for negative space or layout separation.
*   **The Risk:** Cluttering the center can lead to "crowding," making it difficult to distinguish individual elements if too much information is packed into the high-attention zone.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Placing the most important alert or KPI in the far corners or edges.
*   **Why it fails:** @borji_quantitative_2013 indicates that off-center fixations are "non-trivial" and harder to predict; users are statistically less likely to fixate on the periphery during initial viewing.

## How to Check <!-- role: check -->
*   **Visual Sign:** Is the main subject located in the outer 20% of the canvas?
*   **The Test:** Overlay a Gaussian blob at the center of your design. Does it cover the most critical information?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Crop the view or move the main chart to the middle of the layout.
*   **Best Fix:** Re-balance the composition so the "center of gravity" of the data aligns with the geometric center of the canvas.
