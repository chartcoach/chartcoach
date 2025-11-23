---
id: consider-rainbow-for-lookup-tasks
title: Consider Rainbow Scales for Specific Value Search
bibliography: references.bib
description: Rainbow schemes can be effective for tasks requiring the rapid location
  of specific values or categories via a legend.
labels:
- chart:choropleth
- visual:color
- task:filter
- task:locate
- impact:speed
- data:quantitative
- data:categorical
---

## The Rule <!-- role: advice -->
Consider using a hue-varying (rainbow) color scheme *only* if the primary user task is to rapidly search for and locate specific values or categories by matching them to a legend.

## The Logic <!-- role: reason -->
While generally inferior for pattern recognition, rainbow schemes are competitive and sometimes faster than sequential schemes for "locate" and "retrieve value" tasks [@golbiowska_rainbow_2022]. The distinct differences in hue (e.g., distinguishing green from red) allow for faster visual search and legend matching compared to distinguishing subtle shade differences in sequential scales. This nuance is highlighted in the review by Zeng et al. [@zeng_review_2023].

*   **The Principle:** Visual Search / Hue Discriminability
*   **The Evidence:** [@golbiowska_rainbow_2022], [@zeng_review_2023]

## Where to Apply <!-- role: context -->
*   **User Goal:** "Find all regions with value X" or "What is the exact value of region Y?"
*   **Data Type:** Discretized quantitative data or categorical data where order is irrelevant.
*   **Audience:** Users performing lookup tasks where understanding the overall distribution is secondary.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The user needs to understand the distribution shape, find gradients, or identifying anomalies in the data structure.
*   **Reason:** The lack of intuitive order in rainbow scales creates "false boundaries" and obscures general patterns [@golbiowska_rainbow_2022].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You sacrifice the user's ability to intuitively judge magnitude (e.g., "darker is more").
*   **The Risk:** The visualization becomes inaccessible to users with color vision deficiencies (CVD), and overall patterns become difficult to perceive.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a rainbow scale for continuous data where the user needs to see smooth transitions.
*   **Why it fails:** Rainbow scales introduce perceptual banding (artifacts) that look like features but are just changes in hue.

## How to Check <!-- role: check -->
*   **Visual Sign:** Is the visualization used for looking up distinct "buckets" of data?
*   **The Test:** Ask a user to find all areas with value range "50-60". If they can do it instantly by looking for "Yellow," the scheme is working for that specific task.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Ensure the legend is clearly visible and the hues are highly saturated to maximize distinctness.
*   **Best Fix:** If order matters even slightly, switch to a multi-hue sequential scale which offers better discriminability than single-hue scales but retains order.
