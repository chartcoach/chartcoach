---
id: use-filled-shapes-for-color-marks
title: "Use filled shapes for better color discrimination in point-based charts"

tags:
  - impact:perceptual
  - chart:scatter
  - visual:color
  - visual:shape

evidence:
  strength: medium
  summary: "In studies of multi-class scatterplots, filled shapes (e.g., ●) have been shown to make color differences more discriminable than unfilled shapes (e.g., ○) or line-based marks (e.g., +). This increases the viewer's ability to distinguish between categories."

sources:
  - type: research
    ref: Zeng & Battle, 2023
    url: https://doi.org/10.1145/3544548.3581349
    note: "Cites Smart & Szafir [92] finding that 'CH [Color Hue] are generally more discriminable with filled shapes than with unfilled ones' (p. 8) and uses this insight to propose an improvement to a Voyager recommendation (p. 12, Figure 5)."
    role: primary
  - type: research
    ref: Smart & Szafir, 2019
    url: https://doi.org/10.1109/TVCG.2019.2934294
    note: "Primary study on multiclass scatterplots that found filled shapes offer better color discriminability than unfilled shapes."
    role: supporting
---

## Guidance

When using color to distinguish between categories in a point-based visualization like a scatterplot, use filled shapes (e.g., solid circles) rather than unfilled outlines or other non-filled marks (e.g., crosses, pluses).

## Why

A larger, solid area of color provides a stronger and clearer signal to the human visual system than a thin outline or a small line-based mark. This makes it easier for viewers to perceive the color and, consequently, to more quickly and accurately distinguish between different colored categories. Using unfilled shapes effectively reduces the amount of colored area for each mark, diminishing the strength of the color encoding.

## When it applies

- In scatterplots with multiple categorical groups distinguished by color.
- In any chart using a legend where colored point markers represent different categories.
- When accessibility is a concern, as a stronger color signal can also aid viewers with some forms of color vision deficiency.

## Exceptions

- **Overplotting:** In a scatterplot with a very high density of points, using semi-transparent, unfilled circles can sometimes help reveal underlying density and structure that would be obscured by solid, opaque marks. However, even here, using semi-transparent *filled* circles is often a better solution.
- **Redundant Encoding:** If you are also using shape to encode a different variable (e.g., circles for 'Group A', squares for 'Group B'), you must use a mix of shapes. Even in this case, using filled versions of all shapes is preferable to unfilled ones.

## Trade-offs

- **Occlusion:** Filled shapes are more likely to occlude (cover up) other marks behind them compared to unfilled shapes, especially in dense plots. This trade-off can be managed with transparency.

## Signs of Trouble

- **"Find the Category" Game:** It's difficult to distinguish the colors of different categories in the plot because the marks are too small or thin (e.g., using a '.' or '+' marker).
- **Muted Colors:** The colors in the plot appear washed out or less vibrant than in the legend because they are only being used for thin outlines.
- **Legend-Chart Mismatch:** The large, solid color swatches in the legend look very different from the small, thin marks in the chart, making the mapping between them more difficult.

## How to Improve

- **Quick Fix: Change Mark Type.** In your plotting software, change the marker type from an open shape (like `'o'` with no fill in some libraries) or a line-based shape (like `'+'` or `'x'`) to a filled shape (like a solid circle). This is usually a one-line code or one-click setting change.
- **Moderate Approach: Increase Mark Size.** In addition to using filled shapes, slightly increasing the size of the marks can further enhance color discriminability. Be careful not to make them so large that they cause excessive overplotting.
- **Comprehensive Approach: Manage Overplotting with Transparency.** If using filled shapes leads to overplotting in dense areas, apply a level of transparency (alpha) to the marks. This preserves the benefit of the filled shape while allowing viewers to see the density of points where they overlap.
