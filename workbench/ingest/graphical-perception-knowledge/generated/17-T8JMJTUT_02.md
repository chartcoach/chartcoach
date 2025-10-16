---
id: prefer-contiguous-cartograms-for-value-comparison
title: "Prefer contiguous cartograms for comparing values"

tags:
  - impact:perceptual
  - chart:map
  - chart:map.cartogram
  - task:compare
  - task:rank
  - data:spatial
  - data:quantitative
  - visual:size

evidence:
  strength: medium
  summary: "A 2018 study (n=33) found contiguous cartograms led to significantly lower error rates on value comparison and ranking tasks (find top-k) compared to rectangular and Dorling (circle) cartograms (p<0.001 for both tasks). This suggests they are more reliable for judging relative sizes."

sources:
  - type: research
    ref: "Nusrat, Alam, & Kobourov, 2018"
    url: https://doi.org/10.1109/TVCG.2016.2642109
    note: "Experiments H3 (compare, find top-k, detect change) showed contiguous cartograms consistently had the lowest error rates. The accuracy advantage over rectangular and Dorling types was statistically significant for comparison and ranking."
    role: primary

---

## Guidance

When the main goal is for viewers to compare the data values of different regions or to identify which regions are largest or smallest, prefer using a **contiguous cartogram**.

## Why

Although human perception of area is less accurate than length, experiments show that viewers are more accurate at judging the relative areas of the organic, distorted shapes in a contiguous cartogram than the abstract circles or rectangles in Dorling and rectangular cartograms. For tasks that require comparing values (e.g., "Is state A bigger than B?") or ranking them ("Find the top 3 states"), contiguous cartograms result in fewer errors.

### Core Principle

The choice of visual shape can impact the accuracy of area judgments. Irregular but familiar-looking shapes may be easier to compare than uniform, abstract shapes like circles when the task is complex.

## When it applies

- When the primary task is to compare the data values encoded by the area of two or more regions.
- When viewers need to find the regions with the highest or lowest values (i.e., finding extrema or ranking).

## Exceptions

- For very simple comparisons with large, obvious differences (e.g., one region is 10x larger than another), the choice of cartogram type may be less critical.
- If the primary goal is to preserve shape or show a high-level summary, other cartogram types might be chosen despite a trade-off in comparison accuracy.

## Trade-offs

- **Shape Distortion:** Contiguous cartograms distort the original geographic shapes, which can make it harder for viewers to recognize regions.
- **Topology Requirement:** This method is only suitable for data where regions are, in fact, contiguous.

## Signs of Trouble

- **Inaccurate Comparisons:** Viewers consistently make errors when asked to judge which of two regions is larger or to rank several regions by size.
- **Difficulty Finding Extremes:** Viewers struggle to identify the region with the largest or smallest area on the map.

## How to Improve

- **Quick Fix: Add Data Labels or Tooltips.** If you must use a Dorling or rectangular cartogram, add direct labels with the exact data value to each region or provide them in an interactive tooltip. This bypasses perceptual estimation entirely.

- **Moderate Redesign: Switch to a Contiguous Cartogram.** If comparison accuracy is paramount, change the chart from a Dorling or rectangular type to a contiguous cartogram.

- **Comprehensive Redesign: Use a Bar Chart.** If precise comparison and ranking are the most important goals, the most effective visualization is a simple bar chart, which uses the highly accurate visual channel of length on a common baseline. This separates the data from the geography but maximizes comparison accuracy.
