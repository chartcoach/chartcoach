---
id: maintain-consistent-radii-in-pies
title: "Maintain Consistent Radii for All Segments in Pie and Donut Charts"

tags:
  - impact:perceptual
  - impact:ethical
  - chart:pie
  - chart:donut
  - task:compare
  - task:composition
  - visual:area
  - visual:size
  - medium:static

evidence:
  strength: medium
  summary: "Skau & Kosara (2016) found that viewers rely heavily on arc length and area for proportion judgments. As a direct extension, chart variations that distort these cues by using inconsistent radii are likely to impair accurate perception and mislead the viewer."

sources:
  - type: research
    ref: Skau & Kosara, 2016
    url: https://doi.org/10.1111/cgf.12888
    note: "The paper identifies arc length and area as the most important cues, implying that designs which distort them (like varying-radius pie charts) are problematic. The paper explicitly warns against this practice in its discussion."
    role: primary

examples:
  - type: bad
    description: "A pie chart where one segment is made to 'stand out' by giving it a larger radius than the others. This distorts its area and arc length, making it appear larger than its data value dictates."
  - type: good
    description: "A standard pie or donut chart where all segments extend to the same outer radius, ensuring that the area and arc length of each slice are directly proportional to its value."

---

## Guidance

Do not vary the radius of individual segments within a single pie or donut chart. All slices should extend from the center (or inner hole) to the same outer boundary, forming a perfect circle.

## Why

Viewers judge the values in pie and donut charts primarily by comparing the area of the slices and the length of their outer arcs. When you change the radius of a segment, you distort both of these critical perceptual cues, making accurate comparisons impossible. For example, a segment with a larger radius will look bigger than a segment with the same value but a smaller radius, leading to misinterpretation. This is a form of data distortion.

### Core Principle

Visual encodings must be consistent and proportional to the data they represent. Altering a chart's geometry for aesthetic reasons must not break the perceptual mapping between the data and its visual properties.

## When it applies

- When designing infographics or custom visualizations based on pie or donut charts.
- When tempted to make a particular slice "stand out" by extending its radius.

## Exceptions

- None known. This practice is fundamentally misleading as it breaks the geometric encoding of the data.

## Trade-offs

- You may sacrifice a certain aesthetic or stylistic effect used in some infographics. The gain, however, is data integrity and perceptual accuracy.

## Signs of Trouble

- **Uneven Edges:** The outer boundary of the pie or donut chart is not a perfect circle because some slices extend further out than others.
- **Misleading Emphasis:** One slice appears disproportionately large or small not because of its data value, but because its radius has been artificially altered.

## How to Improve

- **Comprehensive approach: Standardize the Radius.** Redesign the chart to use a standard pie or donut chart form where all segments share a common outer radius. If you need to emphasize a particular slice, use a more appropriate visual variable like a distinct color, add a text annotation, or slightly "explode" the segment from the center (while keeping its radius the same as the others).
