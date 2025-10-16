---
id: start-bar-axis-at-zero-for-magnitude
title: "Start bar chart axes at zero when showing magnitude"

tags:
  - impact:perceptual
  - impact:ethical
  - impact:logos
  - chart:bar
  - task:compare
  - task:rank
  - data:quantitative
  - audience:general
  - medium:static
  - medium:interactive

evidence:
  strength: high
  summary: "Truncating the y-axis of a bar chart systematically inflates the perceived magnitude of differences. A 2020 study confirmed that truncating the axis to start at 50% vs 0% caused a significant increase in the 'perceived severity' of the data, an effect consistent with decades of visualization best practices."

sources:
  - type: research
    ref: "Correll, Bertini, & Franconeri, 2020"
    url: "https://doi.org/10.1145/3313831.3376222"
    note: "Primary study finding that y-axis truncation consistently and significantly inflates perceived effect size in bar charts (Experiment 1, F(2,76) = 89, p < 0.0001). This effect persisted even when visual cues for truncation were added (Experiment 2)."
    role: primary
  - type: practitioner
    ref: "Huff, 1993. How to Lie with Statistics"
    note: "Classic text identifying non-zero baselines in bar charts as a primary method of statistical deception, terming them 'Gee-Whiz Graphs'."
    role: supporting
  - type: practitioner
    ref: "Cairo, 2019. How Charts Lie"
    note: "Modern practitioner guide advising a zero baseline for any chart where encoding is done by height or length."
    role: related

examples:
  - type: bad
    description: "This bar chart from Fox News starts the y-axis at 34%, making a 4.6% difference in tax rates appear like a 6-fold increase. The second bar is visually 6 times taller than the first, breaking the principle of proportionality."
    url: https://i.imgur.com/g8nO71d.png
    caption: "A bar chart with a truncated y-axis from Fox News, as analyzed in the source paper."
  - type: good
    description: "By starting the y-axis at 0%, the same data is shown without visual exaggeration. The relative heights of the bars are now proportional to their values, providing an honest comparison of magnitudes."
    url: https://i.imgur.com/rQ0YvKz.png
    caption: "The same data as the 'bad' example, but with a proper zero baseline."
---

## Guidance

When using a bar chart to show and compare the magnitude of values, always start the quantitative axis at zero.

## Why

Bar charts encode numerical values through the length of the bars. Our visual system instinctively compares these lengths to judge the difference between values. Starting the axis at a value other than zero truncates the bars, destroying the proportional relationship between the bar's actual length and the data value it represents. This creates a misleading visual exaggeration, making small differences appear large and significant.

### Core Principle

The visual representation of a number should be directly proportional to the number itself. Truncating a bar chart's axis violates this principle.

## When it applies

-   When using bar charts, column charts, or area charts where the length or area from a baseline is the primary visual encoding for magnitude.
-   When the primary task for the viewer is to compare the absolute size of different categories (e.g., "How big is A compared to B?").

## Exceptions

-   **When showing small but critical changes:** In rare cases, such as visualizing stock price fluctuations or scientific measurements in a very narrow band, a zero baseline might render important changes invisible.
-   **When using dot plots:** A dot plot encodes value using position, not length. Therefore, it is less susceptible to this type of distortion and can be a good alternative for showing values in a narrow range.

Even in these exceptional cases, be aware you are still visually amplifying the differences. It is not a neutral act.

## Trade-offs

-   **Clarity vs. Detail:** A zero-based axis provides an honest representation of magnitude but may obscure small, yet meaningful, variations. Truncating the axis highlights these small variations but at the cost of perceptual accuracy and potential deception.

## Signs of Trouble

-   **Non-Zero Baseline:** The most obvious sign—the quantitative axis on a bar chart starts at a value other than 0.
-   **The "Half is Not Half" Test:** Find a bar that is roughly half the height of another. If its data label is not close to half the value, the axis is likely truncated.
-   **Exaggerated Headlines:** The chart is used to support a dramatic claim (e.g., "Profits Skyrocket!") but the axis reveals the change is numerically small.

## How to Improve

-   **Quick Fix: Reset the Axis.** The most direct and honest solution is to change the axis to start at 0.

-   **Moderate Approach: Add Direct Labels.** If you must truncate for contextual reasons, add clear data labels to the end of each bar. This provides a "cognitive escape hatch," allowing diligent viewers to read the true values, but it does not fix the initial misleading visual impression.

-   **Comprehensive Redesign: Change the Chart Type.** If a zero-based bar chart hides the story, the story might be about change, not magnitude.
    -   Switch to a **dot plot** or **slope chart**. These encode value by position, not length, and are better suited for showing small changes in a narrow numerical range without the expectation of a zero baseline.
    -   Directly visualize the *change* or *difference* itself with a new bar chart (that starts at zero).