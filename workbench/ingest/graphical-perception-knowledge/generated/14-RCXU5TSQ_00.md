---
id: use-colorfield-for-average-summary
title: "Use a colorfield chart to judge average values across time-series regions"

tags:
  - impact:perceptual
  - impact:performance
  - chart:line
  - chart:heatmap
  - task:summary-mean
  - task:compare
  - data:temporal
  - data:quantitative
  - visual:color
  - visual:position
  - audience:general
  - medium:screen
  - access:color-vision-risk

evidence:
  strength: medium
  summary: "Correll et al. (2012, n=66) found in a crowd-sourced experiment that for judging the average value of regions in time-series data, a colorfield chart (color encoding) was significantly more accurate than a standard line chart (position encoding) (F(1,1921)=143.75, p < 0.0001)."

sources:
  - type: research
    ref: Correll et al., 2012
    url: https://doi.org/10.1145/2207676.2208556
    note: "Primary study (n=66 after exclusions) comparing line charts and colorfield charts for an aggregate judgment task. Found colorfields led to significantly higher accuracy."
    role: primary
  - type: research
    ref: "Cleveland & McGill, 1984"
    url: https://doi.org/10.2307/2288400
    note: "Foundational work establishing the general superiority of position over color for quantitative tasks. This guideline represents a task-specific exception to that general principle."
    role: related

examples:
  - type: good
    description: "A colorfield chart (similar to a 1D heatmap) is used to encode time-series values. This leverages perceptual averaging, making it easier to judge the average value of each monthly segment."
    url: https://i.imgur.com/K3Z4a2a.png # Screenshot of Figure 3(c) from the paper
  - type: bad
    description: "A standard line chart is used for the same task. While good for seeing trends and peaks, it requires more cognitive effort to estimate the average value of each monthly segment, leading to lower accuracy on this specific task."
    url: https://i.imgur.com/K5bM23F.png # Screenshot of Figure 3(a) from the paper
---

## Guidance

For tasks requiring users to judge the average value of regions within a dense time-series, prefer encoding the values with color (e.g., a colorfield or 1D heatmap) over position (e.g., a line chart).

## Why

The human visual system can efficiently perform "perceptual averaging" on features like color across a spatial region. In contrast, mentally calculating the average height of a complex line shape is a more cognitively demanding task. Using color outsources this averaging work to the pre-attentive visual system, leading to higher accuracy for this specific summary task.

### Core Principle

Match the visual encoding to the perceptual task. While position is superior for looking up individual values, color can be superior for judging spatial aggregates.

## When it applies

- When the primary task is to compare the *average* value of different segments in a dense time-series (e.g., "Which month had the highest average sales?").
- When an overview or summary judgment is more important than reading precise individual data points.

## Exceptions

- If the primary task is to identify precise values, find peaks/troughs, or judge the exact slope or rate of change. A line chart (position) is superior for these detail-oriented tasks.
- When designing for audiences with color vision deficiencies, as reliance on color introduces accessibility barriers. Additional encodings or affordances would be needed.

## Trade-offs

- **Reduced Precision:** You sacrifice the ability for users to look up precise individual values, which a line chart's y-axis provides.
- **Accessibility:** Relying on color makes the chart inaccessible to users with certain types of color vision deficiency unless a carefully designed, perceptually uniform, and tested palette is used.
- **Familiarity:** Line charts are a much more conventional and familiar representation for time-series data. A colorfield may require more initial explanation for a general audience.

## Signs of Trouble

- **User Error:** Users consistently misjudge which region has the highest or lowest average when using a line chart for a dense dataset.
- **"Peak" Confusion:** Users mistakenly identify the region with the highest single point (the peak) as the one with the highest average.
- **Slow Performance:** Users take a long time to answer questions about regional averages, suggesting they are performing slow, serial mental calculations rather than getting a quick visual impression.

## How to Improve

- **Quick Fix: Annotate the Line Chart.** On an existing line chart, add visual annotations that highlight the average for each region, such as a faint horizontal line. This adds a direct encoding of the summary statistic without changing the chart type.

- **Moderate Redesign: Switch to a Colorfield.** Change the chart type from a line chart to a colorfield (or 1D heatmap). Map the data values to a perceptually uniform color scale (e.g., from ColorBrewer). This directly enables perceptual averaging.

- **Comprehensive Approach: Provide Linked Views.** Offer both a colorfield chart for high-level summary judgments and a traditional line chart for detailed exploration. Selecting a region in the colorfield could highlight or filter the corresponding section in the line chart, giving users the benefits of both encodings.