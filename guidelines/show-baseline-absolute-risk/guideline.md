---
id: show-baseline-absolute-risk
title: Show Baseline and Absolute Risk
bibliography: references.bib
description: Always visualize the baseline risk alongside the treatment effect to
  prevent framing bias.
labels:
- chart:grouped-bar
- task:compare
- visual:context
- impact:clarity
- data:relative-risk
- audience:patient
- audience:provider
---

## The Rule <!-- role: advice -->
Never visualize a relative risk reduction (e.g., "50% lower risk") in isolation. Always display the absolute baseline risk alongside the modified risk (e.g., "Reduced from 4% to 2%").

## The Logic <!-- role: reason -->
Relative differences inflate the apparent magnitude of an effect. A change from 1% to 2% seems huge when presented as a "100% increase," leading to distorted perceptions of drug effectiveness or danger. This framing effect impacts not only patients but also physicians. Explicitly presenting the baseline risk strongly improves the accuracy of interpretation [@ancker_rethinking_2007].

## Where to Apply <!-- role: context -->
*   **User Goal:** Evaluating the effectiveness of a medication or the danger of a behavior.
*   **Data Type:** Clinical trial results or epidemiological data showing change over time or between groups.
*   **Audience:** Both patients and healthcare providers (physicians are also subject to this bias).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** None explicitly supported by the paper for informed decision making.
*   **Reason:** The paper notes that framing effects are nearly universal and stronger among people with poor probability reasoning; omitting baseline risk consistently degrades understanding [@ancker_rethinking_2007].

## The Price <!-- role: costs -->
*   **The Sacrifice:** The "persuasiveness" of the data. The effect will look smaller.
*   **The Risk:** Users may dismiss a medically significant treatment because the absolute numbers (e.g., 1% vs 2%) look "small" visually.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Showing two bars where one is half the height of the other (representing a 50% drop) without scaling them to the total population.
*   **Why it fails:** This visualizes the relative reduction, not the absolute reality.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the chart axis start at 0 and go to 100%? Or does it zoom in on the small difference?
*   **The Test:** Look at the chart. Does it look like the risk has disappeared or doubled? Now look at the raw numbers. Do they match that emotional impression?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add explicit labels for the absolute percentages (e.g., "1%" and "2%") directly on the bars.
*   **Best Fix:** Use two side-by-side icon arrays (100 icons each). Show 1 colored icon in the first, and 2 in the second. This visually grounds the "doubling" in the reality that the event is still rare.
