---
id: use-an-easy-to-read-font-style-for-chart-text
title: Use an easy-to-read font style for chart text
bibliography: references.bib
description: Choose familiar, legible typography and avoid shrinking or narrowing
  text just to make it fit.
labels:
- chart:general
- task:read
- visual:text
- impact:accessibility
- data:general
- audience:novice
- complexity:basic
---

## Prefer familiar, legible typography over tight-fitting text <!-- role: advice -->

Use a font and styling that readers are comfortable reading, and avoid overly narrow or tiny text just to squeeze labels into the chart. If text doesn’t fit, remove or relocate it and rely on tooltips or other placements instead.

## Typography sets the baseline readability of the visualization <!-- role: reason -->

If readers struggle to decipher labels and notes, they will spend attention on decoding letters rather than understanding data. Familiar, sufficiently large, high-contrast text reduces friction and makes the visualization feel approachable.

**Mechanism:** Legible fonts and sizes reduce perceptual effort, improving reading speed and willingness to engage.

**Evidence:** Readability improves when chart text uses familiar, easy-to-read typography and when designers avoid shrinking or narrowing text as a primary way to make it fit [@muth_text_in_data_visualizations_2022].

**Notes:** When space is constrained, hiding low-priority text and providing it on demand can be preferable to compressing typography.

## Apply whenever text is part of the primary reading path <!-- role: context -->

- **User Goal:** Read titles, labels, and annotations quickly and accurately.
- **Task:** Decode categories, understand notes, follow explanations.
- **Data:** Any; especially charts with many labels or small screens.
- **Chart Setting:** Web and mobile visuals where font size constraints are common.
- **Audience:** Broad audiences, including readers with mild vision or attention limitations.
- **Success Criterion:** Most text is comfortably readable without zooming.

## When less legible typography might be tolerated <!-- role: exceptions -->

**Break it when:** Decorative typography is itself the message or brand requirement and the chart is not used for precise reading. **Why:** The purpose shifts from efficient decoding to a stylistic or identity goal.

## Trade visual density for readability <!-- role: costs -->

**Sacrifice:** You may show fewer labels or need more space for the chart. **Risk:** Removing text can reduce immediate information density. **Mitigation:** Provide details via tooltips or a note below the chart.

## Common typography mistakes <!-- role: mistakes -->

**Mistake:** Making labels very small or using narrow fonts so everything fits. **Why it fails:** The chart becomes tiring to read and key information gets skipped.

## Quick checks <!-- role: check -->

**Failure Sign:** You feel tempted to zoom in to read labels or annotations. **Quick Check:** View the chart at its expected embed size; if you can’t read the key text comfortably, the typography is too small or cramped. **Stronger Test:** Ask someone to read an annotation aloud without leaning in; difficulty indicates poor legibility.

## Fixes when text is too tight <!-- role: fix -->

- Shorten labels and annotations using simpler wording.
- Hide low-priority labels and reveal them via tooltips.
- Increase the overall chart size where possible or reduce the number of labeled items.
- Move longer text below the chart instead of forcing it into the plotting area.
