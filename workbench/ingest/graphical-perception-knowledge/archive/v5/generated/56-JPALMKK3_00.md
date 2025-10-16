---
id: prefer-pie-over-simple-bar-for-composition
title: "Prefer pie charts over simple stacked bars for part-to-whole estimations"

tags:
  - impact:perceptual
  - impact:logos
  - chart:pie
  - chart:bar
  - chart:bar.stacked
  - task:composition
  - task:lookup
  - task:compare
  - data:quantitative
  - visual:angle
  - visual:length
  - audience:general
  - medium:static
  - medium:screen

evidence:
  strength: medium
  summary: "A 2019 study of part-to-whole estimations (n=316 participants) found that pie charts resulted in significantly more accurate judgments than simple stacked bar charts without a scale. The mean absolute error was ~25% lower for pie charts (p<0.05, based on non-overlapping confidence intervals)."

sources:
  - type: research
    ref: Redmond, 2019
    url: https://doi.org/10.1109/VISUAL.2019.8933718
    note: "Primary study finding that pie charts (mean absolute error 1.77) significantly outperformed baseline stacked bar charts (mean absolute error 2.35) for estimating segment size. The non-overlapping 95% confidence intervals indicate a significant difference."
    role: primary
  - type: research
    ref: Eells, 1926
    url: https://www.jstor.org/stable/2277413
    note: "Early empirical study that also found pie charts could be read as quickly and more accurately than bar charts for part-to-whole tasks, which Redmond's 2019 study corroborates."
    role: supporting
  - type: practitioner
    ref: Tufte, 1983
    note: "Classic text that famously warns against using pie charts, suggesting a table is 'almost always better'. This guideline presents counter-evidence for a specific task."
    role: related
  - type: practitioner
    ref: Few, 2007
    note: "Influential practitioner who argues strongly against pie charts ('Save the Pies for Dessert'), representing the common wisdom this guideline challenges."
    role: related

examples:
  - type: good
    description: "A pie chart with 2-4 distinct slices used to show the breakdown of a total budget. The relative proportions are easy to estimate, especially for values near 25% or 50%."
  - type: bad
    description: "A single stacked bar chart showing the percentage of a goal met (e.g., 65%) without any scale, gridlines, or labels. It's difficult for a viewer to accurately determine if the value is 60%, 65%, or 70%."
---

## Guidance

For part-to-whole comparisons, prefer a pie chart over a simple stacked bar chart that lacks a quantitative scale.

## Why

Pie charts leverage natural perceptual anchors at 0°, 90°, 180°, and 270°, which correspond to 0%, 25%, 50%, and 75%. These built-in reference points make it easier for viewers to estimate proportions accurately. A simple bar representing a proportion only has anchors at its start (0%) and end (100%), making it perceptually harder to judge intermediate values.

### Core Principle

Humans judge quantities more accurately when aided by strong, naturally occurring perceptual anchors.

## When it applies

- When the primary task is for a viewer to estimate the size of a single part relative to the whole (composition).
- When you are choosing between a pie chart and a stacked bar chart *without* a scale or labels.
- When there are a small number of categories (typically 2-5).

## Exceptions

- **Comparing parts to each other:** If the primary task is to compare the parts *to each other* (e.g., "Is Category A bigger than B?"), a standard bar chart where all bars share a common baseline is superior.
- **Precision is critical:** If exact values must be communicated, a bar chart with a scale or a simple table is more accurate than a pie chart.
- **Many slices:** If you have more than 5-7 categories, a pie chart becomes cluttered and difficult to read. A sorted bar chart is a better alternative.

## Trade-offs

- **Reputation:** While perceptually effective for this specific task, pie charts have a poor reputation among many data visualization practitioners. Using one may be perceived as unprofessional or naive by some audiences.
- **Space:** Pie charts can take up more space to convey the same information as a bar chart, especially when legends are required.

## Signs of Trouble

- **Inaccurate estimations:** Users consistently misjudge the proportions shown in your simple stacked bar chart.
- **No reference points:** Your bar chart lacks a scale, gridlines, and data labels, forcing viewers to rely entirely on judging length.

## How to Improve

- **Quick Fix: Add Labels.** If you must use a simple stacked bar, add direct percentage labels to each segment. This bypasses the perceptual estimation task entirely.

- **Moderate Redesign: Switch to a Pie Chart.** If your goal is estimation and you have few categories, replace the simple stacked bar with a pie chart to leverage its natural perceptual anchors.

- **Comprehensive Redesign: Use a Bar Chart with a Scale.** For the highest accuracy, switch to a bar chart and add a full quantitative axis with labeled ticks. This changes the task from estimation to a more precise value lookup.
