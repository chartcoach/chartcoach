---
id: visualize-polling-trends
title: Visualize Polling Changes Over Time
bibliography: references.bib
description: Use line charts with context annotations to show how public opinion shifts
  during a campaign.
labels:
- chart:line
- task:trend
- visual:annotations
- impact:context
- data:temporal
- audience:public
---

## The Rule <!-- role: advice -->
Move beyond snapshot reporting by showing how polls change over time. Use line charts combined with text annotations to explain shifts.

## The Logic <!-- role: reason -->
A single poll is a static snapshot, but public opinion is dynamic and reacts to campaign events.
*   **The Principle:** Temporal Context. Voters make decisions based on processes and events (scandals, nominations). Showing the trend helps explain *why* numbers are rising or falling [@jockers_election_polls_2021].
*   **The Evidence:** An example shows the Green Party experiencing an upswing after a candidate announcement, followed by a plummet due to negative campaigning. A bar chart of the final week would hide this dramatic narrative [@jockers_election_polls_2021].

## Where to Apply <!-- role: context -->
*   **User Goal:** Explaining the "horse race" dynamics or the impact of specific political events.
*   **Data Type:** Longitudinal polling data (weekly averages or repeated polls).
*   **Audience:** Readers trying to understand the momentum of a campaign.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Immediate breaking news where only the very first poll is available.
*   **Reason:** No historical data exists yet to establish a trend.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Focus on the "now." A trend chart emphasizes the journey, whereas a bar chart emphasizes the current state.
*   **The Risk:** Line charts with many parties can become "spaghetti charts" if not managed with proper coloring or highlighting.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Showing only the most recent numbers without context.
*   **Why it fails:** It ignores momentum (e.g., a party might be in second place but rapidly gaining, which is politically significant).

## How to Check <!-- role: check -->
*   **Visual Sign:** Is the visualization purely static (e.g., a simple bar chart) despite the campaign lasting months?
*   **The Test:** Ask "How did we get here?" If the chart cannot answer that question, it lacks temporal context.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a "Previous week" comparison value (e.g., "+2%" or "-1%").
*   **Best Fix:** Plot the polling averages on a timeline and add annotations for key events (e.g., "Candidate X announced," "TV Debate") to correlate events with shifts in data.
