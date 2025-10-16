---
id: set-yaxis-to-meaningful-scale
title: "Set Y-Axis Range to Match the Scale of Meaningful Change"
tags:
  - impact:perceptual
  - impact:ethical
  - impact:logos
  - chart:bar
  - chart:line
  - task:compare
  - task:trend
  - task:direction
  - data:quantitative
  - audience:general
  - medium:static
evidence:
  strength: medium
  summary: "Correll et al. (2020) found in 3 crowd-sourced experiments (n=40, 32, 25) that truncating the y-axis consistently and significantly increased perceived effect size (p < 0.001). This suggests designers have direct control over perceived importance and should select a range that reflects the domain-specific significance of the data's variation."
sources:
  - type: research
    ref: Correll, Bertini, & Franconeri, 2020
    url: https://doi.org/10.1145/3313831.3376222
    note: "Primary study with three experiments (n=40, 32, 25) showing that y-axis truncation consistently and significantly increases the perceived severity of effect sizes across bar charts, line charts, and charts with 'broken axis' cues."
    role: primary
  - type: practitioner
    ref: Huff, 1993
    note: "Classic text that established the dogmatic view of truncated axes as 'lying with statistics,' which this research re-examines and adds nuance to."
    role: related
examples:
  - type: bad
    description: "A bar chart of tax rates is truncated from 34% to 42%, making a 4.6% increase look like a 6x increase. This exaggerates a minor change."
  - type: good
    description: "A stock chart is truncated to show small but financially significant daily fluctuations. A zero-baseline would render these critical changes invisible."
---
## Guidance

Instead of always defaulting to a zero-baseline, consciously select the y-axis range to match the scale of variation that is meaningful for your data and communication goal.

## Why

Truncating the y-axis visually magnifies the differences between data points. While often seen as deceptive, this magnification can also be used intentionally to highlight small but important changes that would be invisible on a zero-based scale. Experiments show that the perceived severity of a change is directly tied to the y-axis range you select.

### Core Principle

The perceived magnitude of a change is relative to its visible container, not just its absolute numerical value. The designer is responsible for aligning visual salience with data significance.

## When it applies

- When visualizing quantitative data where small absolute changes have significant real-world implications (e.g., stock prices, climate data, clinical trial results).
- When your primary goal is to show a trend, pattern, or small variations over time, and a zero-baseline would flatten the data into an unreadable line.

## Exceptions

- When showing part-to-whole relationships where the sum of parts is meaningful.
- When strict proportional accuracy to a zero baseline is the primary communication goal (e.g., showing budget allocations where the relative size of each bar must represent its share of the total).

## Trade-offs

- You trade proportional accuracy (relative to zero) for the ability to see and emphasize fine-grained trends and variations.
- This increases the risk that the audience will perceive changes as more dramatic than they are in absolute terms, which can be an ethical concern if not handled carefully.

## Signs of Trouble

- **Triviality Magnified:** A chart where the y-axis is truncated, making trivial or statistically insignificant fluctuations look like major events.
- **Flattened Importance:** A zero-baselined chart where a critically important trend is flattened into a nearly straight, unreadable line.
- **Story Mismatch:** The visual story told by the chart's dramatic slopes or bar height differences feels disconnected from the actual numerical change.

## How to Improve

- **Quick approach:** Add clear annotations that state the magnitude and importance of the change in plain language (e.g., "This 0.5°C rise is considered a critical threshold by scientists").
- **Moderate approach:** Create multiple versions of the chart with different y-axis ranges (e.g., zero-baseline, tight-range) and choose the one that best reflects the significance of the story in the data. Solicit feedback from a colleague to see if their perceived takeaway matches your intent.
- **Comprehensive approach:** Use a focus+context technique. Show the detailed, truncated view alongside a smaller "inset" chart that is zero-baselined, giving the viewer both the detailed trend and the overall context.
