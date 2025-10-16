---
id: make-outliers-prominent-in-scatterplots
title: "Make outliers in scatterplots visually prominent"

impact:
  - perceptual
  - performance
  - logos
  - ethical

tags:
  - scatterplot
  - outlier-detection
  - find-anomalies
  - task
  - size
  - opacity
  - visual-design

sources:
  - type: research
    ref: Micallef et al., 2017
    url: https://doi.org/10.1109/TVCG.2017.2674978
    note: "Primary study on optimizing scatterplot design for tasks like outlier detection. Found that larger, more opaque markers are crucial for perceivability."
  - type: research
    ref: Zeng & Battle, 2023
    url: https://doi.org/10.1145/3544548.3581349
    note: "Review paper that collates and structures knowledge from perceptual studies, including the Micallef et al. paper, to create actionable guidelines."

tools:
  - type: implement
    name: Scatterplot Design Optimization
    description: The Micallef et al. paper proposes an automated optimizer that adjusts parameters like marker size and opacity to best suit a given task. While not a public tool, it demonstrates the principle of tuning visual properties for a specific goal.
  - type: implement
    name: Datawrapper, Tableau, or other viz tools
    description: Most visualization software allows you to manually control marker size and opacity to apply this guideline.

examples:
  - type: bad
    description: A scatterplot with many data points where the markers are very small and semi-transparent. Outliers, which are lone points, become nearly invisible or are easily missed.
  - type: good
    description: The same scatterplot, but with a larger marker size and higher opacity. Outliers now pop out from the main distribution and are easy to spot, even at a glance.

---

## Guidance

To help an audience find outliers in a scatterplot, use larger and more opaque markers.

## Why

Outliers are typically single, isolated points. If markers are too small or transparent, they lack visual weight and can be easily overlooked or get lost in the visual noise of the chart. Increasing their size and opacity makes them more visually prominent, which improves the speed and accuracy of their detection. This "pop-out" effect allows them to be perceived without a deliberate, slow search.

## When it applies

- When creating any scatterplot where identifying exceptions, anomalies, or errors is a primary analysis task.
- When you want to draw attention to specific data points that deviate from the norm.
- In domains like fraud detection, quality control, or sensor data analysis, where outliers are often the most important points.

## Exceptions

- When the primary goal is to show the **density** or shape of a large, continuous distribution. In this case, large, opaque markers will cause significant overplotting, obscuring the underlying structure. For density tasks, smaller, semi-transparent markers are preferable.
- When the dataset is so large that making every point large and opaque would render the entire plot as an unreadable solid shape. Consider other techniques like data aggregation (e.g., 2D histograms) or sampling in these cases.

## Trade-offs

- **Clarity of Density:** Making outliers prominent via larger, opaque markers inherently hides the fine-grained structure of dense clusters due to overplotting. You are trading the ability to see density for the ability to see outliers.
- **Visualizing Other Variables:** If you are also using size to encode another variable, you cannot arbitrarily make all markers large.

## Evaluate

- [ ] Are the markers in the scatterplot very small (e.g., 1-2 pixels in diameter)?
- [ ] Do the markers have a low opacity (i.e., they are highly transparent)?
- [ ] Is it difficult to spot individual points that are far from the main group without actively scanning the entire chart?

## Repair

1.  **Increase marker opacity.** Start by making the markers fully opaque (100% opacity). This is often the simplest change with the largest impact.
2.  **Increase marker size.** If outliers are still hard to spot, gradually increase the size of all markers until the outliers are clearly visible.
3.  **Use a hybrid approach.** If increasing the size of all markers causes too much overplotting, consider first identifying outliers programmatically and then highlighting them with a distinct color, shape, or larger size, while keeping the "normal" points smaller.