---
id: ensure-color-background-contrast
title: "Constrain palette colors to a mid-range of lightness"

tags:
  - impact:perceptual
  - impact:accessibility
  - visual:color
  - medium:screen
  - medium:print
  - data:categorical

evidence:
  strength: high
  summary: "To ensure visibility on both light and dark backgrounds, colors must fall within a mid-range of lightness. Gramazio et al. (2017) enforce this by constraining generated colors to a CIELAB L* range of 25-85. This practical rule aligns with foundational accessibility principles (e.g., WCAG) that require sufficient contrast for readability on varied backgrounds."

sources:
  - type: research
    ref: Gramazio, Laidlaw, & Schloss, 2017
    url: https://doi.org/10.1109/TVCG.2016.2598918
    note: "The Colorgorical model explicitly excludes colors lighter than L*=85 and darker than L*=25 'so that all colors are visible on black or white backgrounds'."
    role: primary
  - type: standard
    ref: WCAG 2.1 Success Criterion 1.4.3
    url: https://www.w3.org/TR/WCAG21/#contrast-minimum
    note: "While not a direct mapping, the principle of ensuring sufficient contrast between foreground (color marks) and background is a core accessibility requirement. Clamping lightness is a practical heuristic to help meet this goal in varied contexts."
    role: related

tools:
  - type: implement
    name: Colorgorical
    url: http://vrl.cs.brown.edu/color
    description: "Automatically clamps the lightness of generated colors to an L* range of 25-85."
  - type: validate
    name: Color contrast checker
    url: https://webaim.org/resources/contrastchecker/
    description: "Allows you to manually check the contrast ratio of a foreground color against both a white (#FFFFFF) and black (#000000) background."

examples:
  - type: bad
    description: "A palette that includes a very light yellow. On a standard white background, the yellow marks are nearly invisible."
  - type: bad
    description: "A palette that includes a very dark navy blue. When the chart is placed on a slide with a dark gray or black background, the navy blue marks disappear."
  - type: good
    description: "A palette where all colors are of medium lightness, like the 'Set2' or 'Pastel1' schemes from ColorBrewer. These palettes are robust and remain legible on both light and dark backgrounds."
---

## Guidance

When creating a categorical color palette, constrain your color choices to a mid-range of lightness to ensure they are visible on both light and dark backgrounds. Avoid extremely light and extremely dark colors.

## Why

You cannot always control the context in which your visualization will be displayed. A chart designed on a white background might be pasted into a presentation with a dark theme, or vice versa. Colors that are too light (e.g., pale yellow) will be invisible on a white background. Colors that are too dark (e.g., navy blue) will disappear on a black background. By choosing colors in a medium lightness range (e.g., CIELAB L* between 25 and 85), you create a robust palette that remains legible in a wider variety of contexts.

### Core Principle

Design for resilience. Your visualizations should be robust enough to withstand common changes in their viewing environment without losing legibility.

## When it applies

- Always, when creating a general-purpose color palette.
- Especially critical when you know your visualization will be used in multiple contexts (e.g., in a report, on a website, and in a slideshow).
- When creating a style guide or design system for a team, to ensure all generated charts are robust.

## Exceptions

- **Fixed Background:** If you have absolute control over the background color and know it will never change (e.g., a chart on a printed poster with a specified background), you only need to ensure contrast against that one specific color. You could then use very light colors on a dark background, or vice versa.
- **Highlighting:** When using color for highlighting, you might intentionally use a very light color (like yellow) as a background fill behind black text to draw attention. In this case, the color is the background, not the foreground mark.

## Trade-offs

- **Reduced Dynamic Range:** You are intentionally reducing the range of lightness available to you. This can make it slightly harder to create highly distinct colors, as lightness contrast is a powerful tool for discriminability. However, the gain in robustness usually outweighs this cost.

## Signs of Trouble

- **Disappearing Marks:** Some of your chart elements (bars, points, lines) are invisible or very difficult to see against the background.
- **Context-Dependent Failure:** The chart looks fine on your screen, but when a colleague pastes it into their presentation, some of the data disappears.
- **Low Contrast Warnings:** Accessibility-checking tools flag some of your colors for having insufficient contrast against a standard white or black background.

## How to Improve

- **Quick Fix: Manual Lightness Check.** For each color in your palette, check its contrast against both white (#FFFFFF) and black (#000000) using a contrast checking tool. If a color fails against either background (e.g., a ratio below 2:1 for graphical elements), adjust its lightness until it passes.

- **Moderate Approach: Use a Robust Pre-made Palette.** Choose a pre-made qualitative palette that is known to be robust. For example, the `Set2` and `Pastel1` palettes from ColorBrewer are designed with medium lightness and work well on varied backgrounds.

- **Comprehensive Approach: Build Lightness Clamping into Your Process.** When using a color picker, pay attention to the 'Lightness' or 'Brightness' value (e.g., the 'L' in HSL or the 'B' in HSB/HSV). Avoid values that are very high (e.g., >90%) or very low (e.g., <20%). If using a programmatic tool, use one like Colorgorical that automatically clamps the lightness range of its output.
