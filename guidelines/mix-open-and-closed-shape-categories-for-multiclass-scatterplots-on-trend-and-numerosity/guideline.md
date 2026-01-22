---
id: mix-open-and-closed-shape-categories-for-multiclass-scatterplots-on-trend-and-numerosity
title: Mix open and closed shape categories for multiclass scatterplots when judging
  trends or numerosity
bibliography: references.bib
description: Using shape symbols from different open/closed categories reduces interference
  and improves performance for trend and numerosity judgments in multiclass scatterplots.
labels:
- chart:scatter
- task:correlate
- visual:shape
- impact:accuracy
- data:categorical
- audience:general
- interference:shape-category
---

## Use mixed open/closed shape categories for multiclass scatterplots (trend & numerosity) <!-- role: advice -->

When you encode categories with shape in a multiclass scatterplot and the viewer must judge a trend or compare counts, choose symbols so that categories span both open and closed shape types rather than staying within only open or only closed shapes.

## Open/closed shape categories reduce perceptual interference <!-- role: reason -->

Using two shapes from the same open/closed category makes them more confusable when they appear together, which increases interference and slows or degrades higher-level judgments that require separating classes in a single plot.

**Mechanism:** Separating categories across the open/closed boundary increases distinctiveness between classes, reducing competition during selection and ensemble judgments.

**Evidence:** In high-level scatterplot tasks that require discriminating two symbol classes in one plot, same open/closed-category symbol pairings produced more interference than mixed-category pairings, especially for numerosity and linear relationship (trend) judgments [@burlinsonOpenVsClosed2018]. This rule is captured as actionable visualization-recommendation knowledge in a broader collation of graphical perception evidence for encoding choice [@zengReviewCollationGraphical2023].

**Notes:** The effect is tied to heterogeneous (multi-symbol) displays rather than displays where each plot uses a single symbol type.

## When multiclass symbol separation matters in scatterplots <!-- role: context -->

- **User Goal:** Distinguish multiple classes in one scatterplot while extracting a higher-level pattern from one class.
- **Task:** Correlate (trend judgment) or compare numerosity between classes.
- **Data:** Two or more nominal categories plotted as points; moderate-to-high point density where symbol confusion is plausible.
- **Chart Setting:** A single scatterplot containing multiple symbol types simultaneously (not separated into separate panels).
- **Audience:** Readers who must make quick, correct judgments under visual clutter.
- **Success Criterion:** Faster responses and/or fewer errors when identifying the class with the trend or larger count.

## When not to rely on mixed open/closed categories <!-- role: exceptions -->

**Break it when:** The viewer compares homogeneous displays (e.g., each plot uses only one symbol type, shown side-by-side) instead of separating classes within a single plot. **Why:** Open vs. closed symbol differences did not reliably change response time in the baseline side-by-side (separate-plot) setting.

## Tradeoffs of mixing open and closed symbols <!-- role: costs -->

**Sacrifice:** You reduce freedom to choose any arbitrary set of shapes for stylistic or semantic reasons. **Risk:** If you have many categories, you may still need multiple shapes within the same open/closed group, reintroducing within-group interference. **Mitigation:** None required by default, but be aware that adding more within-group shapes can dilute the benefit.

## Common ways this goes wrong <!-- role: mistakes -->

- **Mistake:** Assigning multiple categories using only open shapes (e.g., plus, asterisk, cross) in the same scatterplot. **Why it fails:** Same-category open shapes create stronger interference when classes must be separated for numerosity or trend judgments.
- **Mistake:** Assigning multiple categories using only closed shapes (e.g., square, triangle, circle) in the same scatterplot. **Why it fails:** Same-category closed shapes can interfere strongly when classes are judged together, particularly when the viewer focuses on a closed-shape target.

## Quick tests for open/closed interference risk <!-- role: check -->

**Failure Sign:** Viewers hesitate or misattribute which class forms the trend or which class has more points. **Quick Check:** Scan the legend: if all category symbols are all open or all closed, the plot is at higher risk of within-category interference. **Stronger Test:** Run a short timed pilot with a trend-identification or “which class has more points” question and compare mixed-category vs same-category symbol assignments.

## What to do instead if you cannot mix categories <!-- role: fix -->

- Use a separate-plot (side-by-side) design where each plot is homogeneous in symbol type rather than mixing classes within one plot.
- Reduce the number of categories shown at once so you do not need many shapes within the same open/closed category.
- Split categories into facets so fewer distinct shapes must be discriminated in any single plotting area.
- Replace within-plot class separation needs with an alternate workflow that avoids requiring the viewer to isolate two shape-defined classes simultaneously.
