---
id: broken-axis-indicators-are-ineffective
title: "Do not rely on broken-axis indicators to fix the perceptual bias of a truncated axis"
tags:
  - impact:perceptual
  - impact:ethical
  - chart:bar
  - task:compare
  - task:trend
  - data:quantitative
sources:
  - type: research
    ref: "Correll et al., 2020"
    url: "https://doi.org/10.1145/3313831.3376222"
    note: "Experiment 2 found no significant difference in perceived severity between standard truncated bar charts and those with broken-axis or gradient-fill indicators, showing these cues do not correct the perceptual bias."
examples:
  - type: bad
    caption: A bar chart with a broken-axis glyph.
    description: "This chart uses a truncated y-axis but adds a 'break' symbol to indicate the non-zero baseline. While this signals transparency, it does not prevent the viewer from perceptually exaggerating the differences between the bars."
---
## Guidance
Avoid using a truncated axis and then attempting to "fix" it with a visual indicator like a broken-axis symbol (`~` or `//`) or a gradient fill. These visual elements do not correct the perceptual exaggeration of change.

## Why
Visual indicators signal that a truncation has occurred, but they do not de-bias the viewer. People still perceive the exaggerated effect size caused by the non-zero baseline, even when the truncation is explicitly marked. The brain processes the magnified visual difference in bar heights or line slopes regardless of the warning symbol on the axis.

## When it applies
- When designing a bar chart or line chart with a non-zero baseline.
- When you are tempted to truncate an axis to show detail but feel you should add an indicator to be "honest."

## Exceptions
While these indicators don't fix the perceptual bias, they can serve as a signal of **transparency**, showing the designer is intentionally truncating the axis and not trying to hide it. This is a matter of authorial ethos, but it's critical to understand that the misleading perceptual effect remains.

## Trade-offs
- Using an indicator adds visual complexity without solving the core perceptual problem. It creates a false sense of "honesty" while allowing the perceptual distortion to persist.

## Signs of Trouble
- **The "It's Okay, I Labeled It" Fallacy:** You've truncated an axis but believe it's acceptable simply because you added a "break" symbol.
- **Justified Deception:** A chart uses a dramatic truncated scale but includes a tiny, hard-to-see axis break as a fig leaf for the exaggeration.

## How to Improve
- **Quick Fix: Remove the Indicator and Fix the Axis.** The best course of action is to remove the ineffective indicator and set the axis to start at zero.

- **Comprehensive Approach: Reframe the Data.** Instead of indicating a break on a truncated chart, choose a chart type or framing that doesn't require one. To show small changes, create a separate chart of the *change itself* (a delta chart) which can be properly zero-based, or switch to a dot plot where position is not dependent on a zero-baseline.