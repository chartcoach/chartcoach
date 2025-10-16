---
id: permute-colorfield-for-averaging
title: "Randomize pixel positions within a colorfield to improve average-value judgments"

tags:
  - impact:perceptual
  - impact:performance
  - chart:heatmap
  - task:summary-mean
  - data:temporal
  - data:quantitative
  - visual:color
  - audience:expert
  - medium:screen

sources:
  - type: research
    ref: Correll et al., 2012
    url: https://doi.org/10.1145/2207676.2208556
    note: "The study found that a 2D-permuted colorfield, where pixels within each month were randomized, led to significantly better performance in judging averages compared to a standard, ordered colorfield."

examples:
  - type: bad
    description: "An ordered colorfield still contains temporal patterns (e.g., a gradient of color within a month). While better than a line chart for averaging, these internal patterns are irrelevant to the task and can be a minor distraction."
  - type: good
    description: "A permuted colorfield shuffles the pixels within each month. This destroys internal patterns but makes the 'average color' of the block easier to perceive, as the visual system can pool colors from a more representative local sample. This is a pure optimization for the aggregation task."
---

## Guidance

When using a colorfield to display data within distinct, pre-defined regions (e.g., months), randomly shuffling the pixels within each region can further improve the accuracy of average value judgments.

## Why

Perceptual averaging is most effective when the visual system can "pool" colors from a local area. In a standard, ordered colorfield, there may be internal trends (e.g., values increasing through the month). Randomly permuting the pixels breaks these irrelevant patterns and creates a more homogenous mixture of colors within the block. This allows the visual system to sample a smaller local area and get a more accurate estimate of the entire region's average, making the averaging task even easier and more accurate.

## When it applies

- You are using a colorfield (1D heatmap) where the data is segmented into known, fixed aggregation boundaries (e.g., days within months, minutes within hours).
- The *only* task for the viewer is to compare the average value *across* these fixed regions.
- Any and all patterns *within* a region are completely irrelevant to the viewer's task and can be discarded.

## Exceptions

**Do not use this technique** if viewers need to see any spatial or temporal patterns *within* the aggregation region. This includes identifying trends, outliers, or distributions within a block. The permutation explicitly and irreversibly destroys this information, making it suitable only for pure aggregation tasks.

## Trade-offs

- **You gain** a further boost in accuracy for the specific task of comparing averages across pre-defined blocks.
- **You sacrifice** all information about intra-region patterns. It becomes impossible to see if values were increasing, decreasing, or volatile within a month, for example. This is an extreme optimization for aggregation at the total expense of detail.

## Signs of Trouble

- **Distracting Internal Patterns:** In an ordered colorfield, viewers may be distracted by gradients or other patterns within a block, even if their task is only to judge the overall average.
- **Sub-Optimal Performance:** While an ordered colorfield is good, it may not be maximally effective for aggregation because the visual system still has to average over potentially non-uniform color distributions.

## How to Improve

- **Moderate approach:** Use a standard, ordered colorfield. This is already a significant improvement over a line chart for aggregation tasks and preserves intra-region details.

- **Comprehensive approach:** If the task is purely to compare averages and intra-region detail is irrelevant, implement a 2D permutation. For each aggregation block (e.g., each month), take all the data points (pixels) within that block and randomly re-assign their positions within the block's boundaries. This optimizes the display for perceptual averaging.
