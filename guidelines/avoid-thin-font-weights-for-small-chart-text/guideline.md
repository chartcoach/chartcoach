---
id: avoid-thin-font-weights-for-small-chart-text
title: Avoid thin font weights for chart labels unless the text is large and high-contrast
bibliography: references.bib
description: Thin type is fragile at small sizes; use regular/medium weights for readability
  and reserve thin weights for large, high-contrast display text.
labels:
- chart:generic
- task:read
- visual:typography
- impact:accessibility
- data:generic
- audience:general
- scope:font-weight
---

## Keep small chart text out of thin and light weights <!-- role: advice -->

Avoid thin or light font weights for axis labels, ticks, tooltips, and table text; use them only for large text set in high-contrast colors.

## Thin strokes disappear and behave like low-contrast text <!-- role: reason -->

Light weights have delicate strokes that visually fade, especially at small sizes, making them functionally similar to using a lighter color; this reduces legibility and can make key scaffolding text hard to read.

**Mechanism:** Thin strokes are more vulnerable to display resolution, compression, and glare, so letterforms lose distinct features and become harder to distinguish quickly.

**Evidence:** Thin weights are described as “really, really hard to read,” and the guidance restricts them to high-contrast color and large sizes (often titles) [@muth_fonts_2022].

**Notes:** Using thin weights to make text “less important” is not a reliable substitute for good hierarchy choices [@muth_fonts_2022].

## Apply when text is small or must be read quickly <!-- role: context -->

- **User Goal:** Read labels and values without zooming.
- **Task:** Scan axes, legends, tooltips, and tables.
- **Data:** Any, especially dense displays with lots of labeling.
- **Chart Setting:** Mobile screens, projected slides, printed exports, or any small-font layout.
- **Audience:** Broad audiences, including readers with lower vision or poor viewing conditions.
- **Success Criterion:** Text remains legible at the smallest intended viewing size.

## Thin weights are acceptable for large, display-only headings <!-- role: exceptions -->

**Break it when:** The text is large (headline-scale) and set in a strong, high-contrast color, and no precise reading is required. **Why:** Large sizes preserve stroke visibility and reduce the fragility of thin weights [@muth_fonts_2022].

## Heavier weights can feel less “elegant” <!-- role: costs -->

**Sacrifice:** Regular/medium text may feel less airy than a light-weight aesthetic. **Risk:** Overcompensating with very bold weights everywhere can make the design feel shouty. **Mitigation:** Use regular/medium for most text and express hierarchy with selective bolding, size, and spacing [@muth_fonts_2022].

## Don’t use thin fonts to dodge contrast requirements <!-- role: mistakes -->

**Mistake:** Switching to a thin weight to make low-contrast text seem acceptable. **Why it fails:** Thin strokes reduce legibility further and can make important scaffolding text effectively unreadable [@muth_fonts_2022].

## Test at smallest size and worst viewing conditions <!-- role: check -->

**Failure Sign:** Labels look gray, spindly, or break up on export. **Quick Check:** View the visualization at its smallest expected embedding size and check if labels are readable without strain. **Stronger Test:** Print or export to PNG and verify the same text remains crisp and legible on a typical laptop screen and a phone [@muth_fonts_2022].

## Increase weight or contrast rather than thinning strokes <!-- role: fix -->

- Switch thin/light text to regular or medium weight.
- Increase text color contrast instead of reducing stroke thickness.
- Increase font size for any text you insist on keeping in a light weight.
- Reduce label density (fewer ticks/labels) if space pressure is the reason you chose thin type [@muth_fonts_2022].
