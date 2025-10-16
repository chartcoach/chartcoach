---
id: use-position-for-quantitative-data
title: "Use position on a common scale to encode quantitative data"

tags:
  - impact:perceptual
  - impact:cognitive
  - task:compare
  - task:rank
  - task:lookup
  - data:quantitative
  - visual:position
  - chart:bar
  - chart:line
  - chart:scatter
  - audience:general
  - medium:static
  - medium:interactive

evidence:
  strength: high
  summary: "Cleveland & McGill (1984) and Mackinlay (1986) established that position along a common scale is the most accurate visual encoding for quantitative tasks. A review by Zeng & Battle (2023) confirms this principle remains a cornerstone of graphical perception, showing position is consistently ranked highest for accuracy across all data types (quantitative, nominal, ordinal)."

sources:
  - type: research
    ref: Cleveland & McGill, 1984
    url: https://doi.org/10.2307/2288400
    note: "Foundational experiment (n=51) demonstrating that judgments of position along a common scale are significantly more accurate than judgments of length, angle, or area."
    role: primary
  - type: research
    ref: Mackinlay, 1986
    url: https://doi.org/10.1145/22949.22950
    note: "Formalized the ranking of visual variables, placing position at the top for encoding quantitative data based on perceptual accuracy."
    role: primary
  - type: research
    ref: Zeng & Battle, 2023
    url: https://doi.org/10.1145/3544548.3581349
    note: "Systematic review of 59 studies confirming position encodings (PX, PY) are the top choices for representing all data types (Table 3, p. 8)."
    role: supporting

tools:
  - type: learn
    name: "Making the Most Important Comparisons the Easiest to See"
    url: https://www.perceptualedge.com/articles/visual_business_intelligence/visual_communication.pdf
    description: "Stephen Few's whitepaper explains the practical implications of perceptual rankings for effective dashboard design."
---
## Guidance
Use position on a common scale—as found in bar charts, dot plots, and scatterplots—as the primary method for representing quantitative values, especially when comparison, ranking, or lookup are key tasks.

## Why
Humans perceive and compare differences in position along an aligned scale more accurately, quickly, and consistently than any other visual variable, such as length, angle, area, or color. Relying on position minimizes the risk of misinterpretation and reduces the cognitive effort required to understand the chart.

### Core Principle
Visual encodings should be chosen based on their perceptual effectiveness for the given data and task. For quantitative comparisons, position is the most effective encoding.

## When it applies
- When the primary goal is for the audience to accurately compare, rank, or look up quantitative values.
- When designing core charts for dashboards or reports, such as bar charts, line charts, or scatterplots.
- For almost any task involving numerical data.

## Exceptions
- **High-level patterns:** When the goal is to see high-level patterns rather than make precise comparisons, other encodings can be primary. For example, using color in a heatmap to spot correlations or using area in a treemap to see the general composition of a large hierarchy.
- **Space constraints:** When display space is extremely limited, more compact representations like treemaps (area) might be necessary, even though they are less accurate for comparison.
- **Geographic data:** For maps, position is already used to encode location, so another channel (like color in a choropleth map) must be used to encode quantitative values.

## Trade-offs
- **Space:** Charts that use position effectively (like bar charts) often require more screen or page space than more compact but less perceptually accurate charts (like treemaps).
- **Aesthetics:** Without careful design, a simple dot plot might be perceived as less visually engaging than a colorful bubble chart, even though the dot plot is far more effective for accurate comparison.

## Signs of Trouble
- **Comparison difficulty:** Viewers struggle to determine which value is larger when the difference is small.
- **Inaccurate judgments:** If you ask someone to estimate the ratio between two values (e.g., "how many times bigger is A than B?"), their answers are inconsistent or inaccurate.
- **Reliance on tooltips:** The chart is unusable for comparison without hovering over every data point to read the exact value in a tooltip.
- **Chart type:** You are using a pie chart, donut chart, treemap, or bubble chart for a task that requires precise comparisons between non-adjacent elements.

## How to Improve
- **Quick Fix: Add Data Labels.** If you must use a less effective chart type like a pie or bubble chart, add direct data labels to each element. This provides an "escape hatch" for viewers to read exact values, bypassing the flawed perceptual encoding.
- **Moderate Redesign: Switch to a Better Chart.** Convert a pie chart or bubble chart into a simple bar chart or dot plot. This immediately improves comparability by placing all values on a common, aligned scale. Sorting the bars by value will make ranking even easier.
- **Comprehensive Approach: Re-evaluate the Task.** If you have multiple variables, instead of overloading a single chart with different encodings (e.g., a bubble chart using x-position, y-position, size, and color), consider using a panel of simpler charts (small multiples) where each panel uses position on a common scale to facilitate easier comparisons.