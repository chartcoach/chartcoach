---
id: avoid-perceptual-pull-multi-series
title: Isolate Series to Prevent Perceptual Pull
bibliography: references.bib
description: Separate data series into distinct panels to prevent the position of
  one series from distorting the perceived average of another.
labels:
- chart:line
- chart:bar
- chart:composite
- task:aggregate
- visual:position
- impact:accuracy
---

## The Rule <!-- role: advice -->
Use small multiples (faceting) instead of superimposing multiple data series on a single chart when the user's task involves estimating the average of individual series.

## The Logic <!-- role: reason -->
When multiple series are plotted together, they visually interfere with the user's ability to estimate the position of a specific target series.
*   **The Principle:** Perceptual Pull. The perceived average position of a target series is gravitationally "pulled" toward the position of an irrelevant series plotted in the same space.
*   **The Evidence:** Xiong et al. [@xiong_biased_2020] demonstrated that in "compound" graphs (e.g., two lines, two bar sets, or mixed line/bar), the presence of a second series distorted the estimate of the first. Zeng et al. [@zeng_review_2023] highlight this as a critical interaction effect where irrelevant data biases the interpretation of relevant data.

## Where to Apply <!-- role: context -->
*   **User Goal:** "Aggregate" tasks where the user must estimate the average of one specific series (the target) while ignoring others.
*   **Data Type:** Multiple quantitative series (Compound Line-Line, Bar-Bar, or Line-Bar displays).
*   **Visual Density:** Charts containing two or more overlapping or adjacent series.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Direct comparison of values at a specific point in time (e.g., "Is Series A higher than Series B on Tuesday?").
*   **Reason:** Superposition is generally superior for local comparison tasks, whereas the "Perceptual Pull" bias specifically degrades *global averaging* tasks [@xiong_biased_2020].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Spatial efficiency. Faceting (small multiples) requires more screen real estate than a single combined chart.
*   **The Risk:** Separating charts makes direct comparison of individual data points more difficult (Eyes beat memory).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Simply changing colors to distinguish series.
*   **Why it fails:** Xiong et al. [@xiong_biased_2020] found the pull effect persists regardless of whether the series are lines or bars; mere color separation does not remove the gravitational pull on the perceived position.

## How to Check <!-- role: check -->
*   **Visual Sign:** A dual-axis or multi-line chart where the lines are vertically separated (one high, one low).
*   **The Test:** Check if the user perceives the bottom line as higher than it is (pulled up) or the top line as lower than it is (pulled down).

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Allow users to toggle visibility, viewing only one series at a time.
*   **Best Fix:** Break the chart into vertically aligned small multiples (separate panels sharing an x-axis).
