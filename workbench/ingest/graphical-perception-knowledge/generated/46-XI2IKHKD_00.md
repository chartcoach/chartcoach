---
id: use-bar-charts-for-finding-extremes
title: "Use bar charts to find the highest or lowest values"

tags:
  - impact:perceptual
  - impact:performance
  - chart:bar
  - task:rank
  - task:lookup
  - data:quantitative
  - data:categorical
  - visual:length
  - visual:position
  - audience:general
  - medium:static

evidence:
  strength: medium
  summary: "In a crowdsourced experiment (n=180), Saket et al. (2019) found bar charts were significantly faster for finding extremum values (min/max) than tables and pie charts (p<0.05). Bar charts were also rated as significantly more preferred by users for this task than all other tested visualizations (line, scatter, pie, table)."

sources:
  - type: research
    ref: Saket et al., 2019
    url: https://doi.org/10.1109/TVCG.2018.2829750
    note: "Primary experiment (n=180) comparing five chart types on ten tasks. For 'Find Extremum', bar charts were significantly faster (p<0.05, η²=0.38) and overwhelmingly preferred by users (p<0.05, η²=0.61)."
    role: primary
  - type: research
    ref: Zeng & Battle, 2023
    url: https://doi.org/10.1145/3544548.3581349
    note: "This meta-review synthesizes empirical findings, including Saket et al.'s, and recommends bar charts for 'Find Extremum' tasks in its summary (Table 9)."
    role: supporting

---

## Guidance

When users need to quickly identify the largest or smallest value in a dataset, use a bar chart.

## Why

Bar charts encode quantitative values as length, with all bars starting from a common baseline (zero). This visual encoding allows for rapid and accurate pre-attentive comparison, making it easy to spot the longest or shortest bar at a glance. Studies confirm that this leads to faster task completion and higher user preference compared to other chart types.

### Core Principle

Humans can compare lengths along a common, aligned scale more quickly and easily than they can compare areas, angles, or non-aligned positions. Making the most important comparison (finding the extreme) perceptually easy improves performance.

## When it applies

- The primary task is to find the maximum or minimum value among a set of categories.
- You are comparing quantitative values across discrete categories.
- The number of categories is manageable (typically under 20-30).

## Exceptions

- If the data has a very large number of categories, a bar chart may become cluttered. In such cases, a sorted table or a simple sentence stating the maximum/minimum might be more effective.
- If the goal is to see the extreme value *in relation to a total*, a pie chart can also be effective, though it is less preferred and may be slower.

## Trade-offs

- Bar charts use more space than a simple text statement of the result.
- While great for finding extremes, they are less effective for showing correlation or distribution tasks, so they may not be the best choice if the user needs to perform multiple, varied tasks.

## Signs of Trouble

- **Slow Search:** Users are scanning the visualization for a long time, reading each value sequentially, to find the highest or lowest one.
- **Inaccurate Clicks:** When asked to identify the extreme, users select the wrong item, especially in a pie chart where a visually small slice might represent a large value if other slices are fragmented.
- **Low Confidence:** Users express uncertainty about their answer or complain that it's "hard to tell."

## How to Improve

- **Quick Fix: Sort the Chart.** If using another chart type, simply sorting the data from highest to lowest (or vice versa) can make the extreme value immediately apparent as the first or last item.

- **Moderate Redesign: Switch to a Bar Chart.** If you are using a pie chart, line chart, or scatterplot, convert it into a horizontal or vertical bar chart. This is the most direct way to improve performance for this specific task.

- **Comprehensive Approach: Highlight the Extreme.** Use a bar chart and add a highlight color or annotation to the extreme value (the longest or shortest bar). This removes any ambiguity and directs the user's attention immediately, combining the strong perceptual cue of length with a pre-attentive visual highlight.