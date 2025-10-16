---
id: adapt-scatterplot-design-to-task
title: "Adapt scatterplot designs to the analytical task"

tags:
  - impact:perceptual
  - impact:performance
  - chart:scatter
  - task:correlation
  - task:cluster
  - task:find-anomalies
  - data:quantitative
  - data:categorical
  - visual:size
  - visual:opacity
  - visual:position
  - audience:general
  - medium:screen

evidence:
  strength: medium
  summary: "A study by Micallef et al. (2017, n=107-127 per task) demonstrated that different scatterplot designs optimized for specific tasks (correlation, class separation, outlier detection) yielded different performance outcomes. For example, a design that was fastest for outlier detection was not the most accurate."

sources:
  - type: research
    ref: Micallef et al., 2017
    url: https://doi.org/10.1109/TVCG.2017.2674978
    note: "Primary study using a perceptually-based cost function to automatically generate scatterplot designs for different tasks. Found significant performance differences (p<0.01) for outlier detection tasks between designs optimized for speed vs. accuracy."
    role: primary
  - type: research
    ref: Zeng & Battle, 2023
    url: https://arxiv.org/abs/2109.01271v3
    note: "Provides the methodological framework for collating and applying graphical perception knowledge, contextualizing the Micallef et al. findings."
    role: related

tools:
  - type: learn
    name: The Micallef et al. (2017) paper
    url: https://doi.org/10.1109/TVCG.2017.2674978
    description: "Explains the model-based optimization approach for adapting scatterplots to specific tasks and data."

examples:
  - type: good
    description: "The paper's Figure 5 shows three different scatterplot designs for the same data, each optimized for a different task (Correlation, Outlier Detection, Class Separation), resulting in distinct visual appearances (marker size, opacity, aspect ratio)."
---

## Guidance

When designing a scatterplot, adapt visual parameters like marker size, opacity, and aspect ratio to the primary analytical task the viewer needs to perform. A single default design is unlikely to be optimal for all tasks.

## Why

The visual properties that make a scatterplot effective for one task can hinder another. For example, estimating correlation benefits from seeing the overall shape and density of the point cloud, which may require semi-transparent, overlapping markers. In contrast, detecting individual outliers requires that points are distinct and not obscured, often benefiting from smaller, more opaque markers. Tailoring the design to the task makes the desired pattern more salient and the task easier and more efficient to perform.

### Core Principle

The optimal visual design of a chart is not fixed; it is a function of the underlying data, the viewer's task, and perceptual principles.

## When it applies

- When creating scatterplots for a specific analytical purpose, such as assessing correlation, identifying clusters (class separation), or finding outliers.
- When you anticipate the user will perform one of these tasks more frequently or with higher priority than others.

## Exceptions

- For general-purpose exploratory analysis where the user might perform many different tasks, a balanced, non-optimized design (like a default from R or MATLAB) may be a reasonable compromise, as it performs adequately across multiple tasks without excelling at any single one.

## Trade-offs

- Optimizing for one task may reduce performance on another. For example, a design optimized for outlier detection speed might be less accurate than a default design.
- Creating task-specific designs requires more effort than using a one-size-fits-all default, and may require specialized tools or programming.

## Signs of Trouble

- **Task Mismatch:** The chart is being used for a task it wasn't designed for (e.g., trying to spot single outliers in a plot optimized for density visualization with high transparency).
- **The "Ink Blob":** For dense datasets, a default design results in a solid, unreadable mass of overlapping points, obscuring all internal structure, density variations, and individual points.
- **User Frustration:** Viewers complain that it's hard to see the correlation, tell classes apart, or spot unusual data points.

## How to Improve

- **Quick approach:** Manually adjust marker size and opacity. If the task is outlier detection, decrease marker size and increase opacity. If the task is correlation in a dense dataset, increase marker size and decrease opacity to see the density distribution.
- **Moderate approach:** Use different chart presets for different tasks. Save the settings from your software (e.g., R, MATLAB, Python) that you find work well for "correlation plots" vs. "outlier plots" and re-apply them.
- **Comprehensive approach:** Use a model-based optimization approach, as described in the source paper, to automatically generate a design based on the data and a specified task. This algorithmically searches the design space for a perceptually optimal solution.
