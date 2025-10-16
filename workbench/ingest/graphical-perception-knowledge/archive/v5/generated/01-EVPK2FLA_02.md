---
id: avoid-clock-metaphor-fallacy
title: "Do not assume a clock-like radial layout is inherently intuitive"
tags:
  - impact:cognitive
  - impact:perceptual
  - impact:aesthetic
  - chart:pie
  - data:periodicity.24h
  - audience:general
  - access:cognitive-load-risk
evidence:
  strength: medium
  summary: "A 2020 study directly tested a 12-hour clock-like radial chart for daily data and found it was the least preferred and most error-prone format. Users found it confusing and could not effectively apply their clock-reading skills to data interpretation."
sources:
  - type: research
    ref: "Waldner et al., 2020"
    url: https://doi.org/10.1109/TVCG.2019.2934784
    note: "The 12-hour radial chart, designed to mimic an analog clock, received the lowest subjective ratings and had the highest error rates on tasks like locating a specific time and reading a value."
    role: primary
examples:
  - type: bad
    caption: 12-Hour Clock-like Radial Chart
    description: "This design attempts to use the familiar metaphor of an analog clock. However, users found it difficult to decipher and it performed worse than all other tested formats, including a non-metaphorical 24-hour radial chart."
    url: https://i.imgur.com/GzQvHl2.png
---
## Guidance

Avoid using radial charts for daily patterns under the assumption that their resemblance to an analog clock makes them more intuitive.

## Why

While the clock metaphor seems appealing, empirical evidence shows it does not translate into better performance. People are trained to read the *orientation of hands* on a clock, not to judge the length or area of *segments* in a corresponding position. This mismatch leads to confusion, high error rates, and poor user satisfaction. The study found this format had the lowest subjective rating and the highest error rates for locating time and reading values, demonstrating that the metaphor fails to provide its promised cognitive benefit.

### Core Principle
A visual metaphor is only effective if the viewer's mental model of the source domain (e.g., a clock) maps directly to the visual decoding task required by the chart. If the tasks do not align, the metaphor becomes a source of confusion.

## When it applies
- When choosing a chart type for visualizing data with a 24-hour cyclical pattern, such as daily website traffic, energy usage, or social media activity.
- When designing for a general audience who may be tempted by the apparent familiarity of a clock face.

## Exceptions
- None known for data analysis tasks. The only potential exception is for purely decorative or artistic purposes where emotional engagement is the sole priority and data accuracy is irrelevant.

## Trade-offs
- You may sacrifice a design that feels 'creative' or 'novel' in favor of a more conventional but effective one, like a standard bar chart.

## Signs of Trouble
- **Explicit Confusion:** Users say things like, "I know it looks like a clock, but I can't figure out what the bars mean," or "This is very confusing."
- **High Error Rates:** The chart performs poorly on basic tasks. In the study, users frequently swapped AM and PM or struggled to locate the correct hour on the 12-hour radial chart.
- **Low Preference:** When given a choice, users actively dislike the clock-like chart and prefer a simpler format. It received the lowest average rating (2.95/5) in the study.

## How to Improve
- **Switch to a Linear Format.** The most effective action is to abandon the clock metaphor and use a standard 24-hour linear bar chart. It is more effective, efficient, and preferred by users.
- **Use a Non-Metaphorical Radial Chart (If Necessary).** If a radial format is required for space or other reasons, a continuous 24-hour radial chart performed better and was rated higher than the 12-hour clock-like version, suggesting it's better to avoid the confusing metaphor altogether.