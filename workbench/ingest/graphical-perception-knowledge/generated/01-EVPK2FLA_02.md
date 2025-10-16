---
id: avoid-clock-like-radial-layouts
title: "Avoid Using Clock-Like Radial Layouts for Time-Series Data"

tags:
  - impact:cognitive
  - impact:perceptual
  - chart:pie
  - chart:bar
  - data:temporal
  - data:periodicity.24h
  - audience:general
  - access:cognitive-load-risk

evidence:
  strength: high
  summary: "A study by Waldner et al. (2020, n=92) explicitly tested the intuitiveness of a 12-hour clock-like rose chart for daily patterns and found the metaphor failed. This design was the most error-prone (30% error rate for locating time) and least-preferred, causing significant user confusion and incorrect AM/PM swaps."

sources:
  - type: research
    ref: Waldner et al., 2020
    url: https://doi.org/10.1109/TVCG.2019.2934784
    note: "Primary experiment refuting the central hypothesis that a clock metaphor aids interpretation. The 12-hour radial chart (12r) had the highest error rates and lowest subjective rating (2.95/5). User feedback highlighted confusion: 'I found it very hard to read initially... This is very confusing.'"
    role: primary

examples:
  - type: good
    description: A standard linear bar chart is less novel but far more effective and less confusing for showing daily patterns.
    url: https://i.imgur.com/8QjU3oE.png
    caption: A 24-hour linear bar chart.
  - type: bad
    description: The 12-hour radial rose chart is designed to look like an analog clock. This metaphor, while tempting, was empirically shown to be confusing and ineffective. The ambiguity of the '12' at the top (noon or midnight?) and the unnatural reading path led to high error rates.
    url: https://i.imgur.com/P5993jO.png
    caption: A 12-hour clock-like radial rose chart.
---

## Guidance

Do not use a radial, clock-like layout to visualize daily time-series data, even though the metaphor seems intuitive. The presumed benefit of the clock metaphor does not translate into better performance and often leads to confusion.

## Why

The skills used to read an analog clock (interpreting the orientation of thin hands) do not transfer to interpreting the length or area of segments in a radial chart. This mismatch between the familiar task (reading a clock) and the novel one (reading a rose chart) creates significant cognitive friction. A clock-like radial layout introduces ambiguity (e.g., is the 12 at the top noon or midnight?), breaks the natural left-to-right reading order, and combines the known perceptual weaknesses of radial charts with the problems of chart separation.

### Core Principle

A visual metaphor is only effective if the cognitive process it evokes matches the task required to decode the chart. If the metaphor suggests one process (reading clock hands) but the chart requires another (judging segment lengths), the metaphor will hinder, not help.

## When it applies

- When visualizing data over a 24-hour or 12-hour cycle.
- When considering a radial chart because its circular nature seems to map well to the cyclical nature of time.
- When designing for a general audience that is familiar with analog clocks.

## Exceptions

- None known for improving perceptual accuracy or speed. The study's central finding was a direct refutation of this specific use case. The presumed benefit was empirically disproven. Any use should be for purely aesthetic reasons with a full understanding of the negative impact on clarity.

## Trade-offs

- **Novelty vs. Clarity:** A clock-like chart might look more novel or creative, but this comes at a direct and significant cost to readability, accuracy, and user confidence. Choosing this design is an explicit decision to prioritize novelty over effective communication.

## Signs of Trouble

- **AM/PM Errors:** Users frequently mix up AM and PM values, selecting the correct hour but in the wrong half of the day.
- **Confusion at Noon/Midnight:** Users are unsure how to interpret the value at the top of the circle, where the AM/PM charts are implicitly joined or separated.
- **Explicit Confusion:** Users state, "It looks like a clock, but it's hard to read," or "I was trying to figure out if the 12pm on the left was for PM or AM."
- **High Error Rates:** Task accuracy is low, particularly for tasks that involve locating a specific time or comparing times across the AM/PM divide.

## How to Improve

- **Comprehensive Redesign: Switch to a Linear Layout.** Abandon the clock metaphor entirely and switch to a standard linear bar chart. This is the most effective way to eliminate the source of confusion and improve performance across the board. A single 24-hour linear bar chart was found to be the most effective design overall.