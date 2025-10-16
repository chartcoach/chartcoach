---
id: increase-color-distance-for-small-marks
title: "Increase Color Distance for Small Marks"

impact:
  - perceptual
  - accessibility
  - logos
  - ethical
tags:
  - color
  - size
  - shape
  - discriminability
  - scatterplot
  - line-chart
  - bar-chart

sources:
  - type: research
    ref: "Szafir, 2018"
    url: https://doi.org/10.1109/TVCG.2017.2744359
    note: "Establishes that perceived color difference varies with mark size and shape, with smaller marks requiring greater perceptual distance to be discriminable."

tools:
  - type: validate
    name: Viz Palette
    url: https://projects.susielu.com/viz-palette
    description: Checks color palettes for colorblind safety and perceptual distance.
  - type: validate
    name: Adobe Color
    url: https://color.adobe.com/create/color-accessibility
    description: Tools to check and create accessible color themes.
  - type: learn
    name: "Paper: Modeling Color Difference for Visualization Design"
    url: https://doi.org/10.1109/TVCG.2017.2744359
    description: The source research paper detailing experiments on how mark size and shape affect color perception.

examples:
  - type: bad
    description: A scatterplot with many small, circular points uses a palette with light green and light teal. The colors are hard to tell apart, making it difficult to distinguish the two categories.
  - type: good
    description: The same scatterplot uses a high-contrast palette with a distinct orange and blue. The categories are now clearly separable, even for the smallest points.
  - type: good
    description: A bar chart uses a more subtle color palette. Because the marks are large and elongated, the colors are still easily discriminable.
---

## Guidance

Increase the perceptual distance between colors when using them on small or thin marks. The smaller the mark, the more distinct the colors need to be.

## Why

Our ability to tell two colors apart is not absolute; it weakens as the marks displaying those colors get smaller. Colors that look clearly different in a palette picker (which shows large swatches) can become indistinguishable when applied to small points in a scatterplot or thin lines in a line chart.

This happens because there are fewer photoreceptor cells in our eyes being stimulated by the color. When marks are small, the visual system has less information to work with, making it harder to discern subtle differences. This can cause viewers to miss important patterns, group data incorrectly, or misinterpret the chart entirely.

## When it applies

- **Charts with small marks:** This is critical for scatterplots, especially those with many data points, where individual marks (points) are small.
- **Charts with thin marks:** This applies to multi-line charts, parallel coordinate plots, and any visualization where data is encoded in thin lines.
- **Responsive or multi-device design:** When a visualization may be viewed on a small screen (like a mobile phone), all marks effectively become smaller, making color discriminability a key concern.

## Exceptions

- **When marks are consistently large:** If your chart uses large, uniform marks (e.g., countries in a choropleth map, large segments in a treemap, or thick bars in a simple bar chart), you can use more subtle color differences.
- **When color is a redundant channel:** If color is used as a secondary visual cue to reinforce another, stronger channel (like shape or position), and is not the primary way to distinguish categories, slight ambiguity in color may be acceptable.

## Trade-offs

- **Palette size vs. discriminability:** Using highly distinct colors means you can fit fewer of them into a perceptually uniform palette. You might have to reduce the number of categories you can display to ensure they are all distinguishable.
- **Aesthetics vs. clarity:** Aggressively boosting color differences can sometimes lead to palettes that feel overly saturated, harsh, or less aesthetically harmonious. There is a balance between a palette being clear and it being visually pleasing.

## Evaluate

- [ ] When you squint at the visualization, do different color categories blend together?
- [ ] Are there any two colors in the palette that are only subtly different in hue, saturation, or lightness?
- [ ] Was the color palette chosen using large swatches without testing it on the smallest marks that will appear in the final chart?
- [ ] Do a colorblindness simulation tool show that key color distinctions are lost?

## Repair

1.  **Select a more distinct palette.** The quickest fix is to choose colors that are further apart in perceptual color space. For a given set of hues, try increasing the differences in their chroma (saturation) and lightness.
2.  **Increase the mark size.** If possible, make points larger or lines thicker. Even a small increase can significantly improve color discriminability.
3.  **Use elongated marks.** Research shows that color differences are easier to perceive on elongated marks (like bars or lines) than on compact marks (like points) of the same thickness. Consider if a different chart type could serve the same purpose.
4.  **Reduce the number of colors.** If you can't make the colors more distinct, reduce the number of categories. This allows for greater perceptual distance between the remaining colors in your palette.