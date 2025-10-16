---
id: scatterplot-weighted-average-illusion
title: "Account for biased averages in scatterplots with size or color"

impact:
  - perceptual
  - cognitive
  - logos
  - ethical

tags:
  - scatterplot
  - bubble-chart
  - size
  - color
  - lightness
  - bias
  - aggregate
  - correlation
  - perceptual-bias
  - central-tendency

sources:
  - type: research
    ref: Hong, Witt, & Szafir, 2022
    url: https://doi.org/10.1109/TVCG.2021.3114783
    note: "This paper introduces and quantifies the 'Weighted Average Illusion,' where larger and darker marks in a scatterplot systematically bias the viewer's perception of the average position."
  - type: research
    ref: Zeng & Battle, 2023
    url: https://arxiv.org/abs/2109.01271v3
    note: "Provides the methodology for collating graphical perception knowledge, contextualizing the creation of this guideline."

examples:
  - type: bad
    description: "A bubble chart shows a positive correlation, with the largest bubbles in the top-right corner. A viewer is likely to perceive the 'center' of the data as being further to the top-right than it actually is, because the larger, more salient points pull their perception of the average."
  - type: good
    description: "The same bubble chart explicitly marks the true statistical mean with a crosshair or reference lines. This annotation provides a factual anchor, helping viewers overcome the perceptual pull of the larger bubbles and correctly interpret the data's central tendency."
---

## Guidance

When using size (as in a bubble chart) or color lightness to encode a third variable in a scatterplot, be aware that viewers will perceive the average position (the "center" of the data) as being pulled toward the larger or darker points.

## Why

This phenomenon, called the "Weighted Average Illusion," is a perceptual bias. Larger and darker marks are more visually salient, capturing more attention. Our visual system gives these marks more "weight" when summarizing the data at a glance. As a result, the perceived average shifts away from the true statistical mean, which can lead to misinterpretations about the data's central tendency. This effect is stronger for size than for color lightness.

## When it applies

- When using scatterplots that encode a third quantitative variable using **point size (bubble charts)** or a **sequential color scheme (lightness/saturation)**.
- When a primary task for the user is to judge the **central tendency** of the data, find its **average position**, or **compare averages** between different groups.
- The bias is amplified when there is a **correlation** between the point positions and their size/lightness (e.g., points in the top-right quadrant are also the largest or darkest).

## Exceptions

- When the task is to find or compare individual, specific data points, rather than summarizing the group as a whole.
- When the explicit goal is to draw attention to the data points with the highest values in the third dimension (e.g., emphasizing the "most important" items, which are encoded as largest). In this case, the perceptual bias becomes a feature, not a bug.

## Trade-offs

- **Avoiding size/lightness:** You prevent the bias but lose a data-dense channel for showing a third variable. This may require using more space for small multiples or choosing a different, less familiar chart type.
- **Using size/lightness anyway:** You achieve a data-dense chart but risk having your audience misjudge the data's true center. The trade-off is between **data density** and the **perceptual accuracy** of summary statistics.

## Evaluate

- [ ] Does the scatterplot use varying point sizes or a sequential color scheme to encode a third variable?
- [ ] Is there a visible correlation where larger/darker points are clustered in one area of the chart?
- [ ] Is a user expected to make a judgment about the "average," "typical value," or "center" of the data points without an explicit visual guide?

## Repair

1.  **Add Reference Lines:** The simplest and most direct fix. Draw explicit lines or a crosshair on the chart to mark the true statistical X and Y means. This gives viewers a factual anchor to correct their perception.
2.  **Prefer Lightness over Size:** If you must use one of these channels, the biasing effect is weaker for color lightness than for size. Consider using a sequential color palette instead of changing point sizes.
3.  **Use Small Multiples:** If space allows, break the single complex chart into several smaller, simpler scatterplots, faceted by the third variable. This eliminates the visual interference entirely.