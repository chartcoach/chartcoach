---
id: use-linear-charts-for-daily-patterns
title: "Use Linear Bar Charts over Radial Rose Charts for Visualizing Daily Patterns"

tags:
  - impact:perceptual
  - impact:cognitive
  - impact:performance
  - chart:bar
  - chart:line
  - chart:pie
  - data:temporal
  - data:periodicity.24h
  - task:compare
  - task:lookup
  - task:rank
  - task:find-extremum
  - audience:general
  - medium:screen
  - medium:static
  - access:cognitive-load-risk

evidence:
  strength: high
  summary: "Waldner et al. (2020, n=92) found that 24-hour linear bar charts are significantly more accurate, efficient (p<0.001), and preferred by users for analyzing daily patterns compared to all tested radial rose chart variants. Linear layouts were 1.2 points higher on a 5-point preference scale."

sources:
  - type: research
    ref: Waldner et al., 2020
    url: https://doi.org/10.1109/TVCG.2019.2934784
    note: "Primary controlled experiment (n=92) directly comparing linear and radial layouts for daily time-series data. Found linear charts were faster for all low-level tasks (p<0.001, η²p=0.126 to 0.259) and received significantly higher subjective ratings (p<0.001, η²p=0.488)."
    role: primary
  - type: research
    ref: "Cleveland & McGill, 1984"
    url: https://doi.org/10.2307/2288400
    note: "Foundational work showing that position judgments (used in bar charts) are more perceptually accurate than angle or area judgments (used in rose/pie charts)."
    role: supporting
  - type: research
    ref: Goldberg & Helfman, 2011
    url: https://doi.org/10.1057/ivs.2011.8
    note: "Eye-tracking study showing value lookups are more efficient on linear graphs than radial graphs."
    role: supporting

examples:
  - type: good
    description: A 24-hour linear bar chart, the most effective design found in the study. It is easy to read, compare values, and find the maximum.
    url: https://i.imgur.com/8QjU3oE.png
    caption: A single, 24-hour linear bar chart.
  - type: bad
    description: A 24-hour radial rose chart. This design was found to be less accurate, slower to read, and less preferred by users than a simple linear bar chart.
    url: https://i.imgur.com/G5qE3yW.png
    caption: A 24-hour radial rose chart.
---

## Guidance

When visualizing periodic daily data (e.g., traffic over 24 hours), use a standard linear bar chart instead of a radial (rose) chart.

## Why

Linear bar charts are significantly more accurate, faster to read, and preferred by general audiences than radial rose charts for analyzing daily patterns. Viewers are more familiar with linear layouts, reducing cognitive load and the risk of misinterpretation. Radial charts, which rely on less accurate angle and area judgments, are often perceived as confusing and unusual, even when they resemble a clock.

### Core Principle

Choose familiar and perceptually effective encodings over novel or metaphorical ones. Human perception is more accurate at judging position and length along a common scale (as in a bar chart) than it is at judging angles or areas (as in a rose chart).

## When it applies

- When visualizing time-series data with a 24-hour periodic pattern.
- When the audience is a general one, without specialized training in reading radial charts.
- When the primary tasks include comparing values, finding the highest or lowest points, or looking up a value at a specific time.

## Exceptions

- When visualizing directional data, such as wind direction and speed, for which a radial "wind rose" is a strong and widely understood convention among experts (e.g., meteorologists).
- In artistic or infographic contexts where aesthetic appeal and engagement are prioritized far above decoding accuracy and speed, and the data is simple. Be aware this choice sacrifices clarity.

## Trade-offs

- **Clarity vs. Aesthetics:** A linear bar chart is clearer but may be perceived as less "fancy" or "engaging" than a circular rose chart. The research shows this aesthetic appeal comes at a high cost to comprehension.
- **Space Efficiency:** A single 24-hour radial chart can be more compact (squarer aspect ratio) than a long 24-hour linear bar chart. However, this space saving is not worth the significant drop in performance and accuracy.

## Signs of Trouble

- **User Feedback:** Viewers say the chart is "confusing," "hard to read," or that they "don't know where to start."
- **Task Errors:** Users make frequent mistakes when asked to find the highest value or compare two time points.
- **Slow Performance:** It takes viewers a long time to answer simple questions about the data.
- **Metaphor Failure:** Viewers mention it "looks like a clock" but still can't interpret it correctly, or don't make the connection at all.

## How to Improve

- **Comprehensive Redesign: Switch to a Linear Bar Chart.** The most effective fix is to replace the radial rose chart with a standard linear bar chart.
  - **Ideal:** Use a single, continuous 24-hour linear bar chart. This is the top-performing design for accuracy, efficiency, and user preference.
  - **Alternative:** If space is a major constraint, you could use two juxtaposed 12-hour linear bar charts (e.g., one for AM, one for PM). Be aware this makes it harder to see the global maximum and can introduce a slight reading bias.