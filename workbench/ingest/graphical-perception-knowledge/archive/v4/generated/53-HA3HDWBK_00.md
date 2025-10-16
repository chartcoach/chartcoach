---
id: balance-speed-accuracy-outlier-scatter
title: "Balance speed and accuracy for outlier detection in scatterplots"
tags:
  - impact:perceptual
  - impact:performance
  - chart:scatter
  - task:find-anomalies
  - data:quantitative
  - visual:size
  - visual:opacity
  - visual:position
  - medium:static
  - medium:interactive
  - audience:general
  - audience:expert
sources:
  - type: research
    ref: "Micallef et al., 2017"
    url: "https://doi.org/10.1109/TVCG.2017.2674978"
    note: "Found that while default scatterplots from R/MATLAB were slightly more accurate for outlier detection, a perceptually-optimized design was significantly faster for users to complete the task (Table 2, Outliers row)."
tools:
  - type: implement
    name: R
    url: https://www.r-project.org/
    description: "Statistical software with robust default plotting capabilities shown to be highly accurate for this task."
  - type: implement
    name: MATLAB
    url: https://www.mathworks.com/products/matlab.html
    description: "A programming and numeric computing platform whose default scatterplots perform with high accuracy for outlier detection."
---

## Guidance

For outlier detection in scatterplots, choose between prioritizing user accuracy or task completion speed. Standard software defaults may yield slightly higher accuracy, while perceptually-optimized designs can be significantly faster.

## Why

Research reveals a trade-off between speed and accuracy for outlier detection. Default scatterplot designs (like those in R or MATLAB) are generally well-tuned, leading to high accuracy in spotting outliers. However, algorithms that automatically optimize marker size and opacity based on data density and perceptual principles can guide the user's attention more efficiently. This makes anomalies more salient and leads to significantly faster task completion times, sometimes at the cost of a small, acceptable drop in accuracy.

## When it applies

- When creating scatterplots where the primary task is identifying outliers or anomalies.
- This is especially relevant in contexts where user time is a critical factor, such as in interactive data exploration or when an analyst needs to review a large number of charts quickly.

## Exceptions

- If the cost of missing an outlier is extremely high (e.g., medical diagnosis, financial fraud detection), prioritize maximum accuracy over speed. In these cases, the marginal accuracy benefit of standard, non-optimized plots is likely worthwhile.

## Trade-offs

- **Optimizing for Speed:** You may gain faster insights and reduce user fatigue but risk a slight decrease in the accuracy of outlier identification.
- **Optimizing for Accuracy:** You may achieve the highest possible accuracy with standard tools but at the cost of longer analysis time for the user.

## Signs of Trouble

- **Slow Discovery:** Users take a long time to scan the plot and find anomalous points.
- **Hidden Points:** Outliers are lost in dense, overplotted regions, making them impossible to distinguish from the main cluster.
- **Visual Clutter:** The plot is a uniform "cloud" of points, with no visual hierarchy to guide the eye toward potential outliers.

## How to Improve

- **Quick Fix: Adjust Opacity.** Manually reduce the opacity of all markers in your plotting software. This is a simple way to simulate a density map, helping reveal dense areas and making isolated points (potential outliers) stand out more.

- **Moderate Approach: Use Default Statistical Software.** Rely on the default scatterplot implementations in established tools like R or MATLAB. Studies show they offer high accuracy for this task out-of-the-box.

- **Comprehensive Approach: Use Perceptual Optimization.** Employ an algorithm or tool that automatically sets marker size and opacity based on data density and perceptual models. This approach is shown to significantly speed up outlier detection tasks by making anomalies more visually salient.