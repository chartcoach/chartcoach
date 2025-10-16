---
id: avoid-pies-and-tables-for-correlation
title: "Avoid pie charts and tables for identifying correlations"

tags:
- impact:perceptual
- impact:performance
- impact:ethical
- chart:pie
- chart:bar
- task:correlation
- data:quantitative
- visual:angle
- visual:area
- audience:general
- medium:static
- access:cognitive-load-risk

evidence:
  strength: medium
  summary: "Saket et al. (2019, n=180) found that for correlation tasks, pie charts and tables were significantly less accurate and slower than line charts, scatterplots, and bar charts (p<0.05). Users also rated them as the least preferred visualizations for this task."

sources:
  - type: research
    ref: Saket et al., 2019
    url: https://doi.org/10.1109/TVCG.2018.2829750
    note: "For correlation tasks, pie charts and tables performed worst in accuracy (p<0.05, η²=0.41), time (p<0.05, η²=0.70), and user preference (p<0.05, η²=0.44)."
    role: primary
  - type: research
    ref: Zeng & Battle, 2023
    url: https://doi.org/10.1145/3544548.3581349
    note: "This review of graphical perception literature confirms through synthesis of empirical studies like Saket et al. that pie charts and tables are not recommended for correlation tasks."
    role: supporting

---

## Guidance

Do not use pie charts or tables when the primary goal is to help a user identify a correlation between variables.

## Why

Pie charts encode values using angles and area, while tables present raw numbers. Neither of these formats is designed for judging relationships across data points. The human visual system cannot easily integrate a series of angles or tabular numbers to perceive a trend or correlation. This leads to poor performance, where users are slower, less accurate, and less confident in their judgments. Using the wrong chart for the task can mislead the audience or cause them to miss important insights.

### Core Principle

A visualization's effectiveness is task-dependent. Visual encodings must be chosen to match the cognitive and perceptual operations required by the user's task. For correlation, the task requires judging a global pattern, which pie charts and tables fail to support.

## When it applies

- When the main question you want to answer is, "Is there a relationship between variable A and variable B?"
- When presenting data to an audience and you want to highlight a correlation.

## Exceptions

- A table may be useful as a *supplement* to a scatterplot, providing a way to look up exact values, but it should not be the primary tool for the correlation task itself.
- There are no known exceptions where a pie chart is an effective tool for showing correlation.

## Trade-offs

- Avoiding these charts for this task has no significant downside. The gain in clarity, accuracy, and speed from using a proper chart (like a scatterplot) far outweighs any perceived familiarity with tables or pie charts.

## Signs of Trouble

- **Visual Chaos:** The visualization (e.g., a series of pie charts) does not present any clear, discernible pattern endometrium the variables.
- **Viewer Frustration:** Users complain that they "can't see the relationship" or have to perform mental math to try and find a trend.
- **Incorrect Takeaways:** The audience draws the wrong conclusion about the relationship between variables or, more likely, concludes there is no relationship because none is visible.
- **Reliance on Reading:** Viewers are forced to read every number in a table and mentally plot the relationship, defeating the purpose of a visualization.

## How to Improve

- **Quick Fix: Convert to a Scatterplot.** The most direct and effective action is to change the visualization to a scatterplot. This is the standard and most effective chart type for showing the relationship between two quantitative variables.

- **Moderate Approach: Use a Line Chart if Ordered.** If the independent variable is ordered (e.g., time), a line chart is an excellent alternative that is also highly effective for correlation tasks.

- **Comprehensive Approach: Re-evaluate the Goal.** If you find yourself trying to show a correlation with a pie chart, it's a sign of a fundamental mismatch between your goal and your tool. Take a step back and ask, "What is the primary message?" If it's about a relationship, choose a chart designed for it. If it's about part-to-whole composition, then a pie or bar chart might be appropriate, but the task is no longer about correlation.