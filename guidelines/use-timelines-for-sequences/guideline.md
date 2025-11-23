---
id: use-timelines-for-sequences
title: Use Timelines for Sequences
bibliography: references.bib
description: Visualize time-based data using standard linear timelines to aid pattern
  recognition and reduce cognitive load.
labels:
- chart:timeline
- data:temporal
- task:trace
- impact:clarity
- impact:interpretability
---

## The Rule <!-- role: advice -->

Present time-related data using linear timelines or chronological sequences to clarify ordering and trends.

## The Logic <!-- role: reason -->

Time is naturally perceived as a linear sequence. Using standard timeline formats reduces the cognitive load required to translate visual positions into temporal concepts.

*   **The Principle:** **Temporal Schemas.** Readers rely on familiar patterns (like left-to-right progression) to deduce causality and sequence. deviating from this requires extra mental processing.
*   **The Evidence:** Field notes indicate that designs combining different timescales or lacking clear linearity make interpretation difficult. Simpler timelines help participants trace patterns and make sense of temporal data [@koesten_what_2023].

## Where to Apply <!-- role: context -->

Use this approach whenever the sequence of events is central to the insight.

*   **User Goal:** Understanding the history of a subject, tracing cause-and-effect, or identifying trends over a period.
*   **Data Type:** Time-series data, logs, historical events, or process steps.
*   **Audience:** Users who need to construct a narrative from the data.

## When to Break It <!-- role: exceptions -->

*   **Scenario:** Analyzing cyclical patterns (e.g., seasonality, circadian rhythms).
*   **Reason:** A linear timeline may obscure the relationship between the end of one cycle and the beginning of the next. Radial charts or calendar heatmaps may be more appropriate.
*   **Scenario:** Comparing duration distributions rather than sequence.
*   **Reason:** If the goal is to compare how long things take, regardless of *when* they happened, a histogram is better than a timeline.

## The Price <!-- role: costs -->

*   **The Sacrifice:** Horizontal screen real estate. Timelines often require significant width to prevent label overlapping.
*   **The Risk:** In high-density datasets, a single timeline can become cluttered, obscuring individual data points.

## Common Mistakes <!-- role: mistakes -->

*   **The Wrong Fix:** Combining multiple inconsistent timescales (e.g., mixing hours and months arbitrarily) on a single axis.
*   **Why it fails:** As found in the evidence, mixed timescales create "cluttered designs" that confuse the viewer's internal clock and break the narrative flow.
*   **The Wrong Fix:** Ordering time-based categories by value (magnitude) rather than chronology.
*   **Why it fails:** It destroys the ability to see trends or sequences.

## How to Check <!-- role: check -->

*   **Visual Sign:** Are the data points scattered without a clear left-to-right or top-to-bottom flow?
*   **The Test:** Can you determine which event happened first and which happened last without reading the specific date labels?

## How to Fix <!-- role: fix -->

*   **Quick Fix:** Sort your axis chronologically.
*   **Best Fix:** Convert the visualization to a Line Chart, Gantt Chart, or a dedicated Timeline component that strictly enforces linear time progression.
