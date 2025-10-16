---
id: avoid-nested-donuts
title: "Avoid using nested donut charts for comparison"

tags:
  - impact:perceptual
  - impact:cognitive
  - chart:donut
  - chart:pie
  - task:compare
  - task:composition
  - access:cognitive-load-risk

sources:
  - type: research
    ref: Skau & Kosara, 2016
    url: https://doi.org/10.1111/cgf.12888
    note: "The paper's recommendations state that 'Nested donuts... are problematic' because comparing circles of different radii and areas is difficult, a direct implication of their findings that area and arc length are key cues."

examples:
  - type: bad
    description: A nested donut chart (or radial bar chart) makes it very difficult to compare the composition of the inner ring to the outer ring. It is hard to tell if the light blue segment is a larger percentage in the inner or outer ring.
---

## Guidance

Do not nest multiple donut charts concentrically to compare the composition of different groups or to show changes over time.

## Why

Nesting donut charts forces viewers to compare segments that have different radii and are not aligned to a common baseline. This makes it perceptually difficult and error-prone to compare the arc lengths and areas, which are the primary cues for reading these charts. The cognitive load required to make these comparisons is high, and the accuracy is low.

## When it applies

- When you need to compare the composition of multiple groups (e.g., survey results for different demographics).
- When you want to show how a part-to-whole relationship changes over multiple time periods.

## Exceptions

- There are no known exceptions where this chart form is effective for comparing compositions. While visually compact, it is perceptually flawed.

## Trade-offs

- **Gained:** By avoiding nested donuts, you gain clarity and accuracy in your comparisons.
- **Sacrificed:** You lose a visually compact, circular layout. The alternatives, like small multiples or bar charts, typically require more screen or page space.

## Signs of Trouble

- **Bullseye Chart:** The visualization looks like a target or a bullseye, with multiple concentric rings each broken into colored segments.
- **Comparison Difficulty:** Viewers struggle to answer questions like "Did Category A's share increase or decrease between the inner and outer ring?"

## How to Improve

- **Moderate Redesign: Use Small Multiples.** Instead of nesting the donut or pie charts, place them side-by-side. This layout is called small multiples. It allows for easier comparison of the overall patterns in each chart, although direct comparison of individual slices between charts is still challenging.

- **Comprehensive Redesign: Use a Stacked Bar Chart.** The most effective alternative is a **100% stacked bar chart**. This chart type aligns all groups along a common baseline, making it much easier to compare the proportional contributions of each category across the groups. For showing change over time, a **stacked area chart** can also be an effective choice.
