---
id: set-axis-range-deliberately
title: "Set quantitative axis ranges deliberately"

impact:
  - perceptual
  - cognitive
  - logos
  - ethos
  - ethical
tags:
  - y-axis
  - axis-truncation
  - bar-chart
  - line-chart
  - comparison
  - trend
  - deception

sources:
  - type: research
    ref: Correll, Bertini, & Franconeri, 2020
    url: https://doi.org/10.1145/3313831.3376222
    note: "Primary source. Found that axis truncation strongly biases perceived effect size, and that visual 'fixes' like broken axes do not mitigate this bias."
  - type: practitioner
    ref: Huff, 1993. How to Lie with Statistics.
    note: "Classic text popularizing the deceptive potential of truncated axes in 'Gee-Whiz Graphs'."
  - type: research
    ref: "Cleveland & McGill, 1984"
    url: https://doi.org/10.2307/2288400
    note: "Foundational work on graphical perception, establishing the importance of position and length for accurate comparisons."

examples:
  - type: bad
    description: "A bar chart where the y-axis starts at 34% instead of 0%. This makes a 4.6% increase in tax rate look like a 6x increase in bar height, visually exaggerating the effect."
  - type: bad
    description: "A line chart of global temperature where the y-axis starts at 0°F. This compresses the data range, making a significant warming trend appear almost flat and insignificant."
  - type: bad
    description: "A bar chart with a 'broken axis' glyph. Research shows these visual indicators do not effectively correct the perceptual bias caused by truncation; viewers still perceive the change as exaggerated."
---

## Guidance

When visualizing quantitative data with a bar or line chart, deliberately set the y-axis range to match your communicative intent. Do not automatically default to a zero-baseline without first considering the story in your data.

## Why

The range of a quantitative axis is one of the most powerful—and dangerous—tools in visualization design.

- **Truncating the axis** (starting it above zero) visually magnifies the differences between values. This makes small changes look large and dramatic.
- **Extending the axis** far beyond the data's range visually minimizes differences. This can make significant trends look flat and unimportant.

This powerful perceptual effect is not easily undone. Research shows that adding visual indicators like a "broken axis" symbol or gradient fills does not correct for the exaggerated perception of change. Viewers' judgments are driven by the magnified visual geometry of the chart, not by the intellectual awareness that the axis has been altered.

Your choice of axis range fundamentally frames the narrative. It is a design decision with ethical implications, not just a technical default.

## When it applies

- When using **bar charts**, where value is encoded by the length of the bars. Viewers instinctively compare lengths from a common baseline (zero).
- When using **line charts**, where value is encoded by the vertical position of points. Viewers judge trends by the slope of the lines.
- Whenever the primary goal is to communicate the size of a change, trend, or difference between values.

## Exceptions

A zero-baseline is a convention, not an iron-clad law. It is acceptable and often preferable to truncate the y-axis in these cases:

- **To show meaningful but subtle fluctuations.** For data with very small variations relative to its total value (e.g., stock prices, climate data, economic indicators), starting at zero would render the changes invisible. In these cases, truncating is necessary to make the trend perceptible.
- **When zero is not a meaningful baseline.** For data scales where zero is arbitrary (e.g., temperature in Celsius/Fahrenheit) or impossible (e.g., SAT scores), there is no logical requirement to include it.

## Trade-offs

- **Clarity vs. Proportionality:** Truncating an axis to make a trend visible sacrifices proportionality. In a truncated bar chart, a bar that is twice as tall does not represent a value that is twice as large, which can mislead viewers about absolute magnitudes.
- **Hiding Detail vs. Showing Context:** Sticking to a zero-baseline provides full context but may obscure important details. A chart showing CEO salary vs. employee salary from $0 would make any change in employee salary completely invisible.

## Evaluate

- [ ] Does a bar chart's quantitative axis start at a value other than zero?
- [ ] Is the axis range on a line chart so wide that a meaningful trend appears flat?
- [ ] Is the axis range on a line chart so narrow that normal, insignificant noise is exaggerated into a dramatic-looking trend?

## Repair

1.  **Clarify Your Intent.** First, decide on your primary message. Is it more important to show the true proportions between values (common for bar charts) or to highlight a subtle but important change over time (common for line charts)?
2.  **Set the Baseline to Match Intent.**
    - If comparing absolute magnitudes is key, **set the baseline to zero.**
    - If showing a subtle trend is key, **set the axis range to closely fit the data's variation.**
3.  **Use a Focus+Context Design as a Fallback.** If you need to show both a subtle trend *and* its context relative to zero, a single chart may not be sufficient. Consider a dual-chart approach: show the full zero-based chart alongside a "zoomed-in" chart that highlights the specific area of change.