---
id: show-form-in-the-color-key-not-just-color
title: Encode mark form in the color key when the chart uses different line or area
  styles
bibliography: references.bib
description: Include strokes, dashes, thickness, or shapes in the legend so readers
  can match styled marks quickly.
labels:
- chart:multiple
- task:identify
- visual:color
- impact:clarity
- data:categorical
- audience:novice
- complexity:intermediate
---

## Match legend symbols to both color and form used in the chart <!-- role: advice -->

If your visualization distinguishes categories using line thickness, dashes, outlines, or shapes, show those same forms in the color key rather than relying on color swatches alone.

## Matching symbols speeds recognition of styled marks <!-- role: reason -->

When marks differ by more than color, a color-only legend makes readers do extra inference to locate the right marks. Showing the same symbol style in the key creates a direct visual match between legend and chart.

**Mechanism:** A legend that mirrors mark appearance supports pattern matching instead of interpretation.

**Evidence:** Using form (e.g., dashed/thick lines, rectangles, hatching, strokes) in the key is recommended as an effective way to help readers find the corresponding elements in the visualization [@muth_color_keys_2023].

**Notes:** This is especially helpful when color differences are subtle or when outlines affect how colors appear.

## When form-enhanced legend items matter most <!-- role: context -->

- **User Goal:** Locate the correct marks in the chart quickly.
- **Task:** Match legend items to styled lines/areas/regions.
- **Data:** Categorical series where style encodes category or additional grouping.
- **Chart Setting:** Line charts, locator maps, interval displays, or maps with hatching/strokes.
- **Audience:** Mixed vision capabilities, including readers who benefit from non-color cues.
- **Success Criterion:** Readers can find the corresponding marks without guessing.

## When not to add extra form detail to the legend <!-- role: exceptions -->

**Break it when:** The visualization uses only color (no meaningful differences in stroke, dash, or shape). **Why:** Adding extra symbol styling would imply distinctions that don’t exist [@muth_color_keys_2023].

## Tradeoffs of including form in legends <!-- role: costs -->

**Sacrifice:** Legend items may take more space than simple color chips. **Risk:** Overly complex legend symbols can become miniature illustrations that are hard to parse. **Mitigation:** Mirror only the distinguishing aspects (e.g., dash pattern or outline), not every decorative detail.

## Common failures with legend symbols <!-- role: mistakes -->

**Mistake:** Showing only color swatches for marks that differ by dashed vs solid or thick vs thin lines. **Why it fails:** Readers can’t quickly connect legend to marks because the most visible cue in the chart is missing from the legend [@muth_color_keys_2023].

## Quick checks for symbol matching <!-- role: check -->

**Failure Sign:** Readers can name the category but still struggle to find it on the chart. **Quick Check:** Do legend symbols look like tiny versions of the marks they refer to? **Stronger Test:** Blur the chart slightly; if style remains the dominant cue but the legend ignores it, the legend is incomplete.

## What to do instead if legend symbols become too complex <!-- role: fix -->

- Simplify marks so categories differ by one or two intentional style cues.
- Add direct labels at key points (e.g., line ends) to reduce reliance on the legend.
- Use grouping in the legend so style variants are visually nested under a shared category.
- Remove non-essential styling and keep only the style that encodes meaning.
