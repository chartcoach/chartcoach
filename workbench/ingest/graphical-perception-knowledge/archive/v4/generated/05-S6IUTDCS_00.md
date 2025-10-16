---
id: prioritize-position-for-quantitative-comparison
title: "Use position on a common scale for accurate quantitative comparisons"
tags:
  - impact:perceptual
  - impact:logos
  - impact:ethical
  - chart:bar
  - chart:line
  - chart:scatter
  - chart:dot-plot
  - task:compare
  - task:rank
  - task:lookup
  - data:quantitative
  - visual:position
  - visual:length
  - visual:angle
  - visual:area
  - audience:general
  - medium:static
  - medium:interactive
sources:
  - type: research
    ref: Cleveland & McGill, 1984
    note: "Referenced as [17] in Zeng & Battle. Established the foundational ranking of perceptual tasks, showing position on a common scale is most accurate."
  - type: research
    ref: Heer & Bostock, 2010
    note: "Referenced as [34] in Zeng & Battle. Replicated and extended Cleveland & McGill's findings, confirming that bar charts (position/length) outperform pie charts (angle) for comparison tasks."
  - type: research
    ref: Mackinlay, 1986
    note: "Referenced as [61] in Zeng & Battle. Formalized the effectiveness rankings of visual channels for quantitative, ordinal, and nominal data, placing position at the top for quantitative data."
examples:
  - type: bad
    description: A pie chart uses angles and area to represent quantitative values, which are difficult for humans to compare accurately. It is hard to tell if 'Category B' is definitively larger than 'Category C'.
  - type: good
    description: A bar chart represents the same data, placing all values on a common baseline. This use of position and length makes it immediately clear that 'Category B' is larger than 'Category C' and allows for much more accurate comparisons between all categories.
---

## Guidance

For tasks that require comparing or ranking quantitative values, encode the data using position along a common, aligned scale. Avoid using less effective visual channels like angle, area, or color saturation as the primary encoding for this task.

## Why

Human perception is most accurate and efficient at judging differences in position along a common scale (e.g., the tops of bars on the same baseline). Other visual properties are progressively harder to compare accurately, following a general hierarchy: position > length (unaligned) > angle/slope > area > volume > color/saturation. Relying on less effective channels like angle (in a pie chart) or area (in a bubble chart) leads to slower, less accurate, and less confident judgments by the viewer.

## When it applies

- The primary goal is for the user to **accurately compare** or **rank** quantitative values.
- You are deciding between chart types, such as a **bar chart vs. a pie chart** or a **dot plot vs. a bubble chart**.
- Data integrity and accurate interpretation are more important than aesthetic novelty.

## Exceptions

- **Part-to-whole relationships:** While bar charts are still often better, pie charts (angle) are conventionally used to emphasize that individual values are components of a total. Even in this case, a bar chart or a treemap can be more effective if there are more than a few slices.
- **Geographic data:** When showing quantitative values on a map, area (for choropleths) or size (for proportional symbols) are often necessary encodings due to the spatial constraints. Supplement with tooltips or labels to provide exact values.
- **General overview:** If the goal is just to give a very rough impression of values ("small", "medium", "large") and precision is not required, area-based encodings like bubble charts can be acceptable.

## Trade-offs

- **Space:** Charts using position, like bar charts, can take up more space than more compact (but less accurate) forms like treemaps or packed bubble charts.
- **Familiarity:** Audiences in some business contexts may have a strong expectation for certain chart types, like pie charts, even if they are perceptually suboptimal. Choosing a bar chart may require a slight reorientation for the viewer, though the gain in clarity is almost always worth it.

## Signs of Trouble

- **Chart type is a pie, donut, or bubble chart:** The chart relies on angle or area for its primary quantitative encoding, which is a red flag for comparison tasks.
- **Viewer uncertainty:** Users express difficulty in determining which value is larger or by how much. They might say, "Is this slice bigger than that one?"
- **Inaccurate takeaways:** If you quiz users on the relationships in the data, they make frequent errors in judgment.
- **Reliance on labels:** The chart is unreadable without direct data labels on every element. The visual encoding itself is failing to communicate the data.

## How to Improve

- **Quick Fix: Add explicit labels.** If you must use a pie or bubble chart, add direct data labels (values and/or percentages) to each segment. This provides an "escape hatch" for the user, allowing them to read and compare numbers directly, bypassing the flawed perceptual task.

- **Moderate Redesign: Switch to a bar or dot plot.** The most effective change is to convert the chart to one that uses position on a common scale.
  - Convert a **pie chart** into a **bar chart**.
  - Convert a **bubble chart** into a **dot plot** or a **bar chart**.
  - Sort the bars or dots in ascending or descending order to make ranking and comparison even easier.

- **Comprehensive Approach: Educate stakeholders.** Explain the perceptual reasoning for choosing bar charts over pie charts, referencing foundational research (like Cleveland & McGill's work) to build trust and establish best practices for future visualizations.