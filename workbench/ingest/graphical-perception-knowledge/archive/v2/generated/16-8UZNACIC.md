---
id: use-wrapped-bars-for-disproportionate-data
title: "Use wrapped bar charts for disproportionate values"

impact:
  - perceptual
  - cognitive
  - ethical
  - logos
  - performance

tags:
  - bar-chart
  - wrapped-bar-chart
  - comparison
  - identification
  - composition
  - disproportionate-data
  - skewed-data
  - high-variance
  - accuracy
  - cognitive-load

sources:
  - type: research
    ref: Karduni et al., 2020
    url: https://doi.org/10.1145/3313831.3376365
    note: "Primary source evaluating the effectiveness of wrapped bar charts, providing empirical evidence for their use, and defining heuristics like entropy and H-spread."
  - type: research
    ref: W. E. B. Du Bois' Data Portraits, 1900
    url: https://www.loc.gov/pictures/collection/anedub/
    note: "Historical inspiration for the technique, used by W. E. B. Du Bois in his infographics for the 1900 Exposition Universelle in Paris to show inequities in African American life."

tools:
  - type: implement
    name: Wrapped Bar Chart Prototype
    url: https://wrapped-barchart.herokuapp.com/
    description: An interactive D3.js implementation of wrapped bar charts from the research paper.
  - type: learn
    name: Du Bois Wrapped Bar Chart Paper
    url: https://dl.acm.org/doi/10.1145/3313831.3376365
    description: The research paper detailing the experiments and findings.

examples:
  - type: bad
    description: A standard bar chart shows presidential ad spending. The largest bar (Trump) is so tall that it makes the bars for most other candidates appear as tiny, unreadable slivers. It is difficult to compare the smaller values.
  - type: good
    description: The same ad spending data is shown with a wrapped bar chart. The largest bar wraps around multiple times, allowing the y-axis to be scaled for the smaller values. This makes it possible to see and compare spending among the candidates with lower totals.
---

## Guidance

When visualizing categorical data with highly disproportionate values, use a wrapped bar chart to make small values visible and comparable.

## Why

Standard bar charts are ineffective when one or a few bars are vastly larger than the rest. The y-axis scale required to show the large bars shrinks the small bars until they are nearly invisible, making them difficult to read, estimate, or compare. Wrapping the large bars preserves a linear scale while dedicating more screen space to the smaller values. This leads to higher accuracy when identifying small values and estimating ratios between the largest and smallest bars.

## When it applies

- When using a bar chart for a dataset containing one or more "far out" values that are orders of magnitude larger than the others.
- When a key goal is for the audience to accurately identify, estimate, or compare the smallest values in the dataset.
- As a technical rule of thumb, this technique is most effective for datasets with low normalized entropy (< 0.75) or a high H-spread (> 4.5), which mathematically describe data where value is concentrated in a few categories.

## Exceptions

- **When speed is critical.** Wrapped charts are less "glanceable" than standard bar charts. They require more time and mental effort to interpret because the viewer must count the wraps, which can slow down identification of the largest values.
- **When there are too many wraps.** If a bar needs to wrap an excessive number of times, it can become cumbersome and annoying for the user to count, defeating the purpose. In such cases, a different chart type or a simple label may be better.

## Trade-offs

- **Accuracy vs. Cognitive Load.** You gain higher accuracy for tasks involving small values but at the cost of increased cognitive load. Viewers must perform a mental calculation (counting wraps and adding the remainder) to determine a wrapped bar's total value, making it less preattentive.
- **Novelty vs. Familiarity.** A wrapped bar chart is an unfamiliar chart type for most audiences and may require a brief explanation or tutorial to be understood correctly.

## Evaluate

- [ ] A bar chart is being used, but some bars are so small they are barely visible or distinguishable from each other.
- [ ] Known misleading techniques like a broken axis or a non-linear (log) scale are used to handle the disproportionate values, which can distort the visual perception of magnitude.
- [ ] It is impossible to accurately judge the ratio between the smallest and largest bars because the smallest bar's height is effectively zero.

## Repair

1.  **Switch to a wrapped bar chart.** Re-render the chart, setting a wrap threshold that allows the smaller bars to be clearly visible and easily compared.
2.  **Add labels to reduce cognitive load.** For bars that wrap many times, consider adding a label indicating the number of wraps to save the viewer from having to count them manually.
3.  **Provide an alternative view.** If a wrapped chart isn't feasible, supplement the standard bar chart with a sorted table or a separate chart focusing only on the smaller values.