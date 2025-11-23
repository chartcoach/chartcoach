---
id: aggregate-poll-sources
title: Show Data from Multiple Pollsters
bibliography: references.bib
description: Display results from various polling organizations to account for outliers
  and house effects.
labels:
- chart:split-bars
- task:compare
- visual:distribution
- impact:objectivity
- data:categorical
- source:external
---

## The Rule <!-- role: advice -->
Visualize data from multiple polling organizations rather than relying on a single source. If you cannot build a statistical aggregation model, use split bars to show deviating results.

## The Logic <!-- role: reason -->
Polls are not exact science; different organizations yield significantly different results due to methodologies or biases (e.g., "house effects").
*   **The Principle:** Bias Mitigation. Some pollsters may lean left or right, or simply get it wrong without bias. Looking at a single pollster risks presenting an outlier as the truth [@jockers_election_polls_2021].
*   **The Evidence:** In the example provided, one pollster (INSA) showed results biased toward the far right, while another (FG Wahlen) leaned left. Aggregating or displaying both reveals the uncertainty [@jockers_election_polls_2021].

## Where to Apply <!-- role: context -->
*   **User Goal:** Providing a neutral, comprehensive view of the political landscape.
*   **Data Type:** Polling data from multiple institutes covering the same time period.
*   **Audience:** Voters seeking an unbiased view of election probabilities.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When only one credible pollster is operating in the specific region or timeframe.
*   **Reason:** Lack of available data prevents comparison.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Space and Brevity. Showing multiple bars per party (split bars) takes up more vertical space than a single aggregated bar.
*   **The Risk:** The chart becomes denser and requires more reading effort from the user.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Picking the poll that aligns with the publication's political stance or the most "dramatic" poll.
*   **Why it fails:** It creates a misleading narrative based on outliers rather than the consensus.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the graphic cite only one source (e.g., "Source: XYZ Polling")?
*   **The Test:** Check if other major pollsters released data in the same week. If their numbers differ significantly and are excluded, the visualization is incomplete.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** List the results of other pollsters in the text or a table accompanying the chart.
*   **Best Fix:** Use a chart type that supports multiple data points per category, such as "split bars" (small multiples) where every pollster gets a bar for every party, allowing direct visual comparison of the spread.
