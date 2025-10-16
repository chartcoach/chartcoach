---
id: use-delta-charts-for-search
title: "Use delta charts to quickly find specific relational patterns"

tags:
  - impact:perceptual
  - impact:performance
  - chart:bar
  - chart:dot-plot
  - task:filter
  - task:lookup
  - data:quantitative
  - visual:position
  - visual:length
  - medium:static
  - medium:screen

evidence:
  strength: medium
  summary: "Nothelfer & Franconeri (2020, n=13) found that for visual search tasks, delta charts were staggeringly more efficient, accelerating search rates by 49-95% compared to charts showing individual values. This effectively transformed a slow serial search into a fast, near-parallel one."

sources:
  - type: research
    ref: Nothelfer & Franconeri, 2020
    url: https://doi.org/10.1109/TVCG.2019.2934801
    note: "Experiment 1 (n=13) measured visual search efficiency for a target relationship. Directly encoding deltas reduced search times from 164-266 ms per additional item to just 8-135 ms per item, a 49-95% improvement (p<0.001)."
    role: primary

---
## Guidance

To help users quickly locate a specific instance of a relationship (e.g., "find the only department that had a decrease"), represent the data using a delta chart.

## Why

Searching for a relationship between two separate marks (e.g., a short bar next to a tall bar) is a slow, serial cognitive task that requires focused attention on each pair. Searching for a single mark with a unique visual property (e.g., a single red bar, or the only bar below the zero line) is a much faster, often pre-attentive perceptual task. A delta chart converts the slow, difficult task into the fast, easy one.

### Core Principle

Transform serial cognitive tasks into parallel perceptual tasks for massive efficiency gains.

## When it applies

- When the user needs to perform a "find the odd one out" or "pop-out" task based on a relationship (e.g., increase vs. decrease, positive vs. negative).
- In dashboards or exploratory tools where a user is scanning a large amount of data for a specific pattern or anomaly.

## Exceptions

- When the absolute values of the items being searched are also important for identification. For example, if the task is "find the state with the biggest increase that started above $50M," a delta chart alone would be insufficient.

## Trade-offs

- Displaying only deltas removes the context of the original absolute values, which might be necessary for other tasks.

## Signs of Trouble

- **Slow Scanning:** Users have to slowly scan from pair to pair to find the one they are looking for, rather than the target "popping out."
- **High Error Rate:** Users frequently miss the target or select the wrong one because the search process is too mentally taxing.
- **User Complaints:** Users describe the task as "tedious" or "like finding a needle in a haystack."

## How to Improve

- **Comprehensive Approach: Use a Delta Chart.** Instead of a grouped bar chart showing 'before' and 'after' values, create a single bar chart showing the 'change'. The item to be found (e.g., the only decrease) will be visually distinct (e.g., the only bar pointing down or colored differently) and will pop out to the viewer.
