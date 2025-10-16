---
id: select-axis-range-as-rhetorical-choice
title: "Intentionally select the y-axis range to frame the data's importance"
tags:
  - impact:ethical
  - impact:pathos
  - impact:logos
  - chart:bar
  - chart:line
  - chart:scatter
  - task:trend
  - task:compare
  - audience:general
sources:
  - type: research
    ref: "Correll et al., 2020"
    url: "https://doi.org/10.1145/3313831.3376222"
    note: "The authors conclude by rejecting a simple 'honest' vs. 'dishonest' dichotomy, arguing designers have a responsibility to consider and control the perceived effect size by selecting the axis range."
---
## Guidance
Recognize that choosing the y-axis range is a powerful rhetorical act, not a neutral technical setting. You are deciding how significant the data's variations should appear. There is no universally "honest" scale; the choice depends on the story you are telling and the real-world meaning of the data.

## Why
The perceived effect size is directly controlled by the y-axis range. A wide range (e.g., starting at zero) minimizes the perceived visual effect, while a narrow, truncated range amplifies it. Instead of searching for a single "correct" scale, designers must consciously weigh this trade-off and take responsibility for the resulting perception their chart creates.

## When it applies
- Always, when designing a chart with a quantitative axis (e.g., bar, line, area, scatter plot).
- When deciding whether to start an axis at zero or to truncate it to show more detail.

## Exceptions
None. This is a fundamental principle about the designer's mindset and responsibility, which always applies.

## Trade-offs
- **Detail vs. Context:** Highlighting small fluctuations (with a truncated axis) sacrifices the "big picture" context of the overall magnitude. Showing the big picture (with a zero-based axis) can obscure small but meaningful details.
- **Rhetorical Goal vs. "Neutrality":** A zero-baseline is often seen as more neutral, but it is also a rhetorical choice that downplays variation. Choosing to amplify variation is also a valid rhetorical choice, provided it is done intentionally and ethically.

## Signs of Trouble
- **Default Settings:** Accepting the default axis range from your software without considering its rhetorical impact.
- **Seeking a Single Rule:** Looking for a simple, universal rule (e.g., "always start at zero" or "always show the data range") without considering the specific data story.
- **Unintended Exaggeration:** A chart makes a minor business fluctuation look like a catastrophic event, causing undue alarm.
- **Unintended Minimization:** A chart makes a critical public health trend look flat and insignificant, causing undue complacency.

## How to Improve
- **Minimal: Self-Critique.** Before publishing, ask yourself: "Does the visual prominence of the change in this chart match its real-world importance?" Adjust the axis range to better align the visual with the contextual meaning.

- **Moderate: Add Framing Text.** Write a descriptive title, subtitle, or annotation that frames the data for the reader. For example, a chart with a dramatic truncated axis could have a title like "A Small but Steady Increase: Quarterly Profits Rise 0.5%." This provides verbal context to temper the visual.

- **Comprehensive: Test with Users.** Show your chart to a few colleagues or target users. Ask them "What is the main takeaway from this chart?" or "How significant does this change seem to you?" If their perception doesn't match the intended message, adjust the axis range or chart design.