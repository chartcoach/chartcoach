---
id: avoid-line-charts-for-precise-lookup
title: "Avoid line charts when users need to look up precise values"

tags:
  - impact:perceptual
  - impact:performance
  - chart:line
  - task:lookup
  - data:quantitative
  - audience:general
  - medium:static

sources:
  - type: research
    ref: Saket et al., 2019
    url: https://doi.org/10.1109/TVCG.2018.2829750
    note: "The study found that line charts had the lowest aggregate accuracy and speed, attributing the low performance on tasks like 'Retrieve Value' to the difficulty of precisely identifying values between axis ticks (Guideline G4)."

examples:
  - type: bad
    description: A line chart shows monthly sales. A user is asked for sales in March, but the data point for March falls between the $100K and $200K gridlines, forcing them to estimate.
  - type: good
    description: A bar chart shows the same monthly sales. The top of each bar aligns with a value on the axis, making it much easier to read the precise value for March.
---

## Guidance

Avoid using a standard line chart if the primary task for the user is to look up the precise value of a specific data point.

## Why

Line charts are optimized for showing trends and overall shape. Their data points often fall between the gridlines or ticks on an axis. This forces the user to perform a difficult perceptual estimation to determine the point's exact value, leading to low accuracy and slow performance. Research has shown that line charts perform poorly for value retrieval tasks compared to tables or bar charts, which are designed for this purpose.

## When it applies

- The user's main goal is to answer questions like, "What was the exact value for Category X?".
- High precision is required.
- The visualization is static and does not have interactive tooltips.

## Exceptions

- **When interactivity is available:** If the user can hover over a data point to see its exact value in a tooltip, the limitation of the static chart is mitigated.
- **When trend is primary:** If the primary goal is to show a trend and value lookup is a secondary, less critical task, a line chart may still be the best choice overall.
- **When direct labels are used:** If each data point on the line is explicitly labeled with its value, the need for estimation is removed.

## Trade-offs

- **Clutter:** Adding direct labels to a line chart to improve lookup can create significant visual clutter, especially if the line is noisy or has many data points.
- **Losing the trend:** Switching to a bar chart or table makes precise lookup easier but can make the overall trend or pattern harder to see at a glance compared to a line chart.

## Signs of Trouble

- **Estimation, not reading:** Users are tilting their heads and using their fingers to trace from a point on the line over to the axis.
- **Low confidence:** Users give answers with qualifiers like "It's about..." or "It looks like...".
- **High error rate:** User answers for specific values are consistently inaccurate.

## How to Improve

- **Quick Fix: Add direct labels.** If you must use a line chart, add text labels with the exact value to each data point (or at least the most important ones).
- **Moderate Approach: Add interactivity.** If the medium allows, implement tooltips that appear on hover, displaying the precise value of the data point.
- **Comprehensive Redesign: Switch chart types.** For tasks prioritizing precise value lookup, replace the line chart with a more suitable visualization:
    - **Use a bar chart:** Encodes values by length against a common baseline, making lookup accurate and fast.
    - **Use a table:** Provides the highest possible precision for value lookup, though it is slower to read and poor for seeing trends.
