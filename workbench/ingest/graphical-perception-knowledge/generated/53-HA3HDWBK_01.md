---
id: scatterplot-outlier-detection-tradeoff
title: "For outlier detection in scatterplots, balance the trade-off between speed and accuracy"

tags:
  - impact:perceptual
  - impact:performance
  - chart:scatter
  - task:find-anomalies
  - data:quantitative
  - audience:general
  - medium:screen

evidence:
  strength: medium
  summary: "In a crowdsourced experiment (Micallef et al., 2017, n=119), default scatterplot designs from MATLAB and R were significantly more accurate for outlier detection than a task-optimized algorithm (p<0.01). However, the optimized algorithm was significantly faster (p<0.01)."

sources:
  - type: research
    ref: Micallef et al., 2017
    url: https://doi.org/10.1109/TVCG.2017.2674978
    note: "Experiment 3 (Outlier Detection) found that the author's algorithm (T) was fastest, but less accurate than MATLAB (M) and R presets. Post hoc tests showed M=R > T > S for success rate, and T < M=R < S for completion time (where S is another preset and '<' means faster/less accurate)."
    role: primary

tools:
  - type: implement
    name: R Project
    url: https://www.r-project.org/
    description: "A language and environment for statistical computing whose default scatterplots were found to be highly accurate for outlier detection."
  - type: implement
    name: MATLAB
    url: https://www.mathworks.com/products/matlab.html
    description: "A programming platform whose default scatterplots were also found to be highly accurate for outlier detection."

examples:
  - type: good
    description: "A standard scatterplot from R or MATLAB with default settings (e.g., small, solid-colored points) is a good choice when accuracy in identifying outliers is the top priority."
  - type: bad
    description: "A scatterplot with large, highly transparent markers, while potentially good for showing density, would be a poor choice for outlier detection as individual points would be faint and easily missed."
---

## Guidance

When designing a scatterplot for outlier detection, recognize the trade-off between interpretation speed and accuracy. Default designs from standard statistical packages (like R or MATLAB) tend to be more accurate, while algorithmically optimized designs may be faster to process. Choose the design that aligns with your primary goal.

## Why

The visual characteristics that enable fast visual processing are not always the same as those that enable high accuracy. An algorithm optimized for speed might generate a design that makes the overall task feel faster (e.g., by creating a visually simpler plot), but in doing so, it may de-emphasize individual points, making them harder to correctly identify as outliers. Conversely, standard software defaults often use small, opaque markers that ensure every point is visible, which supports accurate identification but may increase the time needed to visually scan the entire plot.

## When it applies

- When the primary task for a scatterplot is to identify outliers or anomalous data points.
- When choosing between using a default plot from a statistical package and using a specialized or automated visualization design tool.

## Exceptions

- If the dataset is very sparse, the difference between design choices may be negligible, as overplotting is not an issue and most points are inherently distinct.
- If both speed and accuracy are critical, it may be necessary to test multiple designs or use an interactive system that allows the user to toggle between different views.

## Trade-offs

- **Prioritizing Accuracy:** Using a default R or MATLAB plot may lead to higher accuracy in identifying outliers, but it might take the viewer longer to complete the task.
- **Prioritizing Speed:** Using a perceptually optimized algorithm may result in faster task completion times, but with a higher risk of missing some outliers or making errors.

## Signs of Trouble

- **Missed Outliers:** Users fail to spot obvious outliers because the markers are too faint, too large and overlapping, or otherwise obscured.
- **Slow Performance:** Users complain that it takes a long time to scan the chart and confidently determine if there are any outliers.
- **False Positives:** The design creates optical illusions or artifacts that lead users to incorrectly identify normal points as outliers.

## How to Improve

- **For Maximum Accuracy:** Use the default scatterplot function in a standard statistical package like R or MATLAB. These tend to use settings that make each point clearly visible.
- **For Maximum Speed:** Use an automated, perceptually-optimized tool to generate the scatterplot, but be aware of the potential for reduced accuracy and consider it a first-pass analysis.
- **Balanced Approach:** Start with a default plot. If it suffers from overplotting in dense regions, manually decrease marker size or add a small amount of transparency (alpha) until you find a balance where dense regions are manageable but individual points are still clearly visible.
