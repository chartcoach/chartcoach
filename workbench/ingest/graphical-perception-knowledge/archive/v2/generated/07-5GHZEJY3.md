---
id: prefer-position-for-quantitative-data
title: "Prefer Position Over Other Visual Channels for Quantitative Data"

impact:
  - perceptual
  - logos
  - ethical
  - aesthetic

tags:
  - visual-channels
  - position
  - length
  - area
  - color
  - quantitative
  - comparison
  - estimation
  - foundational-principle

sources:
  - type: research
    ref: Mackinlay, 1986
    url: https://doi.org/10.1145/22949.22950
    note: "Established the theoretical framework for ranking visual encodings by effectiveness, extending earlier empirical work into a generative system."
  - type: research
    ref: "Cleveland & McGill, 1984"
    url: https://doi.org/10.2307/2288400
    note: "Provided the original empirical evidence for ranking perceptual tasks for quantitative data, which forms the basis of this guideline."

examples:
  - type: good
    description: "A bar chart uses the position of the bars' endpoints along a common axis, making it easy to accurately compare the values of different categories."
  - type: good
    description: "A scatter plot uses both vertical and horizontal position to encode two quantitative variables, allowing for accurate judgment of individual points and overall correlation."
  - type: bad
    description: "A bubble chart encodes a quantitative value using circle area. It is very difficult for a person to accurately judge that one circle's area is, for example, 2.5 times larger than another."
  - type: bad
    description: "A chart uses a color gradient (e.g., from light blue to dark blue) to encode revenue numbers. While it shows a general trend, it is impossible to perceive specific values or precise differences accurately."
---

## Guidance

For the most accurate interpretation, encode quantitative (numerical) data using position on a common scale. If position is unavailable, use length. These channels are significantly more effective than angle, area, or color for showing magnitude.

The general ranking of visual channels for quantitative data, from most to least effective, is:
1.  **Position** (on a common scale)
2.  **Length**
3.  **Angle** / **Slope**
4.  **Area**
5.  **Volume**
6.  **Color Saturation / Density**
7.  **Color Hue**

## Why

This ranking is based on how accurately the human brain can perceive and compare visual information. Experiments by Cleveland, McGill, and others have shown that we are best at judging positions along a shared axis (like in a bar chart). We are less accurate when comparing lengths that aren't aligned, and even less accurate when comparing angles, areas, or colors.

Using a more effective channel for your most important data ensures your audience can make more accurate comparisons and judgments, leading to a clearer and more truthful understanding of the information. Using a less effective channel, like area or color, can cause readers to misjudge proportions and draw incorrect conclusions.

This principle extends to other data types as well. For **nominal (categorical)** data, `position` is still highly effective, followed by `color hue` and `shape`. For **ordinal (ordered)** data, `position` is again best, followed by `color saturation` and `density`.

## When it applies

- When designing any chart to show quantitative data, such as revenue, population, or sensor measurements.
- When the primary goal is for the audience to compare values, judge magnitudes, or see precise differences between data points.
- This is the core principle behind the effectiveness of fundamental chart types like **bar charts**, **dot plots**, **scatter plots**, and **line charts**.

## Exceptions

- **Showing General Patterns:** When the goal is to show a broad pattern in a large dataset rather than precise values, a less effective channel like color can be ideal. For example, a **heatmap** uses color to reveal patterns in a large matrix.
- **Geographic Data:** In a **choropleth map**, position is used to represent geographic location. Therefore, a quantitative value (like population density) must be encoded with a different channel, typically `color saturation`.
- **Encoding Additional Variables:** When position is already used to encode two variables (e.g., in a scatter plot), you may need to use a less effective channel like `area` (for a bubble chart) or `color` to encode a third or fourth variable. This is an acceptable trade-off to increase information density.

## Trade-offs

- **Aesthetics vs. Accuracy:** Charts using less effective channels like area (bubble charts) or color can sometimes be more novel or visually engaging. However, this often comes at the cost of perceptual accuracy.
- **Information Density vs. Clarity:** Sticking only to position limits the number of variables you can show. Using channels like size and color allows you to layer more data into a single graphic, but you sacrifice the clarity and precision of those additional variables.

## Evaluate

- [ ] The most important quantitative data is encoded using area, volume, or color when it could have been encoded using position or length.
- [ ] The chart requires the viewer to compare the sizes of non-aligned shapes (like bubbles in a bubble chart or slices in a pie chart) to make a key conclusion.
- [ ] A bar chart is used, but the bars are not aligned to a common baseline (zero), which breaks the position/length encoding and turns it into a less effective length-only comparison.

## Repair

1.  **Switch to a Position-Based Chart:** If using a pie chart, bubble chart, or treemap for precise comparisons, change it to a **bar chart** or **dot plot**. This will immediately make comparisons more accurate.
2.  **Swap Encoding Channels:** If you have multiple variables encoded in a single chart, ensure the most important quantitative variable is mapped to the most effective channel available (e.g., the Y-axis position in a scatter plot).
3.  **Add Direct Labels:** If you must use a less effective channel like area or color due to other constraints, add direct numerical labels to the data points. This provides a "perceptual escape hatch," allowing users to read exact values, but be mindful that it can increase visual clutter.