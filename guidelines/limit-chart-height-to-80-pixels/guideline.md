---
id: limit-chart-height-to-80-pixels
title: Limit Small Multiples Height to 80 Pixels
bibliography: references.bib
description: For web-based sparklines or small multiples on a 1-100 scale, heights
  beyond 80 pixels offer diminishing returns.
labels:
- chart:bar
- chart:line
- visual:size
- impact:efficiency
- data:quantitative
---

## The Rule <!-- role: advice -->
When designing small charts (like sparklines or small multiples) for the web, set the chart height to approximately 80 pixels. Do not make them significantly taller if the goal is simply minimizing reading error on a standard percentage scale.

## The Logic <!-- role: reason -->
Accuracy in reading values plateaus as chart height increases. Experiments showed significant error reduction when moving from 40px to 80px, but found no significant difference in accuracy between 80px and 160px (or higher). The 80px height roughly coincides with the point where pixel resolution matches data resolution (on a 0-100 scale) [@heer_crowdsourcing_2010].
*   **The Principle:** Resolution Matching
*   **The Evidence:** Experiment 3 in [@heer_crowdsourcing_2010] found accuracy plateaus at 80 pixels height.

## Where to Apply <!-- role: context -->
*   **User Goal:** Making quick visual judgments of magnitude or difference.
*   **Data Type:** Quantitative data on a standardized scale (e.g., 0-100).
*   **Audience:** Web users viewing dashboards or lists of charts.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** High-fidelity analysis.
*   **Reason:** If the user needs to read precise distinct values on a scale much larger than 0-100, more vertical pixels are required to resolve the data steps.
*   **Scenario:** 40px or smaller constraints.
*   **Reason:** If space is extremely limited, you can go smaller, but you must accept significantly higher error rates [@heer_crowdsourcing_2010].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Less visual impact or "drama" than a large-scale hero chart.
*   **The Risk:** Users might perceive the data as less important due to smaller physical size.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Making every chart 300+ pixels tall to ensure "readability."
*   **Why it fails:** It consumes screen real estate without actually improving the user's ability to judge the values accurately [@heer_crowdsourcing_2010].

## How to Check <!-- role: check -->
*   **Visual Sign:** Charts taking up more than 10-15% of the vertical viewport height individually.
*   **The Test:** Measure the pixel height of the plotting area.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Reduce CSS height to 80px.
*   **Best Fix:** Re-evaluate the data resolution; if the data is coarse (0-100), cap the height at 80px and use the saved space for more context or charts.
