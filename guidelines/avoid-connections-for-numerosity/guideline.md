---
id: avoid-connections-for-numerosity
title: Remove Lines to Enable Accurate Counting
bibliography: references.bib
description: Visual connections between points cause users to underestimate the total
  number of items.
labels:
- chart:network
- chart:line
- visual:connection
- task:count
- task:estimate
- impact:accuracy
---

## The Rule <!-- role: advice -->
Do not connect data points with lines if the viewer needs to estimate the number of points (numerosity).

## The Logic <!-- role: reason -->
Ensemble coding mechanisms for estimating quantity are biased by visual grouping. When objects are connected, the visual system groups them into a single object gestalt, causing viewers to significantly underestimate the number of original parts [@szafir_four_2016].
*   **The Principle:** Unitary Object Perception / Grouping
*   **The Evidence:** Research indicates that connected items reduce perceived numerosity compared to disconnected items (e.g., in network visualizations or line graphs) [@szafir_four_2016].

## Where to Apply <!-- role: context -->
*   **User Goal:** Estimating the quantity of nodes in a network or points in a series.
*   **Data Type:** Node-link diagrams, scatterplots with trend lines, or time series.
*   **Audience:** Users analyzing density or population size.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The primary task is trend detection or path following.
*   **Reason:** Lines are essential for showing sequence and continuity, which often outweighs the need for accurate counting.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Continuity and relationship mapping.
*   **The Risk:** The visualization becomes a "bucket of dots," making it harder to see structure or flow between entities.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Making the nodes larger while keeping thick connecting lines.
*   **Why it fails:** The connection itself drives the perceptual underestimation, not the size of the node.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are there lines connecting the distinct items you want users to count?
*   **The Test:** Ask a user "How many items are here?" If they consistently guess low, the lines are likely the cause.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Make the connecting lines very faint or semi-transparent.
*   **Best Fix:** Provide a toggle to turn off edges/lines, or use a scatterplot view for density estimation tasks.
