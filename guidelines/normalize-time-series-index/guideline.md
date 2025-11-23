---
id: normalize-time-series-index
title: Use Index Charts to Compare Relative Change
bibliography: references.bib
description: Normalize time-series data to a common baseline to compare growth rates
  rather than absolute prices.
labels:
- chart:line
- data:temporal
- task:compare
- industry:finance
- impact:insight
---

## The Rule <!-- role: advice -->
When comparing the growth rates or percentage changes of multiple time series with vastly different starting values, normalize the data based on a selected index point (making all series start at 0% or 1.0).

## The Logic <!-- role: reason -->
Raw values can obscure relative performance when baselines differ significantly.
*   **The Principle:** Baseline Normalization
*   **The Evidence:** As noted in comparisons of stock prices (e.g., Amazon vs. Google), raw prices may differ dramatically. An index chart reveals the *percentage change* from a base point, allowing meaningful comparison of the *rate* of change rather than the specific price [@heer_tour_2010].

## Where to Apply <!-- role: context -->
*   **User Goal:** Investors or analysts interested in growth rates or relative performance over time.
*   **Data Type:** Multiple time series with different scales (e.g., a stock at $50 vs. a stock at $500).
*   **Audience:** Financial analysts or decision-makers comparing trends.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When absolute magnitude is critical to the decision.
*   **Reason:** If the user needs to know the actual cost or quantity (e.g., "Do we have enough budget?"), relative change is misleading.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose visibility of the raw underlying values (the actual price).
*   **The Risk:** Users may misinterpret a high percentage growth as a high absolute value.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Plotting a cheap stock and an expensive stock on the same raw Y-axis.
*   **Why it fails:** The cheap stock appears as a flat line at the bottom, hiding its volatility or growth relative to the expensive stock.

## How to Check <!-- role: check -->
*   **Visual Sign:** Do all lines originate from the exact same point on the Y-axis (usually 0% or 100) at the start of the time period?
*   **The Test:** Check the Y-axis labels. They should represent percentages or factors (e.g., +10%, 1.5x) rather than currency or raw counts.

## How to Fix <!-- role: fix -->
*   **Best Fix:** Create an interactive Index Chart where the user can click a specific point in time to re-normalize all series to that specific date [@heer_tour_2010].
