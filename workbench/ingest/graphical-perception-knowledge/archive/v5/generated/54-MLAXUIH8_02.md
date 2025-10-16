---
id: broken-axis-glyphs-are-ineffective
title: "Do not rely on broken-axis glyphs to fix a truncated chart"

tags:
  - impact:perceptual
  - impact:ethical
  - impact:cognitive
  - chart:bar
  - chart:line
  - visual:shape
  - task:compare
  - task:trend

evidence:
  strength: medium
  summary: "Visual cues intended to signal a truncated y-axis, such as a 'break' symbol (//) or a gradient at the base of bars, do not significantly reduce the perceptual exaggeration caused by truncation. A 2020 study found no significant difference in inflated 'perceived severity' between a standard truncated bar chart and versions with these explicit visual cues (p > 0.05)."

sources:
  - type: research
    ref: "Correll, Bertini, & Franconeri, 2020"
    url: "https://doi.org/10.1145/3313831.3376222"
    note: "Experiment 2 tested bar charts with broken axes and gradient-bottoms against standard truncated bar charts. The results showed 'no significant difference between perceived severity among visualization designs' (F(2,60) = 3.1, p = 0.05, with post-hoc tests failing to find any significant pairs). This suggests these visual indicators fail to de-bias the viewer."
    role: primary

examples:
  - type: bad
    description: "This design uses a 'break' symbol on the y-axis and in the bars themselves. While it signals that truncation has occurred, research shows this is not effective at correcting the viewer's inflated perception of the differences."
    url: https://i.imgur.com/kS5x87J.png
    caption: "A bar chart with broken axis symbols."
  - type: bad
    description: "This design uses a gradient fill at the bottom of the bars to connote that they 'continue' below the axis. This also failed to reduce the perceptual exaggeration of truncation in experiments."
    url: https://i.imgur.com/uC5EaLg.png
    caption: "A bar chart with a gradient fill to indicate continuation."
---

## Guidance

Do not use visual indicators like a broken-axis symbol (`//`) or a gradient fill as a "fix" for a truncated y-axis. These techniques do not counteract the perceptual distortion they are meant to excuse.

## Why

The exaggeration caused by a truncated axis is a powerful, immediate perceptual effect based on the relative lengths and slopes viewers see. A small, symbolic glyph on an axis is a cognitive cue, not a perceptual one. Viewers must notice the symbol, understand its meaning, and then consciously attempt to adjust their initial visual judgment. Research shows this process is ineffective; the initial misleading impression persists, and perceived effect size remains just as inflated as it would be without the symbol.

## When it applies

-   When you have truncated the y-axis of a bar or line chart and are considering adding a visual mark to indicate the break.
-   When evaluating charts that use these symbols to justify a non-zero baseline.

## Exceptions

None known. While these symbols may signal honest intent, they are not effective at preventing misperception. It is better to address the truncation directly than to apply an ineffective visual patch.

## Trade-offs

-   **Apparent Honesty vs. Actual Clarity:** Using a broken-axis symbol might feel like a more honest way to present a truncated chart, but it provides a false sense of security. It gives the designer an excuse for a poor practice without actually helping the viewer. The trade-off is sacrificing genuine perceptual clarity for the appearance of transparency.

## Signs of Trouble

-   **The "It's Okay, There's a Squiggle" Defense:** A chart has a clearly truncated axis, but the designer points to a small `//` symbol or a wavy line as justification.
-   **A Glyph Doing Heavy Lifting:** The chart relies entirely on a small, non-data symbol to correct a fundamental flaw in the chart's construction.

## How to Improve

Instead of using a symbol to excuse truncation, choose a better method to begin with.

-   **Minimal: Remove the Glyph and Re-evaluate.** Take away the broken-axis symbol. Does the chart now feel deceptive? If so, the symbol wasn't fixing the problem. This forces you to confront the impact of the truncation itself.

-   **Moderate: Use Focus + Context.** Instead of just breaking the axis, use a technique with two linked panels. One panel (the "context") shows the full zero-based axis, while the other (the "focus") is a "magnifying glass" view of the truncated section. This gives the viewer both the honest overview and the detailed view.

-   **Comprehensive: Choose a Better Chart Type or Framing.**
    -   If you must show data in a narrow range, switch to a **dot plot**.
    -   If the story is about the *difference* between two points, create a new chart that visualizes that difference directly.
    -   If the story is about *change over time*, consider an index chart.