---
id: separate-adjacent-marks-and-prevent-overlap-of-primary-elements
title: Separate adjacent marks with at least 1px whitespace and prevent overlap of
  primary chart elements
bibliography: references.bib
description: Ensure chart marks and text are not obscured and that touching segments
  remain visually separable.
labels:
- chart:bar
- chart:pie
- chart:scatter
- task:compare
- task:identify
- visual:space
- visual:layering
- impact:accessibility
- impact:clarity
- data:categorical
- audience:general
- accessibility:perceivable
---

## Maintain separability between marks and text <!-- role: advice -->

Keep primary chart elements visually separable: do not let chart marks or any text be obscured by other elements, and ensure adjacent elements that touch have at least 1px whitespace between them when separability is needed to understand the chart.

## Why distinguishability depends on separability, not only contrast <!-- role: reason -->

When marks or labels overlap, users can no longer reliably separate foreground from background or parse boundaries between adjacent categories. Even if colors are technically high-contrast, occlusion and “touching” shapes reduce discriminability, making it hard to identify elements and interpret the chart accurately.

**Mechanism:** Removing occlusion and adding small gaps restores clear boundaries so viewers can segment elements as distinct units rather than a fused shape.

**Evidence:** Visual presentation should allow users to distinguish foreground from background and separate visual elements so important content remains perceivable, including beyond color and contrast checks [@w3c_understanding_distinguishable]. In visualization accessibility auditing, primary chart elements and text must not be obscured, and adjacent touching elements (e.g., stacked bars, pie slices) should be separated with at least 1px whitespace when separability is required for understanding [@elavskyHowAccessibleMy2022; @observablehq_contrast_and].

**Notes:** This guideline is about separability and occlusion; it complements (but is distinct from) contrast-focused checks.

## When separability is required for understanding <!-- role: context -->

- **User Goal:** Identify and distinguish categories, segments, or individual marks without ambiguity.
- **Task:** Compare adjacent parts (e.g., stacked segments, pie slices) or pick out individual points/marks.
- **Data:** Categorical parts, segmented aggregates, or dense marks where elements can collide or visually fuse.
- **Chart Setting:** Charts with touching segments (stacked bars, pies/donuts) or layered elements (labels over marks, marks over gridlines/annotations).
- **Audience:** Mixed audiences, including people who need strong visual discriminability to parse boundaries.
- **Success Criterion:** No essential mark or label is hidden; adjacent parts remain separable when that separability is needed to interpret the encoding.

## When not to enforce gaps as a hard requirement <!-- role: exceptions -->

**Break it when:** Adjacent elements touching does not affect understanding because separability is not required for the chart’s interpretation. **Why:** This guideline is only a failure condition when discriminability/separability is necessary to understand the chart [@elavskyHowAccessibleMy2022].

## Tradeoffs of adding whitespace and avoiding overlap <!-- role: costs -->

**Sacrifice:** Adding gaps or re-layering can reduce the amount of drawable space for data marks and may slightly change the visual density of the chart. **Risk:** Over-separating can visually fragment grouped parts, making it harder to perceive them as a whole. **Mitigation:** Treat the gap as a minimal separation signal (e.g., the specified 1px whitespace) rather than a strong divider.

## Common ways this fails in charts <!-- role: mistakes -->

- **Mistake:** Letting labels, annotations, or decorative layers overlap data marks. **Why it fails:** Text or primary marks become partially hidden, blocking access to the encoded information [@elavskyHowAccessibleMy2022].
- **Mistake:** Using “touching” stacked segments or pie slices with no whitespace when users must compare boundaries. **Why it fails:** Adjacent elements fuse perceptually and cannot be reliably distinguished [@elavskyHowAccessibleMy2022].
- **Mistake:** Relying on contrast checks alone to claim distinguishability. **Why it fails:** Occlusion and boundary ambiguity can persist even when contrast is sufficient [@w3c_understanding_distinguishable].

## Quick ways to audit separability <!-- role: check -->

**Failure Sign:** Any important mark or any text is partially hidden, or touching segments look like a single merged shape when the viewer must distinguish them. **Quick Check:** Scan for overlaps between marks, labels, and other layers; verify that touching segments have at least 1px whitespace when segment boundaries matter. **Stronger Test:** Inspect close-up at typical viewing size to confirm boundaries remain distinct and no information is obscured [@elavskyHowAccessibleMy2022].

## Practical fixes to restore separability <!-- role: fix -->

- Add at least 1px whitespace between adjacent touching elements when distinguishing boundaries is required to interpret the chart.
- Re-layer or reposition elements so no text (labels, captions inside the chart area, annotations) is obscured or overlapped by other elements.
- Adjust mark placement or spacing to prevent occlusion between primary marks (e.g., reduce overlap in dense mark areas by adding space between marks).
- Remove or move non-essential layers that obscure primary chart elements so the data-encoding marks remain fully visible.
