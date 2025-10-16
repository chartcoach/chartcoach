---
id: use-size-for-extremum-accuracy
title: "Use size to accurately find minimum and maximum values; use grayscale value for speed"

tags:
  - impact:perceptual
  - impact:performance
  - chart:glyphs
  - chart:scatter
  - task:find-extremum
  - task:lookup
  - task:rank
  - data:quantitative
  - data:ordinal
  - visual:size
  - visual:color
  - audience:general
  - medium:static
  - medium:interactive

evidence:
  strength: medium
  summary: "A 2016 crowdsourced study with 87 participants found that encoding data with 'size' led to the highest accuracy for identifying minimum and maximum values in a sequence. Using 'value' (grayscale) resulted in the fastest task completion times."

sources:
  - type: research
    ref: "Chung et al., 2016"
    url: "https://doi.org/10.1111/cgf.12889"
    note: "Experiment 2 tested which visual channel was most effective for min/max value judgments. Size was most accurate (lowest error rate), and value (grayscale) was fastest (lowest response time). Hue and orientation were least accurate."
    role: primary

---
## Guidance
To help users identify minimum or maximum values in a sequence (e.g., finding the biggest/smallest data point), encode the quantitative value using **size** for the best accuracy, or **value** (grayscale intensity) for the fastest performance.

## Why
Humans are highly effective at comparing the sizes of objects to determine extremes, leading to fewer errors. At the same time, judging differences in grayscale value is a very fast pre-attentive task, reducing the time needed to find the target. This guideline optimizes for either accuracy or speed depending on the primary goal of the task.

### Core Principle
The choice of visual channel directly impacts the speed and accuracy of a perceptual task. Channels that are perceptually ordered and quantitative, like size and value, are better suited for tasks involving magnitude judgments than non-ordered channels like hue.

## When it applies
- When designing a series of glyphs or symbols where a quantitative attribute needs to be clearly distinguished.
- When the primary user task is to find the minimum, maximum, or outliers in a set of data points.
- In scatterplots where a third variable is encoded by a visual channel like the size or color of the points.

## Exceptions
- If the dynamic range of the data is very large, using `size` can be problematic: very small items may become invisible, while very large items may occlude others.
- When using `value` (grayscale), the number of distinguishable steps is limited (typically 5-7), so it may not be suitable for data with high cardinality or when subtle differences are important.

## Trade-offs
- Using `size` is highly accurate but can be slower to process than `value`, as it may require more conscious comparison.
- Using `value` (grayscale) is very fast but can be slightly less accurate than `size`.
- Using `shape` (with a countable feature) is surprisingly accurate but is significantly slower than other channels, increasing cognitive load.

## Signs of Trouble
- **High Error Rate:** Users frequently misidentify the minimum or maximum value. This is a common symptom when using channels like color `hue` or `orientation` for this task.
- **Slow Performance:** Users take a long time to complete the task. This often occurs when using cognitively demanding channels like `shape` or when users have to read raw numeric text.
- **User Complaints:** Users express difficulty in telling which item is the largest or smallest.

## How to Improve
- **Quick Fix:** If you are using a poor channel like color `hue`, switch to a sequential color ramp (e.g., from light gray to dark gray, or light blue to dark blue). This changes the encoding from the ineffective `hue` to the more effective `value` (or `saturation`).
- **Moderate Redesign (Prioritizing Accuracy):** Change the primary encoding for the quantitative data to `size`. Ensure the size range is sufficient to make the smallest and largest values clearly distinguishable.
- **Moderate Redesign (Prioritizing Speed):** Change the primary encoding to `value` (grayscale intensity). This is often the fastest way for users to spot the darkest or lightest element in a sequence.
