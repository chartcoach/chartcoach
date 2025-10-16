---
id: pie-cues-area-arc-over-angle
title: "Recognize area and arc length are the dominant cues in pie and donut charts, not angle"

tags:
  - impact:perceptual
  - chart:pie
  - chart:donut
  - task:composition
  - visual:angle
  - visual:size
  - visual:length

sources:
  - type: research
    ref: Skau & Kosara, 2016
    url: https://doi.org/10.1111/cgf.12888
    note: "Study 1 isolated the three visual cues (angle, area, arc length). Charts showing only angle were perceived with the highest error, while area and arc length were more accurate and comparable to a standard pie chart."

---

## Guidance

When designing or evaluating pie and donut charts, understand that viewers primarily rely on the segment's **area** and **arc length** to judge proportions, not the central angle.

## Why

Experiments that isolated the three visual cues found that charts showing *only* angle were the least accurately perceived. While all three cues are present and contribute in a standard chart, the central angle is the weakest perceptual signal. This explains why removing the center to create a donut chart has a negligible effect on accuracy.

## When it applies

- When evaluating novel or "artistic" variations of pie or donut charts seen in infographics.
- When explaining the perceptual principles behind why certain pie chart variations are or are not effective.
- This principle underpins other guidelines, such as why varying segment radii is a bad practice.

## Exceptions

- No exceptions are known. This is a fundamental finding about the perceptual mechanism of these charts. Even if a user believes they are using angle, their judgments are more strongly correlated with area and arc length.

## Trade-offs

- This understanding may conflict with traditional textbook explanations of pie charts, which often focus exclusively on the concept of angles summing to 360 degrees. It requires shifting focus from the geometric construction to the perceptual reality.

## Signs of Trouble

- **Distorted Cues:** A chart design that prioritizes preserving the angle cue while distorting the more important area or arc length cues (e.g., using wedge-shaped icons of different base widths).
- **Misguided Justification:** Defending an ineffective chart variation by claiming "it still shows the right angles."

## How to Improve

- **Quick approach:** When critiquing a pie chart variation, check if the relative areas and arc lengths of the segments correctly represent the data proportions. If they are distorted, the chart is likely misleading, regardless of what the angles show.

- **Comprehensive approach:** When creating an infographic or custom visualization based on a circular layout, ensure that the design choices do not compromise the integrity of the area and arc length encodings. If a stylistic choice (like using a non-circular shape) breaks these cues, switch to a more robust chart type like a bar chart.
